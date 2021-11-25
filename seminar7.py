#task10
myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}



def take_average(total, finalMarks):
	average = 0
	average = total/len(finalMarks)
	return average

def calculateAverage(finalMarks):
	total = 0

	for key in finalMarks:
		total = total+finalMarks[key]
	average = total/len(finalMarks)
	return total

print(take_average(calculateAverage(myFinalMarks), myFinalMarks))


























#task 11
csf = {
'cw1-weight': 0.4,
'cw1-mark':79,
'exam-weight':0.6,
'exam-mark':65
}



#slide 40
def histogram(s): 
	d = dict() 
	for c in s: 
		if c not in d: 
			d[c] = 1 
		else: 
			d[c] += 1 
	return d

def reverse_lookup(d, v):
	for k in d:
		if d[k]==v:
			return k
	raise LookupError()




