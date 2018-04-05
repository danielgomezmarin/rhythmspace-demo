#to clear some doubts check the example called simple.py
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import Delaunay
try:
	import pyext
except:
	print "ERROR: This script must be loaded by the PD/Max pyext external"


# helper function - determine whether argument is a numeric type

global listofpoints

listofpoints=[]

class maketri(pyext._class):

	_inlets=2
	_outlets=3

	# number of inlets and outlets

	def list_2(self,*s): #inlet 2 (from left) receives a list
		listofpoints.append(s)
		#print listofpoints
		#self._outlet(1,s)

	def _anything_1(self,*s): #inlet 1 (from left) receives 'anything'
		message=str(s[0])
		#print type(message)
		if message == 'build':
			print "building space!"
			points=np.array(listofpoints)
			pointsincols=[]

			for i in range(len(points[0])):
				N=[x[i] for x in points]
				N=np.array(N)
				N=(N-min(N))/(max(N)-min(N))
				pointsincols.append(N)
			global N_points
			N_points=[]
			for row in range(len(pointsincols[0])):
				N_point=[x[row] for x in pointsincols]
				N_points.append(N_point)
			N_points=np.array(N_points)
			#print N_points #lista de puntos normalizada

			tri = Delaunay(N_points)
			global listoftri
			listoftri=tri.simplices
			#print tri.simplices
			for t in listoftri:
				tripoints=N_points[t[0]][0],N_points[t[0]][1], N_points[t[1]][0],N_points[t[1]][1], N_points[t[2]][0],N_points[t[2]][1]
				#print tripoints
				self._outlet(1,tripoints) #this is outlet 1 (leftmost)
			#uncomment rto plot
			# plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
			# plt.plot(points[:,0], points[:,1], 'o')
			# plt.show()
			for n,p in enumerate(N_points):
				if n < 3:
					col='red'
				else:
					if n < 6:
						col='blue'
					else:
						col='green'
				mess=col,p

				self._outlet(2,mess) #this is outlet 2 (from left)
			self._outlet(3,len(N_points)+(len(listoftri)*3)) #this is outlet 3 (from left) outputs total no. of patterns
		else:
			a=0

def triangarea(p1,p2,p3):
	area=abs((p1[0]*(p2[1]-p3[1]))+(p2[0]*(p3[1]-p1[1]))+(p3[0]*(p1[1]-p2[1])))*0.5
	return area

def isinside(s,tri):
	#is inside if 
	#print s, listofpoints[tri[0]],tri[1],tri[2]

	a1=triangarea(N_points[tri[0]],N_points[tri[1]],N_points[tri[2]])
	a2=triangarea(N_points[tri[0]],N_points[tri[1]],s)
	a3=triangarea(N_points[tri[1]],N_points[tri[2]],s)
	a4=triangarea(N_points[tri[0]],N_points[tri[2]],s)
	if a1<(a2+a3+a4):
		inside=0
	else:
		inside=1
	return inside

class mouseover(pyext._class):
	_inlets=1
	_outlets=1
	def list_1(self,*s):
		#print s[0]*300,s[1]*300 
		listtestinside=[]
		for tri in listoftri: # tri=ista de tres puntos que forma un triangulo
			#print 'a',listofpoints[tri[0]]
			#print isinside(s,tri)
			listtestinside.append(isinside(s,tri))
		#print listtestinside
		for n,f in enumerate(listtestinside):
			if f==1:
				#print s, listoftri[n],listoftri[n][0], N_points[listoftri[n][0]]
				#print s, N_points(1), listoftri[n]
				
				#print s, N_points(listoftri[n][0]),N_points(listoftri[n][1]),N_points(listoftri[n][2])
				intersec1= find_intersection(s,N_points[listoftri[n][0]],N_points[listoftri[n][1]],N_points[listoftri[n][2]])
				#print s,N_points[listoftri[n][0]],N_points[listoftri[n][1]],N_points[listoftri[n][2]]
				# print s, intersec1
				# print float(distance(s,N_points[listoftri[n][0]]))/distance(N_points[listoftri[n][0]],intersec1)
				w= weights (s, N_points[listoftri[n][0]], N_points[listoftri[n][1]], N_points[listoftri[n][2]])
				w=np.array(w)
				w=w/float(sum(w))


				triweight=float(listoftri[n][0]),w[0],float(listoftri[n][1]),w[1],float(listoftri[n][2]),w[2]
				#print triweight
				self._outlet(1,triweight)
			else:
				a=0
		

def find_intersection( p0, p1, p2, p3 ) :

    s10_x = p1[0] - p0[0]
    s10_y = p1[1] - p0[1]
    s32_x = p3[0] - p2[0]
    s32_y = p3[1] - p2[1]
    
    denom = s10_x * s32_y - s32_x * s10_y

    #if denom == 0 : return None # collinear

    denom_is_positive = denom > 0

    s02_x = p0[0] - p2[0]
    s02_y = p0[1] - p2[1]

    s_numer = s10_x * s02_y - s10_y * s02_x

    #if (s_numer < 0) == denom_is_positive : return None # no collision

    t_numer = s32_x * s02_y - s32_y * s02_x

    #if (t_numer < 0) == denom_is_positive : return None # no collision

    #if (s_numer > denom) == denom_is_positive or (t_numer > denom) == denom_is_positive : return None # no collision


    # collision detected

    t = t_numer / denom

    intersection_point = [ p0[0] + (t * s10_x), p0[1] + (t * s10_y) ]


    return intersection_point

def distance(a,b):
	d=math.sqrt(pow(abs(a[0]-b[0]),2)+pow(abs(a[1]-b[1]),2))
	return d

def weights(s,p1,p2,p3):
	w1=1-(float(distance(s,p1))/distance(p1,find_intersection(s,p1,p2,p3)))
	w2=1-(float(distance(s,p2))/distance(p2,find_intersection(s,p2,p1,p3)))
	w3=1-(float(distance(s,p3))/distance(p3,find_intersection(s,p3,p1,p2)))
	return w1,w2,w3


