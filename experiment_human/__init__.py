from otree.api import *
from settings import Maxround
import random

doc = """
Your app description
"""



class C(BaseConstants):
    NAME_IN_URL = 'experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = Maxround


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

#Find a random reference
def Refer_generate(player:Player):
    players = player.get_others_in_group()
    guesses = [p.guess_1 for p in players]
    Refers =  random.sample(guesses,1)
    return Refers[0]

#Save guess data to participant.Guess_set
 ## every round, generate a list to save the 2 guess and reference.
    ### then save the list_per_round into the participant.Guess_set（list）
def Save_guess(player:Player):
        guess_per_round    = []
        guess_per_round.append(player.guess_1)
        guess_per_round.append(player.guess_2)
        guess_per_round.append(player.random_reference)
        player.participant.Guess_set.append(guess_per_round)



# PAGES
class Round_1(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            player.participant.Guess_set = []   #在一开始赋值总数据列表
        return player.round_number == 1

class News(Page):
    pass

class Guess1(Page):
    form_model = 'player'
    form_fields = ['guess_1']

#此页面必要因为需要提取reference
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


class Finish(Page):
    @staticmethod
    def vars_for_template(player:Player):
        Save_guess(player)
        a = player.round_number +1
        b = Maxround+1
        return dict(
            a = a,
            b = b
        )



page_sequence = [ Round_1, News, Guess1, Wait, Reference, Guess2, Finish]












