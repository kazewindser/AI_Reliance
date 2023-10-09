from otree.api import *
from settings import Maxround
import random

doc = """
Your app description
"""



class C(BaseConstants):
    NAME_IN_URL = 'experiment_human'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = Maxround

    NEWS = '../_templates/global/News_template.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess_1 = models.IntegerField(
        min=0, max=100, initial = -1,
    )
    guess_2 = models.IntegerField(
        min=0, max=100, initial = -1,
    )
    random_reference = models.IntegerField()


# Functions

#Find a random reference
def Refer_generate(player:Player):
    players = player.get_others_in_group()
    guess1_s = []

    for p in players:
        # if p.guess_1_check == 1:
        #     guess1_s.append(p.guess_1)
        guess1_s.append(p.guess_1)
        
    if guess1_s == []:
        Refer = []
        Refer.append(random.randint(1,100))
    else:
        Refer =  random.sample(guess1_s,1)

    return Refer[0]

#Save guess data to participant.Guess_set
 ## every round, generate a list to save the 2 guess and reference.
    ### then save the list_per_round into the participant.Guess_set（list）
# def Save_guess(player:Player):

#         guess_per_round    = []

#         if player.guess_1_check == 1:
#             guess_per_round.append(player.guess_1)
#         else:
#             guess_per_round.append('N')

#         if player.guess_2_check == 1:
#             guess_per_round.append(player.guess_2)
#         else:
#             guess_per_round.append('N')
 
#         guess_per_round.append(player.random_reference)
#         player.participant.Guess_set[player.round_number-1] = guess_per_round
def Save_guess(player:Player):

        guess_per_round    = []

        guess_per_round.append(player.guess_1)
        guess_per_round.append(player.guess_2)
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
    # timeout_seconds = 30
    pass

class Guess1(Page):
    # timeout_seconds = 30
    form_model = 'player'
    form_fields = ['guess_1']


class Wait(WaitPage):
    pass

class Reference(Page):
    # timeout_seconds = 10
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        Refer = Refer_generate(player)
        player.random_reference = Refer
        return dict(
        Refer = Refer
    )

class Guess2(Page):
    # timeout_seconds = 30
    form_model = 'player'
    form_fields = ['guess_2']

class Wait2(WaitPage):
    pass

class Finish_Round(Page):
    timeout_seconds = 1
    @staticmethod
    def is_displayed(player):
        Save_guess(player)
        return player.round_number < Maxround
    @staticmethod
    def vars_for_template(player: Player):
        numq = player.round_number+1
        return dict(
        numq = numq
    )

class Finish_Task(Page):
    @staticmethod
    def is_displayed(player):
        Save_guess(player)
        return player.round_number == Maxround


page_sequence = [ Round_1, News, Guess1, Wait, Reference, Guess2, Wait2, Finish_Round, Finish_Task ]












