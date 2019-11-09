#!/usr/bin/python2
import time
from icm20948 import ICM20948

imu = ICM20948()

print("ax,ay,az,gx,gy,gz,mx,my,mz")

def read_all(imu):
    data = imu.read_accelerometer_gyro_data()
    data += imu.read_magnetometer_data()
    ts = time.time()
    line = ""
    for i,x in enumerate(data):
        line+="{:05.2f},".format(x) 
    line+="{0}".format(ts)
    print(line)
    return line

if __name__ == "__main__":
    while True:
        x, y, z = imu.read_magnetometer_data()
        ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()

    #    print("""
    #Accel: {:05.2f} {:05.2f} {:05.2f}
    #Gyro:  {:05.2f} {:05.2f} {:05.2f}
    #Mag:   {:05.2f} {:05.2f} {:05.2f}""".format(
    #        ax, ay, az, gx, gy, gz, x, y, z
    #    ))

        data = [ax,ay,az,gx,gy,gz,x,y,z]

        line = ""
        for i,x in enumerate(data[:-1]):
            line+="{:05.2f},".format(x) 
        line+="{:05.2f}".format(data[-1])
        print(line)

        time.sleep(0.25)
