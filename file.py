"""
Choose your path games
Author: Yeow Song Wei
Challenge 2 game

Some sites I used for the ascii arts (mainly text):
http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
https://www.oocities.org/spunk1111/mythical.htm

There're many references in this game

add comments
add backstory

"""

import random  # import random module, allows python to generate random value
import time  # import time module, allows python to execute time related codes

playerHP = 100  # Assigning player health to a variable, since it's a value often used, it's way up here as a global value
playerCurrency = 0  # Similar to the one above, but with player coins


def preGameNote():  # Just a function for some text
    print("Before starting the game, take a few seconds to read some info:")
    print("This is a game based on fighting monsters, and the choice is yours!")
    print("Some notes about this game:")
    print(
        "- Pretty dependant on luck, you might not be able to get the full experience (all the random monsters, weapons etc.)"
    )
    print("- Most aspect of the game can be called manually via functions")
    print(
        "- There's a few sound effects implemented in the game, but it won't be played unless you downloaded the music files"
    )
    print()
    print("Class gimmicks")
    print("- Different classes has different chances to proc different benefits!")
    print("  - Melee \u2694: 10% chance to deal double damage")
    print("  - Magic \u269a: Heals player health for 10% of damage dealt")
    print("  - Range \u27b3: 1% change for the enemy to die in one shot")
    print("  - Rogue \u2604: 5% chance for enemy to dodge the enemy's attack")
    print(
        "- Although choosing the class with the holder's weapon is usually a wiser choice, you're free to choose anything based on your preferences"
    )
    print()
    print("Battle gimmicks")
    print(
        "- A random monster will spawn, depending on the the rarity, the stats and coin drops are different"
    )
    print("- Here are the monter's spawn rates:")
    print("  - Super rare Monster = 5%")
    print("  - Rare Monster = 15%")
    print("  - Uncommon Monster = 25%")
    print("  - Common Monster = 55%")
    print("- After 5 battles, the boss will spawn")
    print(
        "================================================================================"
    )


def slowingStory(
    numTimes,
):  # A function for asthethic purposes, with a parameter of the number of repition
    for num in range(numTimes):  # Loops the same amount as parameter
        print("")
        time.sleep(2)


def backStory():  # Another function for some text
    slowingStory(3)  # Using the slowing time function to slow dwn the story
    print('"' + usrName + '..."')
    slowingStory(3)
    print('"Wake up, ' + usrName + '..."')
    slowingStory(3)
    print("You've been woken up by a soft voice in your head")
    slowingStory(2)
    print("You seem to in some sort of building..")
    slowingStory(2)
    print("You tried to remember the past, but got a severe headache instead..")
    slowingStory(2)
    print("Looking around, you found nothing but a piece of paper")
    slowingStory(2)
    print('"Are you ready for one hell of an adventure, ' + usrName + '?"')
    print("Your surronding changed to a mysterious forest.....\u2619")
    slowingStory(4)


def diceRoller(
    diceAmount, diceSide
):  # Dice roller function, with parameters to control the number of dice and dice sides
    global diceTotal  # A global variable so it can be used in other functions
    diceTotal = 0  # Assigning 0 to a variable, it's used for addition later
    diceMax = 0  # Number of max value
    diceMin = 0  # Number of min value
    for dice in range(
        diceAmount
    ):  # A foor loop, the number of loops is equal to the amount of dice
        diceRoll = random.randint(
            1, diceSide
        )  # A random number generator between 1 and the number of dice sides
        diceTotal += diceRoll  # The intergers rolls from the previous lines will be added to the variable diceTotal
        if (
            diceRoll == diceSide
        ):  # If statement used to check if I rolled a maximum value
            diceMax += 1
        elif diceRoll == 1:  # If statement used to check if I rolled a minimum value
            diceMin += 1
    return diceTotal  # Returns the total value of the dice roll, so it can be used in other functions/places


def modifierRoller():  # A roller for player's stats using dice roller
    global meleeAttribute  # A global variable so it can be used in other functions
    global magicAttribute
    global rangeAttribute
    global rogueAttribute
    print(
        "You were given an adventure card with your attributes and stats by some unknown power"
    )
    print(":================================:")
    print(
        "|::|  Name: " + usrName + " " * spacesAfterName + "\u2009|::|"
    )  # \u2009 is a unicode for half space, I use this to control weird spaces
    diceRoller(
        4, 6
    )  # Using the dice roller function to get a total value from 4 dice that has 6 sides
    statNumber = (
        diceTotal // 5
    )  # The total value from the dice is divided by 5 and rounded
    print(
        "|::|  Melee attribute \u2694:", statNumber, "  |::|"
    )  # The weird "\u2694" is a unicode that can be used to display weird symbols
    meleeAttribute = statNumber  # Assigning the number to a clearer variable
    # Everything below in this function is similar to the one above, just with different variables
    diceRoller(4, 6)
    statNumber2 = diceTotal // 5
    print("|::|  Magic attribute \u269a:", statNumber2, "   \u2009|::|")
    magicAttribute = statNumber2
    diceRoller(4, 6)
    statNumber3 = diceTotal // 5
    print("|::|  Range attribute \u27b3:", statNumber3, "  \u2009\u2009|::|")
    rangeAttribute = statNumber3
    diceRoller(4, 6)
    statNumber4 = diceTotal // 5
    print("|::|  Rogue attribute \u2604:", statNumber4, "  |::|")
    rogueAttribute = statNumber4
    print("|::|  Title: Traveler         \u2009|::|")
    print("|::|         Adventurer       \u2009|::|")
    print(":================================:")
    if statNumber <= 1:
        print(
            "Unforunately you have no talent in melee combat, please don't ever swing a sword"
        )
    if statNumber == 4:
        print("A natural borned talent in melee, amazing!")
    if statNumber2 <= 1:
        print(
            "Unforunately you have no talent in magic, please don't ever chant a spell"
        )
    if statNumber2 == 4:
        print("A natural borned talent in magic, amazing!")
    if statNumber3 <= 1:
        print(
            "Unforunately you have no talent in range combat, please don't ever shoot an arrow"
        )
    if statNumber3 == 4:
        print("A natural borned talent in shooting, amazing!")
    if statNumber4 <= 1:
        print(
            "Unforunately you have no talent in rogue combat, please don't ever kill something in stealth"
        )
    if statNumber4 == 4:
        print("A natural borned talent in stealth killing, amazing!")


