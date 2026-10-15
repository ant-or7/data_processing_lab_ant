word=input("Enter a word or short sentence")
vowels='aeiou'
count=0
vcount=0
scount=0
for x in word:
    count+=1
    if x.lower() in vowels:
        vcount+=1
    elif x==' ':
        scount+=1

print(f"Vowel count:             {vcount}")
print(f"Space count:             {scount}")
print(f"Total Character count:   {count}")