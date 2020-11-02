from logic.constants import ALL_TYPES

OPTIONS = [
    {
        'name': 'Dry Run',
        'command': 'dry-run',
        'type': 'boolean',
        'default': False,
        'help': 'Only generate a spoiler log, doesn\'t attempt to patch any game files',
        'ui': 'option_dry_run',
    },
    {
        'name': 'Randomize Tablets',
        'command': 'randomize-tablets',
        'type': 'boolean',
        'default': False,
        'help': 'Randomize the 3 Stone Tablets, blocking the access to the surface',
        'ui': 'option_randomize_tablets',
    },
    {
        'name': 'Closed Thunderhead',
        'command': 'closed-thunderhead',
        'type': 'boolean',
        'default': False,
        'help': 'Thunderhead is closed by default, obtain Ballad of the Goddess to immediately open it',
        'ui': 'option_closed_thunderhead',
    },
    {
        'name': 'Swordless',
        'command': 'swordless',
        'type': 'boolean',
        'default': False,
        'help': 'Instead of starting with the goddess sword, in this mode all sword upgrades, including the pracice sword, have to be found',
        'ui': 'option_swordless',
    },
    # {
    #     'name': 'Randomize Sailcloth',
    #     'command': 'randomize-sailcloth',
    #     'type': 'boolean',
    #     'default': False,
    #     'help': '(not implemented yet) Instead of starting with the Sailcloth, it\'s added to the item pool',
    # },
    {
        'name': 'Invisible Sword',
        'command': 'invisible-sword',
        'type': 'boolean',
        'default': False,
        'help': 'Dumb hack that makes the sword always invisible so it doesn\'t crash on console if obtaining an upgraded sword',
        'ui': 'option_invisible_sword',
    },
    {
        'name': 'Empty unrequired Dungeons',
        'command': 'empty-unrequired-dungeons',
        'type': 'boolean',
        'default': False,
        'help': 'If activated, only the required dungeons will contain progression items',
        'ui': 'option_empty_unrequired_dungeons',
    },
    {
        'name': 'Banned Types',
        'command': 'banned-types',
        'type': 'list',
        'default': '',
        'help': "Choose subtypes that can't contain progression items, as a comma seperated list, available types are: " + ", ".join(ALL_TYPES),
        'ui': 'option_banned_types'
    },
    {
        'name': 'Seed',
        'command': 'seed',
        'type': 'int',
        'default': -1,
        'help': 'Specify a seed to use for randomization, leave empty for random seed',
        'ui': 'seed',
    },
]