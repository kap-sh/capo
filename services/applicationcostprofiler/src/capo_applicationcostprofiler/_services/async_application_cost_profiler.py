"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#AWSApplicationCostProfiler``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_applicationcostprofiler._auth._signers
import capo_applicationcostprofiler._auth._sigv4
from capo_applicationcostprofiler._auth._identity import Credentials
from capo_applicationcostprofiler._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_applicationcostprofiler._auth._zapros_handler import AuthMiddleware
from capo_applicationcostprofiler._pagination import resolve_path as _resolve_path
from capo_applicationcostprofiler._services._aws_config import aaws_config
from capo_applicationcostprofiler._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.delete_report_definition_request
    import capo_applicationcostprofiler.types.delete_report_definition_result
    import capo_applicationcostprofiler.types.format
    import capo_applicationcostprofiler.types.get_report_definition_request
    import capo_applicationcostprofiler.types.get_report_definition_result
    import capo_applicationcostprofiler.types.import_application_usage_request
    import capo_applicationcostprofiler.types.import_application_usage_result
    import capo_applicationcostprofiler.types.integer
    import capo_applicationcostprofiler.types.list_report_definitions_request
    import capo_applicationcostprofiler.types.list_report_definitions_result
    import capo_applicationcostprofiler.types.put_report_definition_request
    import capo_applicationcostprofiler.types.put_report_definition_result
    import capo_applicationcostprofiler.types.report_definition
    import capo_applicationcostprofiler.types.report_description
    import capo_applicationcostprofiler.types.report_frequency
    import capo_applicationcostprofiler.types.report_id
    import capo_applicationcostprofiler.types.s3_location
    import capo_applicationcostprofiler.types.source_s3_location
    import capo_applicationcostprofiler.types.token
    import capo_applicationcostprofiler.types.update_report_definition_request
    import capo_applicationcostprofiler.types.update_report_definition_result


class AsyncApplicationCostProfilerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncApplicationCostProfilerClient:
    """A client for the ``ApplicationCostProfiler`` service.

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
        self._config = AsyncApplicationCostProfilerClientConfig(
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
        self,
        config_overrides: Optional[AsyncApplicationCostProfilerClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncApplicationCostProfilerClientConfig = config_overrides or {}
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

    async def delete_report_definition(
        self,
        report_id: "capo_applicationcostprofiler.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncApplicationCostProfilerClientConfig] = None,
    ) -> "capo_applicationcostprofiler.types.delete_report_definition_result.DeleteReportDefinitionResult":
        """<p>Deletes the specified report definition in AWS Application Cost Profiler. This stops the report from being generated.</p>

        Args:
            report_id: <p>Required. ID of the report to delete.</p>

        Raises:
            capo_applicationcostprofiler.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this action.</p>
            capo_applicationcostprofiler.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_applicationcostprofiler.errors.throttling_exception.ThrottlingException: <p>The calls to AWS Application Cost Profiler API are throttled. The request was denied.</p>
            capo_applicationcostprofiler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints for the API.</p>
            capo_applicationcostprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_applicationcostprofiler.types.delete_report_definition_request.DeleteReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_applicationcostprofiler.types.delete_report_definition_result.DeleteReportDefinitionResult"
        ]:
            import capo_applicationcostprofiler._operations.aws_application_cost_profiler.delete_report_definition

            (
                output,
                http_response,
            ) = await capo_applicationcostprofiler._operations.aws_application_cost_profiler.delete_report_definition.async_delete_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_applicationcostprofiler.types.delete_report_definition_request.DeleteReportDefinitionRequest = {
            "report_id": report_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_report_definition(
        self,
        report_id: "capo_applicationcostprofiler.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncApplicationCostProfilerClientConfig] = None,
    ) -> "capo_applicationcostprofiler.types.get_report_definition_result.GetReportDefinitionResult":
        """<p>Retrieves the definition of a report already configured in AWS Application Cost Profiler.</p>

        Args:
            report_id: <p>ID of the report to retrieve.</p>

        Raises:
            capo_applicationcostprofiler.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this action.</p>
            capo_applicationcostprofiler.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_applicationcostprofiler.errors.throttling_exception.ThrottlingException: <p>The calls to AWS Application Cost Profiler API are throttled. The request was denied.</p>
            capo_applicationcostprofiler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints for the API.</p>
            capo_applicationcostprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_applicationcostprofiler.types.get_report_definition_request.GetReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_applicationcostprofiler.types.get_report_definition_result.GetReportDefinitionResult"
        ]:
            import capo_applicationcostprofiler._operations.aws_application_cost_profiler.get_report_definition

            (
                output,
                http_response,
            ) = await capo_applicationcostprofiler._operations.aws_application_cost_profiler.get_report_definition.async_get_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_applicationcostprofiler.types.get_report_definition_request.GetReportDefinitionRequest = {
            "report_id": report_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_application_usage(
        self,
        source_s3_location: "capo_applicationcostprofiler.types.source_s3_location.SourceS3Location",
        *,
        config_overrides: Optional[AsyncApplicationCostProfilerClientConfig] = None,
    ) -> "capo_applicationcostprofiler.types.import_application_usage_result.ImportApplicationUsageResult":
        """<p>Ingests application usage data from Amazon Simple Storage Service (Amazon S3).</p> <p>The data must already exist in the S3 location. As part of the action, AWS Application Cost Profiler copies the object from your S3 bucket to an S3 bucket owned by Amazon for processing asynchronously.</p>

        Args:
            source_s3_location: <p>Amazon S3 location to import application usage data from.</p>

        Raises:
            capo_applicationcostprofiler.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this action.</p>
            capo_applicationcostprofiler.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_applicationcostprofiler.errors.throttling_exception.ThrottlingException: <p>The calls to AWS Application Cost Profiler API are throttled. The request was denied.</p>
            capo_applicationcostprofiler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints for the API.</p>
            capo_applicationcostprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_applicationcostprofiler.types.import_application_usage_request.ImportApplicationUsageRequest]",
        ) -> AsyncOperationResponse[
            "capo_applicationcostprofiler.types.import_application_usage_result.ImportApplicationUsageResult"
        ]:
            import capo_applicationcostprofiler._operations.aws_application_cost_profiler.import_application_usage

            (
                output,
                http_response,
            ) = await capo_applicationcostprofiler._operations.aws_application_cost_profiler.import_application_usage.async_import_application_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_applicationcostprofiler.types.import_application_usage_request.ImportApplicationUsageRequest = {
            "source_s3_location": source_s3_location
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_report_definitions(
        self,
        *,
        config_overrides: Optional[AsyncApplicationCostProfilerClientConfig] = None,
        next_token: Optional["capo_applicationcostprofiler.types.token.Token"] = None,
        max_results: Optional[
            "capo_applicationcostprofiler.types.integer.Integer"
        ] = None,
    ) -> "capo_applicationcostprofiler.types.list_report_definitions_result.ListReportDefinitionsResult":
        """<p>Retrieves a list of all reports and their configurations for your AWS account.</p> <p>The maximum number of reports is one.</p>

        Args:
            next_token: <p>The token value from a previous call to access the next page of results.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_applicationcostprofiler.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this action.</p>
            capo_applicationcostprofiler.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_applicationcostprofiler.errors.throttling_exception.ThrottlingException: <p>The calls to AWS Application Cost Profiler API are throttled. The request was denied.</p>
            capo_applicationcostprofiler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints for the API.</p>
            capo_applicationcostprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_applicationcostprofiler.types.list_report_definitions_request.ListReportDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_applicationcostprofiler.types.list_report_definitions_result.ListReportDefinitionsResult"
        ]:
            import capo_applicationcostprofiler._operations.aws_application_cost_profiler.list_report_definitions

            (
                output,
                http_response,
            ) = await capo_applicationcostprofiler._operations.aws_application_cost_profiler.list_report_definitions.async_list_report_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_applicationcostprofiler.types.list_report_definitions_request.ListReportDefinitionsRequest = {}
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

    async def iter_list_report_definitions(
        self,
        *,
        config_overrides: Optional[AsyncApplicationCostProfilerClientConfig] = None,
        next_token: Optional["capo_applicationcostprofiler.types.token.Token"] = None,
        max_results: Optional[
            "capo_applicationcostprofiler.types.integer.Integer"
        ] = None,
    ) -> "AsyncIterator[capo_applicationcostprofiler.types.report_definition.ReportDefinition]":
        _token = next_token
        while True:
            _response = await self.list_report_definitions(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("report_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_report_definition(
        self,
        report_id: "capo_applicationcostprofiler.types.report_id.ReportId",
        report_description: "capo_applicationcostprofiler.types.report_description.ReportDescription",
        report_frequency: "capo_applicationcostprofiler.types.report_frequency.ReportFrequency",
        format: "capo_applicationcostprofiler.types.format.Format",
        destination_s3_location: "capo_applicationcostprofiler.types.s3_location.S3Location",
        *,
        config_overrides: Optional[AsyncApplicationCostProfilerClientConfig] = None,
    ) -> "capo_applicationcostprofiler.types.put_report_definition_result.PutReportDefinitionResult":
        """<p>Creates the report definition for a report in Application Cost Profiler.</p>

        Args:
            report_id: <p>Required. ID of the report. You can choose any valid string matching the pattern for the ID.</p>
            report_description: <p>Required. Description of the report.</p>
            report_frequency: <p>Required. The cadence to generate the report.</p>
            format: <p>Required. The format to use for the generated report.</p>
            destination_s3_location: <p>Required. Amazon Simple Storage Service (Amazon S3) location where Application Cost Profiler uploads the report.</p>

        Raises:
            capo_applicationcostprofiler.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this action.</p>
            capo_applicationcostprofiler.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_applicationcostprofiler.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds one or more of the service quotas.</p>
            capo_applicationcostprofiler.errors.throttling_exception.ThrottlingException: <p>The calls to AWS Application Cost Profiler API are throttled. The request was denied.</p>
            capo_applicationcostprofiler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints for the API.</p>
            capo_applicationcostprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_applicationcostprofiler.types.put_report_definition_request.PutReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_applicationcostprofiler.types.put_report_definition_result.PutReportDefinitionResult"
        ]:
            import capo_applicationcostprofiler._operations.aws_application_cost_profiler.put_report_definition

            (
                output,
                http_response,
            ) = await capo_applicationcostprofiler._operations.aws_application_cost_profiler.put_report_definition.async_put_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_applicationcostprofiler.types.put_report_definition_request.PutReportDefinitionRequest = {
            "report_id": report_id,
            "report_description": report_description,
            "report_frequency": report_frequency,
            "format": format,
            "destination_s3_location": destination_s3_location,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_report_definition(
        self,
        report_id: "capo_applicationcostprofiler.types.report_id.ReportId",
        report_description: "capo_applicationcostprofiler.types.report_description.ReportDescription",
        report_frequency: "capo_applicationcostprofiler.types.report_frequency.ReportFrequency",
        format: "capo_applicationcostprofiler.types.format.Format",
        destination_s3_location: "capo_applicationcostprofiler.types.s3_location.S3Location",
        *,
        config_overrides: Optional[AsyncApplicationCostProfilerClientConfig] = None,
    ) -> "capo_applicationcostprofiler.types.update_report_definition_result.UpdateReportDefinitionResult":
        """<p>Updates existing report in AWS Application Cost Profiler.</p>

        Args:
            report_id: <p>Required. ID of the report to update.</p>
            report_description: <p>Required. Description of the report.</p>
            report_frequency: <p>Required. The cadence to generate the report.</p>
            format: <p>Required. The format to use for the generated report.</p>
            destination_s3_location: <p>Required. Amazon Simple Storage Service (Amazon S3) location where Application Cost Profiler uploads the report.</p>

        Raises:
            capo_applicationcostprofiler.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this action.</p>
            capo_applicationcostprofiler.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_applicationcostprofiler.errors.throttling_exception.ThrottlingException: <p>The calls to AWS Application Cost Profiler API are throttled. The request was denied.</p>
            capo_applicationcostprofiler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints for the API.</p>
            capo_applicationcostprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_applicationcostprofiler.types.update_report_definition_request.UpdateReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_applicationcostprofiler.types.update_report_definition_result.UpdateReportDefinitionResult"
        ]:
            import capo_applicationcostprofiler._operations.aws_application_cost_profiler.update_report_definition

            (
                output,
                http_response,
            ) = await capo_applicationcostprofiler._operations.aws_application_cost_profiler.update_report_definition.async_update_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_applicationcostprofiler.types.update_report_definition_request.UpdateReportDefinitionRequest = {
            "report_id": report_id,
            "report_description": report_description,
            "report_frequency": report_frequency,
            "format": format,
            "destination_s3_location": destination_s3_location,
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
