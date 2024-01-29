
import re
#{Game1:{turn1:..turn2:...}
#Game2:{turn1:...}...}
#outermost dictionary
games_dict=dict()
with open('input2.txt', 'r') as file:
    #100 rows in this program
    for i in range(1,101):
        #dictionary for every game
        game_dict=dict()
        game = file.readline()
        game_name=game.split(':')[0]
        
        #Game 1: 1 green, 2 blue; 13 red, 2 blue, 3 green; 4 green, 14 red
        content=str(game.split(':')[1])
        turns=content.split(';')
        #for each turn 
        for j,turn in enumerate(turns,start=1):
            #print(i,turn)
            turn_dict = {}
            if turn:
                colors = turn.split(', ')
                for color_info in colors:
                    color_info=color_info.strip()
                    #print(color_info)
                    count,color = color_info.split(' ')
                    turn_dict[color] = int(count)
                game_dict[f'turn{j}'] = turn_dict

        games_dict[f'Game{i}'] = game_dict
#print(games_dict)
max_color_counts = {'green': 13, 'blue': 14, 'red': 12}
sum=0
valid_games=[]
for game_id, turns in games_dict.items():
        game_valid = True
        for turn, colors in turns.items():
            for color, count in colors.items():
                # Check if count exceeds the maximum allowed count
                if count > max_color_counts.get(color, 0):
                    game_valid = False
                    break  # No need to check other colors if one exceeds the limit

        if game_valid:
            valid_games.append(game_id)
#print(valid_games)
for i in valid_games:
    game_id=re.search(r'\d+',i).group()
    sum+=int(game_id)
print(sum)

    
