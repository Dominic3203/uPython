from uexplore_interfaces import Event
from uexplore_interfaces import PidControl
from uexplore_interfaces import Device
from uexplore_interfaces import Color
from uexplore_interfaces import Math
from uexplore_interfaces import Utils
from uexplore_interfaces import Motion
from uexplore_interfaces import Joypad
import math
from uexplore_interfaces import ControlFlow

var__E6_88_91_E7_9A_84_E5_8F_98_E9_87_8F = 0
var__E9_80_9F_E7_8E_87 = 0
var___E9_80_9F_E7_8E_87 = 0
var_flag = 0
var_negSpeed = 0
var_posSpeed = 0

ubt_Pid_E6_97_8B_E8_BD_AC = PidControl()

ubt_Pid_Throw = PidControl()

ubt_Pid_unnamed = PidControl()

ubt_Pid_Rotate = PidControl()

def func_Rotate(var_v):
  global var_posSpeed

  ubt_Pid_Rotate.update(((var_v / 2)))
  var_posSpeed = ubt_Pid_Rotate.get_output()
  Motion.turn_motor_speed(0,Utils.parseToNumber(var_posSpeed))
  Motion.turn_motor_speed(0,Utils.parseToNumber(var_posSpeed))
  Motion.turn_motor_speed(0,Utils.parseToNumber(var_posSpeed))
  Motion.turn_motor_speed(0,Utils.parseToNumber(var_posSpeed))

def func_upDown(var_v):
  global var_posSpeed,var_negSpeed

  ubt_Pid_Rotate.update(var_v)
  var_posSpeed = ubt_Pid_Rotate.get_output()
  var_negSpeed = (Utils.parseToNumber(var_posSpeed) * -1)
  Motion.turn_motor_speed(0,Utils.parseToNumber(var_posSpeed))
  Motion.turn_motor_speed(0,Utils.parseToNumber(var_negSpeed))
  Motion.turn_motor_speed(0,Utils.parseToNumber(var_posSpeed))
  Motion.turn_motor_speed(0,Utils.parseToNumber(var_negSpeed))


def on_start_event():
  global var_flag

  ubt_Pid_E6_97_8B_E8_BD_AC.set_pid(0.7,0,0.0001)
  var_flag = '0'
  Device.show_light_hsv([Device.Light.ID.TOP,Device.Light.ID.DOWN], Color.create_color_hsv(66,100,100))
  while True:
      if (Math.equal(Utils.parseToNumber(var_flag), 1)):
          while (not (Math.equal(Utils.parseToNumber(var_flag), 0))):
              Motion.turn_servo_speed(21,(Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.RX) / 20))

      else:
          while (not (Math.notEqual((Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.RX)), 0))):
              func_upDown(Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.LY))
              if (Math.equal(Utils.parseToNumber(var_flag), 1)):
                  break


          while (not (Math.notEqual((Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.LY)), 0))):
              func_Rotate(Joypad.get_joypad_coordinate(Joypad.JoystickCoordinate.RX))
              if (Math.equal(Utils.parseToNumber(var_flag), 1)):
                  break



Event.register_start(on_start_event)

def on_joystick_keys_click_event():

  Motion.turn_servo_angle(11,-75,600,False)
  Motion.turn_servo_angle(41,-75,600,False)
  Motion.turn_servo_angle(61,75,600,False)
  Motion.turn_servo_angle(31,75,600,False)
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.L1])

def on_joystick_keys_click_event():

  Motion.turn_servo_angle(11,-25,600,False)
  Motion.turn_servo_angle(41,-25,600,False)
  Motion.turn_servo_angle(61,25,600,False)
  Motion.turn_servo_angle(31,25,600,False)
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.R1])

def on_joystick_keys_click_event():

  Motion.turn_servo_angle(11,-60,600,False)
  Motion.turn_servo_angle(41,-60,600,False)
  Motion.turn_servo_angle(61,60,600,False)
  Motion.turn_servo_angle(31,60,600,False)
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.UP])

def on_joystick_keys_click_event():
  global var_flag

  var_flag = '1'
  Device.show_light_hsv([Device.Light.ID.TOP,Device.Light.ID.DOWN], Color.create_color_hsv(0,100,100))
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.L2])

def on_joystick_keys_click_event():
  global var_flag

  var_flag = '0'
  Device.show_light_hsv([Device.Light.ID.TOP,Device.Light.ID.DOWN], Color.create_color_hsv(66,100,100))
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.R2])

def on_joystick_keys_click_event():

  Motion.turn_motor_speed(0,12)
  while (not (Math.gt(5, (Math.abs(Motion.read_motor_speed(0)))))):
      Motion.turn_motor_speed(0,12)

  Motion.stop_motor(0)
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.B])

def on_joystick_keys_click_event():

  ubt_Pid_Throw.set_pid(1,0,1)
  ubt_Pid_Throw.update(69)
  ControlFlow.wait(600, ControlFlow.TimeUnit.MILLISECOND)
  Motion.turn_motor_speed(0,ubt_Pid_unnamed.get_output())
  ControlFlow.wait(600, ControlFlow.TimeUnit.MILLISECOND)
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.X])

def on_joystick_keys_click_event():

  Motion.turn_motor_speed(0,-42)
  ControlFlow.wait(600, ControlFlow.TimeUnit.MILLISECOND)
  Motion.stop_motor(0)
Event.register_joypad_button(on_joystick_keys_click_event,[Joypad.Button.Y])

Normal readout
large readout
slider
Normal readout
large readout
slider
Normal readout
large readout
slider
Normal readout
large readout
slider
Normal readout
large readout
slider