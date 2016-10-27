'''
Created on Oct 26, 2016 2:32:28 PM

@author: Pati Ram Yadav

@Path: C:\JavaDev\Eclipse Mars.2 (4.5.2)\plugins\org.python.pydev_5.2.0.201608171824\pysrc\pydevd.py

@Module: context_managers.contextmanager_with

'''
with open("any_file.txt", "w") as a:
    for line in a:
        print(line)
    

# "with" is context manager, cares to  open and close the file

# Alternative to with
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
    

