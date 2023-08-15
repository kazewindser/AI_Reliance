from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class News(Page):
    pass

class Guess1(Page):
    pass

class Wait(WaitPage):
    pass

class Reference(Page):
    pass

class Guess2(Page):
    pass


page_sequence = [ News, Guess1, Reference, Guess2 ]












