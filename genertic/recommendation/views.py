from django.shortcuts import render

from random import choice
import operator
from .models import *
import operator
import random
# Create your views here.


def show(request,show_list):
	list_sorted = []

	

	
	for li in show_list :
		duplicate = ""	
		new_dic = {'rule' : '' , 'store' : []}
		sortedlist = sorted(li['store'] , key=lambda elem: "%d " % (elem['count']))

		# new_dic = {'rule' : li['rule'] , 'store' : sortedlist[::-1]}
		new_dic['rule'] = li['rule']
		new_dic['store'] =sortedlist[::-1]
		one = []
		two = []
		three = []
		for index in new_dic['store']:
			if index['count'] == 1 :
				one.append(index)
			elif index['count'] == 2 :
				two.append(index)
			elif index['count'] == 3 :
				three.append(index)
		select = {}
		if len(three) > 0 :
			select = random.choice(three)
			duplicate+= select['name']

			while len(three) > 1 and select['name'] in duplicate :
				select = random.choice(three)


			# duplicate.append(select['name'])
		elif len(two) > 0:
			select = random.choice(two)
			duplicate+= select['name']
		
			while len(two) > 1 and select['name'] in duplicate :
				select = random.choice(two)


			# duplicate.append(select['name'])
		elif len(one) > 0 :
			select = random.choice(one)
			duplicate+= select['name']
			while len(one) > 1 and select['name'] in duplicate :
				select = random.choice(one)
	

			# duplicate.append(select['name'])

		list_sorted.append({'rule':new_dic['rule'],'store':select})
	

	show_list = []
	check_dup = []
	for i in list_sorted :
		if not i['store']['name'] in check_dup :
			show_list.append(i)
			check_dup.append(i['store']['name'])


	Populations.objects.update_or_create(user = request.user, 
		defaults={'chromosome1':list_sorted[0]['rule'],'chromosome2':list_sorted[1]['rule'],
	'chromosome3':list_sorted[2]['rule'],'chromosome4':list_sorted[3]['rule'],'store1': list_sorted[0]['store']['name'],'store2' : list_sorted[1]['store']['name'] ,
		'store3' : list_sorted[2]['store']['name'] ,'store4' : list_sorted[3]['store']['name']})
	

	return show_list

def initial(request):
	size_population = 4
	best_sample = 3
	lucky_few = 3
	number_of_child = 5
	number_of_generation = 25
	chance_of_mutation = 5
	cate = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101']
	price = ['000','001','010','011','100']
	place = ['0','1']
	stores = Store.objects.all()
	show_list = []
	select = []
	first_gen = []
	li = []
	count_num = 0 
	check_dic = {}
	bit_gen = ''
	c = ''
	pr = ''
	pl = ''

	

	while len(show_list) < size_population :
		
		bit_gen = ''.join(random.choice(['0', '1']) for _ in range(8))
		count_num += 1
		c = bit_gen[0:4]
		pr = bit_gen[4:7]
		pl = bit_gen[7:8]
		name_dup = []

		if c in cate and pr in price and pl in place:
			check_dic = {'rule' : '', 'store' :[]}
			# temp += c
			# temp += pr
			# temp += pl

			
				
			for store in stores :
				dic = {'name':'', 'count' : 0}
				count = 0

				if c == '0000' :
					if 'อาหารตามสั่ง' in store.tags :
						count += 1
				elif c == '0001' :
					if 'ก๋วยเตี๋ยว' in store.tags :
						count += 1
				elif c == '0010' :
					if 'ผัดไทย' in store.tags or 'ราดหนา้า' in store.tags :
						count += 1
				elif c == '0011' :
					if 'โจ๊ก' in store.tags or 'ข้าวต้ม' in store.tags :
						count += 1
				elif c == '0100' :
					if 'โรตี' in store.tags :
						count += 1

				elif c == '0101' :
					if 'สเต็ก' in store.tags :
						count += 1
				elif c == '0110' :
					if 'ลูกชิ้น' in store.tags :
						count += 1
				elif c == '0111' :
					if 'ไส้กรอก' in store.tags :
						count += 1
				elif c == '1000' :
					if 'หมูปิ้ง' in store.tags or 'ตับปิ้ง' in store.tags or 'ไก่ปิ้ง' in store.tags  :
						count += 1
				elif c == '1001' :
					if 'น้ำ' in store.tags or 'นำ้ปั่น' in store.tags:
						count += 1
				elif c == '1010' :
					if 'ผลไม้' in store.tags :
						count += 1
				elif c == '1100' :
					if 'มันบด' in store.tags or 'แฮมเบอร์เกอร์' in store.tags or 'มันอบ' in store.tags  or 'เฟรนช์ฟรายส์' in store.tags :
						count += 1
				elif c == '1101' :
					if 'ไก่' in store.tags :
						count += 1

				if pr == '000' :
					if '000' in store.price :
						count += 1
				elif pr == '001' :
					if '001' in store.price :
						count += 1
				elif pr == '010' :
					if '010' in store.price :
						count += 1
				elif pr == '011' :
					if '011' in store.price:
						count += 1
				elif pr == '100' :
					if '100' in store.price :
						count += 1

				if pl == '0' :
					if store.place == 'โต้รุ่ง' :
						count += 1
				elif pl == '1' :
					if store.place == 'เชียงราก' :
						count += 1

				if count > 0 :
					dic['name'] = store.name
					dic['count'] = count

					check_dic['store'].append(dic)
			

			check_dic['rule'] = bit_gen

			show_list.append(check_dic)


	return show_list
	
	




