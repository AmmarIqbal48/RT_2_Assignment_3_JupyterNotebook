[Research Track II](https://corsi.unige.it/en/off.f/2022/ins/60236)<br>
[Ammar Iqbal](https://github.com/ammariqbal48)<br>
[M.Sc Robotics Engineering](https://corsi.unige.it/corsi/10635)<br>
**Professor:** [Prof. Carmine Tommaso Recchiuto](https://rubrica.unige.it/personale/UkNDWV1r)

# Jupyter Notebook User Interface for ROS RVIZ GAZEBO PYTHON


## Abstract
Jupyter Notebook is an open source web application which is used to create and share documents that contain real-time code, equation, data visualizations, text, and so on. This Jupyetr Nootebook is designed to create the User Interface of my code. Also, this notebook is developed as an user interface for the the project Software Architecture for Mobile Robot Control. For this, Jupyter Notebook tool is used.

## Objective
This user interface should be able to control the project ROS RVIZ GAZEBO PYTHON. Also, user can operates and change the robot's behvaiour depending on their choice. Robot's Behvaiour can be autonomous drive, manual drive using teleop, and manual drive using teleop and avoiding the collisions.


## Installation
To create Jupyter Interface, Jupyter Notebook tool is required on your system. To install Jupyter follow the steps given below:

```
pip3 install jupyter bqplot pyyaml ipywidgets
```

```
jupyter nbextension enable --py widgetsnbextension
```
To get started, all you need to do is open up your terminal application and go to a folder of your choice. Then run the below command:
```
jupyter notebook --allow-root
```

Below is the figure which shows Notebook Server.



![Screenshot_20230220_055531](https://user-images.githubusercontent.com/104999107/220174092-e5300b4e-05e9-42b7-aedd-1756934963df.png)


## Jupyter and ROS
Jupyter Notebooks may be used and integrated with ROS called as Jupyter-Ros. As for the other libraries, we need to install some extensions:
```
pip3 install jupyros
```


```
import jupyros as jr
import rospy
from std_msgs.msg import String
rospy.init_node('jupyter_node')
jr.publish('/sometopic', String)
```
This results in a jupyter widget where one can insert the desired message in the text field. The form fields (jupyter widgets) are generated automatically from the message definition. If we use a a different message type, we will get different fields.

ROS3D communicates with ROS via websocket. This communication is configured through the jupyter widgets protocol, but you are also required to run the “rosbridge websocket” package in your ROS environment (or launch file). For this, you need to make sure that you have ros-noetic-rosbridge-suite and ros-noetic-tf2-webrepublisher. Thus, for this example, install:





```
apt-get install ros-noetic-rosbridge-suit
```
```
apt-get install ros-noetic-tf2-web-republisher
```

```
apt-get install ros-noetic-slam-gmapping
```
```
apt-get install ros-noetic-move-base
```
## Description of the Jupyter Code



The Jupyter user interface node is a super easy node. This is used to control the robot's behaviour. This implementation will demonstrates that robot's behavior such as switching to the different modalities such as:

   1) Autonomously reach a x,y coordinate inserted by the user
   2) Letting the user drive the robot with the keyboard
   3) Letting the user drive the robot assisting them to avoid collisions

Additionally, these modalities can also be managed by using this interface.

First, imported the required libraries as given below:



## Import Libraries

```
from ipywidgets import Button, Layout, ButtonStyle, VBox, HBox, GridBox
import ipywidgets as widgets
import rospy
import os
import time
import functools
import numpy as np
from std_msgs.msg import Int32, Bool, String, Float32
from geometry_msgs.msg import Vector3
from actionlib_msgs.msg import GoalStatusArray
from move_base_msgs.msg import MoveBaseActionGoal
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation
import tf
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from tf.transformations import quaternion_matrix

```

## Initialize the node and the buttons for the UI

```
rospy.init_node('jupyter')


b1 = Button(description='First Modality',layout=Layout(width='auto', align="center", grid_area='b1'),style=ButtonStyle(button_color='lightblue'))
b2 = Button(description='Second Modality',layout=Layout(width='auto', grid_area='b2'),style=ButtonStyle(button_color='moccasin'))
b3 = Button(description='Third Modality',layout=Layout(width='auto', grid_area='b3'),style=ButtonStyle(button_color='salmon'))
b4 = Button(description='Quit Modality',layout=Layout(height='auto', grid_area='b4'),style=ButtonStyle(button_color='salmon'))

ok_btn=Button(description='OK',layout=Layout(width='auto', grid_area='ok'),style=ButtonStyle(button_color='salmon'))

#Modality 2 and 3
t1 = Button(description='Left',layout=Layout(width='auto', grid_area='t1'),style=ButtonStyle(button_color='lightblue'))
t2 = Button(description='Forward',layout=Layout(width='auto', grid_area='t2'),style=ButtonStyle(button_color='moccasin'))
t3 = Button(description='Right',layout=Layout(width='auto', grid_area='t3'),style=ButtonStyle(button_color='salmon'))
t4 = Button(description='Stop Motors',layout=Layout(height='auto', grid_area='t4'),style=ButtonStyle(button_color='salmon'))
t11 = Button(description='Front-Left',layout=Layout(width='auto', grid_area='t11'),style=ButtonStyle(button_color='lightblue'))
t12 = Button(description='Front-Right',layout=Layout(width='auto', grid_area='t12'),style=ButtonStyle(button_color='moccasin'))
t13 = Button(description='Back-Left',layout=Layout(width='auto', grid_area='t13'),style=ButtonStyle(button_color='lightblue'))
t14 = Button(description='Back',layout=Layout(width='auto', grid_area='t14'),style=ButtonStyle(button_color='moccasin'))
t15 = Button(description='Back-Right',layout=Layout(width='auto', grid_area='t15'),style=ButtonStyle(button_color='lightblue'))

t5 = Button(description='Left ',layout=Layout(width='auto', align="center", grid_area='t5'),style=ButtonStyle(button_color='lightblue'))
t6 = Button(description='Forward ',layout=Layout(width='auto', grid_area='t6'),style=ButtonStyle(button_color='moccasin'))
t7 = Button(description='Right',layout=Layout(width='auto', grid_area='t7'),style=ButtonStyle(button_color='salmon'))
t8 = Button(description='Stop Motors',layout=Layout(width='auto', grid_area='t8'),style=ButtonStyle(button_color='salmon'))
t21 = Button(description='Front-Left',layout=Layout(width='auto', grid_area='t21'),style=ButtonStyle(button_color='lightblue'))
t22 = Button(description='Front-Right',layout=Layout(width='auto', grid_area='t22'),style=ButtonStyle(button_color='moccasin'))

tdecv=Button(description='Decrease Velocity ',layout=Layout(width='auto', align="center", grid_area='tdecv'),style=ButtonStyle(button_color='lightblue'))
tincv=Button(description='Increase Velocity ',layout=Layout(width='auto', align="center", grid_area='tincv'),style=ButtonStyle(button_color='lightblue'))



mb = {
        'i':(1,0,0,0),
        'o':(1,0,0,-1),
        'j':(0,0,0,1),
        'l':(0,0,0,-1),
        'u':(1,0,0,1),
        ',':(-1,0,0,0),
        '.':(-1,0,0,1),
        'm':(-1,0,0,-1),
        
    }

speed=1.0
incSpeed=1.1
decSpeed=0.9


from teleop import PublishThread
repeat = rospy.get_param("~repeat_rate", 0.0)
pub_thread = PublishThread(repeat)
pub_thread.wait_for_subscribers()
sub = rospy.Subscriber('/scan', LaserScan, clbk_laser) #subscription to /scan topic    

des_pos_x=widgets.FloatText(
    value=0.0,
    description='x coordinate:',
    disabled=False
)
des_pos_y=widgets.FloatText(
    value=0.0,
    description='y coordinate:',
    disabled=False
)
```
## Create publishers for changing the modality and sending goal coordinates
```
pubModality=rospy.Publisher('mode',Int32,queue_size=10) #publisher of 'mode' topic, sends user choice to other nodes
pubGoalPos=rospy.Publisher('goalpos',Vector3,queue_size=10) #publisher of 'goalpos' topic, sends the desired position
x=0.0
y=0.0
goals=[]

```
## Description of the code for the Graphical Representation of the Robot's Odometry & Laser Scanner

This part will demonstrates the graphical representation of the robot's behavior during the Simulation.

   1) The first graph will represents the laser scan on a polar graph representation
   2) The second graph will represents the position described by the odometry topic of the robot. The graph will show the position of the robot in space with red dots.
    

