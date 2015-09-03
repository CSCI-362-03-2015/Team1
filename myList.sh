#!/bin/bash
#This script displays the contents of a directory. written by themonkeycatfishcoalition
touch test.html
echo "<html><body><ul>" >> test.html
ls>>test.html
echo "</ul></body></html>" >> test.html
see test.html
exit 0
