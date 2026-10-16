"""Fixtures for the S3 tests that need no backend.

A mocked client, for the failures a real endpoint cannot produce on demand
(canned replies: ``tests/s3/fakes.py``). The backend fixtures (``s3``,
``async_s3``, ``bucket``, ...) are in ``tests/conftest.py``.
"""

from __future__ import annotations

from typing import Any

import capo_s3._services._pipeline
import pytest
from capo_s3 import AsyncS3Client, S3Client
from zapros.mock import MockMiddleware, MockRouter

OFFLINE_S3_SETTINGS: dict[str, Any] = {
    "credentials": {"access_key": "AKIDEXAMPLE", "secret_key": "secret"},
    "region": "us-east-1",
    "retry_max_attempts": 3,
}


@pytest.fixture
def no_retry_delay(monkeypatch: pytest.MonkeyPatch) -> None:
    """Retry without the backoff between attempts, for tests that count them."""
    monkeypatch.setattr(capo_s3._services._pipeline, "_retry_delay", lambda attempt, is_throttling: 0.0)


@pytest.fixture
def s3_mocks() -> MockRouter:
    """The mocks behind ``offline_s3`` / ``offline_async_s3``; a request none of them matches fails."""
    return MockRouter()


# The offline clients come unopened: the test opens them (``with offline_s3:``), and closing them
# verifies the mocks' expectations inside the test, where an xfail still applies, not in teardown.
@pytest.fixture
def offline_s3(s3_mocks: MockRouter) -> S3Client:
    return S3Client(http_handler=MockMiddleware(s3_mocks), **OFFLINE_S3_SETTINGS)


@pytest.fixture
def offline_async_s3(s3_mocks: MockRouter) -> AsyncS3Client:
    return AsyncS3Client(http_handler=MockMiddleware(s3_mocks), **OFFLINE_S3_SETTINGS)
