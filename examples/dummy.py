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
    latency = 0

    def steer(self, angle, distance):
        return (angle - distance / 2) / 0.785398

    def gear(self, rpm, gear):
        self.latency += 1

        if not gear:
            return 1, 1
        elif self.latency < 7:
            return gear, 0
        elif rpm < 3000:
            self.latency = 0
            return gear - 1, 1
        elif rpm > 7000:
            self.latency = 0
            return gear + 1, 1

        return gear, 0

    def speed(self, speed, accel):
        if speed < 100:
            accel += 0.1
        else:
            accel -= 0.1

        return accel

    def drive(self, state, control):
        # Control steering, gear and speed.
        control.steering = self.steer(state.angle, state.track_position)
        control.gear, control.clutch = self.gear(state.rpm, state.gear)
        control.accel = self.speed(state.speed_X, control.accel)

        return control


if __name__ == '__main__':
    # Set up default client.
    client = capek.Client(verbosity=2)
    # Run client with `DummyDriver`.
    client.run(driver=DummyDriver, angles=angles)
