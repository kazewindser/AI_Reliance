from os import environ
import os
os.environ["NUMEXPR_MAX_THREADS"] = "8"
import pandas as pd

SESSION_CONFIGS = [
    dict(
        name='HUMAN',
        app_sequence=['instruction','Quiz_human','practise','experiment_human','questionnaire','Result_payoff'],
        num_demo_participants=3,
        AI = False
    ),
    dict(
        name='Multi_AI',
        app_sequence=['instruction','Quiz_AI','practise','AI_multi_ref','questionnaire','Result_payoff'],
        num_demo_participants=1,
        AI = True
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
Maxround = 45


#Real Result
REAL_RESULT = [0,26,0,100,0,37,43,100,0,100,
                100,0,0,32,64,87,78,0,0,82,
                0,100,100,70,0,50,48,100,100,100,
                54,100,74,0,0,20,0,100,0,100,
                100,0,100,14,100]
#AI_reference
AI_REF_SET = [21,18,38,91,13,
            4,15,70,23,95,90,45,15,42,34,
            71,73,26,27,72,65,35,70,38,24,
            42,0,85,95,75,27,95,23,15,36,
            5,12,65,0,100,85,16,92,28,95]

#Multi-AI_reference
file = '_static/AI_refs.xlsx'
MULTI_AI_REF_SET = pd.read_excel(file)
#------------------------------------------------#

ROOMS = [
    dict(
        name='Pilot',
        display_name='Pilot',
        participant_label_file='_rooms/pilot.txt',
        use_secure_urls=False
    ),]



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
