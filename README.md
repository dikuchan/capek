# Čapek

A convenient template for developing TORCS SCR robots.

## Getting started

1. Install TORCS.

   The most convenient way is to install TORCS from [this repository](https://github.com/fmirus/torcs-1.3.7).
   The repository contains the most recent version of the simulator with [SCR](https://arxiv.org/pdf/1304.1672.pdf) 
   patches that allow communicating with TORCS via UDP connection.
   
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
   
3. Program the robot logic.

   Example robots are located in `examples` directory.
   You could launch them to test the library. 

4. Test your robot.

   1. Start TORCS.
   2. Select `Race → Practice → Configure Race → Accept`.
   3. Drop `scr_server 1` to the `Selected` menu.
      This is the bot.
   4. Select `Accept → Accept → New Race`.
   5. Start the robot programed in the previous step.
   
5. Fix, if necessary.

## Creating robots

To create a bot using _Čapek_, you have to re-implement the `Driver` class.
The common structure of a bot is demonstrated below.

```python
from capek import Driver, Client

class MyDriver(Driver):
    def drive(self):
        # ...
        # Define behavior on gear change, steering, etc.
        # ...

        if self.state.speed_X < 300:
            self.control.accel = 1  
        else:
            self.control.accel = 0

        # Changes in control are sent to TORCS on a next tick.

client = Client(verbosity=1)
# Enters loop until reaches maximum learning episodes.
# Or is interrupted.
client.run(driver=MyDriver)
```

The only methods that are supposed to be re-implemented are `drive`, `on_shutdown` and `on_restart`.
The two latter exist because of convention with C++ and Java clients.
