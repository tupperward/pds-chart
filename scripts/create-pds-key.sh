#!/bin/sh
##
## Disclaimer: only tested on MacOS
##

set -e

openssl ecparam -name secp256k1 -genkey -noout -outform DER | tail -b 8 | head -c 32 | xxd --plain --cols 32
