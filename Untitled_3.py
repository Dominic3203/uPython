from uexplore_interfaces import Event
from uexplore_interfaces import Audio
from uexplore_interfaces import Device
from uexplore_interfaces import Color
from uexplore_interfaces import Model
from uexplore_interfaces import Math
from uexplore_interfaces import Utils
from uexplore_interfaces import Broadcast
from uexplore_interfaces import PidControl
from uexplore_interfaces import AIVision
import math
from uexplore_interfaces import Detect
from uexplore_interfaces import Screen
from uexplore_interfaces import AISpeech
from uexplore_interfaces import ControlFlow
from uexplore_interfaces import Comparison

var__E6_88_91_E7_9A_84_E5_8F_98_E9_87_8F = 0
var__E5_A5_87_E6_88_96_E5_81_B6 = 0
var_X = 0
var_odd_or_even = 0

ubt_Pid_rotate = PidControl()

def func_line_track(var_distance):
  global var_X

  ubt_Pid_rotate.set_pid(0.065,0,0.02)
  AIVision.load_model([AIVision.Model.track_recognition])
  AIVision.set_track_recognition_line(AIVision.LineType.single)
  while True:
      var_X = AIVision.get_single_track_offset()
      ubt_Pid_rotate.update(Utils.parseToNumber(var_X))
      var_X = ubt_Pid_rotate.get_output()
      if (Math.gt(Utils.parseToNumber(var_X), 0)):
          Model.transform_move_turn(Model.Direction.forward,20,Model.Direction.turn_right,Math.abs(Utils.parseToNumber(var_X)))
      else:
          Model.transform_move_turn(Model.Direction.forward,20,Model.Direction.turn_left,Math.abs(Utils.parseToNumber(var_X)))
      if (Math.lt((Detect.read_distance_sensor(21)), var_distance)):
          Model.transform_stop()
          break


def func_QR_code():
  global var_odd_or_even

  AIVision.load_model([AIVision.Model.qrcode])
  Broadcast.enable(True)
  Broadcast.set_channel(1)
  while (not (Math.gt((AIVision.get_apriltag_info(AIVision.TagInfo.id)), 0))):
      Screen.print_text_newline((AIVision.get_apriltag_info(AIVision.TagInfo.id)),Screen.Color.white)

  if (Math.equal(((AIVision.get_apriltag_info(AIVision.TagInfo.id) % 2)), 0)):
      var_odd_or_even = '2'
      Device.show_light_hsv([Device.Light.ID.DOWN], Color.create_color_hsv(67,100,100))
      AISpeech.play_tts(str('識別到QRcode為偶數'),AISpeech.Timbre.Female,False)
  else:
      var_odd_or_even = '1'
      Device.show_light_hsv([Device.Light.ID.DOWN], Color.create_color_hsv(0,100,100))
      AISpeech.play_tts(str('識別到QRcode為奇數'),AISpeech.Timbre.Female,False)
  ControlFlow.wait(1, ControlFlow.TimeUnit.SECOND)

def func_up_stair():

  Model.transform_adaption_control(Model.Adaption.OFF)
  Model.run_custom_motion([({11:-103,31:25,41:-25,61:103},500)])
  while (not (Detect.check_distance_sensor_data(51,Comparison.LEQ,10))):
      Model.transform_move_speed(Model.Direction.forward,5)

  Model.transform_stop()
  Model.transform_set_chassis_height(7)

def func_detect_toy():

  AIVision.load_model([AIVision.Model.toy_recognition])
  ControlFlow.wait(1, ControlFlow.TimeUnit.SECOND)
  if (AIVision.check_toy(AIVision.Toy.WALKER)):
      Device.show_light_hsv([Device.Light.ID.TOP], Color.create_color_hsv(0,100,100))
      AISpeech.play_tts(str('識別為walker'),AISpeech.Timbre.Female,False)

  if (AIVision.check_toy(AIVision.Toy.YOUYOU)):
      Device.show_light_hsv([Device.Light.ID.TOP], Color.create_color_hsv(58,100,100))
      AISpeech.play_tts(str('識別為yoyo'),AISpeech.Timbre.Female,False)

  if (AIVision.check_toy(AIVision.Toy.WALKERX)):
      Device.show_light_hsv([Device.Light.ID.TOP], Color.create_color_hsv(79,100,100))
      AISpeech.play_tts(str('識別為walker X'),AISpeech.Timbre.Female,False)

  ControlFlow.wait(1, ControlFlow.TimeUnit.SECOND)


def on_start_event():
  global var_odd_or_even

  Audio.set_volume(Audio.Volume.MAXIMUM)
  Device.show_light_effect(Color.create_color_hsv(0,0,100),Device.Light.Effect.FLASHING)
  Model.transform_adaption_control(Model.Adaption.OFF)
  Model.transform_restory()
  Model.transform_move_speed_times(Model.Direction.forward,20,34,Model.Unit.mileage)
  Model.transform_turn_speed_times(Model.Direction.turn_left,30,90,Model.Unit.angle)
  func_line_track((65 + 0.5))
  Model.transform_stop()
  Model.transform_turn_speed_times(Model.Direction.turn_left,35,90,Model.Unit.angle)
  Model.transform_stop()
  Model.transform_set_chassis_height(7)
  func_QR_code()
  Model.run_custom_motion([({11:-30,31:30,41:-30,61:30},800)])
  Model.transform_set_chassis_height(2)
  Model.transform_turn_speed_times(Model.Direction.turn_right,10,5,Model.Unit.angle)
  Model.transform_stop()
  func_detect_toy()
  Model.run_custom_motion([({11:-30,31:30,41:-30,61:30},800)])
  Model.transform_set_chassis_height(5)
  Model.transform_move_speed_times(Model.Direction.backward,30,20,Model.Unit.mileage)
  if (Math.equal(Utils.parseToNumber(var_odd_or_even), 1)):
      for count in range(round((20))):
          Broadcast.send(str('odd'))

      while (not (Broadcast.check_last_message('3'))):
          pass

      Model.transform_turn_speed_times(Model.Direction.turn_left,40,91,Model.Unit.angle)
      Model.transform_move_speed_times(Model.Direction.forward,20,30,Model.Unit.mileage)
      Model.transform_turn_speed_times(Model.Direction.turn_right,40,88,Model.Unit.angle)
      Model.transform_stop()
      func_line_track('10')
      func_up_stair()
  else:
      for count in range(round((20))):
          Broadcast.send(str('even'))

      while (not (Broadcast.check_last_message('3'))):
          pass

      Model.transform_turn_speed_times(Model.Direction.turn_left,40,91,Model.Unit.angle)
      Model.transform_move_speed_times(Model.Direction.forward,20,30,Model.Unit.mileage)
      Model.transform_turn_speed_times(Model.Direction.turn_right,40,88,Model.Unit.angle)
      Model.transform_stop()
      func_line_track('10')
      func_up_stair()
  while True:
      pass
Event.register_start(on_start_event)

Normal readout
large readout
slider
Normal readout
large readout
slider
Normal readout
large readout
slider