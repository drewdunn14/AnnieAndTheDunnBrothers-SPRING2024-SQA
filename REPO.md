# **Final Report - Annie and the Dunn Brothers**
### **COMP 5710 - Software Quality Assurance**

#### **What We Did**
- _Setup_
  - We started by first downloading the zip file and creating a new repository in GitHub with the file contents. We then each cloned the repository from GitHub to our local machine and divided up the work equally among us.
- _Part A_
  - We implemented a git hook in our project that runs vulnerability analysis on each commit. The results of this vulnerabilty analysis can be found in vulnerabilities.csv. Our analysis reported 12 vulnerabilities all with low severity.
  - We utilized 'bandit' as our vulnerability analysis tool, as it is widely trusted throughout the industry and also has great docs. This allowed us to efficiently create the necessary logic for our commit hook.
  - The logic used to create the hook is available in 'commit-hook.txt' and the output of the hook is available in the 'vulnerabilities.csv' file in this repo.
- _Part B_
  - We created a fuzz.py file which picked out 5 functions in the existing repository to pass large amounts of bad input into them. We collected the error messages that fuzzing threw which we could use to make the functions stronger. Additionally the fuzz.py file is automatically executed as a github action upon any push to the repo. This allows for push-by-push analysis of how each of the chosen methods responds to the fuzzing.
      - *List of the five methods that were fuzzed:*
        - 'dumpContentIntoFile' from 'mining.py'
        - 'deleteRepo' from 'mining.py'
        - 'makeChunks' from 'mining.py'
        - 'cloneRepo' from 'mining.py'
        - 'getDevEmailForCommit' from 'mining.py'

  - Below are the relevant screenshots for the fuzzing of each of the five methods when executed from the github actions tab.
  ![Logs from fuzzing methods 1 & 2](fuzzing1&2.png)
  ![Logs from fuzzing methods 3,4, & 5](fuzzing345.png)

- _Part C_
  - We implemented simple logging into 5 functions in the existing repository. These logs would output the parameters given to these functions as well as the data sources accessed within. This is important to ensure the functions are being used in the way that they are intended and not being attacked.

     - *Methods changed:*
          - report.py: reportDensity
          - frequency.py: reportEventDensity, reportProportion
          - dataset.stats.py: getFileLength, getAllFileCount
    
- _Part D_
  - To integrate Continuous Integration, we followed the steps similar to our CI Workshop by creating a .yaml file that implements the Codacy Analysis CLI in our project as a GitHub action. This file can be found in our .github/workflows directory. Once pushed to the branch, it will run the .yaml script on every push going forward.

#### **What We Learned**
- _Git Hooks_
  - We learned that Git Hooks are a helpful tool to automatically check your code for any issues before you end up updating your live deployments. They can act as a safeguard to ensure that large software projects are using best practices.
- _Fuzzing_
  - We learned that fuzzing is an incredibly helpful debugging and testing technique that floods a method with bad input to see if it will break. The error messages we receive from fuzzing allow us to find and fix edge cases in our code.
- _Forensics_
  - We learned that forensics is a helpful practice to log important information about a function (such as the data sources accessed or the parameters passed in). This helps for debugging and ensuring that the functions are being used correctly.
- _Continuous Integration_
  - We learned that Continuous Integration is a way for large software projects to manage complexity and find issues in the code during a push to a branch. This allows for continued accountability as many people might be working on a large project. Codacy checks for things like poor practices, errors, and generates warnings based on what it finds. GitHub Actions in general are a powerful tool that allow you to run scripts from GitHub directly. These can be either event triggered or time triggered.
