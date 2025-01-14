GSWifite
======

This repo is a complete re-write of [`wifite2`](https://github.com/derv82/wifite2), a Python script for auditing wireless networks.

GSWifite is an updated version of Wifite2, since it hasn't been updated since 2018... Some of the processes were improved and a few other
bug fixes. This software serves the purpose of auditing YOUR OWN NETWORKS to see if they are secure against attackers. DO NOT use this on 
networks that you don't have permission to audit. 

GSWifite is designed to use all known methods for retrieving the password of a wireless access point (router).  

These methods include:

1. WPS: The [Offline Pixie-Dust attack](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Offline_brute-force_attack)
1. WPS: The [Online Brute-Force PIN attack](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Online_brute-force_attack)
2. WPA: The [WPA Handshake Capture](https://hashcat.net/forum/thread-7717.html) + offline crack.
3. WPA: The [PMKID Hash Capture](https://hashcat.net/forum/thread-7717.html) + offline crack.
4. WEP: Various known attacks against WEP, including *fragmentation*, *chop-chop*, *aireplay*, etc.

## GSWifite Workflow

1- Run gswifite. <br>
2- Choose Wireless Card to use. <br>
3- Scan the area for networks. <br>
4- Select your targets. <br>
5- Run the attack. <br>

Supported Operating Systems
---------------------------
GSWifite runs under almost any linux distro, however I have only tested this on debian based distros like:

- Linux MX
- Raspian OS
- Ubuntu
- Zorin OS
- Kali
- Parrot OS

To make this as easy as possible to use, I have prepared a script that will install all dependencies on debian based distros.
Script required little to no input from the user.**God Bless Bash.**

Requirements
--------------
First and foremost, you will need a wireless card capable of "Monitor Mode" and packet injection (see [this tutorial for checking if your wireless card is compatible](http://www.aircrack-ng.org/doku.php?id=compatible_cards) and also [this guide](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Offline_brute-force_attack)). There are many cheap wireless cards that plug into USB available from online stores.

I recommend using any ALFA Wireless Card or TP-Link Archer C6 (RTL8812au) 


**Packages Required:**

* `python3`: GSWifite will not support python2, but it may still work with it.
* [`iwconfig`](https://wiki.debian.org/iwconfig): For identifying wireless devices already in Monitor Mode.
* [`ifconfig`](https://en.wikipedia.org/wiki/Ifconfig): For starting/stopping wireless devices.
* [`Aircrack-ng`](http://aircrack-ng.org/) suite, includes:
   * [`airmon-ng`](https://tools.kali.org/wireless-attacks/airmon-ng): For enumerating and enabling Monitor Mode on wireless devices.
   * [`aircrack-ng`](https://tools.kali.org/wireless-attacks/aircrack-ng): For cracking WEP .cap files and WPA handshake captures.
   * [`aireplay-ng`](https://tools.kali.org/wireless-attacks/aireplay-ng): For deauthing access points, replaying capture files, various WEP attacks.
   * [`airodump-ng`](https://tools.kali.org/wireless-attacks/airodump-ng): For target scanning & capture file generation.
   * [`packetforge-ng`](https://tools.kali.org/wireless-attacks/packetforge-ng): For forging capture files.

**Optional, but Recommended:**

* [`tshark`](https://www.wireshark.org/docs/man-pages/tshark.html): For detecting WPS networks and inspecting handshake capture files.
* [`reaver`](https://github.com/t6x/reaver-wps-fork-t6x): For WPS Pixie-Dust & brute-force attacks.
   * Note: Reaver's `wash` tool can be used to detect WPS networks if `tshark` is not found.
* [`bully`](https://github.com/aanarchyy/bully): For WPS Pixie-Dust & brute-force attacks.
   * Alternative to Reaver. Specify `--bully` to use Bully instead of Reaver.
   * Bully is also used to fetch PSK if `reaver` cannot after cracking WPS PIN.
* [`coWPAtty`](https://tools.kali.org/wireless-attacks/cowpatty): For detecting handshake captures.
* [`pyrit`](https://github.com/JPaulMora/Pyrit): For detecting handshake captures.
* [`hashcat`](https://hashcat.net/): For cracking PMKID hashes.
   * [`hcxdumptool`](https://github.com/ZerBea/hcxdumptool): For capturing PMKID hashes.
   * [`hcxpcaptool`](https://github.com/ZerBea/hcxtools): For converting PMKID packet captures into `hashcat`'s format.


Run GSWifite
----------
```
git clone https://github.com/GSCConnect/GSWifite.git
cd GSWifite
sudo ./GSWifite.py
```

Install GSWifite
--------------
To install onto your computer (so you can just run `GSwifite` from any terminal), run:

```bash
sudo python setup.py install
```

This will install `GSWifite` to `/usr/sbin/wifite` which should be in your terminal path.

**Note:** Uninstalling is [not as easy](https://stackoverflow.com/questions/1550226/python-setup-py-uninstall#1550235). The only way to uninstall is to record the files installed by the above command and *remove* those files:

```bash
sudo python setup.py install --record files.txt \
  && cat files.txt | xargs sudo rm \
  && rm -f files.txt
```

Brief Feature List
------------------
* [PMKID hash capture](https://hashcat.net/forum/thread-7717.html) (enabled by-default, force with: `--pmkid`)
* WPS Offline Brute-Force Attack aka "Pixie-Dust". (enabled by-default, force with: `--wps-only --pixie`)
* WPS Online Brute-Force Attack aka "PIN attack". (enabled by-default, force with: `--wps-only --no-pixie`)
* WPA/2 Offline Brute-Force Attack via 4-Way Handshake capture (enabled by-default, force with: `--no-wps`)
* Validates handshakes against `pyrit`, `tshark`, `cowpatty`, and `aircrack-ng` (when available)
* Various WEP attacks (replay, chopchop, fragment, hirte, p0841, caffe-latte)
* Automatically decloaks hidden access points while scanning or attacking.
   * Note: Only works when channel is fixed. Use `-c <channel>`
   * Disable this using `--no-deauths`
* 5Ghz support for some wireless cards (via `-5` switch).
   * Note: Some tools don't play well on 5GHz channels (e.g. `aireplay-ng`)
* Stores cracked passwords and handshakes to the current directory (`--cracked`)
   * Includes information about the cracked access point (Name, BSSID, Date, etc).
* Easy to try to crack handshakes or PMKID hashes against a wordlist (`--crack`)

What's new?
-----------
Comparing this repo to the "old wifite" @ https://github.com/derv82/wifite2

TO BE UPDATED SOON. :)

What's not new?
---------------
* (Mostly) Backwards compatible with the original `wifite`'s arguments.
* Same text-based interface everyone knows and loves.

Screenshots
-----------
Cracking WPS PIN using `reaver`'s Pixie-Dust attack, then fetching WPA key using `bully`:
![Pixie-Dust with Reaver to get PIN and Bully to get PSK](https://i.imgur.com/Q5KSDbg.gif)

-------------

Cracking WPA key using PMKID attack:
![PMKID attack](https://i.imgur.com/CR8oOp0.gif)

-------------

Decloaking & cracking a hidden access point (via the WPA Handshake attack):
![Decloaking and Cracking a hidden access point](https://i.imgur.com/F6VPhbm.gif)

-------------

Cracking a weak WEP password (using the WEP Replay attack):
![Cracking a weak WEP password](https://i.imgur.com/jP72rVo.gif)

-------------

Cracking a pre-captured handshake using John The Ripper (via the `--crack` option):
![--crack option](https://i.imgur.com/iHcfCjp.gif)
