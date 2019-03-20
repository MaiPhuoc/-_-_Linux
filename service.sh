#!/bin/bash

function expand {
    echo 'Expanding swap area...'  #  This should be registred by logger.

    newfile='/swapfile'$1
    dd if=/dev/zero of=$newfile bs=1024 count=$1 #  Creating new swap file to double swap area.
    chmod 600 $newfile  # Only the root user should be able to write and read the file.
    mkswap $newfile  #  Setting up the file as swap area.
    swapon $newfile  # Activating the swap file.

    echo $newfile 'swap swap defaults 0 0' >> /etc/fstab  # To activate new swapfile after reboot.

}

function check {

    swap=$(free -b | grep 'Swap' | tr -s ' ')
    swapsize=$($swap | cut -d' ' -f1)
    freesize=$($swap | cut -d' ' -f2)

    if (( freesize > (swapsize / 2) ))
    then
        expand swapsize
    fi
}

while true
do 
    check
    sleep 30 &
    wait
done