from math import floor

def pretty(raw_generals, generals, action):
    if len(raw_generals) != len(generals) or len(raw_generals) != len(action):
        raise IndexError('raw_generals and generals must be of same length')

    for i in range(len(raw_generals)):
        print(i, action[i], raw_generals[i], generals[i])

def count_actions(loyal_command, action):
    result = 0
    for a in action:
        if a == loyal_command:
            result += 1
    return result

def traitor_or_loyal(traitor, loyal_order):
    return traitor != loyal_order # TODO: Is there a nicer way to do xor?

def traitorous_lieutenants(n_traitors, commander_traitor):
    traitorous_lts = n_traitors
    if commander_traitor:
        traitorous_lts -= 1
    return traitorous_lts

def consensus(opinions): # median
    #TODO: what about the case where there is an even number of generals but no direct order from the commander?
    cmdr = opinions[0]
    ordered = sorted(opinions)
    if len(ordered) % 2 != 0: # Odd
        return ordered[floor(len(ordered) / 2)]
    else: #even
        if ordered[floor(len(ordered)/2)] == ordered[(floor(len(ordered)/2)) - 1]:
            return ordered[floor(len(ordered)/2)]
        else:
            return cmdr

def byzantine(n_generals, n_traitors, commander_traitor):
    if n_traitors > n_generals:
        raise IndexError('Number of traitors cannot exceed total number of generals.')
    traitorous_lts = traitorous_lieutenants(n_traitors, commander_traitor)
    loyal_commander_order = True # What a loyal commander would order
    commander_order = traitor_or_loyal(commander_traitor, loyal_commander_order)
    raw_generals = []
    raw_generals.append(commander_order) # Commander
    for i in range(n_generals - traitorous_lts - 1): # Loyal generals
        raw_generals.append(commander_order)
    for i in range(traitorous_lts): # Traitorous generals
        raw_generals.append(not loyal_commander_order) # TODO: does this make sense?

    generals = []
    generals.append(commander_order) # Commander
    for i in range(n_generals - traitorous_lts - 1): # Loyal generals
        generals.append(raw_generals[1:]) #TODO: is this sufficient for all cases?
    for i in range(traitorous_lts): # Traitorous generals
        generals.append(not loyal_commander_order)

    action = []
    action.append(commander_order) # Commander
    for i in range(1, n_generals - traitorous_lts): # Loyal generals
        action.append(consensus(generals[i]))
    for i in range(traitorous_lts): # Traitorous generals
        action.append(not loyal_commander_order) 

    loyal_actions = count_actions(loyal_commander_order, action)

    result = False
    if loyal_actions >= n_generals - n_traitors:
        result = True

    pretty(raw_generals, generals, action)

    return result

if __name__ == '__main__':
    print(byzantine(6, 3, False))
