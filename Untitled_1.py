from uexplore_interfaces import Event
from uexplore_interfaces import Device
from uexplore_interfaces import Color
from uexplore_interfaces import Broadcast
from uexplore_interfaces import Model
from uexplore_interfaces import AIVision
from uexplore_interfaces import PidControl
from uexplore_interfaces import Utils
from uexplore_interfaces import Math
import math
from uexplore_interfaces import Detect
from uexplore_interfaces import ControlFlow
from uexplore_interfaces import Logic
from uexplore_interfaces import Screen

var__E6_88_91_E7_9A_84_E5_8F_98_E9_87_8F = 0
var_X = 0
var__E5_8D_81_E5_AD_97_E8_B7_AF_E5_8F_A3Y = 0
var__E8_B7_9D_E7_A6_BB = 0
var__E6_96_B9_E5_9D_97_E5_81_8F_E7_A7_BB = 0
var_Z = 0
var__E6_94_BE_E5_9D_97 = 0
var_i = 0
var_flag = 0
list_list__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF = []
list_list__E8_BD_A6_E9_81_93_E7_BA_BF = []
list_list__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97 = []

ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX = PidControl()

def func__E5_B9_B3_E7_A7_BB_E8_B0_83_E6_95_B4():
  global var__E8_BD_A6_E9_81_93_E7_BA_BF,var_X

  AIVision.load_model([AIVision.Model.track_recognition])
  AIVision.set_track_recognition_line(AIVision.LineType.single)
  ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX.set_pid(0.11,0,0.01)
  while True:
      list_list__E8_BD_A6_E9_81_93_E7_BA_BF = [i for i in AIVision.get_single_track_total_info()]
      var_X = Utils.List.getValueByIndex(list_list__E8_BD_A6_E9_81_93_E7_BA_BF, 1)
      if (Math.lt((Math.abs(Utils.parseToNumber(var_X))), 7)):
          Model.mecanum_stop()
          break

      ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX.update(Utils.parseToNumber(var_X))
      Model.mecanum_move_xyz(Math.round_up(ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX.get_output()),0,0)

ubt_Pid_E8_B7_9D_E7_A6_BB = PidControl()

def func__E9_A2_84_E8_B0_83_E8_B7_9D(var__E7_9B_AE_E6_A0_87_E8_B7_9D_E7_A6_BB):
  global var__E8_B7_9D_E7_A6_BB

  ubt_Pid_E8_B7_9D_E7_A6_BB.set_pid(1.7,0,0.05)
  while True:
      var__E8_B7_9D_E7_A6_BB = Detect.read_distance_sensor(21)
      if (Math.lte((Math.abs((var__E7_9B_AE_E6_A0_87_E8_B7_9D_E7_A6_BB - Utils.parseToNumber(var__E8_B7_9D_E7_A6_BB)))), 0)):
          break

      ubt_Pid_E8_B7_9D_E7_A6_BB.update(((var__E7_9B_AE_E6_A0_87_E8_B7_9D_E7_A6_BB - Utils.parseToNumber(var__E8_B7_9D_E7_A6_BB))))
      Model.mecanum_move_xyz(0,Math.round_up(ubt_Pid_E8_B7_9D_E7_A6_BB.get_output()),0)

ubt_Pid_E6_96_B9_E5_9D_97X = PidControl()

def func__E5_A4_B9_E5_8F_96_E9_AB_98_E5_8F_B0_E6_96_B9_E5_9D_97():
  global var__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF,var__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97

  func__E9_A2_84_E8_B0_83_E8_B7_9D((20 + 1.5))
  Model.mechanical_arms_control(Model.ArmControl.RELEASE)
  Model.run_mechanical_motion([({1:90,2:-23,3:45},600)])
  ubt_Pid_E6_96_B9_E5_9D_97X.set_pid(0.16,0,0.001)
  AIVision.load_model([AIVision.Model.color])
  while True:
      list_list__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF = [i for i in AIVision.get_color_total_info()]
      if (Math.lt(len(list_list__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF), 1)):
          continue

      list_list__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97 = [i for i in Utils.List.getValueByIndex(list_list__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF, 1)]
      if (Math.lte((Math.abs((Utils.List.getValueByIndex(list_list__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97, 3) - 0))), 0)):
          Model.mecanum_stop()
          Model.run_mechanical_motion([({1:90,2:-21,3:26},600)])
          func__E9_A2_84_E8_B0_83_E8_B7_9D((12 + 1))
          ControlFlow.wait(1, ControlFlow.TimeUnit.SECOND)
          Model.mechanical_arms_control(Model.ArmControl.CLOSE)
          Model.run_mechanical_motion([({1:90,2:-45,3:11},400),({1:90,2:-94,3:-36},500)])
          break

      ubt_Pid_E6_96_B9_E5_9D_97X.update(((0 - Utils.List.getValueByIndex(list_list__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97, 3))))
      Model.mecanum_move_xyz(Math.ceil(ubt_Pid_E6_96_B9_E5_9D_97X.get_output()),0,0)

