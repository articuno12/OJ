import os
import datetime
import threading
from subprocess import *
db =DAL('sqlite://storage.sqlite')
db2 =DAL('sqlite://scheduler.sqlite')

from gluon.tools import *
auth = Auth(db)
auth.define_tables(username=True,signature=False)
auth.settings.formstyle="bootstrap3_stacked"

db.define_table('contests',
                Field('author','reference auth_user',readable=False,writable=False),
                Field('Contest_Name','string'),
                Field('start_time','datetime'),
                Field('duration','integer'),
                Field('Details','text')
                )
db.define_table('problems',
                Field('contest_id','reference contests'),
                Field('name','string'),
                Field('statement','text'),
                Field('sample_input','text'),
                Field('sample_output','text'),
                Field('think','integer'),
                Field('code','integer'),
                Field('level','string'),
                Field('dp','boolean'),
                Field('graph','boolean'),
                Field('computational_geometry','boolean'),
                Field('greedy','boolean'),
                Field('search','boolean'),
                Field('network_flow','boolean'),
                Field('maths','boolean'),
                Field('heuristic','boolean'),
                Field('string','boolean'),
                Field('adhoc','boolean'),
                Field('ds','boolean'),
                Field('submissions','integer'),
                Field('accuracy','double')
                )
db.define_table('testcases',
                Field('pid','reference problems'),
                Field('score','integer'),
                Field('in_file','upload'),
                Field('out_file','upload'),
                Field('time_limit','integer'),
                Field('memory_limit','integer')
                )

db.define_table('livesubm',
                Field('sid','integer'),
                Field('stime','datetime'),
                Field('pid','reference problems'),
                Field('uid','reference auth_user'),
                Field('lang','string'),
                Field('status','string'),
                Field('score','integer'),
                Field('time','string'),
                Field('memory','string')
)
db.define_table('archsubm',
                Field('sid','integer'),
                Field('stime','datetime'),
                Field('pid','reference problems'),
                Field('uid','reference auth_user'),
                Field('lang','string'),
                Field('status','string'),
                Field('score','integer'),
                Field('time','string'),
                Field('memory','string')
)
db.define_table('problem_image',
                Field('pid','reference problems'),
                Field('file','upload')
                )

db.define_table('leaderboard',
                Field('conid','reference contests'),
                Field('uid','reference auth_user'),
                Field('score','integer')
                )

db.define_table('editorial',
                Field('author','reference auth_user',readable=False,writable=False),
                Field('pid','reference problems',readable=False,writable=False),
                Field('solution', type='text', length=1000),
                Field('number_likes','integer',default=0)
               )

db.define_table('likes_e',
                Field('created_by','reference auth_user'),
                Field('page_id','reference editorial'))

db.define_table('comments_e',
                Field('problem_id','integer',requires=IS_NOT_EMPTY()),
                Field('comment_text','text',requires=IS_NOT_EMPTY()),
                Field('number_likes','integer',default=0),
                )

db.define_table('likes_comment_e',
                Field('created_by','reference auth_user'),
                Field('page_id','reference comments_e'))

db.contests.Contest_Name.requires=IS_NOT_EMPTY()
db.problems.name.requires=IS_NOT_EMPTY()
db.problems.statement.requires=IS_NOT_EMPTY()
db.problems.sample_output.requires=IS_NOT_EMPTY()
db.problems.sample_input.requires=IS_NOT_EMPTY()
