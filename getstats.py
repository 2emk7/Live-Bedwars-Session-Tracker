username = ""
stats = [0,0,0,0,0] #wins, beds broken, beds lost, final kills, final deaths
game_status = 0
win_list = []

game_start_keyword = "Protect your bed and destroy the enemy beds"
FK_keyword = ". FINAL KILL!"
FD_keyword = "You have been eliminated!"
BD_keyword = "Bed was " 
BL_keyword = "BED DESTRUCTION > Your Bed"

def display_stats():
    print("========== Session Stats ===========")
    print(f"Wins          : {stats[0]}")
    print(f"Beds Broken   : {stats[1]}")
    print(f"Beds Lost     : {stats[2]}")
    print(f"Final Kills   : {stats[3]}")
    print(f"Final Deaths  : {stats[4]}")
    print("====================================\n")
    
def find_Win():
    has_BW = any("Bed Wars" in line for line in win_list)
    has_username = any(username in line for line in win_list)
    has_1st = any("1st Killer" in line for line in win_list)
    return has_username and has_BW and has_1st


def start_Tracker():
    global username, game_status

    username = input("Enter your username: ")
    display_stats()

    file = open('C:/Users/ethan/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log', 'r')
    file.seek(0, 2)
    while True:

        for line in file:
            win_list.append(line)
            if len(win_list) > 15:
                win_list.pop(0)

            if game_start_keyword in line and game_status == 0:
                game_status = 1
                print("Game started!")

            elif game_status == 1 and ("joined the lobby!" in line or "Sending you to" in line):
                game_status = 0
                print("Game ended!")

            elif FK_keyword in line and username in line:
                print(line)
                stats[3] += 1
                display_stats()

            elif FD_keyword in line:
                print(line)
                stats[4] += 1
                display_stats()

            elif BD_keyword in line and username in line:
                print(line)
                stats[1] += 1
                display_stats()

            elif BL_keyword in line:
                print(line)
                stats[2] += 1
                display_stats()

            elif find_Win():
                print("WIN DETECTED!")
                stats[0] += 1
                display_stats()
                game_status = 0
                win_list.clear()
        

