#!/bin/sh
# Validate Tor's ntor implementation.

exitcode=0

python /home/mister/Documents/362/Git/theMonkeyCatfishCoalition/TestAutomation/project/src/test/ntor_ref.py test-tor || exitcode=1
python /home/mister/Documents/362/Git/theMonkeyCatfishCoalition/TestAutomation/project/src/test/ntor_ref.py self-test || exitcode=1

exit ${exitcode}
