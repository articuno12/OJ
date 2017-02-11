# Defining Constants

# The location on your system where OJ folder is placed. It is required to serve static content.
SYS_ROOT   = "/var/www/html/"

MYSQL_HOST = "localhost"           # Host address of MySQL server. Maybe "localhost" or an IP.
MYSQL_PORT = "3306"                # The port on which MySQL server is listening. The default for MySQL is 3306
MYSQL_USER = "root"            # USERNAME to which you have granted the database access.
MYSQL_PASS = ""            # PASSWORD for the abode user.
MYSQL_DB   = "oj"                  # The database to use for OJ.


# Language Support [ Just remove all the corresponding entries in following variables to disable submission in them ]
LANGUAGES = ["GNU GCC 4.3","G++"]
LANG_NICK = ["C","CPP"]
LANG_EXT  = ["c","cpp"]
TIME_FACTOR = [1,1]                           # Time limit are multiple by this factor for corresponding language

# Add a entry for each problem

#PROBLEMS_ID = ["P1","P2","P3","P4","P5","P6"]                             # ID of problem.
#ROBLEMS_NAME =  ["iFIBO","COINS","eMATH","SEQ","MCS","GRID"    ]         # Name of problem.
#OBLEMS_PAGE = ["P1.pdf","P2.pdf","P3.html","P4.pdf","P5.pdf","P6.pdf"]                      # File which contains the description of this corresponding entry. It should exists in OJ folder.
#PROBLEMS_SCORE = [100,100,100,100,100,100];                            # Total score attainable for corresponding problem
#MAX_SUBMISSION = [50,50,50,50,50,50];                              # Max. Submission allowed for corresponding problem
#
#TIME_DIFF = 5                                    # Minimum gap in seconds between two consecutive submission for same problem.
#"""

# Add a entry for each problem
PROBLEMS_ID = ["P1", "P2", "P3","P4","P5","P6", "P7", "P8","P9","P10","P11","P12"]#,"P13", "P14","P15", "P16","P17","P18","P19","P20","P21","P22","P23","P24","P25","P26"] 
# ID of problem.
PROBLEMS_NAME =  ["A", "Triangles", "Area of Intersection", "Armstrong Numbers", "Fibonacci Numbers", "The Power of Powers", "Moment of Inertia", "Centroid","Line Segment Intersection","Factorial Length","Divisibility Test","Quadratic"]#, "Number of Numbers","Modern Times","Circular Buffer", "Tom Sawyer Paints the Wall","Daenerys and her Dragons", "Depth of Post Order" ,"Robb Stark and The Mysterious Message", "Fast Minimum", "Diameter of BT","Jon Snow and the White Walker","Rohan and the Greatest Realm","The Three Eyed Raven","Longest Path","Shortest Path","Online Median","Ordering Tasks","Potato Factory","Minimum Spanning Tree","Prime Path"]         			
# Name of problem.
PROBLEMS_PAGE = ["p1.pdf", "p2.pdf", "p3.pdf", "p4.pdf", "p5.pdf", "p6.pdf", "p7.pdf", "p8.pdf","p9.pdf","p10.pdf","p11.pdf","p12.pdf"]#,"P9.pdf","P10.pdf", "P11.pdf","P12.pdf", "P13.pdf", "P14.pdf", "P15.pdf", "P16.pdf","P17.pdf","P18.pdf","P19.pdf","P20.pdf","P21.pdf","P22.pdf","P23.pdf","P24.pdf","P25.pdf","P26.pdf"] 
# File which contains the description of this corresponding entry. It should exists in OJ folder.
PROBLEMS_SCORE = [0,0,0,0,0,0,0,0,0,0,0,0]#, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0]   
# Total score attainable for corresponding problem
MAX_SUBMISSION = [50, 50, 50, 50, 50, 50, 50, 50]#, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50,50,50,50,50,50,50,50]     
# Max. Submission allowed for corresponding problem

TIME_DIFF = 10                                    # Minimum gap in seconds between two consecutive submission for same problem.

# Please stick to the time format. Time is in 24-hours format. And month short nick should be used.

startTime = "19 Mar 2016 17:00"                    # The time the contest start, evaluation starts and problems are visible.
endTime   = "9 Apr 2016 23:59"                   # The time contest ends, evaluation stops and submissions are freezed.
regTime   = "31 Aug 2015 23:59"	                  # The time when registration stops. TeamList is freezed.
