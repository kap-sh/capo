"""Generated from Smithy shape ``com.amazonaws.abusesignal#AbuseReportApi``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Literal, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_abuse_signal._auth._signers
import capo_abuse_signal._auth._sigv4
from capo_abuse_signal._auth._identity import Credentials
from capo_abuse_signal._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_abuse_signal._auth._zapros_handler import AuthMiddleware
from capo_abuse_signal._pagination import resolve_path as _resolve_path
from capo_abuse_signal._services._aws_config import aaws_config
from capo_abuse_signal._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    RateLimiter,
    RetryQuota,
    aexecute_pipeline,
    alog_operation,
    arate_limit,
    aretry,
)

if TYPE_CHECKING:
    import capo_abuse_signal.types.client_token
    import capo_abuse_signal.types.correlation_id
    import capo_abuse_signal.types.create_abuse_report_request
    import capo_abuse_signal.types.create_abuse_report_response
    import capo_abuse_signal.types.get_abuse_report_status_request
    import capo_abuse_signal.types.get_abuse_report_status_response
    import capo_abuse_signal.types.list_abuse_report_statuses_request
    import capo_abuse_signal.types.list_abuse_report_statuses_response
    import capo_abuse_signal.types.next_token
    import capo_abuse_signal.types.report_data
    import capo_abuse_signal.types.report_id
    import capo_abuse_signal.types.report_status_list_item


class AsyncAbuseSignalClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    retry_mode: Literal["standard", "adaptive"] | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncAbuseSignalClient:
    """A client for the ``AbuseSignal`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        retry_mode: ``"standard"`` (the default) or ``"adaptive"``, which also slows the whole client down when the service throttles it.
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
        retry_mode: Literal["standard", "adaptive"] | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = AsyncClient(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = RetryQuota()
        # One send-rate limiter too, used when retry_mode is adaptive.
        self._rate_limiter = RateLimiter()
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
                AsyncClient(raw_handler)
            )
        self._config = AsyncAbuseSignalClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "retry_mode": retry_mode,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[AsyncAbuseSignalClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAbuseSignalClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(alog_operation(operation_logging))
        interceptors_.append(aretry())
        interceptors_.append(arate_limit())
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            rate_limiter=self._rate_limiter,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            retry_mode=overrides.get("retry_mode", self._config.get("retry_mode")),
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

    async def create_abuse_report(
        self,
        report: "capo_abuse_signal.types.report_data.ReportData",
        *,
        config_overrides: Optional[AsyncAbuseSignalClientConfig] = None,
        correlation_id: Optional[
            "capo_abuse_signal.types.correlation_id.CorrelationId"
        ] = None,
        client_token: Optional[
            "capo_abuse_signal.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_abuse_signal.types.create_abuse_report_response.CreateAbuseReportResponse"
    ):
        """<p>Submits a structured report. Amazon Web Services validates it and returns a report ID. A successful response confirms that Amazon Web Services received your report. It doesn't mean that Amazon Web Services has reached an outcome. Use <a>GetAbuseReportStatus</a> with the report ID to check the report's status and outcome.</p> <p>This operation is idempotent within a time window. If you provide a <code>clientToken</code>, duplicate requests within 24 hours return the existing report ID. If you omit it, the service generates a token scoped to 5 minutes.</p> <important> <p> <b>Cross-Region data residency:</b> By submitting a report, you instruct Amazon Web Services to store it in all supported Regions (<code>us-east-1</code>, <code>us-west-2</code>, and <code>eu-west-2</code>), including across the United States and Europe. If data must remain in a single Region, do not include it in the report.</p> </important>

        Args:
            report: <p>The abuse report data in XARF format. Provide the report under the <code>xarf</code> key.</p>
            correlation_id: <p>An optional correlation ID for tracking the report in the reporter's system. The service echoes this value back in responses, and you can use it to filter reports with <a>ListAbuseReportStatuses</a>.</p>
            client_token: <p>An optional, client-provided idempotency token that ensures the operation completes no more than once. If the token matches a previous request within 24 hours, the service returns the existing report ID instead of creating a new report. When you omit this token, the service automatically generates one that is scoped to a 5-minute window.</p>

        Raises:
            capo_abuse_signal.errors.access_denied_exception.AccessDeniedException: <p>The caller does not have sufficient access to perform this operation. Verify that the caller has the specific IAM permission for the operation it is calling (for example, <code>abuse:CreateAbuseReport</code>, <code>abuse:GetAbuseReportStatus</code>, or <code>abuse:ListAbuseReportStatuses</code>). Grant only the actions each caller requires.</p>
            capo_abuse_signal.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request. This error is retryable; check the <code>Retry-After</code> header before you retry.</p>
            capo_abuse_signal.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. This error is retryable; retry with exponential backoff.</p>
            capo_abuse_signal.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service, which indicates that the request is not well-formed. Check <code>fieldList</code> for the specific members that failed validation.</p>
            capo_abuse_signal.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, an idempotency token was reused with a different payload.</p>
            capo_abuse_signal.errors.submission_requirement_exception.SubmissionRequirementException: <p>The report is well-formed and satisfies the XARF schema, but it does not meet one or more submission requirements (for example, the submission lookback window or <code>source_identifier</code> restrictions). This error is distinct from <code>ValidationException</code> (HTTP 400), which indicates that the report is not well-formed. Retrying the same report will not succeed; the report content must change.</p>
            capo_abuse_signal.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Submit an abuse report in X-ARF format

            >>> await client.create_abuse_report(report={'xarf': {}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_abuse_signal.types.create_abuse_report_request.CreateAbuseReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_abuse_signal.types.create_abuse_report_response.CreateAbuseReportResponse"
        ]:
            import capo_abuse_signal._operations.abuse_report_api.create_abuse_report

            (
                output,
                http_response,
            ) = await capo_abuse_signal._operations.abuse_report_api.create_abuse_report.async_create_abuse_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_abuse_signal.types.create_abuse_report_request.CreateAbuseReportRequest",
        ) -> dict[str, Any]:
            import capo_abuse_signal.types.create_abuse_report_request

            return capo_abuse_signal.types.create_abuse_report_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateAbuseReport", redact_input=_redact_input),
        )
        input_: capo_abuse_signal.types.create_abuse_report_request.CreateAbuseReportRequest = {
            "report": report
        }
        if correlation_id is not None:
            input_["correlation_id"] = correlation_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_abuse_report_status(
        self,
        report_id: "capo_abuse_signal.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncAbuseSignalClientConfig] = None,
    ) -> "capo_abuse_signal.types.get_abuse_report_status_response.GetAbuseReportStatusResponse":
        """<p>Retrieves the current processing status of a previously submitted abuse report, including the status, submission timestamp, and last-update time.</p> <p>You can poll this operation to track the report's status. <code>PROCESSING</code> confirms that Amazon Web Services received your report and is processing it. <code>COMPLETED</code> means Amazon Web Services finished resolving the report, and the response includes a <code>reasonCode</code>. The time to reach <code>COMPLETED</code> may vary and can take up to several days depending on the scope and complexity of the suspected abuse.</p> <note> <p> <code>COMPLETED</code> is the only terminal status. To wait for a report, use the <code>ReportProcessing</code> waiter, which succeeds when the report reaches <code>PROCESSING</code> or <code>COMPLETED</code>. If you poll this operation yourself, wait 1–5 seconds between calls.</p> </note>

        Args:
            report_id: <p>The unique identifier of the abuse report to retrieve status for. This is the <code>reportId</code> that is returned by <a>CreateAbuseReport</a>.</p>

        Raises:
            capo_abuse_signal.errors.access_denied_exception.AccessDeniedException: <p>The caller does not have sufficient access to perform this operation. Verify that the caller has the specific IAM permission for the operation it is calling (for example, <code>abuse:CreateAbuseReport</code>, <code>abuse:GetAbuseReportStatus</code>, or <code>abuse:ListAbuseReportStatuses</code>). Grant only the actions each caller requires.</p>
            capo_abuse_signal.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request. This error is retryable; check the <code>Retry-After</code> header before you retry.</p>
            capo_abuse_signal.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. This error is retryable; retry with exponential backoff.</p>
            capo_abuse_signal.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service, which indicates that the request is not well-formed. Check <code>fieldList</code> for the specific members that failed validation.</p>
            capo_abuse_signal.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the <code>reportId</code> is correct.</p>
            capo_abuse_signal.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the status of a submitted report

            >>> await client.get_abuse_report_status(report_id='rpt5a8b3c2d1e4f6g7h8i9j0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_abuse_signal.types.get_abuse_report_status_request.GetAbuseReportStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_abuse_signal.types.get_abuse_report_status_response.GetAbuseReportStatusResponse"
        ]:
            import capo_abuse_signal._operations.abuse_report_api.get_abuse_report_status

            (
                output,
                http_response,
            ) = await capo_abuse_signal._operations.abuse_report_api.get_abuse_report_status.async_get_abuse_report_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetAbuseReportStatus")
        )
        input_: capo_abuse_signal.types.get_abuse_report_status_request.GetAbuseReportStatusRequest = {
            "report_id": report_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_abuse_report_statuses(
        self,
        *,
        config_overrides: Optional[AsyncAbuseSignalClientConfig] = None,
        correlation_id: Optional[
            "capo_abuse_signal.types.correlation_id.CorrelationId"
        ] = None,
        next_token: Optional["capo_abuse_signal.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_abuse_signal.types.list_abuse_report_statuses_response.ListAbuseReportStatusesResponse":
        """<p>Lists abuse report statuses for the calling account, ordered by submission time, with optional filtering and pagination.</p> <p>Use the <code>correlationId</code> parameter to filter results by the reporter-provided correlation ID that was specified during report submission.</p> <p>Results are paginated. Use <code>nextToken</code> to retrieve additional results.</p>

        Args:
            correlation_id: <p>Filters results by the reporter-provided correlation ID.</p>
            next_token: <p>The pagination token for retrieving the next page of results. Omit this parameter to return the first page of results.</p>
            max_results: <p>The maximum number of results to return in a single page. Valid range: 1–50. The default is 50.</p>

        Raises:
            capo_abuse_signal.errors.access_denied_exception.AccessDeniedException: <p>The caller does not have sufficient access to perform this operation. Verify that the caller has the specific IAM permission for the operation it is calling (for example, <code>abuse:CreateAbuseReport</code>, <code>abuse:GetAbuseReportStatus</code>, or <code>abuse:ListAbuseReportStatuses</code>). Grant only the actions each caller requires.</p>
            capo_abuse_signal.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request. This error is retryable; check the <code>Retry-After</code> header before you retry.</p>
            capo_abuse_signal.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. This error is retryable; retry with exponential backoff.</p>
            capo_abuse_signal.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service, which indicates that the request is not well-formed. Check <code>fieldList</code> for the specific members that failed validation.</p>
            capo_abuse_signal.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List abuse report statuses

            >>> await client.list_abuse_report_statuses()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_abuse_signal.types.list_abuse_report_statuses_request.ListAbuseReportStatusesRequest]",
        ) -> AsyncOperationResponse[
            "capo_abuse_signal.types.list_abuse_report_statuses_response.ListAbuseReportStatusesResponse"
        ]:
            import capo_abuse_signal._operations.abuse_report_api.list_abuse_report_statuses

            (
                output,
                http_response,
            ) = await capo_abuse_signal._operations.abuse_report_api.list_abuse_report_statuses.async_list_abuse_report_statuses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListAbuseReportStatuses")
        )
        input_: capo_abuse_signal.types.list_abuse_report_statuses_request.ListAbuseReportStatusesRequest = {}
        if correlation_id is not None:
            input_["correlation_id"] = correlation_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_abuse_report_statuses(
        self,
        *,
        config_overrides: Optional[AsyncAbuseSignalClientConfig] = None,
        correlation_id: Optional[
            "capo_abuse_signal.types.correlation_id.CorrelationId"
        ] = None,
        next_token: Optional["capo_abuse_signal.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_abuse_signal.types.report_status_list_item.ReportStatusListItem]":
        _token = next_token
        while True:
            _response = await self.list_abuse_report_statuses(
                config_overrides=config_overrides,
                correlation_id=correlation_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("reports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
