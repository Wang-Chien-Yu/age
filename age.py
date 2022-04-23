driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit
age = input('請輸入你得年齡')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('你違法了')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考駕照了')
	else:
		print('加油，過幾年就可以去考了')