
#This is an example for the homework.

#Example: score_dict = {}
        #score_dict['Dan'] = 0
        # score_dict
        # {'Dan': 0}
        # We then create 3 people that will have scores in a game, Dan, Dee, and Ryan.
        # score_dict['Dee'] = 0
        # score_dict['Ryan'] = 0
        # This will then print out as {'Dan': 0, 'Dee': 0, 'Ryan': 0}
        # You can then change the numeric values as the game continues.


test_name_list = ["Dee", "Dan", "Ryan"]

def make_scorecard(names):
    print('Is the game working?')
    score_dict = {}
    for name in names:
        print(names)
        score_dict[name] = 0
        print(score_dict)
        return(score_dict)


def update_score(score_dict):
print(score_dict)
score_dict['Dee'] += 1
score_dict['Dan'] += 1

    for name, score in score_dict.items():
        print(f'{name}: {score}')


def play_game():
    update_score(make_scorecard(test_name_list), test_name_list))

play_game()

