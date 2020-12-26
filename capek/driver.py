from .state import State
from .control import Control


class Driver:
    """
    Base class for a TORCS SCR robot.

    Inherited class should re-implement `drive` method, thus modifying values in `self.control` object on each tick.
    With each tick, `Driver` class update data from sensors in `self.state` object and send `self.control` to TORCS.

    Additionally, `on_shutdown` and `on_restart` could be re-implemented.
    """

    def __init__(self, stage):
        self.stage = stage
        self.state = None
        self.control = Control()

    def tick(self, message: str) -> str:
        # Parse data received from TORCS.
        self.state = State(message=message)

        # Make decisions on driving.
        self.drive()

        # Send decisions back to TORCS.
        return str(self.control)

    def drive(self):
        """
        `self.state` represents the current state of the game as perceived by the driver.
        Method should change `self.control`, which represents the actions taken.
        """
        pass

    def on_shutdown(self):
        """
        Method is called at the end of the race, before unloading of the driver module.
        """
        pass

    def on_restart(self):
        """
        Method is called while the race restarting upon the driver request.
        """
        pass
