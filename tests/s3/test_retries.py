"""Which failed requests the client retries, and when it stops."""

from __future__ import annotations

import pytest
from capo_s3 import AsyncS3Client, S3Client
from capo_s3.errors import ServiceError
from zapros.mock import Mock, MockRouter

from tests.s3.fakes import LIST_BUCKETS, LIST_BUCKETS_OK, s3_error


class TestAsyncRetries:  # unasync: generate
    @pytest.mark.usefixtures("no_retry_delay")
    async def test_request_timeout_is_retried(self, offline_async_s3: AsyncS3Client, s3_mocks: MockRouter):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(s3_error(400, "RequestTimeout")).once().name("timeout"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(LIST_BUCKETS_OK).once().name("retry"))
        async with offline_async_s3:
            await offline_async_s3.list_buckets()

    @pytest.mark.usefixtures("no_retry_delay")
    async def test_slow_down_is_a_throttling_error(self, offline_async_s3: AsyncS3Client, s3_mocks: MockRouter):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(s3_error(503, "SlowDown")).expect(3))
        async with offline_async_s3:
            with pytest.raises(ServiceError) as raised:
                await offline_async_s3.list_buckets()
        assert raised.value.is_throttling_error

    @pytest.mark.usefixtures("no_retry_delay")
    @pytest.mark.xfail(
        strict=True,
        raises=AssertionError,
        reason="no retry quota (the standard retry mode's token bucket): every call retries up to max_attempts, "
        "however long the service has been failing",
    )
    async def test_retries_stop_once_the_retry_quota_is_spent(
        self,
        offline_async_s3: AsyncS3Client,
        s3_mocks: MockRouter,
    ):
        # Standard retry mode: a 500-token quota at 5 per retry pays for 100 retries in all,
        # on top of one attempt per call.
        internal_error = s3_error(500, "InternalError")
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).expect(121 + 100).name("within the quota"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).never().name("beyond the quota"))
        async with offline_async_s3:
            for _ in range(121):
                with pytest.raises(ServiceError):
                    await offline_async_s3.list_buckets()


class TestRetries:  # unasync: generated
    @pytest.mark.usefixtures("no_retry_delay")
    def test_request_timeout_is_retried(self, offline_s3: S3Client, s3_mocks: MockRouter):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(s3_error(400, "RequestTimeout")).once().name("timeout"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(LIST_BUCKETS_OK).once().name("retry"))
        with offline_s3:
            offline_s3.list_buckets()

    @pytest.mark.usefixtures("no_retry_delay")
    def test_slow_down_is_a_throttling_error(self, offline_s3: S3Client, s3_mocks: MockRouter):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(s3_error(503, "SlowDown")).expect(3))
        with offline_s3:
            with pytest.raises(ServiceError) as raised:
                offline_s3.list_buckets()
        assert raised.value.is_throttling_error

    @pytest.mark.usefixtures("no_retry_delay")
    @pytest.mark.xfail(
        strict=True,
        raises=AssertionError,
        reason="no retry quota (the standard retry mode's token bucket): every call retries up to max_attempts, "
        "however long the service has been failing",
    )
    def test_retries_stop_once_the_retry_quota_is_spent(
        self,
        offline_s3: S3Client,
        s3_mocks: MockRouter,
    ):
        # Standard retry mode: a 500-token quota at 5 per retry pays for 100 retries in all,
        # on top of one attempt per call.
        internal_error = s3_error(500, "InternalError")
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).expect(121 + 100).name("within the quota"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).never().name("beyond the quota"))
        with offline_s3:
            for _ in range(121):
                with pytest.raises(ServiceError):
                    offline_s3.list_buckets()
