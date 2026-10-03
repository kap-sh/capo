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
    import capo_iotfleetwise.types.create_decoder_manifest_request
    import capo_iotfleetwise.types.create_decoder_manifest_response
    import capo_iotfleetwise.types.decoder_manifest_summary
    import capo_iotfleetwise.types.default_for_unmapped_signals_type
    import capo_iotfleetwise.types.delete_decoder_manifest_request
    import capo_iotfleetwise.types.delete_decoder_manifest_response
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.fqns
    import capo_iotfleetwise.types.get_decoder_manifest_request
    import capo_iotfleetwise.types.get_decoder_manifest_response
    import capo_iotfleetwise.types.import_decoder_manifest_request
    import capo_iotfleetwise.types.import_decoder_manifest_response
    import capo_iotfleetwise.types.interface_ids
    import capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_request
    import capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_response
    import capo_iotfleetwise.types.list_decoder_manifest_signals_request
    import capo_iotfleetwise.types.list_decoder_manifest_signals_response
    import capo_iotfleetwise.types.list_decoder_manifests_request
    import capo_iotfleetwise.types.list_decoder_manifests_response
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.manifest_status
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.network_file_definitions
    import capo_iotfleetwise.types.network_interface
    import capo_iotfleetwise.types.network_interfaces
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.signal_decoder
    import capo_iotfleetwise.types.signal_decoders
    import capo_iotfleetwise.types.tag_list
    import capo_iotfleetwise.types.update_decoder_manifest_request
    import capo_iotfleetwise.types.update_decoder_manifest_response
    from capo_iotfleetwise._services.async_io_t_fleet_wise import (
        AsyncIoTFleetWiseClient,
        AsyncIoTFleetWiseClientConfig,
    )
    from capo_iotfleetwise._services.io_t_fleet_wise import (
        IoTFleetWiseClient,
        IoTFleetWiseClientConfig,
    )


