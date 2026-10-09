"""Generated from Smithy shape ``com.amazonaws.simpledbv2#SimpleDBv2``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_simpledbv2._auth._signers
import capo_simpledbv2._auth._sigv4
from capo_simpledbv2._auth._identity import Credentials
from capo_simpledbv2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_simpledbv2._auth._zapros_handler import AuthMiddleware
from capo_simpledbv2._pagination import resolve_path as _resolve_path
from capo_simpledbv2._services._aws_config import aaws_config
from capo_simpledbv2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_simpledbv2.types.aws_account_id
    import capo_simpledbv2.types.domain_name
    import capo_simpledbv2.types.export_arn
    import capo_simpledbv2.types.export_summary
    import capo_simpledbv2.types.get_export_request
    import capo_simpledbv2.types.get_export_response
    import capo_simpledbv2.types.idempotency_token
    import capo_simpledbv2.types.list_exports_request
    import capo_simpledbv2.types.list_exports_response
    import capo_simpledbv2.types.max_results
    import capo_simpledbv2.types.next_token
    import capo_simpledbv2.types.s3_bucket_name
    import capo_simpledbv2.types.s3_key_prefix
    import capo_simpledbv2.types.s3_sse_algorithm
    import capo_simpledbv2.types.s3_sse_kms_key_id
    import capo_simpledbv2.types.start_domain_export_request
    import capo_simpledbv2.types.start_domain_export_response


class AsyncSimpleDBv2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSimpleDBv2Client:
    """A client for the ``SimpleDBv2`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncSimpleDBv2ClientConfig(
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
        self, config_overrides: Optional[AsyncSimpleDBv2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSimpleDBv2ClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def get_export(
        self,
        export_arn: "capo_simpledbv2.types.export_arn.ExportArn",
        *,
        config_overrides: Optional[AsyncSimpleDBv2ClientConfig] = None,
    ) -> "capo_simpledbv2.types.get_export_response.GetExportResponse":
        """Returns information for an existing domain export.

        Args:
            export_arn: Unique ARN identifier of the export.

        Raises:
            capo_simpledbv2.errors.invalid_parameter_value_exception.InvalidParameterValueException: The specified parameter value is not valid.
            capo_simpledbv2.errors.no_such_export_exception.NoSuchExportException: Export with specified ARN does not exist.
            capo_simpledbv2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get export details

            >>> await client.get_export(export_arn='arn:aws:sdb:us-east-1:123456789012:export/abc123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simpledbv2.types.get_export_request.GetExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_simpledbv2.types.get_export_response.GetExportResponse"
        ]:
            import capo_simpledbv2._operations.simple_d_bv2.get_export

            (
                output,
                http_response,
            ) = await capo_simpledbv2._operations.simple_d_bv2.get_export.async_get_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simpledbv2.types.get_export_request.GetExportRequest = {
            "export_arn": export_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_exports(
        self,
        *,
        config_overrides: Optional[AsyncSimpleDBv2ClientConfig] = None,
        domain_name: Optional["capo_simpledbv2.types.domain_name.DomainName"] = None,
        max_results: Optional["capo_simpledbv2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_simpledbv2.types.next_token.NextToken"] = None,
    ) -> "capo_simpledbv2.types.list_exports_response.ListExportsResponse":
        """Lists all exports that were created. The results are paginated and can be filtered by domain name.

        Args:
            domain_name: The name of the domain to filter exports. If not provided, exports for all the domains will be listed.
            max_results: The maximum number of exports to return in a single response.
            next_token: A pagination token used to retrieve the next page of results. This token is obtained from the nextToken field in the previous ListExportsResponse. Leave empty for the first request.

        Raises:
            capo_simpledbv2.errors.invalid_next_token_exception.InvalidNextTokenException: The specified next token is not valid.
            capo_simpledbv2.errors.invalid_parameter_value_exception.InvalidParameterValueException: The specified parameter value is not valid.
            capo_simpledbv2.errors.no_such_domain_exception.NoSuchDomainException: The specified domain does not exist.
            capo_simpledbv2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all exports

            >>> await client.list_exports()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simpledbv2.types.list_exports_request.ListExportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_simpledbv2.types.list_exports_response.ListExportsResponse"
        ]:
            import capo_simpledbv2._operations.simple_d_bv2.list_exports

            (
                output,
                http_response,
            ) = await capo_simpledbv2._operations.simple_d_bv2.list_exports.async_list_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simpledbv2.types.list_exports_request.ListExportsRequest = {}
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_exports(
        self,
        *,
        config_overrides: Optional[AsyncSimpleDBv2ClientConfig] = None,
        domain_name: Optional["capo_simpledbv2.types.domain_name.DomainName"] = None,
        max_results: Optional["capo_simpledbv2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_simpledbv2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_simpledbv2.types.export_summary.ExportSummary]":
        _token = next_token
        while True:
            _response = await self.list_exports(
                config_overrides=config_overrides,
                domain_name=domain_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("export_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_domain_export(
        self,
        domain_name: "capo_simpledbv2.types.domain_name.DomainName",
        s3_bucket: "capo_simpledbv2.types.s3_bucket_name.S3BucketName",
        *,
        config_overrides: Optional[AsyncSimpleDBv2ClientConfig] = None,
        client_token: Optional[
            "capo_simpledbv2.types.idempotency_token.IdempotencyToken"
        ] = None,
        s3_key_prefix: Optional[
            "capo_simpledbv2.types.s3_key_prefix.S3KeyPrefix"
        ] = None,
        s3_sse_algorithm: Optional[
            "capo_simpledbv2.types.s3_sse_algorithm.S3SseAlgorithm"
        ] = None,
        s3_sse_kms_key_id: Optional[
            "capo_simpledbv2.types.s3_sse_kms_key_id.S3SseKmsKeyId"
        ] = None,
        s3_bucket_owner: Optional[
            "capo_simpledbv2.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "capo_simpledbv2.types.start_domain_export_response.StartDomainExportResponse":
        """Initiates the export of a SimpleDB domain to an S3 bucket.

        Args:
            client_token: Providing a ClientToken makes the call to StartDomainExport API idempotent, meaning that multiple identical calls have the same effect as one single call. A client token is valid for 8 hours after the first request that uses it is completed. After 8 hours, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 8 hours, or the result might not be idempotent. If you submit a request with the same client token but a change in other parameters within the 8-hour idempotency window, a ConflictException will be returned.
            domain_name: The name of the domain to export.
            s3_bucket: The name of the S3 bucket where the domain data will be exported.
            s3_key_prefix: The prefix string to be used to generate the S3 object keys for export artifacts.
            s3_sse_algorithm: The server-side encryption algorithm to use for the exported data in S3. Valid values are: AES256 (SSE-S3) and KMS (SSE-KMS). If not specified, bucket's default encryption will apply.
            s3_sse_kms_key_id: The KMS key ID to use for server-side encryption with AWS KMS-managed keys (SSE-KMS). This parameter is only expected with KMS as the S3 SSE algorithm.
            s3_bucket_owner: The ID of the AWS account that owns the bucket the export will be stored in.

        Raises:
            capo_simpledbv2.errors.conflict_exception.ConflictException: Indicates a conflict with one or more parameters of the request.
            capo_simpledbv2.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: Parameters that must not be used together were used together in the request.
            capo_simpledbv2.errors.invalid_parameter_value_exception.InvalidParameterValueException: The specified parameter value is not valid.
            capo_simpledbv2.errors.no_such_domain_exception.NoSuchDomainException: The specified domain does not exist.
            capo_simpledbv2.errors.number_exports_limit_exceeded.NumberExportsLimitExceeded: Cannot start export as export quota limit was exceeded
            capo_simpledbv2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Start a domain export

            >>> await client.start_domain_export(domain_name='my-domain', s3_bucket='my-export-bucket')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simpledbv2.types.start_domain_export_request.StartDomainExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_simpledbv2.types.start_domain_export_response.StartDomainExportResponse"
        ]:
            import capo_simpledbv2._operations.simple_d_bv2.start_domain_export

            (
                output,
                http_response,
            ) = await capo_simpledbv2._operations.simple_d_bv2.start_domain_export.async_start_domain_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simpledbv2.types.start_domain_export_request.StartDomainExportRequest = {
            "domain_name": domain_name,
            "s3_bucket": s3_bucket,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if s3_key_prefix is not None:
            input_["s3_key_prefix"] = s3_key_prefix
        if s3_sse_algorithm is not None:
            input_["s3_sse_algorithm"] = s3_sse_algorithm
        if s3_sse_kms_key_id is not None:
            input_["s3_sse_kms_key_id"] = s3_sse_kms_key_id
        if s3_bucket_owner is not None:
            input_["s3_bucket_owner"] = s3_bucket_owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
