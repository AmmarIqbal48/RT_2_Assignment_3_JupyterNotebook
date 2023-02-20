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




