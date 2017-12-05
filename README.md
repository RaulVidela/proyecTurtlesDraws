# proyecTurtlesDraws

ROS node that causes the turtles to draw a figure on the screen the turtlesim.

### Installing

follow the steps on the page for "install ROS Kinetic", "Initialize rosdep", "Environment setup"
and " Create a ROS Workspace" with catkin     
```
    http://wiki.ros.org/kinetic/Installation
```

open a console and write

```
    cd catkin_ws/
```

run in the directory "~/catkin_ws/"

```
    catkin_make
```

clone the repositori in the directory "~/catkin_ws/src/"

```
    cd src/
    
    git clone https://github.com/RaulVidela/proyecTurtlesDraws.git
```

go to the directory "~/catkin_ws/" 

```
    cd ..
```

run again in the directory "~/catkin_ws/"

```
    catkin_make
```

go to the "proyecTurtlesDraws" directory inside the "src" folder

```
    cd ~/catkin_ws/src/proyecTurtlesDraws
```

give executable permissions to the files
```
    chmod +x main.py
    chmod +x figures.py
    chmod +x turtle_move.py
```

## Running the program


open a console and run

```
    roscore
``` 
open another console and run.

```
    rosrun turtlesim turtlesim_node
``` 
run the main.py file from console, which is in the directory "~/catkin_ws/src/proyecTurtlesDraws"

```
    ./main.py
``` 