ubt_Pid_E6_97_8B_E8_BD_AC = PidControl()

def func__E5_B7_A1_E7_BA_BF(var__E8_B7_9D_E7_A6_BB, var__E6_98_AF_E5_90_A6_E8_BD_AC_E5_90_91_E5_BC_8F):
  global var_X

  AIVision.load_model([AIVision.Model.track_recognition])
  AIVision.set_track_recognition_line(AIVision.LineType.single)
  ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX.set_pid(0.065,0,0.005)
  ubt_Pid_E6_97_8B_E8_BD_AC.set_pid(0.08,0,0.015)
  while True:
      var_X = AIVision.get_single_track_offset()
      if (Logic.contains(str(var__E6_98_AF_E5_90_A6_E8_BD_AC_E5_90_91_E5_BC_8F),str('是'))):
          ubt_Pid_E6_97_8B_E8_BD_AC.update(Utils.parseToNumber(var_X))
          Model.mecanum_move_xyz(0,30,(Math.round_up(ubt_Pid_E6_97_8B_E8_BD_AC.get_output()) * -1))
      else:
          ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX.update(Utils.parseToNumber(var_X))
          Model.mecanum_move_xyz(Math.round_up(ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX.get_output()),10,0)
      if (Math.lt((Detect.read_distance_sensor(21)), var__E8_B7_9D_E7_A6_BB)):
          Model.mecanum_stop()
          Screen.print_text_newline('已到达位置',Screen.Color.white)
          break


def func__E6_94_BE_E7_BD_AE_E9_AB_98_E5_8F_B0_E6_96_B9_E5_9D_97(var__E9_A2_9C_E8_89_B2):
  global var_flag,var__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF,var_i,var__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97

  ubt_Pid_E6_96_B9_E5_9D_97X.set_pid(0.18,0,0.0015)
  AIVision.load_model([AIVision.Model.color])
  var_flag = '0'
  while True:
      list_list__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF = [i for i in AIVision.get_color_total_info()]
      if (Math.lt(len(list_list__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF), 1)):
          continue

      for var_i in range(1,len(list_list__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF) + 1,1):
          list_list__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97 = [i for i in Utils.List.getValueByIndex(list_list__E6_96_B9_E5_9D_97_E4_BF_A1_E6_81_AF, Utils.parseToNumber(var_i))]
          if ((Logic.contains(str(Utils.List.getValueByIndex(list_list__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97, 1)),str(var__E9_A2_9C_E8_89_B2))) and (Logic.contains(str(Utils.List.getValueByIndex(list_list__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97, 2)),str('方')))):
              var_flag = '1'
              break


      if (Math.equal(Utils.parseToNumber(var_flag), 0)):
          continue

      if (Math.lte((Math.abs((Utils.List.getValueByIndex(list_list__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97, 3) - 0))), 0)):
          func__E9_A2_84_E8_B0_83_E8_B7_9D((1 + 15))
          Model.run_mechanical_motion([({1:90,2:-73,3:-24},300)])
          ControlFlow.wait(400, ControlFlow.TimeUnit.MILLISECOND)
          Model.mecanum_stop()
          Model.mechanical_arms_control(Model.ArmControl.RELEASE)
          ControlFlow.wait(1000, ControlFlow.TimeUnit.MILLISECOND)
          Model.mecanum_move_speed_times(Model.Direction.backward,20,1,Model.Unit.second)
          Model.mecanum_stop()
          while (not (Broadcast.check_last_message('15'))):
              pass

          func__E9_A2_84_E8_B0_83_E8_B7_9D((15 + 3))
          break

      ubt_Pid_E6_96_B9_E5_9D_97X.update(((0 - Utils.List.getValueByIndex(list_list__E4_B8_80_E4_B8_AA_E6_96_B9_E5_9D_97, 3))))
      Model.mecanum_move_xyz(Math.ceil(ubt_Pid_E6_96_B9_E5_9D_97X.get_output()),0,0)

