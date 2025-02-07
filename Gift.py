import random


class GiftExchange():

    def __init__(self, particpant_pairs):
      # LIST OF TUPLES
      self.participant_pairs = particpant_pairs 


    def StartExchange(self):
        partners = {}

        givers = []

        for pair in self.participant_pairs:
          a = pair[0]
          b = pair[1]
          partners[a] = b
          partners[b] = a
          givers.append(a)
          givers.append(b)

        receivers = list(givers)
            
        while True:
            random.shuffle(receivers)
            valid = True
            assignment = {}
            for i in range(len(givers)):
                giver = givers[i]
                receiver = receivers[i]
                if giver == receiver:
                    valid = False
                    break
                if receiver == partners[giver]:
                    valid = False
                    break
                assignment[giver] = receiver
            if valid:
                break

        for giver in assignment:
            print(giver, " gives a gift to", assignment[giver])

        
                

        






test = GiftExchange((("a","b"),("c","d"),("e","f")))

test.StartExchange()
        

       