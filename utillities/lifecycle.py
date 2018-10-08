import time
import utillities.colors as colors
import os
import aiy.toneplayer
from aiy.leds import Leds
import utillities.music as music
from utillities.logger import Logger

log = Logger(__name__)
leds = Leds()
color_cycle = ['blue', 'yellow', 'purple', 'cyan', 'white', 'green']
is_pulsing = False
current_color = (0,0,0)
player = aiy.toneplayer.TonePlayer(22)


def transition_to(from_color, to_color):
	global current_color
	r, g, b = from_color

	while r != to_color[0] or g != to_color[1] or b != to_color[2]:
		if r < to_color[0]:
			r += 1
		elif r > to_color[0]:
			r -= 1

		if g < to_color[1]:
			g += 1
		elif g > to_color[1]:
			g -= 1

		if b < to_color[2]:
			b += 1
		elif b > to_color[2]:
			b -= 1

		leds.update(Leds.rgb_on((r, g, b)))

		current_color = to_color

		time.sleep(0.0008)

def play_sound(pattern):
	player.play(*pattern)


def set_button_color(color):
	global current_color
	transition_to(current_color, color)


def startup():
	log.info("Entering startup")

	for (index, color) in enumerate(color_cycle):
		if index > 0:
			c1 = colors.get(color_cycle[index - 1])
			c2 = colors.get(color_cycle[index])
			transition_to(c1, c2)
		else:
			leds.update(Leds.rgb_on(colors.get(color)))
			time.sleep(0.2)

	leds.update(Leds.privacy_on())



def ConversationMode():
	pass


def LearningMode():
	pass


def stand_by():
	pass


def power_off():
	global state
	log.info("Entering standby")
	x = 25
	leds.update(Leds.rgb_on((x,x,x)))
	leds.update(Leds.privacy_off())


if __name__ == '__main__':
	from time import sleep
	
	play_sound(music.get_music('power_on'))
	sleep(1)
	play_sound(music.get_music("power_off"))
	sleep(1)
	play_sound(music.get_music("right"))
	sleep(1)
	play_sound(music.get_music("wrong"))
	sleep(1)
	play_sound(music.get_music("mode_change"))
