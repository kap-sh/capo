from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.create_data_source_input
    import capo_datazone.types.create_data_source_output
    import capo_datazone.types.data_source_configuration_input
    import capo_datazone.types.data_source_id
    import capo_datazone.types.data_source_status
    import capo_datazone.types.data_source_summary
    import capo_datazone.types.data_source_type
    import capo_datazone.types.delete_data_source_input
    import capo_datazone.types.delete_data_source_output
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.enable_setting
    import capo_datazone.types.form_input_list
    import capo_datazone.types.get_data_source_input
    import capo_datazone.types.get_data_source_output
    import capo_datazone.types.list_data_sources_input
    import capo_datazone.types.list_data_sources_output
    import capo_datazone.types.max_results
    import capo_datazone.types.name
    import capo_datazone.types.pagination_token
    import capo_datazone.types.recommendation_configuration
    import capo_datazone.types.schedule_configuration
    import capo_datazone.types.update_data_source_input
    import capo_datazone.types.update_data_source_output
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class DataSource:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_datazone.types.name.Name",
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: str,
        type: "capo_datazone.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        environment_identifier: Optional[str] = None,
        connection_identifier: Optional[str] = None,
        configuration: Optional[
            "capo_datazone.types.data_source_configuration_input.DataSourceConfigurationInput"
        ] = None,
        recommendation: Optional[
            "capo_datazone.types.recommendation_configuration.RecommendationConfiguration"
        ] = None,
        enable_setting: Optional[
            "capo_datazone.types.enable_setting.EnableSetting"
        ] = None,
        schedule: Optional[
            "capo_datazone.types.schedule_configuration.ScheduleConfiguration"
        ] = None,
        publish_on_import: Optional[bool] = None,
        asset_forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_data_source_output.CreateDataSourceOutput":
        """<p>Creates an Amazon DataZone data source.</p>

        Args:
            name: <p>The name of the data source.</p>
            description: <p>The description of the data source.</p>
            domain_identifier: <p>The ID of the Amazon DataZone domain where the data source is created.</p>
            project_identifier: <p>The identifier of the Amazon DataZone project in which you want to add this data source.</p>
            environment_identifier: <p>The unique identifier of the Amazon DataZone environment to which the data source publishes assets. </p>
            connection_identifier: <p>The ID of the connection.</p>
            type: <p>The type of the data source. In Amazon DataZone, you can use data sources to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone. In the current release of Amazon DataZone, you can create and run data sources for Amazon Web Services Glue and Amazon Redshift.</p>
            configuration: <p>Specifies the configuration of the data source. It can be set to either <code>glueRunConfiguration</code> or <code>redshiftRunConfiguration</code>.</p>
            recommendation: <p>Specifies whether the business name generation is to be enabled for this data source.</p>
            enable_setting: <p>Specifies whether the data source is enabled.</p>
            schedule: <p>The schedule of the data source runs.</p>
            publish_on_import: <p>Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.</p>
            asset_forms_input: <p>The metadata forms that are to be attached to the assets that this data source works with.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.create_data_source_input.CreateDataSourceInput]",
        ) -> OperationResponse[
            "capo_datazone.types.create_data_source_output.CreateDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.create_data_source

            output, http_response = (
                capo_datazone._operations.data_zone.create_data_source.create_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.create_data_source_input.CreateDataSourceInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_data_source_input

            return capo_datazone.types.create_data_source_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.create_data_source_output.CreateDataSourceOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_data_source_output

            return capo_datazone.types.create_data_source_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateDataSource",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.create_data_source_input.CreateDataSourceInput = {
            "name": name,
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if connection_identifier is not None:
            input_["connection_identifier"] = connection_identifier
        if configuration is not None:
            input_["configuration"] = configuration
        if recommendation is not None:
            input_["recommendation"] = recommendation
        if enable_setting is not None:
            input_["enable_setting"] = enable_setting
        if schedule is not None:
            input_["schedule"] = schedule
        if publish_on_import is not None:
            input_["publish_on_import"] = publish_on_import
        if asset_forms_input is not None:
            input_["asset_forms_input"] = asset_forms_input
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

    def read(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_data_source_output.GetDataSourceOutput":
        """<p>Gets an Amazon DataZone data source.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the data source exists.</p>
            identifier: <p>The ID of the Amazon DataZone data source.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.get_data_source_input.GetDataSourceInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_data_source_output.GetDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.get_data_source

            output, http_response = (
                capo_datazone._operations.data_zone.get_data_source.get_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_data_source_output.GetDataSourceOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_data_source_output

            return capo_datazone.types.get_data_source_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDataSource", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_data_source_input.GetDataSourceInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.name.Name"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        enable_setting: Optional[
            "capo_datazone.types.enable_setting.EnableSetting"
        ] = None,
        publish_on_import: Optional[bool] = None,
        asset_forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        schedule: Optional[
            "capo_datazone.types.schedule_configuration.ScheduleConfiguration"
        ] = None,
        configuration: Optional[
            "capo_datazone.types.data_source_configuration_input.DataSourceConfigurationInput"
        ] = None,
        recommendation: Optional[
            "capo_datazone.types.recommendation_configuration.RecommendationConfiguration"
        ] = None,
        retain_permissions_on_revoke_failure: Optional[bool] = None,
    ) -> "capo_datazone.types.update_data_source_output.UpdateDataSourceOutput":
        """<p>Updates the specified data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which to update a data source.</p>
            identifier: <p>The identifier of the data source to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateDataSource</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateDataSource</code> action.</p>
            enable_setting: <p>The enable setting to be updated as part of the <code>UpdateDataSource</code> action.</p>
            publish_on_import: <p>The publish on import setting to be updated as part of the <code>UpdateDataSource</code> action.</p>
            asset_forms_input: <p>The asset forms to be updated as part of the <code>UpdateDataSource</code> action.</p>
            schedule: <p>The schedule to be updated as part of the <code>UpdateDataSource</code> action.</p>
            configuration: <p>The configuration to be updated as part of the <code>UpdateDataSource</code> action.</p>
            recommendation: <p>The recommendation to be updated as part of the <code>UpdateDataSource</code> action.</p>
            retain_permissions_on_revoke_failure: <p>Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.update_data_source_input.UpdateDataSourceInput]",
        ) -> OperationResponse[
            "capo_datazone.types.update_data_source_output.UpdateDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.update_data_source

            output, http_response = (
                capo_datazone._operations.data_zone.update_data_source.update_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.update_data_source_input.UpdateDataSourceInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_data_source_input

            return capo_datazone.types.update_data_source_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.update_data_source_output.UpdateDataSourceOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_data_source_output

            return capo_datazone.types.update_data_source_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateDataSource",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.update_data_source_input.UpdateDataSourceInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if enable_setting is not None:
            input_["enable_setting"] = enable_setting
        if publish_on_import is not None:
            input_["publish_on_import"] = publish_on_import
        if asset_forms_input is not None:
            input_["asset_forms_input"] = asset_forms_input
        if schedule is not None:
            input_["schedule"] = schedule
        if configuration is not None:
            input_["configuration"] = configuration
        if recommendation is not None:
            input_["recommendation"] = recommendation
        if retain_permissions_on_revoke_failure is not None:
            input_["retain_permissions_on_revoke_failure"] = (
                retain_permissions_on_revoke_failure
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        retain_permissions_on_revoke_failure: Optional[bool] = None,
    ) -> "capo_datazone.types.delete_data_source_output.DeleteDataSourceOutput":
        """<p>Deletes a data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the data source is deleted.</p>
            identifier: <p>The identifier of the data source that is deleted.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            retain_permissions_on_revoke_failure: <p>Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.delete_data_source_input.DeleteDataSourceInput]",
        ) -> OperationResponse[
            "capo_datazone.types.delete_data_source_output.DeleteDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_data_source

            output, http_response = (
                capo_datazone._operations.data_zone.delete_data_source.delete_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.delete_data_source_output.DeleteDataSourceOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.delete_data_source_output

            return capo_datazone.types.delete_data_source_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteDataSource", redact_output=_redact_output),
        )
        input_: capo_datazone.types.delete_data_source_input.DeleteDataSourceInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if retain_permissions_on_revoke_failure is not None:
            input_["retain_permissions_on_revoke_failure"] = (
                retain_permissions_on_revoke_failure
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: str,
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        environment_identifier: Optional[str] = None,
        connection_identifier: Optional[str] = None,
        type: Optional["capo_datazone.types.data_source_type.DataSourceType"] = None,
        status: Optional[
            "capo_datazone.types.data_source_status.DataSourceStatus"
        ] = None,
        name: Optional["capo_datazone.types.name.Name"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_data_sources_output.ListDataSourcesOutput":
        """<p>Lists data sources in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to list the data sources.</p>
            project_identifier: <p>The identifier of the project in which to list data sources.</p>
            environment_identifier: <p>The identifier of the environment in which to list the data sources.</p>
            connection_identifier: <p>The ID of the connection.</p>
            type: <p>The type of the data source.</p>
            status: <p>The status of the data source.</p>
            name: <p>The name of the data source.</p>
            next_token: <p>When the number of data sources is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of data sources, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSources</code> to list the next set of data sources.</p>
            max_results: <p>The maximum number of data sources to return in a single call to <code>ListDataSources</code>. When the number of data sources to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSources</code> to list the next set of data sources.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.list_data_sources_input.ListDataSourcesInput]",
        ) -> OperationResponse[
            "capo_datazone.types.list_data_sources_output.ListDataSourcesOutput"
        ]:
            import capo_datazone._operations.data_zone.list_data_sources

            output, http_response = (
                capo_datazone._operations.data_zone.list_data_sources.list_data_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.list_data_sources_input.ListDataSourcesInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.list_data_sources_input

            return capo_datazone.types.list_data_sources_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.list_data_sources_output.ListDataSourcesOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.list_data_sources_output

            return capo_datazone.types.list_data_sources_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListDataSources",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.list_data_sources_input.ListDataSourcesInput = {
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
        }
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if connection_identifier is not None:
            input_["connection_identifier"] = connection_identifier
        if type is not None:
            input_["type"] = type
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDataSource:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_datazone.types.name.Name",
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: str,
        type: "capo_datazone.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        environment_identifier: Optional[str] = None,
        connection_identifier: Optional[str] = None,
        configuration: Optional[
            "capo_datazone.types.data_source_configuration_input.DataSourceConfigurationInput"
        ] = None,
        recommendation: Optional[
            "capo_datazone.types.recommendation_configuration.RecommendationConfiguration"
        ] = None,
        enable_setting: Optional[
            "capo_datazone.types.enable_setting.EnableSetting"
        ] = None,
        schedule: Optional[
            "capo_datazone.types.schedule_configuration.ScheduleConfiguration"
        ] = None,
        publish_on_import: Optional[bool] = None,
        asset_forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_data_source_output.CreateDataSourceOutput":
        """<p>Creates an Amazon DataZone data source.</p>

        Args:
            name: <p>The name of the data source.</p>
            description: <p>The description of the data source.</p>
            domain_identifier: <p>The ID of the Amazon DataZone domain where the data source is created.</p>
            project_identifier: <p>The identifier of the Amazon DataZone project in which you want to add this data source.</p>
            environment_identifier: <p>The unique identifier of the Amazon DataZone environment to which the data source publishes assets. </p>
            connection_identifier: <p>The ID of the connection.</p>
            type: <p>The type of the data source. In Amazon DataZone, you can use data sources to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone. In the current release of Amazon DataZone, you can create and run data sources for Amazon Web Services Glue and Amazon Redshift.</p>
            configuration: <p>Specifies the configuration of the data source. It can be set to either <code>glueRunConfiguration</code> or <code>redshiftRunConfiguration</code>.</p>
            recommendation: <p>Specifies whether the business name generation is to be enabled for this data source.</p>
            enable_setting: <p>Specifies whether the data source is enabled.</p>
            schedule: <p>The schedule of the data source runs.</p>
            publish_on_import: <p>Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.</p>
            asset_forms_input: <p>The metadata forms that are to be attached to the assets that this data source works with.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_data_source_input.CreateDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_data_source_output.CreateDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.create_data_source

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_data_source.async_create_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.create_data_source_input.CreateDataSourceInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_data_source_input

            return capo_datazone.types.create_data_source_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.create_data_source_output.CreateDataSourceOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_data_source_output

            return capo_datazone.types.create_data_source_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateDataSource",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.create_data_source_input.CreateDataSourceInput = {
            "name": name,
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if connection_identifier is not None:
            input_["connection_identifier"] = connection_identifier
        if configuration is not None:
            input_["configuration"] = configuration
        if recommendation is not None:
            input_["recommendation"] = recommendation
        if enable_setting is not None:
            input_["enable_setting"] = enable_setting
        if schedule is not None:
            input_["schedule"] = schedule
        if publish_on_import is not None:
            input_["publish_on_import"] = publish_on_import
        if asset_forms_input is not None:
            input_["asset_forms_input"] = asset_forms_input
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_data_source_output.GetDataSourceOutput":
        """<p>Gets an Amazon DataZone data source.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the data source exists.</p>
            identifier: <p>The ID of the Amazon DataZone data source.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_data_source_input.GetDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_data_source_output.GetDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.get_data_source

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_data_source.async_get_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_data_source_output.GetDataSourceOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_data_source_output

            return capo_datazone.types.get_data_source_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDataSource", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_data_source_input.GetDataSourceInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.name.Name"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        enable_setting: Optional[
            "capo_datazone.types.enable_setting.EnableSetting"
        ] = None,
        publish_on_import: Optional[bool] = None,
        asset_forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        schedule: Optional[
            "capo_datazone.types.schedule_configuration.ScheduleConfiguration"
        ] = None,
        configuration: Optional[
            "capo_datazone.types.data_source_configuration_input.DataSourceConfigurationInput"
        ] = None,
        recommendation: Optional[
            "capo_datazone.types.recommendation_configuration.RecommendationConfiguration"
        ] = None,
        retain_permissions_on_revoke_failure: Optional[bool] = None,
    ) -> "capo_datazone.types.update_data_source_output.UpdateDataSourceOutput":
        """<p>Updates the specified data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which to update a data source.</p>
            identifier: <p>The identifier of the data source to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateDataSource</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateDataSource</code> action.</p>
            enable_setting: <p>The enable setting to be updated as part of the <code>UpdateDataSource</code> action.</p>
            publish_on_import: <p>The publish on import setting to be updated as part of the <code>UpdateDataSource</code> action.</p>
            asset_forms_input: <p>The asset forms to be updated as part of the <code>UpdateDataSource</code> action.</p>
            schedule: <p>The schedule to be updated as part of the <code>UpdateDataSource</code> action.</p>
            configuration: <p>The configuration to be updated as part of the <code>UpdateDataSource</code> action.</p>
            recommendation: <p>The recommendation to be updated as part of the <code>UpdateDataSource</code> action.</p>
            retain_permissions_on_revoke_failure: <p>Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_data_source_input.UpdateDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_data_source_output.UpdateDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.update_data_source

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_data_source.async_update_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.update_data_source_input.UpdateDataSourceInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_data_source_input

            return capo_datazone.types.update_data_source_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.update_data_source_output.UpdateDataSourceOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_data_source_output

            return capo_datazone.types.update_data_source_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateDataSource",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.update_data_source_input.UpdateDataSourceInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if enable_setting is not None:
            input_["enable_setting"] = enable_setting
        if publish_on_import is not None:
            input_["publish_on_import"] = publish_on_import
        if asset_forms_input is not None:
            input_["asset_forms_input"] = asset_forms_input
        if schedule is not None:
            input_["schedule"] = schedule
        if configuration is not None:
            input_["configuration"] = configuration
        if recommendation is not None:
            input_["recommendation"] = recommendation
        if retain_permissions_on_revoke_failure is not None:
            input_["retain_permissions_on_revoke_failure"] = (
                retain_permissions_on_revoke_failure
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        retain_permissions_on_revoke_failure: Optional[bool] = None,
    ) -> "capo_datazone.types.delete_data_source_output.DeleteDataSourceOutput":
        """<p>Deletes a data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the data source is deleted.</p>
            identifier: <p>The identifier of the data source that is deleted.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            retain_permissions_on_revoke_failure: <p>Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_data_source_input.DeleteDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_data_source_output.DeleteDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_data_source

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_data_source.async_delete_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.delete_data_source_output.DeleteDataSourceOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.delete_data_source_output

            return capo_datazone.types.delete_data_source_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteDataSource", redact_output=_redact_output),
        )
        input_: capo_datazone.types.delete_data_source_input.DeleteDataSourceInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if retain_permissions_on_revoke_failure is not None:
            input_["retain_permissions_on_revoke_failure"] = (
                retain_permissions_on_revoke_failure
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        environment_identifier: Optional[str] = None,
        connection_identifier: Optional[str] = None,
        type: Optional["capo_datazone.types.data_source_type.DataSourceType"] = None,
        status: Optional[
            "capo_datazone.types.data_source_status.DataSourceStatus"
        ] = None,
        name: Optional["capo_datazone.types.name.Name"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_data_sources_output.ListDataSourcesOutput":
        """<p>Lists data sources in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to list the data sources.</p>
            project_identifier: <p>The identifier of the project in which to list data sources.</p>
            environment_identifier: <p>The identifier of the environment in which to list the data sources.</p>
            connection_identifier: <p>The ID of the connection.</p>
            type: <p>The type of the data source.</p>
            status: <p>The status of the data source.</p>
            name: <p>The name of the data source.</p>
            next_token: <p>When the number of data sources is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of data sources, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSources</code> to list the next set of data sources.</p>
            max_results: <p>The maximum number of data sources to return in a single call to <code>ListDataSources</code>. When the number of data sources to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSources</code> to list the next set of data sources.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_data_sources_input.ListDataSourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_data_sources_output.ListDataSourcesOutput"
        ]:
            import capo_datazone._operations.data_zone.list_data_sources

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_data_sources.async_list_data_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.list_data_sources_input.ListDataSourcesInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.list_data_sources_input

            return capo_datazone.types.list_data_sources_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.list_data_sources_output.ListDataSourcesOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.list_data_sources_output

            return capo_datazone.types.list_data_sources_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListDataSources",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.list_data_sources_input.ListDataSourcesInput = {
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
        }
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if connection_identifier is not None:
            input_["connection_identifier"] = connection_identifier
        if type is not None:
            input_["type"] = type
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
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
