import Domain.TeamUser as TeamUser


class Team:

    def __init__(self, name, league, team_members=[]):

        if type(name) is not str:
            raise TypeError

        self._team_members = []
        self.add_team_members(team_members)
        self._name = name
        self._league = league
        self._games = []

    def add_team_members(self, team_members):

        if type(team_members) is not list:
            raise TypeError

        for team_member in team_members:
            self.add_team_member(team_member)

    def add_team_member(self, team_member):

        TeamUser.is_team_user(team_member)
        if team_member in self._team_members:
            raise ValueError

        self._team_members.append(team_member)

    def remove_team_members(self, team_members):
        # who can use it?
        if type(team_members) is not list:
            raise TypeError

        for team_member in team_members:
            self.remove_team_member(team_member)

    def remove_team_member(self, team_member):
        # who can use it?
        TeamUser.is_team_user(team_member)
        if team_member not in self._team_members:
            raise ValueError

        self._team_members.remove(team_member)


def type_check(obj):

    if type(obj) is not Team:
        raise TypeError
