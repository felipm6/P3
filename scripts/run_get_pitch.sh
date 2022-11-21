#!/bin/bash

# Put here the program (maybe with path)
umaxnorm=${1:+-m${1}}
unorm=${2:+-u${2}}
pot1=${3:+-p${3}}

GETF0="get_pitch $umaxnorm $unorm $pot1"

for fwav in pitch_db/train/*.wav; do
    ff0=${fwav/.wav/.f0}
    echo "$GETF0 $fwav $ff0 ----"
    $GETF0 $fwav $ff0 > /dev/null || (echo "Error in $GETF0 $fwav $ff0"; exit 1)
done

exit 0