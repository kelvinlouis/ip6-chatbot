import logging

from rasa_core.slots import Slot

logger = logging.getLogger(__name__)

class NumberOfPeopleSlot(Slot):
    type_name = "nr_of_people"

    def feature_dimensionality(self):
        return 3

    def as_feature(self):
        '''
        [0,0,0] - Not set
        [1,0,0] - x <= 190
        [1,1,0] - 190 < x <= 200
        [1,0,1] - 200 < x <= 270
        [1,1,1] - 270 < x
        '''
        
        r = [0.0] * self.feature_dimensionality()
        try:
            if isinstance(self.value, str):
                # Convert string to integer
                self.value = int(float(self.value))

                if self.value <= 190:
                    logger.debug("{} number of people is under or equal to 190".format(self.value))
                    r[0] = 1.0
                elif 190 < self.value <= 200:
                    logger.debug("{} number of people is between 190 and 200".format(self.value))
                    r[0] = 1.0
                    r[1] = 1.0
                elif 200 < self.value <= 270:
                    logger.debug("{} number of people is between 200 and 270".format(self.value))
                    r[0] = 1.0
                    r[2] = 1.0
                else:
                    logger.debug("{} number of people is over 270".format(self.value))
                    r[0] = 1.0
                    r[1] = 1.0
                    r[2] = 1.0
            else:
                pass
        except (TypeError, ValueError):
            logger.warning("Failed to convert value {}, returning {}".format(self.value, r))
            return r

        logger.debug("Returning r: {}".format(r))
        return r