**Run the program**: 
Go to "Testing_Version2.py" file and run. 
It currently works for one small schedule. Need more testing!
The run time is extremely long. Need to upgrade the algorithm to lower the run time

**What is this project for**: 
K-12 principles can use this program to create their master's schedule for the school year. 
It is a work in progress.

**progress**:
able to generate initial schedule and check for its hard constraints
algorithm is implemented
Current work: 1. Build a website for users to input information and get a feasible schedule 
              2. Make the website available to people
              3. Allow certain class "multiple type" to have the classes at the same time (such as language course)

Later improvement: 1. able to generate schedule for different grades
           2. be able to detect the existence of feasible solutions
           3. update the algorithm, such as easier way to calculate hard constraint
           4. calculation of soft constraint and optimization method 

**Assumption for input**: 
1. Teacher name needs to be unique
2.



Program Glossary:
course folder: contain course class, and function related to its database
teacher folder: contain teacher class, and function related to its database
potential_useless_file: may not be of use due to use of "class"
schedule: schedule class with its ability to generate its own schedule and calculate hard constraints
