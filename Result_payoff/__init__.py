from otree.api import *
from settings import REAL_RESULT, Maxround
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Result'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    FINALRESULT_TEMPLATE = '../_templates/global/Final_result.html'
    HIDDEN_FINALRESULT_TEMPLATE = '../_templates/global/Hidden_Final_result.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_round = models.IntegerField()
    selected_guess = models.IntegerField()

    real_result = models.IntegerField() #100r
    R = models.IntegerField(initial = -1)

#Functions

def set_selection(player:Player):  #500+max{0, 2000-0.3(R-100r)^2}=?円
        player.selected_round = random.randint(1,Maxround)
        player.selected_guess = random.randint(1,2)


def set_additional_payoff(player:Player):    #max{0, 2000-0.3(R-100r)^2}=?円
    a = player.selected_round
    b = player.selected_guess
    selcted_R = player.participant.Guess_set[a-1][b-1]
    player.real_result = REAL_RESULT[a-1]

    if selcted_R == 'N':
        player.payoff = 0
    else:
        player.R = selcted_R    
        ad_pay = 2300-0.3*(player.R-player.real_result)**2
        player.payoff = max(0,ad_pay)

def round_up_to_tens(n):
    if n == 0:
        return 0
    return ((n + 9) // 10) * 10

def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'label', 'Final_Payoff']
    for p in players:
        participant = p.participant
        session = p.session
        FINAL_PAYOFF = round_up_to_tens(participant.payoff_plus_participation_fee())
        yield [
        session.code, participant.code, participant.label, FINAL_PAYOFF
        ]      


# PAGES
class Results_show(Page):
    @staticmethod
    def vars_for_template(player: Player):
        set_selection(player) 

        GS = player.participant.Guess_set
        return dict(
            r1 = REAL_RESULT[0],r2 = REAL_RESULT[1],r3 = REAL_RESULT[2],r4 = REAL_RESULT[3],r5 = REAL_RESULT[4],
            r6 = REAL_RESULT[5],r7 = REAL_RESULT[6],r8 = REAL_RESULT[7],r9 = REAL_RESULT[8],r10 = REAL_RESULT[9] ,

            r11 = REAL_RESULT[10],r12 = REAL_RESULT[11],r13 = REAL_RESULT[12],r14 = REAL_RESULT[13],r15 = REAL_RESULT[14],
            r16 = REAL_RESULT[15],r17 = REAL_RESULT[16],r18 = REAL_RESULT[17],r19 = REAL_RESULT[18],r20 = REAL_RESULT[19] ,

            r21 = REAL_RESULT[20],r22 = REAL_RESULT[21],r23 = REAL_RESULT[22],r24 = REAL_RESULT[23],r25 = REAL_RESULT[24],
            r26 = REAL_RESULT[25],r27 = REAL_RESULT[26],r28 = REAL_RESULT[27],r29 = REAL_RESULT[28],r30 = REAL_RESULT[29] ,

            g1_1 = GS[0][0],g1_2 = GS[0][1], g2_1 = GS[1][0],g2_2 = GS[1][1], g3_1 = GS[2][0],g3_2 = GS[2][1], g4_1 = GS[3][0],g4_2 = GS[3][1], g5_1 = GS[4][0],g5_2 = GS[4][1],
            g6_1 = GS[5][0],g6_2 = GS[5][1], g7_1 = GS[6][0],g7_2 = GS[6][1], g8_1 = GS[7][0],g8_2 = GS[7][1], g9_1 = GS[8][0],g9_2 = GS[8][1], g10_1 = GS[9][0],g10_2 = GS[9][1],

            g11_1 = GS[10][0],g11_2 = GS[10][1], g12_1 = GS[11][0],g12_2 = GS[11][1], g13_1 = GS[12][0],g13_2 = GS[12][1], g14_1 = GS[13][0],g14_2 = GS[13][1], g15_1 = GS[14][0],g15_2 = GS[14][1],
            g16_1 = GS[15][0],g16_2 = GS[15][1], g17_1 = GS[16][0],g17_2 = GS[16][1], g18_1 = GS[17][0],g18_2 = GS[17][1], g19_1 = GS[18][0],g19_2 = GS[18][1], g20_1 = GS[19][0],g20_2 = GS[19][1],
            
            g21_1 = GS[20][0],g21_2 = GS[20][1], g22_1 = GS[21][0],g22_2 = GS[21][1], g23_1 = GS[22][0],g23_2 = GS[22][1], g24_1 = GS[23][0],g24_2 = GS[23][1], g25_1 = GS[24][0],g25_2 = GS[24][1],
            g26_1 = GS[25][0],g26_2 = GS[25][1], g27_1 = GS[26][0],g27_2 = GS[26][1], g28_1 = GS[27][0],g28_2 = GS[27][1], g29_1 = GS[28][0],g29_2 = GS[28][1], g30_1 = GS[29][0],g30_2 = GS[29][1],
             
            )

