"""Which failed requests the client retries, and when it stops."""

from __future__ import annotations

import itertools

import pytest
from capo_s3 import AsyncS3Client, S3Client
from capo_s3.errors import ServiceError
from zapros.mock import Mock, MockRouter

from tests.s3.fakes import HEAD_OBJECT, LIST_BUCKETS, LIST_BUCKETS_OK, s3_error


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
    async def test_retries_stop_once_the_retry_quota_is_spent(
        self,
        offline_async_s3: AsyncS3Client,
        s3_mocks: MockRouter,
    ):
        # The client's 500-token quota pays for 35 transient retries at 14 tokens each,
        # on top of one attempt per call.
        internal_error = s3_error(500, "InternalError")
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).expect(20 + 35).name("within the quota"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).never().name("beyond the quota"))
        async with offline_async_s3:
            for _ in range(20):
                with pytest.raises(ServiceError):
                    await offline_async_s3.list_buckets()

    @pytest.mark.usefixtures("no_retry_delay")
    async def test_throttling_retries_cost_less_of_the_quota(
        self,
        offline_async_s3: AsyncS3Client,
        s3_mocks: MockRouter,
    ):
        # At 5 tokens each, the same 500 tokens pay for 100 throttling retries.
        slow_down = s3_error(503, "SlowDown")
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(slow_down).expect(60 + 100).name("within the quota"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(slow_down).never().name("beyond the quota"))
        async with offline_async_s3:
            for _ in range(60):
                with pytest.raises(ServiceError):
                    await offline_async_s3.list_buckets()

    @pytest.mark.usefixtures("no_retry_delay")
    async def test_a_retry_that_succeeds_gives_its_tokens_back(
        self,
        offline_async_s3: AsyncS3Client,
        s3_mocks: MockRouter,
    ):
        # Without the refund, 100 retries at 14 tokens would spend the quota by the 36th call.
        replies = itertools.cycle([s3_error(500, "InternalError"), LIST_BUCKETS_OK])
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(lambda request: next(replies)(request)).expect(200))
        async with offline_async_s3:
            for _ in range(100):
                await offline_async_s3.list_buckets()

    @pytest.mark.usefixtures("no_retry_delay")
    async def test_the_retry_quota_is_shared_by_all_operations_of_a_client(
        self,
        offline_async_s3: AsyncS3Client,
        s3_mocks: MockRouter,
    ):
        internal_error = s3_error(500, "InternalError")
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).expect(20 + 35))
        s3_mocks.add(Mock.given(HEAD_OBJECT).callback(internal_error).once().name("head_object, not retried"))
        async with offline_async_s3:
            for _ in range(20):
                with pytest.raises(ServiceError):
                    await offline_async_s3.list_buckets()
            with pytest.raises(ServiceError):
                await offline_async_s3.head_object("bucket", "key")


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
    def test_retries_stop_once_the_retry_quota_is_spent(
        self,
        offline_s3: S3Client,
        s3_mocks: MockRouter,
    ):
        # The client's 500-token quota pays for 35 transient retries at 14 tokens each,
        # on top of one attempt per call.
        internal_error = s3_error(500, "InternalError")
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).expect(20 + 35).name("within the quota"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).never().name("beyond the quota"))
        with offline_s3:
            for _ in range(20):
                with pytest.raises(ServiceError):
                    offline_s3.list_buckets()

    @pytest.mark.usefixtures("no_retry_delay")
    def test_throttling_retries_cost_less_of_the_quota(
        self,
        offline_s3: S3Client,
        s3_mocks: MockRouter,
    ):
        # At 5 tokens each, the same 500 tokens pay for 100 throttling retries.
        slow_down = s3_error(503, "SlowDown")
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(slow_down).expect(60 + 100).name("within the quota"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(slow_down).never().name("beyond the quota"))
        with offline_s3:
            for _ in range(60):
                with pytest.raises(ServiceError):
                    offline_s3.list_buckets()

    @pytest.mark.usefixtures("no_retry_delay")
    def test_a_retry_that_succeeds_gives_its_tokens_back(
        self,
        offline_s3: S3Client,
        s3_mocks: MockRouter,
    ):
        # Without the refund, 100 retries at 14 tokens would spend the quota by the 36th call.
        replies = itertools.cycle([s3_error(500, "InternalError"), LIST_BUCKETS_OK])
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(lambda request: next(replies)(request)).expect(200))
        with offline_s3:
            for _ in range(100):
                offline_s3.list_buckets()

    @pytest.mark.usefixtures("no_retry_delay")
    def test_the_retry_quota_is_shared_by_all_operations_of_a_client(
        self,
        offline_s3: S3Client,
        s3_mocks: MockRouter,
    ):
        internal_error = s3_error(500, "InternalError")
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(internal_error).expect(20 + 35))
        s3_mocks.add(Mock.given(HEAD_OBJECT).callback(internal_error).once().name("head_object, not retried"))
        with offline_s3:
            for _ in range(20):
                with pytest.raises(ServiceError):
                    offline_s3.list_buckets()
            with pytest.raises(ServiceError):
                offline_s3.head_object("bucket", "key")
