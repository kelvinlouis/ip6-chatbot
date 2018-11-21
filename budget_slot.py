from rasa_core.slots import Slot

class BudgetSlot(Slot):

    def feature_dimensionality(self):
        return 3

    def as_feature(self):
        '''
        [0,0,0] - Not set
        [1,0,0] - x <= 900
        [0,1,0] - 900 < x <= 1100
        [0,0,1] - 1100 < x <= 1400
        [1,1,0] - 1400 < x
        '''
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value <= 900:
                r[0] = 1.0
            elif 900 < self.value <= 1100:
                r[1] = 1.0
            elif 1100 < self.value <= 1400:
                r[2] = 1.0
            else:
                r[0] = 1.0
                r[1] = 1.0
        return r