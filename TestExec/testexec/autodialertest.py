import pprint

from testexec.test import TestExecTest

pp = pprint.PrettyPrinter(indent=4)

class AutodialerTest(TestExecTest):

    def __init__( self, data ):

        TestExecTest.__init__(self, data)

        if data['autodialer_url'] is not None:
            self.autodialer_url = data['autodialer_url']

    def execute( self ):
        testid = self.test_id
        name = self.test_name
        print( f'Executing {testid}, name: {name} - type is Autodialer')
