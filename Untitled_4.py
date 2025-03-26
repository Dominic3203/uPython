from uexplore_interfaces import Event
from uexplore_interfaces import Audio
from uexplore_interfaces import Model
from uexplore_interfaces import AIVision
from uexplore_interfaces import Broadcast
from uexplore_interfaces import Math
from uexplore_interfaces import Device
from uexplore_interfaces import Color
from uexplore_interfaces import ControlFlow
from uexplore_interfaces import AISpeech


def on_start_event():

  Audio.set_volume(Audio.Volume.MAXIMUM)
  Model.transform_move_speed_times(Model.Direction.backward,40,1,Model.Unit.second)
  Model.transform_turn_speed_times(Model.Direction.turn_right,30,3,Model.Unit.second)
  Model.transform_move_speed_times(Model.Direction.forward,40,1,Model.Unit.second)
  Model.transform_turn_speed_times(Model.Direction.turn_left,30,3,Model.Unit.second)
  Model.transform_move_speed_times(Model.Direction.forward,5,1,Model.Unit.second)
  AIVision.load_model([AIVision.Model.qrcode])
  Broadcast.enable(True)
  if (Math.equal(((AIVision.get_qrcode_result() % 2)), 1)):
      Device.show_light_hsv([], Color.create_color_hsv(0,100,100))
      Broadcast.set_channel(0)
      Broadcast.send(str('1'))
  else:
      Device.show_light_hsv([], Color.create_color_hsv(61,100,100))
      Broadcast.set_channel(0)
      Broadcast.send(str('0'))
  AIVision.load_model([AIVision.Model.toy_recognition])
  ControlFlow.wait(1, ControlFlow.TimeUnit.SECOND)
  if (AIVision.check_toy(AIVision.Toy.WALKER)):
      Device.show_light_hsv([], Color.create_color_hsv(0,100,100))
      AISpeech.play_tts(str('walker'),AISpeech.Timbre.Female,True)
  else:
      if (AIVision.check_toy(AIVision.Toy.YOUYOU)):
          AISpeech.play_tts(str('yoyo'),AISpeech.Timbre.Female,True)
          Device.show_light_hsv([], Color.create_color_hsv(67,100,100))
      else:
          if (AIVision.check_toy(AIVision.Toy.WALKERX)):
              AISpeech.play_tts(str('walker x'),AISpeech.Timbre.Female,True)
              Device.show_light_hsv([], Color.create_color_hsv(84,100,100))
          else:
              AISpeech.play_tts(str('unidentified'),AISpeech.Timbre.Female,True)
  Model.transform_move_speed_times(Model.Direction.backward,5,1,Model.Unit.second)
  Model.transform_turn_speed_times(Model.Direction.turn_right,30,3,Model.Unit.second)
  Model.transform_move_speed_times(Model.Direction.backward,40,1,Model.Unit.second)
  Model.transform_turn_speed_times(Model.Direction.turn_left,30,3,Model.Unit.second)
  Model.transform_move_speed_times(Model.Direction.forward,40,1,Model.Unit.second)
Event.register_start(on_start_event)
