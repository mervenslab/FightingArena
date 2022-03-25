#!/usr/bin/env python3.6
# Fighting Arena v0.1.0
# coding: utf-8 

import os;
import re;
import random;
from Classes.classCharacter import Character;
from Classes.classCharacter import Hero;
clear = lambda: os.system('clear');
clear();

hero = None;


def intro():

    print("Welcome to Fighting Arena !");
    print("Choose a character : ");
    print("1 - Warrior");
    print("2 - Rogue");
    print("3 - Mage");
    choice = input();
    if re.search("[1-3]",choice):
        choice = int(choice);

    while choice not in range(1,4,1):
        clear();
        print("Please choose a number between 1 and 3 to select your character :");
        print("1 - Warrior");
        print("2 - Rogue");
        print("3 - Mage");
        choice = input();
        if re.search("[1-3]",choice):
            choice = int(choice);

    if choice == 1:
        print("You have chosen a Warrior.");
        hero = "Warrior";

    if choice == 2:
        print("You have chosen a Rogue.");
        hero = "Rogue";
    if choice == 3:
        print("You have chosen a Mage.");
        hero = "Mage";

    print(" ");
    print(" ");
    print(" ");
    print(" ");
    print(" ");
    print("  /\ ");
    print("  || ");
    print("  || ");
    print("O====O ");
    print("  || ");
    print("  ¯¯ ");

    wait = input("Press Enter to continue.");

    return hero;

def maingame(hero):
    keyboardInput = None;
    
    hero = Hero(hero)

    while keyboardInput!="q":
        clear();
        print("                                                                  Statistics : ");
        print("                                                                  Strengh : "+str(hero.getStrength()));
        print("                                                                  Speed : "+str(hero.getSpeed()));
        print("                                                                  Intelligence : "+str(hero.getIntelligence()));
        print("                                                                  Life : "+str(hero.getLife()));
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print("Menu : ");
        print("ˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍ");
        print("| e to explore | q to quit |");
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯");

        keyboardInput = input();
        if keyboardInput == "e":
            random.seed();
            exploring = random.randrange(1,100,1);
            if exploring in range(0,80,1):
                encounter(hero);
            if exploring in range(81,100,1):
                print("You found a potion of life !")
                keyboardInput = input();

def encounter(hero):
    clear();
    orcStats = {"Strengh" : 7, "Speed" : 6, "Intelligence" : 3, "Life" : 15, "Name" : "Orc"};
    ogerStats = {"Strengh" : 14, "Speed" : 4, "Intelligence" : 1, "Life" : 30, "Name" : "Oger"};
    goblinStats = {"Strengh" : 3, "Speed" : 10, "Intelligence" : 6, "Life" : 8, "Name" : "Goblin"};
    mobSelect = random.randrange(1,4,1);
    mobStats = None;
    if mobSelect == 1:
        mobStats = orcStats;
    if mobSelect == 2:
        mobStats = ogerStats;
    if mobSelect == 3:
        mobStats = goblinStats;    
    print("An "+mobStats["Name"]+" is on your way : ");
    print(""+mobStats["Name"]+" Statistics : ");
    print("Strengh : "+str(mobStats["Strengh"]));
    print("Speed : "+str(mobStats["Speed"]));
    print("Intelligence : "+str(mobStats["Intelligence"]));
    print("Life : "+str(mobStats["Life"]));
    print("                                                                    Statistics :  ");
    print("                                                                    Strengh : "+str(hero.getStrength()));
    print("                                                                    Speed : "+str(hero.getSpeed()));
    print("                                                                    Intelligence : "+str(hero.getIntelligence()));
    print("                                                                    Life : "+str(hero.getLife()));
    print(" ");
    print(" ");
    print(" ");
    print(" ");
    print(" ");
    print(" ");
    print("Menu : ");
    print("ˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍ");
    print("| f to fight  | r to runaway  | q to quit |");
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯");
    keyboardInput = input();
    if keyboardInput == "r":
        runaway = random.randrange(1,5,1);
        if runaway == 4:
            print("You escaped !");
            keyboardInput = input();
        else:
            print("You have failed to run away !");
            keyboardInput = input();
            fight(hero,mobStats);
    if keyboardInput == "f":
        print("Ready to fight !");
        keyboardInput = input();
        fight(hero,mobStats);
        
    
