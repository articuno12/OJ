# -*- coding: utf-8 -*-
def blog_main():
    if len(request.args): page=int(request.args[0])
    else: page=0
    items_per_page=9
    limitby=(page*items_per_page,(page+1)*items_per_page+1)
    order=request.vars.order
    if(order==1):
        rows=db(db.post_blog).select(orderby=(db.post_blog.pub_date),limitby=limitby)
    else:
        rows=db(db.post_blog).select(orderby=~(db.post_blog.number_likes),limitby=limitby)
##    rows_viewed=db(db.post_question).select(orderby=~(db.post_question.number_likes - db.post_question.number_unlikes),limitby=limitby)
    return dict(rows=rows,page=page,items_per_page=items_per_page)


def blog_show():
    post_blog=db.post_blog(request.vars.pi) or redirect(URL('error'))
    v=post_blog.views
    if(v==None) :
        v=0
    else:
        v=v+1

    db(db.post_blog.id==request.vars.pi).update(views=v)

    pido=request.vars.pi
    like = db(db.likes_blog.page_id == pido).select()
    no_likes = len(like)
    if request.vars.page is not None and len(request.vars.page): page=int(request.vars.page)
    else: page=0
    items_per_page=9
    limitby=(page*items_per_page,(page+1)*items_per_page+1)
    comment=db(db.comments_blog.problem_id==pido).select(orderby=~(db.comments_blog.number_likes),limitby=limitby)
    if request.vars.comment_text :

        form=db.comments_blog.validate_and_insert(problem_id=pido,comment_text=request.vars['comment_text'])
        if form.errors :
            session.flash="Comment not posted, please comment again"
        redirect(URL('blog_show',vars=dict(pi=pido,page=page)))

    return dict(post_blog=post_blog,likes=no_likes,comment=comment,page=page,items_per_page=items_per_page)

def post_blog():
    if request.vars:
        form=db.post_blog.insert(title=request.vars.title,description=request.vars.description)
        if form.accepted:
            redirect(URL('blog','blog_main'))
    return dict()

"""@auth.requires_login()
def add_like() :
    this_page = db.comments_blog[request.vars.ids]
    already_likedd=(db.likes_comment_blog.created_by == auth.user.id) & (db.likes_comment_blog.page_id == this_page.id )
    if db(already_likedd).delete():
        response.flash = "Unliked"
    else:
        ret = db.likes_comment_blog.validate_and_insert(created_by=auth.user.id,page_id=this_page.id)
        response.flash = "Liked"
    like = db(db.likes_comment_blog.page_id == this_page.id).select()
    return str(len(like))

@auth.requires_login()
def add_likep() :
    this_page = db.post_blog[request.vars.idss]
    already_liked=(db.likes_blog.created_by == auth.user.id) & (db.likes_blog.page_id == this_page.id )
    if db(already_liked).delete():
        response.flash = "Unliked"
    else:
        ret = db.likes_blog.validate_and_insert(created_by=auth.user.id,page_id=this_page.id)
        response.flash = "Liked"
    like = db(db.likes_blog.page_id == this_page.id).select()
    return str(len(like))
"""

@auth.requires_login()
def add_like() :
    this_page = db.comments_blog[request.vars.ids]
    already_likedd=(db.likes_comment_blog.created_by == auth.user.id) & (db.likes_comment_blog.page_id == this_page.id )
    if db(already_likedd).delete():
        response.flash = "Unliked"
    else:
        ret = db.likes_comment_blog.validate_and_insert(created_by=auth.user.id,page_id=this_page.id)
        response.flash = "Liked"
    like = db(db.likes_comment_blog.page_id == this_page.id).select()
    return str(len(like))

@auth.requires_login()
def add_likep() :
    this_page = db.post_blog[request.vars.idss]
    already_liked=(db.likes_blog.created_by == auth.user.id) & (db.likes_blog.page_id == this_page.id )
    if db(already_liked).delete():
        response.flash = "Unliked"
    else:
        ret = db.likes_blog.validate_and_insert(created_by=auth.user.id,page_id=this_page.id)
        response.flash = "Liked"
    like = db(db.likes_blog.page_id == this_page.id).select()
    return str(len(like))