def func__E6_97_8B_E8_BD_AC_E8_B0_83_E6_95_B4():
  global var__E8_BD_A6_E9_81_93_E7_BA_BF,var_Z

  AIVision.load_model([AIVision.Model.track_recognition])
  AIVision.set_track_recognition_line(AIVision.LineType.single)
  ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX.set_pid(0.23,0,0.02)
  while True:
      list_list__E8_BD_A6_E9_81_93_E7_BA_BF = [i for i in AIVision.get_single_track_total_info()]
      var_Z = Utils.List.getValueByIndex(list_list__E8_BD_A6_E9_81_93_E7_BA_BF, 1)
      if (Math.lte((Math.abs(Utils.parseToNumber(var_Z))), 9)):
          break

      ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX.update(Utils.parseToNumber(var_Z))
      Model.mecanum_move_xyz(0,0,(Math.round_up(ubt_Pid_E8_BD_A6_E9_81_93_E7_BA_BFX.get_output()) * -1))

def func__E5_A5_87_E6_95_B0_E4_BB_BB_E5_8A_A1():

  func__E5_B7_A1_E7_BA_BF((36 + 5), '是')
  Model.mecanum_stop()
  Model.mecanum_turn_speed_times(Model.Direction.turn_right,50,90,Model.Unit.angle)
  func__E5_A4_B9_E5_8F_96_E9_AB_98_E5_8F_B0_E6_96_B9_E5_9D_97()
  Model.mecanum_stop()
  Model.mecanum_turn_speed_times(Model.Direction.turn_right,50,175,Model.Unit.angle)
  func__E5_B9_BF_E6_92_AD()
  func__E5_B7_A1_E7_BA_BF((19 + 0.5), '否')
  func__E6_94_BE_E7_BD_AE_E9_AB_98_E5_8F_B0_E6_96_B9_E5_9D_97('')

def func__E5_81_B6_E6_95_B0_E4_BB_BB_E5_8A_A1():

  func__E5_B7_A1_E7_BA_BF((85 + 7), '是')
  Model.mecanum_stop()
  Model.mecanum_turn_speed_times(Model.Direction.turn_right,50,90,Model.Unit.angle)
  Model.mecanum_stop()
  func__E5_A4_B9_E5_8F_96_E9_AB_98_E5_8F_B0_E6_96_B9_E5_9D_97()
  Model.mecanum_stop()
  Model.mecanum_turn_speed_times(Model.Direction.turn_right,50,176,Model.Unit.angle)
  func__E5_B9_BF_E6_92_AD()
  func__E5_B7_A1_E7_BA_BF((19 + 0.5), '否')
  func__E6_94_BE_E7_BD_AE_E9_AB_98_E5_8F_B0_E6_96_B9_E5_9D_97('')

def func__E5_B9_BF_E6_92_AD():

  for count in range(round((20))):
      Broadcast.send(str('3'))


def on_start_event():

  Device.show_light_effect(Color.create_color_hsv(0,0,100),Device.Light.Effect.FLASHING)
  Broadcast.enable(True)
  Broadcast.set_channel(1)
  Model.mecanum_move_speed_times(Model.Direction.forward,25,35,Model.Unit.mileage)
  Model.mecanum_move_speed_times(Model.Direction.forward,50,37,Model.Unit.mileage)
  Model.mecanum_stop()
  Model.mecanum_move_speed_times(Model.Direction.backward,20,37,Model.Unit.mileage)
  Model.mecanum_stop()
  Model.mecanum_translate_speed_times(90,15,4,Model.Unit.mileage)
  Model.mecanum_stop()
  Model.mecanum_turn_speed_times(Model.Direction.turn_right,50,88,Model.Unit.angle)
  Model.mecanum_stop()
  func__E5_B9_B3_E7_A7_BB_E8_B0_83_E6_95_B4()
  Model.mecanum_stop()
  while True:
      if (Broadcast.check_last_message('')):
          Device.show_light_hsv([Device.Light.ID.DOWN], Color.create_color_hsv(0,100,100))
          func__E5_A5_87_E6_95_B0_E4_BB_BB_E5_8A_A1()
          while True:
              pass

      if (Broadcast.check_last_message('')):
          Device.show_light_hsv([Device.Light.ID.TOP,Device.Light.ID.DOWN], Color.create_color_hsv(72,100,100))
          func__E5_81_B6_E6_95_B0_E4_BB_BB_E5_8A_A1()
          while True:
              pass


Event.register_start(on_start_event)

Export
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
Normal readout
large readout
slider
Normal readout
large readout
slider