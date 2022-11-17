# 1.
halmaz=set(['epre','kurte','fa'])
halmaz.clear()
print(halmaz)

#2.
halmaz=set(['epre','kurte','fa'])
halmaz2=halmaz.copy()
print(halmaz2)

#3.
halmaz1=set(['banán','kesztyü','google'])
halmaz2=set(['microsoft','google','kürt'])

kulonbseg=halmaz1.difference(halmaz2)
print(kulonbseg)

#4.
halmaz1=set(['eper','kürt',':)'])
halmaz2=set(['kürt','google','eper'])
halmaz1.difference_update(halmaz2)

print(halmaz1)

# 5.
halmaz1=set(['banán','kesztyű','google','távcső'])
halmaz2=set(['microsoft','google','kürt','kabát'])

metodús=halmaz1.intersection(halmaz2)
print(metodús)

#A végeredmény az ami a kettő halmaz között megegyezik

# 6.
halmaz1=set(['baan','kesztyű','google','microsoft'])
halmaz2=set(['microsoft','google','kürt','Labda'])

halmaz3 =halmaz1.intersection_update(halmaz2)

halmaz1.discard(halmaz3)
halmaz2.discard(halmaz3)

print(halmaz1)
print(halmaz2)

# 7.
halmaz1=set(['banán','kesztyű','alma'])
halmaz2=set(['kürt','kesztyű','alma','golyó'])

halmaz=halmaz1.isdisjoint(halmaz2)

print(halmaz)

# 8.
halmaz1=set(['a','b','c'])
halmaz2=set(['a','b','c','d','f','g'])

halmaz=halmaz1.issubset(halmaz2)

print(halmaz)

# 9.
halmaz1=set(['a','b','c','d','f','g'])
halmaz2=set(['a','b','c'])

halmaz=halmaz1.issuperset(halmaz2)

print(halmaz)

# 10.
halmaz1=set(['banan','mikró','alma'])
halmaz2=set(['mikró','labda','kürt'])

halmaz=halmaz1.symmetric_difference(halmaz2)

print(halmaz)

# 11.
# symmetric_difference_update():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#pop:
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

# union:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

#add
gyümölcsök = {"alma", "banán", "cseresznye"}
gyümölcsök.add("narancs")

print(gyümölcsök)

#discard
gyümölcsök= {"alma", "banán", "cseresznye"}

gyümölcsök.discard("banán")

print(gyümölcsök)

#remove
gyümölcsök = {"alma", "banán", "cseresznye"}

gyümölcsök.remove("banán")

print(gyümölcsök)