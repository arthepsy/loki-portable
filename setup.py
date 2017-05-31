from setuptools import setup

setup(name='loki',
      version='0.1',
      description='Loki - Simple IOC and Incident Response Scanner',
      url='https://github.com/Neo23x0/Loki',
      author='Florian Roth',
      author_email='florian.roth@bsk-consulting.de',
      license='GPL',
      packages=['Loki'],
      namespace_packages=['Loki'],
      entry_points = {
          'console_scripts': ['loki=Loki.loki:main'],
      },
      zip_safe=False)
