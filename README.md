# Training AMR Under Unknown Complex Environments Using Reinforcement Learning

An **Autonomous Mobile Robot (AMR)** navigation project focused on **learning-based control under unknown and complex environments**, using **Reinforcement Learning (RL)** integrated with **ROS, Gazebo, and TurtleBot3**.

---

## Project Motivation

Modern warehouses and industrial facilities increasingly rely on **Autonomous Mobile Robots (AMRs)** for logistics, inspection, and transportation tasks. However, traditional navigation approaches (SLAM + path planning) struggle in **unknown, dynamic, or partially observable environments**.

This project explores **Reinforcement Learning–based control strategies** that allow an AMR to:

* Learn directly from interaction with the environment
* Avoid obstacles without a pre-built map
* Adapt to unknown and complex layouts
* Generalize from simulation to real-world deployment

---

## Core Objectives

* Develop control algorithms for AMRs in **unknown environments**
* Compare **classical navigation** vs **learning-based navigation**
* Train and evaluate **Q-Learning** and **Double Deep Q-Networks (DDQN)**
* Validate policies in **Gazebo simulation** and on a **real TurtleBot3**

---

## ️ System Overview

### Hardware

* **TurtleBot3 Burger**
* 360° **LiDAR sensor** (range limited to ~3.5 m)
* Onboard computer + remote ROS PC

### Software Stack

| Layer      | Tools                        |
| ---------- | ---------------------------- |
| OS         | Ubuntu 20.04 LTS             |
| Middleware | ROS Noetic                   |
| Simulation | Gazebo                       |
| Learning   | Python (Q-Learning, DDQN)    |
| Perception | LiDAR-based state extraction |

---

## ️ Classical Navigation Baseline

Before applying RL, the project reviews traditional approaches:

### ✔ SLAM (GMapping)

* Occupancy grid mapping
* Probabilistic map generation
* Localization using particle filters

### ✔ Path Planning

* Dijkstra-based global planner
* Cost-based path optimization
* Obstacle avoidance with feedback loop

**Limitation:** Requires a map and struggles with unknown or changing environments fileciteturn1file0

---

## Reinforcement Learning Framework

The AMR is trained to navigate **without a map**, relying only on **LiDAR observations** and rewards.

### RL Loop

```text
Observe → Choose Action → Execute → Receive Reward → Update Policy
```

---

## Q-Learning Approach

### State Space

Discrete states derived from LiDAR:

* Left obstacle distance
* Right obstacle distance
* Obstacle position (left / front / right)

➡️ State space reduced to **144 discrete states**

### Action Space (3 actions)

| Action       | Linear / Angular Velocity |
| ------------ | ------------------------- |
| Move Forward | v = 0.08 m/s              |
| Turn Left    | ω = +0.4 rad/s            |
| Turn Right   | ω = -0.4 rad/s            |

---

### Reward Function Design

Reward composed of:

* ✅ Positive reward for forward motion
* ❌ Penalty for turning
* ❌ Heavy penalty for collision
* Large reward for reaching goal

This encourages **smooth, collision-free navigation** fileciteturn1file0

---

### Q-Learning Results

* Gradual increase in cumulative reward
* Decrease in collision frequency
* Stable policy learned within ~400 episodes
* Q-table converges to optimal state-action values

---

## Double Deep Q-Network (DDQN)

To overcome Q-Learning limitations:

* Curse of dimensionality
* Discrete state approximation

### ✔ DDQN Advantages

* Continuous state handling
* Reduced overestimation bias
* Better generalization
* Higher stability

### Network Architecture

* Input: LiDAR-based observations
* Hidden layers: Fully connected (64 neurons)
* Output: Q-values for each action

---

### ⚙ DDQN Hyperparameters

| Parameter         | Value   |
| ----------------- | ------- |
| Episodes          | 10,000  |
| Max steps         | 500,000 |
| Learning rate     | 1e-3    |
| Discount factor γ | 0.99    |
| Replay buffer     | 200,000 |
| Batch size        | 32      |

---

### Training Environments

DDQN trained progressively in:

1. Empty square map
2. Static obstacle map
3. Dense obstacle environment
4. Maze-like layout
5. Dynamic obstacle scenario

This curriculum improves robustness and convergence fileciteturn1file0

---

## Simulation Results

* Smooth obstacle avoidance
* Reduced oscillatory behavior
* Faster convergence than Q-Learning
* Stable navigation in unseen layouts

---

## Real-World Deployment

The trained policy was deployed on a **real TurtleBot3**:

* ROS master–slave configuration
* LiDAR-based perception
* Real-time velocity command publishing

✔ Robot successfully navigates unknown indoor environment
✔ No collisions observed during test runs

---

## ⚠️ Limitations

| Issue          | Description                  |
| -------------- | ---------------------------- |
| LiDAR range    | Limited sensing distance     |
| Discretization | Q-Learning state abstraction |
| Training time  | High computational cost      |

---

## Future Work

* Multi-robot cooperative learning
* Continuous action RL (PPO, SAC)
* Vision + LiDAR sensor fusion
* Domain randomization for sim-to-real transfer
* Online learning in dynamic environments

---

## Suggested Repository Structure

```text
├── rl/
│   ├── q_learning/
│   ├── ddqn/
├── ros_ws/
│   ├── turtlebot3_navigation/
│   ├── training_nodes/
├── simulation/
│   ├── gazebo_worlds/
├── docs/
│   ├── figures/
│   ├── report.pdf
├── README.md
```

---

## References

* Sutton & Barto – Reinforcement Learning
* ROS Navigation Stack
* TurtleBot3 Documentation
* DeepMind DQN & DDQN

---

## ‍ Author

**Training AMR Under Unknown Complex Environments Using Reinforcement Learning**
Academic Robotics & AI Project

---

⭐ *This project demonstrates learning-based autonomy beyond classical navigation.*
