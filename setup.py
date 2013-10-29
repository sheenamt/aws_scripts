"""
Setup.py template. Try this:

    sed 's/aws_scripts/newpackagename/g;s/aws/newscriptname/g' setup.py
"""

import os
import subprocess
import shutil
from distutils.core import setup
from os.path import join

subprocess.call('git log --pretty=format:%h -n 1 > aws_scripts/data/sha', shell = True)
subprocess.call('git shortlog --format="XXYYXX%h" | grep -c XXYYXX > aws_scripts/data/ver', shell = True)

from aws_scripts import __version__

params = {'author': 'Your name',
          'author_email': 'Your email',
          'description': 'Package description',
          'name': 'aws_scripts',
          'packages': ['aws_scripts','aws_scripts.scripts','aws_scripts.subcommands'],
          'package_dir': {'aws_scripts': 'aws_scripts'},
          'scripts': ['aws'],
          'version': __version__,
          'package_data': {'aws_scripts': [join('data',f) for f in ['sha','ver']]}
          }
    
setup(**params)
