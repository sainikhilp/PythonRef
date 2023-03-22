
import collections

my_list=[1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3]

Dog = collections.namedtuple('Dog',['name','age','breed'])

sammy=Dog(name='Husky',age=5,breed='Lab')

print(sammy)


