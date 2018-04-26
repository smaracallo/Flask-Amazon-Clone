#!/usr/bin/env python3

import csv
import os


os.system('echo "#!/usr/bin/env python3" >> run/core/__init__.py')
os.system('echo "" >> run/core/__init__.py')

os.system('echo "from flask import Flask, render_template" >> run/core/__init__.py')
os.system('echo "" >> run/core/__init__.py')

with open('setup/meta/namespace.txt', 'r') as f:
    rows = csv.reader(f)
    for row in rows:
        os.system('echo "from core.controllers.{stem} import controller as {stem}" >> run/core/__init__.py'.format(stem=row[0]))
os.system('echo "" >> run/core/__init__.py')
os.system('echo "" >> run/core/__init__.py')

os.system('echo "omnibus = Flask(__name__)" >> run/core/__init__.py')
with open('setup/meta/namespace.txt', 'r') as f:
    rows = csv.reader(f)
    for row in rows:
        os.system('echo "omnibus.register_blueprint({stem})" >> run/core/__init__.py'.format(stem=row[0]))

os.system('echo "" >> run/core/__init__.py')
