# db_profiler
Dynamic DB profiling and performance-testing tool that i made.

## Synopsis
This tool is used to easily profile the DB of your choise with easily costumisable tests.
It consists of two main modules:
 * Connectors - wrapper for the connector  DB library and basic functionality for each DB
 * Tests - performance test that mesure the DB execution length
You can easily write your own custom connectors and tests.

## Running
    usage: profile_db_performance.py dbs [dbs ...] [-t TESTS [TESTS ...]] [-c COUNT] [--verbose]
                                 
    positional arguments:
      dbs                   DB connector to use for the tests

    optional arguments:
      -t TESTS [TESTS ...], --tests TESTS [TESTS ...]
                        Tests to preform.
      -c COUNT, --count COUNT
                        How many times to repeat each test.
      --verbose             Display result for each test.
      
      Notes:
       * If no TEST or COUNT are given, the default is set by the settings in const.py
       * Non-verbose mode shows only the DB that's being currently profiled and the final results for each test  
 
## Currently implemented
 * Connectors - MongoDB, ZODB, SQLAlchemy (configured for MySQL)
 * Tests:
    * read - Setup 2,000 records, read 1,000 recods by randomly generated IDs
    * write - write 1,000 new records with randomly generated data
    * update - Setup 2,000 records, update 1,000 recods by randomly generated IDs with randomly generated data
 
## Known bugs and problems
 * ***"Invalid utf8mb4 chatacter"* Warning message** - A bug in the PyMySQL library caused by using a BLOB field in the tests
 * **General slow execution of test setups and cleanups** - Yet to be resolved
 * **SQLAlchemy module can't handle sudden test termination** - Yet to be resolved
