import pybitflyer


class bitFlyer_use_api():

    api = None

    def __init__(self):
        self.api = pybitflyer.API()

    def borad(self):
        board = self.api.board(product_code="BTC_JPY")
        return board
