from setuptools import (setup,
                        find_packages)

from lovelace.config import PACKAGE

setup(name=PACKAGE,
      version='0.0.0',
      packages=find_packages(),
      install_requires=[
          'requests',
      ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest>=3.0.5',
                     'pydevd>=1.0.0',  # debugging
                     'hypothesis>=3.6.1',
                     'pytest-cov>=2.4.0',
                     ])
