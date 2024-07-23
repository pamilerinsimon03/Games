print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
begin = input("Type Start to 'Start' or 'Exit' to leave the game. ")
if begin == "Start":
    print("Let the Treasure Hunt Begin!!!")
    road = input("You are faced with a crossroads, go 'Left' or 'Right'? ")
    if road == "Left":
        swim = input("There is a river in front of you, do you want to 'Swim' across it or 'Wait' for no reason at all? ")
        if swim  == "Wait":
            door = input("Three doors appears in front of you, the door on the left painted 'Red' the door in the middle painted 'Yellow' and the door on the right  painted 'Blue'. Your destiny is in your hands, choose a door: ")
            if door == "Red":
                print("A fire breathing dragon comes out and burns you to a crisp\nGAME OVER!!!")
            elif door == "Yellow":
                print("You are transported to a mystical realm, and in front of you lies the lost treasure, you eyes are filled with excitement as you fix your gaze upon your wife.\nYou Win!!!")
            elif door == "Blue":
                print("Three huge lions came out and they tear you to pieces.\nGAME OVER!!!")
            else: 
                print("GAME OVER!!!")
        else:
            print("You were attacked by Trout.\nGAME OVER!!!")
    else:
        print("You fell into a hole.\nGAME OVER!!!")
else:
    print("Game Exited")