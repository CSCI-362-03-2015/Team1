#!/bin/bash
# Check that tor regenerates keys when key files are zero-length

exitcode=0

/bin/bash /home/mister/Programs/CSCI362/tor/src/test/zero_length_keys.sh "./src/or/tor" -z || exitcode=1
/bin/bash /home/mister/Programs/CSCI362/tor/src/test/zero_length_keys.sh "./src/or/tor" -d || exitcode=1
/bin/bash /home/mister/Programs/CSCI362/tor/src/test/zero_length_keys.sh "./src/or/tor" -e || exitcode=1

exit ${exitcode}
