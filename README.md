# Čapek

Python library for developing TORCS racing robots.

## Getting started

1. Install TORCS.

   The most convenient way is to install TORCS from [this repository](https://github.com/fmirus/torcs-1.3.7).
   The repository contains the most recent version of the simulator with [SCR](https://arxiv.org/pdf/1304.1672.pdf) 
   patches that allow communicating with TORCS via UDP.
   
   ```
   $ git clone https://github.com/fmirus/torcs-1.3.7.git
   $ sudo apt-get install libglib2.0-dev libgl1-mesa-dev libglu1-mesa-dev \
        freeglut3-dev libplib-dev libopenal-dev libalut-dev libxi-dev \ 
        libxmu-dev libxrender-dev libxrandr-dev libpng-dev
   $ cd torcs-1.3.7
   $ ./configure
   $ make
   $ sudo make install
   $ sudo make datainstall
   ```

2. Install _Čapek_.

   ```
   $ pip install capek --user
   ```
   
3. Program a robot's logic.

   Reference robots are located in the `examples` directory. 

4. Test the robot.

   1. Start TORCS.
   2. Select `Race → Practice → Configure Race → Accept`.
   3. Drop `scr_server 1` to the `Selected` menu.
      This is the robot.
   4. Select `Accept → Accept → New Race`.
   5. Observe.
   
5. Fix, if necessary.

## Creating robots

To create a robot using _Čapek_, you have to re-implement the `Driver` class.
The common structure of a robot is demonstrated below.

```python
from capek import Driver, Client

class MyDriver(Driver):
    # ...
    # Initialize necessary classes or variables.
    # ...

    def drive(self, state, control):
        # ...
        # Define behavior on gear change, steering, etc.
        # ...

        if state.speed_X < 300:
            control.accel = 1  
        else:
            control.accel = 0

        # Changes in control are sent to TORCS on the next tick.

        return control

client = Client(verbosity=1)
# Enters loop until reaches maximum learning episodes.
# Or is interrupted.
client.run(driver=MyDriver)
```

The only methods that are supposed to be re-implemented are `drive`, `on_shutdown` and `on_restart`.
The two latter exist because of convention with C++ and Java clients.
