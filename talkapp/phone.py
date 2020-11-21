import nltk
phn = nltk.corpus.cmudict.dict()
 
def to_phoneme(string):
	sr = string.split()
	f = open("datasets/phoneme.txt","w")

	for word in sr:
		try:
			for j in phn[word][0]:
				f.write(str(j)+' ')
			
		except Exception as e:
			f.write(str(e))

		f.write('\n')

