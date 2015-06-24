class Scene(object):

    def enter(self):
        print "Scene configured in the children"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.mapped=scene_map.scene

    def play(self):
        #start_obj=CentralCorridor()
        #   start_obj.enter()
            a_map.next_scene("CentralCorridor")
            print "Two options : "
            print "1. So you want to try and cross the bridge of death to escape with the treasure??"
            print "2. Get some Armor to kill the aliens and have fun??"
            print "    Enter choice "
            choice=raw_input(">")
            
            if choice=="1":
                a_map.next_scene("TheBridge")
            elif choice=="2":
                print"Lets get some badass guns!!"
                a_map.next_scene("LaserWeaponArmory")
            else:
                print"You are dumber than i thought, sweet death by poison"
                exit(1)

class Death(Scene):

    def enter(self):
        print "So you have come to ur death! \nDo you try one last time and be safe??"
        last_chance=raw_input("> ")
        if last_chance=='yes' or last_chance=="Yes":
            print"Jump or kneel?? "
            last_act=raw_input("> ")
            if last_act == 'jump' or last_act=="Jump":
                print "Your head smashed and you die"
                exit(1)
            elif last_act=='kneel' or last_act=="Kneel":
                print "Killed by a bullet, so yeah that sucks!!"
                exit(1)
            else:
                print "Invalid request and you die coz of stupidity, brain bomb activated"
                exit(1)
        else:
            print "Die you !!"
            exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The game begins here :\n\n"

class LaserWeaponArmory(Scene):

    def enter(self):
        print "You want a 1. laser gun or 2. Machine gun ??"
        gun=raw_input("> ")
        if gun=="1":
            print "Good choice, you kill some aliens and move forward towards the escape pod"
            a_map.next_scene("EscapePod")
        elif gun=="2":
            print "Ok, so you wanna be Schwarzenegger?? You look stylish but are kicked into a corner by some aliens"
            a_map.next_scene("Death")
        else:
            print "Invalid request and you die coz of stupidity, brain bomb activated"
            exit(1)

class TheBridge(Scene):

    def enter(self):
        print "Entering the bridge...."
        print "The bridge looks old, sways and you drop down in the dungeon!"
        a_map.next_scene("Death")

class EscapePod(Scene):

    def enter(self):
        print "So you escape!! Long way into the sky, you may not live long, but there's a chance!! Goodbye "
        exit(1)


class Map(object):

    def __init__(self, start_scene):
        self.scene=start_scene

    def next_scene(self, scene_name):
    #   print "Reached here"
        name=eval(scene_name)
        obj=name()
        obj.enter()

    def opening_scene(self):
        print "By default game starts at the central corridor with you having stole the treasure.!!"


print "\n\n********* Welcome to the game He ha ha ha!! ******"
print "You have many choices what to do and try to survive"
a_map = Map("central_corridor")
a_map.opening_scene()
a_game = Engine(a_map)
a_game.play()


