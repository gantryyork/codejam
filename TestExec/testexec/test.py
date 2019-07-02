import pprint

pp = pprint.PrettyPrinter(indent=4)

class TestExecTest(object):

    def __init__( self, data ):

        if data['active'] is not None:
            self.active = data['active']

        if data['immediate'] is not None:
            self.immediate = data['immediate']

        if data['test_id'] is not None:
            self.test_id = data['test_id']

        if data['test_name'] is not None:
            self.test_name = data['test_name']

        if data['test_type'] is not None:
            self.test_type = data['test_type']

        if data['test_weight'] is not None:
            self.test_weight = data['test_weight']
