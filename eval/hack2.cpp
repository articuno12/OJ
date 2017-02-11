#include <string>
#include <fstream>
#include <streambuf>
#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
		ifstream myfile("rt_scripts.py");
		string find="outfile";
		string line;
	//	ofstream middle("middle");
	//	bool already=false;
	/*	if (myfile.is_open())
		{
				while ( getline (myfile,line) )
				{
						int pos=line.find(find);
						if(pos!=string::npos)
						{
							if(already)
							{
							  line.replace(pos,find.length(),"\"newin\"");
							}
							already=true;
						}
						middle<<line<<endl;
				}
				myfile.close();
		}
		else
		{
				exit(11);
		}
		middle.close();*/

		ifstream src("/root/Ass1/1/1.in",ios::binary);
		ofstream dest("backup",ios::binary);
		dest<<src.rdbuf();
		src.close();
		dest.close();
		ifstream src2("newin",ios::binary);
		ofstream dest2("/root/Ass1/1/1.in",ios::binary);
		dest2<<src2.rdbuf();
		src2.close();
		dest2.close();
		//remove("rt_scripts.py");
		return 0;
}
