#!/bin/bash
# Validate Tor's ntor implementation.

exitcode=0

python /home/mister/Programs/CSCI362/tor/src/test/ntor_ref.py test-tor || exitcode=1
python /home/mister/Programs/CSCI362/tor/src/test/ntor_ref.py self-test || exitcode=1

exit ${exitcode}
