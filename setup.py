'''
the setup.py file is an essential part of packaging and distributing the python projects. it 
is used by setuptools (or distutils in older Python versions) to define the configuration of your 
project, such as its metadata,dependencies and more
'''
#find_packages will look in to the folder and look for packages i.e __init__.py file

from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    '''
    This function will return list of requiremnts
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                #ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(

    name="NetworkSecurity",
    version="0.0.0.1",
    author="Rahul Singh",
    author_email="singh.rahul.me07@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
     )

