from src.app import activities


def test_root_redirects_to_frontend(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_activity_data(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert expected_activity in response_data
    assert response_data[expected_activity]["participants"] == activities[expected_activity]["participants"]
    assert "description" in response_data[expected_activity]
    assert "schedule" in response_data[expected_activity]
    assert "max_participants" in response_data[expected_activity]
