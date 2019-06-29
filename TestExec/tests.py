import unittest
import time
import pprint

from testexecconfig import TestExecConfig

pp = pprint.PrettyPrinter(indent=4)

class TestTestExecConfig(unittest.TestCase):

    def test_true( self ):
        self.assertTrue( True )

    def test_get_active_tests( self ):
        cfg = TestExecConfig( './test.config.json' )
        self.assertEqual( cfg.active_tests[0].test_id, 'P31' )
        self.assertEqual( cfg.active_tests[1].test_id, 'P32' )

    def test_calc_total_weight( self ):
        cfg = TestExecConfig( './test.config.json' )
        self.assertEqual( cfg.total_weight, 70 )

    def test_get_next_test( self ):
        cfg = TestExecConfig( './test.config.json' )
        cfg.get_next_test()
        self.assertTrue( True )

    def test_get_immediate_tests( self ):
        cfg = TestExecConfig( './test.config.json' )
        cfg.edit_cfg_file( 'P32', 'immediate', True )
        cfg.read()
        tests = cfg.get_immediate_tests()
        self.assertEqual( tests[0].test_id, 'P32' )
        cfg.edit_cfg_file( 'P32', 'immediate', False )
        self.assertTrue( True )