def home(request):

	s_list = initial(request)
	show_list = show(request,s_list)


	return render(request, 'home.html',{'store':show_list,'list_sorted':'list_sorted'})


def click(request,name,rule):
	pop = Populations.objects.get(user=request.user)
	best = ""
	lucky_list = []
	choose_list = []

	# selection
	if pop.chromosome1 == rule :
		best = pop.chromosome1
		lucky_list.append(pop.chromosome2)
		lucky_list.append(pop.chromosome3)
		lucky_list.append(pop.chromosome4)

	if pop.chromosome2 == rule :
		best = pop.chromosome2
		lucky_list.append(pop.chromosome1)
		lucky_list.append(pop.chromosome3)
		lucky_list.append(pop.chromosome4)

	if pop.chromosome3 == rule :
		best = pop.chromosome3
		lucky_list.append(pop.chromosome2)
		lucky_list.append(pop.chromosome1)
		lucky_list.append(pop.chromosome4)

	if pop.chromosome4 == rule :
		best = pop.chromosome4
		lucky_list.append(pop.chromosome2)
		lucky_list.append(pop.chromosome3)
		lucky_list.append(pop.chromosome1)

	lucky_item = random.choice(lucky_list)

	nextPopulation = []
	nextPopulation.append(best)
	nextPopulation.append(lucky_item)

	# crossover
	nextPopulation.append(createChild(nextPopulation[0],nextPopulation[1]))
	nextPopulation.append(createChild(nextPopulation[0],nextPopulation[2]))

	#mutate
	chance_of_mutation = 0.1
	for i in range(len(nextPopulation)):
		if random.random() < chance_of_mutation:
			nextPopulation[i] = mutateWord(nextPopulation[i])


	print(len(nextPopulation))

	show_list = queryStore(request,nextPopulation)
	list_sorted = show(request,show_list)

	return render(request, 'click.html',{'lucky_item':lucky_item,'best':best,'nextPopulation':nextPopulation,'list_sorted':list_sorted})

def mutateWord(word):



	c = word[0:4]
	pr = word[4:7]
	pl = word[7:8]
	cate = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101']
	price = ['000','001','010','011','100']
	place = ['0','1']
	index_modification = int(random.random() * len(word))

	if (index_modification == 0):
		word = ''.join(random.choice(['0', '1'])) + word[1:]
	else:
		word = word[:index_modification] +''.join(random.choice(['0', '1'])) + word[index_modification+1:]

	c = word[0:4]
	pr = word[4:7]
	pl = word[7:8]

	while True:

		if c in cate and pr in price and pl in place:
			break
		else :

			print("before while: ",word)
			index_modification = int(random.random() * len(word))

			if (index_modification == 0):
				word = ''.join(random.choice(['0', '1'])) + word[1:]
			else:
				word = word[:index_modification] +''.join(random.choice(['0', '1'])) + word[index_modification+1:]

			c = word[0:4]
			pr = word[4:7]
			pl = word[7:8]
			print("adfter while: ",word)



	return word

