def mark_score():
	D = {}
	while True:
		
		Id = input('enter student id: ')
		mark = input('enter your score separated by comma: ')
		more_student_details = input('enter no if there\s no more student details to input:')
		
		if Id in D:
			print('Id exist')
		else:
			D[Id] = mark.split(',')
			
		if more_student_details == 'no':
			break
		
	return D

getdata = mark_score()


def getAvg(D):
	avg = {}
	for x in D:
		L = D[x]
		s = 0
		for i in L:
			s += int(i)
		avg[x] = s/len(L)
	return avg

print(getAvg(getdata))







