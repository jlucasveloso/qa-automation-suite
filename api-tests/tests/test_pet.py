from utils.api_client import APIClient

client = APIClient()

PET_ID = 999888777
PET_PAYLOAD = {
    "id": PET_ID,
    "name": "Buddy",
    "status": "available",
    "category": {"id": 1, "name": "Dogs"},
    "photoUrls": ["https://example.com/photo.jpg"],
    "tags": [{"id": 1, "name": "friendly"}],
}


class TestPet:
    def test_add_pet(self):
        res = client.post("/pet", json=PET_PAYLOAD)
        assert res.status_code == 200
        data = res.json()
        assert data["id"] == PET_ID
        assert data["name"] == "Buddy"
        assert data["status"] == "available"

    def test_get_pet_by_id(self):
        res = client.get(f"/pet/{PET_ID}")
        assert res.status_code == 200
        assert res.json()["id"] == PET_ID

    def test_update_pet(self):
        updated = {**PET_PAYLOAD, "name": "Buddy Updated", "status": "sold"}
        res = client.put("/pet", json=updated)
        assert res.status_code == 200
        data = res.json()
        assert data["name"] == "Buddy Updated"
        assert data["status"] == "sold"

    def test_find_pets_by_status(self):
        for status in ["available", "pending", "sold"]:
            res = client.get("/pet/findByStatus", params={"status": status})
            assert res.status_code == 200
            assert isinstance(res.json(), list)

    def test_update_pet_with_form(self):
        s = client.session
        res = s.post(
            f"{client.base_url}/pet/{PET_ID}",
            data={"name": "FormBuddy", "status": "pending"},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        assert res.status_code == 200

    def test_delete_pet(self):
        res = client.delete(f"/pet/{PET_ID}")
        assert res.status_code in (200, 404)

    def test_get_deleted_pet_returns_404(self):
        res = client.get(f"/pet/{PET_ID}")
        assert res.status_code == 404