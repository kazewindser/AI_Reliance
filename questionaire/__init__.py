from otree.api import *
from settings import REAL_RESULT
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

#Functions
def set_payoffs(player:Player):

    #Randomly select round and guess
    player.participant.selected_round = random.randint(1, 45)
    player.participant.selected_guess = random.randint(1,2)

    # # Get the real result of that round 
    # a = player.participant.selected_round
    # b = player.participant.selected_guess
    # selected_real_result = REAL_RESULT[a-1]

    # #Calculate the payoff
    # guess_of_selected_round = player.participant.Guess_set
    # player.participant.Payoff =     

# PAGES
class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        set_payoffs(player)


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, Results]
