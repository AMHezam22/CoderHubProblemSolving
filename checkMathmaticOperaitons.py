def math_expr(expr: str):
	c1 = (expr[0].isalpha())
	c2 = (expr[1] in "+-*/")
	c3 = expr[2].isalpha()
	return c3 and c2 and c1
