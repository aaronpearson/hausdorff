class RecSeries():
	origin=0
	formulastring=""
	def top(self,n):
		resultlist=[self.origin]
		for x in range(1,n):
			formindex = str(x-1)
			#form= "y = resultlist[" + formindex + "]" + self.formulastring
			y = eval('resultlist[' + formindex + "]" + self.formulastring)	
			resultlist.append(y) #fixed index error
		return resultlist
			
		
testseries=RecSeries()
testseries.origin=1
testseries.formulastring="+1"
