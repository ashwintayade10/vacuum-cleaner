#ASHWIN TAYADE 2015A7PS0058P

from dirt_generator import dirt,gencoordinates
import sys
w=10
h=10



class Node:
	def __init__(self,state,parent,operator,x,y,h1_val,h2_val):
		self.state=state
		self.parent=parent
		self.operator=operator
		self.x=x
		self.y=y
		self.h1=h1_val
		self.h2=h2_val

	# def __cmp__(self,other):
	# 	return -cmp(self.h1,other.h1)

def move_up(x):		#MOVE AGENT UP
	new_x = x;
	if new_x==0:
		return None
	else:
		return new_x-1

def move_down(x):		#MOVE AGENT DOWN
	new_x = x;
	if new_x==9:
		return None
	else:
		return new_x+1

def move_left(y):		#MOVE AGENT LEFT
	new_y = y;
	if new_y==0:
		return None
	else:
		return new_y-1

def move_right(y):		#MOVE AGENT RIGHT
	new_y = y;
	if new_y==9:
		return None
	else:
		return new_y+1


def hueristic2(state,x,y):		#RETURNS NUMBER OF TILES DIRTY WHILE GIVING MORE WEIGHT TO THOSE TILES THAT ARE REACHED IN ONE MOVE...UNFORTUNATELY HEURISTIC 1 SEEMS TO PERFOEM BETTER
	c=0
	i=x-1
	j=y-1
	while(i<=x+1):
		while(j<=y+1):
			if i>=0 and i<=9 and j>=0 and j<=9:
				if state[i][j]==1:
					c=c+1
			j=j+1
		i=i+1
		j=y-1
	k=0;
	i=x-1
	j=y-1
	if i-1>=0 and i-1<=9 and j>=0 and j<=9:
		if state[i-1][j]==1:
			k=k+1
	if i+1>=0 and i+1<=9 and j>=0 and j<=9:
		if state[i+1][j]==1:
			k=k+1
	if i>=0 and i<=9 and j-1>=0 and j-1<=9:
		if state[i][j-1]==1:
			k=k+1
	if i>=0 and i<=9 and j+1>=0 and j+1<=9:
		if state[i][j+1]==1:
			k=k+1
	return c+k

def hueristic1(state,x,y):		#RETURNS NUMBER OF DIRTY TILES...SEEMS TO BE BETTER OF THE TWO HEURISTICS
	c=0
	i=x-1
	j=y-1
	while(i<=x+1):
		while(j<=y+1):
			if i>=0 and i<=9 and j>=0 and j<=9:
				if state[i][j]==1:
					c=c+1
			j=j+1
		i=i+1
		j=y-1
	return c


def clean(state,x,y):		#CLEANS DIRTY TILE
	if state[x][y]!=1:
		return None
	else:
		new_state = [[0 for q in range(w)] for r in range(h)]
		for i in range(w):
			for j in range(h):
				new_state[i][j]=state[i][j]
		new_state[x][y]=0
		return new_state

def create_node(state,parent,operator,x,y):
	h1 = hueristic1(state,x,y)
	h2 = hueristic2(state,x,y)
	return Node(state,parent,operator,x,y,h1,h2)



def isGoal(state,x,y):		#CHECK FOR GOAL STATE
	flag=0
	for i in range(w):
		for j in range(h):
			if state[i][j]!=0:
				flag=1
	if x==0 and y==0 and flag==0:
		return True
	if x==9 and y==0 and flag==0:
		return True
	if x==0 and y==9 and flag==0:
		return True
	if x==9 and y==9 and flag==0:
		return True
	else:
		return False


def get_children(node,nodes_generated):
	children=[]
	k = nodes_generated
	#if node.state[node.x][node.y]==1:
	
	new_state = clean(node.state,node.x,node.y)
	if new_state!=None:
		children.append(create_node(new_state, node, 'S',node.x, node.y))
	
	new_x = move_up(node.x)
	if new_x!=None:
		children.append(create_node(node.state, node, 'U', new_x, node.y))

	new_y = move_left(node.y)
	if new_y!=None:
		children.append(create_node(node.state, node, 'L', node.x, new_y))

	new_x = move_down(node.x)
	if new_x!=None:
		children.append(create_node(node.state, node, 'D', new_x, node.y))

	new_y = move_right(node.y)
	if new_y!=None:
		children.append(create_node(node.state, node, 'R', node.x, new_y))

	children = [n for n in children if n.y!=None and n.x!=None and n.state!=None]
	k = k+len(children)
	return children,k

