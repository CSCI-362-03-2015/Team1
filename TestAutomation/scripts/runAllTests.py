import os
import unittest
import subprocess
from time import localtime, asctime

def delTemp():
     #this portion empties the temp directory 
    for j in os.listdir("./temp/"):
        os.remove("./temp/" + j)

def main():

    delTemp()
    tests=[]
    #changes to the TestAutomation directory
    os.chdir("./")
    print(os.getcwd())
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
                with open("./reports/report.html","a+") as report:
                    report.write("Test ID:" + lines[0]+"<br>")
                    report.write("Time stamp: "+ asctime(localtime())+"<br>")
                    report.write("requirement being tested:" + lines[1]+"<br>")
                    report.write("Component being tested: " +lines[2]+"<br>")
                    report.write("Method being tested: " +lines[3]+"<br>")
                    report.write("Inputs used for testing: " +lines[4]+"<br>")
                    report.write("Expected output: "+lines[5]+"<br>")
                    
                    if answer ==(lines[5].strip('\n')):
                        print("This test has passed")
                        report.write("The outcome was: " + answer+"<br>")
                        report.write("The test was  <font color=\"green\">successful</font>"+"<br>")
                        report.write("<br><br>")
                    else:
                        print("This test has failed")
                        report.write("the outcome was: " + answer+"<br>")
                        report.write("The test was a <font color=\"red\">failure</font>"+"<br>")
                        report.write("<br><br>")
                
            print('\n')
    subprocess.call(["see", "./reports/report.html"])
                


def findComponent(case):
    path =""
    driver = 0
    #todo: make independent of the case name, switch based on method name instead?
    print("searching for test case "+case+ " driver")
    if( case == '1' or case == '2'):
        driver = 1
    elif(case == '3' or case == '4' or case=='5' or case=='6' or case=='7'):
        driver = 2

    for (root,dirs,files) in os.walk("./testCasesExecutables/"):
        for i in dirs:
            if i == "testcase"+ str(driver):
                path=(root+i)
                print("component found in " + path)
                subprocess.call(["gcc", "./testCasesExecutables/testcase"+str(driver)+"/Driver"+str(driver)+".c","-w","-o", os.getcwd()+path.strip('.')+"/a.out"])
                
    return path
    
def findAnswer(case):
    answer=""
    found = False
    if( case == '1' or case == '2'):
        driver = 1
    elif(case == '3' or case == '4' or case=='5' or case=='6' or case=='7'):
        driver = 2
    for (root,dirs,files) in os.walk("./temp"):
        for i in files:
            if i == "TestCase"+str(driver)+".txt":
                path=(root)
                print("answer found in " + path)
                with open(path+"/TestCase"+str(driver)+".txt", "r") as f:
                    for line in f:
                        answer=line.strip('\n')
                found = True
    if found == False :
        print("no answer found")
    return answer
    
            

main()
