#! /usr/bin/python

import web

from Elevator import elevator

urls = (
    '/call', 'call',
    '/go', 'go', 
    '/userHasEntered', 'userHasEntered', 
    '/userHasExited', 'userHasExited', 
    '/reset', 'reset', 
    '/nextCommand', 'nextCommand', 
)

app = web.application(urls, globals())
elevator = elevator()

class call:        
    def GET(self):
        atFloor = web.input().get('atFloor')
        elevator.call(atFloor)
        return web.http.web.OK

class go:
    def GET(self):
        toFloor = web.input().get('floorToGo')
        elevator.go(toFloor)
        return web.http.web.OK

class userHasEntered:
    def GET(self):
        elevator.userEntrance()
        return web.http.web.OK

class userHasExited:
    def GET(self):
        elevator.userExit()
        return web.http.web.OK

class nextCommand:
    def GET(self):
        return elevator.getNextMove()

class reset:
    def GET(self): 
        elevator.reset()
        return web.http.web.OK

if __name__ == "__main__":
    app.run()
