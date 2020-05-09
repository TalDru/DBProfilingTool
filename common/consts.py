# Definitions and consts

# Settings
DEFAULT_DBS = ['mongodb']
DEFAULT_TESTS = ['write', 'update', 'read']
DEFAULT_COUNT = 10

# Defaults
DEFAULT_SAMPLE_SIZE = 1000
DEFAULT_POOL_MAGNIFIER = 2
DEFAULT_DB_NAME = "data"
DEFAULT_TABLE_NAME = "people"
SAMPLE_IMAGE = "common/icon.png"

# Modules
CONNECTOR_FORMAT = "connectors.{}_connector"
TEST_FORMAT = "tests.{}_test"

# Messages
DB_NAME_FORMAT = "Profiling {db_name}:"
TEST_NAME_FORMAT = "* Running {test_name} test [{count} time(s)]"
CURRENT_RESULTS_FORMAT = "\t\tCurrent results for '{test_name}' [{num}/{total}]: " \
                         "{latest:.2f} ms (AVG {avg:.2f}, MIN {min:.2f}, MAX {max:.2f})"
SUMMERY_FORMAT = "\t> Results for running '{test_name}' {total} time(s): " \
                 "AVG {avg:.2f} ms , MIN {min:.2f} ms, MAX {max:.2f} ms.\n"
