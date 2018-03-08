import os
from setuptools import setup

setup(name="LED3",
      version="0.1",
      description="LED Testing Assignment3 COMP30670",
      url="",
      author="Sophie Heseltine",
      author_email="sophie.heseltine@ucdconnect.ie",
      license="GPL3",
      packages=['LED3'],
      entry_points={
          'console_scripts':['LED3=LED3.main:main']
          }
      )
