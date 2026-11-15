"""Unit tests for Turkce-Bench web dashboard and API endpoints."""

import unittest
from app import app


class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Turkce-Bench", res.data)
        self.assertIn(b"Liderlik Tablosu", res.data)

    def test_api_leaderboard(self):
        res = self.client.get("/api/leaderboard")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "success")
        self.assertIn("models", data)

    def test_api_runs(self):
        res = self.client.get("/api/runs")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "success")
        self.assertIn("runs", data)


if __name__ == "__main__":
    unittest.main()
