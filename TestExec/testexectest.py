import pprint

pp = pprint.PrettyPrinter(indent=4)

class TestExecTest(object):

    def __init__( self, data ):

        if data['active'] is not None:
            self.active = data['active']

        if data['immediate'] is not None:
            self.immediate = data['immediate']

        if data['test_id']:
            self.test_id = data['test_id']

        if data['test_name']:
            self.test_name = data['test_name']

        if data['test_type']:
            self.test_type = data['test_type']

        if data['test_weight']:
            self.test_weight = data['test_weight']

    def execute( self ):
        testid = self.test_id
        name = self.test_name
        print( f'Executing {testid}, name: {name}')
