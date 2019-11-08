#!/usr/bin/python3
# Automates test case C700-OO-001c9

import os
import argparse

import pprint
pp = pprint.PrettyPrinter(indent=4)


def main():

    test_pass = False

    exit_code = setup_provisioning()
    test_pass = calc_pass(exit_code)

    if test_pass:
        exit_code = verify_iperf3()
        test_pass = calc_pass(exit_code)

    if test_pass:
        exit_code = run_sip_autodialer()
        test_pass = calc_pass(exit_code)

    if test_pass:
        exit_code = setup_classmark9()
        test_pass = calc_pass(exit_code)

    # Other stuff

    if test_pass:
        exit_code = collect_artifacts()
        test_pass = calc_pass(exit_code)

    return

 
def setup_provisioning():

    # Use existing wrapper script
    # Must work from speedbuild-01

    cmd = '/usr/bin/expect expectProv-qpsk-bdu3'
    exit_code = os.system(cmd)

    return exit_code


def verify_iperf3():
    
    # Need a wrapper script for this

    return exit_code


def run_sip_autodialer():

    cmd = 'vl1_sip_autodialer'
    exit_code = os.system(cmd)

    return exit_code


def setup_classmark9():

    cmd = 'setup-c700-classmark9.sh onOrbit-C700 C700-OO-x01c9-v'
    # No need to tee the output
    # I don't know what to do with the output file
    exit_code = os.system(cmd)

    return exit_code


def collect_artifacts():

    cmd = 'C700-OO-001-qpsk.bash'
    exit_code = os.system(cmd)

    return exit_code


def calc_pass(result):

    if code != 0:
        return False
    else:
        return True





if __name__ == "__main__":
    parser = argpars.ArgumentParser()
    parser.add_argument( 
        "-x", "--xid", 
        help = "Execution ID",
        action = "store_true"
    )
    args = parser.parse_args()
    main(args)
