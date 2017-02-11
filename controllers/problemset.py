import os
from datetime import date, timedelta
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    return dict(message=T('Welcome to web2py!'))


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

def submit() :
    pid=request.args[0]
    form=SQLFORM.factory(
        Field('language',requires=IS_IN_SET(['C', 'CPP', 'Java'])),
        Field('Upload_code','upload',uploadfolder=os.path.join(request.folder,'uploads'))
    )
    if form.process().accepted:
        sid = scheduler.queue_task('check_submission', pvars={'sid':auth.user_id, 'pid':pid,'language':form.vars.language,'filename':form.vars.Upload_code},immediate=True).id
        redirect(URL('default',status,args=sid))

    elif form.errors:
        response.flash = 'form has errors'
    return dict(form=form)

def status():
    sid=request.args[0]
    return locals()

def statusajax():
    sub_id=request.args[0]
    schd_stat=scheduler.task_status(int(sub_id),output=True)
    if schd_stat.scheduler_task.status == "COMPLETED":
        return schd_stat.result['status'],str(schd_stat.result['score'])
    elif schd_stat.scheduler_task.status == "QUEUED":
        return "RUNNING",str(0)
    else:
        return "ERROR",str(0)

def problemset():
    if len(request.args)>0: page=int(request.args[0])
    else: page=0
    items_per_page=20
    limitby=(page*items_per_page,(page+1)*items_per_page+1)

    levelinp=request.vars['difficulty'] or 'easy'
    orderby=request.vars['orderby'] or '1'

    levelmap={'easy':'Easy','medium':'Medium','hard':'Hard'}
    level=levelmap[levelinp]

    if orderby=='1':
        allproblems=db(db.problems.level==level).select(orderby=(~db.problems.submissions|~db.problems.accuracy),limitby=limitby)
    elif orderby=='2':
        allproblems=db(db.problems.level==level).select(orderby=(db.problems.submissions|db.problems.accuracy),limitby=limitby)
    elif orderby=='3':
        allproblems=db(db.problems.level==level).select(orderby=(~db.problems.accuracy|~db.problems.submissions),limitby=limitby)
    else:
        allproblems=db(db.problems.id>0).select(orderby=(db.problems.accuracy|db.problems.submissions),limitby=limitby)

    result=[]
    for p in allproblems:
        if (p.contest_id.start_time + datetime.timedelta(hours=p.contest_id.duration) < request.now):
            result.append(p)

    # return dict()
    return dict(problems=result,page=page,items_per_page=items_per_page,difficulty=levelinp,orderby=orderby)
