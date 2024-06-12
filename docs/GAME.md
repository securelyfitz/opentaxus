# Game

| [Readme](../README.md) | [Using the Badge](BADGE.md) | [Playing the Game](GAME.md) | [Software Development](DEVELOP.md) | [Badge Hardware](HARDWARE.md) |
| ---------------------- | --------------------------- | --------------------------- | ---------------------------------- | ----------------------------- |

## Premise

You are an analyst looking for clues to attribute an attack. For BSidesSF, we expanded the attribution to a wider array of mad-libs style phrases.

The matching clues to the actual solution/attribution are sealed away - no alibi will vouch for them.

## Playing

Each badge has a clue which it can share with other badges. If someone's badge (the alibi) shares a signed clue,
then that item cannot be in the solution and can be eliminated from consideration.

Each badge also has an owner, represented by the string you enter. That owner is providing the
alibi for that clue. ex: 'Morgan says it wasn't Crazy Pande'

Once you have ruled out all of the possible clues, you know what cards are in the solution, and thus
the proper attribution of the actor, tool, and victim - or what the extended categories might be

Your badge has a relatively simple UI to allow you to trade your badge's card with other badges.

On your badge, you can see what identified provided you with each card.

There are several "rounds" of the game. Once you have solved a round, you can move on to the next.

There is no prize other than bragging rights to finishing the game.

### Trading

[![Badge Trading](https://img.youtube.com/vi/KiMAsULP7pg/0.jpg)](https://www.youtube.com/watch?v=KiMAsULP7pg)

## Security

We believe the game is cryptographically protected against a malicious
attendee cheating or otherwise spoiling the game, and we eagerly await
challenges to that expectation.

If you think you have managed to defeat these protection,
please find @securelyfitz in the BSidesSF slack. You will
be expected to show a PoC.

Access to the BSidesSF slack can
be found in the nav of the [BSidesSF Website](https://bsidessf.org).
