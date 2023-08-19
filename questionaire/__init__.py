from otree.api import *
from settings import REAL_RESULT, Maxround
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



# PAGES
class Q1(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Q1, Results]
