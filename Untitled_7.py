from uexplore_interfaces import Event
from uexplore_interfaces import Device
from uexplore_interfaces import Color
from uexplore_interfaces import Math
from uexplore_interfaces import Utils
from uexplore_interfaces import Model
from uexplore_interfaces import Motion
from uexplore_interfaces import Joypad
from uexplore_interfaces import ControlFlow

var__E6_88_91_E7_9A_84_E5_8F_98_E9_87_8F = 0
var__E8_B7_9D_E7_A6_BB = 0
var__E5_81_8F_E7_A7_BB = 0
var_i = 0
var_j = 0
var_flag = 0
var_flag_E5_B0_8F_E7_90_83 = 0
list_list__E6_89_80_E6_9C_89_E5_B0_8F_E7_90_83 = []
list_list__E4_B8_80_E4_B8_AA_E5_B0_8F_E7_90_83 = []


def on_start_event():
  global var_flag

  var_flag = '0'
  Device.show_light_hsv([Device.Light.ID.TOP,Device.Light.ID.DOWN], Color.create_color_hsv(65,66,100))
  while True:
      while (not (Math.equal(Utils.parseToNumber(var_flag), 0))):
          Model.mecanum_stop()
          Motion.turn_servo_speed(51,(Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.RX) / 25))
          Motion.turn_servo_speed(52,(Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.LY) / -21))
          Motion.turn_servo_speed(53,(Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.RY) / 20))
          Model.mecanum_stop()

      Model.mecanum_move_xyz((Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.LX) / 5),(Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.LY) / 5),(Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.RX) / -3))

Event.register_start(on_start_event)

def on_joystick_keys_click_event():

  Model.run_mechanical_motion([({1:90,2:-23,3:49},600)])
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.Y])

def on_joystick_keys_click_event():

  Model.run_mechanical_motion([({1:90,2:-32,3:-45},600)])
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.B])

def on_joystick_keys_click_event():

  if (Model.mechanical_check_arm_status(Model.ArmControl.RELEASE)):
      Model.mechanical_arms_control(Model.ArmControl.CLOSE)
  else:
      Model.mechanical_arms_control(Model.ArmControl.RELEASE)
  ControlFlow.wait(600, ControlFlow.TimeUnit.MILLISECOND)
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.A])

def on_joystick_keys_click_event():

  Model.run_mechanical_motion([({1:90,2:-97,3:-23},600),({1:90,2:-144,3:-61},300)])
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.X])

def on_joystick_keys_click_event():

  Model.run_mechanical_motion([({1:90,2:-64,3:-19},600),({1:90,2:-74,3:-23},200)])
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.UP])

def on_joystick_keys_click_event():

  Model.run_mechanical_motion([({1:90,2:-23,3:22},600)])
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.DOWN])

def on_joystick_keys_click_event():
  global var_flag

  var_flag = '0'
  Device.show_light_hsv([Device.Light.ID.TOP,Device.Light.ID.DOWN], Color.create_color_hsv(65,100,100))
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.R2])

def on_joystick_keys_click_event():
  global var_flag

  var_flag = '1'
  Device.show_light_hsv([Device.Light.ID.TOP,Device.Light.ID.DOWN], Color.create_color_hsv(0,100,100))
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.L2])

Export
Normal readout
large readout
slider
Export
Normal readout
large readout
slider
Normal readout
large readout
slider
Normal readout
large readout
slider