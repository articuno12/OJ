# -*- coding: utf-8 -*-

def discuss_main():
    if len(request.args): page=int(request.args[0])
    else:
        page=0
    items_per_page=10
    limitby=(page*items_per_page,(page+1)*items_per_page+1)

##    if show_recent==1:
    order=request.vars.order
    if(order==1):
        rows=db(db.post_question).select(orderby=(db.post_question.pub_date),limitby=limitby)
    else:
        rows=db(db.post_question).select(orderby=~(db.post_question.number_likes),limitby=limitby)
##    rows_viewed=db(db.post_question).select(orderby=~(db.post_question.number_likes - db.post_question.number_unlikes),limitby=limitby)
    return dict(rows=rows,page=page,items_per_page=items_per_page)



def discuss_show():
    post_question=db.post_question(request.vars.pid) or redirect(URL('error'))

    v=post_question.views
    v+=1
    print v
    db(db.post_question.id==request.vars.pid).update(views=v)

    pido=request.vars.pid
    like = db(db.likes.page_id == pido).select()
    no_likes = len(like)
    if request.vars.page is not None and len(request.vars.page): page=int(request.vars.page)
    else: page=0
    items_per_page=9
    limitby=(page*items_per_page,(page+1)*items_per_page+1)
    comment=db(db.comments.problem_id==pido).select(orderby=~(db.comments.number_likes),limitby=limitby)
    """t=db.comments
    rec = t(request.args(0))
    t.number_likes.readable = t.number_likes.writable = False
    t.number_unlikes.readable = t.number_unlikes.writable = False
    t.problem_id.readable = t.problem_id.writable = False
    form=SQLFORM(t,rec).process()"""
    if request.vars.comment_text :
        # print "its fine"
        # print request.vars

        form=db.comments.validate_and_insert(problem_id=pido,comment_text=request.vars['comment_text'])
        # print form.id
        if form.errors :
            session.flash="Comment not posted, please comment again"
        redirect(URL('discuss_show',vars=dict(pid=pido,page=page)))

    """form=SQLFORM(db.comments).process()"""
    if post_question.problem_id :
        problem=db(db.problems.name==post_question.problem_id).select()
        return dict(post_question=post_question,likes=no_likes,comment=comment,page=page,items_per_page=items_per_page,problem=problem)
    else:
        return dict(post_question=post_question,likes=no_likes,comment=comment,page=page,items_per_page=items_per_page,problem=None)

@auth.requires_login()
def ask_question():
    if request.vars:
        if request.vars.problem:
            problem=request.vars.problem
            row=db(db.problems.name==problem).select()
            if len(row)==0:
                response.flash="This problem is not in database"
                return dict()
            form=db.post_question.insert(title=request.vars.title,description=request.vars.description,problem_id=row[0].name)
        else:
            form=db.post_question.insert(title=request.vars.title,description=request.vars.description)
        redirect(URL('discuss','discuss_main',vars=dict(order=1)))
    return dict()

@auth.requires_login()
def add_like() :
    this_page = db.comments[request.vars.ids]
    already_likedd=(db.likes_comment.created_by == auth.user.id) & (db.likes_comment.page_id == this_page.id )
    if db(already_likedd).delete():
        response.flash = "Unliked"
    else:
        ret = db.likes_comment.validate_and_insert(created_by=auth.user.id,page_id=this_page.id)
        response.flash = "Liked"
    like = db(db.likes_comment.page_id == this_page.id).select()
    return str(len(like))

@auth.requires_login()
def add_likep() :
    this_page = db.post_question[request.vars.idss]
    already_liked=(db.likes.created_by == auth.user.id) & (db.likes.page_id == this_page.id )
    if db(already_liked).delete():
        this_page.update_record(number_likes=this_page.number_likes-1)
        response.flash = "Unliked"
    else:
        ret = db.likes.validate_and_insert(created_by=auth.user.id,page_id=this_page.id)
        this_page.update_record(number_likes=this_page.number_likes+1)
        response.flash = "Liked"
    like = db(db.likes.page_id == this_page.id).select()
    return str(len(like))

def problem_input():
    return dict()

def problem_selector():
    if not request.vars.problem:
        return ''
    pattern = request.vars.problem.capitalize() + '%'
    selected = [row.name for row in db(db.problems.name.like(pattern)).select()]
    return ''.join([DIV(k,
                 _onclick="jQuery('#problem').val('%s')" % k,
                 _onmouseover="this.style.backgroundColor='yellow'",
                 _onmouseout="this.style.backgroundColor='white'"
                 ).xml() for k in selected])
