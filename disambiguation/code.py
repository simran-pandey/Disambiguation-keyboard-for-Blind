import re
f1 = open('C:\\Users\\pande\\Desktop\\IDC\\disambiguation\\india_wiki.txt','r')#Wiki file
f2 = open('C:\\Users\\pande\\Desktop\\IDC\\disambiguation\\corpus_1k.txt','r')#Swarachakra Corpus
f3 = open('C:\\Users\\pande\\Desktop\\IDC\\disambiguation\\out.txt','w')#unique words in wiki
f4 = open('C:\\Users\\pande\\Desktop\\IDC\\disambiguation\\output.txt','w')#Matched correct words
f5 = open('C:\\Users\\pande\\Desktop\\IDC\\disambiguation\\output2.txt','w')#unmatched incorrect words
dictionary = []
freq= []
words = []
wiki=[]
counter =0
ctr =0
for line in f2:#for every line in swara corpus
    a , b = line.split( )#Each line in Swara corpus splitting into two arrays
    dictionary.append(a)#containing the words
    freq.append(b)#containing the freq
for line in f1:#for every line in wiki corpus
    words = words + line.split()#split a string into a list
words = set(words)#return unique words from the text file

for i in xrange(len(words)):#loop running for full length of array dictionary
     for char in words:
      if char.isalpha():#if a word in swara corpus matches wiki corpus
			f3.write(words[i])#writing that word to output file
			f3.write('\n')
			ctr = ctr+1
			print ctr


#for word in words:
    #words = regexprep(words,'a.*','')
	#f3.write(word)#writing unique words to file out
	#f3.write('\n')
	#counter = counter+1
	#print counter
f3.close()
f6 = open('C:\\Users\\pande\\Desktop\\IDC\\disambiguation\\out.txt','r')



for i in xrange(len(dictionary)):#loop running for full length of array dictionary
 if dictionary[i] in words:#if a word in swara corpus matches wiki corpus
		f4.write(dictionary[i])#writing that word to output file
		f4.write(" ")
		f4.write(freq[i])# writing it's frequency infront of it
		f4.write('\n')
		ctr = ctr+1
		print ctr
		
 elif dictionary[i] not in words:#if a word in swara corpus matches wiki corpus
		f5.write(dictionary[i])#writing that word to output file
		f5.write(" ")
		f5.write(freq[i])# writing it's frequency infront of it
		f5.write('\n')
f4.close()
f5.close()
