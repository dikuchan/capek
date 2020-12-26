#!/usr/bin/env python

import capek
import logging

logging.basicConfig(level=logging.INFO)

# Set sensors on custom angles.
angles = [0 for _ in range(19)]

for i in range(5):
    angles[i] = -90 + i * 15
    angles[18 - i] = 90 - i * 15

for i in range(5, 9):
    angles[i] = -20 + (i - 5) * 5
    angles[18 - i] = 20 - (i - 5) * 5


# Inherit the template `Driver` class.
class DummyDriver(capek.Driver):
    previous_rpm = None

    def steer(self):
        # Get data from `state`.
        angle = self.state.angle
        distance = self.state.track_position

        # Set parameters in `control`.
        self.control.steering = (angle - distance / 2) / 0.785398

    def gear(self):
        rpm = self.state.rpm
        gear = self.state.gear

        if self.previous_rpm is None:
            up = True
        else:
            up = self.previous_rpm - rpm < 0

        if up and rpm > 7000:
            gear += 1
        if not up and rpm < 3000:
            gear -= 1

        self.control.gear = gear

    def speed(self):
        speed = self.state.speed_X
        accel = self.control.accel

        if speed < 100:
            accel += 0.1
        else:
            accel -= 0.1

        self.control.accel = accel

    def drive(self):
        # Control steering, gear and speed.
        # A signal is sent after execution of the method is complete.
        self.steer()
        self.gear()
        self.speed()


if __name__ == '__main__':
    # Set up default client.
    client = capek.Client()
    # Run client with `DummyDriver`.
    client.run(driver=DummyDriver, angles=angles)
