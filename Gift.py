import random


class GiftExchange():

    def __init__(self, particpant_pairs):
      self.participant_pairs = particpant_pairs 


    def StartExchange(self):
        participants = {}

        givers = []

        for pair in self.participant_pairs:
          a = pair[0]
          b = pair[1]
          participants[a] = b
          participants[b] = a

        print(participants)



test = GiftExchange((("a","b"),("c","d")))

test.StartExchange()
        

        