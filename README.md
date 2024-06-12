# OpenTaxus Default Text

| [Readme](README.md) | [Using the Badge](docs/BADGE.md) | [Playing the Game](docs/GAME.md) | [Software Development](docs/DEVELOP.md) | [Badge Hardware](docs/HARDWARE.md) |
| ------------------- | -------------------------------- | -------------------------------- | --------------------------------------- | ---------------------------------- |

## Badge Game

The OpenTaxus Badge is designed for playing the Attribution Game.
Similar to the board game Clue or some versions of Carmen Sandiego,
you need to figure out who the threat actor, attack tool, and victim
are for each round of the game. You do this by trading cards (or
'clues') as well as your self-entered alibi name with others
at the conference.

## Attribution Game basics

In order to play in the Attribution Game, you will need to enter a name or handle when you first turn on your badge. This will stay through power cycles. It can be cleared in your settings which will force you to enter a new one.

To trade cards with someone, scroll left or right until you get to the "BSidesSF '24" screen.
Once there, press the toggle up, and place your badge edge at the top of the screen against
the same badge edge of the person you are trading with. You should see once your card has
been transmitted and you have received a card from them.

You can check your collected cards by scrolling right from the "Badge '24" screen.

When you collect enough cards, the one remaining is the solution that completes the phrase. There are 6 games to play through - try them all!

Please see [Playing the Game](docs/GAME.md) for more details

## Repo Contents

This repository contains the hardware and software for
the badge and game. We hope it is useful for those who wish to hack
the badges and game, anyone who wants to use the badge to learn some
circuitpython, as well as others who might like to reuse some or all
of it for other projects.

The badge hardware was designed and produced by @securityfitz, with variants being used for BSidesSF 2024 and Labscon.
Ths badge software is a fork of the Labscon badge software, further mangled by @rlc4, @lanrat, and @securelyfitz.
