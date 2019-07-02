import json
import random
import pprint

from testexec.test import TestExecTest
from testexec.mttest import MTTest
from testexec.autodialertest import AutodialerTest

valid_test_types = [
    'MTTest',
    'Autodialer'
]
pp = pprint.PrettyPrinter(indent=4)

class TestExecConfig(object):


    def __init__(self, cfg_file):

        self.cfg_file = cfg_file
        self.read()


    def read( self ):

        with open( self.cfg_file ) as json_file:
            data = json.load( json_file )

        self.elasticsearch = data['elasticsearch']
        self.tests = data['tests']
        self.active_tests = list()  # List of TestExecTest
        self.total_weight = 0

        self.get_active_tests( )
        self.calc_total_weight( )

    def get_active_tests( self ):

        valid_tests = list()
        for test in self.tests:
            if test['test_type'] in valid_test_types:
                if test['active']:
                    if test['test_type'].lower() == 'mttest':
                        valid_test = MTTest( test )
                    elif test['test_type'].lower() == 'autodialer':
                        valid_test = AutodialerTest( test )
                    else:
                        valid_test = TestExecTest( test )
                    valid_tests.append( valid_test )

        self.active_tests = valid_tests

        return valid_test

    def get_immediate_tests( self ):

        immediate_tests = list()
        for active_test in self.active_tests:
            if active_test.immediate:
                immediate_tests.append( active_test )

        return immediate_tests

    def edit_cfg_file( self, test_id, attribute, value ):

        with open( self.cfg_file ) as infile:
            data = json.load( infile )

        for i in range( 0, len(data['tests']) ):
            if data['tests'][i]['test_id'] == test_id:
                data['tests'][i][attribute] = value
            i += 1

        with open( self.cfg_file, 'w' ) as outfile:
            json.dump(data, outfile, sort_keys=True, indent=4)

        return

    def calc_total_weight( self ):

        total_weight = 0
        for active_test in self.active_tests:
            total_weight += active_test.test_weight

        self.total_weight = total_weight

        return total_weight

    def get_next_test( self ):

        R = random.randint( 0, self.total_weight )

        r_start = 0
        r_end = 0

        for active_test in self.active_tests:

            r_end = r_start + active_test.test_weight
            #print('[{0} - {1}] R = {2}'.format(r_start,r_end,R))

            if r_start <= R and R <= r_end:
                #pp.pprint( active_test.test_name )
                return active_test

            r_start = r_end

        return None
