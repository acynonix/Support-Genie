import random

"""
'agent_av' is a boolean
'since' is a list containing [hr, m, sec]
'role' is a list containing strings that defines the agent's role
"""

data = {'agent_1': {'agent_av': True, 'since': [11, 59, 00], 'role': ['Spanish Speaker', 'Support']},
        'agent_2': {'agent_av': True, 'since': [12, 00, 00], 'role': ['Spanish Speaker']},
        'agent_3': {'agent_av': False, 'since': [12, 9, 00], 'role': ['English Speaker', 'Sales']},
        'agent_4': {'agent_av': True, 'since': [13, 10, 00], 'role': ['Sales']}
        }
issue_category = ['Spanish Speaker', 'Sales']


def agent_available(data, issue_category):
    agents_true = []
    agents_true_role_match = []
    try:
        for key in data:
            if data[key]['agent_av']:
                agents_true.append((key, data[key]['role']))
                for i in range(len(agents_true)):
                    if data[key]['role'][i] in issue_category:
                        agents_true_role_match.append((key, data[key]['since'], data[key]['role']))
    except:
        print('\nWe have these agents right now')

    # Storing non repeatable agents
    new = []
    for x in agents_true_role_match:
        if x not in new:
            new.append(x)
    print(new)
    return new


def random_agent():
    # Getting the available agents with the issue matching roles
    agents_true_role_match = agent_available(data, issue_category)

    # Selecting Random agents out of them
    ran_agent = random.choice(agents_true_role_match)
    print(ran_agent)


def avail_since_long():
    # Getting the available agents with the issue matching roles
    agents_true_role_match = agent_available(data, issue_category)

    # creating an empty list for storing all agent's available time converted in seconds
    seconds = []
    for i in range(len(agents_true_role_match)):
        # converting time to seconds and appending
        seconds.append((agents_true_role_match[i][1][0] * 3600)
                       + (agents_true_role_match[i][1][1] * 60)
                       + (agents_true_role_match[i][1][2]))

    print('\nAgents available since long', agents_true_role_match[seconds.index(min(seconds))])
    return agents_true_role_match[seconds.index(min(seconds))]
