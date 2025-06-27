#  Count how many vowels are in a tuple
t1=("a","b","i","t","u")
vowelscount=0
for ch in t1:
        if ch in ("a","e","i","o","u"):
             vowelscount+=1
             print(vowelscount)
# Tuple of tuples (Nested tuple loop)
Students=("Ali",3.5),("Fatima",3.3),("Hasan",3.5)
for Student in Students:
       name,GPA=Student

print(f"{name} scored {GPA}")
      