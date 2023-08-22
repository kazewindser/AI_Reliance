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
        min=-1, max=100, label="Please pick a number from 0 to 100:"
    )
    guess_2 = models.IntegerField(
        min=-1, max=100, label="Please pick a number from 0 to 100:",
    )
    random_reference = models.IntegerField()
    timeout_1 = models.BooleanField(initial=False)
    timeout_2 = models.BooleanField(initial=False)

    guess_1_check = models.IntegerField()


# Functions

#Find a random reference
def Refer_generate(player:Player):
    players = player.get_others_in_group()
    guess1_s = []
    for p in players:
        if p.timeout_1 == False:
            guess1_s.append(p.guess_1)
        else:
            if p.guess_1 != 0:
                guess1_s.append(p.guess_1)

    Refer =  random.sample(guess1_s,1)


    return Refer[0]

#Save guess data to participant.Guess_set
 ## every round, generate a list to save the 2 guess and reference.
    ### then save the list_per_round into the participant.Guess_set（list）
def Save_guess(player:Player):

        guess_per_round    = []

        if player.timeout_1 == False:
            guess_per_round.append(player.guess_1)
        else: #when there exist a timeout
            if player.guess_1 == 0:       #if there is no input (when timeout)
                guess_per_round.append('X')
            else:                          #if there is a input (when timeout)
                guess_per_round.append(player.guess_1)
            player.timeout_1 = False 

        if player.timeout_2 == False:
            guess_per_round.append(player.guess_2)
        else:
            if player.guess_2 == 0:
                guess_per_round.append('X')
            else:
                guess_per_round.append(player.guess_2)
            player.timeout_2 = False
 
        guess_per_round.append(player.random_reference)
        player.participant.Guess_set[player.round_number-1] = guess_per_round
      



# PAGES
class Round_1(Page):
    timeout_seconds = 0.8
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            player.participant.Guess_set = ['NN']*45   #在一开始赋值总数据列表
        return player.round_number == 1

class News(Page):
    timeout_seconds = 5

class Guess1(Page):
    timeout_seconds = 16
    form_model = 'player'
    form_fields = ['guess_1', 'guess_1_check']
    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            # you may want to fill a default value for any form fields,
            # because otherwise they may be left null.
            player.timeout_1 = True

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
    timeout_seconds = 60
    form_model = 'player'
    form_fields = ['guess_2']
    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            # you may want to fill a default value for any form fields,
            # because otherwise they may be left null.
            player.timeout_2 = True


class Finish(Page):
    timeout_seconds = 0.8
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












