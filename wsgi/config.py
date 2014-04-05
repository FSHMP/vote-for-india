#! coding==utf-8

# a dictionary to maintain range and ranks
metrics = {
    'Low': {
        'range': range(1,8),
        'rank': 0
    },

    'Normal': {
        'range': range(8,13),
        'rank': 1
    },

    'High': {
        'range': range(13,21),
        'rank': 2
    }

}


# dict with each domain for individual parties

bjp = { 
	'agriculture': 0, 'industry': 2, 'technology': 2, 'security': 2, 'anti_corruption': 1, 'minorities': 0, 'infrastructure': 2, 'public_sector': 0, 'social_sector': 1, 'environment': 0
	}

congress = { 
	'agriculture': 1, 'industry': 2, 'technology': 1, 'security': 1, 'anti_corruption': 0, 'minorities': 2, 'infrastructure': 1, 'public_sector': 1, 'social_sector': 2, 'environment': 1
	}

aap = { 
	'agriculture': 1, 'industry': 0, 'technology': 1, 'security': 0, 'anti_corruption': 2, 'minorities': 1, 'infrastructure': 1, 'public_sector': 0, 'social_sector': 2, 'environment': 2
	}

left = { 
	'agriculture': 2, 'industry': 0, 'technology': 1, 'security': 1, 'anti_corruption': 1, 'minorities': 2, 'infrastructure': 0, 'public_sector': 2, 'social_sector': 2, 'environment': 1
	}

}


