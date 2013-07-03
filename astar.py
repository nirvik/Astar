#!/usr/bin/python


from numpy import *
from random import *
from math import *
from operator import *
import logging

logging.root.setLevel(logging.INFO)

targetx=0
targety=7
grid = [[1 for j in range(8)] for i in range(6)]

for i in range(4):
	grid[i][4]=0
for i in range(5,0,-1):
	grid[i][2]=0
for i in range(2,6):
	grid[5][i]=0
grid[2][5]=0

l = array(grid)
print array(grid)
	
print '********'

def manhattan(x,y):
	return 10*(abs(x-targetx)+abs(y-targety))

# COMBINATION OF DIJIKSTRA AND BEST FIRST 
# BALANCING MANHATTAN DISTANCE AND SHORTEST DISTANCE
def ASTAR(source, closed_list,open_list):
	xmove= [1,-1,-1,1,1,0,-1,0]
	ymove= [1,-1,1,-1,0,1,0,-1]
	global grid
	for i in zip(xmove,ymove):
		pos = (source[0][0]+i[0],source[0][1]+i[1]) #the exact position
		if pos[0]>=6 or pos[1]>=8 or pos[0]<0 or pos[1]<0 or grid[pos[0]][pos[1]]==0:
			logging.error('INDEX OUT OF RANGE')
			continue
		else:
			logging.error('THE ERROR POS {0}'.format(pos))
			if pos not in closed_list: # if the path is walkable or if its not in the closed list 
				if i[0]>0 and i[1]>0 or i[0]<0 and i[1]<0 or i[0]>0 and i[1]<0 or i[0]<0 and i[1]>0: # if its a diagonal element 
					if pos in open_list: #checking if the key already exists in the open list 
						logging.info('{0} already in open_list and diagonal'.format(pos))
						if g_cost(source[1][0],'diagonal')< open_list[pos][0]: #checking if going to the square is easier from the new parent or its earlier parent is only better 
								g = g_cost(source[1][0],'diagonal')
								h = manhattan(pos[0],pos[1])
								f = g+h
								parent = source[0] # parent becomes the new source 
								open_list[pos]=[g,h,f,parent]
								logging.info('NEW PARENT:{1} ADDED FOR {0}'.format(pos,parent))
						else:
							
							pass
					else:					#not in the open list ! new square
						logging.info('New entry added diagonal {0}'.format(source[1][0]))
						g= g_cost(source[1][0],'diagonal')
						h = manhattan(pos[0],pos[1])
						f = g+h
						parent = source[0]
						open_list[pos]=[g,h,f,parent]
				else:
					if pos in open_list:
						logging.info('{0} already in the open list and horizontal'.format(pos))	
						if g_cost(source[1][0],'horizontal') < open_list[pos][0]:
							parent = source[0]
							g = g_cost(source[1][0],'horizontal')
							h = manhattan(pos[0],pos[1])
							f = g+h
							open_list[pos]=[g,h,f,parent]
							logging.info('NEW PARENT:{1} ADDED FOR {0}'.format(pos,parent))
						else:
							pass
					else:
						logging.info('New entry added horizontal')
						g = g_cost(source[1][0],'horizontal')
						h = manhattan(pos[0],pos[1])
						f = g+h
						parent = source[0]
						open_list[pos] = [g,h,f,parent]
							
					
def g_cost(curr_g,signal):
	
	if signal == 'horizontal':
		return curr_g + 10
	else:
		return curr_g + 14
	

def f_cost(g,h):
	return g+h



def main():
	
	open_list = {}
	source = input('Enter source:')
	h = manhattan(source[0],source[1])
	g = 0 # g value of source is 0
	f = f_cost(g,h)
	parent = source
	open_list[source]=[g,h,f_cost,parent] #hash table implementation  
	closed_list={}
 	target = (targetx,targety)
	while target not in closed_list or open_list:  #open_list
	#	logging.error('{0} current error'.format(current))	
		current=sorted(open_list.iteritems(),key = lambda x:x[1][2])[0] #extracting the lowest f value 
		del open_list[current[0]] # deleting that entry from the open_list 
		logging.info('OPEN_LIST {0} DELETED'.format(current[0]))
		closed_list[current[0]]=current[1]
		ASTAR(current,closed_list,open_list)
		print closed_list

	print 'FINAL \n'
	global grid
	grid = array(grid)
	print grid
	print target
	path = closed_list[(targetx,targety)][-1]
	while path!=source:
		print path
		path = closed_list[path][-1]
	print source

if __name__=='__main__':
	main()
