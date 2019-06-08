import json
import pprint

class TestExecConfig:


    def __init__(self, cfg_file):

        self.cfg_file = cfg_file
        self.read()


    def read( self ):

        with open( self.cfg_file ) as json_file:
            data = json.load( json_file )

        self.elasticsearch = data['elasticsearch']
        self.cycle = data['cycle']
        self.tests = data['tests']
