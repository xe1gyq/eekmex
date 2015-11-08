#!/usr/bin/python

import logging
import sys
import time
from threading import Thread

class emDemo(object):

    def __init__(self, subsystem):

        logging.info('Demo')
        self.subsystem = subsystem

        self.emDemoSetup()

        #thread = Thread(target=self.emDemoExecute)
        #thread.start()

    def emDemoGps(self):

        from subsystems.emgps import emGps

        self.emgpsfd = emGps()

        latitude = self.emgpsfd.emGpsLatitudeGet()
        longitude = self.emgpsfd.emGpsLongitudeGet()
        altitude = self.emgpsfd.emGpsAltitudeGet()
        gpsdata = ("Gps: {0}," "{1}," "{2}".format( \
                    latitude, longitude, altitude))
        logging.info(gpsdata)

    def emDemoImuSetup(self):

        from subsystems.emimu import emImu

        self.emimu = emImu()

    def emDemoImu(self):

        roll = self.emimu.emImuRollGet()
        pitch = self.emimu.emImuPitchGet()
        yaw = self.emimu.emImuYawGet()
        imudata = ("Imu: {0}," "{1}," "{2},".format(roll, pitch, yaw))
        logging.info(imudata)

    def emDemoSensors(self):

        from sensors.emaltitude import emAltitudeGet
        from sensors.empressure import emPressureGet
        from sensors.emsealevelpressure import emSeaLevelPressureGet
        from sensors.emtemperature import emTemperatureGet

        altitude = emAltitudeGet()
        pressure = emPressureGet()
        sealevelpressure = emSeaLevelPressureGet()
        temperature = emTemperatureGet()
        sensorsdata = ("Sensors: {0}," "{1}," "{2}," "{3}".format( \
                        altitude, pressure, sealevelpressure, temperature))
        logging.info(sensorsdata)

    def emDemoSetup(self):
        if self.subsystem == 'imu':
            self.emDemoImuSetup()

    def emDemoExecute(self):
        if self.subsystem == 'gps':
            self.emDemoGps()
        elif self.subsystem == 'imu':
            self.emDemoImu()
        elif self.subsystem == 'sensors':
            self.emDemoSensors()
        else:
            logging.info('Specific Demo Not Found!')
            sys.exit(1)

# End of File