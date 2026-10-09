"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#AWSBillingAndCostManagementDataExports``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_bcm_data_exports._auth._signers
import capo_bcm_data_exports._auth._sigv4
from capo_bcm_data_exports._auth._identity import Credentials
from capo_bcm_data_exports._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bcm_data_exports._auth._zapros_handler import AuthMiddleware
from capo_bcm_data_exports._pagination import resolve_path as _resolve_path
from capo_bcm_data_exports._resources.aws_billing_and_cost_management_data_exports.data_export import (
    AsyncDataExport,
)
from capo_bcm_data_exports._services._aws_config import aaws_config
from capo_bcm_data_exports._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn
    import capo_bcm_data_exports.types.create_export_request
    import capo_bcm_data_exports.types.create_export_response
    import capo_bcm_data_exports.types.delete_export_request
    import capo_bcm_data_exports.types.delete_export_response
    import capo_bcm_data_exports.types.execution_reference
    import capo_bcm_data_exports.types.export
    import capo_bcm_data_exports.types.export_reference
    import capo_bcm_data_exports.types.generic_string
    import capo_bcm_data_exports.types.get_execution_request
    import capo_bcm_data_exports.types.get_execution_response
    import capo_bcm_data_exports.types.get_export_request
    import capo_bcm_data_exports.types.get_export_response
    import capo_bcm_data_exports.types.get_table_request
    import capo_bcm_data_exports.types.get_table_response
    import capo_bcm_data_exports.types.list_executions_request
    import capo_bcm_data_exports.types.list_executions_response
    import capo_bcm_data_exports.types.list_exports_request
    import capo_bcm_data_exports.types.list_exports_response
    import capo_bcm_data_exports.types.list_tables_request
    import capo_bcm_data_exports.types.list_tables_response
    import capo_bcm_data_exports.types.list_tags_for_resource_request
    import capo_bcm_data_exports.types.list_tags_for_resource_response
    import capo_bcm_data_exports.types.max_results
    import capo_bcm_data_exports.types.next_page_token
    import capo_bcm_data_exports.types.resource_tag_key_list
    import capo_bcm_data_exports.types.resource_tag_list
    import capo_bcm_data_exports.types.table
    import capo_bcm_data_exports.types.table_name
    import capo_bcm_data_exports.types.table_properties
    import capo_bcm_data_exports.types.tag_resource_request
    import capo_bcm_data_exports.types.tag_resource_response
    import capo_bcm_data_exports.types.untag_resource_request
    import capo_bcm_data_exports.types.untag_resource_response
    import capo_bcm_data_exports.types.update_export_request
    import capo_bcm_data_exports.types.update_export_response


class AsyncBCMDataExportsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncBCMDataExportsClient:
    """A client for the ``BCMDataExports`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        self._config = AsyncBCMDataExportsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.data_export = AsyncDataExport(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBCMDataExportsClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def get_execution(
        self,
        export_arn: "capo_bcm_data_exports.types.arn.Arn",
        execution_id: "capo_bcm_data_exports.types.generic_string.GenericString",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
    ) -> "capo_bcm_data_exports.types.get_execution_response.GetExecutionResponse":
        """<p>Exports data based on the source data update.</p>

        Args:
            export_arn: <p>The Amazon Resource Name (ARN) of the Export object that generated this specific execution.</p>
            execution_id: <p>The ID for this specific execution.</p>

        Raises:
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Resource Name (ARN) in the request doesn't exist.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.get_execution_request.GetExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.get_execution_response.GetExecutionResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_execution

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_execution.async_get_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.get_execution_request.GetExecutionRequest = {
            "export_arn": export_arn,
            "execution_id": execution_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table(
        self,
        table_name: "capo_bcm_data_exports.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
        table_properties: Optional[
            "capo_bcm_data_exports.types.table_properties.TableProperties"
        ] = None,
    ) -> "capo_bcm_data_exports.types.get_table_response.GetTableResponse":
        """<p>Returns the metadata for the specified table and table properties. This includes the list of columns in the table schema, their data types, and column descriptions.</p>

        Args:
            table_name: <p>The name of the table.</p>
            table_properties: <p>TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. Tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified.</p>

        Raises:
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.get_table_request.GetTableRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.get_table_response.GetTableResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_table

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_table.async_get_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.get_table_request.GetTableRequest = {
            "table_name": table_name
        }
        if table_properties is not None:
            input_["table_properties"] = table_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_executions(
        self,
        export_arn: "capo_bcm_data_exports.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
        max_results: Optional[
            "capo_bcm_data_exports.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bcm_data_exports.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_bcm_data_exports.types.list_executions_response.ListExecutionsResponse":
        """<p>Lists the historical executions for the export.</p>

        Args:
            export_arn: <p>The Amazon Resource Name (ARN) for this export.</p>
            max_results: <p>The maximum number of objects that are returned for the request.</p>
            next_token: <p>The token to retrieve the next set of results.</p>

        Raises:
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Resource Name (ARN) in the request doesn't exist.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.list_executions_request.ListExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.list_executions_response.ListExecutionsResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_executions

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_executions.async_list_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.list_executions_request.ListExecutionsRequest = {
            "export_arn": export_arn
        }
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

    async def iter_list_executions(
        self,
        export_arn: "capo_bcm_data_exports.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
        max_results: Optional[
            "capo_bcm_data_exports.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bcm_data_exports.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_data_exports.types.execution_reference.ExecutionReference]":
        _token = next_token
        while True:
            _response = await self.list_executions(
                export_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tables(
        self,
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
        next_token: Optional[
            "capo_bcm_data_exports.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_data_exports.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_data_exports.types.list_tables_response.ListTablesResponse":
        """<p>Lists all available tables in data exports.</p>

        Args:
            next_token: <p>The token to retrieve the next set of results.</p>
            max_results: <p>The maximum number of objects that are returned for the request.</p>

        Raises:
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.list_tables_request.ListTablesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.list_tables_response.ListTablesResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_tables

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_tables.async_list_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.list_tables_request.ListTablesRequest = {}
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

    async def iter_list_tables(
        self,
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
        next_token: Optional[
            "capo_bcm_data_exports.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_data_exports.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_data_exports.types.table.Table]":
        _token = next_token
        while True:
            _response = await self.list_tables(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tables",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_bcm_data_exports.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
        max_results: Optional[
            "capo_bcm_data_exports.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bcm_data_exports.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_bcm_data_exports.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List tags associated with an existing data export.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            max_results: <p>The maximum number of objects that are returned for the request.</p>
            next_token: <p>The token to retrieve the next set of results.</p>

        Raises:
            capo_bcm_data_exports.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Resource Name (ARN) in the request doesn't exist.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }
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

    async def tag_resource(
        self,
        resource_arn: "capo_bcm_data_exports.types.arn.Arn",
        resource_tags: "capo_bcm_data_exports.types.resource_tag_list.ResourceTagList",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
    ) -> "capo_bcm_data_exports.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags for an existing data export definition.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            resource_tags: <p>The tags to associate with the resource. Each tag consists of a key and a value, and each key must be unique for the resource.</p>

        Raises:
            capo_bcm_data_exports.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Resource Name (ARN) in the request doesn't exist.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.tag_resource

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "resource_tags": resource_tags,
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
        resource_arn: "capo_bcm_data_exports.types.arn.Arn",
        resource_tag_keys: "capo_bcm_data_exports.types.resource_tag_key_list.ResourceTagKeyList",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
    ) -> "capo_bcm_data_exports.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes tags associated with an existing data export definition.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            resource_tag_keys: <p>The tag keys that are associated with the resource ARN.</p>

        Raises:
            capo_bcm_data_exports.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Resource Name (ARN) in the request doesn't exist.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.untag_resource

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "resource_tag_keys": resource_tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_export(
        self,
        export: "capo_bcm_data_exports.types.export.Export",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
        resource_tags: Optional[
            "capo_bcm_data_exports.types.resource_tag_list.ResourceTagList"
        ] = None,
    ) -> "capo_bcm_data_exports.types.create_export_response.CreateExportResponse":
        """<p>Creates a data export and specifies the data query, the delivery preference, and any optional resource tags.</p> <p>A <code>DataQuery</code> consists of both a <code>QueryStatement</code> and <code>TableConfigurations</code>.</p> <p>The <code>QueryStatement</code> is an SQL statement. Data Exports only supports a limited subset of the SQL syntax. For more information on the SQL syntax that is supported, see <a href="https://docs.aws.amazon.com/cur/latest/userguide/de-data-query.html">Data query</a>. To view the available tables and columns, see the <a href="https://docs.aws.amazon.com/cur/latest/userguide/de-table-dictionary.html">Data Exports table dictionary</a>.</p> <p>The <code>TableConfigurations</code> is a collection of specified <code>TableProperties</code> for the table being queried in the <code>QueryStatement</code>. TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. However, tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified. For more information on table configurations, see <a href="https://docs.aws.amazon.com/cur/latest/userguide/de-data-query.html">Data query</a>. To view the table properties available for each table, see the <a href="https://docs.aws.amazon.com/cur/latest/userguide/de-table-dictionary.html">Data Exports table dictionary</a> or use the <code>ListTables</code> API to get a response of all tables and their available properties.</p>

        Args:
            export: <p>The details of the export, including data query, name, description, and destination configuration.</p>
            resource_tags: <p>An optional list of tags to associate with the specified export. Each tag consists of a key and a value, and each key must be unique for the resource.</p>

        Raises:
            capo_bcm_data_exports.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.create_export_request.CreateExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.create_export_response.CreateExportResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.create_export

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.create_export.async_create_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.create_export_request.CreateExportRequest = {
            "export": export
        }
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_export(
        self,
        export_arn: "capo_bcm_data_exports.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
    ) -> "capo_bcm_data_exports.types.get_export_response.GetExportResponse":
        """<p>Views the definition of an existing data export.</p>

        Args:
            export_arn: <p>The Amazon Resource Name (ARN) for this export.</p>

        Raises:
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Resource Name (ARN) in the request doesn't exist.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.get_export_request.GetExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.get_export_response.GetExportResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_export

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_export.async_get_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.get_export_request.GetExportRequest = {
            "export_arn": export_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_export(
        self,
        export_arn: "capo_bcm_data_exports.types.arn.Arn",
        export: "capo_bcm_data_exports.types.export.Export",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
    ) -> "capo_bcm_data_exports.types.update_export_response.UpdateExportResponse":
        """<p>Updates an existing data export by overwriting all export parameters. All export parameters must be provided in the UpdateExport request.</p>

        Args:
            export_arn: <p>The Amazon Resource Name (ARN) for this export.</p>
            export: <p>The name and query details for the export.</p>

        Raises:
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Resource Name (ARN) in the request doesn't exist.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.update_export_request.UpdateExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.update_export_response.UpdateExportResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.update_export

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.update_export.async_update_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.update_export_request.UpdateExportRequest = {
            "export_arn": export_arn,
            "export": export,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_export(
        self,
        export_arn: "capo_bcm_data_exports.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
    ) -> "capo_bcm_data_exports.types.delete_export_response.DeleteExportResponse":
        """<p>Deletes an existing data export.</p>

        Args:
            export_arn: <p>The Amazon Resource Name (ARN) for this export.</p>

        Raises:
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Resource Name (ARN) in the request doesn't exist.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.delete_export_request.DeleteExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.delete_export_response.DeleteExportResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.delete_export

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.delete_export.async_delete_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.delete_export_request.DeleteExportRequest = {
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
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
        max_results: Optional[
            "capo_bcm_data_exports.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bcm_data_exports.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_bcm_data_exports.types.list_exports_response.ListExportsResponse":
        """<p>Lists all data export definitions.</p>

        Args:
            max_results: <p>The maximum number of objects that are returned for the request.</p>
            next_token: <p>The token to retrieve the next set of results.</p>

        Raises:
            capo_bcm_data_exports.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_bcm_data_exports.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_data_exports.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_data_exports.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_data_exports.types.list_exports_request.ListExportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_data_exports.types.list_exports_response.ListExportsResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_exports

            (
                output,
                http_response,
            ) = await capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_exports.async_list_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.list_exports_request.ListExportsRequest = {}
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
        config_overrides: Optional[AsyncBCMDataExportsClientConfig] = None,
        max_results: Optional[
            "capo_bcm_data_exports.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bcm_data_exports.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_data_exports.types.export_reference.ExportReference]":
        _token = next_token
        while True:
            _response = await self.list_exports(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
