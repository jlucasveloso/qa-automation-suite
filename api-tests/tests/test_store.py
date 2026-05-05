from utils.api_client import APIClient

client = APIClient()

ORDER_ID = 5
ORDER_PAYLOAD = {
    "id": ORDER_ID,
    "petId": 1,
    "quantity": 2,
    "shipDate": "2025-01-01T00:00:00.000Z",
    "status": "placed",
    "complete": True,
}


class TestStore:
    def test_get_inventory(self):
        res = client.get("/store/inventory")
        assert res.status_code == 200
        assert isinstance(res.json(), dict)

    def test_place_order(self):
        res = client.post("/store/order", json=ORDER_PAYLOAD)
        assert res.status_code == 200
        data = res.json()
        assert data["id"] == ORDER_ID
        assert data["status"] == "placed"

    def test_get_order_by_id(self):
        res = client.get(f"/store/order/{ORDER_ID}")
        assert res.status_code == 200
        assert res.json()["id"] == ORDER_ID

    def test_delete_order(self):
        res = client.delete(f"/store/order/{ORDER_ID}")
        assert res.status_code in (200, 404)

    def test_get_deleted_order_returns_404(self):
        res = client.get(f"/store/order/{ORDER_ID}")
        assert res.status_code == 404

    def test_invalid_order_id(self):
        res = client.get("/store/order/99999999")
        assert res.status_code == 404