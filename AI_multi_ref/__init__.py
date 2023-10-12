from otree.api import *
from settings import Maxround, AI_REF_SET, MULTI_AI_REF_SET
import random

doc = """
Your app description
"""



class C(BaseConstants):
    NAME_IN_URL = 'experiment_AI_multi_ref'
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
    AI_ref_id = models.IntegerField()
    AI_reference = models.IntegerField()

# Functions
# Find a random reference

def Gen_AIref(player:Player):
    round_id = player.round_number-1
    ref_id = random.randint(0,23)

    player.AI_ref_id = ref_id+1
    player.AI_reference = int(MULTI_AI_REF_SET.iloc[round_id, ref_id])


def Save_guess(player:Player):
    guess_per_round    = []
    guess_per_round.append(player.guess_1)
    guess_per_round.append(player.guess_2)
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
    @staticmethod
    def is_displayed(player):
        Gen_AIref(player)
        return player.round_number < Maxround
    
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
        numq = player.round_number-1
        Refer = player.AI_reference
        ref_id = player.AI_ref_id
        return dict(
        Refer = Refer,
        ref_id = ref_id,
        image_path='AI_REF/{}/{}.png'.format(player.round_number,ref_id)
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


page_sequence = [ Round_1, News, Guess1, Reference, Guess2, Finish_Round, Finish_Task]