class DecoderManifestResource:
    def __init__(self, service: IoTFleetWiseClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        model_manifest_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        signal_decoders: Optional[
            "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
        ] = None,
        network_interfaces: Optional[
            "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
        ] = None,
        default_for_unmapped_signals: Optional[
            "capo_iotfleetwise.types.default_for_unmapped_signals_type.DefaultForUnmappedSignalsType"
        ] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_decoder_manifest_response.CreateDecoderManifestResponse":
        """<p>Creates the decoder manifest associated with a model manifest. To create a decoder manifest, the following must be true:</p> <ul> <li> <p>Every signal decoder has a unique name.</p> </li> <li> <p>Each signal decoder is associated with a network interface.</p> </li> <li> <p>Each network interface has a unique ID.</p> </li> <li> <p>The signal decoders are specified in the model manifest.</p> </li> </ul>

        Args:
            name: <p> The unique name of the decoder manifest to create.</p>
            description: <p>A brief description of the decoder manifest. </p>
            model_manifest_arn: <p> The Amazon Resource Name (ARN) of the vehicle model (model manifest). </p>
            signal_decoders: <p> A list of information about signal decoders. </p>
            network_interfaces: <p> A list of information about available network interfaces. </p>
            default_for_unmapped_signals: <p>Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>
            tags: <p>Metadata that can be used to manage the decoder manifest.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.decoder_manifest_validation_exception.DecoderManifestValidationException: <p>The request couldn't be completed because it contains signal decoders with one or more validation errors.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.create_decoder_manifest_request.CreateDecoderManifestRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.create_decoder_manifest_response.CreateDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_decoder_manifest

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_decoder_manifest.create_decoder_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_decoder_manifest_request.CreateDecoderManifestRequest = {
            "name": name,
            "model_manifest_arn": model_manifest_arn,
        }
        if description is not None:
            input_["description"] = description
        if signal_decoders is not None:
            input_["signal_decoders"] = signal_decoders
        if network_interfaces is not None:
            input_["network_interfaces"] = network_interfaces
        if default_for_unmapped_signals is not None:
            input_["default_for_unmapped_signals"] = default_for_unmapped_signals
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
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_decoder_manifest_response.GetDecoderManifestResponse":
        """<p> Retrieves information about a created decoder manifest. </p>

        Args:
            name: <p> The name of the decoder manifest to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.get_decoder_manifest_request.GetDecoderManifestRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.get_decoder_manifest_response.GetDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_decoder_manifest

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_decoder_manifest.get_decoder_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_decoder_manifest_request.GetDecoderManifestRequest = {
            "name": name
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
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        signal_decoders_to_add: Optional[
            "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
        ] = None,
        signal_decoders_to_update: Optional[
            "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
        ] = None,
        signal_decoders_to_remove: Optional["capo_iotfleetwise.types.fqns.Fqns"] = None,
        network_interfaces_to_add: Optional[
            "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
        ] = None,
        network_interfaces_to_update: Optional[
            "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
        ] = None,
        network_interfaces_to_remove: Optional[
            "capo_iotfleetwise.types.interface_ids.InterfaceIds"
        ] = None,
        status: Optional[
            "capo_iotfleetwise.types.manifest_status.ManifestStatus"
        ] = None,
        default_for_unmapped_signals: Optional[
            "capo_iotfleetwise.types.default_for_unmapped_signals_type.DefaultForUnmappedSignalsType"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_decoder_manifest_response.UpdateDecoderManifestResponse":
        """<p> Updates a decoder manifest.</p> <p>A decoder manifest can only be updated when the status is <code>DRAFT</code>. Only <code>ACTIVE</code> decoder manifests can be associated with vehicles.</p>

        Args:
            name: <p> The name of the decoder manifest to update.</p>
            description: <p> A brief description of the decoder manifest to update. </p>
            signal_decoders_to_add: <p> A list of information about decoding additional signals to add to the decoder manifest. </p>
            signal_decoders_to_update: <p> A list of updated information about decoding signals to update in the decoder manifest. </p>
            signal_decoders_to_remove: <p> A list of signal decoders to remove from the decoder manifest. </p>
            network_interfaces_to_add: <p> A list of information about the network interfaces to add to the decoder manifest. </p>
            network_interfaces_to_update: <p> A list of information about the network interfaces to update in the decoder manifest. </p>
            network_interfaces_to_remove: <p> A list of network interfaces to remove from the decoder manifest.</p>
            status: <p> The state of the decoder manifest. If the status is <code>ACTIVE</code>, the decoder manifest can't be edited. If the status is <code>DRAFT</code>, you can edit the decoder manifest. </p>
            default_for_unmapped_signals: <p>Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.decoder_manifest_validation_exception.DecoderManifestValidationException: <p>The request couldn't be completed because it contains signal decoders with one or more validation errors.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.update_decoder_manifest_request.UpdateDecoderManifestRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.update_decoder_manifest_response.UpdateDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_decoder_manifest

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_decoder_manifest.update_decoder_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_decoder_manifest_request.UpdateDecoderManifestRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if signal_decoders_to_add is not None:
            input_["signal_decoders_to_add"] = signal_decoders_to_add
        if signal_decoders_to_update is not None:
            input_["signal_decoders_to_update"] = signal_decoders_to_update
        if signal_decoders_to_remove is not None:
            input_["signal_decoders_to_remove"] = signal_decoders_to_remove
        if network_interfaces_to_add is not None:
            input_["network_interfaces_to_add"] = network_interfaces_to_add
        if network_interfaces_to_update is not None:
            input_["network_interfaces_to_update"] = network_interfaces_to_update
        if network_interfaces_to_remove is not None:
            input_["network_interfaces_to_remove"] = network_interfaces_to_remove
        if status is not None:
            input_["status"] = status
        if default_for_unmapped_signals is not None:
            input_["default_for_unmapped_signals"] = default_for_unmapped_signals

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_decoder_manifest_response.DeleteDecoderManifestResponse":
        """<p> Deletes a decoder manifest. You can't delete a decoder manifest if it has vehicles associated with it. </p>

        Args:
            name: <p> The name of the decoder manifest to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.delete_decoder_manifest_request.DeleteDecoderManifestRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.delete_decoder_manifest_response.DeleteDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_decoder_manifest

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_decoder_manifest.delete_decoder_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_decoder_manifest_request.DeleteDecoderManifestRequest = {
            "name": name
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
        model_manifest_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_decoder_manifests_response.ListDecoderManifestsResponse":
        """<p> Lists decoder manifests. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            model_manifest_arn: <p> The Amazon Resource Name (ARN) of a vehicle model (model manifest) associated with the decoder manifest. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: decoder manifest name, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.list_decoder_manifests_request.ListDecoderManifestsRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_decoder_manifests_response.ListDecoderManifestsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifests

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifests.list_decoder_manifests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_decoder_manifests_request.ListDecoderManifestsRequest = {}
        if model_manifest_arn is not None:
            input_["model_manifest_arn"] = model_manifest_arn
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

    def import_decoder_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        network_file_definitions: "capo_iotfleetwise.types.network_file_definitions.NetworkFileDefinitions",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.import_decoder_manifest_response.ImportDecoderManifestResponse":
        """<p> Creates a decoder manifest using your existing CAN DBC file from your local device. </p> <p>The CAN signal name must be unique and not repeated across CAN message definitions in a .dbc file. </p>

        Args:
            name: <p> The name of the decoder manifest to import. </p>
            network_file_definitions: <p> The file to load into an Amazon Web Services account. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.decoder_manifest_validation_exception.DecoderManifestValidationException: <p>The request couldn't be completed because it contains signal decoders with one or more validation errors.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.import_decoder_manifest_request.ImportDecoderManifestRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.import_decoder_manifest_response.ImportDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_decoder_manifest

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_decoder_manifest.import_decoder_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.import_decoder_manifest_request.ImportDecoderManifestRequest = {
            "name": name,
            "network_file_definitions": network_file_definitions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_decoder_manifest_network_interfaces(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_response.ListDecoderManifestNetworkInterfacesResponse":
        """<p> Lists the network interfaces specified in a decoder manifest. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the decoder manifest to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_request.ListDecoderManifestNetworkInterfacesRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_response.ListDecoderManifestNetworkInterfacesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_network_interfaces

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_network_interfaces.list_decoder_manifest_network_interfaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_request.ListDecoderManifestNetworkInterfacesRequest = {
            "name": name
        }
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

    def list_decoder_manifest_signals(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_decoder_manifest_signals_response.ListDecoderManifestSignalsResponse":
        """<p> A list of information about signal decoders specified in a decoder manifest. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the decoder manifest to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.list_decoder_manifest_signals_request.ListDecoderManifestSignalsRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_decoder_manifest_signals_response.ListDecoderManifestSignalsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_signals

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_signals.list_decoder_manifest_signals(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_decoder_manifest_signals_request.ListDecoderManifestSignalsRequest = {
            "name": name
        }
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


class AsyncDecoderManifestResource:
    def __init__(self, service: AsyncIoTFleetWiseClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        model_manifest_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        signal_decoders: Optional[
            "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
        ] = None,
        network_interfaces: Optional[
            "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
        ] = None,
        default_for_unmapped_signals: Optional[
            "capo_iotfleetwise.types.default_for_unmapped_signals_type.DefaultForUnmappedSignalsType"
        ] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_decoder_manifest_response.CreateDecoderManifestResponse":
        """<p>Creates the decoder manifest associated with a model manifest. To create a decoder manifest, the following must be true:</p> <ul> <li> <p>Every signal decoder has a unique name.</p> </li> <li> <p>Each signal decoder is associated with a network interface.</p> </li> <li> <p>Each network interface has a unique ID.</p> </li> <li> <p>The signal decoders are specified in the model manifest.</p> </li> </ul>

        Args:
            name: <p> The unique name of the decoder manifest to create.</p>
            description: <p>A brief description of the decoder manifest. </p>
            model_manifest_arn: <p> The Amazon Resource Name (ARN) of the vehicle model (model manifest). </p>
            signal_decoders: <p> A list of information about signal decoders. </p>
            network_interfaces: <p> A list of information about available network interfaces. </p>
            default_for_unmapped_signals: <p>Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>
            tags: <p>Metadata that can be used to manage the decoder manifest.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.decoder_manifest_validation_exception.DecoderManifestValidationException: <p>The request couldn't be completed because it contains signal decoders with one or more validation errors.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_decoder_manifest_request.CreateDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_decoder_manifest_response.CreateDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_decoder_manifest.async_create_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_decoder_manifest_request.CreateDecoderManifestRequest = {
            "name": name,
            "model_manifest_arn": model_manifest_arn,
        }
        if description is not None:
            input_["description"] = description
        if signal_decoders is not None:
            input_["signal_decoders"] = signal_decoders
        if network_interfaces is not None:
            input_["network_interfaces"] = network_interfaces
        if default_for_unmapped_signals is not None:
            input_["default_for_unmapped_signals"] = default_for_unmapped_signals
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
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_decoder_manifest_response.GetDecoderManifestResponse":
        """<p> Retrieves information about a created decoder manifest. </p>

        Args:
            name: <p> The name of the decoder manifest to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_decoder_manifest_request.GetDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_decoder_manifest_response.GetDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_decoder_manifest.async_get_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_decoder_manifest_request.GetDecoderManifestRequest = {
            "name": name
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
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        signal_decoders_to_add: Optional[
            "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
        ] = None,
        signal_decoders_to_update: Optional[
            "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
        ] = None,
        signal_decoders_to_remove: Optional["capo_iotfleetwise.types.fqns.Fqns"] = None,
        network_interfaces_to_add: Optional[
            "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
        ] = None,
        network_interfaces_to_update: Optional[
            "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
        ] = None,
        network_interfaces_to_remove: Optional[
            "capo_iotfleetwise.types.interface_ids.InterfaceIds"
        ] = None,
        status: Optional[
            "capo_iotfleetwise.types.manifest_status.ManifestStatus"
        ] = None,
        default_for_unmapped_signals: Optional[
            "capo_iotfleetwise.types.default_for_unmapped_signals_type.DefaultForUnmappedSignalsType"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_decoder_manifest_response.UpdateDecoderManifestResponse":
        """<p> Updates a decoder manifest.</p> <p>A decoder manifest can only be updated when the status is <code>DRAFT</code>. Only <code>ACTIVE</code> decoder manifests can be associated with vehicles.</p>

        Args:
            name: <p> The name of the decoder manifest to update.</p>
            description: <p> A brief description of the decoder manifest to update. </p>
            signal_decoders_to_add: <p> A list of information about decoding additional signals to add to the decoder manifest. </p>
            signal_decoders_to_update: <p> A list of updated information about decoding signals to update in the decoder manifest. </p>
            signal_decoders_to_remove: <p> A list of signal decoders to remove from the decoder manifest. </p>
            network_interfaces_to_add: <p> A list of information about the network interfaces to add to the decoder manifest. </p>
            network_interfaces_to_update: <p> A list of information about the network interfaces to update in the decoder manifest. </p>
            network_interfaces_to_remove: <p> A list of network interfaces to remove from the decoder manifest.</p>
            status: <p> The state of the decoder manifest. If the status is <code>ACTIVE</code>, the decoder manifest can't be edited. If the status is <code>DRAFT</code>, you can edit the decoder manifest. </p>
            default_for_unmapped_signals: <p>Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.decoder_manifest_validation_exception.DecoderManifestValidationException: <p>The request couldn't be completed because it contains signal decoders with one or more validation errors.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_decoder_manifest_request.UpdateDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_decoder_manifest_response.UpdateDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_decoder_manifest.async_update_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_decoder_manifest_request.UpdateDecoderManifestRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if signal_decoders_to_add is not None:
            input_["signal_decoders_to_add"] = signal_decoders_to_add
        if signal_decoders_to_update is not None:
            input_["signal_decoders_to_update"] = signal_decoders_to_update
        if signal_decoders_to_remove is not None:
            input_["signal_decoders_to_remove"] = signal_decoders_to_remove
        if network_interfaces_to_add is not None:
            input_["network_interfaces_to_add"] = network_interfaces_to_add
        if network_interfaces_to_update is not None:
            input_["network_interfaces_to_update"] = network_interfaces_to_update
        if network_interfaces_to_remove is not None:
            input_["network_interfaces_to_remove"] = network_interfaces_to_remove
        if status is not None:
            input_["status"] = status
        if default_for_unmapped_signals is not None:
            input_["default_for_unmapped_signals"] = default_for_unmapped_signals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_decoder_manifest_response.DeleteDecoderManifestResponse":
        """<p> Deletes a decoder manifest. You can't delete a decoder manifest if it has vehicles associated with it. </p>

        Args:
            name: <p> The name of the decoder manifest to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_decoder_manifest_request.DeleteDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_decoder_manifest_response.DeleteDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_decoder_manifest.async_delete_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_decoder_manifest_request.DeleteDecoderManifestRequest = {
            "name": name
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
        model_manifest_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_decoder_manifests_response.ListDecoderManifestsResponse":
        """<p> Lists decoder manifests. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            model_manifest_arn: <p> The Amazon Resource Name (ARN) of a vehicle model (model manifest) associated with the decoder manifest. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: decoder manifest name, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_decoder_manifests_request.ListDecoderManifestsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_decoder_manifests_response.ListDecoderManifestsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifests

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifests.async_list_decoder_manifests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_decoder_manifests_request.ListDecoderManifestsRequest = {}
        if model_manifest_arn is not None:
            input_["model_manifest_arn"] = model_manifest_arn
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

    async def import_decoder_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        network_file_definitions: "capo_iotfleetwise.types.network_file_definitions.NetworkFileDefinitions",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.import_decoder_manifest_response.ImportDecoderManifestResponse":
        """<p> Creates a decoder manifest using your existing CAN DBC file from your local device. </p> <p>The CAN signal name must be unique and not repeated across CAN message definitions in a .dbc file. </p>

        Args:
            name: <p> The name of the decoder manifest to import. </p>
            network_file_definitions: <p> The file to load into an Amazon Web Services account. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.decoder_manifest_validation_exception.DecoderManifestValidationException: <p>The request couldn't be completed because it contains signal decoders with one or more validation errors.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.import_decoder_manifest_request.ImportDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.import_decoder_manifest_response.ImportDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_decoder_manifest.async_import_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.import_decoder_manifest_request.ImportDecoderManifestRequest = {
            "name": name,
            "network_file_definitions": network_file_definitions,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_decoder_manifest_network_interfaces(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_response.ListDecoderManifestNetworkInterfacesResponse":
        """<p> Lists the network interfaces specified in a decoder manifest. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the decoder manifest to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_request.ListDecoderManifestNetworkInterfacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_response.ListDecoderManifestNetworkInterfacesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_network_interfaces

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_network_interfaces.async_list_decoder_manifest_network_interfaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_request.ListDecoderManifestNetworkInterfacesRequest = {
            "name": name
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

    async def list_decoder_manifest_signals(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_decoder_manifest_signals_response.ListDecoderManifestSignalsResponse":
        """<p> A list of information about signal decoders specified in a decoder manifest. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the decoder manifest to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_decoder_manifest_signals_request.ListDecoderManifestSignalsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_decoder_manifest_signals_response.ListDecoderManifestSignalsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_signals

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_signals.async_list_decoder_manifest_signals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_decoder_manifest_signals_request.ListDecoderManifestSignalsRequest = {
            "name": name
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
