from os import environ
import os
os.environ["NUMEXPR_MAX_THREADS"] = "8"
import pandas as pd

SESSION_CONFIGS = [
    dict(
        name='EXPERT',
        app_sequence=['instruction','Quiz_EXPERT','practise','questionnaire','EXPERT','Result_payoff'],
        num_demo_participants=1,
        AI = False
    ),
    dict(
        name='EXPERT_test',
        app_sequence=['EXPERT'],
        num_demo_participants=1,
        AI = False
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=500, doc=""
)


PARTICIPANT_FIELDS = ['Guess_set']

SESSION_FIELDS = []



#------------------------------------------------#
Maxround = 30


#Real Result
REAL_RESULT = [26,0,100,0,43,
                100,100,0,32,64,
                87,78,0,0,100,
                100,0,50,48,100,
                100,100,74,0,0,
                100,0,100,0,14]

#preHuman_advice
AI_file = '_static/preHumanAdvice.xlsx'
MULTI_AI_REF_SET = pd.read_excel(AI_file)

#Expert_advice
EXPERT_file = '_static/ExpertAdvice.csv'
EXPERT_ADVICE = pd.read_csv(EXPERT_file)
#------------------------------------------------#

ROOMS = [
    dict(
        name='pclab',
        display_name='社研PCラボ',
        participant_label_file='_rooms/pclab.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(
        name='virtual_Lab',
        display_name='Room for virtual Lab 40 subjects (sub**)',
        participant_label_file='_rooms/virtualLab.txt',
    )
]




# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1890941141757'
