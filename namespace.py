class Namespace:
    def __init__(self, dict={}, **kwargs):
        for key, value in dict.items():
            self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def set(self, key, value):
        setattr(self, key, value)
    
    def get(self, key):
        return getattr(self, key)
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)