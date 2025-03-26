from uexplore_interfaces import Event
from uexplore_interfaces import Model
from uexplore_interfaces import Broadcast
from uexplore_interfaces import ControlFlow


def on_start_event():

  Model.mecanum_move_speed_times(Model.Direction.backward,40,2,Model.Unit.second)
Event.register_start(on_start_event)

def on_broadcast_receive():

  ControlFlow.wait(10, ControlFlow.TimeUnit.SECOND)
  Model.mecanum_move_speed_times(Model.Direction.forward,40,1,Model.Unit.second)
  Model.mecanum_move_xyz(40,0,0)
  Model.mecanum_move_speed_times(Model.Direction.forward,40,1,Model.Unit.second)
  Model.mechanical_arms_control(Model.ArmControl.RELEASE)
  Model.mechanical_single_joint_control(Model.Mechanical.joint1,0,400)
  Model.mechanical_arms_control(Model.ArmControl.CLOSE)
  Model.mecanum_move_xyz(0,0,180)
  Model.mecanum_move_speed_times(Model.Direction.forward,40,1,Model.Unit.second)
  Model.mecanum_move_xyz(0,-10,0)
  Model.mecanum_move_speed_times(Model.Direction.forward,40,1,Model.Unit.second)
  Model.mechanical_arms_control(Model.ArmControl.RELEASE)
Event.register_broadcast(on_broadcast_receive, str('0'))

def on_broadcast_receive():

  ControlFlow.wait(10, ControlFlow.TimeUnit.SECOND)
  Model.mecanum_move_speed_times(Model.Direction.forward,40,1,Model.Unit.second)
  Model.mecanum_move_xyz(40,0,0)
  Model.mecanum_move_speed_times(Model.Direction.forward,40,3,Model.Unit.second)
  Model.mechanical_arms_control(Model.ArmControl.RELEASE)
  Model.mechanical_single_joint_control(Model.Mechanical.joint1,0,400)
  Model.mechanical_arms_control(Model.ArmControl.CLOSE)
  Model.mecanum_move_xyz(0,0,180)
  Model.mecanum_move_speed_times(Model.Direction.forward,40,1,Model.Unit.second)
  Model.mecanum_move_xyz(0,10,0)
  Model.mecanum_move_speed_times(Model.Direction.forward,40,1,Model.Unit.second)
  Model.mechanical_arms_control(Model.ArmControl.RELEASE)
Event.register_broadcast(on_broadcast_receive, str('1'))
