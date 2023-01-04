# config_sh512sum = "70b7935817ca5db239be5763c6e4efbe617ac2230293cdde19d6acb7ef117bd070b5ee03b42ca3c4954e96867c48e54fd7dbedfbcef0945e428f5f879fd8ab2c"
if ! sha512sum --quiet -c sha512sums.txt; then
    cp /home/john/config.txt.backup /boot/config.txt
    reboot
fi
