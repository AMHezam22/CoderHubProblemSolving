# https://coderhub.sa/challenge/44be3e9f-8b91-495d-91f2-c514693ff190
#  Done


def dec_to_any(num, base: int):
	hexi_dict = {
		1: "1", 2: "2", 3: "3",
		4: "4", 5: "5", 6: "6",
		7: "7", 8: "8", 9: "9",
		10: 'A', 11: 'B', 12: 'C',
		13: 'D', 14: 'E', 15: 'F'
	}
	ans = ""
	while num != 0:
		num, temp = divmod(num, base)
		ans += str(temp)
	return ans[::-1]


def oct_to_bin(octi):
	num = int(str(octi), 8)
	ans = dec_to_any(num, 2)
	return ans
