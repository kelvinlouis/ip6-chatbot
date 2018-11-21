from rasa_core.slots import Slot

class NumberOfPeopleSlot(Slot):

    def feature_dimensionality(self):
        return 3

    def as_feature(self):
        '''
        [0,0,0] - Not set
        [1,0,0] - x <= 190
        [0,1,0] - 190 < x <= 200
        [0,0,1] - 200 < x <= 270
        [1,1,0] - 270 < x
        '''
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value <= 190:
                r[0] = 1.0
            elif 190 < self.value <= 200:
                r[1] = 1.0
            elif 200 < self.value <= 270:
                r[2] = 1.0
            else:
                r[0] = 1.0
                r[1] = 1.0
        return r