# Cpu_taker





This requires Python and Pygame 
Running this file will take up lot of cpu but your os will lagging depending on your device

How it works:

    1. It uses threading to do the trick
    2. that thread plays a sound using pygame mxer
    3. when a thread finished playing a sound or still playing a sound it will trigger another thread. causing to multiply
    4. Before threads run a while loop triggers thread cause to create lot of thread and so on
    5. when executing for long time your os is sill running fine but this will lag a lot and sometimes it freezes it depending on your device

Is this crash your os:
Depending on your device.
if your device is low end. There is a chance you device will restart because your os crashed
if your device is high end. Then it will not crash your os 
