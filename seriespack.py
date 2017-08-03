import pygame
import math
import series
from series import RecSeries

#create an object to _approximate_ the nth iteration in the construction of a Cantor set from an infinite series.

class CantorApprox(RecSeries):
	"represent a Cantor set based either on a formula or an interactive construction" 
	length = 1
	def nthapprox(self,n):
		leftroom=self.length
		rightroom=self.length
		intervallist=[]
		
