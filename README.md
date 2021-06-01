# Selenium BDD framework

Automated selenium tests of http://automationpractice.com/ written in BDD

### Following tech stack is using:

python  
behave  
hamcrest 
invoke

## Setup:  
1. open terminal
2. run `git clone https://github.com/RafalRymek/bootcamp_selenium_bdd_framework` to clone repository 
3. run `cd bootcamp_selenium_bdd_framework` to move to local repository folder
4. run `pipenv install` to set up all necessary dependencies from Pipfile.lock
5. run `pipenv shell` to be able to use all pipenv dependencies from terminal

## Execution:

to run tests with specific parameters:  
`invoke run --tags=search_1 --browser=CH_HL --resolution=1200x800`

to run all tests without parameters:  
`invoke run`

## Docker Execution:
1. navigate to project directory
2. run `docker build -t bdd_tests .`
3. run `docker run -it bdd_tests`
4. open new terminal 
5. in new terminal run `docker ps` and find CONTAINER ID
6. run `docker exec -it [CONTAINER ID] sh`
7. run `pipenv install`
8. run `pipenv shell`
9. to run all tests without parameters run command `invoke run`
