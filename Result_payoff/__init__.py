from otree.api import *
from settings import REAL_RESULT, Maxround
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Result'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_round = models.IntegerField()
    selected_guess = models.IntegerField()

    real_result = models.IntegerField() #100r
    R = models.IntegerField()

#Functions

def set_selection(player:Player):  #500+max{0, 2000-0.3(R-100r)^2}=?円
    player.selected_round = random.randint(1,Maxround)
    player.selected_guess = random.randint(1,2)

    a = player.selected_round
    b = player.selected_guess
    player.real_result = REAL_RESULT[a-1]
    player.R = player.participant.Guess_set[a-1][b-1]

def set_payoff(player:Player):    #500+max{0, 2000-0.3(R-100r)^2}=?円
    a = 2000-0.3*(player.R-player.real_result)**2
    player.payoff = max(0,a)


# PAGES
class Results_show(Page):
    @staticmethod
    def vars_for_template(player: Player):
        set_selection(player) 
        return dict(
            )

class Final_Payoff(Page):
    @staticmethod
    def vars_for_template(player: Player):
        set_payoff(player) 
        return dict(
            )
class Thanks(Page):
    pass


page_sequence = [Results_show, Final_Payoff, Thanks]
