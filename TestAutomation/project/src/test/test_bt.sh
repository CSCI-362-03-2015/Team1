#!/bin/bash
# Test backtrace functionality.

exitcode=0

./src/test/test-bt-cl assert | python /home/mister/Programs/CSCI362/tor/src/test/bt_test.py || exitcode=1
./src/test/test-bt-cl crash | python /home/mister/Programs/CSCI362/tor/src/test/bt_test.py || exitcode=1

exit ${exitcode}
