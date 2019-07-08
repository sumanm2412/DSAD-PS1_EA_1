# -*- coding: utf-8 -*-

class EmpNode:
    def __init__(self, EId):
        self.empId = EId
        self.attCtr = 1
        self.left = None
        self.right = None

class BinaryTreeOperations:
    headCount = 0
    freqEmpID = 0
    freqCount = 0
    outputString = "\n\n"
    
    #1. def _readEmployeesRec(self, eNode, Eid): 
    #This function reads from the inputPS1.txt file the ids of employees entering and leaving the organization premises. 
    #One employee id should be populated per line (in the input text file) indicating their swipe (entry or exit). 
    #The input data is used to populate the tree. 
    #If the employee id is already added to the tree, 
    #then the attendance counter is incremented for every subsequent occurrence of that employee id in the input file. 
    #Use a trigger function to call this recursive function from the root node.
    def _readEmployeesRec(self, eNode, EId):
        if EId < eNode.empId:
            if eNode.left == None:
                eNode.left = EmpNode(EId)
            else:
                self._readEmployeesRec(eNode.left, EId)
        elif EId > eNode.empId:
            if eNode.right == None:
                eNode.right = EmpNode(EId)
            else:
                self._readEmployeesRec(eNode.right, EId)
        elif EId == eNode.empId:
            eNode.attCtr += 1
            
    #2. Def _getHeadcountRec(self, eNode): 
    #This function counts the number of unique IDs stored in the tree 
    #and prints the employee headcount for the day into the output.txt file as shown below.
    #Total number of employees today: xx
    #Use a trigger function to call this recursive function from the root node.
    def _getHeadCountRec(self, eNode):
        if eNode != None:
            self._getHeadCountRec(eNode.left)
            self.headCount+=1
            self._getHeadCountRec(eNode.right)


    #3. def _searchIDRec(self, eNode, eId): 
    #This function searches whether a particular employee has attended today or not. 
    #The function reads the search id from the file promptsPS1.txt 
    #where the search id is mentioned with the tag as shown below.
    #searchID:23, searchID:22
    #The search function is called for every searchID tag the program finds in the promptsPS1.txt file.
    #If the employee id is found it outputs the below string into the outputPS1.txt file
    #Employee id xx is present today.
    #If the employee id is not found it outputs the below string into the outputPS1.txt file
    #Employee id xx is absent today.
    #Use a trigger function to call this recursive function from the root node.	
    
    def _searchIDRec(self, eNode, eId):
        if eId < eNode.empId:
            if eNode.left == None:
                self.outputString += 'Employee id {} is absent today'.format(eId) + '\n'
            else:
                self._searchIDRec(eNode.left, eId)
        elif eId > eNode.empId:
            if eNode.right == None:
                self.outputString += 'Employee id {} is absent today'.format(eId)+ '\n'
            else:
                self._searchIDRec(eNode.right, eId)
        elif eId == eNode.empId:
            self.outputString += 'Employee id {} is present today'.format(eId)+'\n'
    

    #4. def _howOften_Rec(self, eNode, EId): 
    #This function counts the number of times a particular employee swiped today and 
    #if the employee is currently in the office or outside.
    #The function reads the id from the file promptsPS1.txt where the search id is mentioned with the tag as shown below.
    #howOften:12
    #howOften:22
    #howOften:11
    #The search function is called for every howOften tag the program finds in the promptsPS1.txt file.
    #If the employee id is found with an odd attendance count the below string is output into the outputPS1.txt file
    #Employee id xx swiped yy times today and is currently in office
    #If the employee id is found with an even attendance count the below string is output into the outputPS1.txt file
    #Employee id xx swiped yy times today and is currently outside office
    #If the employee id is not found it outputs the below string into the outputPS1.txt file
    #Employee id xx did not swipe today.
    
    def _howOften_Rec(self, eNode, EId):
        if EId < eNode.empId:
            if eNode.left == None:
                self.outputString += 'Employee id {} did not swipe today.'.format(EId) + '\n'
            else:
                self._howOften_Rec(eNode.left, EId)
        elif EId > eNode.empId:
            if eNode.right == None:
                self.outputString += 'Employee id {} did not swipe today.'.format(EId) + '\n'
            else:
                self._howOften_Rec(eNode.right, EId)
        elif EId == eNode.empId:
            if eNode.attCtr % 2 == 1:
                self.outputString += 'Employee id {} swiped {} times today and is currently in office'.format(EId, eNode.attCtr) + '\n'
            else:
                self.outputString += 'Employee id {} swiped {} times today and is currently outside office'.format(EId, eNode.attCtr) + '\n'
    
    #5. def _frequentVisitorRec(self, eNode): 
    #This function searches for the employee who has swiped the most number of times 
    #and outputs the below string into the outputPS1.txt file.
    #Employee id xx swiped the most number of times today with a count of yy
    #Use a trigger function to call this recursive function from the root node. 
    #For the sake of the assignment, you need to display any one of the employee ids 
    #if there are more than one employee who have entered maximum number of times. 
    #For example, if employee id 22 and 23 have both visited 3 times, the output should show either 22 or 23.
    
    def _frequentVisitorRec(self, eNode):
        if eNode != None:
            self._frequentVisitorRec(eNode.left)
            if self.freqCount < eNode.attCtr:
                self.freqCount = eNode.attCtr
                self.freqEmpID = eNode.empId
            self._frequentVisitorRec(eNode.right)
            
    #6. def printRangePresent(self, StartId, EndId): 
    #This function prints the employee ids 
    #in the range StartId to EndId and 
    #how often they have entered the organization in a file name outputPS1.txt.
    #The input should be read from the promptsPS1.txt file where the range is mentioned with the tag as shown below.
    #range:23:125
    #If Input range is given as 23 to 125 the output file should show:
    #Range: 23 to 125
    #Employee attendance:
    #23, 1, in
    #41, 3, in
    #121, 2, out
    
    def printRangePresent(self, eNode, StartId, EndId):
        self.outputString += 'Range: {} to {} '.format(StartId, EndId) + '\n'
        self.outputString += 'Employee attendance:' + '\n'
        endRange = EndId + 1
        
        for eId in range(StartId, endRange):
            self._printRangePresent(eId, eNode)

    def _printRangePresent(self, EId, eNode):
        if EId < eNode.empId:
            if eNode.left != None:
                self._printRangePresent(EId, eNode.left)
        elif EId > eNode.empId:
            if eNode.right != None:
                self._printRangePresent(EId, eNode.right)
        elif EId == eNode.empId:
            if eNode.attCtr % 2 == 1:
                self.outputString += '{}, {}, in'.format(EId, eNode.attCtr) + '\n'
            else:
                self.outputString += '{}, {}, out'.format(EId, eNode.attCtr) + '\n'

            
