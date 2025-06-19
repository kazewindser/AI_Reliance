from otree.api import *
from settings import Maxround,EXPERT_ADVICE
import random, time

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
    Expert_advice = models.IntegerField()
    Expert_source = models.IntegerField()

    #parameter to count time
    time_readnews = models.FloatField()  
    time_guess_1 = models.FloatField()  
    # time_readref = models.IntegerField()  
    time_guess_2 = models.FloatField()

    start = models.FloatField()
    end = models.FloatField()  


# Functions

# #Find a random reference
# def Refer_generate(player:Player):
#     players = player.get_others_in_group()
#     guess1_s = []
#
#     for p in players:
#         guess1_s.append(p.guess_1)
#
#     if guess1_s == []:
#         Refer = []
#         Refer.append(random.randint(1,100))
#     else:
#         Refer =  random.sample(guess1_s,1)
#
#     return Refer[0]


def GenExpertAdvice(player: Player):
    current_round_data = EXPERT_ADVICE.iloc[player.round_number-1]
    # 获取非NA值的索引
    valid_indices = current_round_data.dropna().index
    # 随机选择一个索引
    chosen_index = random.choice(valid_indices)
    # 获取对应的值
    player.Expert_advice = int(current_round_data[chosen_index])
    # 保存列索引（从1开始计数）
    # 获取列名列表中的位置，而不是直接使用列名
    player.Expert_source = list(EXPERT_ADVICE.columns).index(chosen_index) + 1




def Save_guess(player:Player):

        guess_per_round    = []

        guess_per_round.append(player.guess_1)
        guess_per_round.append(player.guess_2)
        guess_per_round.append(player.Expert_advice)
        player.participant.Guess_set[player.round_number-1] = guess_per_round

def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'label', 'round_number', 'id_in_group','guess_1','expert_advice','guess_2',
    'time_readnews','time_guess_1','time_guess_2']
    for p in players:
        participant = p.participant
        session = p.session
        yield [
        session.code, participant.code, participant.label, p.round_number, p.id_in_group, 
        p.guess_1, p.Expert_advice, p.guess_2,
        p.time_readnews, p.time_guess_1, p.time_guess_2
        ]      



# PAGES
class Round_1(Page):
    timeout_seconds = 0.8
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            player.participant.Guess_set = ['NN']*30   #在一开始赋值总数据列表
        return player.round_number == 1
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.start = time.time()

class News(Page):
    # timeout_seconds = 30
    @staticmethod
    def is_displayed(player):
        player.start = time.time()
        return player.round_number <= Maxround
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.end = time.time()
        time_readnews = player.end - player.start
        player.time_readnews = float(format(time_readnews,'.1f'))
        player.start = time.time()

class Guess1(Page):
    form_model = 'player'
    form_fields = ['guess_1']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.end = time.time()
        time_guess_1 = player.end - player.start
        player.time_guess_1 = float(format(time_guess_1,'.1f'))
        player.start = time.time()


class Wait(WaitPage):
    pass

class Reference(Page):
    timeout_seconds = 10
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        GenExpertAdvice(player)
        Refer = player.Expert_advice
        return dict(
        Refer = Refer
    )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.start = time.time()

class Guess2(Page):
    # timeout_seconds = 30
    form_model = 'player'
    form_fields = ['guess_2']
    def before_next_page(player: Player, timeout_happened):
        player.end = time.time()
        time_guess_2= player.end - player.start
        player.time_guess_2 = float(format(time_guess_2,'.1f')) 
        player.start = time.time()

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