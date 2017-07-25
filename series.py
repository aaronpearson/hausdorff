class RecSeries():
	origin=0
	formulastring=""
	def top(self,n):
		resultlist=[self.origin]
		for x in range(1,n):
			formindex = str(x-1)
			form= "y = resultlist[" + formindex + "]" + self.formulastring
			eval(form)
			resultlist[n] = y

			
		
