import random
class Character:
    """
    This is the base class for our zombie game
    It should set up some basic properties that are used in common
    with both our monsters (zombies) and our Hero
    """
    def __init__(self,hitpoints,attackpower,playertype,name=None):
        """

        :param hitpoints:
        :param attackpower:
        :param playertype:
        :param name:
        """
        self.hp = hitpoints
        self.ap = attackpower
        self.playerType = playertype
        self.name = name

class Zombie(Character):
    """

    """
    def __init__(self,hitpoints,attackpower,name):
        """

        :param hitpoints:
        :param attackpower:
        :param name:
        """
        Character.__init__(self,hitpoints,attackpower,"Zombie",name)


    def attack(self,target):
        """

        :param target: pass a character object to attack, probably a "Hero"
        :return:
        """
        pass

    def gethit(self,damage):
        pass

class Hero(Character):
    """

    """
    def __init__(self,hitpoints,attackpower,name):
        """

        :param hitpoints:
        :param attackpower:
        :param name:
        """
        Character.__init__(self,hitpoints,attackpower,"Hero",name)
        self.fullhealth = self.hp

if __name__ == "__main__":
    # NOTE: DO NOT CHANGE ANYTHING BELOW THIS LINE, these are the tests
    # First we will create a Hero to be used in the attack method
    hero1 = Hero(2000,50,"Ash")
    print("Hero: ",hero1.name, hero1.hp)

    zom1 = Zombie(100,40,"Robert")
    print("Starting HP: {0}".format(zom1.hp))
    zom1.gethit(25)
    print(zom1.injurymessage)
    # Should be of the form "The hero hits you for 35 points of damage, you have 35 hp left" but using variables
    print("After Getting hit,  HP: {0}".format(zom1.hp))

    zom1.attack(hero1)
    print(zom1.attackmessage)
    # Should be of the form  "Zombie Robert did 30 points of damage" but using variables
    print("Hero:", hero1.name, hero1.hp)
    zom1.gethit(300)

    # this should probably kill your zombie
    print(zom1.injurymessage)
    print("After Getting hit,  HP: {0}".format(zom1.hp))

