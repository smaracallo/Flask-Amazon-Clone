#!/usr/bin/env python3

import csv
import os


with open('setup/meta/namespace.txt', 'r') as e:
    rows = csv.reader(e)
    for row in rows:
        # Create controllers
        os.system('touch run/core/controllers/{stem}.py'.format(stem=row[0]))
        with open('run/core/controllers/{stem}.py'.format(stem=row[0]), 'w') as f:
            # Write controllers
            f.write("#!/usr/bin/env python3\n")
            f.write("from flask import Blueprint, render_template\n\n")
            f.write("controller = Blueprint('{stem}', __name__, url_prefix='/{stem}')\n")
            f.write("@controller.route('/<string:title>', methods=['GET'])\n")
            f.write("def lookup(title):\n")
            f.write("    if title == 'Republic':                     # TODO 2\n")
            f.write("        return render_template('republic.html') # TODO 2\n")
            f.write("    else:                                       # TODO 2\n")
            f.write("        pass                                    # TODO 2\n")
            # Create templates
        os.system("touch run/core/templates/{stem}.html".format(stem=row[0]))
            # Write templates
            # f.write("extends \"structure.html\"' >> run/core/templates/{stem}.html".format(stem=row[0]))
            # f.write("block main' >> run/core/templates/{stem}.html".format(stem=row[0]))
            # f.write("<h1>This is an H1 header</h1>' >> run/core/templates/{stem}.html".format(stem=row[0]))
            # f.write("endblock main' >> run/core/templates/{stem}.html".format(stem=row[0]))
            # # Rewrite templates
            # x = "sed -i -e 's/extends \"structure.html\"/\{% extends \"structure.html\" %\}/' {stem}.html".format(stem=row[0])
            # print(x)
            # f.write(x)
            # f.write("sed -i -e \"s/block main/\{% block main %\}/\" {stem}.html".format(stem=row[0]))
            # f.write("sed -i -e \"s/endblock main/\{% endblock main %\}/\" {stem}.html".format(stem=row[0]))