def readTickSummary(lines, index):
	if(index+1>len(lines)):
		return index+1

	line = lines[index].strip().split('\t')
	count = 0
	while(1):
		count+=1
		# print(line)
		index = index+1
		line = lines[index].strip().split('\t')

		if ("Market Quantity-Cumul" in line[0]):
			results = map(float, line[1:14])
			print((results[0]-results[6])/(results[0]+1))
			print("market tightness")

			next_line = lines[index+1].strip().split('\t')
			our_results = map(float, next_line[1:14])
			print(our_results[0]/(results[0]+1))
			print("Percentage we targeted")

			print(our_results[0]/(results[6]+1))
			print("percentage targetted in our bins")

			print(results[0])
			print("total trades")
			break

	return index


def main():

	f = open('/home/trader/Desktop/Summary/NIFTY', "r")
	lines = f.readlines()
	f.close()

	count = -1
	for line in lines:
		
		count+=1
		line = line.strip().split('\t')
		
		if(not not line and "Tick Summary" in line[0] and "51101" in line[0]):
			readTickSummary(lines, count+1)
			print(lines[count-1])
			if (count>=len(lines)):
				break
			continue
		
		if (count>=len(lines)):
			break



	'''with open('/home/trader/Desktop/Summary/NIFTY','r') as tsvfile:
					tsvreader = csv.reader(tsvfile, delimiter="\t")
			
					count = 0
					print(type(tsvreader))
					for line in tsvreader:
						if(not not line and "Delta" in line[0]):
							print(line)
						count+=1
			
					print(count)
					print("here")'''

if __name__ == "__main__":
	main()