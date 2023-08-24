from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'quiz'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    WAIT = True

    SLIDE_HUMAN = '../_templates/global/Slide_human.html'
    HIDDEN_SLIDE_HUMAN =  '../_templates/global/Hidden_Slide_human.html'

    # 二択問題の選択肢
    TF = [[True, Lexicon.true],
        [False, Lexicon.false]]
    # 問題番号と問題の対応
    q_dict = {1:['q1'], 2:['q2'], 3:['q3'], 4:['q4'],
        5:['q5_1', 'q5_2'], 6:['q6_1', 'q6_2']}
    # 各問題について選択肢の種類と正答
    corrects = {
        'q1': {'opt': TF, 'correct': False},
        'q2': {'opt': TF, 'correct': True},
        'q3': {'opt': TF, 'correct': False},
        'q4': {'opt': TF, 'correct': False},
        'q5_1': {'opt': Lexicon.questions['q5_1']['opt'], 'correct': 1},
        'q5_2': {'opt': Lexicon.questions['q5_2']['opt'], 'correct': 2},
        'q6_1': {'opt': Lexicon.questions['q6_1']['opt'], 'correct': 2},
        'q6_2': {'opt': Lexicon.questions['q6_2']['opt'], 'correct': 4}
    }

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
