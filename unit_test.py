# unit_test.py

"""Unit tests for the FastAPI main application."""

import unittest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestMainApp(unittest.TestCase):
    """Test case class for testing FastAPI endpoints."""

    def test_generate_name(self):
        """Test generating a name and adding it to the list."""
        response = client.get("/generate_name/John")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Name generated successfully",
                      response.json()["message"])
        self.assertIn("John", response.json()["name"])

    def test_read_names(self):
        """Test reading the list of names."""
        client.get("/generate_name/Alice")  # Add a name for testing
        response = client.get("/read_names")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Alice", response.json()["names"])

    def test_update_name(self):
        """Test updating a name in the list."""
        client.get("/generate_name/Bob")  # Add a name for testing
        response = client.put("/update_name/0", json={"new_name": "Robert"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Name updated successfully", response.json()["message"])

    def test_delete_name(self):
        """Test deleting a name from the list."""
        client.get("/generate_name/Charlie")  # Add a name for testing
        response = client.delete("/delete_name/0")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Name deleted successfully", response.json()["message"])

    def test_calculate_sin(self):
        """Test calculating the sine of a number."""
        number = 0
        response = client.get(f"/calculate_sin/{number}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["sin"], 0)

    def test_calculate_cos(self):
        """Test calculating the cosine of a number."""
        number = 0
        response = client.get(f"/calculate_cos/{number}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["cos"], 1)

    def test_generate_random_number(self):
        """Test generating a random number within a specified range."""
        response = client.get("/generate_random_number?start=5&end=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["random_number"], 5)


if __name__ == "__main__":
    unittest.main()
