#dictionary comprehension
cities=["mumbai","new york","paris"]
countries=["india","usa","france"]
#creat dictionary where key is city and value is country, we can do tihs using
#dictinoary comprehension
#zip will zip two lists together
z=zip(cities,countries)
for a in z:#it will create tuples like ('mumbai', 'india')
    print(a)

#use curly brackets for dic comprehension
d={city:country for city , country in zip(cities,countries)}
print(d)
