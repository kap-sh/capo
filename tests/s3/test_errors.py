"""Turning a response the client cannot decode into one of its own errors."""

from __future__ import annotations

from xml.etree.ElementTree import ParseError

import pytest
from capo_s3 import AsyncS3Client, S3Client
from capo_s3.errors import DeserializationError, UnknownServiceError
from zapros.mock import Mock, MockRouter

from tests.s3.fakes import LIST_BUCKETS, LIST_BUCKETS_OK, PROXY_BODIES, reply


class TestAsyncUndecodableBodies:  # unasync: generate
    @pytest.mark.parametrize("body", PROXY_BODIES)
    @pytest.mark.usefixtures("no_retry_delay")
    async def test_5xx_from_a_proxy_is_retried(
        self,
        offline_async_s3: AsyncS3Client,
        s3_mocks: MockRouter,
        body: bytes,
    ):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(reply(502, body)).once().name("proxy 502"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(LIST_BUCKETS_OK).once().name("retry"))
        async with offline_async_s3:
            await offline_async_s3.list_buckets()

    @pytest.mark.parametrize("body", PROXY_BODIES)
    async def test_4xx_from_a_proxy_is_a_service_error(
        self,
        offline_async_s3: AsyncS3Client,
        s3_mocks: MockRouter,
        body: bytes,
    ):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(reply(403, body)).once())
        async with offline_async_s3:
            with pytest.raises(UnknownServiceError) as raised:
                await offline_async_s3.list_buckets()
        assert raised.value.code is None
        assert isinstance(raised.value.__cause__, ParseError)
        assert raised.value.response.status == 403
        assert not raised.value.is_retryable

    @pytest.mark.parametrize(
        "body",
        [
            pytest.param(b"", id="empty"),
            pytest.param(b"<ListAllMyBucketsResult><Buck", id="truncated"),
        ],
    )
    @pytest.mark.xfail(
        strict=True,
        raises=ParseError,
        reason="handle_response parses a 2xx body without catching the parser's exception",
    )
    async def test_undecodable_success_body_is_a_deserialization_error(
        self,
        offline_async_s3: AsyncS3Client,
        s3_mocks: MockRouter,
        body: bytes,
    ):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(reply(200, body)).once())
        async with offline_async_s3:
            with pytest.raises(DeserializationError):
                await offline_async_s3.list_buckets()


class TestUndecodableBodies:  # unasync: generated
    @pytest.mark.parametrize("body", PROXY_BODIES)
    @pytest.mark.usefixtures("no_retry_delay")
    def test_5xx_from_a_proxy_is_retried(
        self,
        offline_s3: S3Client,
        s3_mocks: MockRouter,
        body: bytes,
    ):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(reply(502, body)).once().name("proxy 502"))
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(LIST_BUCKETS_OK).once().name("retry"))
        with offline_s3:
            offline_s3.list_buckets()

    @pytest.mark.parametrize("body", PROXY_BODIES)
    def test_4xx_from_a_proxy_is_a_service_error(
        self,
        offline_s3: S3Client,
        s3_mocks: MockRouter,
        body: bytes,
    ):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(reply(403, body)).once())
        with offline_s3:
            with pytest.raises(UnknownServiceError) as raised:
                offline_s3.list_buckets()
        assert raised.value.code is None
        assert isinstance(raised.value.__cause__, ParseError)
        assert raised.value.response.status == 403
        assert not raised.value.is_retryable

    @pytest.mark.parametrize(
        "body",
        [
            pytest.param(b"", id="empty"),
            pytest.param(b"<ListAllMyBucketsResult><Buck", id="truncated"),
        ],
    )
    @pytest.mark.xfail(
        strict=True,
        raises=ParseError,
        reason="handle_response parses a 2xx body without catching the parser's exception",
    )
    def test_undecodable_success_body_is_a_deserialization_error(
        self,
        offline_s3: S3Client,
        s3_mocks: MockRouter,
        body: bytes,
    ):
        s3_mocks.add(Mock.given(LIST_BUCKETS).callback(reply(200, body)).once())
        with offline_s3:
            with pytest.raises(DeserializationError):
                offline_s3.list_buckets()
