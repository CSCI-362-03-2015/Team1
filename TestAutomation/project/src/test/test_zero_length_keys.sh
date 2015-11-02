#!/bin/sh
# Check that tor regenerates keys when key files are zero-length

exitcode=0

/bin/sh /home/mister/Documents/362/Git/theMonkeyCatfishCoalition/TestAutomation/project/src/test/zero_length_keys.sh "./src/or/tor" -z || exitcode=1
/bin/sh /home/mister/Documents/362/Git/theMonkeyCatfishCoalition/TestAutomation/project/src/test/zero_length_keys.sh "./src/or/tor" -d || exitcode=1
/bin/sh /home/mister/Documents/362/Git/theMonkeyCatfishCoalition/TestAutomation/project/src/test/zero_length_keys.sh "./src/or/tor" -e || exitcode=1

exit ${exitcode}
