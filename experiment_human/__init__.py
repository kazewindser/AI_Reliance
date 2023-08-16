from otree.api import *
import random

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
    guess_1 = models.IntegerField(
        min=0, max=100, label="Please pick a number from 0 to 100:"
    )
    guess_2 = models.IntegerField(
        min=0, max=100, label="Please pick a number from 0 to 100:"
    )
    random_reference = models.IntegerField()

# Functions

#find a random reference
def Refer_generate(player:Player):
    players = player.get_others_in_group()
    guesses = [p.guess_1 for p in players]
    Refers =  random.sample(guesses,1)
    return Refers[0]



# PAGES
class News(Page):
    pass

class Guess1(Page):
    form_model = 'player'
    form_fields = ['guess_1']


class Wait(WaitPage):
    pass

class Reference(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        Refer = Refer_generate(player)
        player.random_reference = Refer
        return dict(
        Refer = Refer
    )

class Guess2(Page):
    form_model = 'player'
    form_fields = ['guess_2']



page_sequence = [ News, Guess1, Wait, Reference, Guess2 ]












