from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function willl return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]# requiremnts.txt will contains "\n" when going to next line

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements



setup(
    name='BrandNewRepo',
    version='0.0.1',
    author='Ashish Tak',
    author_email='ashishtak21101@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

