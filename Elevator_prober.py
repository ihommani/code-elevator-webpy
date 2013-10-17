#! /usr/bin/env python

import unittest
from Elevator import elevator

class TestElevator(unittest.TestCase):
    
    def setUp(self):
        self.elevator = elevator()

    def test_elevator_should_be_closed(self):
        self.assertTrue(self.elevator.isClosed())

    def test_elevator_should_be_opened(self):
        self.elevator.openDoor()
        self.assertTrue(self.elevator.isOpen())

    def test_elevator_should_be_at_ground_zero(self):
        self.assertEqual(self.elevator.getCurrentFloor(), 0)

    def test_elevator_should_go_to_floor_x(self):
        self.elevator.call(5)
        self.assertEqual(self.elevator.getCurrentFloor(), 5)

    def test_elevator_should_be_empty(self):
        self.assertEqual(self.elevator.userExit(), 0)

    def test_elevator_should_contain_one_more_user(self):
        first = self.elevator.userEntrance()
        second = self.elevator.userEntrance()
        self.assertEqual(second, first + 1)

    def test_elevator_should_contain_one_less_user(self):
        first = self.elevator.userEntrance()
        second = self.elevator.userEntrance()
        third = self.elevator.userExit()
        self.assertEqual(third, second - 1)

    def test_elevator_cannot_go_below_0(self):
        self.assertEqual(self.elevator.call(-6), 0)
        return

    def test_elevator_cannot_go_below_0(self):
        #self.assertEqual(self.elevator.call(-6), 0)
        return
    
    def test_should_return_NOTHING(self):
        self.assertEqual(self.elevator.getNextMove(), "NOTHING")
        
    def test_elevator_should_compute_next_command(self):
        self.elevator.call(5)
        self.elevator.call(3)
        self.elevator.call(3)
        self.assertEqual(self.elevator.getNextMove(), "UP")
        self.assertEqual(self.elevator.getNextMove(), "UP")
        self.assertEqual(self.elevator.getNextMove(), "UP")
        self.assertEqual(self.elevator.getNextMove(), "UP")
        self.assertEqual(self.elevator.getNextMove(), "UP")
        self.assertEqual(self.elevator.getNextMove(), "OPEN")
        self.assertEqual(self.elevator.getNextMove(), "CLOSE")
        self.assertEqual(self.elevator.getNextMove(), "DOWN")
        self.assertEqual(self.elevator.getNextMove(), "DOWN")
        self.assertEqual(self.elevator.getNextMove(), "OPEN")
        self.assertEqual(self.elevator.getNextMove(), "NOTHING")
        
    def test_should_compute_go_command(self):
         self.elevator.call(5)
         self.elevator.go(3)
         self.elevator.call(4)
         self.elevator.go(1)
         self.elevator.go(5)
         self.assertEqual(self.elevator.getNextMove(), "UP")
         self.assertEqual(self.elevator.getNextMove(), "UP")
         self.assertEqual(self.elevator.getNextMove(), "UP")
         self.assertEqual(self.elevator.getNextMove(), "UP")
         self.assertEqual(self.elevator.getNextMove(), "UP")
         self.assertEqual(self.elevator.getNextMove(), "OPEN")
         self.assertEqual(self.elevator.getNextMove(), "CLOSE")
         self.assertEqual(self.elevator.getNextMove(), "DOWN")
         self.assertEqual(self.elevator.getNextMove(), "DOWN")
         self.assertEqual(self.elevator.getNextMove(), "OPEN")
         self.assertEqual(self.elevator.getNextMove(), "CLOSE")
         self.assertEqual(self.elevator.getNextMove(), "UP")
         self.assertEqual(self.elevator.getNextMove(), "OPEN")
         self.assertEqual(self.elevator.getNextMove(), "CLOSE")
         self.assertEqual(self.elevator.getNextMove(), "DOWN")
         self.assertEqual(self.elevator.getNextMove(), "DOWN")
         self.assertEqual(self.elevator.getNextMove(), "DOWN")
         self.assertEqual(self.elevator.getNextMove(), "OPEN")
         self.assertEqual(self.elevator.getNextMove(), "CLOSE")
         self.assertEqual(self.elevator.getNextMove(), "UP")
         self.assertEqual(self.elevator.getNextMove(), "UP")
         self.assertEqual(self.elevator.getNextMove(), "UP")
         self.assertEqual(self.elevator.getNextMove(), "UP")


if __name__ == '__main__':
    unittest.main()
