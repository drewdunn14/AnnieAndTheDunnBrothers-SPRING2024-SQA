import pandas as pd 
from mining import mining


def fuzzValuesForDumpContentMethod(val1, val2):
   res = mining.dumpContentIntoFile(val1, val2)
   return res  

def fuzzValuesForDeleteRepo(val1, val2):
   res = mining.deleteRepo(val1, val2)
   return res

def fuzzValuesForMakeChunks(val1, val2):
   res = mining.makeChunks(val1, val2)
   return res

def fuzzValuesForCloneRepo(val1, val2):
   res = mining.cloneRepo(val1, val2)
   return res


def fuzzValuesForGetDevEmailForCommit(val1, val2):
   res = mining.getDevEmailForCommit(val1, val2)
   return res


def simpleFuzzer(): 
    ls_ = [
       ({}, 2),
       ("real", None),
       ("real", "notreal"),
       (0, 3),
       ("real", 30.0),
       (None,None),
       (10.324, 0),
       ([], 2)]

    print("Fuzzing for method #1...")
    print("Start fuzzing for method 'dumpContentIntoFile' from 'mining.py'")
    for i in range(0, len(ls_)):
      

      try:
         fuzzValuesForDumpContentMethod(ls_[i][0], ls_[i][1])  
      except Exception as error:
         print("values entered: ", ls_[i][0], ls_[i][1])
         print("Error message: ", error)
    print("End fuzzing for method 'dumpContentIntoFile' from 'mining.py'\n\n\n")

    print("Fuzzing for method #2...")
    print("Start fuzzing for method 'deleteRepo' from 'mining.py'")
    for i in range(0, len(ls_)):
      

      try:
         fuzzValuesForDeleteRepo(ls_[i][0], ls_[i][1])  
      except Exception as error:
         print("values entered: ", ls_[i][0], ls_[i][1])
         print("Error message: ", error)
    print("End fuzzing for method 'deleteRepo' from 'mining.py'\n\n\n")

    print("Fuzzing for method #3...")
    print("Start fuzzing for method 'makeChunks' from 'mining.py'")
    for i in range(0, len(ls_)):
      

      try:
         fuzzValuesForMakeChunks(ls_[i][0], ls_[i][1])  
      except Exception as error:
         print("values entered: ", ls_[i][0], ls_[i][1])
         print("Error message: ", error)
    print("End fuzzing for method 'makeChunks' from 'mining.py'\n\n\n")

    print("Fuzzing for method #4...")
    print("Start fuzzing for method 'cloneRepo' from 'mining.py'")
    for i in range(0, len(ls_)):
      

      try:
         fuzzValuesForCloneRepo(ls_[i][0], ls_[i][1])  
      except Exception as error:
         print("values entered: ", ls_[i][0], ls_[i][1])
         print("Error message: ", error)
    print("End fuzzing for method 'cloneRepo' from 'mining.py'\n\n\n")

    print("Fuzzing for method #5...")
    print("Start fuzzing for method 'getDevEmailForCommit' from 'mining.py'")
    for i in range(0, len(ls_)):
      

      try:
         fuzzValuesForGetDevEmailForCommit(ls_[i][0], ls_[i][1])  
      except Exception as error:
         print("values entered: ", ls_[i][0], ls_[i][1])
         print("Error message: ", error)
    print("End fuzzing for method 'getDevEmailForCommit' from 'mining.py'\n\n\n")

if __name__=='__main__':
    simpleFuzzer()
