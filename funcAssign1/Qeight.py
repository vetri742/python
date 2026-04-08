# COUNT THE VOWELS IN A STRING 
def count_vowels(n):
    count=0
    vowels="aeiouAEIOU"
    for i in n:
        if(i in vowels):
            count+=1
    return count

print(count_vowels("virat"))
print(count_vowels("abraham"))



vowels1="aeiouAEIOU"
def check(s):
    count1=0
    for i in s:
        if(i in vowels1):
            count1+=1
    return count1
print(check("vetri"))
    