# Main module

import argparse
import importlib

from common.consts import *


def get_test_class(test_name, connector):
    # Load the test class by test type

    test_module = importlib.import_module(TEST_FORMAT.format(test_name))
    return test_module.Test(connector)


def get_connector_class(db_type):
    # Load the DB connector class by DB type

    connector_module = importlib.import_module(CONNECTOR_FORMAT.format(db_type))
    return connector_module.Connector()


def run_tests(dbs, tests, count, is_verbose):
    # Run chosen tests count times per test on chosen DBs

    # TODO: handle KeyboardInterruption

    for db_type in dbs:
        print DB_NAME_FORMAT.format(db_name=db_type.capitalize())
        for test_type in tests:

            metadata = {'exec_times': []}

            if is_verbose:
                print TEST_NAME_FORMAT.format(test_name=test_type, count=count)

            for test_num in range(1, count + 1):
                with get_connector_class(db_type) as connector:
                    with get_test_class(test_type, connector) as test:
                        test.run_test(metadata=metadata)

                print_results(test_type, test_num, count, metadata['exec_times'], is_verbose)


def print_results(test_name, num, total, time_data, is_verbose):
    latest_run = time_data[-1]
    time_data = sorted(time_data)
    min_time = time_data[0]
    max_time = time_data[-1]
    avg_time = sum(time_data) / len(time_data)

    # Mid-run report
    if is_verbose:
        print CURRENT_RESULTS_FORMAT.format(test_name=test_name, num=num, total=total, latest=latest_run, avg=avg_time,
                                            min=min_time, max=max_time)

    if num == total:
        # Last run, show full summery
        print SUMMERY_FORMAT.format(test_name=test_name, total=total, avg=avg_time, min=min_time, max=max_time)


def parse_args():
    # Parse command line arguments

    parser = argparse.ArgumentParser()
    parser.add_argument('dbs', nargs='+', help="DB connector to use for the tests.", default=DEFAULT_DBS)
    parser.add_argument('-t', '--tests', nargs='+', help="Tests to preform.", default=DEFAULT_TESTS)
    parser.add_argument('-c', '--count', type=int, help="How many times to repeat each test.", default=DEFAULT_COUNT)
    parser.add_argument('--verbose', action='store_true', help="Display result for each test.", default=False)
    return parser.parse_args()


def main():
    args = parse_args()
    run_tests(dbs=args.dbs, tests=args.tests, count=args.count, is_verbose=args.verbose)


if __name__ == '__main__':
    main()
