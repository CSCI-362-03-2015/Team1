import os
import unittest
import subprocess

def delTemp():
     #this portion empties the temp directory 
    for j in os.listdir("../temp/"):
        os.remove("../temp/" + j)

def main():

    delTemp()
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
                path = findComponent(lines[0].strip('\n'))
                a,b =lines[4].split(',')
                subprocess.call([path+"/a.out", a, b])
                answer = findAnswer(lines[0].strip('\n'))
                print("program gave us: " +answer)
                if answer ==(lines[5].strip('\n')):
                    print("This test has passed")
                else:
                    print("This test has failed")
                
                


def findComponent(case):
    path =""
    print("searching for test case "+case+ " driver")
    for (root,dirs,files) in os.walk("./testCasesExecutables/"):
        for i in dirs:
            if i == "testcase"+case:
                path=(root+i)
                print("component found in " + path)
                
    return path
    
def findAnswer(testnumber):
    answer=""
    for (root,dirs,files) in os.walk("./temp"):
        for i in files:
            if i == "TestCase"+testnumber+".txt":
                path=(root)
                print("answer found in " + path)
                with open(path+"/TestCase"+testnumber+".txt", "r") as f:
                    for line in f:
                        answer=line.strip('\n')
    if answer=="":
        print("no answer found")
    return answer
    
            

main()
