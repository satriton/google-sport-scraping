from setuptools import find_packages, setup

setup(
    name='sport-scrapper',
    packages=find_packages(include=['sport-scrapper']),
    version='0.1.0',
    description='Sport scrapper that aim to get score of particular team',
    author='satriton',
    install_requires=['python-dotenv', 'bs4', 'selenium'],
)
