<h3>Singleton Design Pattern</h3>

<dt>Ensuring that one and only one object of the class gets created</dt>
<dt>Providing an access point for an object that is global to the program</dt>
<dt>Controlling concurrent access to resources that are shared</dt>

Concept:<br> Make constructor private and create a static method that does the object initialization. Each time return same existing object.

Problem: <br>Python don't have private constructor.

Goal: <br>Check each time object already exits or not. if yes then return the existing object else create new one

Solution:<br> Use __new__(special method and check whether class have existing instance or not)


Python Concept:<br> when we create an instance of a class then first __new__ method is called and then only __init__ method. This means if we can stop __init__ from being called when we have already an instance then that particular class becomes Singleton. 


More:
Only when __new__ returns the created instance then __init__ gets called. If __new__ does not return an instance then __init__ would not be called. Remember __new__ is always called before __init__.