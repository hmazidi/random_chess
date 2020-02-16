class RandomChess:
    """
    RandomChess is a class for creating random first rank according to a certain random mode which
    specifies the rules with which the randomly shuffled peices should be situated
    """
    
    import random
    
    def __init__(self):
        # firstRank=['rookKingSide','knightKingSide','bishopKingSide','king','queen','bishopQueenSide','knightQueenSide','rookQueenSide']
        # firstRank=[u'\u2656'.encode('utf-8'),u'\u2658'.encode('utf-8'),u'\u2657'.encode('utf-8'),u'\u2654'.encode('utf-8'),
#            u'\u2655'.encode('utf-8'),u'\u2657'.encode('utf-8'),u'\u2658'.encode('utf-8'),u'\u2656'.encode('utf-8')]
        self._firstRank=['♖','♘','♗','♔','♕','♗','♘','♖']
        self._ShuffledFirstRank={'firstRank':['♖','♘','♗','♔','♕','♗','♘','♖'],
                                'state':{'KingPos':3,'RookPos':[0,7],'BishopPos':[2,5]}}
    @property    
    def ShuffledFirstRank(self):  
        print('getting ShuffledFirstRank...')
        return self._ShuffledFirstRank
    
    def ShuffleFirstRank(self,RandomMode=None):
            l=self._ShuffledFirstRank['firstRank']
            n=len(l)
            RookfirstPos=-1
            RooksecPos=-1
            kingPos=-1
            bishopFirstPos=-1
            bishopSecPos=-1

            for i in range(n):

                indRandom=random.randint(i,n-1)
                l[indRandom],l[i]=l[i],l[indRandom]

                p=l[i]
                
                if p==self._firstRank[0] and RookfirstPos>=0:
                    RooksecPos=i
                elif p==self._firstRank[0]:
                    RookfirstPos=i
                elif p==self._firstRank[2] and bishopFirstPos>=0:
                    bishopSecPos=i
                elif p==self._firstRank[2]:
                    bishopFirstPos=i
                elif p==self._firstRank[3]:
                    kingPos=i
            
            self._ShuffledFirstRank['state']['KingPos']=kingPos
            self._ShuffledFirstRank['state']['RookPos']=[RookfirstPos,RooksecPos]
            self._ShuffledFirstRank['state']['BishopPos']=[bishopFirstPos,bishopSecPos]
            
            if RandomMode is not None:
                if RandomMode=='Fischer':
                    if not ((bishopFirstPos+bishopSecPos)% 2==1 and kingPos>RookfirstPos and kingPos<RooksecPos):
                        
                        self._ShuffledFirstRank={'firstRank':['♖','♘','♗','♔','♕','♗','♘','♖'],
                                'state':{'KingPos':3,'RookPos':[0,7],'BishopPos':[2,5]}}
                    else:    
                        return False
            return True
                
    def printFirstRank(self):
        print(repr(self._ShuffledFirstRank['firstRank']).decode('string-escape'))