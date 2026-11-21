"""One real AWS call per kind of generated client: wire protocol x auth scheme.

Every service package comes out of the same generator, so two services that
share a protocol and an auth scheme build, sign and parse requests with the
same code. One call per combination below therefore stands in for the other
services of that kind:

=================================  ===================  ===========================
protocol (as generated)            auth                 checked with
=================================  ===================  ===========================
restJson1                          sigv4                amp
awsJson1_1                         sigv4                application-auto-scaling
awsJson1_0                         sigv4                apprunner
awsJson1_0 + awsQueryCompatible    sigv4                sqs
awsQuery                           sigv4                elasticache
awsQuery (awsJson1_0 also listed)  sigv4                cloudwatch
ec2Query                           sigv4                ec2
restXml                            sigv4                route-53 (s3 has its own suite)
rpcv2Cbor                          sigv4                cloudwatchomni
restJson1                          sigv4a (endpoint)    sustainability
awsJson1_0                         sigv4a (endpoint)    partnercentral-channel
rpcv2Cbor                          sigv4a (endpoint)    partnercentral-revenue-measurement
restJson1                          httpBearerAuth       bedrock (codecatalyst: same signer)
restJson1                          none (``@auth([])``)  sso-oidc
awsJson1_1                         none (``@auth([])``)  cognito-identity-provider
awsQuery                           none (``@auth([])``)  sts
=================================  ===================  ===========================

Services that list rpcv2Cbor next to an awsJson protocol are generated with the
awsJson one, so they are covered by the awsJson rows.

All calls are free reads or requests the service rejects. A modeled error that
can only come back after the service authenticated the request (access denied
for an account that is not enrolled, a missing resource) counts as a pass: a
bad signature or a malformed body would fail earlier with another error.
``ry`` generates the sync twins.
"""

from __future__ import annotations

import base64
import datetime

import pytest
from capo_amp import AsyncampClient, ampClient
from capo_application_auto_scaling import ApplicationAutoScalingClient, AsyncApplicationAutoScalingClient
from capo_apprunner import AppRunnerClient, AsyncAppRunnerClient
from capo_bedrock import AsyncBedrockClient, BedrockClient
from capo_bedrock.errors import AccessDeniedException as BedrockAccessDenied
from capo_cloudwatch import AsyncCloudWatchClient, CloudWatchClient
from capo_cloudwatchomni import AsyncCloudWatchOmniClient, CloudWatchOmniClient
from capo_cognito_identity_provider import AsyncCognitoIdentityProviderClient, CognitoIdentityProviderClient
from capo_cognito_identity_provider import EnvCredentialsProvider as CognitoEnvCredentials
from capo_cognito_identity_provider.errors import ResourceNotFoundException as CognitoNotFound
from capo_ec2 import AsyncEC2Client, EC2Client
from capo_elasticache import AsyncElastiCacheClient, ElastiCacheClient
from capo_partnercentral_channel import AsyncPartnerCentralChannelClient, PartnerCentralChannelClient
from capo_partnercentral_channel.errors import AccessDeniedException as ChannelAccessDenied
from capo_partnercentral_revenue_measurement import (
    AsyncPartnerCentralRevenueMeasurementClient,
    PartnerCentralRevenueMeasurementClient,
)
from capo_partnercentral_revenue_measurement.errors import AccessDeniedException as RevenueAccessDenied
from capo_route_53 import AsyncRoute53Client, Route53Client
from capo_sqs import AsyncSQSClient, SQSClient
from capo_sqs.errors import QueueDoesNotExist
from capo_sso_oidc import AsyncSSOOIDCClient, SSOOIDCClient
from capo_sso_oidc import EnvCredentialsProvider as SSOOIDCEnvCredentials
from capo_sts import AsyncSTSClient, STSClient
from capo_sts import EnvCredentialsProvider as STSEnvCredentials
from capo_sts.errors import InvalidIdentityTokenException
from capo_sustainability import AsyncSustainabilityClient, SustainabilityClient

from tests.conftest import AWS_REGION, unique_name

# partner central and sustainability only answer in us-east-1
GLOBAL_REGION = "us-east-1"


