#ASHWIN TAYADE 2015A7PS0058P

import turtle as t
from dirt_generator import gencoordinates,dirt
from VacuumCleaner import bfs
from VacuumCleanerT2 import gbfh1,gbfh2
import time
import sys

w=10
h=10

def square(x,y):
	t.setpos(x,y)
	t.pendown()
	for i in range(4):
		t.fd(15)
		t.right(90)
	t.penup()

def fill(x,y):			#Fills Dirt
	t.color('brown')
	t.penup()
	t.setpos(x,y)
	t.pendown()
	t.begin_fill()
	square(x,y)
	t.end_fill()
	t.color('black')

def clean(x,y):			#Cleans dirt
	t.color('lightblue')
	t.penup()
	t.setpos(x,y)
	t.pendown()
	t.begin_fill()
	square(x,y)
	t.end_fill()
	t.color('black')
	square(x,y)

def write(x,y,s):
	t.penup()
	t.setpos(x,y)
	t.pendown()
	t.write(s)
	t.penup()

def main():				#Sets up environment
	s = t.Screen()
	s.bgcolor('lightblue')
	t.speed(0)
	#t.hideturtle()
	t.hideturtle()
	t.tracer(0,0)
	t.setup(900,600)
	t.screensize(900, 600)
	t.setworldcoordinates(0, 0, 900, 600)
	t.penup()
	t.setpos(300, 0) 
	t.pendown()
	t.setpos(300, 600)
	t.penup()
	t.setpos(600, 0)
	t.pendown()
	t.setpos(600, 600)
	t.penup()
	t.setpos(300,300)
	t.pendown()
	t.setpos(900,300)
	t.penup()


	x=450
	y=450
	for i in range(10):
		m=y
		for j in range(10):
			square(x,m)
			m=m-15
		t.penup()
		x=x+15
		t.setpos(x,y)
	
	x=750
	y=450

	for i in range(10):
		m=y
		for j in range(10):
			square(x,m)
			m=m-15
		t.penup()
		x=x+15
		t.setpos(x,y)

	d = int(input("Percentage Dirt"))
	dirty_coordinates = dirt(d)  #FUNCTION GENERATES DIRT IN NUMBER OF THE TOTAL TILES
	t.penup()
	t.setpos(457.5,450-7.5)
	t.update()
	t.tracer(1,10)
	t.speed(10)
	start_state=[[0 for q in range(w)] for r in range(h)]
	for i in dirty_coordinates:
 		start_state[i[0]][i[1]]=1

	while True:
		option = int(input("Enter option: \n 1] Room Environment \n 2] Path using T1 \n 3] Path using T2 \n 4] Show results \n 5] Exit\n")) 
		if option==1:
			t.tracer(0,0)
			for i in dirty_coordinates:
				x1 = 450 + i[1]*15
				y1 = 450 - i[0]*15
				fill(x1,y1)

			for i in dirty_coordinates:
				x1 = 750 + i[1]*15
				y1 = 450 - i[0]*15
				fill(x1,y1)
			t.update()
			t.tracer(1,10)
		if option==2:
			start_time = time.time()
			(moves,size_node,max_queue,nodes_generated) = bfs(start_state)	#UNINFORMED SERACH
			end_time = time.time()
			tot_time = end_time - start_time
			moves1 = None
		if option==3:
			start_time = time.time()
			(moves,size_node,max_queue,nodes_generated) = gbfh1(start_state)	#INFORMED SEARCH HEURISTIC 1
			end_time = time.time()
			tot_time = end_time - start_time
			start_time1 = time.time()
			(moves1,size_node1,max_queue1,nodes_generated1) = gbfh2(start_state) #INFORMED SEARCH HEURISTIC 2
			end_time1 = time.time()
			tot_time1 = end_time1 - start_time1
		if option==4:		#DISPLAYS RESULTS
			cost=0
			t.penup()
			x_cur=457.5
			y_cur=442.5
			t.setpos(x_cur,y_cur)
			prev=None
			text_pointer_x=20
			text_pointer_y=400
			for move in moves:
				t.color('red')
				if(move=='S'):
					cost = cost+1
					(m,n)=t.position()
					t.penup()
					t.setpos(text_pointer_x,text_pointer_y)
					t.pendown()
					t.write("Cleaning")
					text_pointer_y = text_pointer_y-10
					time.sleep(.1)
					t.penup()
					t.setpos(m,n)
					time.sleep(.1)
					t.tracer(0,0)
					t.pendown()
					(x,y)=t.position()
					c=x-7.5
					d=y+7.5
				 	clean(c,d)
				 	t.color('red')
				 	t.penup()
				 	t.setpos(x,y)
				 	if prev!=None:
				 		if prev=='U':
				 			t.penup()
				 			t.setpos(x,y-7.5)
				 			t.pendown()
				 			t.setpos(x,y)
				 			t.penup()
				 		if prev=='L':
				 			t.penup()
				 			t.setpos(x+7.5,y)
				 			t.pendown()
				 			t.setpos(x,y)
				 			t.penup()
				 		if prev=='D':
				 			t.penup()
				 			t.setpos(x,y+7.5)
				 			t.pendown()
				 			t.setpos(x,y)
				 			t.penup()
				 		if prev=='R':
				 			t.penup()
				 			t.setpos(x-7.5,y)
				 			t.pendown()
				 			t.setpos(x,y)
				 			t.penup()
				 	prev='S'
				 	t.update()
				 	t.tracer(1,10)
				 	time.sleep(.1)
				elif(move=='U'):
					cost = cost+2
					(m,n)=t.position()
					t.penup()
					t.setpos(text_pointer_x,text_pointer_y)
					t.pendown()
					t.write("Moving Up")
					text_pointer_y = text_pointer_y-10
					t.penup()
					time.sleep(.1)
					t.setpos(m,n)
					time.sleep(.1)
					t.pendown()
					(x,y)=t.position()
					t.setpos(x,y+15)
					t.penup()
					time.sleep(.1)
					prev='U'
				elif(move=='L'):
					cost = cost+2
					(m,n)=t.position()
					t.penup()
					t.setpos(text_pointer_x,text_pointer_y)
					t.pendown()
					t.write("Moving Left")
					text_pointer_y = text_pointer_y-10
					t.penup()
					time.sleep(.1)
					t.setpos(m,n)
					time.sleep(.1)
					t.pendown()
					(x,y)=t.position()
					t.setpos(x-15,y)
					t.penup()
					time.sleep(.1)
					prev='L'
				elif(move=='D'):
					cost = cost+2
					(m,n)=t.position()
					t.penup()
					t.setpos(text_pointer_x,text_pointer_y)
					t.pendown()
					t.write("Moving Down")
					text_pointer_y = text_pointer_y-10
					t.penup()
					time.sleep(.1)
					t.setpos(m,n)
					time.sleep(.1)
					t.pendown()
					(x,y)=t.position()
					t.setpos(x,y-15)
					t.penup()
					time.sleep(.1)
					prev='D'
				elif(move=='R'):
					cost = cost+2
					(m,n)=t.position()
					t.penup()
					t.setpos(text_pointer_x,text_pointer_y)
					t.pendown()
					t.write("Moving Right")
					text_pointer_y = text_pointer_y-10
					t.penup()
					time.sleep(.1)
					t.setpos(m,n)
					time.sleep(.1)
					t.pendown()
					(x,y)=t.position()
					t.setpos(x+15,y)
					t.penup()
					time.sleep(.1)
					prev='R'
			t.penup()
			t.setpos(20,550)
			t.pendown()
			t.write("Size of Node in bytes:")
			t.penup()
			t.setpos(20,540)
			t.pendown()
			t.write(size_node)
			t.penup()
			t.setpos(20,520)
			t.pendown()
			t.write("Max queue size")
			t.penup()
			t.setpos(20,510)
			t.pendown()
			t.write(max_queue)
			t.penup()
			t.setpos(20,490)
			t.pendown()
			t.write("Cleaning Cost:")
			t.penup()
			t.setpos(20,480)
			t.pendown()
			t.write(cost)
			t.penup()
			t.setpos(20,460)
			t.pendown()
			t.write("Total number of nodes generated:")
			t.penup()
			t.setpos(20,450)
			t.pendown()
			t.write(nodes_generated)
			t.penup()
			t.setpos(20,430)
			t.pendown()
			t.write("Total Time to compute Path:")
			t.penup()
			t.setpos(20,420)
			t.pendown()
			t.write(tot_time)

			if moves1!=None:
				t.color('darkgreen')
				cost=0
				t.penup()
				x_cur=757.5
				y_cur=442.5
				t.setpos(x_cur,y_cur)
				prev=None
				text_pointer_x=100
				text_pointer_y=400
				for move in moves1:
					if(move=='S'):
						cost = cost+1
						# (m,n)=t.position()
						# write(text_pointer_x,text_pointer_y,"Cleaning")
						# text_pointer_y = text_pointer_y - 20
						# t.setpos(m,n)
						(m,n)=t.position()
						t.penup()
						t.setpos(text_pointer_x,text_pointer_y)
						t.pendown()
						t.write("Cleaning")
						text_pointer_y = text_pointer_y-10
						time.sleep(.1)
						t.penup()
						t.setpos(m,n)
						time.sleep(.1)
						t.tracer(0,0)
						t.pendown()
						(x,y)=t.position()
						c=x-7.5
						d=y+7.5
						#t.tracer(0,0)
					 	clean(c,d)
					 	t.color('darkgreen')
					 	t.penup()
					 	t.setpos(x,y)
					 	if prev!=None:
					 		if prev=='U':
					 			t.penup()
					 			t.setpos(x,y-7.5)
					 			t.pendown()
					 			t.setpos(x,y)
					 			t.penup()
					 		if prev=='L':
					 			t.penup()
					 			t.setpos(x+7.5,y)
					 			t.pendown()
					 			t.setpos(x,y)
					 			t.penup()
					 		if prev=='D':
					 			t.penup()
					 			t.setpos(x,y+7.5)
					 			t.pendown()
					 			t.setpos(x,y)
					 			t.penup()
					 		if prev=='R':
					 			t.penup()
					 			t.setpos(x-7.5,y)
					 			t.pendown()
					 			t.setpos(x,y)
					 			t.penup()
					 	prev='S'
					 	t.update()
					 	t.tracer(1,10)
					 	time.sleep(.1)
					elif(move=='U'):
						cost = cost+2
						(m,n)=t.position()
						t.penup()
						t.setpos(text_pointer_x,text_pointer_y)
						t.pendown()
						t.write("Moving Up")
						text_pointer_y = text_pointer_y-10
						t.penup()
						time.sleep(.1)
						t.setpos(m,n)
						time.sleep(.1)
						t.pendown()
						(x,y)=t.position()
						t.setpos(x,y+15)
						t.penup()
						time.sleep(.1)
						prev='U'
					elif(move=='L'):
						cost = cost+2
						(m,n)=t.position()
						t.penup()
						t.setpos(text_pointer_x,text_pointer_y)
						t.pendown()
						t.write("Moving Left")
						text_pointer_y = text_pointer_y-10
						t.penup()
						time.sleep(.1)
						t.setpos(m,n)
						time.sleep(.1)
						t.pendown()
						(x,y)=t.position()
						t.setpos(x-15,y)
						t.penup()
						time.sleep(.1)
						prev='L'
					elif(move=='D'):
						cost = cost+2
						(m,n)=t.position()
						t.penup()
						t.setpos(text_pointer_x,text_pointer_y)
						t.pendown()
						t.write("Moving Down")
						text_pointer_y = text_pointer_y-10
						t.penup()
						time.sleep(.1)
						t.setpos(m,n)
						time.sleep(.1)
						t.pendown()
						(x,y)=t.position()
						t.setpos(x,y-15)
						t.penup()
						time.sleep(.1)
						prev='D'
					elif(move=='R'):
						cost = cost+2
						(m,n)=t.position()
						t.penup()
						t.setpos(text_pointer_x,text_pointer_y)
						t.pendown()
						t.write("Moving Right")
						text_pointer_y = text_pointer_y-10
						t.penup()
						time.sleep(.1)
						t.setpos(m,n)
						time.sleep(.1)
						t.pendown()
						(x,y)=t.position()
						t.setpos(x+15,y)
						t.penup()
						time.sleep(.1)
						prev='R'
				t.penup()
				t.setpos(100,550)
				t.pendown()
				t.write("Size of Node in bytes:")
				t.penup()
				t.setpos(100,540)
				t.pendown()
				t.write(size_node1)
				t.penup()
				t.setpos(100,520)
				t.pendown()
				t.write("Max queue size")
				t.penup()
				t.setpos(100,510)
				t.pendown()
				t.write(max_queue1)
				t.penup()
				t.setpos(100,490)
				t.pendown()
				t.write("Cleaning Cost:")
				t.penup()
				t.setpos(100,480)
				t.pendown()
				t.write(cost)
				t.penup()
				t.setpos(100,460)
				t.pendown()
				t.write("Total number of nodes generated:")
				t.penup()
				t.setpos(100,450)
				t.pendown()
				t.write(nodes_generated1)
				t.penup()
				t.setpos(100,430)
				t.pendown()
				t.write("Total Time to compute Path:")
				t.penup()
				t.setpos(100,420)
				t.pendown()
				t.write(tot_time1)
				t.color('black')
			t.getscreen()._root.mainloop()
		if option==5:
			return


if __name__=="__main__":
	main()