import enum

class Meta(enum.EnumMeta): 
    def __contains__(cls, item): 
        return isinstance(item, cls) or item in [v.value for v in cls.__members__.values()] 