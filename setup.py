from setuptools import setup, find_packages

setup(
    name='pianoplayer',
    version='0.0.1',
    packages=find_packages(exclude=('tests', 'docs')),
    url='',
    license='',
    author='archydeberker',
    author_email='archy.deberker@gmail.com',
    description='Animate a piano to visualize sequences of notes',
    install_requires=[open('requirements.txt').read()],
    include_package_data=True,
)
