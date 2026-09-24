"""Credentials and request signing against real AWS endpoints.

The credentials tests are free but need an AWS identity: they run when the
active profile resolves and skip otherwise. The unsigned-payload tests write
to a real EBS snapshot and are paid.
"""

from __future__ import annotations

import base64
import hashlib
import os
import time
from collections.abc import Iterator
from pathlib import Path

import anyio
import pytest
from capo_ebs import AsyncEBSClient, Body, EBSClient
from capo_ec2 import AsyncEC2Client, EC2Client
from capo_iam import (
    AsyncIAMClient,
    ChainedProvider,
    Credentials,
    EnvCredentialsProvider,
    IAMClient,
    ProfileCredentialsProvider,
    SsoCredentialsProvider,
)
from capo_sts import AsyncSTSClient, STSClient
from capo_sts.errors import UnknownServiceError
from zapros import AsyncClient, Client

from tests.conftest import AWS_REGION

BLOCK = 512 * 1024  # the only block size PutSnapshotBlock accepts
BLOCK_0 = os.urandom(BLOCK)
BLOCK_1 = os.urandom(BLOCK)


def sha256_b64(data: bytes) -> str:
    return base64.b64encode(hashlib.sha256(data).digest()).decode()


@pytest.fixture(scope="session")
def aws_credentials() -> Credentials:
    """Credentials of the active profile, or a skip when there are none."""
    chain = ChainedProvider(EnvCredentialsProvider(), SsoCredentialsProvider(Client()), ProfileCredentialsProvider())
    try:
        return chain.resolve_identity()
    except Exception as exc:  # each provider raises its own error type
        pytest.skip(f"no AWS credentials: {exc}")


@pytest.fixture
def snapshot(aws_credentials: Credentials) -> Iterator[str]:
    """A pending 1 GiB snapshot; cancelled by AWS after 10 minutes and deleted here."""
    with EBSClient(region=AWS_REGION) as ebs:
        started = ebs.start_snapshot(
            volume_size=1,
            timeout=10,
            description="capo integration test, safe to delete",
            tags=[{"key": "Name", "value": "capotest"}],
        )
    snapshot_id = started["snapshot_id"]
    assert snapshot_id
    yield snapshot_id
    with EC2Client(region=AWS_REGION) as ec2:
        ec2.delete_snapshot(snapshot_id=snapshot_id)


class TestAsyncCredentials:  # unasync: generate
    pytestmark = pytest.mark.usefixtures("aws_credentials")

    async def test_default_chain_signs_a_request(self):
        # No credentials given: the client resolves them itself (env, SSO, profile, ...).
        async with AsyncIAMClient(region=AWS_REGION) as iam:
            assert "account_aliases" in await iam.list_account_aliases()

    async def test_sso_provider(self, aws_credentials: Credentials):
        provider = SsoCredentialsProvider(AsyncClient())
        try:
            credentials = await provider.aresolve_identity()
        except Exception as exc:
            pytest.skip(f"active profile is not an SSO profile: {exc}")
        assert credentials.get("session_token"), "SSO credentials are always temporary"
        async with AsyncSTSClient(region=AWS_REGION, credentials=credentials) as sts:
            identity = await sts.get_caller_identity()
        assert identity.get("account") == (await self._account(aws_credentials))
        assert ":assumed-role/" in identity.get("arn", "")

    async def test_query_protocol_request_is_signed(self, aws_credentials: Credentials):
        async with AsyncSTSClient(region=AWS_REGION, credentials=aws_credentials) as sts:
            identity = await sts.get_caller_identity()
        account = identity.get("account", "")
        assert len(account) == 12 and account.isdigit()
        assert identity.get("arn", "").startswith(f"arn:aws:sts::{account}:") or identity.get("arn", "").startswith(
            f"arn:aws:iam::{account}:"
        )

    async def test_bad_credentials_are_rejected(self):
        bad: Credentials = {
            "access_key": "AKIAIOSFODNN7EXAMPLE",
            "secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        }
        async with AsyncSTSClient(region=AWS_REGION, credentials=bad) as sts:
            with pytest.raises(UnknownServiceError) as info:
                await sts.get_caller_identity()
        assert info.value.code == "InvalidClientTokenId"

    @staticmethod
    async def _account(credentials: Credentials) -> str:
        async with AsyncSTSClient(region=AWS_REGION, credentials=credentials) as sts:
            return (await sts.get_caller_identity()).get("account", "")


class TestCredentials:  # unasync: generated
    pytestmark = pytest.mark.usefixtures("aws_credentials")

    def test_default_chain_signs_a_request(self):
        # No credentials given: the client resolves them itself (env, SSO, profile, ...).
        with IAMClient(region=AWS_REGION) as iam:
            assert "account_aliases" in iam.list_account_aliases()

    def test_sso_provider(self, aws_credentials: Credentials):
        provider = SsoCredentialsProvider(Client())
        try:
            credentials = provider.resolve_identity()
        except Exception as exc:
            pytest.skip(f"active profile is not an SSO profile: {exc}")
        assert credentials.get("session_token"), "SSO credentials are always temporary"
        with STSClient(region=AWS_REGION, credentials=credentials) as sts:
            identity = sts.get_caller_identity()
        assert identity.get("account") == (self._account(aws_credentials))
        assert ":assumed-role/" in identity.get("arn", "")

    def test_query_protocol_request_is_signed(self, aws_credentials: Credentials):
        with STSClient(region=AWS_REGION, credentials=aws_credentials) as sts:
            identity = sts.get_caller_identity()
        account = identity.get("account", "")
        assert len(account) == 12 and account.isdigit()
        assert identity.get("arn", "").startswith(f"arn:aws:sts::{account}:") or identity.get("arn", "").startswith(
            f"arn:aws:iam::{account}:"
        )

    def test_bad_credentials_are_rejected(self):
        bad: Credentials = {
            "access_key": "AKIAIOSFODNN7EXAMPLE",
            "secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        }
        with STSClient(region=AWS_REGION, credentials=bad) as sts:
            with pytest.raises(UnknownServiceError) as info:
                sts.get_caller_identity()
        assert info.value.code == "InvalidClientTokenId"

    @staticmethod
    def _account(credentials: Credentials) -> str:
        with STSClient(region=AWS_REGION, credentials=credentials) as sts:
            return (sts.get_caller_identity()).get("account", "")
