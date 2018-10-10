#prompt user to enter 2 words

word1 = input('enter first word :')
word2 = input('enter 2nd word :')

#transform 2 words into 2 lists of their own letters

wordlist1 = [ch for ch in word1]
wordlist2 = [ch for ch in word2]

#sort the lists alphabetically. making an easy comparison since the orders of the letters aren't of concerns 

wordlist1.sort()
wordlist2.sort()

#output result using an if statement

if wordlist1 == wordlist2:
    print('both words are anagrams of one another')