def playerHealing():  # A function used for player healing
    global playerCurrency
    playerHealLoop = True  # A variable used later on to make sure the game runs smoothly and doesn't crash, via accepting wrong inputs
    while playerHealLoop == True:  # A loop if the previous variable is true
        print("\u2624 Adventure Guild \u2624")
        print("You need 50 coins to heal your Hp to max!")
        print("Do you want to spend 50 gold coins to heal your player?")
        playerHealOption = input(
            "(Yes/No): "
        )  # Player input, accepts all inputs without crashing
        if (
            playerHealOption == "Yes"
        ):  # If the answer is "Yes", executes the codes indented below
            if (
                playerCurrency >= 50
            ):  # A nested if, this makes it so the code indented below will only run if player has more than 50 coins
                playerHP = (
                    100  # Basically the "healing" part, player hp restores to default
                )
                playerCurrency -= 50  # Subtracts 50 coins from playeer's total coins
                print("Your player's hp is back to " + str(playerHP) + "!")
                playerHealLoop = False  # Assigning the previous variable to false so it can end the loop
            elif (
                playerCurrency < 50
            ):  # Same idea as before, but this one is for players without 50 coins
                print("You don't have enough gold coins! Go slay more monsters!")
                break  # Forces the loop to end early
        elif (
            playerHealOption == "No"
        ):  # If the input is not "Yes", but "No", executes the codes indented below
            print("Alright, I'll see you next time!")
            break
        else:  # Any other input will execute codes indented below
            # playerHealLoop will stay true as nothing changed, therefore, it will loop forever until user inputs Yes or No
            print("Player input not accepted, try again")


def randomWeapon():  # A function that generates a random weapon for the user
    global weaponDrop  # All these global variables are to be used in other functions
    global weapon1
    global weapon2
    global weapon3
    global weapon3
    global weaponMeleeDmg
    global weaponMagicDmg
    global weaponRangeDmg
    global weaponRogueDmg
    weaponMeleeDmg = 0  # These are similar to how player hp and currency work
    weaponMagicDmg = 0
    weaponRangeDmg = 0
    weaponRogueDmg = 0
    # Listing weapons and assigning them to their respected rarity
    commonWeaponList = [
        "Wooden Stick (\u2694)",
        "Wand of Sparkling (\u269a)",
        "Wooden Bow (\u27b3)",
        "Wooden Dagger (\u2604)",
    ]
    uncommonWeaponList = [
        "Broadsword (\u2694)",
        "Fire Magic Staff (\u269a)",
        "Silver Bow (\u27b3)",
        "Shuriken (\u2604)",
    ]
    rareWeaponList = [
        "Excalibur (\u2694)",
        "Staff of Explosion (\u269a)",
        "Atermis's Bow (\u27b3)",
        "Takuma's dagger(\u2604)",
    ]
    legendaryWeaponList = [
        "Master Sword (\u2694)",
        "The Elder Wand (\u269a)",
        "Hero's Bow (\u27b3)",
        "Star of Destruction (\u2604)",
    ]
    # Selecting a random weapon from the list
    uncommonWeapon = random.choice(uncommonWeaponList)
    commonWeapon = random.choice(commonWeaponList)
    rareWeapon = random.choice(rareWeaponList)
    legendaryWeapon = random.choice(legendaryWeaponList)
    weapon1 = (
        "You've received a gift from the unknown power! It's a "
        + commonWeapon
        + ", a common weapon that deals 2 extra damage!"
    )
    weapon2 = (
        "You've received a gift from the unknown power! It's a "
        + uncommonWeapon
        + ", a uncommon weapon that deals 5 extra damage!"
    )
    weapon3 = (
        "You've received a gift from the unknown power! It's a "
        + rareWeapon
        + ", a rare weapon that deals 10 extra damage!"
    )
    weapon4 = (
        "You've received a gift from the unknown power! It's a "
        + legendaryWeapon
        + ", a legendary weapon that dedals 20 extra damage!"
    )
    # To control the drop rates, I used a random.randint system where the rarer the number, the smaller the number range it is that triggers its spawn
    weaponDropRates = diceRoller(
        1, 100
    )  # Here is the dice roller where I randomly generate a between 1 and 100
    if (
        weaponDropRates <= 5
    ):  # For example, the codes indented below will only execute when the random number is 5 or below, hence making the drop chance of legendary weapon 5%
        weaponDrop = legendaryWeapon
        if (
            weaponDrop == "Master Sword (\u2694)"
        ):  # To differenciate the classes within the rarity, a seperate if statement is needed to assign damage to their respected class
            weaponMeleeDmg += 20  # For example, if the weapon is a Master Sword from Zelda, melee class would deal 20 more damage
        elif weaponDrop == "The Elder Wand (\u269a)":
            weaponMagicDmg += 20
        elif weaponDrop == "Hero's Bow (\u27b3)":
            weaponRangeDmg += 20
        elif weaponDrop == "Star of Destruction (\u2604)":
            weaponRogueDmg += 20
        print(weapon4)
    # Everything below in this function is similar to the one above, just with different variables
    elif weaponDropRates <= 25:
        weaponDrop = rareWeapon
        if weaponDrop == "Excalibur (\u2694)":
            weaponMeleeDmg += 10
        elif weaponDrop == "Staff of Explosion (\u269a)":
            weaponMagicDmg += 10
        elif weaponDrop == "Atermis's Bow (\u27b3)":
            weaponRangeDmg += 10
        elif weaponDrop == "Takuma's dagger(\u2604)":
            weaponRogueDmg += 10
        print(weapon3)
    elif weaponDropRates <= 55:
        weaponDrop = uncommonWeapon
        if weaponDrop == "Broadsword (\u2694)":
            weaponMeleeDmg += 5
        elif weaponDrop == "Fire Magic Staff (\u269a)":
            weaponMagicDmg += 5
        elif weaponDrop == "Silver Bow (\u27b3)":
            weaponRangeDmg += 5
        elif weaponDrop == "Shuriken (\u2604)":
            weaponRogueDmg += 5
        print(weapon2)
    else:
        weaponDrop = commonWeapon
        if weaponDrop == "Wooden Stick (\u2694)":
            weaponMeleeDmg += 2
        elif weaponDrop == "Wand of Sparkling (\u269a)":
            weaponMagicDmg += 2
        elif weaponDrop == "Wooden Bow (\u27b3)":
            weaponRangeDmg += 2
        elif weaponDrop == "Wooden Dagger (\u2604)":
            weaponRogueDmg += 2
        print(weapon1)


