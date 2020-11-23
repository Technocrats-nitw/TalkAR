import nltk



#string = "Technocrats will surely win OIC tomorrow."
 


def to_phoneme(string):
	phn = nltk.corpus.cmudict.dict()
	sr = string.split()
	f = open("phoneme.txt","w")

	for word in sr:
		try:
			for j in phn[word][0]:
				f.write(str(j)+' ')
			
		except Exception as e:
			f.write(str(e))

		f.write('\n')

	

#to_phoneme(string)

