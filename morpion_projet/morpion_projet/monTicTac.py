# -*- coding: utf-8 -*-
"""
Created on Fri May 14 07:35:26 2021

@author: armand
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:07:02 2021

@author: armand
"""

from copy import deepcopy
import time
import copy
import math

"""
    Initialization of the global variables
"""
size = 4
sizeInit = 8
min_util = -999999999999999
max_util = +999999999999999
x_player = 'X'
o_player = 'O'
empty = ' '
moves = 0
timeStop = 8
cutOffOccured = False
inf = 1000
neg_inf = -1000
computer_player = x_player
human_player = o_player
gameLast = None
noued = 0
endGame = False

"""
    Changes the player after a move
"""

def other_player(player):
    if player == x_player:
        return o_player
    else:
        return x_player


"""
    Class state maintains the game parameters
"""


class State:
    def __init__(self, nextPlayer, other=None, matrice=""):
        self.nextPlayer = nextPlayer
        self.table = {}
        self.utility = 0
        self.value = 0
        self.children = {}

        i = 0
        if matrice != "":
            for y in range(sizeInit):
                for x in range(sizeInit):
                    self.table[x, y] = matrice[x][y]
        else:
            for y in range(sizeInit):
                for x in range(sizeInit):
                    self.table[x, y] = empty
                
        # copy constructor
        if other:
            self.__dict__ = deepcopy(other.__dict__)
            

    def is_full(self):
        for i in range(0, size):
            for j in range(0, size):
                if self.table[i, j] == empty:
                    return False

        return True

"""
    Action function gives the next possible legal moves
"""

def ACTIONS(state):
    children = []
    for i in range(0, size):
        for j in range(0, size):
            if state.table[i, j] == empty:
                childTable = deepcopy(state.table)
                childTable[i, j] = state.nextPlayer
                childState = State(nextPlayer=state.nextPlayer)
                childState.nextPlayer = other_player(state.nextPlayer)
                childState.table = childTable
                childState.value = state.value
                childState.depth = state.depth + 1
                children.append(childState)

    return children


""""
    Terminal function to check if the terminal state has been reached
"""

def TERMINAL_TEST(state):
    if state.is_full():
        return True

    player = other_player(player=state.nextPlayer)
    if state.table[0, 0] == state.table[0, 1] \
            and state.table[0, 1] == state.table[0, 2] \
            and state.table[0, 2] == state.table[0, 3] \
            and state.table[0, 0] != empty:
        return True
    if state.table[1, 0] == state.table[1, 1] \
            and state.table[1, 1] == state.table[1, 2] \
            and state.table[1, 2] == state.table[1, 3] \
            and state.table[1, 0] != empty:
        return True
    if state.table[2, 0] == state.table[2, 1] \
            and state.table[2, 1] == state.table[2, 2] \
            and state.table[2, 2] == state.table[2, 3] \
            and state.table[2, 0] != empty:
        return True
    if state.table[3, 0] == state.table[3, 1] \
            and state.table[3, 1] == state.table[3, 2] \
            and state.table[3, 2] == state.table[3, 3] \
            and state.table[3, 0] != empty:
        return True
    if state.table[0, 0] == state.table[1, 0] \
            and state.table[1, 0] == state.table[2, 0] \
            and state.table[2, 0] == state.table[3, 0] \
            and state.table[0, 0] != empty:
        return True
    if state.table[0, 1] == state.table[1, 1] \
            and state.table[1, 1] == state.table[2, 1] \
            and state.table[2, 1] == state.table[3, 1] \
            and state.table[0, 1] != empty:
        return True
    if state.table[0, 2] == state.table[1, 2] \
            and state.table[1, 2] == state.table[2, 2] \
            and state.table[2, 2] == state.table[3, 2] \
            and state.table[0, 2] != empty:
        return True
    if state.table[0, 3] == state.table[1, 3] \
            and state.table[1, 3] == state.table[2, 3] \
            and state.table[2, 3] == state.table[3, 3] \
            and state.table[0, 3] != empty:
        return True
    if state.table[0, 0] == state.table[1, 1] \
            and state.table[1, 1] == state.table[2, 2] \
            and state.table[2, 2] == state.table[3, 3] \
            and state.table[0, 0] != empty:
        return True
    if state.table[0, 3] == state.table[1, 2] \
            and state.table[1, 2] == state.table[2, 1] \
            and state.table[2, 1] == state.table[3, 0] \
            and state.table[0, 3] != empty:
        return True

    return False


