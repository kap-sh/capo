"""How waiters treat what the polled operation returns."""

from __future__ import annotations

import pytest
from capo_s3 import AsyncS3Client, S3Client
from capo_s3.errors import ServiceError
from zapros.mock import Mock, MockRouter

from tests.s3.fakes import HEAD_OBJECT, reply


class TestAsyncWaiters:  # unasync: generate
    async def test_waiter_fails_on_an_error_no_acceptor_matches(
        self,
        offline_async_s3: AsyncS3Client,
        s3_mocks: MockRouter,
    ):
        s3_mocks.add(Mock.given(HEAD_OBJECT).callback(reply(403)).once())
        async with offline_async_s3:
            with pytest.raises(ServiceError):
                await offline_async_s3.wait_until_object_exists("bucket", "key", max_wait_time=2)


class TestWaiters:  # unasync: generated
    def test_waiter_fails_on_an_error_no_acceptor_matches(
        self,
        offline_s3: S3Client,
        s3_mocks: MockRouter,
    ):
        s3_mocks.add(Mock.given(HEAD_OBJECT).callback(reply(403)).once())
        with offline_s3:
            with pytest.raises(ServiceError):
                offline_s3.wait_until_object_exists("bucket", "key", max_wait_time=2)