Below is the function shows the plotting of the data of the robot's odometery and laser scanner.

```
colors=[]
x_fromAni=[]
y_fromAni=[]
legend_elements = [Line2D([0], [0],marker='o', color='w', label='Not Achieved: 0',
                          markerfacecolor='r', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Pending',
                          markerfacecolor='y', markersize=10),
                    Line2D([0], [0], marker='o', color='w', label='Achieved: 0',
                          markerfacecolor='g', markersize=10)]

vis = Visualiser(x,y,goals,colors,legend_elements) #instance of Visualiser class
subOdom = rospy.Subscriber('/odom', Odometry, vis.clbk_odom) #subscription to '/odom' topic
subScan = rospy.Subscriber('/scan', LaserScan, vis.clbk_scan) #subscription to '/scan' topic
subStatus=rospy.Subscriber('/move_base/status',GoalStatusArray,vis.clbk_status) #subscription to '/move_base/status' topic
subGoal=rospy.Subscriber('/move_base/goal',MoveBaseActionGoal,vis.clbk_goal) #subscription to '/move_base/goal' topic
```
![Screenshot from 2023-02-20 18-24-35](https://user-images.githubusercontent.com/104999107/220170330-e1acc38e-1939-4175-a180-d3919408de94.png)







![Screenshot from 2023-02-20 18-24-42](https://user-images.githubusercontent.com/104999107/220170160-f4f321fc-09c9-4453-8c8c-8ad4afb1d4cd.png)


## Conclusion and Improvements

I'm satisfied with the final result, even if better improvements can be done. First of all some parameters can be changed since they may be not optimal. Having said that, there are some particular improvenments that I want to highlight:

In jupyter notebook data real time data is updating using %matplotlib widget but at some stage it's lagged and due to this data updation is lagged. This can be improve in further imporvement of the code.

Below are the two improvements which is based on the project Software Architecture for Mobile Robot Control.

1) In the assisted driving mode, the robot avoid obstacles in the front/left/right related to its vision field, but since it can go also backwards it will inevitably crush on the back side, not avoiding the wall. Future improvements can be done, in order to avoid hitting the wall on the back side, probably using the geometry and the space of the environment.
   
2) In the reach point node, we may compute the current position of the robot in the environment and match it to the goal position in order to have an instant feedback if the robot has reached the Point(x,y). The ROS topic base_scan/status takes a long time to control if the robot has reached the goal.



