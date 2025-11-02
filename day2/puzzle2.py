data = open('input2.txt', 'r')
total_game_num = 0
not_possible = []
# game_possible = True
for line in data:
    game_possible = True
    first_split = line.split(':')
    game_num = first_split[0].split(' ')[1]
    turns = first_split[1].split(';')
    for i in range(len(turns)):
        num_blue = 0
        num_green = 0
        num_red = 0
        counts = turns[i].split(',')
        for j in range(len(counts)):
            # print("counts[j]="+counts[j])
            temp = counts[j].split(' ')
            # print("temp="+str(temp))
            n = temp[1]
            col = temp[2]
            # print("n="+n)
            if col == "blue":
                num_blue = int(n)
                # print("numblue="+str(num_blue))
            elif col == "green":
                num_green = int(n)
            elif col == "red":
                num_red = int(n)
        if num_blue > 14 or num_green > 13 or num_red > 12:
            not_possible.append(int(game_num))
            # print("games not possible = "+str(not_possible))
            game_possible = False
            break
    if game_possible == True:
        total_game_num += int(game_num)

print("Total = "+str(total_game_num))

    