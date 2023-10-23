def alpha(*args, **kwargs):
    print(f'args={args}')#args contains a tuple of all positional arguments
    print(f'kwargs={kwargs}')#kwargs is a dictionary with the named arguments

alpha('a',2,None ,x=8,y=22,z=23)
