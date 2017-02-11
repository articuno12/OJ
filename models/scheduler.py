from gluon.scheduler import Scheduler
scheduler = Scheduler(db2)

LANGUAGES = ["GNU G++ 4.3","GNU GCC 4.3","GNU GCJ"]
LANG_NICK = ["CPP","C","JAVA"]
LANG_EXT  = ["cpp","c","java"]
TIME_FACTOR = [1,1,2]


def eval(*url):
	return os.path.join(request.folder,'eval',*url)

def compile_code(lang,filename):
	outexepath=eval("userexefiles",(filename+".exe"))
	code=os.path.join(request.folder,'uploads',filename)
	if lang == "CPP":
		exit_code = os.system("g++ -O2 --std=c++11 -s -static -o " + outexepath +" "+code)
		if exit_code != 0:
			return "ERROR",""
	elif lang == "C":
		exit_code = os.system("gcc -O3 -s -static -o " + outexepath +" "+code +" -lm")
		if exit_code != 0:
			return "ERROR11",""
	elif lang == "Java":
		exit_code = os.system("gcj --main=Main -o " + outexepath +" "+code)
		if exit_code !=0:
			return "ERROR",""
	return "OK",outexepath

def run_code(pid,lang,filename,exepath):
	score=0
	timeFactor = TIME_FACTOR[LANG_NICK.index(lang)]
	testfileList=db(db.testcases.pid == pid).select()
	tf=0
	mf=0
	for testfile in testfileList:
		try:
			infile = os.path.join(request.folder,'uploads',testfile.in_file)
			outfile = os.path.join(request.folder,'uploads',testfile.out_file)
			useroutput=eval("useroutfiles",(filename+".out"))
			cmd = eval('box.out')+" -a3 -f -m %d -t %d -i %s -o %s %s" % (testfile.memory_limit*1024,testfile.time_limit*timeFactor,infile,useroutput,exepath)
			p = Popen(cmd,shell=True,stdout=PIPE,stderr=STDOUT,close_fds=True)
			p.wait()
			status = p.stdout.read().strip().split('\n')[0]
			print status
			if status.split(' ')[0] == "OK":
				status=status.split(",")
				t=status[0].split(" ")[1]
				t=t.strip("(")
				tf=tf+float(t)
				m=status[2].strip(" ")
				mf=mf+float(m.split(" ")[0])
				cmd = "%s %s %s" % (eval("exact.out"),outfile,useroutput)
				print cmd
				p = Popen(cmd,close_fds=True,shell=True)
				if p.wait()==0:
					score+=testfile.score
				else:
					return "Wrong Answer",score,tf,mf
			else:
				if status.split(' ')[0]=="Caught":
					return "SegFault",score,None,None
				return status,score,None,None
		except:
			return "UnKnown Error",score,None,None
	return "Accepted",score,tf,mf


def check_submission(uid,pid,language,filename):
	# if auth.is_logged_in()==False:
		# return
	score=0
	status,exepath = compile_code(str(language),str(filename))
	if status == "OK" :
		status,score,time,memory = run_code(pid,language,filename,exepath)
		print str(time)+"  "+str(memory)+" MB"
	else:
		score = 0
		status = "Compile Error"
		time,memory=None,None
	print status

	problemquery=db(db.problems.id==pid)
	problemrecord=problemquery.select()  # problem record
	if status=="Accepted":
		newprobsubm=problemrecord[0].submissions+1
		newprobaccu=((problemrecord[0].submissions*problemrecord[0].accuracy)+1)/newprobsubm
		problemquery.update(submissions=newprobsubm,accuracy=newprobaccu)  # updating problem stats
	else:
		newprobaccu=((problemrecord[0].submissions*problemrecord[0].accuracy))/(problemrecord[0].submissions+1)
		problemquery.update(accuracy=newprobaccu)  # updating problem stats

	problemrecord=db.problems[pid]
	if problemrecord.contest_id.start_time + datetime.timedelta(hours=problemrecord.contest_id.duration) < datetime.datetime.now():
		print "contest ended"
	else:
		userquery=db((db.leaderboard.uid==uid) & (db.leaderboard.conid==problemrecord.contest_id) )
		userrecord=userquery.select()   # user records from leaderboard
		if(len(userrecord)==0):
			db.leaderboard.insert(conid=db.problems[pid].contest_id,uid=uid,score=score)
		else:
			alreadysubmitted=db((db.livesubm.pid==pid) & (db.livesubm.uid==uid)).select(orderby=~db.livesubm.score)
			if len(alreadysubmitted)>0:
				if score>alreadysubmitted[0].score:
					updatedscore=score+userrecord[0].score-alreadysubmitted[0].score
					userquery.update(score=updatedscore)
			else:
				updatedscore=score+userrecord[0].score
				userquery.update(score=updatedscore)

	db.livesubm.insert(sid=W2P_TASK.id,stime=datetime.datetime.now(),pid=pid,uid=uid,lang=str(language),status=str(status),score=score,time=str(time),memory=str(memory))

	db.commit()
	return dict(score=score,status=status)
