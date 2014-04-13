#Base Item List
melee_item_list = [
    {
        'name': 'Sword',
        'dmg_type': 'slashing',
        'min_dmg': 1,
        'max_dmg': 6,
        'hands': 1,
        'low_percent': 1,
        'high_percent': 30
    },
    {
        'name': 'Axe',
        'dmg_type': 'slashing',
        'min_dmg': 3,
        'max_dmg': 8,
        'hands': 1,
        'low_percent': 31,
        'high_percent': 50
    },
    {
        'name': 'Hammer',
        'dmg_type': 'bludgeoning',
        'min_dmg': 5,
        'max_dmg': 10,
        'hands': 1,
        'low_percent': 51,
        'high_percent': 70
    },
    {
        'name': 'Mace',
        'dmg_type': 'bludgeoning',
        'min_dmg': 2,
        'max_dmg': 7,
        'hands': 1,
        'low_percent': 71,
        'high_percent': 80
    },
    {
        'name': 'Dagger',
        'dmg_type': 'peircing',
        'min_dmg': 1,
        'max_dmg': 4,
        'hands': 1,
        'low_percent': 81,
        'high_percent': 90
    },
    {
        'name': 'Foil',
        'dmg_type': 'peircing',
        'min_dmg': 2,
        'max_dmg': 4,
        'hands': 2,
        'low_percent': 91,
        'high_percent': 100
    }
]
ranged_item_list = [
    {
        'name': 'Short Bow',
        'dmg_type': 'peircing',
        'min_dmg': 1,
        'max_dmg': 6,
        'hands': 2,
        'low_percent': 1,
        'high_percent': 33
    },
    {
        'name': 'Long Bow',
        'dmg_type': 'peircing',
        'min_dmg': 4,
        'max_dmg': 10,
        'range': 1,
        'low_percent': 34,
        'high_percent': 66
    },
    {
        'name': 'CrossBow',
        'dmg_type': 'peircing',
        'min_dmg': 2,
        'max_dmg': 4,
        'hands': 1,
        'low_percent': 67,
        'high_percent': 100
    }
]

item_list = [
    {
        'type': 'melee',
        'list': melee_item_list,
        'low_percent': 1,
        'high_percent': 50
    },
    {
        'type': 'ranged',
        'list': ranged_item_list,
        'low_percent': 51,
        'high_percent': 100
    }
]
