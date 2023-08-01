# https://coderhub.sa/challenge/5bd914c3-ab6d-49df-bf9b-5c01ef189974

def dec_to_any(num, base: int):
	hexi_dict = {
		1: "1", 2: "2", 3: "3",
		4: "4", 5: "5", 6: "6",
		7: "7", 8: "8", 9: "9",
		10: 'A', 11: 'B', 12: 'C',
		13: 'D', 14: 'E', 15: 'F'
	}
	ans = ""
	if base == 16:
		while num != 0:
			num, temp = divmod(num, base)
			ans += hexi_dict[temp]
	else:
		while num != 0:
			num, temp = divmod(num, base)
			ans += str(temp)
	return ans[::-1]


def bin_to_oct(b):
	num = int(b,2)
	ans = dec_to_any(num,8)
	return ans


print(bin_to_oct("10011100"))

