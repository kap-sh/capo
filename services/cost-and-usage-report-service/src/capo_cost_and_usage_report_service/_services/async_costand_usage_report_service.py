"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#AWSOrigamiServiceGatewayService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_cost_and_usage_report_service._auth._signers
import capo_cost_and_usage_report_service._auth._sigv4
from capo_cost_and_usage_report_service._auth._identity import Credentials
from capo_cost_and_usage_report_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cost_and_usage_report_service._auth._zapros_handler import AuthMiddleware
from capo_cost_and_usage_report_service._pagination import resolve_path as _resolve_path
from capo_cost_and_usage_report_service._services._aws_config import aaws_config
from capo_cost_and_usage_report_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.delete_report_definition_request
    import capo_cost_and_usage_report_service.types.delete_report_definition_response
    import capo_cost_and_usage_report_service.types.describe_report_definitions_request
    import capo_cost_and_usage_report_service.types.describe_report_definitions_response
    import capo_cost_and_usage_report_service.types.generic_string
    import capo_cost_and_usage_report_service.types.list_tags_for_resource_request
    import capo_cost_and_usage_report_service.types.list_tags_for_resource_response
    import capo_cost_and_usage_report_service.types.max_results
    import capo_cost_and_usage_report_service.types.modify_report_definition_request
    import capo_cost_and_usage_report_service.types.modify_report_definition_response
    import capo_cost_and_usage_report_service.types.put_report_definition_request
    import capo_cost_and_usage_report_service.types.put_report_definition_response
    import capo_cost_and_usage_report_service.types.report_definition
    import capo_cost_and_usage_report_service.types.report_name
    import capo_cost_and_usage_report_service.types.tag_key_list
    import capo_cost_and_usage_report_service.types.tag_list
    import capo_cost_and_usage_report_service.types.tag_resource_request
    import capo_cost_and_usage_report_service.types.tag_resource_response
    import capo_cost_and_usage_report_service.types.untag_resource_request
    import capo_cost_and_usage_report_service.types.untag_resource_response


class AsyncCostandUsageReportServiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncCostandUsageReportServiceClient:
    """A client for the ``CostandUsageReportService`` service.

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
        self._config = AsyncCostandUsageReportServiceClientConfig(
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
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCostandUsageReportServiceClientConfig = config_overrides or {}
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
        report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "capo_cost_and_usage_report_service.types.delete_report_definition_response.DeleteReportDefinitionResponse":
        """<p>Deletes the specified report. Any tags associated with the report are also deleted.</p>

        Args:
            report_name: <p>The name of the report that you want to delete. The name must be unique, is case sensitive, and can't include spaces.</p>

        Raises:
            capo_cost_and_usage_report_service.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_and_usage_report_service.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_and_usage_report_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete the AWS Cost and Usage report named ExampleReport.
            The following example deletes the AWS Cost and Usage report named ExampleReport.

            >>> await client.delete_report_definition(report_name='ExampleReport')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cost_and_usage_report_service.types.delete_report_definition_request.DeleteReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_cost_and_usage_report_service.types.delete_report_definition_response.DeleteReportDefinitionResponse"
        ]:
            import capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.delete_report_definition

            (
                output,
                http_response,
            ) = await capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.delete_report_definition.async_delete_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_and_usage_report_service.types.delete_report_definition_request.DeleteReportDefinitionRequest = {
            "report_name": report_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_report_definitions(
        self,
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
        max_results: Optional[
            "capo_cost_and_usage_report_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_cost_and_usage_report_service.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_cost_and_usage_report_service.types.describe_report_definitions_response.DescribeReportDefinitionsResponse":
        """<p>Lists the Amazon Web Services Cost and Usage Report available to this account.</p>

        Raises:
            capo_cost_and_usage_report_service.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_and_usage_report_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the AWS Cost and Usage reports for the account.
            The following example lists the AWS Cost and Usage reports for the account.

            >>> await client.describe_report_definitions(max_results=5)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cost_and_usage_report_service.types.describe_report_definitions_request.DescribeReportDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cost_and_usage_report_service.types.describe_report_definitions_response.DescribeReportDefinitionsResponse"
        ]:
            import capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.describe_report_definitions

            (
                output,
                http_response,
            ) = await capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.describe_report_definitions.async_describe_report_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_and_usage_report_service.types.describe_report_definitions_request.DescribeReportDefinitionsRequest = {}
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

    async def iter_describe_report_definitions(
        self,
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
        max_results: Optional[
            "capo_cost_and_usage_report_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_cost_and_usage_report_service.types.generic_string.GenericString"
        ] = None,
    ) -> "AsyncIterator[capo_cost_and_usage_report_service.types.describe_report_definitions_response.DescribeReportDefinitionsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_report_definitions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "capo_cost_and_usage_report_service.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with the specified report definition.</p>

        Args:
            report_name: <p>The report name of the report definition that tags are to be returned for.</p>

        Raises:
            capo_cost_and_usage_report_service.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_and_usage_report_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified report (<code>ReportName</code>) in the request doesn't exist.</p>
            capo_cost_and_usage_report_service.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_and_usage_report_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cost_and_usage_report_service.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_cost_and_usage_report_service.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_and_usage_report_service.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "report_name": report_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_report_definition(
        self,
        report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName",
        report_definition: "capo_cost_and_usage_report_service.types.report_definition.ReportDefinition",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "capo_cost_and_usage_report_service.types.modify_report_definition_response.ModifyReportDefinitionResponse":
        """<p>Allows you to programmatically update your report preferences.</p>

        Raises:
            capo_cost_and_usage_report_service.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_and_usage_report_service.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_and_usage_report_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cost_and_usage_report_service.types.modify_report_definition_request.ModifyReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_cost_and_usage_report_service.types.modify_report_definition_response.ModifyReportDefinitionResponse"
        ]:
            import capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.modify_report_definition

            (
                output,
                http_response,
            ) = await capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.modify_report_definition.async_modify_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_and_usage_report_service.types.modify_report_definition_request.ModifyReportDefinitionRequest = {
            "report_name": report_name,
            "report_definition": report_definition,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_report_definition(
        self,
        report_definition: "capo_cost_and_usage_report_service.types.report_definition.ReportDefinition",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
        tags: Optional[
            "capo_cost_and_usage_report_service.types.tag_list.TagList"
        ] = None,
    ) -> "capo_cost_and_usage_report_service.types.put_report_definition_response.PutReportDefinitionResponse":
        """<p>Creates a new report using the description that you provide.</p>

        Args:
            report_definition: <p>Represents the output of the PutReportDefinition operation. The content consists of the detailed metadata and data file information. </p>
            tags: <p>The tags to be assigned to the report definition resource.</p>

        Raises:
            capo_cost_and_usage_report_service.errors.duplicate_report_name_exception.DuplicateReportNameException: <p>A report with the specified name already exists in the account. Specify a different report name.</p>
            capo_cost_and_usage_report_service.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_and_usage_report_service.errors.report_limit_reached_exception.ReportLimitReachedException: <p>This account already has five reports defined. To define a new report, you must delete an existing report.</p>
            capo_cost_and_usage_report_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified report (<code>ReportName</code>) in the request doesn't exist.</p>
            capo_cost_and_usage_report_service.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_and_usage_report_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a report named ExampleReport.
            The following example creates a AWS Cost and Usage report named ExampleReport.

            >>> await client.put_report_definition(report_definition={'ReportName': 'ExampleReport', 'TimeUnit': 'DAILY', 'Format': 'textORcsv', 'Compression': 'ZIP', 'AdditionalSchemaElements': ['RESOURCES'], 'S3Bucket': 'example-s3-bucket', 'S3Prefix': 'exampleprefix', 'S3Region': 'us-east-1', 'AdditionalArtifacts': ['REDSHIFT', 'QUICKSIGHT']})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cost_and_usage_report_service.types.put_report_definition_request.PutReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_cost_and_usage_report_service.types.put_report_definition_response.PutReportDefinitionResponse"
        ]:
            import capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.put_report_definition

            (
                output,
                http_response,
            ) = await capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.put_report_definition.async_put_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_and_usage_report_service.types.put_report_definition_request.PutReportDefinitionRequest = {
            "report_definition": report_definition
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName",
        tags: "capo_cost_and_usage_report_service.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "capo_cost_and_usage_report_service.types.tag_resource_response.TagResourceResponse":
        """<p>Associates a set of tags with a report definition.</p>

        Args:
            report_name: <p>The report name of the report definition that tags are to be associated with.</p>
            tags: <p>The tags to be assigned to the report definition resource.</p>

        Raises:
            capo_cost_and_usage_report_service.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_and_usage_report_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified report (<code>ReportName</code>) in the request doesn't exist.</p>
            capo_cost_and_usage_report_service.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_and_usage_report_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cost_and_usage_report_service.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_cost_and_usage_report_service.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_and_usage_report_service.types.tag_resource_request.TagResourceRequest = {
            "report_name": report_name,
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
        report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName",
        tag_keys: "capo_cost_and_usage_report_service.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "capo_cost_and_usage_report_service.types.untag_resource_response.UntagResourceResponse":
        """<p>Disassociates a set of tags from a report definition.</p>

        Args:
            report_name: <p>The report name of the report definition that tags are to be disassociated from.</p>
            tag_keys: <p>The tags to be disassociated from the report definition resource.</p>

        Raises:
            capo_cost_and_usage_report_service.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_and_usage_report_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified report (<code>ReportName</code>) in the request doesn't exist.</p>
            capo_cost_and_usage_report_service.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_and_usage_report_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cost_and_usage_report_service.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_cost_and_usage_report_service.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_and_usage_report_service.types.untag_resource_request.UntagResourceRequest = {
            "report_name": report_name,
            "tag_keys": tag_keys,
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
