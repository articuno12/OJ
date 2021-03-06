# Contains information about test data for problems

TEST_ROOT = "/root/Ass1/"   # The location where test cases input/output files are located on your system. Absolute Path.

# 'testcases' should map problemID to a list of test cases.
# Each test case is a tuple in following format.
# ( inputFilename, outputfilename, score, memory limit in MBs, time limit in secs)

testcases = {
#	"P1" : [ ("min_in1","min_out1",25,10,3) ,("min_in2","min_out2",25,10,3) ,("min_in3","min_out3",25,10,3) ,("min_in4","min_out4",25,10,3) ],
	



#"P1" : [ ("1/1.in","1/1.out",30,256,1),("1/2.in","1/2.out",70,256,2)],

#"P2" : [ ("2/1.in","2/1.out",100,256,3)],

#"P3" : [ ("3/1.in","3/1.out",100,256,3)],

#"P4" : [ ("4/1.in","4/1.out",50,256,13),("4/2.in","4/2.out",50,256,13)],

#"P5" : [ ("5/1.in","5/1.out",50,256,2),("5/2.in","5/2.out",50,256,2)],

#"P7" : [ ("7/1.in","7/1.out",20,256,1),("7/2.in","7/2.out",20,256,1),("7/3.in","7/3.out",10,256,1),("7/4.in","7/4.out",10,256,1),("7/5.in","7/5.out",10,256,1),("7/6.in","7/6.out",10,256,1),("7/7.in","7/7.out",10,256,1),("7/8.in","7/8.out",10,256,1)],

#"P1" : [ ("1/1.in","1/1.out",50,256,7),("1/2.in","1/2.out",50,256,7)],

#"P2" : [ ("2/i1.in","2/1.out",30,256,1),("2/2.in","2/2.out",30,256,1),("2/3.in","2/3.out",40,256,1)],

#"P1" : [ ("1/1.in","1/1.out",50,256,7),("1/2.in","1/2.out",50,256,7)],

#"P2" : [ ("2/1.in","2/1.out",30,256,1),("2/2.in","2/2.out",30,256,1),("2/3.in","2/3.out",40,256,1)],

#"P1" : [ ("1/1.in","1/1.out",30,256,1),("1/2.in","1/2.out",30,256,2),("1/3.in","1/3.out",40,256,2)],

#"P2" : [ ("2/1.in","2/1.out",30,256,5),("2/2.in","2/2.out",30,256,5),("2/3.in","2/3.out",40,256,5)],

#"P1" : [ ("1/1.in","1/1.out",30,256,1),("1/2.in","1/2.out",40,256,2),("1/3.in","1/3.out",40,256,2)],

#"P2" : [ ("2/1.in","2/1.out",30,256,1),("2/2.in","2/2.out",40,256,3),("2/3.in","2/3.out",40,256,3)],

"P1" : [ ("1/1.in","1/1.out",30,256,1),("1/2.in","1/2.out",30,256,1),("1/3.in","1/3.out",40,256,2)],

"P2" : [ ("2/1.in","2/1.out",50,256,6),("2/2.in","2/2.out",50,256,6)],

"P3" : [ ("3/1.in","3/1.out",30,256,1),("3/2.in","3/2.out",30,256,4),("3/3.in","3/3.out",40,256,3)],

"P4" : [ ("4/1.in","4/1.out",30,256,1),("4/2.in","4/2.out",30,256,3),("4/3.in","4/3.out",40,256,3)],
}

# 'checker' should map problemID to a program name that is to be used to check out.
# You can code checker as per your need. They are simple C/CPP programs that take as argument two filenames locally available.
# The first file is, JUDGE output and second is contestant solution. If your problem has no JUDGE output, use a empty file and dont use it latter on.
# The program as its exit code ( return '0' / return '1' ) should return verdict as correct (0) or wrong (!0).
#
# By default, we provide a simple checker, exact.out that checks character by character.

checker  = {"P1":"exact.out","P2":"exact.out","P3":"exact.out","P4":"exact.out", "P6":"exact.out","P5":"exact.out","P7":"exact.out","P8":"exact.out","P9":"exact.out","P10":"exact.out","P11":"exact.out","P12":"exact.out","P13":"exact.out","P13":"exact.out","P13":"exact.out","P13":"exact.out","P13":"exact.out","P13":"exact.out","P14":"exact.out","P13":"exact.out","P14":"exact.out","P15":"exact.out","P18":"exact.out","P18":"exact.out","P18":"exact.out","P17":"exact.out","P16":"exact.out","P16":"exact.out","P19":"exact.out","P20":"exact.out","P21":"exact.out","P22":"exact.out","P23":"exact.out","P23":"exact.out","P24":"exact.out","P25":"exact.out","P26":"exact.out","P27":"exact.out","P28":"exact.out","P28":"exact.out","P29":"exact.out","P29":"exact.out","P30":"exact.out","P31":"exact.out","P31":"exact.out","P4":"exact.out","P4":"exact.out","P1":"exact.out","P3":"exact.out","P4":"exact.out","P5":"exact.out","P6":"exact.out","P7":"exact.out","P8":"exact.out","P9":"exact.out","P10":"exact.out","P2":"exact.out","P2":"exact.out","P7":"exact.out","P8":"exact.out","P9":"exact.out","P10":"exact.out","P6":"exact.out","P1":"exact.out","P2":"exact.out","P3":"exact.out","P4":"exact.out","P5":"exact.out","P1":"exact.out","P1":"exact.out","P2":"exact.out","P3":"exact.out","P4":"exact.out","P1":"exact.out","P2":"exact.out","P3":"exact.out","P4":"exact.out","P5":"exact.out","P7":"exact.out","P1":"exact.out","P2":"exact.out","P1":"exact.out","P2":"exact.out","P1":"exact.out","P2":"exact.out","P1":"exact.out","P2":"exact.out","P1":"exact.out","P2":"exact.out","P3":"exact.out","P4":"exact.out"}
