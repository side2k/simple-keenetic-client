import pytest

from .fixtures import *  # noqa


@pytest.mark.asyncio
async def test_client_login(client_with_mocked_session):
    async with client_with_mocked_session:
        pass


@pytest.mark.asyncio
async def test_client_fails_on_unknown_auth_method(client_with_mocked_session):
    unsupported_method = "unsupported-method"
    client_with_mocked_session._mocked_session.get.return_value.headers["WWW-Authenticate"] = (
        f"{unsupported_method} "
    )
    try:
        async with client_with_mocked_session:
            pass

    except Exception as exc:
        [msg] = exc.args
        assert unsupported_method in msg
