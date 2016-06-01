# very simple example of generating a report from data
# assuming each data point looks something like
# (name,currentValue,previousValue,date)
def summarize(x,compare=False):
	# deconstruct data tuple:
	name,current,previous,date = x
	if not compare:
		print("The price of {} closed at {} on {}".format(name,current,date))
	else:
		verb = "increased"
		diff = current - previous
		if diff < 0:
			verb = "decreased"
		print("The price of {} {} {} points on {}".format(name,verb,diff,date))
	