def isStateSame(state1,state2):
	flag=0
	for i in range(w):
		for j in range(h):
			if state1[i][j]!=state2[i][j]:
				flag=1
	if flag==0:
		return True
	else:
		return False

def isInFrontier(node,frontier):
	i=0
	for each in frontier:
		if isStateSame(node.state,each.state)==True and node.x==each.x and node.y==each.y:
			return (True,i)
		i=i+1
	return (False,i)

def isInExplored(node,explored):
	for each in explored:
		if isStateSame(node.state,each.state)==True and node.x==each.x and node.y==each.y:
			return True
	return False




def insertInQueueh1(frontier,node):			#INSERTS NODES IN QUEUE SUCH THAT NODES WITH A BETTER HEURISTIC 1 VALUE ARE AT THE FOREFRONT
	i=0;
	if(len(frontier)==0):
		frontier.insert(0,node)
		return 
	#elif node.operator=='S':
	#	frontier.insert(0,node)
	#	return
	else:	 
		for k in frontier:
			if node.h1<k.h1:
				i=i+1
		frontier.insert(i,node)
		return

def insertInQueueh2(frontier,node):			#INSERTS NODES IN QUEUE SUCH THAT NODES WITH A BETTER HEURISTIC 2 VALUE ARE AT THE FOREFRONT
	i=0;
	if(len(frontier)==0):
		frontier.insert(0,node)
		return 
	# elif node.operator=='S':
	# 	frontier.insert(0,node)
	# 	return
	else:	 
		for k in frontier:
			if node.h2<k.h2:
				i=i+1
		frontier.insert(i,node)
		return



def gbfh1(start_state):						#PEERFORM GREEDY BEST FIRST SEARCH USING HEURISTIC 1
	node = create_node(start_state,None,None,0,0)
	size_node = sys.getsizeof(node)
	max_queue = 0
	nodes_generated=1
	frontier= []
	explored=[]
	insertInQueueh1(frontier,node)
	while True:
		if len(frontier)==0:
			return None
		node=frontier.pop(0)
		if isGoal(node.state,node.x,node.y):
			moves=[]
			temp=node
			while temp.parent!=None:
				moves.insert(0,temp.operator)
				temp=temp.parent
			return moves,size_node,max_queue,nodes_generated
		explored.append(node)			#ADD TO EXPLORED QUEUE
		(children,nodes_generated) = get_children(node,nodes_generated)
		for child in children:
			(boolean,val)=isInFrontier(child,frontier)
			if isInExplored(child,explored)==False and boolean==False:
				insertInQueueh1(frontier,child)			#ADD TO 'TO BE EXPLORED QUEUE'
			if boolean==True:
				if child.h1>frontier[val].h1:
					frontier.pop(val)
					insertInQueueh1(frontier,child)		#REPLACE EXISTING STATE WITH BETTER HEURISTIC VALUE
		temp = len(frontier)
		if temp>max_queue:
			max_queue = temp


def gbfh2(start_state):						#PEERFORM GREEDY BEST FIRST SEARCH USING HEURISTIC 2
	node = create_node(start_state,None,None,0,0)
	size_node = sys.getsizeof(node)
	max_queue = 0
	nodes_generated=1
	frontier= []
	explored=[]
	insertInQueueh2(frontier,node)		#ADD TO 'TO BE EXPLORED QUEUE'
	while True:
		if len(frontier)==0:
			return None
		node=frontier.pop(0)
		if isGoal(node.state,node.x,node.y):
			moves=[]
			temp=node
			while temp.parent!=None:
				moves.insert(0,temp.operator)
				temp=temp.parent
			return moves,size_node,max_queue,nodes_generated
		explored.append(node)
		(children,nodes_generated) = get_children(node,nodes_generated)
		for child in children:
			(boolean,val)=isInFrontier(child,frontier)
			if isInExplored(child,explored)==False and boolean==False:
				insertInQueueh2(frontier,child)
			if boolean==True:
				if child.h2>frontier[val].h2:
					frontier.pop(val)
					insertInQueueh2(frontier,child)		#REPLACE EXISTING STATE WITH BETTER HEURISTIC VALUE
		temp = len(frontier)
		if temp>max_queue:
			max_queue = temp

