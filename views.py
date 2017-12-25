#!/usr/bin/env python3.5
# encoding: utf-8
from gpiozero import LEDBoard

from sanic.response import json
from sanic.views import HTTPMethodView

ON = [0, 1]
OFF = [1, 0]

tree = LEDBoard(*range(2, 28), pwm=True)


class PinView(HTTPMethodView):
    _url = '/api/<pin>/<switch>'

    async def change_led(self, pin, switch='on'):
        getattr(tree[pin], switch)()

    async def handle_request(self, pin, switch='on'):
        if pin == 'all':
            getattr(tree, switch)()
        else:
            try:
                pin = int(pin)
                if 25 < pin < 0:
                    raise IndexError
            except:
                return json({'ok': False, 'reason': 'must be all or integer between 0 and 25'})
            await self.change_led(pin, switch=switch)
        return json({'ok': True})

    async def get(self, _, pin, switch):
        if switch not in ['on', 'off', 'pulse', 'blink']:
            return json({'ok': False, 'reason': "only 'on', 'off', 'pulse', 'blink' are allowed"})
        return await self.handle_request(pin, switch=switch)
