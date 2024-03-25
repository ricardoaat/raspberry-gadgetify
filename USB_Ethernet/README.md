# Access RaspberryPi throught USB 

1. Add ```dtoverlay=dwc2,dr_mode=peripheral``` at the end of ```/boot/config.txt```
2. Add ```modules-load=dwc2,g_ether``` immediately after ```rootwait``` in ```/boot/cmdline.txt```
3. Install ```sudo apt install dnsmasq -y```
4. Copy ```usb.sh``` to ```/etc/rc.local``` give ```chmod a+x /path/to/script``` permissions. 
5. Reboot


# Not sure if necesary
```
sh /root/usb.sh
```
To /etc/rc.local

/etc/network/interfaces.d/usb0
```
auto usb0
allow-hotplug usb0
iface usb0 inet static
    address 10.55.0.1
    netmask 255.255.255.248
```