"""
    Utility function to calculate the utility of a state
"""

def UTILITYSimple(state):
    
    if state[0][0] == state[0][1] \
            and state[0][1] == state[0][2] \
            and state[0][2] == state[0][3] \
            and state[0][0] != empty:
        return PLAYER_UTIL(state[0][0])
    if state[1][0] == state[1][1] \
            and state[1][1] == state[1][2] \
            and state[1][2] == state[1][3] \
            and state[1][0] != empty:
        return PLAYER_UTIL(state[1][0])
    if state[2][0] == state[2][1] \
            and state[2][1] == state[2][2] \
            and state[2][2] == state[2][3] \
            and state[2][0] != empty:
        return PLAYER_UTIL(state[2][0])
    if state[3][0] == state[3][1] \
            and state[3][1] == state[3][2] \
            and state[3][2] == state[3][3] \
            and state[3][0] != empty:
        return PLAYER_UTIL(state[3][0])
    if state[0][0] == state[1][0] \
            and state[1][0] == state[2][0] \
            and state[2][0] == state[3][0] \
            and state[0][0] != empty:
        return PLAYER_UTIL(state[0][0])
    if state[0][1] == state[1][1] \
            and state[1][1] == state[2][1] \
            and state[2][1] == state[3][1] \
            and state[0][1] != empty:
        return PLAYER_UTIL(state[0][1])
    if state[0][2] == state[1][2] \
            and state[1][2] == state[2][2] \
            and state[2][2] == state[3][2] \
            and state[0][2] != empty:
        return PLAYER_UTIL(state[0][2])
    if state[0][3] == state[1][3] \
            and state[1][3] == state[2][3] \
            and state[2][3] == state[3][3] \
            and state[0][3] != empty:
        return PLAYER_UTIL(state[0][3])
    if state[0][0] == state[1][1] \
            and state[1][1] == state[2][2] \
            and state[2][2] == state[3][3] \
            and state[0][0] != empty:
        return PLAYER_UTIL(state[0][0])
    if state[0][3] == state[1][2] \
            and state[1][2] == state[2][1] \
            and state[2][1] == state[3][0] \
            and state[0][3] != empty:
        return PLAYER_UTIL(state[0][3])

    return 0


def PLAYER_UTIL(player):
    if player == computer_player:
        return max_util
    elif player == human_player:
        return min_util
    return 0


