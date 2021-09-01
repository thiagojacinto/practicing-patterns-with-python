# encoding=utf8

def additional_three(target):
    """Decorator that adds 3 units to the target function"""
    def wrapper(self, value):
        return target(self, value) + 3
    
    return wrapper