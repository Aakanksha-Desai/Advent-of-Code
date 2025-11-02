if num_blue > 14 or num_green > 13 or num_red > 12:
            not_possible.append(int(game_num))
            print("games not possible = "+str(not_possible))
            game_possible = False
            