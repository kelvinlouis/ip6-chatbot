import logging
from re import sub
from rasa_core.slots import Slot

logger = logging.getLogger(__name__)

class RoomSlot(Slot):
    """
    Custom slot that maps a set of words to specific rooms.
    This ensures that words 'like' this or 'it' refer to the current room,
    and words like 'other' to all rooms except the current room.
    The slot is one hot encoded (see below).
    """

    def feature_dimensionality(self):
        return 6

    def as_feature(self):
        """
        [0,0,0,0,0,0] - Not set
        [1,0,0,0,0,0] - Alpha, first...
        [0,1,0,0,0,0] - Beta, second...
        [0,0,1,0,0,0] - Gamma, third...
        [0,0,0,1,0,0] - other, others...
        [0,0,0,0,1,0] - this, it...
        [0,0,0,0,0,1] - all
        """

        r = [0.0] * self.feature_dimensionality()

        lookup = {
            "alpha":    0,
            "first":    0,

            "beta":     1,
            "second":   1,

            "gamma":    2,
            "third":    2,
            "last":     2,

            "other":    3,
            "others":   3,
            "different": 3,
            "another":  3,

            "this":     4,
            "that":     4,
            "it":       4,
            "the":      4,
            "there":    4,

            "all":      5,
            "every":    5,
            "each":     5,
        }

        try:
            if isinstance(self.value, str):
                lower_value = self.value.lower()

                try:
                    idx_r = lookup[lower_value]
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