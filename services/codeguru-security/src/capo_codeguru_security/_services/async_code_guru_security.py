"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#AwsCodeGuruSecurity``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_codeguru_security._auth._signers
import capo_codeguru_security._auth._sigv4
from capo_codeguru_security._auth._identity import Credentials
from capo_codeguru_security._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_codeguru_security._auth._zapros_handler import AuthMiddleware
from capo_codeguru_security._pagination import resolve_path as _resolve_path
from capo_codeguru_security._services._aws_config import aaws_config
from capo_codeguru_security._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_codeguru_security.types.account_findings_metric
    import capo_codeguru_security.types.analysis_type
    import capo_codeguru_security.types.batch_get_findings_request
    import capo_codeguru_security.types.batch_get_findings_response
    import capo_codeguru_security.types.client_token
    import capo_codeguru_security.types.create_scan_request
    import capo_codeguru_security.types.create_scan_response
    import capo_codeguru_security.types.create_upload_url_request
    import capo_codeguru_security.types.create_upload_url_response
    import capo_codeguru_security.types.encryption_config
    import capo_codeguru_security.types.finding
    import capo_codeguru_security.types.finding_identifiers
    import capo_codeguru_security.types.get_account_configuration_request
    import capo_codeguru_security.types.get_account_configuration_response
    import capo_codeguru_security.types.get_findings_request
    import capo_codeguru_security.types.get_findings_response
    import capo_codeguru_security.types.get_metrics_summary_request
    import capo_codeguru_security.types.get_metrics_summary_response
    import capo_codeguru_security.types.get_scan_request
    import capo_codeguru_security.types.get_scan_response
    import capo_codeguru_security.types.list_findings_metrics_request
    import capo_codeguru_security.types.list_findings_metrics_response
    import capo_codeguru_security.types.list_scans_request
    import capo_codeguru_security.types.list_scans_response
    import capo_codeguru_security.types.list_tags_for_resource_request
    import capo_codeguru_security.types.list_tags_for_resource_response
    import capo_codeguru_security.types.next_token
    import capo_codeguru_security.types.resource_id
    import capo_codeguru_security.types.scan_name
    import capo_codeguru_security.types.scan_name_arn
    import capo_codeguru_security.types.scan_summary
    import capo_codeguru_security.types.scan_type
    import capo_codeguru_security.types.status
    import capo_codeguru_security.types.tag_key_list
    import capo_codeguru_security.types.tag_map
    import capo_codeguru_security.types.tag_resource_request
    import capo_codeguru_security.types.tag_resource_response
    import capo_codeguru_security.types.untag_resource_request
    import capo_codeguru_security.types.untag_resource_response
    import capo_codeguru_security.types.update_account_configuration_request
    import capo_codeguru_security.types.update_account_configuration_response
    import capo_codeguru_security.types.uuid


class AsyncCodeGuruSecurityClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncCodeGuruSecurityClient:
    """A client for the ``CodeGuruSecurity`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncCodeGuruSecurityClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCodeGuruSecurityClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def batch_get_findings(
        self,
        finding_identifiers: "capo_codeguru_security.types.finding_identifiers.FindingIdentifiers",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
    ) -> "capo_codeguru_security.types.batch_get_findings_response.BatchGetFindingsResponse":
        """<p>Returns a list of requested findings from standard scans.</p>

        Args:
            finding_identifiers: <p>A list of finding identifiers. Each identifier consists of a <code>scanName</code> and a <code>findingId</code>. You retrieve the <code>findingId</code> when you call <code>GetFindings</code>.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.batch_get_findings_request.BatchGetFindingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.batch_get_findings_response.BatchGetFindingsResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.batch_get_findings

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.batch_get_findings.async_batch_get_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.batch_get_findings_request.BatchGetFindingsRequest = {
            "finding_identifiers": finding_identifiers
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_scan(
        self,
        resource_id: "capo_codeguru_security.types.resource_id.ResourceId",
        scan_name: "capo_codeguru_security.types.scan_name.ScanName",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
        client_token: Optional[
            "capo_codeguru_security.types.client_token.ClientToken"
        ] = None,
        scan_type: Optional["capo_codeguru_security.types.scan_type.ScanType"] = None,
        analysis_type: Optional[
            "capo_codeguru_security.types.analysis_type.AnalysisType"
        ] = None,
        tags: Optional["capo_codeguru_security.types.tag_map.TagMap"] = None,
    ) -> "capo_codeguru_security.types.create_scan_response.CreateScanResponse":
        """<p>Use to create a scan using code uploaded to an Amazon S3 bucket.</p>

        Args:
            client_token: <p>The idempotency token for the request. Amazon CodeGuru Security uses this value to prevent the accidental creation of duplicate scans if there are failures and retries.</p>
            resource_id: <p>The identifier for the resource object to be scanned.</p>
            scan_name: <p>The unique name that CodeGuru Security uses to track revisions across multiple scans of the same resource. Only allowed for a <code>STANDARD</code> scan type. </p>
            scan_type: <p>The type of scan, either <code>Standard</code> or <code>Express</code>. Defaults to <code>Standard</code> type if missing.</p> <p> <code>Express</code> scans run on limited resources and use a limited set of detectors to analyze your code in near-real time. <code>Standard</code> scans have standard resource limits and use the full set of detectors to analyze your code.</p>
            analysis_type: <p>The type of analysis you want CodeGuru Security to perform in the scan, either <code>Security</code> or <code>All</code>. The <code>Security</code> type only generates findings related to security. The <code>All</code> type generates both security findings and quality findings. Defaults to <code>Security</code> type if missing.</p>
            tags: <p>An array of key-value pairs used to tag a scan. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A tag key. For example, <code>CostCenter</code>, <code>Environment</code>, or <code>Secret</code>. Tag keys are case sensitive.</p> </li> <li> <p>An optional tag value field. For example, <code>111122223333</code>, <code>Production</code>, or a team name. Omitting the tag value is the same as using an empty string. Tag values are case sensitive.</p> </li> </ul>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.create_scan_request.CreateScanRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.create_scan_response.CreateScanResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.create_scan

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.create_scan.async_create_scan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.create_scan_request.CreateScanRequest = {
            "resource_id": resource_id,
            "scan_name": scan_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if scan_type is not None:
            input_["scan_type"] = scan_type
        if analysis_type is not None:
            input_["analysis_type"] = analysis_type
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_upload_url(
        self,
        scan_name: "capo_codeguru_security.types.scan_name.ScanName",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
    ) -> "capo_codeguru_security.types.create_upload_url_response.CreateUploadUrlResponse":
        """<p>Generates a pre-signed URL, request headers used to upload a code resource, and code artifact identifier for the uploaded resource.</p> <p>You can upload your code resource to the URL with the request headers using any HTTP client.</p>

        Args:
            scan_name: <p>The name of the scan that will use the uploaded resource. CodeGuru Security uses the unique scan name to track revisions across multiple scans of the same resource. Use this <code>scanName</code> when you call <code>CreateScan</code> on the code resource you upload to this URL.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.create_upload_url_request.CreateUploadUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.create_upload_url_response.CreateUploadUrlResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.create_upload_url

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.create_upload_url.async_create_upload_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.create_upload_url_request.CreateUploadUrlRequest = {
            "scan_name": scan_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account_configuration(
        self, *, config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None
    ) -> "capo_codeguru_security.types.get_account_configuration_response.GetAccountConfigurationResponse":
        """<p>Use to get the encryption configuration for an account.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.get_account_configuration_request.GetAccountConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.get_account_configuration_response.GetAccountConfigurationResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.get_account_configuration

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.get_account_configuration.async_get_account_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.get_account_configuration_request.GetAccountConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_findings(
        self,
        scan_name: "capo_codeguru_security.types.scan_name.ScanName",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_security.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
        status: Optional["capo_codeguru_security.types.status.Status"] = None,
    ) -> "capo_codeguru_security.types.get_findings_response.GetFindingsResponse":
        """<p>Returns a list of all findings generated by a particular scan.</p>

        Args:
            scan_name: <p>The name of the scan you want to retrieve findings from.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the <code>nextToken</code> element is returned in the response. Use <code>nextToken</code> in a subsequent request to retrieve additional results. If not specified, returns 1000 results.</p>
            status: <p>The status of the findings you want to get. Pass either <code>Open</code>, <code>Closed</code>, or <code>All</code>.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.get_findings_request.GetFindingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.get_findings_response.GetFindingsResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.get_findings

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.get_findings.async_get_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.get_findings_request.GetFindingsRequest = {
            "scan_name": scan_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_findings(
        self,
        scan_name: "capo_codeguru_security.types.scan_name.ScanName",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_security.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
        status: Optional["capo_codeguru_security.types.status.Status"] = None,
    ) -> "AsyncIterator[capo_codeguru_security.types.finding.Finding]":
        _token = next_token
        while True:
            _response = await self.get_findings(
                scan_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
            )
            _page = _resolve_path(_response, ("findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_metrics_summary(
        self,
        date: datetime.datetime,
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
    ) -> "capo_codeguru_security.types.get_metrics_summary_response.GetMetricsSummaryResponse":
        """<p>Returns a summary of metrics for an account from a specified date, including number of open findings, the categories with most findings, the scans with most open findings, and scans with most open critical findings. </p>

        Args:
            date: <p>The date you want to retrieve summary metrics from, rounded to the nearest day. The date must be within the past two years.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.get_metrics_summary_request.GetMetricsSummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.get_metrics_summary_response.GetMetricsSummaryResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.get_metrics_summary

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.get_metrics_summary.async_get_metrics_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.get_metrics_summary_request.GetMetricsSummaryRequest = {
            "date": date
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_scan(
        self,
        scan_name: "capo_codeguru_security.types.scan_name.ScanName",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
        run_id: Optional["capo_codeguru_security.types.uuid.Uuid"] = None,
    ) -> "capo_codeguru_security.types.get_scan_response.GetScanResponse":
        """<p>Returns details about a scan, including whether or not a scan has completed.</p>

        Args:
            scan_name: <p>The name of the scan you want to view details about.</p>
            run_id: <p>UUID that identifies the individual scan run you want to view details about. You retrieve this when you call the <code>CreateScan</code> operation. Defaults to the latest scan run if missing.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.get_scan_request.GetScanRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.get_scan_response.GetScanResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.get_scan

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.get_scan.async_get_scan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.get_scan_request.GetScanRequest = {
            "scan_name": scan_name
        }
        if run_id is not None:
            input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_findings_metrics(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_security.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_codeguru_security.types.list_findings_metrics_response.ListFindingsMetricsResponse":
        """<p>Returns metrics about all findings in an account within a specified time range.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the <code>nextToken</code> element is returned in the response. Use <code>nextToken</code> in a subsequent request to retrieve additional results. If not specified, returns 1000 results.</p>
            start_date: <p>The start date of the interval which you want to retrieve metrics from. Rounds to the nearest day.</p>
            end_date: <p>The end date of the interval which you want to retrieve metrics from. Round to the nearest day.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.list_findings_metrics_request.ListFindingsMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.list_findings_metrics_response.ListFindingsMetricsResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.list_findings_metrics

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.list_findings_metrics.async_list_findings_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.list_findings_metrics_request.ListFindingsMetricsRequest = {
            "start_date": start_date,
            "end_date": end_date,
        }
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

    async def iter_list_findings_metrics(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_security.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_codeguru_security.types.account_findings_metric.AccountFindingsMetric]":
        _token = next_token
        while True:
            _response = await self.list_findings_metrics(
                start_date,
                end_date,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("findings_metrics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_scans(
        self,
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_security.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_codeguru_security.types.list_scans_response.ListScansResponse":
        """<p>Returns a list of all scans in an account. Does not return <code>EXPRESS</code> scans.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the <code>nextToken</code> element is returned in the response. Use <code>nextToken</code> in a subsequent request to retrieve additional results. If not specified, returns 100 results.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.list_scans_request.ListScansRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.list_scans_response.ListScansResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.list_scans

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.list_scans.async_list_scans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.list_scans_request.ListScansRequest = {}
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

    async def iter_list_scans(
        self,
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_security.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_codeguru_security.types.scan_summary.ScanSummary]":
        _token = next_token
        while True:
            _response = await self.list_scans(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_codeguru_security.types.scan_name_arn.ScanNameArn",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
    ) -> "capo_codeguru_security.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of all tags associated with a scan.</p>

        Args:
            resource_arn: <p>The ARN of the <code>ScanName</code> object. You can retrieve this ARN by calling <code>CreateScan</code>, <code>ListScans</code>, or <code>GetScan</code>.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_codeguru_security.types.scan_name_arn.ScanNameArn",
        tags: "capo_codeguru_security.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
    ) -> "capo_codeguru_security.types.tag_resource_response.TagResourceResponse":
        """<p>Use to add one or more tags to an existing scan.</p>

        Args:
            resource_arn: <p>The ARN of the <code>ScanName</code> object. You can retrieve this ARN by calling <code>CreateScan</code>, <code>ListScans</code>, or <code>GetScan</code>.</p>
            tags: <p>An array of key-value pairs used to tag an existing scan. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A tag key. For example, <code>CostCenter</code>, <code>Environment</code>, or <code>Secret</code>. Tag keys are case sensitive.</p> </li> <li> <p>An optional tag value field. For example, <code>111122223333</code>, <code>Production</code>, or a team name. Omitting the tag value is the same as using an empty string. Tag values are case sensitive.</p> </li> </ul>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.tag_resource

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_codeguru_security.types.scan_name_arn.ScanNameArn",
        tag_keys: "capo_codeguru_security.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
    ) -> "capo_codeguru_security.types.untag_resource_response.UntagResourceResponse":
        """<p>Use to remove one or more tags from an existing scan.</p>

        Args:
            resource_arn: <p>The ARN of the <code>ScanName</code> object. You can retrieve this ARN by calling <code>CreateScan</code>, <code>ListScans</code>, or <code>GetScan</code>.</p>
            tag_keys: <p>A list of keys for each tag you want to remove from a scan.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.untag_resource

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_account_configuration(
        self,
        encryption_config: "capo_codeguru_security.types.encryption_config.EncryptionConfig",
        *,
        config_overrides: Optional[AsyncCodeGuruSecurityClientConfig] = None,
    ) -> "capo_codeguru_security.types.update_account_configuration_response.UpdateAccountConfigurationResponse":
        """<p>Use to update the encryption configuration for an account.</p>

        Args:
            encryption_config: <p>The customer-managed KMS key ARN you want to use for encryption. If not specified, CodeGuru Security will use an AWS-managed key for encryption. If you previously specified a customer-managed KMS key and want CodeGuru Security to use an AWS-managed key for encryption instead, pass nothing.</p>

        Raises:
            capo_codeguru_security.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_security.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_security.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_codeguru_security.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_security.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_security.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_security.types.update_account_configuration_request.UpdateAccountConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_security.types.update_account_configuration_response.UpdateAccountConfigurationResponse"
        ]:
            import capo_codeguru_security._operations.aws_code_guru_security.update_account_configuration

            (
                output,
                http_response,
            ) = await capo_codeguru_security._operations.aws_code_guru_security.update_account_configuration.async_update_account_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_security.types.update_account_configuration_request.UpdateAccountConfigurationRequest = {
            "encryption_config": encryption_config
        }

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
