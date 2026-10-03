from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_bcm_data_exports._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn
    import capo_bcm_data_exports.types.create_export_request
    import capo_bcm_data_exports.types.create_export_response
    import capo_bcm_data_exports.types.delete_export_request
    import capo_bcm_data_exports.types.delete_export_response
    import capo_bcm_data_exports.types.export
    import capo_bcm_data_exports.types.export_reference
    import capo_bcm_data_exports.types.get_export_request
    import capo_bcm_data_exports.types.get_export_response
    import capo_bcm_data_exports.types.list_exports_request
    import capo_bcm_data_exports.types.list_exports_response
    import capo_bcm_data_exports.types.max_results
    import capo_bcm_data_exports.types.next_page_token
    import capo_bcm_data_exports.types.resource_tag_list
    import capo_bcm_data_exports.types.update_export_request
    import capo_bcm_data_exports.types.update_export_response
    from capo_bcm_data_exports._services.async_bcm_data_exports import (
        AsyncBCMDataExportsClient,
        AsyncBCMDataExportsClientConfig,
    )
    from capo_bcm_data_exports._services.bcm_data_exports import (
        BCMDataExportsClient,
        BCMDataExportsClientConfig,
    )


class DataExport:
    def __init__(self, service: BCMDataExportsClient) -> None:
        self._service = service

    def create(
        self,
        export: "capo_bcm_data_exports.types.export.Export",
        *,
        config_overrides: Optional[BCMDataExportsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_bcm_data_exports.types.create_export_request.CreateExportRequest]",
        ) -> OperationResponse[
            "capo_bcm_data_exports.types.create_export_response.CreateExportResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.create_export

            output, http_response = (
                capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.create_export.create_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.create_export_request.CreateExportRequest = {
            "export": export
        }
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        export_arn: "capo_bcm_data_exports.types.arn.Arn",
        *,
        config_overrides: Optional[BCMDataExportsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_bcm_data_exports.types.get_export_request.GetExportRequest]",
        ) -> OperationResponse[
            "capo_bcm_data_exports.types.get_export_response.GetExportResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_export

            output, http_response = (
                capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_export.get_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.get_export_request.GetExportRequest = {
            "export_arn": export_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        export_arn: "capo_bcm_data_exports.types.arn.Arn",
        export: "capo_bcm_data_exports.types.export.Export",
        *,
        config_overrides: Optional[BCMDataExportsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_bcm_data_exports.types.update_export_request.UpdateExportRequest]",
        ) -> OperationResponse[
            "capo_bcm_data_exports.types.update_export_response.UpdateExportResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.update_export

            output, http_response = (
                capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.update_export.update_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.update_export_request.UpdateExportRequest = {
            "export_arn": export_arn,
            "export": export,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        export_arn: "capo_bcm_data_exports.types.arn.Arn",
        *,
        config_overrides: Optional[BCMDataExportsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_bcm_data_exports.types.delete_export_request.DeleteExportRequest]",
        ) -> OperationResponse[
            "capo_bcm_data_exports.types.delete_export_response.DeleteExportResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.delete_export

            output, http_response = (
                capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.delete_export.delete_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.delete_export_request.DeleteExportRequest = {
            "export_arn": export_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BCMDataExportsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_bcm_data_exports.types.list_exports_request.ListExportsRequest]",
        ) -> OperationResponse[
            "capo_bcm_data_exports.types.list_exports_response.ListExportsResponse"
        ]:
            import capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_exports

            output, http_response = (
                capo_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_exports.list_exports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bcm_data_exports.types.list_exports_request.ListExportsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDataExport:
    def __init__(self, service: AsyncBCMDataExportsClient) -> None:
        self._service = service

    async def create(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def update(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
