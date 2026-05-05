from utils.api_client import APIClient

client = APIClient()

USERNAME = "qa_autouser_42"
USER_PAYLOAD = {
    "id": 42,
    "username": USERNAME,
    "firstName": "QA",
    "lastName": "Automation",
    "email": "qa@automation.com",
    "password": "Test@123",
    "phone": "11999999999",
    "userStatus": 1,
}


class TestUser:
    def test_create_user(self):
        res = client.post("/user", json=USER_PAYLOAD)
        assert res.status_code == 200

    def test_create_users_with_array(self):
        users = [
            {**USER_PAYLOAD, "id": 43, "username": "qa_user_array_1"},
            {**USER_PAYLOAD, "id": 44, "username": "qa_user_array_2"},
        ]
        res = client.post("/user/createWithArray", json=users)
        assert res.status_code == 200

    def test_create_users_with_list(self):
        users = [
            {**USER_PAYLOAD, "id": 45, "username": "qa_user_list_1"},
            {**USER_PAYLOAD, "id": 46, "username": "qa_user_list_2"},
        ]
        res = client.post("/user/createWithList", json=users)
        assert res.status_code == 200

    def test_login(self):
        res = client.get("/user/login", params={"username": USERNAME, "password": "Test@123"})
        assert res.status_code == 200
        assert "logged in" in res.json().get("message", "").lower()

    def test_get_user(self):
        res = client.get(f"/user/{USERNAME}")
        assert res.status_code == 200
        assert res.json()["username"] == USERNAME

    def test_update_user(self):
        updated = {**USER_PAYLOAD, "firstName": "Updated"}
        res = client.put(f"/user/{USERNAME}", json=updated)
        assert res.status_code == 200

    def test_logout(self):
        res = client.get("/user/logout")
        assert res.status_code == 200

    def test_delete_user(self):
        res = client.delete(f"/user/{USERNAME}")
        assert res.status_code in (200, 404)