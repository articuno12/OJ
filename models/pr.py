import math
def yousuck():

    #< [A] Construct User Point in d-dimension space
    user_coord = []  #Binary Content list
    user_cw = 5   #code-wise rating  [1,10]
    user_tw = 7   #think-wise rating [1,10]
    user_weight = 5 #inversly proportional to noobness of user ; use in k-mean clustering ; [1,10]
    user_solved_pid = []

    #<<Populate solved problems by logged-in user
    user_solved_prblm = [[0 for x in range(50)] for y in range(20)]   #2D array (refer Doc)
    user_solved_hard_cw = []
    user_solved_hard_tw = []
    pc=0 #Problem count as populated in row1 defined next

    row1=db((db.livesubm.uid==auth.user_id) & (db.livesubm.status=="Accepted")).select(join=db.problems.on((db.problems.id==db.livesubm.pid)))#<DONE>: change to livesubm.uid==current_uid in place of [.lang=="CPP"]
    for r1 in row1:

        user_solved_hard_cw.append(r1.problems.code)
        user_solved_hard_tw.append(r1.problems.think)
        user_solved_pid.append(r1.problems.id)

        #Below 15 is the constant for parameters , current parameters are features (dp,graph,etc)
        param=15

        for i in range(param):    #Initialize each coloumn with 0
            user_solved_prblm[i][pc]=0

        if r1.problems.dp==True:
            user_solved_prblm[0][pc]=1

        if r1.problems.graph==True:
            user_solved_prblm[1][pc]=1

        if r1.problems.computational_geometry==True:
            user_solved_prblm[2][pc]=1

        if r1.problems.greedy==True:
            user_solved_prblm[3][pc]=1

        if r1.problems.search==True:
            user_solved_prblm[4][pc]=1

        if r1.problems.network_flow==True:
            user_solved_prblm[5][pc]=1

        if r1.problems.maths==True:
            user_solved_prblm[6][pc]=1

        if r1.problems.heuristic==True:
            user_solved_prblm[7][pc]=1

        if r1.problems.string==True:
            user_solved_prblm[8][pc]=1

        if r1.problems.adhoc==True:
            user_solved_prblm[9][pc]=1

        if r1.problems.ds==True:
            user_solved_prblm[10][pc]=1

        pc+=1

        #<<<Now use just built user_solved_prblm table to compute user_coord
        cur=0

        for x in range(param):
            cur=0

            for y in range(pc):
                cur=cur+(user_solved_prblm[x][y]*(user_solved_hard_cw[y]+user_solved_hard_tw[y])) #<TIL>

            user_coord.append(cur)
        #>>>

    #>>

    #>

    #< [B] Construct Problem points

    prblm_coord = [[0 for x in range(50)] for y in range(20)] #Refer doc
    prblm_hard_cw=[]
    prblm_hard_tw=[]
    ppc=0 #populated problem count

    row2=db(db.problems.id>0).select() #Select all problems initially

    for r2 in row2:
        ju=1
        for x in user_solved_pid:  #Don't construct points off problems already solved
            if r2.id==x:
                ju=0
                break

        if ju==0:   #Skip populating space with problems already solved
            continue

        for i in range(17):
            prblm_coord[i][ppc]=0

        fact=r2.think+r2.code   #<TIL>

        if r2.dp==True:
            prblm_coord[0][ppc]=fact

        if r2.dp==True:
            prblm_coord[0][ppc]=fact

        if r2.graph==True:
            prblm_coord[1][ppc]=fact

        if r2.computational_geometry==True:
            prblm_coord[2][ppc]=fact

        if r2.greedy==True:
            prblm_coord[3][ppc]=fact

        if r2.search==True:
            prblm_coord[4][ppc]=fact

        if r2.network_flow==True:
            prblm_coord[5][ppc]=fact

        if r2.maths==True:
            prblm_coord[6][ppc]=fact

        if r2.heuristic==True:
            prblm_coord[7][ppc]=fact

        if r2.string==True:
            prblm_coord[8][ppc]=fact

        if r2.adhoc==True:
            prblm_coord[9][ppc]=fact

        if r2.ds==True:
            prblm_coord[10][ppc]=fact

        ppc+=1

    #>

    #< [C] Create first 2 PRs , for mantaining ladder structure

    cur_prblm_coord = []
    #<TEL>:Get currently displayed problem's coordinate
    selected=2
    for i in range(15):
        cur_prblm_coord.append(prblm_coord[i][selected])
    #</TEL>

    res1,res2=1,2
    fin1_ham_dist,fin1_euc_dist=999999999999,999999999999
    fin2_ham_dist,fin2_euc_dist=999999999999,999999999999

    for i in range(ppc):
        if i==selected:   #<TEL/>
            continue

        cur_ham_dist,cur_euc_dist=0,0

        for j in range(15):
            if cur_prblm_coord[j]*prblm_coord[j][i]==0:
                cur_ham_dist+=1

            dif=(cur_prblm_coord[j]-prblm_coord[j][i])*(cur_prblm_coord[j]-prblm_coord[j][i])
            cur_euc_dist+=dif

        cur_euc_dist=math.sqrt(cur_euc_dist)

        if ((fin2_ham_dist>cur_ham_dist) or (fin2_ham_dist==cur_ham_dist and fin2_euc_dist>cur_euc_dist)):
            fin2_ham_dist=cur_ham_dist
            fin2_euc_dist=cur_euc_dist
            r2=i

        if ((fin1_ham_dist>fin2_ham_dist) or (fin1_ham_dist==fin2_ham_dist and fin1_euc_dist>fin2_euc_dist)):
            fin1_ham_dist,fin2_ham_dist=fin2_ham_dist,fin1_ham_dist
            fin1_euc_dist,fin2_euc_dist=fin2_euc_dist,fin1_euc_dist
            r1,r2=r2,r1


    '''    print ('<ans:'),
        print (r1,r2), #<RES\>
        print (':/ans>') '''

        #>

        #< [D] Modified K-mean Clustering for last 3 PRs

    km1=[1,0,4,1,5,9,0,2,4,8,1,0,4,8,0]  #Initial Clusters , k=3
    km2=[0,8,2,0,1,7,9,8,1,3,3,7,0,4,1]
    km3=[4,2,8,4,2,0,1,5,2,0,4,3,2,0,0]

    color = [1 for i in range(ppc+5)] #Store ith point falls under which cluster's Voronoi Region

    for iterations in range(1000):  #Max iterations untill assuming distrubtion weightage function converges
        td1 = [0 for xx in range(15)]
        td2 = [0 for xx in range(15)]
        td3 = [0 for xx in range(15)]

        for i in range(ppc):
            ed1,hd1=0,0   #Eucledian Distance,Hamming Distance wrt km1
            ed2,hd2=0,0
            ed3,hd3=0,0

            for j in range(15):
                if prblm_coord[j][i]*km1[j]==0:
                    hd1+=1

                if prblm_coord[j][i]*km2[j]==0:
                    hd2+=1

                if prblm_coord[j][i]*km3[j]==0:
                    hd3+=1

                ed1=ed1+((prblm_coord[j][i]-km1[j])*(prblm_coord[j][i]-km1[j]))
                ed2=ed2+((prblm_coord[j][i]-km2[j])*(prblm_coord[j][i]-km2[j]))
                ed3=ed3+((prblm_coord[j][i]-km3[j])*(prblm_coord[j][i]-km3[j]))

            ed1=math.sqrt(ed1)
            ed2=math.sqrt(ed2)
            ed3=math.sqrt(ed3)

            c1 = ed1 # = (30-hd1)+ed1 #70% ED + 30% Inverse HD composition
            c2 = ed2
            c3 = ed3

            if c1<=c2 and c1<=c3:
                color[i]=1

                for j in range(15):
                    td1[j]+=(prblm_coord[j][i])

            if c2<=c3 and c2<=c1:
                color[i]=2

                for j in range(15):
                    td2[j]+=(prblm_coord[j][i])

            if c3<=c1 and c3<=c2:
                color[i]=3

                for j in range(15):
                    td3[j]+=(prblm_coord[j][i])

        for xy in range(15):
            km1[xy]=td1[xy]/ppc
            km2[xy]=td2[xy]/ppc
            km3[xy]=td3[xy]/ppc

    ans1,d1=1,99999999999
    ans2,d2=2,99999999999
    ans3,d3=3,99999999999
    tmp1=0
    tmp2=0
    tmp3=0

    for bc in range(ppc):
        if r1==bc:
            continue

        if r2==bc:
            continue

        tmp1=0
        tmp2=0
        tmp3=0

        for j in range(15):
            tmp1+=((prblm_coord[j][bc]-km1[j])*(prblm_coord[j][bc]-km1[j]))
            tmp2+=((prblm_coord[j][bc]-km2[j])*(prblm_coord[j][bc]-km2[j]))
            tmp3+=((prblm_coord[j][bc]-km3[j])*(prblm_coord[j][bc]-km3[j]))

        tmp1=math.sqrt(tmp1)
        tmp2=math.sqrt(tmp2)
        tmp3=math.sqrt(tmp3)

        if tmp1<d1:
            ans1=bc
            d1=tmp1
            continue

        if tmp2<d2:
            ans2=bc
            d2=tmp2
            continue

        if tmp3<d3:
            ans3=bc
            d3=tmp3

    '''print('$'),
    print(ans1 , ans2 , ans3),
    print('$')'''

    rpl=[]
    rpl.append(ans1)
    rpl.append(ans2)
    rpl.append(ans3)

    rpl2=rpl[:]
    rpl2.append(r1)
    rpl2.append(r2)

    #>
    #return locals()
    #return dict(user_solved_prblm=user_solved_prblm,prblm_coord=prblm_coord,user_coord=user_coord)

    return dict(rpl=rpl,rpl2=rpl2)
