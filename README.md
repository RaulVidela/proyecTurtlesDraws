# proyecTurtlesDraws

ROS node that causes the turtles to draw a figure on the screen the turtlesim.

### Installing

follow the steps on the page for "install ROS Kinetic", "Initialize rosdep" and "Environment setup"
    
```
      http://wiki.ros.org/kinetic/Installation
```

open a console and write

```
cd catkin_ws/
```

run

```
catkin_make
```

clone the repositori in the directory "~/catkin_ws/src/"

```
    cd src/
    
    git clone git@github.com:RaulVidela/proyecTurtlesDraws.git
```

run again

```
    catkin_make
```

go to the "src" directory inside the "turlte_drsw" folder

```
    cd turtle_draw/src/
```

give executable permissions to the files
```
    chmod +x main.py
    chmod +x figures.py
    chmod +x turtle_move.py
```

## Running the program

run the main.py file, which is in the directory "~/catkin_ws/src/turtle_draw/src/"

```
    ./main.py
``` 
