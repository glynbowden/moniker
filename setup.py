from distutils.core import setup

setup(name='moniker',
      version='0.9.0',
      description='Python module to generate human readable names',
      author='Brian Stengaard',
      author_email='brian+github@stengaard.eu',
      url='http://github.com/stengaard/moniker',
      packages=['moniker'],
      package_data={'moniker': ['*txt']}
      )
