import pprint

from testexec.test import TestExecTest

pp = pprint.PrettyPrinter(indent=4)

class MTTest(TestExecTest):

    def __init__( self, data ):

        TestExecTest.__init__(self, data)

        if data['mt_test_file'] is not None:
            self.mt_test_file = data['mt_test_file']

    def execute( self ):
        testid = self.test_id
        name = self.test_name
        print( f'Executing {testid}, name: {name} - type is MT')
