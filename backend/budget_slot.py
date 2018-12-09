import logging

from rasa_core.slots import Slot

logger = logging.getLogger(__name__)

class BudgetSlot(Slot):

    def feature_dimensionality(self):
        return 3

    def as_feature(self):
        '''
        [0,0,0] - Not set
        [1,0,0] - x <= 900
        [1,1,0] - 900 < x <= 1100
        [1,0,1] - 1100 < x <= 1400
        [1,1,1] - 1400 < x
        '''

        r = [0.0] * self.feature_dimensionality()
        try:
            if self.value is not None:
                self.value = int(float(self.value))
                if self.value:
                    if self.value <= 900:
                        logger.debug("Provided budget {} is under or equal to 900".format(self.value))
                        r[0] = 1.0
                    elif 900 < self.value <= 1100:
                        logger.debug("Provided budget {} is between 900 and 1100".format(self.value))
                        r[0] = 1.0
                        r[1] = 1.0
                    elif 1100 < self.value <= 1400:
                        logger.debug("Provided budget {} is between 1100 and 1400".format(self.value))
                        r[0] = 1.0
                        r[2] = 1.0
                    else:
                        logger.debug("Provided budget {} is more than 1400".format(self.value))
                        r[0] = 1.0
                        r[1] = 1.0
                        r[1] = 1.0
            else:
                pass
        except (TypeError, ValueError):
            logger.warning("Failed to convert value {}, returning {}".format(self.value, r))
            return r

        logger.debug("Returning r: {}".format(r))
        return r