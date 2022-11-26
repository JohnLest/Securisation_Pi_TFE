#!/bin/sh -e

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

apt-get update
apt-get upgrade -y

apt install busybox cryptsetup initramfs-tools clevis clevis-tpm2 clevis-luks clevis-udisks2 clevis-systemd clevis-initramfs -y

sed -i "s/#dtparam=spi=on/dtparam=spi=on/" /boot/config.txt
sed -i "/\[cm4\]/ i # Load the TPM device tree overlay\ndtoverlay=tpm-slb9670\n" /boot/config.txt

udevadm trigger

reboot