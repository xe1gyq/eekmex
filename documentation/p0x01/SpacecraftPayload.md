Payload
==

## Gpsd Daemon

> gpsd is a service daemon that monitors one or more GPSes or AIS receivers attached to a host computer through serial or USB ports, making all data on the location/course/velocity of the sensors available

- [GPSD Homepage](http://www.catb.org/gpsd/)
- [1](http://stackoverflow.com/questions/28511485/how-to-write-this-in-python)

```sh
    root@spacecraft:~# dmesg
    [  514.492900] usb 1-1: reset full-speed USB device number 2 using dwc3-host
    [  514.513505] dwc3-host dwc3-host.2: xHCI xhci_drop_endpoint called with disabled ep f5626500
    [  514.513566] usb 1-1: ep 0x81 - rounding interval to 1024 microframes, ep desc says 2040 microframes
    [  514.922543] usb 1-1.2: new full-speed USB device number 3 using dwc3-host
    [  514.953097] usb 1-1.2: New USB device found, idVendor=0403, idProduct=6001
    [  514.953128] usb 1-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [  514.953149] usb 1-1.2: Product: FT232R USB UART
    [  514.953168] usb 1-1.2: Manufacturer: FTDI
    [  514.953186] usb 1-1.2: SerialNumber: A60442H3
    [  514.959035] ftdi_sio 1-1.2:1.0: FTDI USB Serial Device converter detected
    [  514.959298] usb 1-1.2: Detected FT232RL
    [  514.959322] usb 1-1.2: Number of endpoints 2
    [  514.959341] usb 1-1.2: Endpoint 1 MaxPacketSize 64
    [  514.959360] usb 1-1.2: Endpoint 2 MaxPacketSize 64
    [  514.959378] usb 1-1.2: Setting MaxPacketSize 64
    [  514.960259] usb 1-1.2: FTDI USB Serial Device conerverter now attached to ttyUSB0
    root@spacecraft:~# gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
    root@spacecraft:~# cgps -s
    lqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqklqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqk
    x    Time:       2011-11-13T00:00:39.090Z   xxPRN:   Elev:  Azim:  SNR:  Used: x
    x    Latitude:   n/a                        xx                                 x
    x    Longitude:  n/a                        xx                                 x
    x    Altitude:   n/a                        xx                                 x
    x    Speed:      n/a                        xx                                 x
    x    Heading:    n/a                        xx                                 x
    x    Climb:      n/a                        xx                                 x
    x    Status:     NO FIX (15 secs)           xx                                 x
    x    Longitude Err:   n/a                   xx                                 x
    x    Latitude Err:    n/a                   xx                                 x
    x    Altitude Err:    n/a                   xx                                 x
    x    Course Err:      n/a                   xx                                 x
    x    Speed Err:       n/a                   xx                                 x
    x    Time offset:     124046999.723         xx                                 x
    x    Grid Square:     n/a                   xx                                 x
    mqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqjmqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqj
    root@spacecraft:~# gpscat -s [baudrate] [serial_port]
```

```sh
      print
      print ' GPS reading'
      print '----------------------------------------'
      print 'latitude    ' , gpsd.fix.latitude
      print 'longitude   ' , gpsd.fix.longitude
      print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
      print 'altitude (m)' , gpsd.fix.altitude
      print 'eps         ' , gpsd.fix.eps
      print 'epx         ' , gpsd.fix.epx
      print 'epv         ' , gpsd.fix.epv
      print 'ept         ' , gpsd.fix.ept
      print 'speed (m/s) ' , gpsd.fix.speed
      print 'climb       ' , gpsd.fix.climb
      print 'track       ' , gpsd.fix.track
      print 'mode        ' , gpsd.fix.mode
      print
      print 'sats        ' , gpsd.satellites

    latitude = gpsc.fix.latitude
    longitude = gpsc.fix.longitude
    timeUTC = gpsc.utc
    timeFIX = gpsc.fix.time
    altitudeGPS = gpsc.fix.altitude
    eps = gpsc.fix.eps #Speed error estimate in meter/sec
    epx = gpsc.fix.epx #Estimated Longitude error in meters
    epv = gpsc.fix.epv #Estimated vertical error in meters
    ept = gpsc.gpsd.fix.ept #Estimated timestamp error
    speed = gpsc.fix.speed
    climb = gpsc.fix.climb #Climb (positive) or sink (negative rate, meters per second
    track = gpsc.fix.track #Course over ground, degrees from true north
    mode = gpsc.fix.mode #NMEA mode: %d, 0=no mode value yet seen, 1=no fix, 2=2D, 3=3D
    satellites = len(gpsc.satellites)
```

## Simulator

> Simulator Definition

## PreRequisites

```sh
    Debian GNU/Linux 8 eekmex tty1

    eekmex login: eekmex
    Password: eekmex
    ...
    eekmex@eekmex:~$ su
    Password: edison
    eekmex@eekmex:/home/eekmex# cd
    eekmex@eekmex:/home/eekmex# apt-get update
    eekmex@eekmex:/home/eekmex# apt-get install python-pip
    eekmex@eekmex:/home/eekmex# apt-get install git build-essential python-dev swig libtool zlib1g-dev
    eekmex@eekmex:/home/eekmex# apt-get install python-smbus lm-sensors
    eekmex@eekmex:/home/eekmex# apt-get install gpsd gpsd-clients python-gps libxml2-dev libxslt1-dev
    eekmex@eekmex:/home/eekmex# pip install dweepy RandomWords LoremIpsum
```

## General Sensors

  - Temperature
  - Pressure
  - Sea Level Pressure
  - Altitude

```sh
    root@ubilinux:/home/edison# cd eekmex/spacecraft
    root@ubilinux:/home/edison/eekmex/spacecraft# python eekmex.py -d all
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Demo
    root: emvirtual  INFO Virtual
    root: emsensors  INFO Sensors
    root: emsensors  INFO Sensors: 2839,1586,1603,29
    ...
```

## Position (Global Positioning System)

  - Latitude
  - Longitude
  - Altitude
  - Satellites
  - Speed
  - Track

```sh
    root@eekmex:/home/eekmex/eekmex/spacecraft# python eekmex.py -d all
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Virtual
    root: emvirtual  INFO Virtual
    root: emgps      INFO Global Positioning System
    root: emgps      INFO Gps: 21.1640478895,-101.613045967,1828, 7, 31, 320
    ...
```

 - [1](https://github.com/martinohanlon/vidGPSOverlay/blob/master/GPSController.py)

## Attitude (Inertial Measurement Unit)

> LSM9DS0 9DOF IMU for full-range motion sensing. This chip combines a 3-axis accelerometer, a 3-axis gyroscope, and a 3-axis magnetometer.

- Roll
- Pitch
- Yaw

```sh
    root@eekmex:/home/eekmex/eekmex/spacecraft# python eekmex.py -d all
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Demo
    root: emvirtual  INFO Virtual
    root: emimu      INFO Inertial Measurement Unit
    root: emimu      INFO Imu: -153,64,39
    ...
```