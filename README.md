# Terminal Battle Game - Codecademy Computer Science Project

This is a solution to the First Chapter of the Computer Science Course in Codecademy: Introduction to Programming.

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [About the game](#about-the-game)
- [Run the game](#run-the-game)
- [The Rules](#the-rules)
  - [Player setup](#player-setup)
  - [Soldiers setup](#soldiers-setup)
  - [Position and range](#position-and-range)
  - [Initiative](#initiative)
  - [Health points](#health-points)
  - [Attack and defence](#attack-and-defence)
  - [Arrow protection](#arrow-protection)
  - [Game flow](#game-flow)
- [Author](#author)

## Overview

### The challenge

The goal of the project was to create an interactive terminal program in Python.
The Terminal Battle Game (TBG) is mainly written in object-oriented programming concept.

### About the game

The TBG it's a simple turn-based tactical game set in the medieval ages. Two teams (parties) with an equal
number of soldiers fight to the death or surrender. Soldiers are fixed in their positions in one of two lines 
and they can attack enemy soldiers only in their range.
The TBG allows you to play against a human player or a computer.

## Run the game

To run the game copy files: `party.py`, `data.py`, `gameplay.py`, `script.py` and `soldier.py`.
Type in your terminal:
```
$ python3 script.py
```

## The Rules

### Player setup

At the beginning of the game Player 1 is asked to set the soldiers' number in both parties.
Then Player 1 writes the party's name and creates soldiers.
After creating Player's 1 party the type of Player 2 is chosen between the human or the computer.
The computer party is created randomly and the user does not influence that process.
The human second player creates a party in the same way as the first player.

### Soldiers setup

A player writes the soldier's name and chooses his specialization from the below list:
- swordsman: attack: 3, defence: 1, initiative: 2, position: 1, range: 1,
- defender: attack: 0, defence: 3, initiative: 1, position: 1, range: 1,
- archer: attack: 2, defence: 0, initiative: 3, position: 2, range: 2, 
- pikeman: attack: 3, defence: 1, initiative: 1, position: 2, range: 1.
In each row, basic attributes of specializations are shown. If you want to do some modifications, edit the `data.py` file.
Warning! Don't change position and range due to possible program issues.
Attack, defence and initiative can be enhanced in the further part of the setup. Each soldier has 4 attribute points
which can be spent on the above three attributes.

### Position and range

Soldiers can be placed in four rows respectively two rows for each party. Close combat soldiers such as swordsmen and defenders stand
in two middle rows (position attribute equal 1 - front-line). Ranged combat soldiers such as archers and pikemen stand in two external rows (position attribute equal 2, back-line).
If a soldier's position attribute is greater than the enemy's range attribute the soldier cannot be hit.
Note! It is possible that all soldiers in the frot-line are dead or any close combat soldiers were not chosen during setup. 
      In these situations, the position of backline soldiers is reduced and such soldiers become vulnerable to close attacks.

### Initiative

The order of the attack depends on initiative attribute value - the higher initiative, the earlier the soldier attacks.
Note! It is possible to eliminate a soldier before his turn.

### Health points

Each soldier has 10 health points (HP).
If you want to change this value, modify the below code in `soldier.py`.

```python
class Soldier:
  #The constructor function
  def __init__(self, name):
    self.health = 10
```

### Attack and defence

Damage points calculation is based on the below formula:
```
damage = attack - enemy defence // 2
```
The enemy loses at least 1 HP even though the calculated damage points are less than 1.
This rule helps to avoid the situation when soldiers don't lose HP and the game is infinitely long.

### Arrow protection

Defenders provide additional defence to soldiers who stand in the back line against arrows.
```
arrow damage = attack - (enemy defence + arrow protection) // 2
```
In case of the presence of more than one defender, the mean value based on their defence attributes is computed.

### Game flow

The game is divided into rounds and each round is divided into turns.
In each turn, one soldier can attack one enemy who stands in his range.
Human players can also check the statistics of each soldier and surrender to finish the game earlier.
The computer player fights until has live soldiers.
The Game finishes when all soldiers in one party are dead.

## Author

- Website - [Krzysztof Łęczycki](https://krzysztofleczycki.github.io/portfolio/)

