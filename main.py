#!/usr/bin/env python3.6
# Fighting Arena v0.1.0
# coding: utf-8 

import os;
import re;
import random;
from Classes.classCharacter import Character;
from Classes.classCharacter import Hero;
from Classes.classCharacter import Monster;
from Classes.classItem import Item;
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

    while keyboardInput!="q" and hero.getLife() > 0:
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

    if hero.getLife() <= 0 :
        clear();
        print("... You are dead ...");
        print(" ");
        print("... Game over !");
        print(" ");
        print(" ");
        print(" ");
        print("Press Enter to leave.");
        keyboardInput = input();

def encounter(hero):
    clear();
    mobSelect = random.randrange(1,4,1);

    if mobSelect == 1:
        monster = "Orc"
    if mobSelect == 2:
        monster = "Oger"
    if mobSelect == 3:
        monster = "Goblin" 

    monster = Monster(monster)
    print("An "+monster.getType()+" is on your way : ");
    print(""+monster.getType()+" Statistics : ");
    print("Strength : "+str(monster.getStrength()))
    print("Speed : "+str(monster.getSpeed()))
    print("Intelligence : "+str(monster.getIntelligence()))
    print("Life : "+str(monster.getLife()))
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
            fight(hero,monster);
    if keyboardInput == "f":
        print("Ready to fight !");
        keyboardInput = input();
        fight(hero,monster);
        
    
def fight(hero,monster):
    clear();
    turn = 0;
    if monster.getSpeed() < hero.getSpeed():
        turn = 1;
    else:
        turn = 2;
    while monster.getLife() > 0 and hero.getLife() > 0:
        clear();
        print(""+monster.getType()+" Statistics : ");
        print("Strengh : "+str(monster.getStrength()))
        print("Speed : "+str(monster.getSpeed()))
        print("Intelligence : "+str(monster.getIntelligence()))
        print("Life : "+str(monster.getLife()))
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
                print(monster.getType()+" choose to block high ! ");
            if mobChoice == 2:
                print(monster.getType()+" choose to block low ! ");
            if mobChoice == 3:
                print(monster.getType()+" choose to block right ! ");
            if mobChoice == 4:
                print(monster.getType()+" choose to block left ! ");
            if attackChoice == mobChoice:
                damage = hero.getStrength()+hero.getSpeed()-monster.getStrength()-monster.getSpeed();
                if damage > 0:
                    print("You have dealed "+str(damage)+" damages !");
                    monster.setLife(monster.getLife()-damage);
            else:
                damage = hero.getStrength();
                print("You have dealed "+str(damage)+" damages !");
                monster.setLife(monster.getLife()-damage);
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
                print(monster.getType()+" choose to strike high ! ");
            if mobChoice == 2:
                print(monster.getType()+" choose to strike low ! ");
            if mobChoice == 3:
                print(monster.getType()+" choose to strike right ! ");
            if mobChoice == 4:
                print(monster.getType()+" choose to strike left ! ");
            if blockChoice == mobChoice:
                damage = monster.getStrength()+monster.getSpeed()-hero.getStrength()-hero.getSpeed();
                if damage > 0:
                    print("You have taken "+str(damage)+" damages !");
                    hero.setLife(hero.getLife()-damage);
            else:
                damage = monster.getStrength();
                print("You have taken "+str(damage)+" damages !");
                hero.setLife(hero.getLife()-damage);
            turn = 1;
            keyboardInput = input();
    keyboardInput = input();

hero = intro();
maingame(hero);