import random
import os
import time
import sys

mission_spec = [2, 3, 3, 4, 4]
fail_spec = [1, 1, 1, 2, 1]

roles = ['morgana', 'assassin', 'oberon', 'merlin', 'percival'] + (['vt'] * 2)

class Game:
    def __init__(self, roles, mission_spec, fail_spec):
        self.roles = roles
        self.mission_spec = mission_spec
        self.fail_spec = fail_spec
        self.mission_fails = [] # will be filled as game goes on

    def assign_roles(self):
        random.shuffle(self.roles)
        for role in self.roles:
            print('Only one person looks at the screen. Press enter to see your role')
            input()
            print('Your role is %s. Pless enter to clear' % role)
            input()
            os.system('clear')
        print('All roles have been assigned. Enter to continue')

    def vote_on_mission(self):
        current_mission = len(self.mission_fails)
        print('Mission number {0}, {1} Pariticpants, {2} Fails needed'\
                .format(current_mission+1, self.mission_spec[current_mission], self.fail_spec[current_mission])
            )
        print('Each person, enter your vote')
        num_fails = 0
        for _ in range(self.mission_spec[current_mission]):
            vote = None
            while vote != 'S' and vote != 'F':
                print('Enter S for success, F for fail')
                vote = str(input()).upper()
            if vote.upper() == 'F':
                num_fails += 1
            print('Your vote has been recorded. Press enter to clear. Thank you')
            input()
            os.system('clear')
        self.mission_fails.append(num_fails)

    def print_game_state(self):
        print('Missions Spec: {0}'.format(self.mission_spec))
        print('Fail Count: {0}'.format(self.mission_fails))

if __name__ == '__main__':
    g = Game(roles, mission_spec, fail_spec)
    g.assign_roles()
    g.print_game_state()
    for _ in range(len(g.mission_spec)):
        g.vote_on_mission()
        g.print_game_state()

