import time
global isRunning

username = ""
global stats
stats = [0,0,0,0,0,0] #wins, losses beds broken, beds lost, final kills, final deaths
game_status = 0
win_list = []

game_start_keyword = "Protect your bed and destroy the enemy beds"
FK_keyword = ". FINAL KILL!"
FD_keyword = "You have been eliminated!"
BD_keyword = "Bed was " 
BL_keyword = "BED DESTRUCTION > Your Bed"
    
def find_Win():
    has_BW = any("Bed Wars" in line for line in win_list)
    has_username = any(username in line for line in win_list)
    has_1st = any("1st Killer" in line for line in win_list)
    return has_username and has_BW and has_1st


def start_Tracker():
    isRunning = True
    global username, game_status

    file = open('C:/Users/ethan/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log', 'r')
    file.seek(0, 2)

    while isRunning == True:

        time.sleep(1)

        for line in file:
            print(username)
            win_list.append(line)
            if len(win_list) > 15:
                win_list.pop(0)

            if game_start_keyword in line and game_status == 0:
                game_status = 1
                print("Game started!")

            elif game_status == 1 and ("joined the lobby!" in line or "Sending you to" in line):
                game_status = 0
                stats[1] += 1
                print("Game ended!")

            elif FK_keyword in line and username in line:
                print(line)
                stats[4] += 1

            elif FD_keyword in line:
                print(line)
                stats[5] += 1

            elif BD_keyword in line and username in line:
                print(line)
                stats[2] += 1

            elif BL_keyword in line:
                print(line)
                stats[3] += 1

            elif find_Win():
                print("WIN DETECTED!")
                stats[0] += 1
                game_status = 0
                win_list.clear()

    print("Tracker stopped.")
        