def meleeWeaponAbilities():  # Function for melee class abilties
    global totalPlayerDmg
    meleeProcRate = diceRoller(
        1, 10
    )  # Again, similar to weapon drop rates, the chance of the ability activating is decided using dice roller
    if meleeProcRate == 1:
        totalPlayerDmg = (
            totalPlayerDmg * 2
        )  # This makes the variable totalPlayerDmg multiplied by 2, this variable will appear later on in other functions and everything will make sense
        print("You bursted into flames, doing 2x the damage!")


# The few functions below is similar to the one above, just with different variables
def magicWeaponAbilities():
    global playerHP
    global playerHealAmountRd
    playerHealAmount = totalPlayerDmg / 10  # The total damage dealt is divided by 10
    playerHealAmountRd = round(
        playerHealAmount
    )  # And then, rounded up, the reason I used round instead of // it because at time it gives weird numbers
    playerHP += (
        playerHealAmountRd  # Player health is increased by whatever the heal amount is
    )
    print("Your magic attack heals you for around 10% of it's damage, good stuff!")


def rangeWeaponAbilities():
    global totalPlayerDmg
    rangeProcRate = diceRoller(
        1, 100
    )  # Similar with the melee class proc rate, just with a larger number
    if rangeProcRate == 1:
        totalPlayerDmg = 999999999  # Ensures the one shot
        print("Bullseye! You hit it's only weakspot!")


def rogueWeaponAbilities():
    global monsterDmg
    rogueProcRate = diceRoller(1, 20)  # Same concept as before
    if rogueProcRate == 1:
        monsterDmg = 0  # Enemey's damage will be nulified when dodged
        print("You have a 10% chance to dodge the monster's attack!")


