from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='rpa-tools',
   version='1.0',
   description='Processing tools for automation using Python',
   license="MIT",
   long_description=long_description,
   author='Donovan Adams',
   author_email='',
   url="https://github.com/hydrotik/rpa-tools",
   packages=['rpa-tools'],  #same as name
   install_requires=['rpa', 'face_recognition', 'fuzzywuzzy'], #external packages as dependencies
   # scripts=[
   #          'scripts/cool',
   #          'scripts/skype',
   #         ]
)