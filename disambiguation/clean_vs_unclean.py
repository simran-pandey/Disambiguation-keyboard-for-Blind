import re
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\disambiguation\\hindib1000.txt','r')
f2 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\disambiguation\\output_56k.txt' ,'r')
f3 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\disambiguation\\outout.txt','w')
dictionary = []
freq= []
dict = []
fre= []

for line in f1:#for every line in swara corpus
    a , b = line.split( )#Each line in Swara corpus splitting into two arrays
    dictionary.append(a)#containing the words
    freq.append(b)#containing the freq
for line in f2:#for every line in swara corpus
    a , b = line.split( )#Each line in Swara corpus splitting into two arrays
    dict.append(a)#containing the words
    fre.append(b)#containing the freq
	
for i in xrange(len(dictionary)):#loop running for full length of array dictionary
	if dictionary[i] not in dict:#if a word in swara corpus matches wiki corpus
		f3.write(dictionary[i])#writing that word to output file
		f3.write(" ")
		f3.write(freq[i])# writing it's frequency infront of it
		f3.write('\n')

f3.close()
	
