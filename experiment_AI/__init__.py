from otree.api import *
from settings import Maxround,AI_REF_SET
import random

doc = """
Your app description
"""



class C(BaseConstants):
    NAME_IN_URL = 'experiment_AI'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = Maxround

    NEWS = '../_templates/global/News_template.html'
    REFS = '../_templates/global/AI_Refs.html'

    SLIDER_STYLE = '../_static/global/mgslider_style.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess_1 = models.IntegerField(
        min=0, max=100, label="Please pick a number from 0 to 100:"
    )
    guess_2 = models.IntegerField(
        min=0, max=100, label="Please pick a number from 0 to 100:",
    )
    AI_reference = models.IntegerField()
    timeout_1 = models.BooleanField(initial=False)
    timeout_2 = models.BooleanField(initial=False)

    guess_1_check = models.IntegerField(initial=999)
    guess_2_check = models.IntegerField(initial=999)


# Functions
#Save guess data to participant.Guess_set
 ## every round, generate a list to save the 2 guess and reference.
    ### then save the list_per_round into the participant.Guess_set（list）
def Save_guess(player:Player):

        guess_per_round    = []

        if player.guess_1_check == 1:
            guess_per_round.append(player.guess_1)
        else:
            guess_per_round.append('N')

        if player.guess_2_check == 1:
            guess_per_round.append(player.guess_2)
        else:
            guess_per_round.append('N')
 
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
    timeout_seconds = 30

class Guess1(Page):
    timeout_seconds = 30
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
    timeout_seconds = 10
    @staticmethod
    def vars_for_template(player: Player):
        numq = player.round_number-1
        Refer = AI_REF_SET[numq]
        player.AI_reference = Refer
        return dict(
        Refer = Refer
    )

class Guess2(Page):
    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['guess_2','guess_2_check']
    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            # you may want to fill a default value for any form fields,
            # because otherwise they may be left null.
            player.timeout_2 = True

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


page_sequence = [ Round_1, News, Guess1, Wait, Reference, Guess2, Wait2, Finish_Round, Finish_Task]












