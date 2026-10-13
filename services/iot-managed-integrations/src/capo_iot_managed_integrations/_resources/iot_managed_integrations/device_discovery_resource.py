from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
from capo_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.connector_association_id
    import capo_iot_managed_integrations.types.connector_device_id_list
    import capo_iot_managed_integrations.types.custom_protocol_detail
    import capo_iot_managed_integrations.types.device_discovery_id
    import capo_iot_managed_integrations.types.device_discovery_status
    import capo_iot_managed_integrations.types.device_discovery_summary
    import capo_iot_managed_integrations.types.discovered_device_summary
    import capo_iot_managed_integrations.types.discovery_auth_material_string
    import capo_iot_managed_integrations.types.discovery_auth_material_type
    import capo_iot_managed_integrations.types.discovery_type
    import capo_iot_managed_integrations.types.get_device_discovery_request
    import capo_iot_managed_integrations.types.get_device_discovery_response
    import capo_iot_managed_integrations.types.list_device_discoveries_request
    import capo_iot_managed_integrations.types.list_device_discoveries_response
    import capo_iot_managed_integrations.types.list_discovered_devices_request
    import capo_iot_managed_integrations.types.list_discovered_devices_response
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.protocol_type
    import capo_iot_managed_integrations.types.start_device_discovery_request
    import capo_iot_managed_integrations.types.start_device_discovery_response
    import capo_iot_managed_integrations.types.tags_map
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class DeviceDiscoveryResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        discovery_type: "capo_iot_managed_integrations.types.discovery_type.DiscoveryType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        custom_protocol_detail: Optional[
            "capo_iot_managed_integrations.types.custom_protocol_detail.CustomProtocolDetail"
        ] = None,
        controller_identifier: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
        connector_association_identifier: Optional[
            "capo_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
        ] = None,
        account_association_id: Optional[
            "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
        authentication_material: Optional[
            "capo_iot_managed_integrations.types.discovery_auth_material_string.DiscoveryAuthMaterialString"
        ] = None,
        authentication_material_type: Optional[
            "capo_iot_managed_integrations.types.discovery_auth_material_type.DiscoveryAuthMaterialType"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
        connector_device_id_list: Optional[
            "capo_iot_managed_integrations.types.connector_device_id_list.ConnectorDeviceIdList"
        ] = None,
        protocol: Optional[
            "capo_iot_managed_integrations.types.protocol_type.ProtocolType"
        ] = None,
        end_device_identifier: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse":
        """<p> This API is used to start device discovery for hub-connected and third-party-connected devices. The authentication material (install code) is delivered as a message to the controller instructing it to start the discovery.</p>

        Args:
            discovery_type: <p>The discovery type supporting the type of device to be discovered in the device discovery task request.</p>
            custom_protocol_detail: <p>Additional protocol-specific details required for device discovery, which vary based on the discovery type.</p> <note> <p>For a <code>DiscoveryType</code> of <code>CUSTOM</code>, the string-to-string map must have a key value of <code>Name</code> set to a non-empty-string.</p> </note>
            controller_identifier: <p>The id of the end-user's IoT hub.</p>
            connector_association_identifier: <p>The id of the connector association.</p>
            account_association_id: <p>The identifier of the cloud-to-cloud account association to use for discovery of third-party devices.</p>
            authentication_material: <p>The authentication material required to start the local device discovery job request.</p>
            authentication_material_type: <p>The type of authentication material used for device discovery jobs.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the device discovery request.</p>
            connector_device_id_list: <p>Used as a filter for PLA discoveries.</p>
            protocol: <p>The protocol type for capability rediscovery (ZWAVE, ZIGBEE, or CUSTOM).</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>
            end_device_identifier: <p>The unique id of the end device for capability rediscovery.</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery.start_device_discovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.start_device_discovery_request

            return capo_iot_managed_integrations.types.start_device_discovery_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartDeviceDiscovery", redact_input=_redact_input),
        )
        input_: capo_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest = {
            "discovery_type": discovery_type
        }
        if custom_protocol_detail is not None:
            input_["custom_protocol_detail"] = custom_protocol_detail
        if controller_identifier is not None:
            input_["controller_identifier"] = controller_identifier
        if connector_association_identifier is not None:
            input_["connector_association_identifier"] = (
                connector_association_identifier
            )
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id
        if authentication_material is not None:
            input_["authentication_material"] = authentication_material
        if authentication_material_type is not None:
            input_["authentication_material_type"] = authentication_material_type
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if connector_device_id_list is not None:
            input_["connector_device_id_list"] = connector_device_id_list
        if protocol is not None:
            input_["protocol"] = protocol
        if end_device_identifier is not None:
            input_["end_device_identifier"] = end_device_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        identifier: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse":
        """<p> Get the current state of a device discovery.</p>

        Args:
            identifier: <p>The id of the device discovery job request.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery.get_device_discovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_device_discovery_response

            return capo_iot_managed_integrations.types.get_device_discovery_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDeviceDiscovery", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest = {
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
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        type_filter: Optional[
            "capo_iot_managed_integrations.types.discovery_type.DiscoveryType"
        ] = None,
        status_filter: Optional[
            "capo_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse":
        """<p>Lists all device discovery tasks, with optional filtering by type and status.</p>

        Args:
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of device discovery jobs to return in a single response.</p>
            type_filter: <p>The discovery type to filter device discovery jobs by.</p>
            status_filter: <p>The status to filter device discovery jobs by.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries.list_device_discoveries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDeviceDiscoveries")
        )
        input_: capo_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type_filter is not None:
            input_["type_filter"] = type_filter
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_discovered_devices(
        self,
        identifier: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse":
        """<p>Lists all devices discovered during a specific device discovery task.</p>

        Args:
            identifier: <p>The identifier of the device discovery job to list discovered devices for.</p>
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of discovered devices to return in a single response.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices.list_discovered_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.list_discovered_devices_response

            return capo_iot_managed_integrations.types.list_discovered_devices_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListDiscoveredDevices", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest = {
            "identifier": identifier
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


class AsyncDeviceDiscoveryResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        discovery_type: "capo_iot_managed_integrations.types.discovery_type.DiscoveryType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        custom_protocol_detail: Optional[
            "capo_iot_managed_integrations.types.custom_protocol_detail.CustomProtocolDetail"
        ] = None,
        controller_identifier: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
        connector_association_identifier: Optional[
            "capo_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
        ] = None,
        account_association_id: Optional[
            "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
        authentication_material: Optional[
            "capo_iot_managed_integrations.types.discovery_auth_material_string.DiscoveryAuthMaterialString"
        ] = None,
        authentication_material_type: Optional[
            "capo_iot_managed_integrations.types.discovery_auth_material_type.DiscoveryAuthMaterialType"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
        connector_device_id_list: Optional[
            "capo_iot_managed_integrations.types.connector_device_id_list.ConnectorDeviceIdList"
        ] = None,
        protocol: Optional[
            "capo_iot_managed_integrations.types.protocol_type.ProtocolType"
        ] = None,
        end_device_identifier: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse":
        """<p> This API is used to start device discovery for hub-connected and third-party-connected devices. The authentication material (install code) is delivered as a message to the controller instructing it to start the discovery.</p>

        Args:
            discovery_type: <p>The discovery type supporting the type of device to be discovered in the device discovery task request.</p>
            custom_protocol_detail: <p>Additional protocol-specific details required for device discovery, which vary based on the discovery type.</p> <note> <p>For a <code>DiscoveryType</code> of <code>CUSTOM</code>, the string-to-string map must have a key value of <code>Name</code> set to a non-empty-string.</p> </note>
            controller_identifier: <p>The id of the end-user's IoT hub.</p>
            connector_association_identifier: <p>The id of the connector association.</p>
            account_association_id: <p>The identifier of the cloud-to-cloud account association to use for discovery of third-party devices.</p>
            authentication_material: <p>The authentication material required to start the local device discovery job request.</p>
            authentication_material_type: <p>The type of authentication material used for device discovery jobs.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the device discovery request.</p>
            connector_device_id_list: <p>Used as a filter for PLA discoveries.</p>
            protocol: <p>The protocol type for capability rediscovery (ZWAVE, ZIGBEE, or CUSTOM).</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>
            end_device_identifier: <p>The unique id of the end device for capability rediscovery.</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery.async_start_device_discovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.start_device_discovery_request

            return capo_iot_managed_integrations.types.start_device_discovery_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartDeviceDiscovery", redact_input=_redact_input),
        )
        input_: capo_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest = {
            "discovery_type": discovery_type
        }
        if custom_protocol_detail is not None:
            input_["custom_protocol_detail"] = custom_protocol_detail
        if controller_identifier is not None:
            input_["controller_identifier"] = controller_identifier
        if connector_association_identifier is not None:
            input_["connector_association_identifier"] = (
                connector_association_identifier
            )
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id
        if authentication_material is not None:
            input_["authentication_material"] = authentication_material
        if authentication_material_type is not None:
            input_["authentication_material_type"] = authentication_material_type
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if connector_device_id_list is not None:
            input_["connector_device_id_list"] = connector_device_id_list
        if protocol is not None:
            input_["protocol"] = protocol
        if end_device_identifier is not None:
            input_["end_device_identifier"] = end_device_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        identifier: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse":
        """<p> Get the current state of a device discovery.</p>

        Args:
            identifier: <p>The id of the device discovery job request.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery.async_get_device_discovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_device_discovery_response

            return capo_iot_managed_integrations.types.get_device_discovery_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDeviceDiscovery", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest = {
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
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        type_filter: Optional[
            "capo_iot_managed_integrations.types.discovery_type.DiscoveryType"
        ] = None,
        status_filter: Optional[
            "capo_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse":
        """<p>Lists all device discovery tasks, with optional filtering by type and status.</p>

        Args:
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of device discovery jobs to return in a single response.</p>
            type_filter: <p>The discovery type to filter device discovery jobs by.</p>
            status_filter: <p>The status to filter device discovery jobs by.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries.async_list_device_discoveries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDeviceDiscoveries")
        )
        input_: capo_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type_filter is not None:
            input_["type_filter"] = type_filter
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_discovered_devices(
        self,
        identifier: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse":
        """<p>Lists all devices discovered during a specific device discovery task.</p>

        Args:
            identifier: <p>The identifier of the device discovery job to list discovered devices for.</p>
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of discovered devices to return in a single response.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices.async_list_discovered_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.list_discovered_devices_response

            return capo_iot_managed_integrations.types.list_discovered_devices_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListDiscoveredDevices", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest = {
            "identifier": identifier
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
