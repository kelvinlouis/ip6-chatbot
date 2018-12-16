import logging
from re import sub
from rasa_core.slots import Slot

logger = logging.getLogger(__name__)

class RoomSlot(Slot):

    def feature_dimensionality(self):
        return 7

    def as_feature(self):
        '''
        [0,0,0,0,0,0,0] - Not set
        [1,1,0,0,0,0,0] - Alpha, first...
        [1,0,1,0,0,0,0] - Beta, second...
        [1,0,0,1,0,0,0] - Gamma, third...
        [1,0,0,0,1,0,0] - other, others...
        [1,0,0,0,0,1,0] - this, it...
        [1,0,0,0,0,0,1] - all
        '''

        r = [0.0] * self.feature_dimensionality()

        lookup = {
            "alpha":    1,
            "first":    1,

            "beta":     2,
            "second":   2,

            "gamma":    3,
            "third":    3,
            "last":     3,

            "other":    4,
            "others":   4,
            "diffrent": 4,
            "another":  4,

            "this":     5,
            "that":     5,
            "it":       5,
            "the":      5,
            "there":    5,

            "all":      6,
            "every":    6
        }

        try:
            if isinstance(self.value, str):
                lower_value = self.value.lower()

                try:
                    idx_r = lookup[lower_value]
                    r[0] = 1.0
                    r[idx_r] = 1.0
                    #logger.debug("{} is in lookup table".format(lower_value))
                except KeyError:
                    logger.warning("{} is not in room lookup table".format(lower_value))
                    pass
            else:
                pass
        except TypeError as e:
            logger.warning("Failed to convert value {}, returning {}, error: {}".format(self.value, r, e))
            return r
        except ValueError as e:
            logger.warning("Failed to convert value {}, returning {}, error: {}".format(self.value, r, e))
            return r

        #logger.debug("Returning r: {}".format(r))
        return r