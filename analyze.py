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
    print(problemurl)
    problemnumber = re.search(r"\[[0-9]+ \[", problemurl).group()[1:-2]
    return int(problemnumber)

folder = '.'
filelist = os.listdir(folder)
print(filelist)
mdfiles = [f for f in filelist if re.search("^[0-9]+-[0-9]+.md", f)]
print(mdfiles)

companymap = dict()
wholeregex = r"## [0-9]+ \[[A-Z][a-z]*\][\n]*This problem[A-Za-z ]+\."

for mdfile in mdfiles:
    with open(mdfile, 'r') as file:
        data = file.read()
        problemlist = re.findall(wholeregex, data)
        for problem in problemlist:
            print(problem)
            problemnumber = re.search(r"## [0-9]+ \[[A-Z][a-z]+\]", problem).group()[3:]
            companyname = re.search(r"by [A-Za-z ]+\.", problem).group()[3:-1]
            print(problemnumber)
            print(companyname)
            if companymap.get(companyname) is None:
                companymap[companyname] = set()
            companymap[companyname].add(warpstring(mdfile, problemnumber))

with open('output.md', "w+") as f:
    f.write("| company | problem set |\n")
    f.write("| ------- | ----------- |\n")
    for key in sorted(companymap):
        print key, companymap[key]
        f.write("| ")
        f.write(key)
        f.write(" | ")
        f.write(", ".join(sorted(companymap[key], key = urlkey)))
        f.write(" | \n")