objBinaryTreeOperations = BinaryTreeOperations()

inputPSfile = open("inputPS1.txt", "r")
empRoot = None
for employeeId in inputPSfile:
	intEmployeeId = int(employeeId)
	if empRoot == None:
		empRoot = EmpNode(intEmployeeId)
	else:
		objBinaryTreeOperations._readEmployeesRec(empRoot, intEmployeeId)
            
objBinaryTreeOperations._getHeadCountRec(empRoot)
objBinaryTreeOperations.outputString += "Total number of employees today: {}".format(objBinaryTreeOperations.headCount) + '\n'

promptsf = open("promptsPS1.txt", "r")

for x in promptsf:
    prompt = x.split(':')[0]
    if prompt.strip().lower() == "searchid":
        objBinaryTreeOperations._searchIDRec(empRoot, int(x.split(':')[1]))
    elif prompt.strip().lower() == "howoften":
        objBinaryTreeOperations._howOften_Rec(empRoot, int(x.split(':')[1]))
    elif prompt.strip().lower() == "range":
        startId = int(x.split(':')[1])
        endId = int(x.split(':')[2]) + 1
        objBinaryTreeOperations.printRangePresent(empRoot, startId, endId)

objBinaryTreeOperations._frequentVisitorRec(empRoot)
objBinaryTreeOperations.outputString += "Employee id {} swiped the most number of times today with a count of {}".format(objBinaryTreeOperations.freqEmpID, objBinaryTreeOperations.freqCount) + '\n'
        
f = open("outputPS1.txt", "a")
f.write(objBinaryTreeOperations.outputString)
f.close()
