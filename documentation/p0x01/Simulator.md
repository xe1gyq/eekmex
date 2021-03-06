Simulator
==

We will work in our Linux Debian based Personal Computer to have a Spacecraft simulated

## PreRequisites

    Debian GNU/Linux 8 eekmex tty1

    eekmex login: eekmex
    Password: eekmex
    ...
    eekmex@eekmex:~$ su
    Password: edison
    eekmex@eekmex:/home/eekmex# cd
    root@ubilinux:~# apt-get update
    root@ubilinux:~# apt-get install python-pip
    root@ubilinux:~# apt-get install git build-essential python-dev swig libtool zlib1g-dev
    root@ubilinux:~# apt-get install python-smbus lm-sensors
    root@ubilinux:~# apt-get install gpsd gpsd-clients python-gps libxml2-dev libxslt1-dev

## Simulator Base Code

    eekmex@eekmex:~$ git clone https://github.com/xe1gyq/eekmex.git
    Cloning into 'eekmex'...
    remote: Counting objects: 3542, done.
    remote: Compressing objects: 100% (88/88), done.
    remote: Total 3542 (delta 52), reused 0 (delta 0), pack-reused 3451
    Receiving objects: 100% (3542/3542), 325.81 KiB | 377.00 KiB/s, done.
    Resolving deltas: 100% (2404/2404), done.
    Checking connectivity... done.
    eekmex@eekmex:~$ cd eekmex
    eekmex@eekmex:~/eekmex$ ls
    documentation  eekmex  LICENSE  README.md  sandbox  simulator  SUMMARY.md  training
    eekmex@eekmex:~/eekmex$ cd simulator

### Simulator Clean

    eekmex@eekmex:~/eekmex/simulator$ python eekmex.py -c files
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Clean Up, Remove Files

### Simulator Demo IMU

    eekmex@eekmex:~/eekmex/simulator$ python eekmex.py -d imu
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Demo
    root: emdemo     INFO Demo
    root: emimu      INFO Inertial Measurement Unit
    root: emimu      INFO IMU Simulator
    root: emimu      INFO IMU Initialization Succeeded!
    root: emdemo     INFO Imu: 12,54,26,
    root: emdemo     INFO Imu: 4,110,176,
    root: emdemo     INFO Imu: 35,16,18,
    root: emdemo     INFO Imu: 111,62,126,
    root: emdemo     INFO Imu: 65,127,68,
    root: emdemo     INFO Imu: 64,110,144,
    root: emdemo     INFO Imu: 130,99,91,
    ...
    ...
    ^Z
    eekmex@eekmex:~/eekmex/simulator$ 

## Simulator Demo GPS

    eekmex@eekmex:~/eekmex/simulator$ python eekmex.py -d gps
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Demo
    root: emdemo     INFO Demo
    root: emgps      INFO Global Positioning System
    root: emdemo     INFO Gps: 0.0,0.0,nan
    root: emdemo     INFO Gps: 0.0,0.0,nan
    ...
    ...
    ^Z
    eekmex@eekmex:~/eekmex/simulator$ 

### Simulator Demo Sensors

    eekmex@eekmex:~/eekmex/simulator$ python eekmex.py -d sensors
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Demo
    root: emdemo     INFO Demo
    root: emaltitude INFO Altitude 2020
    root: empressure INFO Pressure 1484
    root: emsealevelpressure INFO Sea Level Pressure 1900
    root: emtemperature INFO Temperature 40
    root: emdemo     INFO Sensors: 2020,1484,1900,40
    ...
    ...
    ^Z
    eekmex@eekmex:~/eekmex/simulator$ 