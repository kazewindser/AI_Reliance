from otree.api import *
from ._lexicon import Lexicon


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'quiz'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 100
    # クイズ終了後他の参加者を待つときはTrueとする
    WAIT = True

    SLIDE_HUMAN = '../_templates/global/Slide_human.html'
    HIDDEN_SLIDE_HUMAN =  '../_templates/global/Hidden_Slide_human.html'

    # 二択問題の選択肢
    TF = [[True, Lexicon.true],
        [False, Lexicon.false]]
    # 問題番号と問題の対応
    q_dict = {1:['q1'], 2:['q2'], 3:['q3'], 4:['q4'],5:['q5']}
    # 各問題について選択肢の種類と正答
    corrects = {
        'q1': {'opt': TF, 'correct': True},
        'q2': {'opt': TF, 'correct': True},
        'q3': {'opt': TF, 'correct': False},
        'q4': {'opt': TF, 'correct': False},
        'q5': {'opt': Lexicon.questions['q5']['opt'], 'correct': 2},
    }

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

# -------------------- class Player -------------------- #
class Player(BasePlayer):
    numq = models.IntegerField(initial=1)
    wait = models.BooleanField(initial=False)

for k, v in C.corrects.items():
    if v['opt'] == C.TF:
        v['field'] = models.BooleanField
    else:
        v['field'] = models.IntegerField
    setattr(    # k = models.IntegerField(choices=...)と等価
        Player,
        k,
        v['field'](
            choices=v['opt'],
            widget=widgets.RadioSelect,
            label=Lexicon.questions[k]['question'],
        )
    )
# -------------------- class Player -------------------- #

# FUNCTIONS
def judge(player: Player):
    judges = []
    for key in C.q_dict.get(player.numq):
        answer = getattr(player, key)
        correct = C.corrects[key]['correct']
        judges.append(answer == correct)
    return all(judges)



# PAGES
class Start(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Quiz(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            Lexicon=Lexicon,
            numq = player.numq
        )
    @staticmethod
    def get_form_fields(player: Player):
        return C.q_dict[player.numq]

class Incorrect(Page):
    @staticmethod
    def is_displayed(player: Player):
        return judge(player) == False
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            Lexicon=Lexicon,
            numq = player.numq,
            comms = [Lexicon.questions[q]['comment'] for q in C.q_dict[player.numq]]
        )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        next = player.in_round(player.round_number + 1)
        next.numq = player.numq
        return

class Correct(Page):
    @staticmethod
    def is_displayed(player: Player):
        return judge(player) == True
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            Lexicon=Lexicon,
            numq = player.numq,
            comms = [Lexicon.questions[q]['comment'] for q in C.q_dict[player.numq]]
        )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        next = player.in_round(player.round_number + 1)
        next.numq = player.numq + 1
        return
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.numq == 5:
            player.wait = True
            if C.WAIT == True:
                pass
            else:
                return upcoming_apps[0]
    


class Wait(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.wait
    
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return upcoming_apps[0]


class Results(Page):
    pass


page_sequence = [Start, Quiz,Incorrect,Correct, Wait]
