from otree.api import *
from ._lexicon_q import Lexicon

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        min=17, max=100,
        label = Lexicon.q_age
    )
    gender = models.IntegerField(
        label = Lexicon.q_gender,
        choices = Lexicon.q_gender_opts
    )
    lan_jp = models.IntegerField(
        label = Lexicon.q_lan_jp,
        choices = Lexicon.q_lan_jp_opts
    )
    affiliate = models.IntegerField(
        label = Lexicon.q_affiliate,
        choices = Lexicon.q_affiliate_opts
    )
    chatGPT = models.IntegerField(
        label = Lexicon.q_chatGPT,
        choices = Lexicon.q_chatGPT_opts
    )
    chatGPT_times = models.IntegerField(min=0, max=7,label = '週平均で何日間ChatGPTを使用していますか？(０から７までの整数を入力してください)')
    programming = models.IntegerField(
        label = Lexicon.q_programming,
        choices = Lexicon.q_programming_opts
    )
    AIorHUMAN = models.IntegerField(
        label = Lexicon.q_AIorHUMAN,
        choices = Lexicon.q_AIorHUMAN_opts
    )

# PAGES
def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'label',  'id_in_group',
    'age','gender','lan_jp',
    'affiliate','chatGPT','chatGPT_times','programming','AIorHUMAN']
    for p in players:
        participant = p.participant
        session = p.session
        yield [
        session.code, participant.code, participant.label,  p.id_in_group, 
        p.age, p.gender, p.lan_jp,
        p.affiliate, p.chatGPT, p.chatGPT_times,p.programming,p.AIorHUMAN
        ]      


class Questions(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','lan_jp',
                    'affiliate','chatGPT','chatGPT_times',
                    'programming','AIorHUMAN']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            Lexicon=Lexicon,
        )

page_sequence = [Questions]
