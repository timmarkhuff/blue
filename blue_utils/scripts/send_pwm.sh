#!/usr/bin/env bash

# Send a PWM command to the BlueROV2

ros2 topic pub /mavros/rc/override mavros_msgs/msg/OverrideRCIn "{channels: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}"
