#!/usr/bin/env python
# encoding: utf-8
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\telugu\\tewiki.txt','r')
f2 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\telugu\\replaced.txt','w')
dict=[]
pure=[]
counter=0


for line in f1:
	#dict.append(line)#array for word
	line = line.replace('a','')
	line = line.replace('b','')
	line = line.replace('c','')
	line = line.replace('d','')
	line = line.replace('e','')
	line = line.replace('f','')
	line = line.replace('g','')
	line = line.replace('h','')
	line = line.replace('i','')
	line = line.replace('j','')
	line = line.replace('k','')
	line = line.replace('l','')
	line = line.replace('m','')
	line = line.replace('n','')
	line = line.replace('o','')
	line = line.replace('p','')
	line = line.replace('q','')
	line = line.replace('r','')
	line = line.replace('s','')
	line = line.replace('t','')
	line = line.replace('u','')
	line = line.replace('v','')
	line = line.replace('w','')
	line = line.replace('x','')
	line = line.replace('y','')
	line = line.replace('z','')
	line = line.replace('A','')
	line = line.replace('B','')
	line = line.replace('C','')
	line = line.replace('D','')
	line = line.replace('E','')
	line = line.replace('F','')
	line = line.replace('G','')
	line = line.replace('H','')
	line = line.replace('I','')
	line = line.replace('J','')
	line = line.replace('K','')
	line = line.replace('L','')
	line = line.replace('M','')
	line = line.replace('N','')
	line = line.replace('O','')
	line = line.replace('P','')
	line = line.replace('Q','')
	line = line.replace('R','')
	line = line.replace('S','')
	line = line.replace('T','')
	line = line.replace('U','')
	line = line.replace('V','')
	line = line.replace('W','')
	line = line.replace('X','')
	line = line.replace('Y','')
	line = line.replace('Z','')
	line = line.replace('>','')
	line = line.replace('!','')
	line = line.replace('@','')
	line = line.replace('#','')
	line = line.replace('$','')
	line = line.replace('%','')
	line = line.replace('^','')
	line = line.replace('&','')
	line = line.replace('*','')
	line = line.replace('(','')
	line = line.replace(')','')
	line = line.replace(';','')
	line = line.replace(':','')
	line = line.replace('"','')
	line = line.replace('>','')
	line = line.replace('<','')
	line = line.replace('||','')
	line = line.replace('1','')
	line = line.replace('2','')
	line = line.replace('3','')
	line = line.replace('4','')
	line = line.replace('5','')
	line = line.replace('6','')
	line = line.replace('7','')
	line = line.replace('8','')
	line = line.replace('9','')
	line = line.replace('0','')
	line = line.replace(',','')
	line = line.replace('.','')
	line = line.replace('+','')
	line = line.replace('=','')
	line = line.replace('-','')
	line = line.replace('[','')
	line = line.replace(']','')
	line = line.replace('{','')
	line = line.replace('}','')
	line = line.replace('|','')
	line = line.replace('//','')
	line = line.replace('?','')
	line = line.replace('/','')
	line = line.replace('_','')
	#line = line.replace('','')
	
	
	pure.append(line)
for line in pure:
	f2.write(line)
	counter=counter+1
	print counter