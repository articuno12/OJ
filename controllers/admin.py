# submitted by aakash
def add_problem() : ##bandaria pass the contest id as argument
    contest=db.contests(request.args(0,cast=int))
    if not auth.is_logged_in() :
        redirect(URL('admin','login_error'))
    if contest.author != auth.user_id :
        redirect(URL('admin','login_error'))

    db.problems.submissions.default=0
    db.problems.accuracy.default=0.00
    if request.vars :
        # print "its fine"
        form=db.problems.validate_and_insert(contest_id=contest.id,name=request.vars['name'],statement=request.vars['statement'],
                                        sample_input=request.vars['sample_input'],sample_output=request.vars['sample_output'],
                                        think=request.vars['think'],code=request.vars['code'],level=request.vars['level'],dp=request.vars['dp'],
                                        graph=request.vars['graph'],
                                        computational_geometry=request.vars['computational_geometry'],
                                        greedy=request.vars['greedy'],
                                        search=request.vars['search'],
                                        network_flow=request.vars['network_flow'],
                                        heuristic=request.vars['heuristic'],
                                        maths=request.vars['maths'],
                                        string=request.vars['string'],
                                        adhoc=request.vars['adhoc'],
                                        ds=request.vars['ds']
                                        )
        if form.errors :
            session.flash="Form not filled right.!! Plz try again "
            redirect(URL('add_problem'))
        # print "its fine 2"
        image_index=1
        image_subname='uploadimage'
        image_name='uploadimage0'
        # print str(request.vars[image_name])
        while request.vars[image_name]!=None:
            print image_name
            if request.vars[image_name] == '' :
                image_name = image_subname + str(image_index)
                image_index += 1
                continue
            form2=db.problem_image.validate_and_insert(pid=form.id,file=request.vars[image_name])
            image_name = image_subname + str(image_index)
            image_index += 1
        redirect(URL('add_testcase',args=form.id))
    return dict()


def add_testcase():
    # if request.function != "add_problem" :
        # redirect(URL('admin','login_error'))
    problem=db.problems(request.args(0,cast=int)) or redirect(URL('add_problem'))
    contest = db(db.contests.id == problem.contest_id).select()
    if not auth.is_logged_in() :
        redirect(URL('admin','login_error'))
    if contest[0].author != auth.user_id :
        redirect(URL('admin','login_error'))

    no = len(db(db.testcases.pid == problem.id).select())
    no += 1
    if request.vars :
        # print request.vars
        form=db.testcases.validate_and_insert(pid=problem.id,score=request.vars['score'],in_file=request.vars['in_file'],out_file=request.vars['out_file'],
                                        time_limit=request.vars['time_limit'],memory_limit=request.vars['memory_limit'])
        if form.errors :
            session.flash = "Form not filled right.!!Plz try again"
            redirect(URL('add_testcase',args=problem.id))
        if request.vars.add_next !=None :
            redirect(URL('add_testcase',args=problem.id))
        else :
            total=0
            for testcase in db(db.testcases.pid == problem.id).select() :
                total += testcase.score
            if total != 100 :
                session.flash="Total sum unequal to 100,Please edit"
                redirect(URL('edit_testcases',args=problem.id))
        redirect(URL('edit_testcases',args=problem.id)) #bandaria change redirect to where the setter should go after he has added the testcases
    return dict(testcase_number=no)
def edit_problems():
    problem = db.problems(request.args(0,cast=int))  ##need to add from where this controler is being called
    contest = db(db.contests.id == problem.contest_id).select()
    if not auth.is_logged_in() :
        redirect(URL('admin','login_error'))
    if contest[0].author != auth.user_id :
        redirect(URL('admin','login_error'))
    # images =[ image for image in db(db.problem_image.pid == problem.id).select() ]
    images = db(db.problem_image.pid == problem.id).select()
    if request.vars :
        # print "its here"
        # print request.vars
        if problem.name == request.vars['name'] :
            form = db(db.problems.id == problem.id).validate_and_update(statement=request.vars['statement'],
                                        sample_input=request.vars['sample_input'],sample_output=request.vars['sample_output'],
                                        think=request.vars['think'],code=request.vars['code'],level=request.vars['level'],dp=request.vars['dp'],
                                        graph=request.vars['graph'],
                                        computational_geometry=request.vars['computational_geometry'],
                                        greedy=request.vars['greedy'],
                                        search=request.vars['search'],
                                        network_flow=request.vars['network_flow'],
                                        heuristic=request.vars['heuristic'],
                                        maths=request.vars['maths'],
                                        string=request.vars['string'],
                                        adhoc=request.vars['adhoc'],
                                        ds=request.vars['ds']
                                        )
            if form.errors :
                session.flash = "Form not filled right.!! Plz try again"
                redirect(URL('edit_problems',args=problem.id))
        else :
            form = db(db.problems.id == problem.id).validate_and_update(name=request.vars['name'],statement=request.vars['statement'],
                                        sample_input=request.vars['sample_input'],sample_output=request.vars['sample_output'],
                                        think=request.vars['think'],code=request.vars['code'],level=request.vars['level'],dp=request.vars['dp'],
                                        graph=request.vars['graph'],
                                        computational_geometry=request.vars['computational_geometry'],
                                        greedy=request.vars['greedy'],
                                        search=request.vars['search'],
                                        network_flow=request.vars['network_flow'],
                                        heuristic=request.vars['heuristic'],
                                        maths=request.vars['maths'],
                                        string=request.vars['string'],
                                        adhoc=request.vars['adhoc'],
                                        ds=request.vars['ds']
                                        )
            if form.errors :
                session.flash = "Form not filled right.!! Plz try again"
                redirect(URL('edit_problems',args=problem.id))

        subname="deletebox"
        c=0
        for image in images :
            name=subname + str(c)
            c = c + 1
            if request.vars[name] == "1" :
                db(db.problem_image.id == image.id ).delete()

        image_index=1
        image_subname='uploadimage'
        image_name='uploadimage0'
        while request.vars[image_name]!=None :
            if request.vars[image_name] == '' :
                image_name = image_subname + str(image_index)
                image_index += 1
                continue
            form2=db.problem_image.validate_and_insert(pid=problem.id,file=request.vars[image_name])
            image_name = image_subname + str(image_index)
            image_index += 1

        redirect(URL('edit_problems',args=problem.id))
    return dict(problem=problem,images=images)

