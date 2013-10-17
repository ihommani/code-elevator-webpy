# Code elevator

Implementation of the code story challenge _The One In The Elevator_. 

Description can be found [here](http://www.code-story.net/blog/posts/s03e01, "code story")
The algorithm is for now simple. 
The elevator treat the demands in the order they arrive. This strategy has some limits in efficiency but works. 

# How to launch the server
To implement the server i use python with web.py framework. The code is tested under python2.7. 
I strongly advise to use wirtualenv to install web.py.
When installed, simply run *python code_elevator.py [port]*
The server will be listening to the specified port.

# Why use web.py
web.py is a simple web framework that allow me to nuke all boiler plate code and configuration files we can found when using server such as Tomcat or Jetty.
It's perfectly rounded for small projects like this, and according the documentation for more.
Despite a [documentation](http://webpy.org/, "webpy") not really up to date, i enjoyed to focus myself on the algorithm rather than spending time to configure and build a small instance of tomcat server. 


Cheer