def BestMove(v,state):
#retval contient l'ensemble des bonnes positions pour la machine
    retVal = sorted(list(filter(lambda x: x.value == v, state.children)), key = lambda g: HEURISTICchoixMatrice(convertStateFromMatrice(g), 1))
    reheuristique = [ HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) for g in retVal]
    print(reheuristique, "-->")

    # si la machine va gagner
    if 999999999999999 in reheuristique:
        return [ g for g in retVal if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 999999999999999][0]

    # si l'humain a aligné 3  points 
    print(v,"<-----------------")
    if -1001 in reheuristique or -1002 in reheuristique:
        positionPossibleBonne = [ g for g in retVal if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) != -1001 and HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) != -1002]
        #je regarde si je peux aligner 3 points
        l = [ g for g in positionPossibleBonne if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 1001 or HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 0 or HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) != -1000]

        if len(l)!=0:
            l = sorted(l, key=lambda x : HEURISTICchoixMatrice(convertStateFromMatrice(x), 1) )
            return l[0]
        else:
            #je regarde si je peux aligner 2 points
            l = [ g for g in positionPossibleBonne if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 1000]
            if len(l)!=0:
                return l[0]
            else:
                #alors je bloque son jeu
                if len(positionPossibleBonne)!=0:
                    for g in positionPossibleBonne:
                        point=getNewPoint(convertStateFromMatrice(state), convertStateFromMatrice(g))
                        if point!=None:
                            #trouver le point à proximité
                            if point[1]-1>=0 and g.table[point[0],point[1]-1]!=empty or point[1]+1<4 and g.table[point[0],point[1]+1]!=empty or point[0]+1<4 and g.table[point[0]+1,point[1]]!=empty or point[0]-1>=0 and g.table[point[0]-1,point[1]]!=empty or (point[0]-1>=0 and point[1]-1>=0) and g.table[point[0]-1,point[1]-1]!=empty or (point[0]-1>=0 and point[1]+1<4) and g.table[point[0]-1,point[1]+1]!=empty or (point[0]+1<4 and point[1]-1>=0) and g.table[point[0]+1,point[1]-1]!=empty or (point[0]+1<4 and point[1]+1<4) and g.table[point[0]+1,point[1]+1]!=empty:#check bas droit
                                return g
                else:
                    for g in retVal:
                        point=getNewPoint(convertStateFromMatrice(state), convertStateFromMatrice(g))
                        if point!=None:
                            #trouver le point à proximité
                            if point[1]-1>=0 and g.table[point[0],point[1]-1]!=empty or point[1]+1<4 and g.table[point[0],point[1]+1]!=empty or point[0]+1<4 and g.table[point[0]+1,point[1]]!=empty or point[0]-1>=0 and g.table[point[0]-1,point[1]]!=empty or (point[0]-1>=0 and point[1]-1>=0) and g.table[point[0]-1,point[1]-1]!=empty or (point[0]-1>=0 and point[1]+1<4) and g.table[point[0]-1,point[1]+1]!=empty or (point[0]+1<4 and point[1]-1>=0) and g.table[point[0]+1,point[1]-1]!=empty or (point[0]+1<4 and point[1]+1<4) and g.table[point[0]+1,point[1]+1]!=empty:#check bas droit
                                return g

    # si la machine peux aligner 3 points

    if 1001 in reheuristique or 1002 in reheuristique:
        l = [ g for g in retVal if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 1002]
        if len(l)!=0:
            return l[0]
        else:
            return [ g for g in retVal if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 1001][0]

    # si l'humain a aligné 2  points 
    if -1000 in reheuristique or -1000.5 in reheuristique:
        positionPossibleBonne = [ g for g in retVal if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) != -1000 and HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) != -1000.5]
        if len(positionPossibleBonne)!=0:
            #je regarde si je peux aligner 3 points
            l = [ g for g in positionPossibleBonne if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 1001]
            if len(l)!=0:
                return l[0]
            else:
                    #alors je bloque son jeu
                    for g in positionPossibleBonne:
                        point=getNewPoint(convertStateFromMatrice(state), convertStateFromMatrice(g))
                        if point!=None:
                            #trouver le point à proximité
                            if point[1]-1>=0 and g.table[point[0],point[1]-1]!=empty or point[1]+1<4 and g.table[point[0],point[1]+1]!=empty or point[0]+1<4 and g.table[point[0]+1,point[1]]!=empty or point[0]-1>=0 and g.table[point[0]-1,point[1]]!=empty or (point[0]-1>=0 and point[1]-1>=0) and g.table[point[0]-1,point[1]-1]!=empty or (point[0]-1>=0 and point[1]+1<4) and g.table[point[0]-1,point[1]+1]!=empty or (point[0]+1<4 and point[1]-1>=0) and g.table[point[0]+1,point[1]-1]!=empty or (point[0]+1<4 and point[1]+1<4) and g.table[point[0]+1,point[1]+1]!=empty:#check bas droit
                                return g


        else:
            for g in retVal:
                point=getNewPoint(convertStateFromMatrice(state), convertStateFromMatrice(g))
                if point!=None:
                    #trouver le point à proximité
                    if point[1]-1>=0 and g.table[point[0],point[1]-1]!=empty or point[1]+1<4 and g.table[point[0],point[1]+1]!=empty or point[0]+1<4 and g.table[point[0]+1,point[1]]!=empty or point[0]-1>=0 and g.table[point[0]-1,point[1]]!=empty or (point[0]-1>=0 and point[1]-1>=0) and g.table[point[0]-1,point[1]-1]!=empty or (point[0]-1>=0 and point[1]+1<4) and g.table[point[0]-1,point[1]+1]!=empty or (point[0]+1<4 and point[1]-1>=0) and g.table[point[0]+1,point[1]-1]!=empty or (point[0]+1<4 and point[1]+1<4) and g.table[point[0]+1,point[1]+1]!=empty:#check bas droit
                        return g

    # si la machine peux aligner 2 points
    if 1000 in reheuristique or 1000.5 in reheuristique:
        positionPossibleBonne = [ g for g in retVal if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 1000 or HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 1000.5]
        if len(positionPossibleBonne)!=0:
            l = [ g for g in retVal if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 1000.5 ]
            if len(l)!=0:
                return l[0]
            else:
                return positionPossibleBonne[-1]
        else:
            #je recherche la position du point machine
            pos = (0,0)
            choix = 0
            for key, value in state.table.items():
                if value == x_player:
                    pos = key 
                    break
            
            #je recherche la matrice la plus proche de mon
            distance = 1000
            for g in retVal:
                postmp = (0,0)
                for key, value in g.table.items():
                    if value == x_player:
                        postmp = key 
                        break  
                
                rc = (pos[0]-postmp[0])**2 + (pos[1]-postmp[1])**2
                do = math.sqrt(rc)
                if do < distance:
                    do = distance
                    choix = g

            if choix!=0:
                return g 
            else:
                l =sorted( [ g for g in retVal], key = lambda x :  HEURISTICchoixMatrice(convertStateFromMatrice(x), 1))
                return l[math.floor(len(l)/2)]

    # si il y a pas de cas, la machine cherche une position qui se rapproche plus d'une point hummain tiré au hazard
    #liste position humain
    reponse = retVal[0]
    humain = [key for key,val in state.table.items() if val == o_player]

    if len(humain)!=0:
        choix = humain[0]

        #la machine doit choisir une position de tel sorte à avoir une distance minimal avec mon choix
        print("oui", len(humain))
        if len(humain) == 1:
            distance = 1000
            for g in retVal:
                # trouver la position machine
                p = (0,0)
                for key,val in g.table.items():
                    if val == x_player:
                        p = key
                        break
                distanceTmp = math.sqrt((p[0]-choix[0])**2 + (p[1]-choix[1])**2)
                if distanceTmp < distance:
                    distance = distanceTmp
                    reponse = g   
        else:
            #je regarde si je peux aligner 2 points
            l = [ g for g in state.children if HEURISTICchoixMatrice(convertStateFromMatrice(g), 1) == 1000]
            if len(l)!=0:
                return l[0]


    return reponse

