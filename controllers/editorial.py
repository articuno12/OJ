def editorial_home() :
    auth_user=db(db.auth_user.id > 0).select()
    contests=db(db.contests.id > 0).select()
    return dict(auth_user=auth_user,contests=contests)
def contest_editorial() :
    cid=request.args(0,cast=int)
    editorial=db(db.editorial.id > 0).select()
    auth_user=db(db.auth_user.id > 0).select()
    problems=db(db.problems.id > 0).select()
    return dict(cid=cid,editorial=editorial,auth_user=auth_user,problems=problems)

def ind_editorial() :
    ed=request.args(0,cast=int)
    editorial=db(db.editorial.id > 0).select()
    auth_user=db(db.auth_user.id > 0).select()
    problems=db(db.problems.id > 0).select()
    req = db(db.editorial.id == ed).select() #req is required row of the editorial
    reqprob=db(db.problems.id == req[0].pid).select()
    con=db(db.contests.id == reqprob[0].contest_id).select()
    image=db(db.problem_image.pid == reqprob[0].id).select()
    #comments and likes
    editorial=db.editorial(request.args[0]) or redirect(URL('error'))

    pido=request.args[0]
    like = db(db.likes_e.page_id == pido).select()
    no_likes = len(like)
    if request.vars.page is not None and len(request.vars.page): page=int(request.vars.page)
    else: page=0
    items_per_page=9
    limitby=(page*items_per_page,(page+1)*items_per_page+1)
    comment=db(db.comments_e.problem_id==pido).select(orderby=~(db.comments_e.number_likes),limitby=limitby)
    if request.vars.comment_text :
        form=db.comments_e.validate_and_insert(problem_id=pido,comment_text=request.vars['comment_text'])
        if form.errors :
            session.flash="Comment not posted, please comment again"
        redirect(URL('ind_editorial',args=[pido],vars=dict(page=page)))

    """if editorial.problem_id :
        problem=db(db.problems.name==post_question.problem_id).select()
        return dict(post_question=post_question,likes=no_likes,comment=comment,page=page,items_per_page=items_per_page,problem=problem)
    else:
        return dict(post_question=post_question,likes=no_likes,comment=comment,page=page,items_per_page=items_per_page,problem=None)
"""
    return dict(image=image,ed=ed,editorial=editorial,auth_user=auth_user,problems=problems,req=req,reqprob=reqprob,con=con,likes=no_likes,comment=comment,page=page,items_per_page=items_per_page)

@auth.requires_login()
def addeditorial():
    if request.vars:
        form=db.editorial.insert(author=auth.user_id,pid=request.args[0],solution=request.vars.solution,number_likes=0)
        redirect(URL('editorial','editorial_home'))
    return dict()
