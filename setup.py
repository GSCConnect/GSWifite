from distutils.core import setup

from wifite.config import Configuration

setup(
    name='GSWifite',
    version=Configuration.version,
    author='GSCconnect',
    author_email='admin@gscloudnetwork.com',
    url='https://github.com/GSCConnect/wifite2',
    packages=[
        'wifite',
        'wifite/attack',
        'wifite/model',
        'wifite/tools',
        'wifite/util',
    ],
    data_files=[
        ('share/dict', ['wordlist-top4800-probable.txt'])
    ],
    entry_points={
        'console_scripts': [
            'wifite = wifite.wifite:entry_point'
        ]
    },
    license='GNU GPLv2',
    scripts=['bin/wifite'],
    description='Wireless Network Auditor for Linux',
    #long_description=open('README.md').read(),
    long_description='''Wireless Network Auditor for Linux.
    Crack WEP, WPA, and WPS encrypted networks.
    
    GSWitite is a port from wifite2 written by derv82
    https://github.com/derv82/wifite2
    
    GSWifite looks to improve it's efficiency and update it 
    to todays new security standards and fix bugs.
    
    GSWifite will also include an installer that will make 
    installation effortless on almost any debian based distro.
   
    Packages Required for optimal results:
    
    - Aircrack-ng.
    - Tshark (Wireshark)
    - Reaver.
    - Bully.
    - Pixie WPS.
    - Hashcat.
    - Hcxdumptool (OPTIONAL)
    - Hcxtools (OPTIONAL)
    - Macchanger (OPTIONAL)
    - Pyrit (OPTIONAL)
    ''',
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ]
)
