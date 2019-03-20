#!/bin/bash

function init {
    # Creating new swap file with the initial size of 20Mb.
    dd if=/dev/zero of=/swapfile bs=1024 count=20480  # bs - 
    chmod 600 /swapfile  # Only the root user should be able to write and read the file.
    mkswap /swapfile  #  Setting up the file as swap area.
    swapon /swapfile  # Activating the swap file.

    echo '/swapfile swap swap defaults 0 0' >> /etc/fstab  # To activate /swapfile after reboot.
}