def queryStore(request,lists):

	show_list = []
	list_sorted = []
	size_population = 4
	cate = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101']
	price = ['000','001','010','011','100']
	place = ['0','1']
	stores = Store.objects.all()
	# print(len(lists))
	for li in lists :
		

		c = li[0:4]
		pr = li[4:7]
		pl = li[7:8]

		print(li)
		if c in cate and pr in price and pl in place:
			check_dic = {'rule' : '', 'store' :[]}

			for store in stores :
				dic = {'name':'', 'count' : 0}
				count = 0

				if c == '0000' :
					if 'อาหารตามสั่ง' in store.tags :
						count += 1
				elif c == '0001' :
					if 'ก๋วยเตี๋ยว' in store.tags :
						count += 1
				elif c == '0010' :
					if 'ผัดไทย' in store.tags or 'ราดหนา้า' in store.tags :
						count += 1
				elif c == '0011' :
					if 'โจ๊ก' in store.tags or 'ข้าวต้ม' in store.tags :
						count += 1
				elif c == '0100' :
					if 'โรตี' in store.tags :
						count += 1

				elif c == '0101' :
					if 'สเต็ก' in store.tags :
						count += 1
				elif c == '0110' :
					if 'ลูกชิ้น' in store.tags :
						count += 1
				elif c == '0111' :
					if 'ไส้กรอก' in store.tags :
						count += 1
				elif c == '1000' :
					if 'หมูปิ้ง' in store.tags or 'ตับปิ้ง' in store.tags or 'ไก่ปิ้ง' in store.tags  :
						count += 1
				elif c == '1001' :
					if 'น้ำ' in store.tags or 'นำ้ปั่น' in store.tags:
						count += 1
				elif c == '1010' :
					if 'ผลไม้' in store.tags :
						count += 1
				elif c == '1100' :
					if 'มันบด' in store.tags or 'แฮมเบอร์เกอร์' in store.tags or 'มันอบ' in store.tags  or 'เฟรนช์ฟรายส์' in store.tags :
						count += 1
				elif c == '1101' :
					if 'ไก่' in store.tags :
						count += 1

				if pr == '000' :
					if '000' in store.price :
						count += 1
				elif pr == '001' :
					if '001' in store.price :
						count += 1
				elif pr == '010' :
					if '010' in store.price :
						count += 1
				elif pr == '011' :
					if '011' in store.price:
						count += 1
				elif pr == '100' :
					if '100' in store.price :
						count += 1

				if pl == '0' :
					if store.place == 'โต้รุ่ง' :
						count += 1
				elif pl == '1' :
					if store.place == 'เชียงราก' :
						count += 1

				if count > 0 :
					dic['name'] = store.name
					dic['count'] = count

					check_dic['store'].append(dic)
			

			check_dic['rule'] = li

			list_sorted.append(check_dic)

	print(len(list_sorted))
	return list_sorted

def createChild(individual1, individual2):
	cate = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101']
	price = ['000','001','010','011','100']
	place = ['0','1']
	name_dup = []

	child = ""
	for i in range(len(individual1)):
		if (int(100 * random.random()) < 50):
			child += individual1[i]
		else:
			child += individual2[i]
	c = child[0:4]
	pr = child[4:7]
	pl = child[7:8]
	while True:

		if c in cate and pr in price and pl in place:
			break
		else :
			child = ""
			for i in range(len(individual1)):
				if (int(100 * random.random()) < 50):
					child += individual1[i]
				else:
					child += individual2[i]

			c = child[0:4]
			pr = child[4:7]
			pl = child[7:8]




	return child