#!/bin/sh
# Test backtrace functionality.

exitcode=0

./src/test/test-bt-cl assert | python /home/aaron/theMonkeyCatfishCoalition/TestAutomation/project/src/test/bt_test.py || exitcode=1
./src/test/test-bt-cl crash | python /home/aaron/theMonkeyCatfishCoalition/TestAutomation/project/src/test/bt_test.py || exitcode=1

exit ${exitcode}
