from setuptools import setup

setup(
   name='pacifica',
   version='1.0',
   description='Pacifica Sessions Servie',
   author='Marat Valiev`',
   author_email='marat.valiev@gmail.com',
   packages=['pacifica'],  #same as name
   install_requires=['cherrypy'], #external packages as dependencies
)
