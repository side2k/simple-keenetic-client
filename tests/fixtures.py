from unittest.mock import AsyncMock, MagicMock

import pytest

from simple_keenetic_client import SimpleKeeneticClient


@pytest.fixture
def client_with_mocked_session(mocker):
    """Returns SimpleKeeneticClient instance with mocked aiohttp.ClientSession object,
    accessible as client.mocked_session
    """
    challenge_headers = {
        "WWW-Authenticate": "x-ndw2-interactive ololo=atata",
        "X-NDM-Realm": "mocked Keenetic",
        "X-NDM-Challenge": "ABCDEF12345",
    }

    mocked_client_session = MagicMock(
        get=AsyncMock(return_value=MagicMock()),
        post=AsyncMock(return_value=MagicMock()),
        delete=AsyncMock(return_value=MagicMock()),
        close=AsyncMock(return_value=MagicMock()),
    )

    mocker.patch(
        "simple_keenetic_client.aiohttp.ClientSession", return_value=mocked_client_session
    )
    client_instance = SimpleKeeneticClient(
        "http://keenetic-router.test", "testuser", "testpassword"
    )
    client_instance._mocked_session = mocked_client_session

    client_instance._mocked_session.get.return_value = MagicMock(headers=challenge_headers)

    return client_instance
