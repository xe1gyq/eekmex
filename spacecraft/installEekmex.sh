#!/bin/sh

# Ubilinux

apt-get update
apt-get install gpsd gpsd-clients python-gps libxml2-dev libxslt1-dev python-dev minicom setserial python-matplotlib
pip install numpy psutil XBee pyserial pykml

# Adafruit BMP108 Python
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
python setup.py install

# UPM

wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz
tar xvf cmake-3.2.2.tar.gz
cd cmake-3.2.2
./bootstrap && make && make install

git clone https://github.com/swig/swig.git
./autogen.sh
./configure
make
make install

git clone https://github.com/intel-iot-devkit/upm.git
mkdir build
cd build
cmake .. -DBUILDSWIGNODE=OFF
make
make install

export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages/
mount -o umask=0,uid=nobody /dev/mmcblk1p1 /media/sdcard/

# GPS

gpsd -N -D3 -F /var/run/gpsd.sock /dev/ttyUSB0
gpspipe -w -n 100
gpsmon /dev/ttyUSB1 4800

# End of File
