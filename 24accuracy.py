#24accuracy.py by Sophia Chen & Devin Fan

def acc_f1(tp, fp, tn, fn):
	acc = (tp + tn) / (tp + tn + fp + fn)
	prec = tp / (tp + fp)
	sens = tp / (tp + fn)
	f1 = (2 * prec * sens) / (prec + sens)
	print('Your accurary is', round(acc, 2), 'and your F1 score is', round(f1, 2))
	return acc, f1
	
acc_f1(5, 8, 10, 2)
acc_f1(10, 3, 12, 4)
acc_f1(2, 9, 5, 6)