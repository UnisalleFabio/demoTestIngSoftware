# tests/test_integration.py

import unittest
from app import TaskManager

class TestTaskManagerIntegration(unittest.TestCase):
    def test_add_task(self):
        manager = TaskManager()
        manager.add_task("Buy groceries", "Milk, eggs, bread")
        self.assertEqual(len(manager.tasks), 1)
        self.assertEqual(manager.tasks[0].title, "Buy groceries")

    def test_complete_task(self):
        manager = TaskManager()
        manager.add_task("Wash car", "Clean the car")
        manager.complete_task(0)
        self.assertTrue(manager.tasks[0].completed)

if __name__ == "__main__":
    unittest.main()
