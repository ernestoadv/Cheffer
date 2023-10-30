import enum

class Enum(enum.Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))