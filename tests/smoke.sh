#!/bin/sh -eux

# Create testing iso image
rm -rf ./isocontent
mkdir isocontent
dd if=/dev/zero of=isocontent/big_enough_file  bs=500K  count=1
mkisofs -o test.iso isocontent

# Implant and check md5 sum
implantisomd5 test.iso
checkisomd5 --verbose test.iso

# Destroy testing iso image
rm -rf ./isocontent
rm test.iso
