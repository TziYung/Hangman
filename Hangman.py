import random
word=input('Please enter the word\n').lower()
wordlist=['_' for n in range(len(word))]
pic=['O','|','/','\\','/','\\']
graph=[' ' for n in range(6)]

fail=0
used=[]
while ''.join(wordlist)!=word and fail<6:
    character=input('please enter a character').lower()
    if len(character)!=1:
        print('you can only enter a character in one time')
    elif ord(character)<97 or ord(character)>122:
        print('you can only enter an alphabet')
    else:
        if word.count(character):
            for a in range(len(word)):
                if character==word[a]:
                    wordlist[a]=character
        else:
            fail+=1
            used.append(character)
            graph[fail-1]=pic[fail-1]
        hanging=f'''
   ------
   {graph[0]}    |
  {graph[2]}{graph[1]}{graph[3]}   |
  {graph[4]} {graph[5]}   |
        |
        '''
        print(wordlist)
        print(hanging)
        print(used)
        
if ''.join(wordlist)==word:        
    print('congratulation, you have win the game')
else: 
    print('you failed')
