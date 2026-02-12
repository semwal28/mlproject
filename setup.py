from setuptools import setup, find_packages

HYPEN_DOT = '-e .'

def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.read().splitlines()
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='Dhruv Semwal',
    author_email='dhruvsewmwal51@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)