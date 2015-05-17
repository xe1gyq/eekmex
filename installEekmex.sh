#!/bin/sh

apt-get update
pip install numpy psutil

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

# End of File
