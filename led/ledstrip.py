import rpi_ws281x as ws
import utillities.colors as colors
import config.ledstrip_config as lc
from time import sleep

class LedStrip:

    def __init__(self):
        self.controller = ws.PixelStrip(lc.LED_COUNT, lc.LED_PIN, lc.LED_FREQ_HZ, lc.LED_DMA, lc.LED_INVERT, lc.LED_BRIGHTNESS, lc.LED_CHANNEL)
        self.is_on = False
        self.current_color = (0, 0, 0)

    def start(self):
        assert not self.is_on

        self.controller.begin()
        self.is_on = True

    def stop(self):
        assert self.is_on

        self.transition_to(colors.get('black'), 0)
        self.is_on = False

    def transition_to(self, color, ms):
        c = colors.convert(color)

        for i in range(self.controller.numPixels()):
            self.controller.setPixelColor(i, c)
            self.controller.show()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--color')

    args = parser.parse_args()

    strip = LedStrip()

    strip.start()

    c = colors.get(args.color)

    strip.transition_to(c, 100)

    sleep(5)

    strip.stop()