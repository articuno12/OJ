import os
import json
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if auth.is_logged_in():
        rproblems=yousuck()
    else:
        rproblems={'rpl':[],'rpl2':[]}


    recentques=db(db.post_question.id>0).select(orderby=db.post_question.pub_date,limitby=(0,5))
    upcoming=db(db.contests.start_time>datetime.datetime.now()).select(orderby=db.contests.start_time,limitby=(0,5))
    return dict(rproblems=rproblems,recentques=recentques,upcoming=upcoming)


def user():
    return dict(form=auth())


@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()

def problem_upload():
    form=SQLFORM(db.problems)
    form.process()
    return dict(form=form)

@auth.requires_login()
def submit() :
    pid=request.args[0]
    form=SQLFORM.factory(
        Field('language',requires=IS_IN_SET(['C', 'CPP', 'Java'])),
        Field('Upload_code','upload',uploadfolder=os.path.join(request.folder,'uploads'))
    )
    if form.process().accepted:
        # sid=db.livesubm.insert(uid=auth.user_id,pid=pid,lang=str(form.vars.language),status="Queued",filename=form.vars.Upload_code)
        sid = scheduler.queue_task('check_submission', pvars={'uid':auth.user_id, 'pid':pid,'language':form.vars.language,'filename':form.vars.Upload_code},immediate=True).id
        redirect(URL('default',status,args=sid))

    elif form.errors:
        response.flash = 'form has errors'
    return dict(form=form)

def status():
    sid=request.args[0]
    # aa=db.livesubm.insert(pid=1,uid=1,lang="fdas",status="11",score=10,time="fda",memory="Fdas")# record=db.livesubm[aa]
    return locals()

def statusajax():
    sub_id=request.vars['sid']
    schd_stat=scheduler.task_status(int(sub_id),output=True)
    result={}
    if schd_stat.scheduler_task.status == "COMPLETED":
        result['status']='DONE'
        info=db(db.livesubm.sid==sub_id).select()
        if(len(info)==1):
            result['result']=info[0].status
            if(info[0].time != None):
                result['time']=info[0].time
            if(info[0].memory!=None):
                result['memory']=info[0].memory

    elif schd_stat.scheduler_task.status == "FAILED":
        result['status']='FAILED'
    else:
        result['status']="RUNNING"
    return json.dumps(result)

def problem():
    pid=request.args[0]
    problem=db.problems(pid)
    if problem.contest_id.start_time>datetime.datetime.now():
        redirect(URL('admin','login_error'))

    form=SQLFORM.factory(
        Field('language',requires=IS_IN_SET(['C', 'CPP', 'Java'])),
        Field('Upload_code','upload',uploadfolder=os.path.join(request.folder,'uploads')),
        # formstyle="bootstrap3_stacked"
    )
    if form.process().accepted:
        # sid=db.livesubm.insert(uid=auth.user_id,pid=pid,lang=str(form.vars.language),status="Queued",filename=form.vars.Upload_code)
        sid = scheduler.queue_task('check_submission', pvars={'uid':auth.user_id, 'pid':pid,'language':form.vars.language,'filename':form.vars.Upload_code},immediate=True).id
        redirect(URL('default',status,args=sid))

    elif form.errors:
        response.flash = 'form has errors'

    if problem.contest_id.start_time+datetime.timedelta(hours=problem.contest_id.duration)<datetime.datetime.now():
    # if 1==1:
        archive=True
    else:
        archive=False
    return dict(archive=archive,problems=problem,form=form)