def fight(hero,mobStats):
    clear();
    turn = 0;
    if mobStats['Speed'] < hero.getSpeed():
        turn = 1;
    else:
        turn = 2;
    while mobStats['Life'] > 0 and hero.getLife() > 0:
        clear();
        print(""+mobStats["Name"]+" Statistics : ");
        print("Strengh : "+str(mobStats["Strengh"]));
        print("Speed : "+str(mobStats["Speed"]));
        print("Intelligence : "+str(mobStats["Intelligence"]));
        print("Life : "+str(mobStats["Life"]));
        print("                                                                    Statistics :  ");
        print("                                                                    Strengh : "+str(hero.getStrength()));
        print("                                                                    Speed : "+str(hero.getSpeed()));
        print("                                                                    Intelligence : "+str(hero.getIntelligence()));
        print("                                                                    Life : "+str(hero.getLife()));
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print(" ");
        print("Menu : ");
        


    
        if turn == 1:
            print("Select an attack : ");
            print("1 - High Strike");
            print("2 - Low Strike");
            print("3 - Right Strike");
            print("4 - Left Strike");
            attackChoice = int(input());
            mobChoice = random.randrange(1,5,1);
            if attackChoice == 1:
                print("You choose to strike high ! ");
            if attackChoice == 2:
                print("You choose to strike low ! ");
            if attackChoice == 3:
                print("You choose to strike right ! ");
            if attackChoice == 4:
                print("You choose to strike left ! ");
            if mobChoice == 1:
                print(mobStats['Name']+" choose to block high ! ");
            if mobChoice == 2:
                print(mobStats['Name']+" choose to block low ! ");
            if mobChoice == 3:
                print(mobStats['Name']+" choose to block right ! ");
            if mobChoice == 4:
                print(mobStats['Name']+" choose to block left ! ");
            if attackChoice == mobChoice:
                damage = hero.getStrength()+hero.getSpeed()-mobStats['Strengh']-mobStats['Speed'];
                if damage > 0:
                    print("You have dealed "+str(damage)+" damages !");
                    mobStats['Life'] = mobStats['Life']-damage;
            else:
                damage = hero.getStrength();
                print("You have dealed "+str(damage)+" damages !");
                mobStats['Life'] = mobStats['Life']-damage;
            turn = 2;
            keyboardInput = input();
        elif turn == 2:
            print("Select a block : ");
            print("1 - High Block");
            print("2 - Low Block");
            print("3 - Right Block");
            print("4 - Left Block");
            blockChoice = int(input());
            mobChoice = random.randrange(1,5,1);
            if blockChoice == 1:
                print("You choose to block high ! ");
            if blockChoice == 2:
                print("You choose to block low ! ");
            if blockChoice == 3:
                print("You choose to block right ! ");
            if blockChoice == 4:
                print("You choose to block left ! ");
            if mobChoice == 1:
                print(mobStats['Name']+" choose to strike high ! ");
            if mobChoice == 2:
                print(mobStats['Name']+" choose to strike low ! ");
            if mobChoice == 3:
                print(mobStats['Name']+" choose to strike right ! ");
            if mobChoice == 4:
                print(mobStats['Name']+" choose to strike left ! ");
            if blockChoice == mobChoice:
                damage = mobStats['Strengh']+mobStats['Speed']-hero.getStrength()-hero.getSpeed();
                if damage > 0:
                    print("You have taken "+str(damage)+" damages !");
                    hero.setLife(hero.getLife()-damage);
            else:
                damage = mobStats['Strengh'];
                print("You have taken "+str(damage)+" damages !");
                hero.setLife(hero.getLife()-damage);
            turn = 1;
            keyboardInput = input();
    keyboardInput = input();

hero = intro();
maingame(hero);