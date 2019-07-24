
class Hotel():
    def __init__(self , name='empty' , reviews = []):
        self.name = name
        self.reviews = reviews
        self.joyCount = 0
        self.joyComm = 0
        self.sadnessCount = 0
        self.sadnessComm = 0
        self.angerCount = 0
        self.angerComm = 0
        self.joyScore = 0
        self.sadnessScore = 0
        self.angerScore = 0

    def serialize(self):
        return {
            'Name': self.name, 
            'JoyScore': self.joyScore,
            'SadnessScore': self.sadnessScore,
            'AngerScore': self.angerScore,
        }
