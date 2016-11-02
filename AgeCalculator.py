# -*- coding: utf-8 -*-
"""
Age Calculator ...

@author: kianoush
"""
import re
from subprocess import call
from platform import system
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
if(system()=="Linux"): call("clear", shell=True)
if(system()=="Windows"): call("cls", shell=True)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class color:
    if(system() == 'Linux'):
        cyan = '\033[96m'
        blue = '\033[94m'
        green = '\033[92m'
        yellow = '\033[93m'
        red = '\033[91m'
        end = '\033[0m'
    else:
        cyan, blue, green, yellow, red, end = '', '', '', '', '', ''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print color.cyan+"""
</></></></></></></></></></></></>
</>                              </>\
"""+color.end
print color.yellow+"""\
</>   Age Calculator Script      </>\
"""+color.end
print color.cyan+"""\
</>                              </>
</></></></></></></></></></></></>

[+] Date Pattern: year/month/day
[+] You can enter (Shamsi) date or (Garigorie) date or ...
[+] Version 1.1
[+] Author : Kianoush0098
[*] I LOVE IRAN ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
"""+color.end
print color.yellow+"[?] For example 2000/12/17 |or| 1378/9/17 "+color.end
print color.blue+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+color.end
age = raw_input("Birth Date >>> ")
date = raw_input("Today Date >>> ")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
simple = re.compile("\d*/\d*/\d*")
pattern1 = re.search(simple, age)
pattern2 = re.search(simple, date)
if(pattern1 and pattern2):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    ageSep = pattern1.group().split("/")
    dateSep = pattern2.group().split("/")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    year1, year2 = int(ageSep[0]), int(dateSep[0])
    month1, month2 = int(ageSep[1]), int(dateSep[1])
    day1, day2 = int(ageSep[2]), int(dateSep[2])
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    if(month1<=12 and month2<=12 and day1<=31 and day2<=31):
        if(year2 >= year1):
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            if(month2 < month1):
                month2 += 12
                year2 -= 1
                b = month2 - month1
            else: b = month2 - month1
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            if(day2 < day1):
                day2 += 30
                if(month2 > month1):
                    month2 -= 1
                else:
                    month2 -= 1
                    year2 -= 1
                c = day2 - day1
            else: c = day2 - day1
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            a = year2 - year1
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            print color.cyan+"=============================================="
            print "# birth date: "+pattern1.group()
            print "# Today date: "+pattern2.group()+color.end
            print color.yellow+"[^] Your age is (%i) Year , (%i) Month , (%i) Day " % (a, b, c)+color.end
            print color.cyan+"=============================================="+color.end
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        else: print color.red+"[!] Your birth year can\'t be bigger than this year [!]"+color.end
    else:
        print color.red+"[!] Error in The Birth date or Today date [!]"+color.end
else:
    print color.red+"[!] Error in The Birth date or Today date [!]"+color.end