"""
    ALPHA BETA SEARCH ALGORITHM
"""

def ALPHA_BETA_SEARCH(state, start):
    global noued
    noued = 0
    x=0
    o =0 
    for k,v in state.table.items():
        if v == x_player:
            x+=1
        if v == o_player:
            o+=1
    if x>o:
        v = MAX_VALUE(state=state, alpha=min_util, beta=max_util, start=start)
    else:
        v = MIN_VALUE(state=state, alpha=min_util, beta=max_util, start=start)
    
    if len(state.children) == 0:
        print("match null")
        global endGame
        endGame = True
        return state

    return BestMove(v,state)
    


def MAX_VALUE(state, alpha, beta, start):
    global cutOffOccured
    global noued
    noued+=1
    if TERMINAL_TEST(state=state):
        return UTILITYSimple(state=convertStateFromMatrice(state))

    if noued >= 100:
        cutOffOccured = True
        return HEURISTICchoixMatrice(convertStateFromMatrice(state), 1)


    
    v = neg_inf
    new_alpha = alpha
    state.children = ACTIONS(state)
    for a in state.children:        
            v = max(v, MIN_VALUE(state=a, alpha=new_alpha, beta=beta, start=start))
            a.value = v
            if v >= beta:
                return v
            new_alpha = max(new_alpha, v)
    return v


def MIN_VALUE(state, alpha, beta, start):
    global cutOffOccured
    global noued
    noued+=1
    if TERMINAL_TEST(state=state):
        return UTILITYSimple(state=convertStateFromMatrice(state))

    if noued >= 100:
        cutOffOccured = True
        return HEURISTICchoixMatrice(convertStateFromMatrice(state), -1)


    
    v = inf
    new_beta = beta
    state.children = ACTIONS(state)
    for a in state.children:
            v = min(v, MAX_VALUE(state=a, alpha=alpha, beta=new_beta, start=start))
            a.value = v
            if v <= alpha:
                return v
            new_beta = min(new_beta, v)
    return v

def convertStateFromMatrice(state):
    inits = [["_","_","_","_"], ["_","_","_","_"], ["_","_","_","_"], ["_","_","_","_"]]
    for ligne in range(4):
        for colonne in range(4):
            inits[ligne][colonne] = state.table[(ligne, colonne)]

    return inits

def getNewPoint(base, state):
    pos = None
    for i in range(4):
        for j in range(4):
            if base[i][j] != state[i][j]:
                return (i,j)


