from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='game-of-life',
    version='0.1.0',
    description='Sample Game of Life',
    long_description=readme,
    author='mpoqq',
    author_email='matthias.poqq@gmail.com',
    license=license,
    packages=find_packages(exclude='examples')
)
