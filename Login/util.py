from redisService import *
from network import *


class Util:
    def __init__(self):
        self.redisService= redisService()

    def signIn(self, data):
        if data['kind'] == "signIn":
            result = self.redisService.signIn(data)

            if result is False:
                return sendData(data)
            else:
                self.redisService.reInsertValue(data)
                return "http://61.254.240.172:30000"
        else:
          return False

    def signUp(self, data):
        if data['kind'] == "signUp":
            result1 = sendData(data)

            if result1 is not None:
                self.redisService.signUp(data)
                return True

            return False
        else:
            return False