# lambda

def add(a,b):
    return a + b

add_by_Lambda=lambda x, y: x + y

# ----------------------------------------------------------------

# MAP
def add_to_mark(mark):
    if mark>=90:
        return min(mark+5,100)
    elif mark>=80:
        return min(mark+3,90)
    elif mark>=80:
        return min(mark+1,80)
    else:
        return mark+2
    
    
marks=[95,100,100,70,85,91,55]

newMarks=[]

for i in marks:
    newMarks.append(add_to_mark(i))
    
print(newMarks)

print(list(map (add_to_mark,marks)))

# ----------------------------------------------------------------

# Filter

print(list(filter(lambda x: x<90,marks)))


# ----------------------------------------------------------------

# reduce

from functools import reduce


result =reduce(lambda x,y:x+y,marks)
print(result)


# ----------------------------------------------------------------

# reduce