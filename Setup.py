from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requiremensts(file_path:str)->List[str]:
    '''
    this funtion used for getting the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='neha',
    author_email='nehasoni01@gmail.com',
    packages=find_packages(),
    command_packages=get_requiremensts('requirements.txt')
    

)