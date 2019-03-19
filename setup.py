from setuptools import setup, find_packages

setup(
    name='newpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/EBIMASTER117/newpackage',
    author='EBIMASTER117',
    author_email='ebimaster117@gmail.com'
)
