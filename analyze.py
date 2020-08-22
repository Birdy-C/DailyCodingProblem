import os
import re

url = "https://github.com/Birdy-C/DailyCodingProblem/blob/master/"
def warpstring(mdfile, problemnumber):
    problemurl = problemnumber
    problemurl = problemurl.replace(' ', '-')
    problemurl = problemurl.replace('[', '')
    problemurl = problemurl.replace(']', '')
    problemurl = problemurl.lower()
    return "[" + problemnumber + "](" +url + mdfile + '#' + problemurl + ")"

def urlkey(problemurl):
    problemnumber = re.search(r"\[[0-9]+ \[", problemurl).group()[1:-2]
    return int(problemnumber)

def mapfile(mdfile):
    number = mdfile[:-3]
    return '[' + number + "](" + mdfile + ")\n"


def filekey(mdfile):
    print mdfile
    problemnumber = re.search(r"[0-9]+\.md", mdfile).group()[:-3]
    return int(problemnumber)


folder = '.'
filelist = os.listdir(folder)
print(filelist)
mdfiles = [f for f in filelist if re.search("^[0-9]+-[0-9]+.md", f)]
mdfiles = sorted(mdfiles, key = filekey)
print(mdfiles)

companymap = dict()
wholeregex = r"[0-9]+ \[[A-Z][a-z]*\][\n]*This problem[A-Za-z ]+\."
for mdfile in mdfiles:
    with open(mdfile, 'r') as file:
        data = file.read()
        problemlist = re.findall(wholeregex, data)
        for problem in problemlist:
            problemnumber = re.search(r"[0-9]+ \[[A-Z][a-z]+\]", problem).group()
            companyname = re.search(r"by [A-Za-z ]+\.", problem).group()[3:-1]
            print(problemnumber)
            print(companyname)
            if companymap.get(companyname) is None:
                companymap[companyname] = set()
            companymap[companyname].add(warpstring(mdfile, problemnumber))



# print out the readme.md
with open('README.md', "w+") as f:
    f.write("# DailyCodingProblem\n \
https://www.dailycodingproblem.com/\n\n\
## Problem List\n\n")

    mdfilestring = map(mapfile, mdfiles)
    f.write("\n".join(mdfilestring))

    f.write("## Tag\n\n")
    f.write("| company | problem set |\n")
    f.write("| ------- | ----------- |\n")
    for key in sorted(companymap):
        f.write("| ")
        f.write(key)
        f.write(" | ")
        f.write(", ".join(sorted(companymap[key], key = urlkey)))
        f.write(" | \n")

