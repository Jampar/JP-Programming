# Import standard Python time library.
import time

# Import GPIO and FT232H modules.
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.FT232H as FT232H

class TurretController:

    halfstep_seq = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]
    ]

    controlPins_1 = [4, 5, 6, 7]
    controlPins_2 = [8, 9, 10, 11]

    displacement = [0,0]

    global ft232h

    def __init__(self):
        # Temporarily disable the built-in FTDI serial driver on Mac & Linux platforms.
        FT232H.use_FT232H()
        # Create an FT232H object that grabs the first available FT232H device found.
        self.ft232h = FT232H.FT232H()

        for pin in self.controlPins_1 + self.controlPins_2:
            self.ft232h.setup(pin, GPIO.OUT)

    def DriveMotor(self,motor_index,steps):

            if motor_index == 0:
                self.displacement[0] += steps
            else:
                self.displacement[1] += steps

            for i in range(abs(steps)):
                if steps < 0:
                    for halfstep in reversed(range(8)):
                        for pin in range(4):

                            if motor_index == 0:
                                self.ft232h.output(self.controlPins_1[pin], self.halfstep_seq[halfstep][pin])
                            else:
                                self.ft232h.output(self.controlPins_2[pin], self.halfstep_seq[halfstep][pin])

                        time.sleep(0.001)

                else:
                    for halfstep in range(8):
                        for pin in range(4):

                            if motor_index == 0:
                                self.ft232h.output(self.controlPins_1[pin], self.halfstep_seq[halfstep][pin])
                            else:
                                self.ft232h.output(self.controlPins_2[pin], self.halfstep_seq[halfstep][pin])

                        time.sleep(0.001)

    def Reset(self):
        self.DriveMotor(0,-self.displacement[0])
        self.DriveMotor(1,-self.displacement[1])




