# dobot


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
import DobotClient as dc
```

## Demo
### Launch the Sample Client
```
rosrun dobot DobotServer Portname
rosrun dobot Dobot_jog.py
```


