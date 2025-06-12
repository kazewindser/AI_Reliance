from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'instruction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    SLIDE_HUMAN = '../_templates/global/Slide_human.html'
    SLIDE_AI = '../_templates/global/Slide_AI.html'
    SLIDE_preHUMAN = '../_templates/global/Slide_preHuman.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Waitplease(Page):
    pass

class Instruction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        inAI = player.session.config['AI']
        return dict(
        inAI = inAI
    )



page_sequence = [Waitplease,Instruction]
