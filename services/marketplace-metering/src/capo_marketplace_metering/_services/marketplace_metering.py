"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#AWSMPMeteringService``."""

import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_marketplace_metering._auth._signers
import capo_marketplace_metering._auth._sigv4
from capo_marketplace_metering._auth._identity import Credentials
from capo_marketplace_metering._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_marketplace_metering._auth._zapros_handler import AuthMiddleware
from capo_marketplace_metering._services._aws_config import aws_config
from capo_marketplace_metering._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_marketplace_metering.types.batch_meter_usage_request
    import capo_marketplace_metering.types.batch_meter_usage_result
    import capo_marketplace_metering.types.boolean
    import capo_marketplace_metering.types.client_token
    import capo_marketplace_metering.types.meter_usage_request
    import capo_marketplace_metering.types.meter_usage_result
    import capo_marketplace_metering.types.non_empty_string
    import capo_marketplace_metering.types.nonce
    import capo_marketplace_metering.types.product_code
    import capo_marketplace_metering.types.register_usage_request
    import capo_marketplace_metering.types.register_usage_result
    import capo_marketplace_metering.types.resolve_customer_request
    import capo_marketplace_metering.types.resolve_customer_result
    import capo_marketplace_metering.types.timestamp
    import capo_marketplace_metering.types.usage_allocations
    import capo_marketplace_metering.types.usage_dimension
    import capo_marketplace_metering.types.usage_quantity
    import capo_marketplace_metering.types.usage_record_list
    import capo_marketplace_metering.types.version_integer


class MarketplaceMeteringClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class MarketplaceMeteringClient:
    """A client for the ``MarketplaceMetering`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = MarketplaceMeteringClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[MarketplaceMeteringClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MarketplaceMeteringClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def batch_meter_usage(
        self,
        usage_records: "capo_marketplace_metering.types.usage_record_list.UsageRecordList",
        *,
        config_overrides: Optional[MarketplaceMeteringClientConfig] = None,
        product_code: Optional[
            "capo_marketplace_metering.types.product_code.ProductCode"
        ] = None,
    ) -> (
        "capo_marketplace_metering.types.batch_meter_usage_result.BatchMeterUsageResult"
    ):
        """<important> <p>Amazon Web Services Marketplace is introducing Concurrent Agreements, enabling buyers to make multiple purchases per Amazon Web Services account. Starting June 1, 2026, new SaaS products must use <code>CustomerAWSAccountId</code> (instead of <code>CustomerIdentifier</code>), <code>LicenseArn</code> (instead of <code>ProductCode</code>) to support this feature. <code>BatchMeterUsage</code> does not support <code>CustomerIdentifier</code> for new integrations. Existing integrations continue to work. Review the new integration for Concurrent Agreements <a href="https://catalog.workshops.aws/mpseller/en-US/saas/integration-for-concurrent-agreements">here</a>. For additional implementation details, see <a href="https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-batchmeterusage-licensearn-example">BatchMeterUsage code example with LicenseArn</a> in the <i>Amazon Web Services Marketplace Seller Guide</i>.</p> </important> <p>To post metering records for customers, SaaS applications call <code>BatchMeterUsage</code>, which is used for metering SaaS flexible consumption pricing (FCP). Identical requests are idempotent and can be retried with the same records or a subset of records. Each <code>BatchMeterUsage</code> request is for only one product. If you want to meter usage for multiple products, you must make multiple <code>BatchMeterUsage</code> calls.</p> <p>Usage records should be submitted in quick succession following a recorded event. Usage records aren't accepted 24 hours or more after an event. At the end of each billing cycle, a 6-hour grace period applies. We accept usage records for the previous billing month until 06:00 UTC on the first day of the next month. For example, you must submit March usage records before 06:00 UTC on April 1. On April 1 at 05:00 UTC, you can still submit records for March 31 (within the 6-hour grace period). After 06:00 UTC on April 1, March records are rejected regardless of the normal 24-hour submission window. After this grace period, we return a <code>TimestampOutOfBoundsException</code> error.</p> <p> <code>BatchMeterUsage</code> can process up to 25 <code>UsageRecords</code> at a time, and each request must be less than 1 MB in size. Optionally, you can have multiple usage allocations for usage data that's split into buckets according to predefined tags.</p> <p> <code>BatchMeterUsage</code> returns a list of <code>UsageRecordResult</code> objects, which have each <code>UsageRecord</code>. It also returns a list of <code>UnprocessedRecords</code>, which indicate errors on the service side that should be retried.</p> <p>For Amazon Web Services Regions that support <code>BatchMeterUsage</code>, see <a href="https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#batchmeterusage-region-support">BatchMeterUsage Region support</a>. </p> <note> <p>For an example of <code>BatchMeterUsage</code>, see <a href="https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-batchmeterusage-example"> BatchMeterUsage code example</a> in the <i>Amazon Web Services Marketplace Seller Guide</i>.</p> </note>

        Args:
            usage_records: <p>The set of <code>UsageRecords</code> to submit. <code>BatchMeterUsage</code> accepts up to 25 <code>UsageRecords</code> at a time.</p>
            product_code: <p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p> <important> <p> <code>ProductCode</code> is required only for legacy integrations that use <code>CustomerIdentifier</code>. For new integrations using <code>LicenseArn</code> (Concurrent Agreements), do NOT include <code>ProductCode</code> at the request level. The <code>LicenseArn</code> in each <code>UsageRecord</code> identifies both the product and the specific agreement.</p> <p>Sending metering records with both <code>ProductCode</code> and <code>LicenseArn</code> for the same customer within the same hour will result in duplicate billing. If you are migrating from product-based metering to license-based metering, stop sending <code>ProductCode</code> before you start sending <code>LicenseArn</code>.</p> </important>

        Raises:
            capo_marketplace_metering.errors.disabled_api_exception.DisabledApiException: <p>The API is disabled in the Region.</p>
            capo_marketplace_metering.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error has occurred. Retry your request. If the problem persists, post a message with details on the Amazon Web Services forums.</p>
            capo_marketplace_metering.errors.invalid_customer_identifier_exception.InvalidCustomerIdentifierException: <p>You have metered usage for a <code>CustomerIdentifier</code> that does not exist.</p>
            capo_marketplace_metering.errors.invalid_license_exception.InvalidLicenseException: <p>Ensure the <code>LicenseArn</code> is valid, matches the customer, and usage is within the license activation period.</p>
            capo_marketplace_metering.errors.invalid_product_code_exception.InvalidProductCodeException: <p>The product code passed does not match the product code used for publishing the product.</p>
            capo_marketplace_metering.errors.invalid_tag_exception.InvalidTagException: <p>The tag is invalid, or the number of tags is greater than 5.</p>
            capo_marketplace_metering.errors.invalid_usage_allocations_exception.InvalidUsageAllocationsException: <p>Sum of allocated usage quantities is not equal to the usage quantity.</p>
            capo_marketplace_metering.errors.invalid_usage_dimension_exception.InvalidUsageDimensionException: <p>The usage dimension does not match one of the <code>UsageDimensions</code> associated with products.</p>
            capo_marketplace_metering.errors.throttling_exception.ThrottlingException: <p>The calls to the API are throttled.</p>
            capo_marketplace_metering.errors.timestamp_out_of_bounds_exception.TimestampOutOfBoundsException: <p>The <code>timestamp</code> value passed in the <code>UsageRecord</code> is out of allowed range.</p> <p>For <code>BatchMeterUsage</code>, if any of the records are outside of the allowed range, the entire batch is not processed. You must remove invalid records and try again.</p>
            capo_marketplace_metering.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_marketplace_metering.types.batch_meter_usage_request.BatchMeterUsageRequest]",
        ) -> OperationResponse[
            "capo_marketplace_metering.types.batch_meter_usage_result.BatchMeterUsageResult"
        ]:
            import capo_marketplace_metering._operations.awsmp_metering_service.batch_meter_usage

            output, http_response = (
                capo_marketplace_metering._operations.awsmp_metering_service.batch_meter_usage.batch_meter_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_metering.types.batch_meter_usage_request.BatchMeterUsageRequest = {
            "usage_records": usage_records
        }
        if product_code is not None:
            input_["product_code"] = product_code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def meter_usage(
        self,
        product_code: "capo_marketplace_metering.types.product_code.ProductCode",
        timestamp: "capo_marketplace_metering.types.timestamp.Timestamp",
        usage_dimension: "capo_marketplace_metering.types.usage_dimension.UsageDimension",
        *,
        config_overrides: Optional[MarketplaceMeteringClientConfig] = None,
        usage_quantity: Optional[
            "capo_marketplace_metering.types.usage_quantity.UsageQuantity"
        ] = None,
        dry_run: Optional["capo_marketplace_metering.types.boolean.Boolean"] = None,
        usage_allocations: Optional[
            "capo_marketplace_metering.types.usage_allocations.UsageAllocations"
        ] = None,
        client_token: Optional[
            "capo_marketplace_metering.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_marketplace_metering.types.meter_usage_result.MeterUsageResult":
        """<p>As a seller, your software hosted in the buyer's Amazon Web Services account uses this API action to emit metering records directly to Amazon Web Services Marketplace. You must use the following buyer Amazon Web Services account credentials to sign the API request.</p> <ul> <li> <p>For <b>Amazon EC2</b> deployments, your software must use the <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html">IAM role for Amazon EC2</a> to sign the API call for <code>MeterUsage</code> API operation.</p> </li> <li> <p>For <b>Amazon EKS</b> deployments, your software must use <a href="https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html">IAM roles for service accounts (IRSA)</a> to sign the API call for the <code>MeterUsage</code> API operation. Using <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html">EKS Pod Identity</a>, the node role, or long-term access keys is not supported.</p> </li> <li> <p>For <b>Amazon ECS</b> deployments, your software must use <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">Amazon ECS task IAM</a> role to sign the API call for the <code>MeterUsage</code> API operation. Using the node role or long-term access keys are not supported.</p> </li> <li> <p>For <b>Amazon Bedrock AgentCore Runtime</b> deployments, your software must use the <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html#runtime-permissions-execution">AgentCore Runtime execution role</a> to sign the API call for the <code>MeterUsage</code> API operation. Long-term access keys are not supported.</p> </li> </ul> <p>The handling of <code>MeterUsage</code> requests varies between Amazon Bedrock AgentCore Runtime and non-Amazon Bedrock AgentCore deployments.</p> <ul> <li> <p>For <b>non-Amazon Bedrock AgentCore Runtime</b> deployments, you can only report usage once per hour for each dimension. For AMI-based products, this is per dimension and per EC2 instance. For container products, this is per dimension and per ECS task or EKS pod. You can't modify values after they're recorded. If you report usage before a current hour ends, you will be unable to report additional usage until the next hour begins. The <code>Timestamp</code> request parameter is rounded down to the hour and used to enforce this once-per-hour rule for idempotency. For requests that are identical after the <code>Timestamp</code> is rounded down, the API is idempotent and returns the metering record ID.</p> </li> <li> <p>For <b>Amazon Bedrock AgentCore Runtime</b> deployments, you can report usage multiple times per hour for the same dimension. You do not need to aggregate metering records by the hour. You must include an idempotency token in the <code>ClientToken</code> request parameter. If using an Amazon SDK or the Amazon Web Services CLI, you must use the latest version which automatically includes an idempotency token in the <code>ClientToken</code> request parameter so that the request is processed successfully. The <code>Timestamp</code> request parameter is not rounded down to the hour and is not used for duplicate validation. Requests with duplicate <code>Timestamps</code> are aggregated as long as the <code>ClientToken</code> is unique.</p> </li> </ul> <p>If you submit records more than six hours after events occur, the records won't be accepted. The timestamp in your request determines when an event is recorded.</p> <p>You can optionally include multiple usage allocations, to provide customers with usage data split into buckets by tags that you define or allow the customer to define.</p> <p>For Amazon Web Services Regions that support <code>MeterUsage</code>, see <a href="https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#meterusage-region-support-ec2">MeterUsage Region support for Amazon EC2</a> and <a href="https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#meterusage-region-support-ecs-eks">MeterUsage Region support for Amazon ECS and Amazon EKS</a>. </p>

        Args:
            product_code: <p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p>
            timestamp: <p>Timestamp, in UTC, for which the usage is being reported. Your application can meter usage for up to six hours in the past. Make sure the <code>timestamp</code> value is not before the start of the software usage.</p>
            usage_dimension: <p>It will be one of the fcp dimension name provided during the publishing of the product.</p>
            usage_quantity: <p>Consumption value for the hour. Defaults to <code>0</code> if not specified.</p>
            dry_run: <p>Checks whether you have the permissions required for the action, but does not make the request. If you have the permissions, the request returns <code>DryRunOperation</code>; otherwise, it returns <code>UnauthorizedException</code>. Defaults to <code>false</code> if not specified.</p>
            usage_allocations: <p>The set of <code>UsageAllocations</code> to submit.</p> <p>The sum of all <code>UsageAllocation</code> quantities must equal the <code>UsageQuantity</code> of the <code>MeterUsage</code> request, and each <code>UsageAllocation</code> must have a unique set of tags (include no tags).</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotencyConflictException</code> error.</p>

        Raises:
            capo_marketplace_metering.errors.customer_not_entitled_exception.CustomerNotEntitledException: <p>Exception thrown when the customer does not have a valid subscription for the product.</p>
            capo_marketplace_metering.errors.duplicate_request_exception.DuplicateRequestException: <p>A metering record has already been emitted by the same EC2 instance, ECS task, or EKS pod for the given {<code>usageDimension</code>, <code>timestamp</code>} with a different <code>usageQuantity</code>.</p>
            capo_marketplace_metering.errors.idempotency_conflict_exception.IdempotencyConflictException: <p>The <code>ClientToken</code> is being used for multiple requests.</p>
            capo_marketplace_metering.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error has occurred. Retry your request. If the problem persists, post a message with details on the Amazon Web Services forums.</p>
            capo_marketplace_metering.errors.invalid_endpoint_region_exception.InvalidEndpointRegionException: <p>The endpoint being called is in a Amazon Web Services Region different from your EC2 instance, ECS task, or EKS pod. The Region of the Metering Service endpoint and the Amazon Web Services Region of the resource must match.</p>
            capo_marketplace_metering.errors.invalid_product_code_exception.InvalidProductCodeException: <p>The product code passed does not match the product code used for publishing the product.</p>
            capo_marketplace_metering.errors.invalid_tag_exception.InvalidTagException: <p>The tag is invalid, or the number of tags is greater than 5.</p>
            capo_marketplace_metering.errors.invalid_usage_allocations_exception.InvalidUsageAllocationsException: <p>Sum of allocated usage quantities is not equal to the usage quantity.</p>
            capo_marketplace_metering.errors.invalid_usage_dimension_exception.InvalidUsageDimensionException: <p>The usage dimension does not match one of the <code>UsageDimensions</code> associated with products.</p>
            capo_marketplace_metering.errors.throttling_exception.ThrottlingException: <p>The calls to the API are throttled.</p>
            capo_marketplace_metering.errors.timestamp_out_of_bounds_exception.TimestampOutOfBoundsException: <p>The <code>timestamp</code> value passed in the <code>UsageRecord</code> is out of allowed range.</p> <p>For <code>BatchMeterUsage</code>, if any of the records are outside of the allowed range, the entire batch is not processed. You must remove invalid records and try again.</p>
            capo_marketplace_metering.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_marketplace_metering.types.meter_usage_request.MeterUsageRequest]",
        ) -> OperationResponse[
            "capo_marketplace_metering.types.meter_usage_result.MeterUsageResult"
        ]:
            import capo_marketplace_metering._operations.awsmp_metering_service.meter_usage

            output, http_response = (
                capo_marketplace_metering._operations.awsmp_metering_service.meter_usage.meter_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_metering.types.meter_usage_request.MeterUsageRequest = {
            "product_code": product_code,
            "timestamp": timestamp,
            "usage_dimension": usage_dimension,
        }
        if usage_quantity is not None:
            input_["usage_quantity"] = usage_quantity
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if usage_allocations is not None:
            input_["usage_allocations"] = usage_allocations
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_usage(
        self,
        product_code: "capo_marketplace_metering.types.product_code.ProductCode",
        public_key_version: "capo_marketplace_metering.types.version_integer.VersionInteger",
        *,
        config_overrides: Optional[MarketplaceMeteringClientConfig] = None,
        nonce: Optional["capo_marketplace_metering.types.nonce.Nonce"] = None,
    ) -> "capo_marketplace_metering.types.register_usage_result.RegisterUsageResult":
        """<p>Paid container software products sold through Amazon Web Services Marketplace must integrate with the Amazon Web Services Marketplace Metering Service and call the <code>RegisterUsage</code> operation for software entitlement and metering. Free and BYOL products for Amazon ECS or Amazon EKS aren't required to call <code>RegisterUsage</code>, but you may choose to do so if you would like to receive usage data in your seller reports. The sections below explain the behavior of <code>RegisterUsage</code>. <code>RegisterUsage</code> performs two primary functions: metering and entitlement.</p> <ul> <li> <p> <i>Entitlement</i>: <code>RegisterUsage</code> allows you to verify that the customer running your paid software is subscribed to your product on Amazon Web Services Marketplace, enabling you to guard against unauthorized use. Your container image that integrates with <code>RegisterUsage</code> is only required to guard against unauthorized use at container startup, as such a <code>CustomerNotSubscribedException</code> or <code>PlatformNotSupportedException</code> will only be thrown on the initial call to <code>RegisterUsage</code>. Subsequent calls from the same Amazon ECS task instance (e.g. task-id) or Amazon EKS pod will not throw a <code>CustomerNotSubscribedException</code>, even if the customer unsubscribes while the Amazon ECS task or Amazon EKS pod is still running.</p> </li> <li> <p> <i>Metering</i>: <code>RegisterUsage</code> meters software use per ECS task, per hour, or per pod for Amazon EKS with usage prorated to the second. A minimum of 1 minute of usage applies to tasks that are short lived. For example, if a customer has a 10 node Amazon ECS or Amazon EKS cluster and a service configured as a Daemon Set, then Amazon ECS or Amazon EKS will launch a task on all 10 cluster nodes and the customer will be charged for 10 tasks. Software metering is handled by the Amazon Web Services Marketplace metering control plane—your software is not required to perform metering-specific actions other than to call <code>RegisterUsage</code> to commence metering. The Amazon Web Services Marketplace metering control plane will also bill customers for running ECS tasks and Amazon EKS pods, regardless of the customer's subscription state, which removes the need for your software to run entitlement checks at runtime. For containers, <code>RegisterUsage</code> should be called immediately at launch. If you don’t register the container within the first 6 hours of the launch, Amazon Web Services Marketplace Metering Service doesn’t provide any metering guarantees for previous months. Metering will continue, however, for the current month forward until the container ends. <code>RegisterUsage</code> is for metering paid hourly container products.</p> <p>For Amazon Web Services Regions that support <code>RegisterUsage</code>, see <a href="https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#registerusage-region-support">RegisterUsage Region support</a>. </p> </li> </ul>

        Args:
            product_code: <p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p>
            public_key_version: <p>Public Key Version provided by Amazon Web Services Marketplace</p>
            nonce: <p>(Optional) To scope down the registration to a specific running software instance and guard against replay attacks.</p>

        Raises:
            capo_marketplace_metering.errors.customer_not_entitled_exception.CustomerNotEntitledException: <p>Exception thrown when the customer does not have a valid subscription for the product.</p>
            capo_marketplace_metering.errors.disabled_api_exception.DisabledApiException: <p>The API is disabled in the Region.</p>
            capo_marketplace_metering.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error has occurred. Retry your request. If the problem persists, post a message with details on the Amazon Web Services forums.</p>
            capo_marketplace_metering.errors.invalid_product_code_exception.InvalidProductCodeException: <p>The product code passed does not match the product code used for publishing the product.</p>
            capo_marketplace_metering.errors.invalid_public_key_version_exception.InvalidPublicKeyVersionException: <p>Public Key version is invalid.</p>
            capo_marketplace_metering.errors.invalid_region_exception.InvalidRegionException: <p> <code>RegisterUsage</code> must be called in the same Amazon Web Services Region the ECS task was launched in. This prevents a container from hardcoding a Region (e.g. withRegion(“us-east-1”) when calling <code>RegisterUsage</code>.</p>
            capo_marketplace_metering.errors.platform_not_supported_exception.PlatformNotSupportedException: <p>Amazon Web Services Marketplace does not support metering usage from the underlying platform. Currently, Amazon ECS, Amazon EKS, and Fargate are supported.</p>
            capo_marketplace_metering.errors.throttling_exception.ThrottlingException: <p>The calls to the API are throttled.</p>
            capo_marketplace_metering.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_marketplace_metering.types.register_usage_request.RegisterUsageRequest]",
        ) -> OperationResponse[
            "capo_marketplace_metering.types.register_usage_result.RegisterUsageResult"
        ]:
            import capo_marketplace_metering._operations.awsmp_metering_service.register_usage

            output, http_response = (
                capo_marketplace_metering._operations.awsmp_metering_service.register_usage.register_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_metering.types.register_usage_request.RegisterUsageRequest = {
            "product_code": product_code,
            "public_key_version": public_key_version,
        }
        if nonce is not None:
            input_["nonce"] = nonce

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def resolve_customer(
        self,
        registration_token: "capo_marketplace_metering.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[MarketplaceMeteringClientConfig] = None,
    ) -> (
        "capo_marketplace_metering.types.resolve_customer_result.ResolveCustomerResult"
    ):
        """<p> <code>ResolveCustomer</code> is called by a SaaS application during the registration process. When a buyer visits your website during the registration process, the buyer submits a registration token through their browser. The registration token is resolved through this API to obtain a <code>CustomerIdentifier</code> along with the <code>CustomerAWSAccountId</code>, <code>ProductCode</code>, and <code>LicenseArn</code>.</p> <important> <p>For new SaaS product integrations, the <code>CustomerIdentifier</code> field is not populated in the <code>ResolveCustomer</code> API response. New integrations must use <code>CustomerAWSAccountId</code> and <code>LicenseArn</code> to identify customers. Existing integrations continue to work unchanged.</p> </important> <note> <p>To successfully resolve the token, the API must be called from the account that was used to publish the SaaS application. For an example of using <code>ResolveCustomer</code>, see <a href="https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-resolvecustomer-example"> ResolveCustomer code example</a> in the <i>Amazon Web Services Marketplace Seller Guide</i>.</p> </note> <p>Permission is required for this operation. Your IAM role or user performing this operation requires a policy to allow the <code>aws-marketplace:ResolveCustomer</code> action. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacemeteringservice.html">Actions, resources, and condition keys for Amazon Web Services Marketplace Metering Service</a> in the <i>Service Authorization Reference</i>.</p> <p>For Amazon Web Services Regions that support <code>ResolveCustomer</code>, see <a href="https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#resolvecustomer-region-support">ResolveCustomer Region support</a>. </p>

        Args:
            registration_token: <p>When a buyer visits your website during the registration process, the buyer submits a registration token through the browser. The registration token is resolved to obtain a <code>CustomerIdentifier</code> along with the <code>CustomerAWSAccountId</code>, <code>ProductCode</code>, and <code>LicenseArn</code>.</p> <note> <p>For new SaaS product integrations, the <code>CustomerIdentifier</code> field is not populated. Use <code>CustomerAWSAccountId</code> and <code>LicenseArn</code> for customer identification.</p> </note>

        Raises:
            capo_marketplace_metering.errors.disabled_api_exception.DisabledApiException: <p>The API is disabled in the Region.</p>
            capo_marketplace_metering.errors.expired_token_exception.ExpiredTokenException: <p>The submitted registration token has expired. This can happen if the buyer's browser takes too long to redirect to your page, the buyer has resubmitted the registration token, or your application has held on to the registration token for too long. Your SaaS registration website should redeem this token as soon as it is submitted by the buyer's browser.</p>
            capo_marketplace_metering.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error has occurred. Retry your request. If the problem persists, post a message with details on the Amazon Web Services forums.</p>
            capo_marketplace_metering.errors.invalid_token_exception.InvalidTokenException: <p>Registration token is invalid.</p>
            capo_marketplace_metering.errors.throttling_exception.ThrottlingException: <p>The calls to the API are throttled.</p>
            capo_marketplace_metering.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_marketplace_metering.types.resolve_customer_request.ResolveCustomerRequest]",
        ) -> OperationResponse[
            "capo_marketplace_metering.types.resolve_customer_result.ResolveCustomerResult"
        ]:
            import capo_marketplace_metering._operations.awsmp_metering_service.resolve_customer

            output, http_response = (
                capo_marketplace_metering._operations.awsmp_metering_service.resolve_customer.resolve_customer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_metering.types.resolve_customer_request.ResolveCustomerRequest = {
            "registration_token": registration_token
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
