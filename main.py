with open('data.txt', 'r') as data:
	data = [i.strip('\n') for i in data.readlines()]
	
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = alpha+alpha.upper()
alpha = {alpha[i]: i+1 for i in range(52)}


def get_packsum(data, score):
	packsum = 0
	for pack in data:
		half = int(len(pack)/2)
		front, back = set(pack[:half:]), set(pack[half::])
		inter = list(front.intersection(back))
		packsum += score[inter[0]]
	return packsum
	
print(get_packsum(data, alpha))


def get_badges(data, score):
	badge_sum = index = 0
	temp = []
	for i in range(len(data)):
		if (i + 1) % 3 == 0:
			x = set(data[i]).intersection(*temp)
			badge_sum += score[list(x)[0]]
			temp = []
		else:
			temp.append(set(data[i]))
	return badge_sum
	
print(get_badges(data, alpha))