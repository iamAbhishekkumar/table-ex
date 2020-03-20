from setuptools import setup

setup(
    name="convert",
    version='0.1',
    author="Abhishek",
    description="Table extracter from PDF",
    url='https://github.com/iamAbhishekkumar/table-Ex',
    py_modules=['main'],
    install_requires=[
        'click', 'tabula-py', ],
    entry_points='''
        [console_scripts]
        convert=convert:cli
    ''',
)
