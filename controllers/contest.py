@auth.requires_login()
def add():
    db.contests.author.default=auth.user_id
    form=SQLFORM(db.contests,formstyle="bootstrap3_stacked")
    if form.process().accepted:
        redirect(URL('contest','view',args=form.vars.id))
    return dict(form=form)

def all():
    presentcontests=[]
    pastcontests=[]
    futurecontests=[]
    c=db(db.contests.id>0).select()
    for cs in c:
        if (cs.start_time > request.now):
            futurecontests.append(cs)
        elif ((cs.start_time + datetime.timedelta(hours=cs.duration)) < request.now):
            pastcontests.append(cs)
        elif((cs.start_time <= request.now) & ((cs.start_time + datetime.timedelta(hours=cs.duration)) >=request.now)):
            presentcontests.append(cs)
    return dict(pastcontests=pastcontests , presentcontests=presentcontests , futurecontests=futurecontests)


def view():
    conid=request.args[0]
    contest=db.contests[conid]
    start=contest.start_time
    end=contest.start_time + datetime.timedelta(hours=contest.duration)
    if start > datetime.datetime.now():
        status = "Future"
        timerem=start-datetime.datetime.now()
    elif end < datetime.datetime.now():
        status="Past"
        timerem=None
    else:
        status="Live"
        timerem=end-datetime.datetime.now()
    problems=db(db.problems.contest_id==conid).select(db.problems.id,db.problems.name,db.problems.submissions,db.problems.accuracy)

    for problem in problems:
        if auth.is_logged_in():
            submitted=db((db.livesubm.uid==auth.user_id) & (db.livesubm.pid == problem.id)).count()
            if submitted==0:
                problem.status=0  #DIDN'T TRY
            elif db((db.livesubm.uid==auth.user_id) & (db.livesubm.pid== problem.id) & (db.livesubm.status=="Accepted")).count()>0:
                problem.status=3 #ACCEPTED
            elif db((db.livesubm.uid==auth.user_id) & (db.livesubm.pid== problem.id) & (db.livesubm.score>0)).count()>0:
                problem.status=2   #PARTIAL MARKS
            else:
                problem.status=1 #WRONG SUB

    # suc=db(db.scheduler_task.vars['pid']==problems[0].id).select()
    return dict(contest=contest,status=status,end=end,problems=problems,timerem=timerem,suc=0)

def allsubmissions():
    conid=request.args(0)
    contest=db.contests[conid]
    s=db(db.problems.contest_id == conid).select(join=db.livesubm.on((db.problems.id==db.livesubm.pid)))
    response.view="contest/allsubm.html"
    return dict(role="all",submissions=s,contest=contest)

def successful_selections():
    s=db((db.livesubm.status=="Accepted") & (db.livesubm.pid==request.args(0))).select(orderby=~db.livesubm.sid)
    return dict(submissions=s)

def submissions():
    uid=request.args(1) or "my"
    if uid=="my":
        uid=auth.user_id
    conid=request.args(0)
    contest=db.contests[conid]
    s=db(db.problems.contest_id == conid).select(join=db.livesubm.on((db.problems.id==db.livesubm.pid) & (db.livesubm.uid==uid)))
    # response.view="generic.html"
    response.view="contest/allsubm.html"
    return dict (role="user",uid=uid,submissions=s,contest=contest)

def leaderboard():
    conid=request.args(0)
    leaderboard=db(db.leaderboard.conid==conid).select(orderby=~db.leaderboard.score)
    # response.view="generic.html"
    return dict(conid=conid,leaderboard=leaderboard)

def problemsubm():
    pid=request.args(0)
    submissions=db((db.livesubm.pid==pid)&(db.livesubm.status=="Accepted")).select()
    response.view="contest/sucsubm.html"
    return dict(pid=pid,submissions=submissions)
