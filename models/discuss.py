# -*- coding: utf-8 -*-
db.define_table('post_question',
               Field('title','string',requires=IS_NOT_EMPTY()),
               #Fiedescription','text',requires=IS_NOT_EMPTY()),
                Field('description',requires=IS_NOT_EMPTY(), type='text', length=1000, notnull=True,
    represent=lambda text, row: XML(text.replace('\n', '<br />'),
        sanitize=True, permitted_tags=['br/'])),
               Field('user_id','reference auth_user',default=auth.user_id,writable=False,readable=False),
               Field('problem_id','string',requires=IS_IN_DB(db,db.problems.name)),
               Field('pub_date', 'datetime', default=request.now, writable=False),
               Field('number_likes','integer',default=0),
               Field('number_unlikes','integer',default=0),
               Field('views','integer',default=0)
                )
db.define_table('likes',
                Field('created_by','reference auth_user'),
                Field('page_id','reference post_question'))

db.define_table('comments',
                Field('problem_id','integer',requires=IS_NOT_EMPTY()),
                Field('comment_text','text',requires=IS_NOT_EMPTY()),
                Field('number_likes','integer',default=0),
                )

db.define_table('likes_comment',
                Field('created_by','reference auth_user'),
                Field('page_id','reference comments'))
