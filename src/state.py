from ctypes import c_uint


# Help class to enable shared enums
class EnumerationType(type(c_uint)):
    def __new__(metacls, name, bases, dict):
        if not "_members_" in dict:
            _members_ = {}
            for key, value in dict.items():
                if not key.startswith("_"):
                    _members_[key] = value

            dict["_members_"] = _members_
        else:
            _members_ = dict["_members_"]

        dict["_reverse_map_"] = {v: k for k, v in _members_.items()}
        cls = type(c_uint).__new__(metacls, name, bases, dict)
        for key, value in cls._members_.items():
            globals()[key] = value
        return cls

    def __repr__(self):
        return "<Enumeration %s>" % self.__name__


# Help class to enable shared enums
class CEnumeration(c_uint):
    __metaclass__ = EnumerationType
    _members_ = {}

    def __repr__(self):
        value = self.value
        return "<%s.%s: %d>" % (
            self.__class__.__name__,
            self._reverse_map_.get(value, '(unknown)'),
            value
        )

    def __eq__(self, other):
        if isinstance(other, (int, long)):
            return self.value == other

        return type(self) == type(other) and self.value == other.value


class State(CEnumeration):
    RUNNING = 0
    STEPWISE = 1
    WAIT = 2
    PAUSE = 3
    STOP = 4