def allFights():  # A function for the core of the game, the fights
    global playerHP  # A lot of globals here because many of these variables are shared across other functions
    global monsterHealth
    global weaponMeleeDmg
    global weaponMagicDmg
    global weaponRangeDmg
    global weaponRogueDmg
    global totalPlayerDmg
    global currencyDrop
    global playerCurrency
    global monsterStatus
    global loopChecker
    global generalLoopCheck
    global gameLoop
    global deadLoop
    global playerDeadOption
    monsterStatus = True  # A variable useful for the next line that is the loop
    while (
        monsterStatus == True
    ):  # This will loop when the monster's alive, as there's a a variable later that will assign monster status to false when dead        time.sleep(0.2)
        print()
        print("Processing.")
        time.sleep(0.2)
        print("Processing..")  # Just for asthethic purposes
        time.sleep(0.2)
        print("Processing...")
        time.sleep(0.2)
        print()  # Below is a ASCII art that shows the player in battle
        print("=====================================================================")
        print(monsterClass)
        print(monsterType)
        print("Monster Health:", monsterHealth, "                            ,------.")
        print("Monster Damage:", monsterDmg, "                           '  .--.  '")
        print("==============================                |  |  |  |")
        print("                                              '--'  |  |")
        print("                                                  __.  |")
        print("                                                 |   .'")
        print("                                                 |___|")
        print("                                                 .---.")
        print("                                                 '---'")
        print("           /^^^^\ ")
        print("      ___^/      \__            Player Health:", playerHP)
        print("     \     _*^^^*, _/           Current Weapon:", weaponDrop)
        print("       - //  ^   _\             Melee attribute \u2694:", meleeAttribute)
        print("        {{|  .   .\             Magic attribute \u269a:", magicAttribute)
        print("         {|    _  /             Range attribute \u27b3:", rangeAttribute)
        print("           {  __ }  {^_-        Rogue attribute \u2604:", rogueAttribute)
        print("        _ {   \/ \  }|          Player coins:", playerCurrency)
        print("        /{|     \ \/}           ====================================")
        print("       /  |        |     ")
        print(":==================================================================:")
        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
        print("||:                           ||:     Fight    ||      Heal      :||")
        print("||:    Monster Encounter...   ||:--------------------------------:||")
        print("||:                           ||:      Run     ||   UNAVAILABLE  :||")
        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
        print(":==================================================================:")
        print("What is your course of action?")
        print("\u21f0 Fight \u265e ")
        print("\u21f0 Flee \u265f")
        print("\u21f0 Heal \u2665")
        playerOptionInput = input(
            "Option: "
        )  # For player to input their option, any answer wouldn't crash the game
        loopChecker = (
            True  # This variable is useful for later as I design this to be crash proof
        )
        while (
            loopChecker == True
        ):  # Any code indented below will loop as long as loopCheck is true
            if (
                playerOptionInput == "Fight"
            ):  # If the player input is Fight, executes the codes indented below
                print("What type of attack do you want to use?")
                print("\u21f0 Melee \u2694")
                print("\u21f0 Magic \u269a")
                print("\u21f0 Range \u27b3")
                print("\u21f0 Rogue \u2604")
                attributeInput = input(
                    "Option: "
                )  # Another option for player to input the classes, after they chose fight
                print("Processing.")  # Asthethic purposes
                time.sleep(0.3)
                print("Processing..")
                time.sleep(0.3)
                print("Processing...")
                time.sleep(0.3)
                print()
                if (
                    attributeInput == "Melee"
                ):  # If the player chose Melee, executes the codes indented below
                    random20Damage = diceRoller(
                        1, 20
                    )  # Using the dice roller, the player rolls a 20 side dice to dictate the additional damage
                    totalPlayerDmg = (
                        meleeAttribute + random20Damage + weaponMeleeDmg
                    )  # Calculates the total damage done
                    meleeWeaponAbilities()  # This is the function I mentioned earlier, for example, this is the melee class, so if the 1 in 10 chance activates, the damage will double
                    monsterRemainHp = (
                        monsterHealth - totalPlayerDmg
                    )  # Calculates the remaning health of the monster by subtracting
                    monsterHealth = monsterRemainHp  # Give the monster it's new health (remaining health)
                    print(
                        "You rolled a " + str(random20Damage) + " on your 20 side dice!"
                    )
                    print(
                        "You did "
                        + str(totalPlayerDmg)
                        + "DMG to the "
                        + monsterType
                        + "!"
                    )
                # All these elif statements below are similar to the one above, just different variables with slight changes for class procs
                elif attributeInput == "Magic":
                    random20Damage = diceRoller(1, 20)
                    totalPlayerDmg = magicAttribute + random20Damage + weaponMagicDmg
                    monsterRemainHp = monsterHealth - totalPlayerDmg
                    magicWeaponAbilities()
                    monsterHealth = monsterRemainHp
                    monsterHealth = monsterRemainHp
                    print(
                        "You rolled a " + str(random20Damage) + " on your 20 side dice!"
                    )
                    print(
                        "You did "
                        + str(totalPlayerDmg)
                        + "DMG to the "
                        + monsterType
                        + "!"
                    )
                    print("You healed " + str(playerHealAmountRd) + "HP!")
                elif attributeInput == "Range":
                    print("You have 1% chance to hit the monster's weakspot!")
                    random20Damage = diceRoller(1, 20)
                    totalPlayerDmg = rangeAttribute + random20Damage + weaponRangeDmg
                    print(
                        "You rolled a " + str(random20Damage) + " on your 20 side dice!"
                    )
                    rangeWeaponAbilities()
                    monsterRemainHp = monsterHealth - totalPlayerDmg
                    monsterHealth = monsterRemainHp
                    print(
                        "You did "
                        + str(totalPlayerDmg)
                        + "DMG to the "
                        + monsterType
                        + "!"
                    )
                elif attributeInput == "Rogue":
                    rogueWeaponAbilities()
                    random20Damage = diceRoller(1, 20)
                    totalPlayerDmg = rogueAttribute + random20Damage + weaponRogueDmg
                    monsterRemainHp = monsterHealth - totalPlayerDmg
                    monsterHealth = monsterRemainHp
                    print(
                        "You rolled a " + str(random20Damage) + " on your 20 side dice!"
                    )
                    print(
                        "You did "
                        + str(totalPlayerDmg)
                        + "DMG to the "
                        + monsterType
                        + "!"
                    )
                elif (
                    attributeInput != "Melee" or "Magic" or "Range" or "Rogue"
                ):  # If the player input is not any of the one mentioned, executes the codes indented below
                    print("Player input not accepted, try again")
                    break  # Forces the game to get out of the loop early, but since monsterstatus loop is still true, it will loop everything above until it receives a valid input

            if (
                playerOptionInput == "Flee"
            ):  # If the player input is flee, executes codes indented below
                loopChecker = (
                    False  # Assign the loopchecker to false, so it stops looping
                )
                fleeNumber = diceRoller(
                    1, 5
                )  # Using dice roller number to generate a number between 1 and 5, this is similar to the weapon drop rates, but instead, this determine the chances of fleeing
                # Everything indented below is similar to weapon drop rates, but with fleeing
                if fleeNumber > 1:
                    loopChecker = True
                    print(
                        "You've failed to escape! The monster was way ahead of your movements"
                    )
                    playerRemainHP = (
                        playerHP - monsterDmg
                    )  # When the player fails to flee, the player will take damage
                    playerHP = playerRemainHP
                    print(
                        "The monster attacked you when you were not focusing on the battle, you have "
                        + str(playerRemainHP)
                        + "HP left!"
                    )
                    break
                elif fleeNumber == 1:
                    print("You've successfully escaped!")
                    playerHealing()  # The healing function, if asks if the player wants to heal, since you usually take damage when trying to flee
                    monsterStatus = False  # Stops the monsterStatus from looping since the player escaped the monster
                    break

            if (
                playerOptionInput == "Heal"
            ):  # If the player input is heal, executes codes indented below
                playerHealing()  # Healing function, allows player with sufficient coins to heal
                break  # Forces out of the loop, but since monsterStatus is still true, it will continute to loop

            elif (
                monsterHealth >= 1
                and playerOptionInput == "Fight"
                and loopChecker == True
            ):  # If monster still has health, player input is fight and the loop checker is true, executes codes below
                monsterStatus = True
                print("The monster has " + str(monsterRemainHp) + "HP left!")
                playerRemainHP = (
                    playerHP - monsterDmg
                )  # Player will take damage since the monster counterattac
                playerHP = playerRemainHP  # Calculates player reamining HP
                if (
                    monsterDmg == 0
                ):  # This is for the range class ability, since if it procs, monsterDmg will be 0
                    print("You manage to dodge the monster's attack!")
                else:
                    if (
                        playerHP <= 0
                    ):  # This two lines is to ensure when printing remaining player health, it doesn't go negative as it looks weird
                        playerHP = 0
                    print(
                        "The "
                        + monsterType
                        + " counterattacked! You took "
                        + str(monsterDmg)
                        + "DMG and have "
                        + str(playerHP)
                        + "HP left!"
                    )
                    print("The monster lived to tell its tale")
                    time.sleep(5)
                    print()
                break

            # Elif statement below is similar to the one above, only change is it executes when monster health is 0 or lower
            elif monsterHealth <= 0 and loopChecker == True:
                monsterStatus = False  # Stops the fight from looping
                print("The monster was subjugated \u2620")
                playerCurrency += currencyDrop  # Player gains currency depending on the type of monster
                print("You got " + str(currencyDrop) + " gold coins!")
                print("You currently have " + str(playerCurrency) + " gold coins!")
                break

            elif (
                playerOptionInput != "Flee" or "Fight" or "Heal" and loopChecker == True
            ):  # Similar to the class option, this is to ensure the code is crash proof
                print()
                print("Player input not accepted, try again")
                break

        if (
            playerHP <= 0
        ):  # If player health is 0 or lower, executes codes indented below
            monsterStatus = True
            print(
                " __  __     ______     __  __        _____     __     ______     _____  "
            )
            time.sleep(0.5)
            print(
                "/\ \_\ \   /\  __ \   /\ \/\ \      /\  __-.  /\ \   /\  ___\   /\  __-."
            )
            time.sleep(0.5)
            print(
                "\ \____ \  \ \ \/\ \  \ \ \_\ \     \ \ \/\ \ \ \ \  \ \  __\   \ \ \/\ \ "
            )
            time.sleep(0.5)
            print(
                " \/\_____\  \ \_____\  \ \_____\     \ \____-  \ \_\  \ \_____\  \ \____- "
            )
            time.sleep(0.5)
            print(
                "  \/_____/   \/_____/   \/_____/      \/____/   \/_/   \/_____/   \/____/ "
            )
            deadLoop = True  # Another variable used for loop similar to monsterStatus or loopChecker
            while deadLoop == True:  # As long as deadLoop is true, this code will loop
                loopChecker = False  # Stops the option code from looping
                monsterStatus = False  # Stops the monster fight code from looping
                print(
                    "Do you want to be reincaranted into the world? (New stats, weapons etc.)"
                )
                playerDeadOption = input("(Yes/No): ")
                if playerDeadOption == "Yes":
                    gameLoop = True  # A variable which you'll see later on, it controls the looping of the whole game
                    print("You wish has been granted")
                    break
                elif playerDeadOption == "No":
                    deadLoop = False  # Stops the dead message from looping
                    gameLoop = False  # Make sure the game stops looping
                    generalLoopCheck = False  # This is a loop check you'll see later, it controls the monster spawn and other things
                    print("Oh well, guess you'll die")
                    break
                else:
                    print("Player input not accepted, try again")
                    print()


