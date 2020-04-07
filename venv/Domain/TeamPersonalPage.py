class TeamPersonalPage:

    def __init__(self):
        raise NotImplementedError

def type_check(obj):

    if type(obj) is not TeamPersonalPage:
        raise TypeError