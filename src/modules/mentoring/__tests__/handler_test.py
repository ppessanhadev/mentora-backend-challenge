def test_mentoring_route(client):
    response = client.get("/api/mentoring")
    print(response)
    assert response.status_code == 200
