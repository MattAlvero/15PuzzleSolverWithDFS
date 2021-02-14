# Assignment 43 for CS 411
# Author: Matthew Alvero
# NetID: malver2
# UIN: 663738906
# Created on 02/12/21

"""
Any imports
"""
from queue import LifoQueue

"""
Puzzle node to make nodes for the tree
"""
class node:

    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.children = []
        self.cost = 1
    
    def add_children(self):
        self.children.append((self.state.getLeftState()), self, 'L')
        self.children.append((self.state.getRightState()), self, 'R')
        self.children.append((self.state.getUpState()), self, 'U')
        self.children.append((self.state.getDownState()), self, 'D')

    def getState(self):
        return self.state


class state:

    def __init__(self, board):
        self.grid = board
        self.emptySpaceIdx = 0
        for i in range(len(self.grid)):
            if self.grid[i] == 0:
                self.emptySpaceIdx = i
                break
        
    def getLeftState(self):
        # check if we can even move left
        if self.emptySpaceIdx == 0 or self.emptySpaceIdx % 4 == 0:
            pass
        # otherwise, get the left state
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.grid
            # perform the left move by swaping values in the array
            temp = newState[self.emptySpaceIdx-1]
            newState[self.emptySpaceIdx - 1] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            leftState = state(newState)
            return leftState

    def getRightState(self):
        # check if we can even move left
        if self.emptySpaceIdx % 3 == 0:
            pass
        # otherwise, get the left state
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.grid
            # perform the left move by swaping values in the array
            temp = newState[self.emptySpaceIdx+1]
            newState[self.emptySpaceIdx + 1] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            rightState = state(newState)
            return rightState

    def getUpState(self):
        # check if we can even move left
        if self.emptySpaceIdx in range (0,5):
            pass
        # otherwise, get the left state
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.grid
            # perform the left move by swaping values in the array
            temp = newState[self.emptySpaceIdx - 4]
            newState[self.emptySpaceIdx - 4] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            upState = state(newState)
            return upState
    
    def getDownState(self):
        # check if we can even move left
        if self.emptySpaceIdx in range (12,16):
            pass
        # otherwise, get the left state
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.grid
            # perform the left move by swaping values in the array
            temp = newState[self.emptySpaceIdx + 4]
            newState[self.emptySpaceIdx + 4] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            downState = state(newState)
            return downState
    
    def getGrid(self):
        return self.grid

def dfs(root,endState):
    frontier = LifoQueue()
    frontier.put_nowait(root)
    explored = set()
    while not frontier.empty():
        state = frontier.get_nowait()
        explored.add(state.getState())
        if endState == state.getState().getGrid():
            return state
        for children in state.children:
            if children not in frontier and children not in frontier:
                frontier.append(children)
    return "Failure"


def main():
    board = [int(square) for square in input().split()]
    initialState = state(board)
    initialNode = node(initialState, None, None)
    solved = dfs(initialNode, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0])
    print(solved)
    print("Moves: ")
    print("Number of Nodes expanded: ")
    print("Time Taken: ")
    print("Amount of Memory Used: ")

if __name__ == '__main__':
    main()  