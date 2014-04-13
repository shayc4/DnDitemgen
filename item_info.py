#Base Item List
melee_item_list = [
    {
        'name': 'Sword',
        'dmg_type': 'slashing',
        'min_dmg': 1,
        'max_dmg': 6,
        'hands': 1
    },
    {
        'name': 'Axe',
        'dmg_type': 'slashing',
        'min_dmg': 3,
        'max_dmg': 8,
        'hands': 1
    },
    {
        'name': 'Hammer',
        'dmg_type': 'bludgeoning',
        'min_dmg': 5,
        'max_dmg': 10,
        'hands': 1
    },
    {
        'name': 'Mace',
        'dmg_type': 'bludgeoning',
        'min_dmg': 2,
        'max_dmg': 7,
        'hands': 1
    },
    {
        'name': 'Dagger',
        'dmg_type': 'peircing',
        'min_dmg': 1,
        'max_dmg': 4,
        'hands': 1
    },
    {
        'name': 'Foil',
        'dmg_type': 'peircing',
        'min_dmg': 2,
        'max_dmg': 4,
        'hands': 2
    }
]
ranged_item_list = [
    {
        'name': 'Short Bow',
        'dmg_type': 'peircing',
        'min_dmg': 1,
        'max_dmg': 6,
        'hands': 2
    },
    {
        'name': 'Long Bow',
        'dmg_type': 'peircing',
        'min_dmg': 4,
        'max_dmg': 10,
        'range': 1,
    },
    {
        'name': 'CrossBow',
        'dmg_type': 'peircing',
        'min_dmg': 2,
        'max_dmg': 4,
        'hands': 1
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
