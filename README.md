# dobot

## Install

```
cd ~/catkin_ws/src
git clone https://github.com/shuto1441/dobot.git
cd ../
catkin build
```
## Usage
### Look up the Dobot Magician serial port name

```
ls /dev -l
```
### Start ROS

```
roscore
```

### Launch the Server
DobotServer.cpp is required to run dobot's server.
Please rewrite the port name.
```
rosrun dobot DobotServer Portname
```
### Writing a Client
Functions for running dobot on client are organized in DobotClient.py.
Import DobotClient.py to create a client
```
import sys
LIBPATH = "../../dobot/src"
sys.path.append(LIBPATH)
import DobotClient as dc
```

## Demo
### Launch the Sample Python Code 
```
rosrun dobot DobotServer Portname
rosrun dobot DobotClient_JOG.py
```

### Launch the Sample C++ Code 
```
rosrun dobot DobotServer Portname
rosrun dobot DobotClient_JOG
```
```
rosrun dobot DobotServer Portname
rosrun dobot DobotClient_PTP
```

