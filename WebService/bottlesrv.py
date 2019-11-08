#!/usr/bin/python3

import os
import re
import json
import subprocess

import pprint
pp = pprint.PrettyPrinter(indent=4)

from bottle import route, run


@route('/hello')
def hello():
    return "hello world"

@route('/filesystems')
def ps():
    result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').splitlines()

    fss = list()

    regex = re.compile('Filesystem')

    for line in lines:
        if regex.match(line):
            continue
        name, size, used, avail, pct, mount = line.split()
        fs = {
            'name':name,
            'size':size,
            'used':used,
            'avail':avail,
            'pct':pct,
            'mount':mount
        }
        fss.append(fs)

    response = {'filesystems':fss}


    return json.dumps(response)

run(host='localhost', port=8080, debug=True)
