#CREATE A TEXT FILE.

f=open("D:\\sqlite\\dbms\\data\\python01.txt","w")

#WRITE 15 LINES FROM THE USER

line=[]
while True:
    l=input()
    if l:
        line.append(l+"\n")
    else:
        break
text="\n".join(line)
f.writelines(line)
f.close()

#TAKE USER INPUT WORD WHICH YOU WANT TO FIND, AND REPLACE IT WITH APPROPRIATE REPLACEMENT WORD

f=open("D:\\sqlite\\dbms\\data\\python01.txt","r")
l=f.read()
word_find=input("Enter the word you want to find : ")
replacement_word=input(f"Enter the word to replace '{word_find}' with : ")

#REPLACE THE WORD IN THE CONTENT WITH THE USE OF "REPLACE()"

updated_word=l.replace(word_find,replacement_word)
f.close()

#WRITE THE UPDATED WORD BACK TO THE FILE

f=open("D:\\sqlite\\dbms\\data\\python01.txt","w")
f.write(updated_word)
f.close()
f=open("D:\\sqlite\\dbms\\data\\python01.txt","r")
w=f.read()
print(w)
f.close()
