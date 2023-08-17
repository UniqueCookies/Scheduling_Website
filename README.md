**Run the program**: 
Go to "interface_for_database.py" file and run. 
It currently works for one small schedule. Need more testing!
The run time is extremetly long. Need to upgrade the algorithm to lower the run time

**What is this project for**: 
K-12 principles can use this program to create their master's schedule for the school year. 
It is a work in progress.

**progress**:
able to generate initial schedule and check for its hard constraints
algorithm is implemented
Later improvement: 1. able to generate schedule for different grades 
           2. Allow certain class "multiple type" to have the classes at the same time
           3. be able to detect the existence of feasible solutions
           4. update the algorithm, such as easier way to calculate hard constraint
           5. calculation of soft constraint and optimization method 

**Assumption for input**: 
1. Teacher name needs to be unique
2.



Program Glossory:
course folder: contain course class, and function related to its database
teacher folder: contain teacher class, and function related to its database
potential_useless_file: may not be of use due to use of "class"
schedule: schedule class with its ability to generate its own schedule and calculate hard constraints
