from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_timestream_influxdb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.create_db_parameter_group_input
    import capo_timestream_influxdb.types.create_db_parameter_group_output
    import capo_timestream_influxdb.types.db_parameter_group_identifier
    import capo_timestream_influxdb.types.db_parameter_group_name
    import capo_timestream_influxdb.types.db_parameter_group_summary
    import capo_timestream_influxdb.types.get_db_parameter_group_input
    import capo_timestream_influxdb.types.get_db_parameter_group_output
    import capo_timestream_influxdb.types.list_db_parameter_groups_input
    import capo_timestream_influxdb.types.list_db_parameter_groups_output
    import capo_timestream_influxdb.types.max_results
    import capo_timestream_influxdb.types.next_token
    import capo_timestream_influxdb.types.parameters
    import capo_timestream_influxdb.types.request_tag_map
    from capo_timestream_influxdb._services.async_timestream_influx_db import (
        AsyncTimestreamInfluxDBClient,
        AsyncTimestreamInfluxDBClientConfig,
    )
    from capo_timestream_influxdb._services.timestream_influx_db import (
        TimestreamInfluxDBClient,
        TimestreamInfluxDBClientConfig,
    )


class DbParameterGroupResource:
    def __init__(self, service: TimestreamInfluxDBClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        description: Optional[str] = None,
        parameters: Optional[
            "capo_timestream_influxdb.types.parameters.Parameters"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
    ) -> "capo_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput":
        """<p>Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.</p>

        Args:
            name: <p>The name of the DB parameter group. The name must be unique per customer and per region.</p>
            description: <p>A description of the DB parameter group.</p>
            parameters: <p>A list of the parameters that comprise the DB parameter group.</p>
            tags: <p>A list of key-value pairs to associate with the DB parameter group.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group.create_db_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDbParameterGroup")
        )
        input_: capo_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if parameters is not None:
            input_["parameters"] = parameters
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        identifier: "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput":
        """<p>Returns a Timestream for InfluxDB DB parameter group.</p>

        Args:
            identifier: <p>The id of the DB parameter group.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group.get_db_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDbParameterGroup")
        )
        input_: capo_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput = {
            "identifier": identifier
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
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput":
        """<p>Returns a list of Timestream for InfluxDB DB parameter groups.</p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups.list_db_parameter_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbParameterGroups")
        )
        input_: capo_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput = {}
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


class AsyncDbParameterGroupResource:
    def __init__(self, service: AsyncTimestreamInfluxDBClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        description: Optional[str] = None,
        parameters: Optional[
            "capo_timestream_influxdb.types.parameters.Parameters"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
    ) -> "capo_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput":
        """<p>Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.</p>

        Args:
            name: <p>The name of the DB parameter group. The name must be unique per customer and per region.</p>
            description: <p>A description of the DB parameter group.</p>
            parameters: <p>A list of the parameters that comprise the DB parameter group.</p>
            tags: <p>A list of key-value pairs to associate with the DB parameter group.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group.async_create_db_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDbParameterGroup")
        )
        input_: capo_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if parameters is not None:
            input_["parameters"] = parameters
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        identifier: "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput":
        """<p>Returns a Timestream for InfluxDB DB parameter group.</p>

        Args:
            identifier: <p>The id of the DB parameter group.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group.async_get_db_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDbParameterGroup")
        )
        input_: capo_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput = {
            "identifier": identifier
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
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput":
        """<p>Returns a list of Timestream for InfluxDB DB parameter groups.</p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups.async_list_db_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbParameterGroups")
        )
        input_: capo_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput = {}
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