def bossFights():  # This is very similar to allFight() function, but for bosses, as there's different option and variables for bosses, starting from here, I'll only mention anything different
    global playerHP
    global monsterHealth
    global weaponMeleeDmg
    global weaponMagicDmg
    global weaponRangeDmg
    global weaponRogueDmg
    global totalPlayerDmg
    global currencyDrop
    global playerCurrency
    global monsterStatus
    global loopChecker
    global generalLoopCheck
    global gameLoop
    global deadLoop
    global playerDeadOption
    global randomBossDmg
    monsterStatus = True
    while monsterStatus == True:
        randomBossDmg = random.randint(
            10, 50
        )  # Instead of consistent damage, this boss does random damage between 1 and 50
        royalGuardSpawn = diceRoller(
            1, 3
        )  # This boss has a special ability to do 5 extra damage by summoning royal guards
        if royalGuardSpawn == 1:
            randomBossDmg = randomBossDmg + 5
        print()
        print("Processing.")
        time.sleep(0.2)
        print("Processing..")
        time.sleep(0.2)
        print("Processing...")
        time.sleep(0.2)
        print()
        print("=====================================================================")
        print(monsterClass)
        print(monsterType)
        print("Boss Health:", monsterHealth, "                               V'.'.'V ")
        print("Boss Damage: ???? (Random)                      {/_\}  ")
        print("==============================                 (/. .\)")
        print("                                               (\_-_/)")
        print("                                              .-~'='~-.")
        print("                                             /`~`*Y*`~`\ ")
        print("                                            / /(_ * _)\ \ ")
        print("                                           / /  )   (  \ \ ")
        print("                                           \ \_/\\_//\_/ /")
        print("           /^^^^\                           \/_) '*' (_\/")
        print("      ___^/      \__            Player Health:", playerHP)
        print("     \     _*^^^*, _/           Current Weapon:", weaponDrop)
        print("       - //  ^   _\             Melee attribute \u2694:", meleeAttribute)
        print("        {{|  .   .\             Magic attribute \u269a:", magicAttribute)
        print("         {|    _  /             Range attribute \u27b3:", rangeAttribute)
        print("           {  __ }  {^_-        Rogue attribute \u2604:", rogueAttribute)
        print("        _ {   \/ \  }|          Player coins:", playerCurrency)
        print("        /{|     \ \/}           ====================================")
        print("       /  |        |     ")
        print(":==================================================================:")
        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
        print("||:                           ||:     Fight     ||  UNAVAILABLE  :||")
        print("||:      Boss Encounter...    ||:--------------------------------:||")
        print("||:                           ||:  UNAVAILABLE  ||  UNAVAILABLE  :||")
        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
        print(":==================================================================:")
        print(
            "Queen Elizabeth stared into your soul, your ability to run or heal has been locked!"
        )
        print(
            "She's wearing her favourite yellow polka-dot dress! Your 20 sided dice roll must be larger than 8 to deal damage!"
        )
        print("What is your course of action?")
        print("\u21f0 Fight \u265e ")
        print(
            "\u21f0 UNAVAILABLE"
        )  # Running and healing becomes unavailable, I didn't want people healing during mid boss fight
        print("\u21f0 UNAVAILABLE")
        playerOptionInput = input("Option: ")
        loopChecker = True
        while loopChecker == True:
            if playerOptionInput == "Fight":
                print("What type of attack do you want to use?")
                print("\u21f0 Melee \u2694")
                print("\u21f0 Magic \u269a")
                print("\u21f0 Range \u27b3")
                print("\u21f0 Rogue \u2604")
                attributeInput = input("Option: ")
                print("Processing.")
                time.sleep(0.3)
                print("Processing..")
                time.sleep(0.3)
                print("Processing...")
                time.sleep(0.3)
                print()
                if attributeInput == "Melee":
                    random20Damage = diceRoller(1, 20)
                    if random20Damage == 20:
                        # Added natural 20 damage roll for all the classes, it doubles the 20 roll when its a natural
                        print("You rolled a natural 20! The roll now counts as 40dmg!")
                        random20Damage = random20Damage * 2
                    totalPlayerDmg = meleeAttribute + random20Damage + weaponMeleeDmg
                    if (
                        random20Damage <= 8
                    ):  # As part of the boss' gimmicks, only rolls above 10 will count as damage, otherwise, it's nulified
                        totalPlayerDmg = 0
                        print(
                            "Your roll was smaller than 8, the attack was nulified by her yellow polka-dot dress!"
                        )
                    meleeWeaponAbilities()
                    monsterRemainHp = monsterHealth - totalPlayerDmg
                    monsterHealth = monsterRemainHp
                    print(
                        "You rolled a "
                        + str(random20Damage)
                        + " on your 20 sided dice!"
                    )
                    print(
                        "You did "
                        + str(totalPlayerDmg)
                        + "DMG to the "
                        + monsterType
                        + "!"
                    )
                elif attributeInput == "Magic":
                    random20Damage = diceRoller(1, 20)
                    if random20Damage == 20:
                        print("You rolled a natural 20! The roll now counts as 40dmg!")
                        random20Damage = random20Damage * 2
                    totalPlayerDmg = magicAttribute + random20Damage + weaponMagicDmg
                    if random20Damage <= 8:
                        totalPlayerDmg = 0
                        print(
                            "Your roll was smaller than 8, the attack was nulified by her yellow polka-dot dress!"
                        )
                    monsterRemainHp = monsterHealth - totalPlayerDmg
                    magicWeaponAbilities()
                    monsterHealth = monsterRemainHp
                    monsterHealth = monsterRemainHp
                    print(
                        "You rolled a "
                        + str(random20Damage)
                        + " on your 20 sided dice!"
                    )
                    print(
                        "You did "
                        + str(totalPlayerDmg)
                        + "DMG to the "
                        + monsterType
                        + "!"
                    )
                    print("You healed " + str(playerHealAmountRd) + "HP!")
                elif attributeInput == "Range":
                    print("You have 1% chance to hit the monster's weakspot!")
                    random20Damage = diceRoller(1, 20)
                    if random20Damage == 20:
                        print("You rolled a natural 20! The roll now counts as 40dmg!")
                        random20Damage = random20Damage * 2
                    totalPlayerDmg = rangeAttribute + random20Damage + weaponRangeDmg
                    if random20Damage <= 8:
                        totalPlayerDmg = 0
                        print(
                            "Your roll was smaller than 8, the attack was nulified by her yellow polka-dot dress!"
                        )
                    print(
                        "You rolled a "
                        + str(random20Damage)
                        + " on your 20 sided dice!"
                    )
                    rangeWeaponAbilities()
                    monsterRemainHp = monsterHealth - totalPlayerDmg
                    monsterHealth = monsterRemainHp
                    print(
                        "You did "
                        + str(totalPlayerDmg)
                        + "DMG to the "
                        + monsterType
                        + "!"
                    )
                elif attributeInput == "Rogue":
                    rogueWeaponAbilities()
                    random20Damage = diceRoller(1, 20)
                    if random20Damage == 20:
                        print("You rolled a natural 20! The roll now counts as 40dmg!")
                        random20Damage = random20Damage * 2
                    totalPlayerDmg = rogueAttribute + random20Damage + weaponRogueDmg
                    if random20Damage <= 8:
                        totalPlayerDmg = 0
                        print(
                            "Your roll was smaller than 8, the attack was nulified by her yellow polka-dot dress!"
                        )
                    monsterRemainHp = monsterHealth - totalPlayerDmg
                    monsterHealth = monsterRemainHp
                    print(
                        "You rolled a "
                        + str(random20Damage)
                        + " on your 20 sided dice!"
                    )
                    print(
                        "You did "
                        + str(totalPlayerDmg)
                        + "DMG to the "
                        + monsterType
                        + "!"
                    )
                elif attributeInput != "Melee" or "Magic" or "Range" or "Rogue":
                    print("Player input not accepted, try again")
                    break

            if playerOptionInput != "Fight":
                print()
                print("Player input not accepted, try again")
                break

            if monsterHealth >= 1 and loopChecker == True:
                monsterStatus = True
                print("The monster has " + str(monsterRemainHp) + "HP left!")
                playerRemainHP = playerHP - randomBossDmg
                playerHP = playerRemainHP
                if royalGuardSpawn == 1:
                    print(
                        "Her majesty received help from her royal guards, dealing 5 extra damage!"
                    )
                elif randomBossDmg == 0:
                    print("You manage to dodge the boss' attack!")
                else:
                    if (
                        playerHP <= 0
                    ):  # This two lines is to ensure when printing remaining player health, it doesn't go negative as it looks weird
                        playerHP = 0
                    print(
                        monsterType
                        + " fired her SA80 rifle. You took "
                        + str(randomBossDmg)
                        + "DMG and have "
                        + str(playerHP)
                        + "HP left!"
                    )
                    print("The monster lived to tell its tale")
                    time.sleep(5)
                    print()
                break

            elif monsterHealth <= 0 and loopChecker == True:
                monsterStatus = False
                print("The monster was subjugated \u2620")
                playerCurrency += currencyDrop
                print("You got " + str(currencyDrop) + " gold coins!")
                print("You currently have " + str(playerCurrency) + " gold coins!")
                break

        if playerHP <= 0:
            monsterStatus = True
            print(
                " __  __     ______     __  __        _____     __     ______     _____  "
            )
            time.sleep(0.5)
            print(
                "/\ \_\ \   /\  __ \   /\ \/\ \      /\  __-.  /\ \   /\  ___\   /\  __-."
            )
            time.sleep(0.5)
            print(
                "\ \____ \  \ \ \/\ \  \ \ \_\ \     \ \ \/\ \ \ \ \  \ \  __\   \ \ \/\ \ "
            )
            time.sleep(0.5)
            print(
                " \/\_____\  \ \_____\  \ \_____\     \ \____-  \ \_\  \ \_____\  \ \____- "
            )
            time.sleep(0.5)
            print(
                "  \/_____/   \/_____/   \/_____/      \/____/   \/_/   \/_____/   \/____/ "
            )
            deadLoop = True
            while deadLoop == True:
                loopChecker = False
                monsterStatus = False
                print(
                    "Do you want to be reincaranted into the world? (New stats, weapons etc.)"
                )
                playerDeadOption = input("(Yes/No): ")
                if playerDeadOption == "Yes":
                    gameLoop = True
                    print("You wish has been granted")
                    break
                elif playerDeadOption == "No":
                    deadLoop = False
                    gameLoop = False
                    generalLoopCheck = False
                    print("Oh well, guess you'll die")
                    break
                else:
                    print("Player input not accepted, try again")
                    print()


