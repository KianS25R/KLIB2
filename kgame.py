from KLIB2.kmath import random

class blackjack():
    def __init__(self, digit6):
        """creates blackjack instance"""
        super().__init__()
        self.__gen = random(digit6, 0.01, 0.53)
        self.__phand = []
        self.__dhand = []