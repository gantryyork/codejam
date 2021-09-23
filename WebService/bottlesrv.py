#!/usr/bin/python3

import os
import re
import json
import subprocess
from bottle import route, run
import pprint

pp = pprint.PrettyPrinter(indent=4)


VERSION = '1.0.0'


@route('/version')
def version():

    return VERSION


@route('/filesystems')
def filesystems():
    fss = fs()
    return fss


def fs():
    result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').splitlines()
    print(lines)

    fss = list()

    regex = re.compile('Filesystem')

    for line in lines:
        if regex.match(line):
            continue
        name, size, used, avail, pct, mount = line.split()
        fs = {
            'name': name,
            'size': size,
            'used': used,
            'avail': avail,
            'pct': pct,
            'mount': mount
        }

    return response


run(host='localhost', port=8080, debug=True)