# Functions below are pretty similar, but for different rarity of monsters (including boss), so I'll only comment on the common monster spawns/fight
def randomCommonMonster(
    spawnNum,
):  # A function to spawn random common monster with a parameter how the amount
    for spawn in range(
        spawnNum
    ):  # Loop according to the amount of spawns in the parameter
        global monsterSpawn  # Some global variables to be used in other functions
        global monster1
        global monsterHealth
        global monsterDmg
        global monsterType
        global monsterClass
        global currencyDrop
        commonMonsterList = [
            "Slime",
            "Goblin",
            "Giant Rat",
            "Angry Vulture",
            "Pixie",
            "Bokoblin",
        ]  # List of monsters(common)
        commonMonster = random.choice(
            commonMonsterList
        )  # Chooses a random string within the list
        monster1 = "You've ecountered a " + commonMonster + ", it's a common monster!"
        monsterType = commonMonster
        monsterClass = "Common Monster"
        monsterSpawn = monster1
        monsterHealth = 20
        monsterDmg = 15
        currencyDrop = 20


def randomUncommonMonster(spawnNum):
    for spawn in range(spawnNum):
        global monsterSpawn
        global monster2
        global monsterHealth
        global monsterDmg
        global monsterType
        global monsterClass
        global currencyDrop
        uncommonMonsterList = [
            "Ogre",
            "Poison Spider",
            "Jackalope",
            "Chest Mimic",
            "Lizalfos",
        ]
        uncommonMonster = random.choice(uncommonMonsterList)
        monster2 = (
            "You've ecountered a " + uncommonMonster + ", it's an uncommon monster!"
        )
        monsterType = uncommonMonster
        monsterClass = "Uncommon Monster"
        monsterSpawn = monster2
        monsterHealth = 30
        monsterDmg = 15
        currencyDrop = 30


