# Random chess
Random chess is a pyhton class for creating *random* first rank according to a certain random mode. The random mode
    specifies the rules with which the randomly shuffled peices should be situated. For example, *Fischer random chess* requires that the king be between two rooks and that the bishops must have different colors.

## Usage
Here is a minimal example using Fischer random mode:

```
RC=RandomChess()# create a random chess object

# RC has a method called  ShuffleFirstRank that 
# shuffles the first rank if the conditions of RandomMode
# are satisfied. It internally changes a property called 
# ShuffledFirstRank. 

RC.ShuffleFirstRank(RandomMode='Fischer')

# To see the shuffled first rank use a method called
# printFirstRank.

RC.printFirstRank()
['♖', '♗', '♗', '♘', '♔', '♕', '♖', '♘']
```