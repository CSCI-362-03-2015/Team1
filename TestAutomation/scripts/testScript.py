import os
import unittest
import subprocess

def delTemp():
     #this portion empties the temp directory 
    for j in os.listdir("../temp/"):
        os.remove("../temp/" + j)

def main():

    #delTemp()
    tests=[]
    #changes to the TestAutomation directory
    os.chdir("../")
    for file in os.listdir("testCases"):
        if file.endswith(".txt"):
            print(file)
            with open(os.getcwd()+"/testCases/"+file, "r") as f:
                i =0
                lines =[]
                path = ""
                for line in f:
                    lines.append(line)
                    i = i+1
                print("this is test case #: "+lines[0].strip('\n'))
                tests.append(lines[0])
                print("this will be "+lines[1].strip('\n'))
                path = findComponent(lines[2].strip('\n'))
                root = (os.getcwd()+path.strip('.'))
                print(root)
                subprocess.call([root+"/a.out", "4","4"])
                print(findAnswer(lines[0].strip('\n')))


def findComponent(component):
    path =""
    print("searching for " + component)
    for (root,dirs,files) in os.walk("./testCasesExecutables"):
        for i in files:
            if i == component:
                path=(root)
                print("component found in " + root)
                
    return path
    
def findAnswer(testnumber):
    
    for (root,dirs,files) in os.walk("./temp"):
        for i in files:
            if i == "testcase"+testnumber+".txt":
                path=(root)
                print("answer found in " + path)
                with open(path+"/testcase"+testnumber+".txt", "r") as f:
                    for line in f:
                        answer=line.strip('\n')
                
    return answer
    
            

main()