def randomRareMonster(spawnNum):
    for spawn in range(spawnNum):
        global monsterSpawn
        global monster3
        global monsterHealth
        global monsterDmg
        global monsterType
        global monsterClass
        global currencyDrop
        rareMonsterList = ["Harpy", "Hell Hound", "Griffin", "Moblin", "Lynel"]
        rareMonster = random.choice(rareMonsterList)
        monster3 = "You've ecountered a " + rareMonster + ", it's a rare monster!"
        monsterType = rareMonster
        monsterClass = "Rare Monster"
        monsterSpawn = monster3
        monsterHealth = 40
        monsterDmg = 18
        currencyDrop = 40


def randomSuperrareMonster(spawnNum):
    for spawn in range(spawnNum):
        global monsterSpawn
        global monster4
        global monsterHealth
        global monsterDmg
        global monsterType
        global monsterClass
        global currencyDrop
        superrareMonsterList = [
            "Wyvern",
            "Earth Golem",
            "Orge King",
            "landkreuzer p. 1000 ratte tank",
            "Waterblight Ganon",
        ]
        superrareMonster = random.choice(superrareMonsterList)
        monster4 = (
            "You've ecountered a " + superrareMonster + ", it's a super rare monster!"
        )
        monsterType = superrareMonster
        monsterClass = "SuperRare Monster"
        monsterSpawn = monster4
        monsterHealth = 70
        monsterDmg = 20
        currencyDrop = 50


def bossSpawn(spawnNum):
    for spawn in range(spawnNum):
        global monsterSpawn
        global monster5
        global monsterHealth
        global monsterDmg
        global monsterType
        global monsterClass
        global currencyDrop
        bossMonster = "Queen Elizabeth the Immortal"
        monster5 = "You've ecountered the final boss, it's " + bossMonster + " herself"
        monsterType = bossMonster
        monsterClass = "Boss Monster"
        monsterSpawn = monster5
        monsterHealth = 100
        currencyDrop = 100


def commonMonsterFight():  # A function for the actual fight with a common monster
    randomCommonMonster(
        1
    )  # The function that spawns a common monster with the parameter 1
    print(monster1)
    allFights()  # The function that initiates the fight with the common monster


def uncommonMonsterFight():
    randomUncommonMonster(1)
    print(monster2)
    allFights()


