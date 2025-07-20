'''the stup.py file is an essential in distributing python projects
it is used by setuptools(or distutils in older python version)to define the configuration
of ur project,such as its metadata its dependencies and more'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->list[str]:
    requirement_lst:list[str]=[]
    try:
        with open('requirement.txt','r')as file:
        #read lines from the file 
            lines=file.readlines()
        ## process each line
            for line in lines:
                requirement=line.strip()
            ## ignore empty lines
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirement.txt file not found ')
    
    return requirement_lst

setup(
    name="Networksecurity",
    version="0.0.1",
    author="Kuldeep",
    author_email="kuldeep0009sharma@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements( )
)