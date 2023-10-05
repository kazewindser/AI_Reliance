from otree.api import *

import random

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'slider_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    SLIDER_STYLE = '../_static/global/mgslider_style.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess_1 = models.IntegerField()
    guess_2 = models.IntegerField()
    random_reference = models.IntegerField()
    timeout_1 = models.BooleanField(initial=False)
    timeout_2 = models.BooleanField(initial=False)


    guess_1_check = models.IntegerField(initial=999)
    guess_2_check = models.IntegerField(initial=999)


# Functions

#Find a random reference
def Refer_generate(player:Player):
    players = player.get_others_in_group()
    guess1_s = []
    for p in players:
        if p.guess_1_check == 1:
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
    form_fields = ['guess_1','guess_1_check']
    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            # you may want to fill a default value for any form fields,
            # because otherwise they may be left null.
            player.timeout_1 = True

#此页面必要因为需要提取reference
class Wait(WaitPage):
    pass

class p_Reference(Page):
    # timeout_seconds = 10
    @staticmethod
    def vars_for_template(player: Player):
        inAI = player.session.config['AI']
        if inAI == False:
            Refer = Refer_generate(player)      
            player.random_reference = Refer
        else:
            Refer = 'Now in AI Group'
        return dict(
        Refer = Refer,
        inAI = inAI
    )

class p_Guess2(Page):
    # timeout_seconds = 30
    form_model = 'player'
    form_fields = ['guess_2','guess_2_check']
    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            # you may want to fill a default value for any form fields,
            # because otherwise they may be left null.
            player.timeout_2 = True
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
        if player.guess_1_check == 1:
            p_g1 = player.guess_1
        else:
            p_g1 = 'N'

        if player.guess_2_check == 1:
            p_g2 = player.guess_2
        else:
            p_g2 = 'N'

        return dict(
            p_g1 = p_g1,
            p_g2 = p_g2
        )



page_sequence = [ p_Start, p_News, p_Guess1, Wait, p_Reference, p_Guess2, p_Finish, Wait2]












