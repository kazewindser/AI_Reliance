from os import environ

SESSION_CONFIGS = [
    dict(
        name='experiment_human_test',
        app_sequence=['experiment_human','Result_payoff'],
        num_demo_participants=3,
        AI = False
    ),
    dict(
        name='experiment_AI_test',
        app_sequence=['experiment_AI','Result_payoff'],
        num_demo_participants=1,
        AI = True
    ),
    dict(
        name='instruction_test',
        app_sequence=['instruction'],
        num_demo_participants=1,
        AI = True
    ),
    dict(
        name='quiz_test',
        app_sequence=['quiz','practise'],
        num_demo_participants=1,
    ),
    dict(
        name='questionnaire_test',
        app_sequence=['questionnaire'],
        num_demo_participants=1,
    ),
    dict(
        name='practise_test',
        app_sequence=['practise'],
        num_demo_participants=1,
        AI = True
    ),
    dict(
        name='HUMAN',
        app_sequence=['instruction','quiz','practise','experiment_human','questionnaire','Result_payoff'],
        num_demo_participants=3,
        AI = False
    ),
    dict(
        name='AI',
        app_sequence=['instruction','quiz','practise','experiment_AI','questionnaire','Result_payoff'],
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
Maxround = 3
#Real Result
REAL_RESULT = [0,26,0,100,0,37,43,100,0,100,
                100,0,0,32,64,87,78,0,0,82,
                0,100,100,70,0,50,48,100,100,100,
                54,100,74,0,0,20,0,100,0,100,
                100,0,100,14,100]
#AI_reference
AI_REF_SET = [45,44,43,42,41,
            40,39,38,37,36,35,34,33,32,31,
            30,29,28,27,26,25,24,23,22,21,
            20,19,18,17,16,15,14,13,12,11,
            10,9,8,7,6,5,4,3,2,1]
#------------------------------------------------#





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
