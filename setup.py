from setuptools import setup, find_packages

setup(
   name='pacifica',
   version='1.0',
   description='Pacifica Sessions Servie',
   author='Marat Valiev`',
   author_email='marat.valiev@gmail.com',
   packages=find_packages(),
   include_package_data=True,
   install_requires=['cherrypy'], #external packages as dependencies
)
