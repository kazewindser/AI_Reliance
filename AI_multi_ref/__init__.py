from otree.api import *
from settings import Maxround, MULTI_AI_REF_SET
import random, time

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

    #parameter to count time
    time_readnews = models.FloatField()  
    time_guess_1 = models.FloatField()  
    # time_readref = models.IntegerField()  
    time_guess_2 = models.FloatField()

    start = models.FloatField()
    end = models.FloatField()  

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

def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'label', 'round_number', 'id_in_group',
    'guess_1','AI_ref','guess_2',
    'time_readnews','time_guess_1','time_guess_2']

    for p in players:
        participant = p.participant
        session = p.session
        yield [
        session.code, participant.code, participant.label, p.round_number, p.id_in_group, 
        p.guess_1, p.AI_reference, p.guess_2,
        p.time_readnews, p.time_guess_1, p.time_guess_2
        ]




# PAGES
class Round_1(Page):
    timeout_seconds = 0.8
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            player.participant.Guess_set = ['NN']*Maxround   #在一开始赋值总数据列表
        return player.round_number == 1
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.start = time.time()

class News(Page):
    @staticmethod
    def is_displayed(player):
        player.start = time.time()
        Gen_AIref(player)
        return player.round_number <= Maxround
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.end = time.time()
        time_readnews = player.end - player.start
        player.time_readnews = float(format(time_readnews,'.1f'))
        player.start = time.time()
    
class Guess1(Page):
    # timeout_seconds = 30
    form_model = 'player'
    form_fields = ['guess_1']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.end = time.time()
        time_guess_1 = player.end - player.start
        player.time_guess_1 = float(format(time_guess_1, '.1f'))
        player.start = time.time()

class Wait(WaitPage):
    pass

class Reference(Page):
    timeout_seconds = 5
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
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.start = time.time()

class Guess2(Page):
    # timeout_seconds = 30
    form_model = 'player'
    form_fields = ['guess_2']
    def before_next_page(player: Player, timeout_happened):
        player.end = time.time()
        time_guess_2 = player.end - player.start
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


page_sequence = [ Round_1, News, Guess1, Reference, Guess2, Finish_Round, Finish_Task]












