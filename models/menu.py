# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('OJ'),
                  _class="navbar-brand",_href=URL('default','index'),
                  _id="web2py-logo")
response.title = "OJ"
response.subtitle = 'Learn Competitive programming'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Sourav Goyal'
response.meta.description = 'Online Judge for Competitive Programming'
response.meta.keywords = 'C,C++,Java,Competitive,Programming,OJ'

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]
# DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    # response.menu+=[
    # ('Practice',False,URL('problemset','problemset',[
    # ('Easy',False,URL('problemset','problemset')),
    # ]))
    # ]
    response.menu+=[

          (T('Practice'), False, URL('problemset', 'problemset'), [
              (T('Easy'), False, URL('problemset', 'problemset',vars=dict(difficulty='easy'))),
              (T('Medium'), False, URL('problemset', 'problemset',vars=dict(difficulty='medium'))),
              (T('Hard'), False, URL('problemset', 'problemset',vars=dict(difficulty='hard'))),
              ]),
        (T('Compete'),False,URL('contest','all')),
        (T('Discuss'),False,URL('discuss','discuss_main')),
        (T('Blog'),False,URL('blog','blog_main')),

        ]

    if auth.is_logged_in():
        response.menu+=[
        (T('Admin'),False,URL(),[
        (T('My Contests'),False,URL('admin','user_contests')),
        (T('New Contest'),False,URL('admin','new_contest'))
        ]),
        ]

_()

if "auth" in locals(): auth.wikimenu()
