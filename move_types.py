
class Types():
    normal = 0
    grass = 1
    fire = 2
    water = 3

    # Case-insensitive keys
    @classmethod
    def __getitem__(cls, key):
        return cls.__dict__[key.lower()]
    
    @classmethod
    def _keys(cls):
        return [key for key in cls.__dict__.keys() if not key.startswith('_')]
    
    @classmethod
    def _values(cls):
        return [cls.__dict__[key] for key in cls.__dict__.keys() if not key.startswith('_')]
    
    @classmethod
    def _items(cls):
        return [(key, cls.__dict__[key]) for key in cls.__dict__.keys() if not key.startswith('_')]
    
    @classmethod
    def _get(cls, key):
        return cls.__dict__[key.lower()]

SUPEREFFECTIVE = {
    Types.normal: [],
    Types.grass: [Types.water],
    Types.fire: [Types.grass],
    Types.water: [Types.fire]
}

WEAK = {
    Types.normal: [],
    Types.grass: [Types.fire],
    Types.fire: [Types.water],
    Types.water: [Types.grass]
}

IMMUNE = {
    Types.normal: [],
    Types.grass: [],
    Types.fire: [],
    Types.water: []
}

def supereffective(attack_type, defender_type):
    return Types._get(defender_type) in SUPEREFFECTIVE[Types._get(attack_type)]

def weak(attack_type, defender_type):
    return Types._get(defender_type) in WEAK[Types._get(attack_type)]

def immune(attack_type, defender_type):
    return Types._get(defender_type) in IMMUNE[Types._get(attack_type)]