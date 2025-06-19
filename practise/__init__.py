from otree.api import *

import random

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'slider_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess_1 = models.IntegerField(initial=-1)
    guess_2 = models.IntegerField(initial=-1)
    random_reference = models.IntegerField(initial=-1)


# Functions

#Find a random reference
def Refer_generate(player:Player):
    players = player.get_others_in_group()
    guess1_s = []
    for p in players:
        guess1_s.append(p.guess_1)
    if guess1_s == []:
        Refer = []
        Refer.append(random.randint(1,100))
    else:
        Refer =  random.sample(guess1_s,1)

    return Refer[0]



# PAGES
class p_Start(Page):
    # timeout_seconds = 1
    pass

class p_News(Page):
    # timeout_seconds = 30
    pass

class p_Guess1(Page):
    # timeout_seconds = 30
    form_model = 'player'
    # form_fields = ['guess_1','guess_1_check']
    form_fields = ['guess_1']


#此页面必要因为需要提取reference
class Wait(WaitPage):
    pass

class p_Reference(Page):
    timeout_seconds = 10
    @staticmethod
    def vars_for_template(player: Player):
        inAI = player.session.config['AI']
        return dict(
        inAI = inAI
    )

class p_Guess2(Page):
    # timeout_seconds = 30
    form_model = 'player'
    form_fields = ['guess_2']

    @staticmethod
    def vars_for_template(player: Player):
        inAI = player.session.config['AI']
        return dict(
        inAI = inAI
    )

class Wait2(WaitPage):
    pass

class p_Finish(Page):
    @staticmethod
    def vars_for_template(player:Player):
        p_g1 = player.guess_1
        p_g2 = player.guess_2

        
        return dict(
            p_g1 = p_g1,
            p_g2 = p_g2
        )



page_sequence = [p_Start, p_News, p_Guess1, Wait, p_Reference, p_Guess2, p_Finish, Wait2]












