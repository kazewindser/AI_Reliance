from os import environ

SESSION_CONFIGS = [
    dict(
        name='experiment_human_test',
        app_sequence=['experiment_human','Result_payoff'],
        num_demo_participants=3,
    ),
    dict(
        name='experiment_AI_test',
        app_sequence=['experiment_AI','Result_payoff'],
        num_demo_participants=1,
    ),
    dict(
        name='instruction_test',
        app_sequence=['instruction'],
        num_demo_participants=1,
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
        name='HUMAN',
        app_sequence=['instruction','quiz','practise','experiment_human','questionnaire','Result_payoff'],
        num_demo_participants=3,
    ),
    dict(
        name='AI',
        app_sequence=['instruction','quiz','practise','experiment_AI','questionnaire','Result_payoff'],
        num_demo_participants=3,
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

Maxround = 3
#Real Result
REAL_RESULT = [1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,19,20,
                21,22,23,24,25,26,27,28,29,30,
                31,32,33,34,35,36,37,38,39,40,
                41,42,43,44,45]

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
