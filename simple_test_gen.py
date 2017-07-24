# Name: Jarid Bredemeier
# Date: 04/28/2017
# Modified: 05/05/2017

import sut
import random
import time
import sys

def takeAction(action):
    ok = sut.safely(action)
    checkOk = sut.check()

    if len(sut.newStatements()) > 0:
        print "NEW STATEMENT COVERAGE:", time.time(), len(sut.allStatements()), sut.newStatements()
    if len(sut.newBranches()) > 0:
        print "NEW BRANCH COVERAGE:", time.time() - start, len(sut.allBranches()), sut.newBranches()

    if (not ok) or (not checkOk):
        print "FAILED TEST"
        sut.prettyPrintTest(sut.test())
        sut.saveTest(sut.test(), "failure.test")
        sys.exit(255)


timeout = int(sys.argv[1])
start = time.time()

sut = sut.sut()

sut.setDebugSafelyMode(True)

R = random.Random(sys.argv[2])

# only command line arguments are 1) how long to test and 2) a random number seed for reproducibility

goodTests = []
PEXTEND = .32                                                                  
TEST_LENGTH = 32 
MEMORY = 8
                                                    
while (time.time() - start) < timeout:                                          
	
    if (len(goodTests) > 0) and (random.random() < PEXTEND):                                          
        index = random.randint(0, len(goodTests) - 1)
        state = goodTests[index][1]                                               
        sut.backtrack(state)
		
    else:                                                                       
        print("Restarting test...")                                                     
        sut.restart()                                                           
                                                                                
    for i in range(TEST_LENGTH):                                                                          
        action = sut.randomEnabled(R)                                           
        takeAction(action)       
		
    if MEMORY > 0:
        goodTests.append((sut.currBranches(), sut.state()))
        goodTests = sorted(goodTests, reverse = True)[:MEMORY]

sut.internalReport()
sys.exit(0)