class Final_Payoff(Page):
    @staticmethod
    def vars_for_template(player: Player):
        set_additional_payoff(player) 

        GS = player.participant.Guess_set
        return dict(
            r1 = REAL_RESULT[0],r2 = REAL_RESULT[1],r3 = REAL_RESULT[2],r4 = REAL_RESULT[3],r5 = REAL_RESULT[4],
            r6 = REAL_RESULT[5],r7 = REAL_RESULT[6],r8 = REAL_RESULT[7],r9 = REAL_RESULT[8],r10 = REAL_RESULT[9] ,

            r11 = REAL_RESULT[10],r12 = REAL_RESULT[11],r13 = REAL_RESULT[12],r14 = REAL_RESULT[13],r15 = REAL_RESULT[14],
            r16 = REAL_RESULT[15],r17 = REAL_RESULT[16],r18 = REAL_RESULT[17],r19 = REAL_RESULT[18],r20 = REAL_RESULT[19] ,

            r21 = REAL_RESULT[20],r22 = REAL_RESULT[21],r23 = REAL_RESULT[22],r24 = REAL_RESULT[23],r25 = REAL_RESULT[24],
            r26 = REAL_RESULT[25],r27 = REAL_RESULT[26],r28 = REAL_RESULT[27],r29 = REAL_RESULT[28],r30 = REAL_RESULT[29] ,

            g1_1 = GS[0][0],g1_2 = GS[0][1], g2_1 = GS[1][0],g2_2 = GS[1][1], g3_1 = GS[2][0],g3_2 = GS[2][1], g4_1 = GS[3][0],g4_2 = GS[3][1], g5_1 = GS[4][0],g5_2 = GS[4][1],
            g6_1 = GS[5][0],g6_2 = GS[5][1], g7_1 = GS[6][0],g7_2 = GS[6][1], g8_1 = GS[7][0],g8_2 = GS[7][1], g9_1 = GS[8][0],g9_2 = GS[8][1], g10_1 = GS[9][0],g10_2 = GS[9][1],

            g11_1 = GS[10][0],g11_2 = GS[10][1], g12_1 = GS[11][0],g12_2 = GS[11][1], g13_1 = GS[12][0],g13_2 = GS[12][1], g14_1 = GS[13][0],g14_2 = GS[13][1], g15_1 = GS[14][0],g15_2 = GS[14][1],
            g16_1 = GS[15][0],g16_2 = GS[15][1], g17_1 = GS[16][0],g17_2 = GS[16][1], g18_1 = GS[17][0],g18_2 = GS[17][1], g19_1 = GS[18][0],g19_2 = GS[18][1], g20_1 = GS[19][0],g20_2 = GS[19][1],
            
            g21_1 = GS[20][0],g21_2 = GS[20][1], g22_1 = GS[21][0],g22_2 = GS[21][1], g23_1 = GS[22][0],g23_2 = GS[22][1], g24_1 = GS[23][0],g24_2 = GS[23][1], g25_1 = GS[24][0],g25_2 = GS[24][1],
            g26_1 = GS[25][0],g26_2 = GS[25][1], g27_1 = GS[26][0],g27_2 = GS[26][1], g28_1 = GS[27][0],g28_2 = GS[27][1], g29_1 = GS[28][0],g29_2 = GS[28][1], g30_1 = GS[29][0],g30_2 = GS[29][1],
            )

class Thanks(Page):
    pass


page_sequence = [Results_show, Final_Payoff, Thanks]
