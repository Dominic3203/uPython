from uexplore_interfaces import Event
from uexplore_interfaces import Audio
from uexplore_interfaces import Device
from uexplore_interfaces import Color
from uexplore_interfaces import Model
from uexplore_interfaces import Detect
from uexplore_interfaces import Comparison
from uexplore_interfaces import Math
from uexplore_interfaces import Utils
from uexplore_interfaces import Broadcast
from uexplore_interfaces import AIVision
from uexplore_interfaces import Screen
from uexplore_interfaces import AISpeech
from uexplore_interfaces import PidControl
import math
from uexplore_interfaces import ControlFlow

var__E6_88_91_E7_9A_84_E5_8F_98_E9_87_8F = 0
var__E5_A5_87_E6_88_96_E5_81_B6 = 0
var_X = 0

def func__E4_BA_8C_E7_BB_B4_E7_A0_81_E8_AF_86_E5_88_AB():
  global var__E5_A5_87_E6_88_96_E5_81_B6

  AIVision.load_model([AIVision.Model.qrcode])
  Broadcast.enable(True)
  Broadcast.set_channel(1)
  while (not (Math.gt((AIVision.get_apriltag_info(AIVision.TagInfo.id)), 0))):
      Screen.print_text_newline((AIVision.get_apriltag_info(AIVision.TagInfo.id)),Screen.Color.white)

  if False:
      var__E5_A5_87_E6_88_96_E5_81_B6 = '2'
      Device.show_light_hsv([Device.Light.ID.DOWN], Color.create_color_hsv(67,100,100))
      AISpeech.play_tts(str('识别到标签为偶数'),AISpeech.Timbre.Female,False)
  else:
      var__E5_A5_87_E6_88_96_E5_81_B6 = '1'
      Device.show_light_hsv([Device.Light.ID.DOWN], Color.create_color_hsv(0,100,100))
      AISpeech.play_tts(str('识别到标签为奇数'),AISpeech.Timbre.Female,False)

ubt_Pid_E6_97_8B_E8_BD_AC = PidControl()

def func__E5_B7_A1_E7_BA_BF(var__E8_B7_9D_E7_A6_BB):
  global var_X

  Model.run_custom_motion([({11:-10,31:45,41:-45,61:10},600)])
  ubt_Pid_E6_97_8B_E8_BD_AC.set_pid(0.2,0,0.001)
  AIVision.load_model([AIVision.Model.track_recognition])
  AIVision.set_track_recognition_line(AIVision.LineType.single)
  while True:
      var_X = AIVision.get_single_track_offset()
      ubt_Pid_E6_97_8B_E8_BD_AC.update(Utils.parseToNumber(var_X))
      var_X = ubt_Pid_E6_97_8B_E8_BD_AC.get_output()
      if (Math.gt(Utils.parseToNumber(var_X), 0)):
          Model.transform_move_turn(Model.Direction.forward,20,Model.Direction.turn_right,Math.abs(Utils.parseToNumber(var_X)))
      else:
          Model.transform_move_turn(Model.Direction.forward,20,Model.Direction.turn_left,Math.abs(Utils.parseToNumber(var_X)))
      if (Math.gte((Detect.read_distance_sensor(51)), var__E8_B7_9D_E7_A6_BB)):
          Model.transform_stop()
          break


def func__E4_B8_8A_E5_8F_B0():

  Model.transform_adaption_control(Model.Adaption.OFF)
  Model.run_custom_motion([({11:-103,31:25,41:-25,61:103},500)])
  while (not False):
      pass

  Model.transform_stop()
  Model.transform_set_chassis_height(7)

def func__E8_AF_86_E5_88_AB_E5_85_AC_E4_BB_94():

  AIVision.load_model([AIVision.Model.toy_recognition])
  ControlFlow.wait(1, ControlFlow.TimeUnit.SECOND)
  if (False):
      Device.show_light_hsv([Device.Light.ID.TOP], Color.create_color_hsv(0,100,100))
      AISpeech.play_tts(str('识别到公仔为walker'),AISpeech.Timbre.Female,False)

  if (False):
      Device.show_light_hsv([Device.Light.ID.TOP], Color.create_color_hsv(58,100,100))
      AISpeech.play_tts(str('识别到公仔为优悠'),AISpeech.Timbre.Female,False)

  if (False):
      Device.show_light_hsv([Device.Light.ID.TOP], Color.create_color_hsv(78,100,100))
      AISpeech.play_tts(str('识别到公仔为walker X'),AISpeech.Timbre.Female,False)

  ControlFlow.wait(1, ControlFlow.TimeUnit.SECOND)


def on_start_event():
  global var__E5_A5_87_E6_88_96_E5_81_B6

  Audio.set_volume(Audio.Volume.MAXIMUM)
  Device.show_light_effect(Color.create_color_hsv(0,0,100),Device.Light.Effect.FLASHING)
  Model.transform_adaption_control(Model.Adaption.OFF)
  Model.transform_restory()
  func__E5_B7_A1_E7_BA_BF((38 + 0.5))
  Model.transform_turn_speed_times(Model.Direction.turn_left,40,93,Model.Unit.angle)
  Model.transform_stop()
  func__E5_B7_A1_E7_BA_BF((59 + 0.5))
  Model.transform_turn_speed_times(Model.Direction.turn_left,40,90,Model.Unit.angle)
  Model.transform_stop()
  Model.transform_set_chassis_height(7)
  func__E4_BA_8C_E7_BB_B4_E7_A0_81_E8_AF_86_E5_88_AB()
  Model.run_custom_motion([({11:-30,31:30,41:-30,61:30},800)])
  Model.transform_set_chassis_height(2)
  while (not (Detect.check_distance_sensor_data(51,Comparison.LEQ,10))):
      Model.transform_move_speed(Model.Direction.backward,40)

  Model.transform_stop()
  func__E8_AF_86_E5_88_AB_E5_85_AC_E4_BB_94()
  Model.transform_stop()
  if (Math.equal(Utils.parseToNumber(var__E5_A5_87_E6_88_96_E5_81_B6), 1)):
      for count in range(round((20))):
          Broadcast.send(str('奇'))

      while (not (Broadcast.check_last_message('3'))):
          pass

      Model.transform_move_speed_times(Model.Direction.forward,20,40,Model.Unit.mileage)
      Model.transform_turn_speed_times(Model.Direction.turn_left,40,88,Model.Unit.angle)
      Model.transform_stop()
      func__E5_B7_A1_E7_BA_BF((99 + 0))
      Model.transform_turn_speed_times(Model.Direction.turn_left,40,91,Model.Unit.angle)
      func__E4_B8_8A_E5_8F_B0()
  else:
      for count in range(round((20))):
          Broadcast.send(str('偶'))

      while (not (Broadcast.check_last_message('3'))):
          pass

      Model.transform_move_speed_times(Model.Direction.forward,20,40,Model.Unit.mileage)
      Model.transform_turn_speed_times(Model.Direction.turn_right,40,84,Model.Unit.angle)
      Model.transform_stop()
      func__E5_B7_A1_E7_BA_BF((95 + 0))
      Model.transform_turn_speed_times(Model.Direction.turn_right,40,88,Model.Unit.angle)
      Model.transform_stop()
      func__E4_B8_8A_E5_8F_B0()
  while True:
      pass
Event.register_start(on_start_event)

Normal readout
large readout
slider
Normal readout
large readout
slider