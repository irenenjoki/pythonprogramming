thisdict =	{
  "name": "john",
  "email": "johnming@gmail.com",
  "age": 19,
  "DOB":2000,
  "school":"mangu"
}
x = thisdict.keys()
print(x)
#prints keys which are(name,email,age,DOB,school)#
y = thisdict.values()
print(y)
#prints out values which are(john,johnming@gmail.com,19,2000,mangu)#
z = thisdict.items()
print(z)
#print out everything in the dictionary#
a = thisdict["name"]
print(a)
#prints out the name john#
b = thisdict.get("age")
print(b)
#prints out the age of john#
thisdict["address"] = "New York"
print(thisdict)
#adds address to the dictionary#
thisdict["DOB"] = 2001
print(thisdict)
#changes the date of birth#
thisdict.update({"DOB": 2002})
print(thisdict)
#updates date of birth#
thisdict.pop("school")
print(thisdict)
#removes school from the dictionary#

