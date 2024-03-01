#if input is "EOF" then stop taking input and start processing the multiple lines of input data
the_players_details = {}
BEST_OF_3='best_of_3'
BEST_OF_5='best_of_5'
NO_OF_BEST5_WON='No_Of_best5_won'
NO_OF_BEST3_WON='No_Of_best3_won'
NO_OF_SETS_WON='No_Of_sets_won'
NO_OF_GAMES_WON='No_Of_games_won'
NO_OF_SETS_LOST='No_Of_sets_lost'
NO_OF_GAMES_LOST='No_Of_games_lost'
match = input()
while match!="EOF":
    match_details = match.split(":")
    games_won_by_fisrt_player=0
    sets_won_by_fisrt_player=0
    games_lost_by_fisrt_player=0
    sets_lost_by_fisrt_player=0

    games_won_by_second_player=0
    sets_won_by_second_player=0
    games_lost_by_second_player=0
    sets_lost_by_second_player=0

    if match_details[0] not in the_players_details.keys():
        the_players_details[match_details[0]]={NO_OF_BEST5_WON:0,NO_OF_BEST3_WON:0,NO_OF_SETS_WON:0,NO_OF_GAMES_WON:0,NO_OF_SETS_LOST:0,NO_OF_GAMES_LOST:0}
    if match_details[1] not in the_players_details.keys():
        the_players_details[match_details[1]]={NO_OF_BEST5_WON:0,NO_OF_BEST3_WON:0,NO_OF_SETS_WON:0,NO_OF_GAMES_WON:0,NO_OF_SETS_LOST:0,NO_OF_GAMES_LOST:0}
    sets = match_details[2].split(',')
    type_of_match=''
    # Store the set details for each player in local variables
    for a_set in sets:
        #Converting all strings in list to integers Using list comprehension - https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
        games=a_set.split('-')
        games = [int(i) for i in games]
        games_won_by_fisrt_player+=games[0]
        games_lost_by_fisrt_player+=games[1]
        games_won_by_second_player+=games[1]
        games_lost_by_second_player+=games[0]
        if(games[0]>games[1]):
            sets_won_by_fisrt_player+=1
            sets_lost_by_second_player+=1
        else:
            sets_lost_by_fisrt_player+=1
            sets_won_by_second_player+=1
    #identify if the match is best of 5 or best of 3
    if len(sets) in [2]:
        type_of_match=BEST_OF_3
    elif len(sets) in [4,5]:
        type_of_match=BEST_OF_5
    elif len(sets) in [3]:
        # if all three are won by first player then best_of_5 else best_of_3
        if(sets_won_by_fisrt_player==3):
            type_of_match=BEST_OF_5
        else:
            type_of_match=BEST_OF_3
    
    the_players_details[match_details[0]][NO_OF_SETS_WON]+=sets_won_by_fisrt_player
    the_players_details[match_details[0]][NO_OF_GAMES_WON]+=games_won_by_fisrt_player
    the_players_details[match_details[0]][NO_OF_SETS_LOST]+=sets_lost_by_fisrt_player
    the_players_details[match_details[0]][NO_OF_GAMES_LOST]+=games_lost_by_fisrt_player
    if(type_of_match==BEST_OF_5):
        the_players_details[match_details[0]][NO_OF_BEST5_WON]+=1
    else:
        the_players_details[match_details[0]][NO_OF_BEST3_WON]+=1
    
    the_players_details[match_details[1]][NO_OF_SETS_WON]+=sets_won_by_second_player
    the_players_details[match_details[1]][NO_OF_GAMES_WON]+=games_won_by_second_player
    the_players_details[match_details[1]][NO_OF_SETS_LOST]+=sets_lost_by_second_player
    the_players_details[match_details[1]][NO_OF_GAMES_LOST]+=games_lost_by_second_player
    match = input()
# Sort and Display the_players_details in the expected format
list_of_tuples = []
for key1, value1 in the_players_details.items():
    my_tuple = (value1[NO_OF_BEST5_WON],value1[NO_OF_BEST3_WON],value1[NO_OF_SETS_WON],value1[NO_OF_GAMES_WON],value1[NO_OF_SETS_LOST],value1[NO_OF_GAMES_LOST],key1 )
    list_of_tuples.append(my_tuple)
list_of_tuples.sort(key=lambda t:(-t[0],-t[1],-t[2],-t[3],t[4],t[5]))
#print(the_players_details)
for k in list_of_tuples:
    print(k[6],k[0],k[1],k[2],k[3],k[4],k[5])
