"""
File: boggle.py
Name: Jack Chen
----------------------------------------
This algorithm will be able to find out all the words that appears in an 4x4 boggle game.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Please insert a total of 16 alphabets that build up the boggle game.
	The algorithm will be able to find out all the words that appears the game.
	"""
	start = time.time()
	####################
	first_row = input('1 row of letters: ')
	second_row = input('2 row of letters: ')
	third_row = input('3 row of letters: ')
	forth_row = input('4 row of letters: ')
	game_alpha = turn_to_list(first_row, second_row, third_row, forth_row)
	boggle_game(game_alpha)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def turn_to_list(a, b, c, d):
	'''
	:param a: str, The first four letters of the boggle game.
	:param b: str, The second four letters of the boggle game.
	:param c: str, The third four letters of the boggle game.
	:param d: str, The forth four letters of the boggle game.
	:return: list, a list that includes a orderly listed 16 lower-case alphabets in the boggle game.
	'''
	rows = (a, b, c, d)
	letter_lst = []
	for x in rows:  # append all the letters in the boggle game into the list.
		for alpha in x.split():
			letter_lst.append(alpha)
	case_sensitive_lst = case_sensitive(letter_lst)  # Case-sensitive
	return case_sensitive_lst


def case_sensitive(words):
	lower_lst = []
	for word in words:
		lower_lst.append(word.lower)
	return lower_lst


def boggle_game(alpha):
	# Alpha is the complete boggle game list that include all 16 characters.
	cur_lst = []  # lst, current list that is used to append one single letter.
	sum_lst = []  # lst, summarized list that is used to record all the words in the boggle game.
	cur_number_helper = []  # lst, a list that records the track number(0-15) that the word had gone through.
	d_lst = read_dictionary()
	boggle_lst = [-5, -4, -3, -1, 1, 3, 4, 5]  # Index 1, 2, 5, 6, 9, 10, 13, 14. Index that doesn't have to change row.
	boggle_lst_left = [-4, -3, 1, 4, 5]  # Index 0, 4, 8, 12. Index on the left.
	boggle_lst_right = [-5, -4, -1, 3, 4]  # Index 0, 4, 8, 12. Index on the right.
	for i in range(len(alpha)):  # Loop from the first index of the alphabet lst to the last.
		cur_lst.append(alpha[i])
		cur_number_helper.append(i)
		boggle_game_helper(alpha, cur_lst, sum_lst, d_lst, i, boggle_lst, boggle_lst_left, boggle_lst_right, cur_number_helper)
		cur_lst = []  # Clean up the lst to get to the next index.
		cur_number_helper = []
	print(f'There are {len(sum_lst)} words in total')


def boggle_game_helper(alpha, cur_lst, sum_lst, d_lst, cur_num, boggle_lst, boggle_lst_left, boggle_lst_right, cur_num_helper):
	'''
	:param alpha: The complete boggle game list that include all 16 characters.
	:param cur_lst: lst, current list that is used to append one single letter.
	:param sum_lst: lst, summarized list that is used to record all the words in the boggle game.
	:param d_lst: lst, the whole dictionary
	:param cur_num: The current position on the boggle game index. 0-15
	:param boggle_lst: Index 1, 2, 5, 6, 9, 10, 13, 14. Index that doesn't have to change row.
	:param boggle_lst_left: Index 0, 4, 8, 12. Index on the left.
	:param boggle_lst_right: Index 0, 4, 8, 12. Index on the right.
	:param cur_num_helper: lst, a list that records the track number(0-15) that the word had gone through.
	'''
	if has_prefix(''.join(cur_lst), d_lst) is False:  # BASE CASE! If the current list will not be able to form a letter.
		pass
	else:
		if ''.join(cur_lst) in d_lst and ''.join(cur_lst) not in sum_lst:
			# If the current list is in the dictionary and also has not appeared yet.
			print('Found: ' + ''.join(cur_lst))
			sum_lst.append(''.join(cur_lst))
		if cur_num in [0, 4, 8, 12]:
			for num in boggle_lst_left:
				if -1 < num + cur_num < 16 and cur_num + num not in cur_num_helper:
					# num + cur_num should stay in between 0-15, which is the 4x4 boggle game.
					# cur_num + num not in cur_num_helper: To make sure not to fall back to a index already visited.
					cur_lst.append(alpha[cur_num + num])
					cur_num_helper.append(cur_num + num)
					boggle_game_helper(alpha, cur_lst, sum_lst, d_lst, num + cur_num, boggle_lst,
									   boggle_lst_left, boggle_lst_right, cur_num_helper)
					cur_lst.pop()
					cur_num_helper.pop()
		elif cur_num in [3, 7, 11, 15]:
			for num in boggle_lst_right:
				if -1 < num + cur_num < 16 and cur_num + num not in cur_num_helper:
					cur_lst.append(alpha[cur_num + num])
					cur_num_helper.append(cur_num + num)
					boggle_game_helper(alpha, cur_lst, sum_lst, d_lst, num + cur_num, boggle_lst,
									   boggle_lst_left, boggle_lst_right, cur_num_helper)
					cur_lst.pop()
					cur_num_helper.pop()
		else:
			for num in boggle_lst:
				if -1 < num + cur_num < 16 and cur_num + num not in cur_num_helper:
					cur_lst.append(alpha[cur_num + num])
					cur_num_helper.append(cur_num + num)
					boggle_game_helper(alpha, cur_lst, sum_lst, d_lst, num + cur_num, boggle_lst,
									   boggle_lst_left, boggle_lst_right, cur_num_helper)
					cur_lst.pop()
					cur_num_helper.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	d_lst = []
	with open(FILE, 'r') as f:
		for line in f:
			words = line.split()
			words_str = ''.join(words)
			if len(words_str) >= 4:
				d_lst.append(words_str)
	return d_lst


def has_prefix(sub_s, d_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for alpha in d_lst:
		if alpha.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
