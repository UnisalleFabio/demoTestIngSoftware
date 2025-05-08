# tests/test_acceptance.py

import unittest
from app import TaskManager

class TestAcceptance(unittest.TestCase):
    def test_full_workflow(self):
        manager = TaskManager()
        
        # Adding tasks
        manager.add_task("Learn Python", "Practice coding")
        manager.add_task("Walk the dog", "Take Max for a walk")
        self.assertEqual(len(manager.tasks), 2)

        # Completing a task
        manager.complete_task(0)
        self.assertTrue(manager.tasks[0].completed)

        # Removing a task
        manager.remove_task(1)
        self.assertEqual(len(manager.tasks), 1)

if __name__ == "__main__":
    unittest.main()