def HEURISTICchoixMatrice(state, player = 1):
    x3 = 0
    x2 = 0
    x1 = 0
    o3 = 0
    o2 = 0
    o1 = 0

    #code pour verifier que 3 éléments se suivent, avec un vide 
    # parcours ligne horizontale
    for l in state:
        if (all(map(lambda x: x==o_player or x==" ",l))):
            if len([xc for xc in l if xc==o_player ]) == 4:
                return -999999999999999*player
            if len([xc for xc in l if xc==o_player ]) == 3:
                ro = list(map(lambda x: x,l))
                if ro[0] == empty or ro[3] == empty:
                    return -1002*player
                return -1001*player
        if (all(map(lambda x: x==x_player or x==" ",l))):
            ro = list(map(lambda x: x,l))
            if len([xc for xc in l if xc==x_player ]) == 3:
                if ro[0] == empty or ro[3] == empty:
                    return 1002*player
                return 1001*player
            if len([xc for xc in l if xc==x_player ]) == 4:
                return 999999999999999*player


    # parcours ligne vertical
    for i in range(len(state[0])):
        l = []
        for j in range(len(state[0])):
            l.append(state[j][i])            
        
        if (all(map(lambda x: x==o_player or x==" ",l))):
            if len([xc for xc in l if xc==o_player ]) == 4:
                return -999999999999999*player
            if len([xc for xc in l if xc==o_player ]) == 3:
                ro = list(map(lambda x: x,l))
                if ro[0] == empty or ro[3] == empty:
                    return -1002*player
                return -1001*player
        if (all(map(lambda x: x==x_player or x==" ",l))):
            if len([xc for xc in l if xc==x_player ]) == 3:
                ro = list(map(lambda x: x,l))
                if ro[0] == empty or ro[3] == empty:
                    return 1002*player
                return 1001*player
            if len([xc for xc in l if xc==x_player ]) == 4:
                return 999999999999999*player
            
            
    # parcours diagonale gauche droit                           
    diagonalGaucheDroitO = all(map(lambda x: x==o_player or x==" ",[state[i][i] for i in range(len(state[0]))]))
    diagonalGaucheDroitX = all(map(lambda x: x==x_player or x==" ",[state[i][i] for i in range(len(state[0]))]))
    
    if diagonalGaucheDroitO:
        if len([state[i][i] for i in range(len(state[0])) if state[i][i]==o_player ]) == 4:
            return -999999999999999*player
        if len([state[i][i] for i in range(len(state[0])) if state[i][i]==o_player ]) == 3:
            ro = list(map(lambda x: x,[state[i][i] for i in range(len(state[0]))]))
            if ro[0] == empty or ro[3] == empty:
                return -1002*player
            return -1001*player
    if diagonalGaucheDroitX:
        if len([state[i][i] for i in range(len(state[0])) if state[i][i]==x_player ]) == 3:
            ro = list(map(lambda x: x,[state[i][i] for i in range(len(state[0]))]))
            if ro[0] == empty or ro[3] == empty:
                return 1002*player
            return 1001*player
        if len([state[i][i] for i in range(len(state[0])) if state[i][i]==x_player ]) == 4:
            return 999999999999999*player
        
    # parcours diagonale droit gauche
    diagonalDroitGaucheO = all(map(lambda x: x==o_player or x==" ",[state[j][i] for j,i in enumerate(range(len(state[0])-1, -1, -1))]))
    diagonalDroitGaucheX = all(map(lambda x: x==x_player or x==" ",[state[j][i] for j,i in enumerate(range(len(state[0])-1, -1, -1))]))
    
    if diagonalDroitGaucheO:
        if len([state[j][i] for j,i in enumerate(range(len(state[0])-1, -1, -1)) if state[j][i]==o_player ]) == 4:
            return -999999999999999*player
        if len([state[j][i] for j,i in enumerate(range(len(state[0])-1, -1, -1)) if state[j][i]==o_player ]) == 3:
            ro = list(map(lambda x: x,[state[j][i] for j,i in enumerate(range(len(state[0])-1, -1, -1))]))
            if ro[0] == empty or ro[3] == empty:
                return -1002*player
            return -1001*player
    if diagonalDroitGaucheX:
        if len([state[j][i] for j,i in enumerate(range(len(state[0])-1, -1, -1)) if state[j][i]==x_player ]) == 3:
            ro = list(map(lambda x: x,[state[j][i] for j,i in enumerate(range(len(state[0])-1, -1, -1))]))
            print(*ro,"----")
            if ro[0] == empty or ro[3] == empty:
                return 1002*player
            return 1001*player
        if len([state[j][i] for j,i in enumerate(range(len(state[0])-1, -1, -1)) if state[j][i]==x_player ]) == 4:
            return 999999999999999*player
            
            
    # check row wise
    jaiTrouverEspaceVideX = False
    jaiTrouverEspaceVideO = False
    PointLierX = False
    PointLierO = False
    for r in range(0, 4):
        os = 0
        xs = 0
        space = 0
        jaiTrouverEspace = 0
        nbrPointLierX = 0
        nbrPointLierO = 0
        for c in range(0, 4):
            if state[r][c] == x_player:
                xs += 1
                nbrPointLierX+=1
            if state[r][c] == o_player:
                os += 1
                nbrPointLierO+=1
            if ((state[r][c] == " " and (c+1<4 and state[r][c+1] == " " ) and c!=0) and (c+2<4 and state[r][c+2] != " ")):
                jaiTrouverEspace=1
            if state[r][c] == " ":
                if nbrPointLierX<2:
                    nbrPointLierX=0
                if nbrPointLierO<2:
                    nbrPointLierO=0
                    
                    
        if (xs == 2 and os == 0) and nbrPointLierX==2:
            PointLierX = True
        if (os == 2 and xs == 0) and nbrPointLierO==2:
            PointLierO = True
            
        if (xs == 2 and os == 0) and jaiTrouverEspace==0:
            jaiTrouverEspaceVideX = True
        if (os == 2 and xs == 0) and  jaiTrouverEspace==0:
            jaiTrouverEspaceVideO = True

        if xs == 0:
            if os == 1:
                o1 += 1
            elif os == 2:
                o2 += 1
            elif os == 3:
                o3 += 1

        if os == 0:
            if xs == 1:
                x1 += 1
            elif xs == 2:
                x2 += 1
            elif xs == 3:
                x3 += 1

    # check column wise
    for c in range(0, 4):
        os = 0
        xs = 0
        space = 0
        jaiTrouverEspace = 0
        nbrPointLierX = 0
        nbrPointLierO = 0
        for r in range(0, 4):
            if state[r][c] == x_player:
                xs += 1
                nbrPointLierX+=1
            if state[r][c] == o_player:
                os += 1
                nbrPointLierO+=1
            if ((state[r][c] == " " and (r+1<4 and state[r+1][c] == " " ) and r!=0) and (r+2<4 and state[r+2][c] != " ")):
                jaiTrouverEspace=1
            if state[r][c] == " ":
                if nbrPointLierX<2:
                    nbrPointLierX=0
                if nbrPointLierO<2:
                    nbrPointLierO=0
                    
                    
        if (xs == 2 and os == 0) and nbrPointLierX==2:
            PointLierX = True
        if (os == 2 and xs == 0) and nbrPointLierO==2:
            PointLierO = True
            
        if (xs == 2 and os == 0) and jaiTrouverEspace==0:
            jaiTrouverEspaceVideX = True
        if (os == 2 and xs == 0) and  jaiTrouverEspace==0:
            jaiTrouverEspaceVideO = True

        if xs == 0:
            if os == 1:
                o1 += 1
            elif os == 2:
                o2 += 1
            elif os == 3:
                o3 += 1

        if os == 0:
            if xs == 1:
                x1 += 1
            elif xs == 2:
                x2 += 1
            elif xs == 3:
                x3 += 1

    # check main diagonal
    os = 0
    xs = 0
    space = 0
    jaiTrouverEspace = 0
    nbrPointLierX = 0
    nbrPointLierO = 0
    for i in range(0, 4):
        if state[i][i] == x_player:
            xs += 1
            nbrPointLierX+=1
        if state[i][i] == o_player:
            os += 1
            nbrPointLierO+=1
        if ((state[i][i] == " " and (i+1<4 and state[i+1][i+1] == " " ) and i!=0) and (i+2<4 and state[i+2][i+2] != " ")):
            jaiTrouverEspace=1
        if state[i][i] == " ":
            if nbrPointLierX<2:
                nbrPointLierX=0
            if nbrPointLierO<2:
                nbrPointLierO=0
                
                
    if (xs == 2 and os == 0) and nbrPointLierX==2:
        PointLierX = True
    if (os == 2 and xs == 0) and nbrPointLierO==2:
        PointLierO = True

    if (xs == 2 and os == 0) and jaiTrouverEspace==0:
        jaiTrouverEspaceVideX = True
    if (os == 2 and xs == 0) and  jaiTrouverEspace==0:
        jaiTrouverEspaceVideO = True

    if xs == 0:
        if os == 1:
            o1 += 1
        elif os == 2:
            o2 += 1
        elif os == 3:
            o3 += 1

    if os == 0:
        if xs == 1:
            x1 += 1
        elif xs == 2:
            x2 += 1
        elif xs == 3:
            x3 += 1

            # check secondaire diagonal
    os = 0
    xs = 0
    space = 0
    jaiTrouverEspace = 0
    nbrPointLierX = 0
    nbrPointLierO = 0
    for i in range(0, 4):
        if state[4 - i - 1][i] == x_player:
            xs += 1
            nbrPointLierX+=1
        if state[4 - i - 1][i] ==o_player:
            os += 1
            nbrPointLierO+=1
        if ((state[4 - i - 1][i] == " " and ((4 - i - 2>=0 and i+1<4) and state[4 - i - 2][i+1] == " " ) and 4 - i - 1!=3) and ((4 - i - 3>=0 and i+2<4) and state[4 - i - 3][i+2] != " ")):
            jaiTrouverEspace=1
        if state[4 - i - 1][i] == " ":
            if nbrPointLierX<2:
                nbrPointLierX=0
            if nbrPointLierO<2:
                nbrPointLierO=0
                
                
    if (xs == 2 and os == 0) and nbrPointLierX==2:
        PointLierX = True
    if (os == 2 and xs == 0) and nbrPointLierO==2:
        PointLierO = True
        
    if (xs == 2 and os == 0) and jaiTrouverEspace==0:
        jaiTrouverEspaceVideX = True
    if (os == 2 and xs == 0) and  jaiTrouverEspace==0:
        jaiTrouverEspaceVideO = True

    if xs == 0:
        if os == 1:
            o1 += 1
        elif os == 2:
            o2 += 1
        elif os == 3:
            o3 += 1

    if os == 0:
        if xs == 1:
            x1 += 1
        elif xs == 2:
            x2 += 1
        elif xs == 3:
            x3 += 1
    

    if player!=0:
        if PointLierX == True and PointLierO == False:
            return 1000.5
        if PointLierO == True and PointLierX == False:
            return -1000.5
        if PointLierO == True and PointLierX == True:
            return -1000.5
        
        if jaiTrouverEspaceVideX == True and jaiTrouverEspaceVideO==False:
            return 1000
        if jaiTrouverEspaceVideO == True and jaiTrouverEspaceVideX == False:
            return -1000
        if jaiTrouverEspaceVideO == True and jaiTrouverEspaceVideX == True:
            return -1000

    t = (6 * x3 + 3 * x2 + x1) - (6 * o3 + 3 * o2 + o1)
    
    
    return t



