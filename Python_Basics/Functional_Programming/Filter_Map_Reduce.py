# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

##Using FILTER with Lambda
ini_list = [[1, 2, 3], [1, 2], [1, 2, 3, 4],
                [1, 2, 3, 4, 5], [2, 4, 6]]
ans = list(filter(lambda x : x if(x[0]>1) else None ,ini_list))
print(ans)


## Using MAP with Lambda

animals = ['dog', 'cat', 'parrot', 'rabbit']
 
# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
 
print(uppered_animals)
