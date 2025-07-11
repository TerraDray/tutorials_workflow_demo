from django.test import TestCase

from django.urls import reverse
import pytest

@pytest.fixture
def test_user(db, django_user_model):
    user = django_user_model.objects.create_user(
        username="test_username", password="test_password"
    )
    return "test_username", "test_password"  # Or return user if needed

def test_login_user(client, test_user):
    test_username, test_password = test_user
    login_result = client.login(username=test_username, password=test_password)
    assert login_result is True

