import unittest
from unittest.mock import patch
from app import fetch_user, fetch_posts

class TestApp(unittest.TestCase):

    @patch("app.get_user_from_db")
    def test_fetch_user(self, mock_db):

        mock_db.return_value = {
            "id":1,
            "name":"Harshitha"
        }

        result = fetch_user(1)

        self.assertEqual(result["name"],"Harshitha")
        mock_db.assert_called_once_with(1)


    @patch("app.requests.get")
    def test_fetch_posts(self,mock_get):

        mock_get.return_value.json.return_value=[
            {
                "id":1,
                "title":"Mock Post"
            }
        ]

        posts=fetch_posts()

        self.assertEqual(posts[0]["title"],"Mock Post")
        mock_get.assert_called_once()

if __name__=="__main__":
    unittest.main()