class TestAsyncSigV4:  # unasync: generate
    pytestmark = pytest.mark.usefixtures("async_aws_credentials")

    async def test_rest_json1(self):
        async with AsyncampClient(region=AWS_REGION) as client:
            out = await client.list_workspaces(max_results=1)
        assert isinstance(out.get("workspaces"), list)

    async def test_aws_json1_1(self):
        async with AsyncApplicationAutoScalingClient(region=AWS_REGION) as client:
            out = await client.describe_scalable_targets("ecs", max_results=1)
        assert isinstance(out.get("scalable_targets"), list)

    async def test_aws_json1_0(self):
        async with AsyncAppRunnerClient(region=AWS_REGION) as client:
            out = await client.list_services(max_results=1)
        assert isinstance(out.get("service_summary_list"), list)

    async def test_aws_json1_0_query_compatible(self):
        # the error code comes from the x-amzn-query-error header, not the JSON __type
        async with AsyncSQSClient(region=AWS_REGION) as client:
            with pytest.raises(QueueDoesNotExist):
                await client.get_queue_url(unique_name())

    async def test_aws_query(self):
        async with AsyncElastiCacheClient(region=AWS_REGION) as client:
            out = await client.describe_cache_clusters(max_records=20)
        assert isinstance(out.get("cache_clusters"), list)

    async def test_aws_query_with_aws_json_listed(self):
        async with AsyncCloudWatchClient(region=AWS_REGION) as client:
            out = await client.list_dashboards(dashboard_name_prefix=unique_name())
        assert out.get("dashboard_entries") == []

    async def test_ec2_query(self):
        async with AsyncEC2Client(region=AWS_REGION) as client:
            out = await client.describe_regions(region_names=[AWS_REGION])
        assert [r.get("region_name") for r in out.get("regions", [])] == [AWS_REGION]

    async def test_rest_xml(self):
        async with AsyncRoute53Client(region=AWS_REGION) as client:
            out = await client.list_hosted_zones(max_items=1)
        assert isinstance(out.get("hosted_zones"), list)

    async def test_rpc_v2_cbor(self):
        async with AsyncCloudWatchOmniClient(region=AWS_REGION) as client:
            out = await client.list_domains(max_results=1)
        assert isinstance(out.get("items"), list)


class TestSigV4:  # unasync: generated
    pytestmark = pytest.mark.usefixtures("aws_credentials")

    def test_rest_json1(self):
        with ampClient(region=AWS_REGION) as client:
            out = client.list_workspaces(max_results=1)
        assert isinstance(out.get("workspaces"), list)

    def test_aws_json1_1(self):
        with ApplicationAutoScalingClient(region=AWS_REGION) as client:
            out = client.describe_scalable_targets("ecs", max_results=1)
        assert isinstance(out.get("scalable_targets"), list)

    def test_aws_json1_0(self):
        with AppRunnerClient(region=AWS_REGION) as client:
            out = client.list_services(max_results=1)
        assert isinstance(out.get("service_summary_list"), list)

    def test_aws_json1_0_query_compatible(self):
        # the error code comes from the x-amzn-query-error header, not the JSON __type
        with SQSClient(region=AWS_REGION) as client:
            with pytest.raises(QueueDoesNotExist):
                client.get_queue_url(unique_name())

    def test_aws_query(self):
        with ElastiCacheClient(region=AWS_REGION) as client:
            out = client.describe_cache_clusters(max_records=20)
        assert isinstance(out.get("cache_clusters"), list)

    def test_aws_query_with_aws_json_listed(self):
        with CloudWatchClient(region=AWS_REGION) as client:
            out = client.list_dashboards(dashboard_name_prefix=unique_name())
        assert out.get("dashboard_entries") == []

    def test_ec2_query(self):
        with EC2Client(region=AWS_REGION) as client:
            out = client.describe_regions(region_names=[AWS_REGION])
        assert [r.get("region_name") for r in out.get("regions", [])] == [AWS_REGION]

    def test_rest_xml(self):
        with Route53Client(region=AWS_REGION) as client:
            out = client.list_hosted_zones(max_items=1)
        assert isinstance(out.get("hosted_zones"), list)

    def test_rpc_v2_cbor(self):
        with CloudWatchOmniClient(region=AWS_REGION) as client:
            out = client.list_domains(max_results=1)
        assert isinstance(out.get("items"), list)


class TestAsyncSigV4A:  # unasync: generate
    pytestmark = [
        pytest.mark.usefixtures("async_aws_credentials"),
        pytest.mark.skip(reason="SigV4A signing is not implemented"),
    ]

    async def test_rest_json1(self):
        end = datetime.datetime.now(datetime.timezone.utc).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        start = (end - datetime.timedelta(days=1)).replace(day=1)
        async with AsyncSustainabilityClient(region=GLOBAL_REGION) as client:
            out = await client.get_estimated_carbon_emissions_dimension_values(
                {"start": start, "end": end}, ["REGION"], max_results=1
            )
        assert isinstance(out.get("results"), list)

    async def test_aws_json1_0(self):
        async with AsyncPartnerCentralChannelClient(region=GLOBAL_REGION) as client:
            with pytest.raises(ChannelAccessDenied):
                await client.list_channel_handshakes("START_SERVICE_PERIOD", "Sandbox", "SENDER", max_results=1)

    async def test_rpc_v2_cbor(self):
        async with AsyncPartnerCentralRevenueMeasurementClient(region=GLOBAL_REGION) as client:
            with pytest.raises(RevenueAccessDenied):
                await client.list_revenue_attributions("Sandbox")