def edit_testcases() :
    problem = db.problems(request.args(0,cast=int))  ##need to add from where this controler is being called
    contest = db(db.contests.id == problem.contest_id).select()
    if not auth.is_logged_in() :
        redirect(URL('admin','login_error'))
    if contest[0].author != auth.user_id :
        redirect(URL('admin','login_error'))
    testcases = [testcase for testcase in db(db.testcases.pid == problem.id).select()]
    if request.vars :
        print request.vars
        c=1
        subname="test"
        for testcase in testcases :
            name = subname + str(c)
            c += 1
            if request.vars[name] == "1" :
                db(db.testcases.id == testcase.id).delete()
        if request.vars.add_more != None :
            redirect(URL('add_testcase',args=problem.id))
        else :
            redirect(URL('edit_testcases',args=problem.id))
    total=0
    for testcase in testcases :
        total += testcase.score
    if total != 100 :
        response.flash="Total sum unequal to 100,Please edit"
    else:
        pass#LINK COMES HERE
    return dict(testcases=testcases)

def edit_testcase() :
    if request.function != "edit_testcases" :
        redirect(URL('admin','login_error'))
    testcase = db.testcases(request.args(0,cast=int))
    problem = db(db.problems.id == testcase.pid).select()
    contest = db(db.contests.id == problem.contest_id).select()
    if not auth.is_logged_in() :
        redirect(URL('admin','login_error'))
    if contest[0].author != auth.user_id :
        redirect(URL('admin','login_error'))
    if request.vars :
        form=db(db.testcases.id==testcase.id).validate_and_update(score=request.vars['score'],in_file=request.vars['in_file'],out_file=request.vars['out_file'],
                                        time_limit=request.vars['time_limit'],memory_limit=request.vars['memory_limit'])
        if form.errors :
            session.flash = "Form not filled right.!!Plz try again"
            redirect(URL('edit_testcase',args=testcase.id))
        redirect(URL('edit_testcases',args=testcase.pid))
    return dict(testcase=testcase)
def login_error() :
    return dict()

def edit_contest():
    this_page = db.contests(request.args(0,cast=int)) or redirect(URL('contests','user_contests'))
    form = SQLFORM(db.contests, this_page).process( next = URL('contest','view',args=this_page.id))
    return dict(form=form)

def show_problems():
    p=db(db.problems.contest_id==request.args[0]).select()
    return dict(prob=p)

def delete_problems():
    if not auth.is_logged_in() :
        redirect(URL('admin','login_error'))
    pid=request.args(0)
    if db.problems(pid).contest_id.author != auth.user_id :
        redirect(URL('admin','login_error'))
    db(db.testcases.pid==request.args[0]).delete()
    db(db.problem_image.pid==request.args[0]).delete()
    db(db.problems.id==request.args[0]).delete()
    session.flash="Problem Succesfully Deleted"
    redirect(URL('admin','user_contests'))
    return dict()

def user_contests():
    if not auth.is_logged_in() :
        redirect(URL('admin','login_error'))
    c=db(db.contests.author==auth.user).select()
    confp=[]
    conpast=[]
    for c in c:
        if((c.start_time + datetime.timedelta(hours=c.duration)) > request.now):
            confp.append(c)
        else:
            conpast.append(c)
    return dict(conf=confp,conpast=conpast)

@auth.requires_login()
def new_contest():
    db.contests.author.default=auth.user_id
    form=SQLFORM(db.contests,formstyle="bootstrap3_stacked")
    if form.process().accepted:
        redirect(URL('admin','show_problems',args=form.vars.id))
    return locals()
