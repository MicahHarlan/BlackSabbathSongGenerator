import random
import sys
n = 100
if len(sys.argv) == 3:
	if int(sys.argv[2]) < 1:
		print("TOO LOW OF VALUE FOR N")
	else:
		n = int(sys.argv[2])
	

f = open(sys.argv[1], encoding='utf-8')
lyrics = f.readlines()

strings = " ".join(lyrics)
strings = strings.lower()
strLyrics = " ".join(lyrics)
strLyrics = strLyrics.replace("?"," ")
strLyrics = strLyrics.replace("\n"," ")
strLyrics = strLyrics.replace('"'," ")
strLyrics = strLyrics.replace(","," ")
strLyrics = strLyrics.lower()
strLyrics = strLyrics.replace("-"," ")
strLyrics = strLyrics.replace("."," ")
strLyrics = strLyrics.replace(":"," ")
strLyrics = strLyrics.replace(";"," ")
strLyrics = strLyrics.replace("("," ")
strLyrics = strLyrics.replace(")"," ")
strLyrics = strLyrics.replace("!"," ")
black_sabbath = strLyrics.split(' ') 


#START OF UNIGRAMS
unigrams = {} #empty Dictionary
#This for loop creates a unigram dictionary and counts each word.
for ozzy_token in black_sabbath:
	if ozzy_token != "":

		if unigrams.get(ozzy_token) == None:
			unigrams[ozzy_token] = 1

		else:
			num = unigrams[ozzy_token]
			unigrams[ozzy_token] = num + 1

#Testing the Unigram Model
key = list(unigrams.keys())
val = list(unigrams.values())
sentence = random.choices(key, weights = val, k = n)
str2 =  " ".join(sentence)


#UNCOMMENT
print("UNIGRAMS MODEL")
print(str2)
#UNCOMMENT
print(" ")

#UNIGRAMS END
######################################################
#BIGRAMS START
print("BIGRAMS MODEL")
bigrams = {}
for i in range(len(black_sabbath)):
	if black_sabbath[i] != "" and black_sabbath[i+1] != "":
		#if this bigram doesn't exist

		if bigrams.get(black_sabbath[i]) == None:
			second = {black_sabbath[i+1] :1}
			bigrams[black_sabbath[i]] = second
	
		#If this bigram exists with this word
		elif bigrams.get(black_sabbath[i]) != None:
			existing  = bigrams[black_sabbath[i]]
			#if existing first word doesn't have this second word
			if(existing.get(black_sabbath[i+1]) == None ):
				existing[black_sabbath[i + 1]] = 1
				bigrams[black_sabbath[i]].update(existing)
			else:
			#if this bigram occured already add one to its count
				num = existing[black_sabbath[i+1]]
				existing[black_sabbath[i+1]] = num + 1
				bigrams[black_sabbath[i]] = existing


i = 0
uni = random.choices(key,weights = val, k = 1)
nextWord = " ".join(uni)
song = []
while i < n:
	if bigrams.get(nextWord,None) == None:
		uni = random.choices(key,weights = val, k = 1)
		nextWord = " ".join(uni)
	else:
		temp = bigrams.get(nextWord)     	
		key2 = (list(temp.keys())) 
		vals2 = (list(temp.values()))
		phrase = random.choices(key2, weights = vals2, k = 1)
		song.append(" " + " ".join(phrase))
		nextWord = " ".join(phrase)
		i+= 1

print("".join(song).strip())



#END OF BIGRAMS
######################################################
#START OF TRIGRAMS
trigrams = {} 
for i in range(len(black_sabbath)):
	if black_sabbath[i] != "" and black_sabbath[i+1] != "" and black_sabbath[i+2] != "": 
		#Case 1: First word in trigram doesn't exist
		if trigrams.get(black_sabbath[i]) == None:
			next_two = {black_sabbath[i+1] :{black_sabbath[i+2]:1}} 
			trigrams[black_sabbath[i]] = next_two	

		#Case 2: First word exists, second word doesn't exist.
		elif trigrams.get(black_sabbath[i]) != None:
			first_word = trigrams[black_sabbath[i]]
			
	
			#if second word doesn't exist add it. 
			if first_word.get(black_sabbath[i+1]) == None:
				next_two = {black_sabbath[i+1] :{black_sabbath[i+2]:1}}
				trigrams[black_sabbath[i]].update(next_two)
			#second Word is there third isn't
			elif first_word.get(black_sabbath[i+1]) != None:  
				second_word = trigrams[black_sabbath[i]][black_sabbath[i+1]]				
				#HAS THIRD WORD
				if second_word.get(black_sabbath[i+2]) != None:
					num = second_word[black_sabbath[i+2]]
					trigrams[black_sabbath[i]][black_sabbath[i+1]][black_sabbath[i+2]] = num + 1
				#NO THIRD WORD	  
				elif second_word.get(black_sabbath[i+2]) == None:
					last = {black_sabbath[i+2]: 1}
					trigrams[black_sabbath[i]][black_sabbath[i+1]].update(last)



	
print(" ")
print("TRIGRAMS")
i = 0
uni = random.choices(key,weights = val, k = 1)
nextWord = " ".join(uni)
song = []
while i < n:
	##If no trigram starts with this.
	if trigrams.get(nextWord) == None:		
		uni = random.choices(key,weights = val, k = 1)
		nextWord = " ".join(uni)	
	else: #If there is a trigram
		first = trigrams.get(nextWord) #FIRST WORD
		temp = list(first.keys())	
		second = random.choices(temp) #SECOND WORD	
		third = first.get(second[0]) #RN ITS A DICT
		third_keys = list(third.keys())
		third_vals = list(third.values())
		third = random.choices(third_keys,weights=third_vals, k = 1)
		tri_list = [nextWord,second[0]]
		phrase = " ".join(tri_list)	
		song.append(phrase)
		nextWord = "".join(third[0])
		i = i+1


	

	


print(" ".join(song).strip())
#END OF TRIGRAMS