class TestSigV4A:  # unasync: generated
    pytestmark = [
        pytest.mark.usefixtures("aws_credentials"),
        pytest.mark.skip(reason="SigV4A signing is not implemented"),
    ]

    def test_rest_json1(self):
        end = datetime.datetime.now(datetime.timezone.utc).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        start = (end - datetime.timedelta(days=1)).replace(day=1)
        with SustainabilityClient(region=GLOBAL_REGION) as client:
            out = client.get_estimated_carbon_emissions_dimension_values(
                {"start": start, "end": end}, ["REGION"], max_results=1
            )
        assert isinstance(out.get("results"), list)

    def test_aws_json1_0(self):
        with PartnerCentralChannelClient(region=GLOBAL_REGION) as client:
            with pytest.raises(ChannelAccessDenied):
                client.list_channel_handshakes("START_SERVICE_PERIOD", "Sandbox", "SENDER", max_results=1)

    def test_rpc_v2_cbor(self):
        with PartnerCentralRevenueMeasurementClient(region=GLOBAL_REGION) as client:
            with pytest.raises(RevenueAccessDenied):
                client.list_revenue_attributions("Sandbox")


class TestAsyncBearer:  # unasync: generate
    async def test_rest_json1(self):
        # Well-formed but unknown key: the service parsed the Bearer header as an
        # API key. Without the header it answers "Authorization header is missing".
        key = "ABSK" + base64.b64encode(b"BedrockAPIKey-capotest-at-123456789012:invalid").decode()
        async with AsyncBedrockClient(region=AWS_REGION, bearer=key) as client:
            with pytest.raises(BedrockAccessDenied) as info:
                await client.list_foundation_models()
        assert "API Key is valid" in str(info.value)


class TestBearer:  # unasync: generated
    def test_rest_json1(self):
        # Well-formed but unknown key: the service parsed the Bearer header as an
        # API key. Without the header it answers "Authorization header is missing".
        key = "ABSK" + base64.b64encode(b"BedrockAPIKey-capotest-at-123456789012:invalid").decode()
        with BedrockClient(region=AWS_REGION, bearer=key) as client:
            with pytest.raises(BedrockAccessDenied) as info:
                client.list_foundation_models()
        assert "API Key is valid" in str(info.value)


class TestAsyncNoAuth:  # unasync: generate
    """``@auth([])`` operations: sent unsigned, so they work with no AWS credentials at all."""

    @pytest.fixture(autouse=True)
    def no_credentials(self, monkeypatch: pytest.MonkeyPatch) -> None:
        # each client below gets EnvCredentialsProvider, which then has nothing to resolve
        monkeypatch.delenv("AWS_ACCESS_KEY_ID", raising=False)
        monkeypatch.delenv("AWS_SECRET_ACCESS_KEY", raising=False)

    async def test_rest_json1(self):
        async with AsyncSSOOIDCClient(region=AWS_REGION, credentials_provider=SSOOIDCEnvCredentials()) as client:
            out = await client.register_client(unique_name(), "public")
        assert out.get("client_id") and out.get("client_secret")

    async def test_aws_json1_1(self):
        provider = CognitoEnvCredentials()
        async with AsyncCognitoIdentityProviderClient(region=AWS_REGION, credentials_provider=provider) as client:
            with pytest.raises(CognitoNotFound):
                await client.initiate_auth(
                    "USER_PASSWORD_AUTH",
                    "capotestnosuchclient0000000",
                    auth_parameters={"USERNAME": "capo", "PASSWORD": "capo"},
                )

    async def test_aws_query(self):
        async with AsyncSTSClient(region=AWS_REGION, credentials_provider=STSEnvCredentials()) as client:
            with pytest.raises(InvalidIdentityTokenException):
                await client.assume_role_with_web_identity(
                    "arn:aws:iam::123456789012:role/capotest", unique_name(), "not-a-jwt"
                )


class TestNoAuth:  # unasync: generated
    """``@auth([])`` operations: sent unsigned, so they work with no AWS credentials at all."""

    @pytest.fixture(autouse=True)
    def no_credentials(self, monkeypatch: pytest.MonkeyPatch) -> None:
        # each client below gets EnvCredentialsProvider, which then has nothing to resolve
        monkeypatch.delenv("AWS_ACCESS_KEY_ID", raising=False)
        monkeypatch.delenv("AWS_SECRET_ACCESS_KEY", raising=False)

    def test_rest_json1(self):
        with SSOOIDCClient(region=AWS_REGION, credentials_provider=SSOOIDCEnvCredentials()) as client:
            out = client.register_client(unique_name(), "public")
        assert out.get("client_id") and out.get("client_secret")

    def test_aws_json1_1(self):
        provider = CognitoEnvCredentials()
        with CognitoIdentityProviderClient(region=AWS_REGION, credentials_provider=provider) as client:
            with pytest.raises(CognitoNotFound):
                client.initiate_auth(
                    "USER_PASSWORD_AUTH",
                    "capotestnosuchclient0000000",
                    auth_parameters={"USERNAME": "capo", "PASSWORD": "capo"},
                )

    def test_aws_query(self):
        with STSClient(region=AWS_REGION, credentials_provider=STSEnvCredentials()) as client:
            with pytest.raises(InvalidIdentityTokenException):
                client.assume_role_with_web_identity(
                    "arn:aws:iam::123456789012:role/capotest", unique_name(), "not-a-jwt"
                )