def rareMonsterFight():
    randomRareMonster(1)
    print(monster3)
    allFights()


def superrareMonsterFight():
    randomSuperrareMonster(1)
    print(monster4)
    allFights()


def bossFight():
    bossSpawn(1)
    print(monster5)
    bossFights()


preGameNote()  # Runs the function preGameNote, it's a wall of text
print()
input(
    "Press any key and enter to continue... "
)  # Just so the game doesn't start immediately, it gives player time to read the wall of text
print()
usrName = input(
    "What is your name, brave adventurer?: "
)  # Allows players to input their name
usrNameLen = len(usrName)  # Calculates the amount of letters in the player's name
spacesAfterName = (
    18 - usrNameLen
)  # This is used for adding appropriate spaces in the adventure card
print("Henry stickmin would be proud of you, " + usrName)
backStory()
gameLoop = True  # Assigning a variable that is useful in the next line for looping
while (
    gameLoop == True
):  # As long as gameLoop is true, the codes indented below will loop
    time.sleep(1)
    modifierRoller()  # Runs the function modifierRoller, gives the player random stats
    print()
    time.sleep(1)
    randomWeapon()  # Runs the function random Weapon, gives the player a random weapon
    print()
    time.sleep(1)
    bossCheck = 4  # Assigning 0 to a variable, so it can be used later via checking the number of times the codes were loop
    generalLoopCheck = True  # Assigning a variable that is useful in the next line for looping, in particular, crash proofing
    while (
        generalLoopCheck == True
    ):  # As long as generalLoopCheck is true, the codes indented below will loop
        print()
        print("Are you ready to take on an adventure?")
        playerAdInput = input(
            "(Yes/No): "
        )  # Another input for the user on yes or no, but any other answers will not crash the game
        print()

        if (
            playerAdInput == "Yes"
        ):  # If statement for the input, if the input is yes, executes the codes indented below
            bossCheck += 1  # Adds one to the variable I previously mentioned, this happens everything the codes are looped
            randomMonsterType = diceRoller(
                1, 100
            )  # Similar to how I control weapon spawn rates, it also used to control monster spawn rate
            if (
                randomMonsterType <= 10
            ):  # For example, the chance of super rare monster spawning is 10%
                superrareMonsterFight()
            elif randomMonsterType <= 30:
                rareMonsterFight()
            elif randomMonsterType <= 55:
                uncommonMonsterFight()
            elif randomMonsterType <= 100:
                commonMonsterFight()

        elif (
            playerAdInput == "No"
        ):  # Elif statement for the input, if the input is no, executes the codes indented below
            print("Seems like you're not ready for the adventure :(")
            print("Do you wish to heal your character?")
            playerHealingOption = input(
                "(Yes/No): "
            )  # Another input choice for players
            if playerHealingOption == "Yes":
                playerHealing()  # Executes the healing function for player
            elif playerHealingOption == "No":
                print("Hmm..Do you wish to check my functions?")
                playerCustomFunction = input("(Yes/No): ")
                if playerCustomFunction == "Yes":
                    print("Do as you please")
                    gameLoop = False  # Stops the game from looping
                    break  # Forces the game out of loop early
                elif playerCustomFunction == "No":
                    print("Well than why aren't you ready?")
                else:  # This else is for playerCustomFunction
                    print("Player input not accepted, try again")
            else:  # This else is for playerHealingOption
                print("Player input not accepted, try again")
        else:  # This else is for playerAdInput
            print("Player input not accepted, don't worry, I can wait")

        if (
            bossCheck == 5
        ):  # If the previously mentioned variable reaches 5, executes codes indented below
            time.sleep(2)
            gameLoop = False  # Stops the game from looping
            generalLoopCheck = False  # Stops the monster spawning from looping
            bossFight()  # Executes the function for boss fight
            if (
                monsterStatus == False and playerHP >= 1
            ):  # If the boss is dead, and player has more than 0 hp, executes codes indented below
                print(
                    "You've somehow defeated the final boss in the game, congratulations!"
                )
                print(
                    " __   __   __     ______     ______   ______     ______     __  __ "
                )
                time.sleep(0.5)
                print(
                    "/\ \ / /  /\ \   /\  ___\   /\__  _\ /\  __ \   /\  == \   /\ \_\ \   "
                )
                time.sleep(0.5)
                print(
                    "\ \  '/   \ \ \  \ \ \____  \/_/\ \/ \ \ \/\ \  \ \  __<   \ \____ \  "
                )
                time.sleep(0.5)
                print(
                    " \ \__|    \ \_\  \ \_____\    \ \_\  \ \_____\  \ \_\ \_\  \/\_____\ "
                )
                time.sleep(0.5)
                print(
                    "  \/_/      \/_/   \/_____/     \/_/   \/_____/   \/_/ /_/   \/_____/ "
                )
                print("One impostor remains..")
                gameEndCheck = True  # Another one of those variable things for loop
                while (
                    gameEndCheck == True
                ):  # As long as gameEndCheck is true, it will continue to loop, used for crash proofing
                    print("Do you want to play the game again?")
                    gameEndLoop = input("(Yes/No): ")
                    if (
                        gameEndLoop == "Yes"
                    ):  # If player inputs yes, executes codes indented below
                        playerHP = 100  # Resets player health to 100
                        playerCurrency = 0  # Resets player coing to 0
                        bossCheck = 0  # Resets loop check to 0
                        print("OK, your request was granted")
                        gameEndCheck = False  # Ends the loop for monster spawning
                        gameLoop = True  # The gameLoop will stay true, so the game will continue to loop
                        break  # Forces the game out of this loop
                    elif gameEndLoop == "No":
                        gameEndCheck = False
                        break
                    else:
                        print("Player input not accepted, try again")
            break

        if (
            playerHP <= 0
        ):  # If player is dead, executes break below, forces the game out of loop
            break
