BOX_BOT_SIM_PATH=/home/simulations/ros2_sims_ws/install/setup.bash
source $BOX_BOT_SIM_PATH
export GAZEBO_MODEL_PATH=/home/simulations/ros2_sims_ws/src/box_bot/box_bot_gazebo/models:/home/simulations/ros2_sims_ws/src:/home/simulations/ros2_sims_ws/src/box_bot
ros2 launch box_bot_gazebo main_simple.launch.xml