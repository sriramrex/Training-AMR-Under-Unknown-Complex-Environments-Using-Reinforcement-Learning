# autonomous-driving-turtlebot-with-reinforcement-learning
Implementation of Q-learning algorithm for the mobile robot (turtlebot3_burger) in ROS.

 * To run the code in gazebo simulator, export the model (burger) and roslaunch turtlebot3_world.launch file.
 * To run the code live on a physical TurtleBot, the ROS_MASTER_URI and ROS_HOSTNAME need to be set via the terminal by editing the ~/.bashrc script.
 * After setting up the environment, rosrun the desired nodes!
 * Link to video: https://drive.google.com/file/d/1tV8Xu_rSkW3aD0BQ_Nik-lein43kujJS/view?usp=sharing


# Content

* [Log_learning ...](Data) -> folder containing data and parameters from the learning phase, as well as the Q-table 
* [scripts](scripts) -> python scripts
    * [Control.py](scripts/Control.py) -> functions for robot control, Odometry message processing and setting robot's initial position
    * [Lidar.py](scripts/Lidar.py) -> functions for Lidar message processing and discretization
    * [Qlearning.py](scripts/Qlearning.py) -> functions for Q-learning algorithm
    * [Plots.py](scripts/Plots.py) -> plotting the data from learning phase and Q-table
    * [scan_node.py](scripts/scan_node.py) -> initializing the node for displaying the Lidar measurements and the current state of the agent
    * [learning_node.py](scripts/learning_node.py) -> initializing the node for learning session
    * [control_node.py](scripts/control_node.py) -> initializing the node for applying the Q-learning algorithm combined with Feedback control
    

This project was inspired from the work that are derived form the the github repository (https://github.com/lukovicaleksa/autonomous-driving-turtlebot-with-reinforcement-learning.git). Because the for the following Q-learning algorithm it is very difficult to estimate a exact hyperparemetes such as ( alpha ,discount factor, epislon ) which are very crucial for the convergence. so we have derived some training parameter which were stated in this repository.