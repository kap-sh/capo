from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_iotfleetwise._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.create_state_template_request
    import capo_iotfleetwise.types.create_state_template_response
    import capo_iotfleetwise.types.delete_state_template_request
    import capo_iotfleetwise.types.delete_state_template_response
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.get_state_template_request
    import capo_iotfleetwise.types.get_state_template_response
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.list_state_templates_request
    import capo_iotfleetwise.types.list_state_templates_response
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.resource_identifier
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_properties
    import capo_iotfleetwise.types.state_template_summary
    import capo_iotfleetwise.types.tag_list
    import capo_iotfleetwise.types.update_state_template_request
    import capo_iotfleetwise.types.update_state_template_response
    from capo_iotfleetwise._services.async_io_t_fleet_wise import (
        AsyncIoTFleetWiseClient,
        AsyncIoTFleetWiseClientConfig,
    )
    from capo_iotfleetwise._services.io_t_fleet_wise import (
        IoTFleetWiseClient,
        IoTFleetWiseClientConfig,
    )


class StateTemplateResource:
    def __init__(self, service: IoTFleetWiseClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        state_template_properties: "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        data_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
        ] = None,
        metadata_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
        ] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_state_template_response.CreateStateTemplateResponse":
        """<p>Creates a state template. State templates contain state properties, which are signals that belong to a signal catalog that is synchronized between the Amazon Web Services IoT FleetWise Edge and the Amazon Web Services Cloud.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            name: <p>The name of the state template.</p>
            description: <p>A brief description of the state template.</p>
            signal_catalog_arn: <p>The ARN of the signal catalog associated with the state template.</p>
            state_template_properties: <p>A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.</p>
            data_extra_dimensions: <p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p>
            metadata_extra_dimensions: <p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p> <p>Default: An empty array</p>
            tags: <p>Metadata that can be used to manage the state template.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.create_state_template_request.CreateStateTemplateRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.create_state_template_response.CreateStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_state_template

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_state_template.create_state_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_state_template_request.CreateStateTemplateRequest = {
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
            "state_template_properties": state_template_properties,
        }
        if description is not None:
            input_["description"] = description
        if data_extra_dimensions is not None:
            input_["data_extra_dimensions"] = data_extra_dimensions
        if metadata_extra_dimensions is not None:
            input_["metadata_extra_dimensions"] = metadata_extra_dimensions
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
        identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_state_template_response.GetStateTemplateResponse":
        """<p>Retrieves information about a state template.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            identifier: <p>The unique ID of the state template.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.get_state_template_request.GetStateTemplateRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.get_state_template_response.GetStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_state_template

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_state_template.get_state_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_state_template_request.GetStateTemplateRequest = {
            "identifier": identifier
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
        identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        state_template_properties_to_add: Optional[
            "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
        ] = None,
        state_template_properties_to_remove: Optional[
            "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
        ] = None,
        data_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
        ] = None,
        metadata_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_state_template_response.UpdateStateTemplateResponse":
        """<p>Updates a state template.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            identifier: <p>The unique ID of the state template.</p>
            description: <p>A brief description of the state template.</p>
            state_template_properties_to_add: <p>Add signals from which data is collected as part of the state template.</p>
            state_template_properties_to_remove: <p>Remove signals from which data is collected as part of the state template.</p>
            data_extra_dimensions: <p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p> <p>Default: An empty array</p>
            metadata_extra_dimensions: <p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.update_state_template_request.UpdateStateTemplateRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.update_state_template_response.UpdateStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_state_template

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_state_template.update_state_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_state_template_request.UpdateStateTemplateRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if state_template_properties_to_add is not None:
            input_["state_template_properties_to_add"] = (
                state_template_properties_to_add
            )
        if state_template_properties_to_remove is not None:
            input_["state_template_properties_to_remove"] = (
                state_template_properties_to_remove
            )
        if data_extra_dimensions is not None:
            input_["data_extra_dimensions"] = data_extra_dimensions
        if metadata_extra_dimensions is not None:
            input_["metadata_extra_dimensions"] = metadata_extra_dimensions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_state_template_response.DeleteStateTemplateResponse":
        """<p>Deletes a state template.</p>

        Args:
            identifier: <p>The unique ID of the state template.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.delete_state_template_request.DeleteStateTemplateRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.delete_state_template_response.DeleteStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_state_template

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_state_template.delete_state_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_state_template_request.DeleteStateTemplateRequest = {
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
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_state_templates_response.ListStateTemplatesResponse":
        """<p>Lists information about created state templates.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            next_token: <p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: state template ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.list_state_templates_request.ListStateTemplatesRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_state_templates_response.ListStateTemplatesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_state_templates

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_state_templates.list_state_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_state_templates_request.ListStateTemplatesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncStateTemplateResource:
    def __init__(self, service: AsyncIoTFleetWiseClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        state_template_properties: "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        data_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
        ] = None,
        metadata_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
        ] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_state_template_response.CreateStateTemplateResponse":
        """<p>Creates a state template. State templates contain state properties, which are signals that belong to a signal catalog that is synchronized between the Amazon Web Services IoT FleetWise Edge and the Amazon Web Services Cloud.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            name: <p>The name of the state template.</p>
            description: <p>A brief description of the state template.</p>
            signal_catalog_arn: <p>The ARN of the signal catalog associated with the state template.</p>
            state_template_properties: <p>A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.</p>
            data_extra_dimensions: <p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p>
            metadata_extra_dimensions: <p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p> <p>Default: An empty array</p>
            tags: <p>Metadata that can be used to manage the state template.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_state_template_request.CreateStateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_state_template_response.CreateStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_state_template

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_state_template.async_create_state_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_state_template_request.CreateStateTemplateRequest = {
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
            "state_template_properties": state_template_properties,
        }
        if description is not None:
            input_["description"] = description
        if data_extra_dimensions is not None:
            input_["data_extra_dimensions"] = data_extra_dimensions
        if metadata_extra_dimensions is not None:
            input_["metadata_extra_dimensions"] = metadata_extra_dimensions
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
        identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_state_template_response.GetStateTemplateResponse":
        """<p>Retrieves information about a state template.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            identifier: <p>The unique ID of the state template.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_state_template_request.GetStateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_state_template_response.GetStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_state_template

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_state_template.async_get_state_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_state_template_request.GetStateTemplateRequest = {
            "identifier": identifier
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
        identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        state_template_properties_to_add: Optional[
            "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
        ] = None,
        state_template_properties_to_remove: Optional[
            "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
        ] = None,
        data_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
        ] = None,
        metadata_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_state_template_response.UpdateStateTemplateResponse":
        """<p>Updates a state template.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            identifier: <p>The unique ID of the state template.</p>
            description: <p>A brief description of the state template.</p>
            state_template_properties_to_add: <p>Add signals from which data is collected as part of the state template.</p>
            state_template_properties_to_remove: <p>Remove signals from which data is collected as part of the state template.</p>
            data_extra_dimensions: <p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p> <p>Default: An empty array</p>
            metadata_extra_dimensions: <p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_state_template_request.UpdateStateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_state_template_response.UpdateStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_state_template

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_state_template.async_update_state_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_state_template_request.UpdateStateTemplateRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if state_template_properties_to_add is not None:
            input_["state_template_properties_to_add"] = (
                state_template_properties_to_add
            )
        if state_template_properties_to_remove is not None:
            input_["state_template_properties_to_remove"] = (
                state_template_properties_to_remove
            )
        if data_extra_dimensions is not None:
            input_["data_extra_dimensions"] = data_extra_dimensions
        if metadata_extra_dimensions is not None:
            input_["metadata_extra_dimensions"] = metadata_extra_dimensions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_state_template_response.DeleteStateTemplateResponse":
        """<p>Deletes a state template.</p>

        Args:
            identifier: <p>The unique ID of the state template.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_state_template_request.DeleteStateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_state_template_response.DeleteStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_state_template

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_state_template.async_delete_state_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_state_template_request.DeleteStateTemplateRequest = {
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
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_state_templates_response.ListStateTemplatesResponse":
        """<p>Lists information about created state templates.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            next_token: <p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: state template ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_state_templates_request.ListStateTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_state_templates_response.ListStateTemplatesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_state_templates

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_state_templates.async_list_state_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_state_templates_request.ListStateTemplatesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
