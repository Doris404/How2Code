# Instruction of Texas Holdem
> Texas hold 'em (also known as Texas holdem, hold 'em, and holdem) is one of the most popular variants of the card game of poker. Each player in this game hold 2 cards and tries to construct specific patterns with 5 public cards on board. It is one of the most interesting poker game in the world! (ps: at least I think so!)

The pipeline of this game is simple, and can be summarized as follow:

- **step 1** each player get 2 cards in hand (without showing them to others of course) 
- **step 2** blind deal: offer a price of their cards without any public cards
- **step 3** flop cards (3 of them) are delivered publicly
- **step 4** deal: now each player know 2 private cards and 3 public cards and offer another price for their card
- **step 5** turn card (1 of it) are deliverd publicly
- **step 6** deal: 4 public cards are shown now
- **step 7** river cards (1 of it are delivered) which is the last card delivered
- **step 8** deal: the last deal
- **step 9** showdown: each players that still on board show their patterns and the biggest pattern get all money
  
In each deal, players should pay for the next step. For example, if player A bet on 10, you must at least bet on 10, or else, you will have to leave the game (ps: You can also bet on more than 10 e.g. 20, 40 anyway).

# Rules of Texas Holdem
As mentioned before, each player should pay for their cards. The price should be set based on specific rules.

**Rules for bet**
- SB (Small Blind) and BB (Big Blind) **MUST PAY** in the blind deal. This is a rule for pushing players to pay for this game. Players may pay nothing to play this game if this rule is not strictly executed. (ps: This game is not interesting if no one pay)
- The price you call should be one of: 1/ the same as the last player call 2/ you do not want to play this turn and call 0 (ps: fold) 3/ you think your card is likely to win, so you want to call more, then you should call integer multiple of the previous player (ps: the last player bet on $10, you can bet on $20 but not $11)
- All players bet one by one until the dealer do the last bet.

**Special player**
- SB (Small Blind) & BB (Big Blind): They are the first player to bet in the first deal. To speed up the game, they are required to bet on specific price. In general, we can make SB must bet on 5 and BB must bet on 10 in the first deal. Or you can make SB and BB must bet on 10 and 20 respectively. By the way, BB must bet on two times of SB.
- D (Dealer): The last player to bet. (ps: It can also be called Button)
- T (Trigger): The first player who can decide its bet free.

The order of bet is: SB->BB->T->other players->D

**Pattern**
The biggest pattern left on board will win all money.
|  Name   | Description  |  Example |
|  ----  | ----  |  ----    |
| High Card (高牌)  |   Simple value of the card. Lowest: 2 – Highest: Ace (King in the example)    |   CT H4 D7 CK S2|
| Pair（一对）| Two cards with the same value | CT HT D7 CK S2 |
| Two pairs (两对)| Two times two cards with the same value | CT HT D7 C7 S2 |
| Three of a kind (三条)| Three cards with the same value | CT HT DT C7 S2 |
| Straight (顺子) | Sequence of 5 cards in increasing value (Ace can precede 2 and follow up King), not of the same suit | H3 C4 S5 D6 S7 |
| Flush (同花) | 5 cards of the same suit, not in sequential order | CT C4 C7 CK C2 | 
| Full house (葫芦) | Combination of three of a kind and a pair | CK HK SK S7 D7|
| Four of a kind (四条) | Four cards of the same value | C6 H6 D6 S6 SK |
| Straight flush (同花顺) | Straight of the same suit | S2 S3 S4 S5 S6 |
| Royal Flush (皇家同花顺) | Straight of spade and the contains SA | ST SJ SQ SK SA | 


# Strategy
The strategy is hard to summary. Basically, some experts can decide their price based on the possiblity of each pattern. For example, if you get SK and HK your hand, it is claimed that you are likely to win the game, and you should bet on more. 

Possiblity of each hand to win the game has been summrized by several, and you can find the result in the internet.

# Reference
- Instruction on wikipedia: https://en.wikipedia.org/wiki/Texas_hold_%27em 
