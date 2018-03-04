from django.shortcuts import render

from random import choice
import operator
# Create your views here.

def home(request):
	

	size_population = 10
	best_sample = 3
	lucky_few = 3
	number_of_child = 5
	number_of_generation = 25
	chance_of_mutation = 5
	cate = ['00','01','10']
	price = ['000','001','010','011','100']
	place = ['0','1']

        
	first_gen = []
	while(len(first_gen) <= size_population) :
		temp = ''
		bit_gen = ''.join(choice(['0', '1']) for _ in range(6))
		c = bit_gen[0:2]
		pr = bit_gen[2:5]
		pl = bit_gen[5:6]
		if c in cate and pr in price and pl in place:
			temp += c
			temp += pr
			temp += pl       
			first_gen.append(temp)



	return render(request, 'home.html',{'first_gen':first_gen})