def TERMINAL_GAME(state):
    for i in range(sizeInit):
        for j in range(sizeInit):
            if state.table[i,j] == " ":
                return False
            
    return True
        
start = time.time()

first = "h"

"""
    Code for the GUI of the game using Tkinter library
"""


class GUI:
    def __init__(self, matrice):
        self.game = State(nextPlayer=human_player, matrice=matrice)

        if first == "c":
            self.game.nextPlayer = computer_player
            self.game.table[(sizeInit-1)//2,(sizeInit-1)//2] = x_player


    def move(self, x, y):
        self.game.table[x, y] = human_player
        self.game.nextPlayer = computer_player

        self.computer_move()
        if TERMINAL_GAME(self.game):
            if UTILITYSimple(convertStateFromMatrice(self.game)) == 0:
                print("match null")
            return

    def getBestMatrice4(self,listM,nbrX):

        m = None
        reheuristique = [ g[0] for g in listM]
        find = False

        # si l'humain a aligné 3 et l'ordinateur non
        if (1001 not in reheuristique and 1002 not in reheuristique ) and (-1001 in reheuristique or -1002 in reheuristique):
            m=[ g[1] for g in listM if g[0] == -1001]
            if len(m)==0:
                m=[ g[1] for g in listM if g[0] == -1002][0]
            else:
                m=m[0]
            find = True
        # si les deux on aligné 3 point
        elif (1001 in reheuristique or 1002 in reheuristique ) and (-1001 in reheuristique or -1002 in reheuristique):
            m=[ g[1] for g in listM if g[0] == 1001]
            if len(m)==0:
                m=[ g[1] for g in listM if g[0] == 1002][0]
            else:
                m=m[0]
            find = True
            #si non
        elif (1001 in reheuristique or 1002 in reheuristique ) and (-1001 not in reheuristique and -1002 not in reheuristique):
            m=[ g[1] for g in listM if g[0] == 1001]
            if len(m) == 0:
                m=[ g[1] for g in listM if g[0] == 1002][0]
            else:
                m=m[0]
            find = True
        elif 1000 in reheuristique or 1000.5 in reheuristique:
            m=[ g[1] for g in listM if g[0] == 1000]
            if len(m) == 0:
                m=[ g[1] for g in listM if g[0] == 1000.5][0]
            else:
                m = m[0]
            find = True
        elif -1000 in reheuristique or -1000.5 in reheuristique:
            m = [ g[1] for g in listM if g[0] == -1000]
            if len(m) == 0:
                m=[ g[1] for g in listM if g[0] == -1000.5][0]
            else:
                m = m[0]
            find = True
        else:
            print("c'est entrer ici", nbrX)
            if nbrX==0:
                m=min(listM, key= lambda b: b[0])[1]
            else:
                m=max(listM, key= lambda b: b[0])[1]

        return m

    def computer_move(self):
        global endGame
        self.game.depth = 0
        """ quel matrice d'ordre 4 choisir pour faire l'ahpha beta"""
        listM = []
        inits = [["_","_","_","_"], ["_","_","_","_"], ["_","_","_","_"], ["_","_","_","_"]]
        nbrX = 0
        nbrO = 0
        for i in range(sizeInit-size+1):
            for j in range(sizeInit-size+1):
                #construcction de la matrice
                mapGame = deepcopy(inits)
                
                for ligne in range(len(mapGame)):
                    for colonne in range(len(mapGame)):
                        if self.game.table[ligne+i, colonne+j] == x_player:
                            nbrX+=1
                            
                        mapGame[ligne][colonne] = [self.game.table[ligne+i, colonne+j], (ligne+i, colonne+j)]
                mapGamevalue = deepcopy(inits)
                
                for ligne in range(len(mapGame)):
                    for colonne in range(len(mapGame)):
                        mapGamevalue[ligne][colonne] = mapGame[ligne][colonne][0]
                h = HEURISTICchoixMatrice(mapGamevalue)
                if h == -999999999999999:
                    endGame=True
                    print("humman win")
                    return 
                if h!=0:
                    listM.append((h,mapGame))
        

        """
            selection de la meilleur matrice
        """
        m = self.getBestMatrice4(listM,nbrX)


        print("-------------")
        print(m)
        print("-------------")
        monNouveauState = {j[1]:j[0] for i in m for j in i }
        monNouveauStateDanslodreIndex={}

        for i in range(len(m)):
            for j in range(len(m)):
                monNouveauStateDanslodreIndex[ i,j ] = m[i][j][0]
        
        cop = copy.deepcopy(self.game)
        cop.table=monNouveauStateDanslodreIndex
        
        cop = ALPHA_BETA_SEARCH(cop, time.time())
        listeValeur = list(cop.table.values())
        

        lo = 0
        for item in monNouveauState.keys():
            monNouveauState[item] = listeValeur[lo]
            lo+=1
      
        for item in monNouveauState.keys():
            self.game.table[item] = monNouveauState[item]
        
        u = UTILITYSimple(convertStateFromMatrice(cop))
        if u == -999999999999999:
            endGame=True
            print("humman win")
        elif u == 999999999999999:
            endGame=True
            print("machine win")
        #print(self.game.table)

"""
    Code for a dialog box to select who goes first: human or the computer
"""


class Select:
    def __init__(self):
        print("welcome")

    def choose(self, option, matrice):
        global first
        first = option
        return GUI(matrice)

    def mainloop(self, matrice, numeSaisie):
        dic = { }
                
        ind = 1
        for i in range(sizeInit) :
            for j in range(sizeInit):
                dic[ind] = (i,j)
                ind+=1

        gameLast.move(dic[numeSaisie][0], dic[numeSaisie][1])
        
        nouvelleMat = []
        noeudx = 0
        ligne = []

        for i in range(len(matrice[0])):
            nouvelleMat.append([0 for i in range(len(matrice[0]))])

        for key,val in gameLast.game.table.items():
            nouvelleMat[key[0]][key[1]] = val

        for i in range(len(matrice[0])):
            for j in range(len(matrice[0])):
                if matrice[i][j] != nouvelleMat[i][j]:
                    return (i,j)

        return (-1,-1)
"""
    main function starts from here
"""
def fin(matrice, reponse, numeroUser ):
    global sizeInit
    global gameLast
    sizeInit = len(matrice[0])
    window = Select()
    if reponse == False:
        gameLast=window.choose("c",matrice)

        return ((sizeInit-1)//2,(sizeInit-1)//2)
    else:
        gameLast = window.choose("h",matrice)
        
    return window.mainloop(matrice, int(numeroUser))

def bonjour():
    return "oui"
