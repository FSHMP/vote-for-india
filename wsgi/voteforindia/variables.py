#! coding==utf-8

L, N, H = 0, 1, 2

# a dictionary to maintain range and ranks
metrics = {
    'Low': {
        'range': range(1, 8),
        'rank': L
    },

    'Normal': {
        'range': range(8, 13),
        'rank': N
    },

    'High': {
        'range': range(13, 21),
        'rank': H
    }

}


# dict with each domain for individual parties

bjp_dict = {
    'agriculture': L, 'industry': H, 'technology': H, 'security': H, 'antiCorruption': N,
    'minorities': L, 'infrastructure': H, 'publicSector': L, 'socialSector': N, 'environment': L
}

cong_dict = {
    'agriculture': N, 'industry': H, 'technology': N, 'security': N, 'antiCorruption': L,
    'minorities': H, 'infrastructure': N, 'publicSector': N, 'socialSector': H, 'environment': N
}

aap_dict = {
    'agriculture': N, 'industry': L, 'technology': N, 'security': L, 'antiCorruption': H,
    'minorities': N, 'infrastructure': N, 'publicSector': L, 'socialSector': H, 'environment': H
}

left_dict = {
    'agriculture': H, 'industry': L, 'technology': N, 'security': N, 'antiCorruption': N,
    'minorities': H, 'infrastructure': L, 'publicSector': H, 'socialSector': H, 'environment': N
}
