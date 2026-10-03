from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
from capo_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.auth_material_string
    import capo_iot_managed_integrations.types.auth_material_type
    import capo_iot_managed_integrations.types.brand
    import capo_iot_managed_integrations.types.capabilities
    import capo_iot_managed_integrations.types.capability_id
    import capo_iot_managed_integrations.types.capability_report
    import capo_iot_managed_integrations.types.capability_schemas
    import capo_iot_managed_integrations.types.classification
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.connector_destination_id
    import capo_iot_managed_integrations.types.connector_device_id
    import capo_iot_managed_integrations.types.connector_policy_id
    import capo_iot_managed_integrations.types.create_managed_thing_request
    import capo_iot_managed_integrations.types.create_managed_thing_response
    import capo_iot_managed_integrations.types.credential_locker_id
    import capo_iot_managed_integrations.types.delete_managed_thing_request
    import capo_iot_managed_integrations.types.endpoint_id
    import capo_iot_managed_integrations.types.get_managed_thing_capabilities_request
    import capo_iot_managed_integrations.types.get_managed_thing_capabilities_response
    import capo_iot_managed_integrations.types.get_managed_thing_certificate_request
    import capo_iot_managed_integrations.types.get_managed_thing_certificate_response
    import capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_request
    import capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_response
    import capo_iot_managed_integrations.types.get_managed_thing_meta_data_request
    import capo_iot_managed_integrations.types.get_managed_thing_meta_data_response
    import capo_iot_managed_integrations.types.get_managed_thing_request
    import capo_iot_managed_integrations.types.get_managed_thing_response
    import capo_iot_managed_integrations.types.hub_network_mode
    import capo_iot_managed_integrations.types.list_managed_thing_schemas_request
    import capo_iot_managed_integrations.types.list_managed_thing_schemas_response
    import capo_iot_managed_integrations.types.list_managed_things_request
    import capo_iot_managed_integrations.types.list_managed_things_response
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.managed_thing_schema_list_item
    import capo_iot_managed_integrations.types.managed_thing_summary
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.meta_data
    import capo_iot_managed_integrations.types.model
    import capo_iot_managed_integrations.types.name
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.owner
    import capo_iot_managed_integrations.types.parent_controller_id
    import capo_iot_managed_integrations.types.provisioning_status
    import capo_iot_managed_integrations.types.role
    import capo_iot_managed_integrations.types.serial_number
    import capo_iot_managed_integrations.types.tags_map
    import capo_iot_managed_integrations.types.update_managed_thing_request
    import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class ManagedThingResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        role: "capo_iot_managed_integrations.types.role.Role",
        authentication_material: "capo_iot_managed_integrations.types.auth_material_string.AuthMaterialString",
        authentication_material_type: "capo_iot_managed_integrations.types.auth_material_type.AuthMaterialType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        owner: Optional["capo_iot_managed_integrations.types.owner.Owner"] = None,
        credential_locker_id: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        wi_fi_simple_setup_configuration: Optional[
            "capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
        ] = None,
        serial_number: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        brand: Optional["capo_iot_managed_integrations.types.brand.Brand"] = None,
        model: Optional["capo_iot_managed_integrations.types.model.Model"] = None,
        name: Optional["capo_iot_managed_integrations.types.name.Name"] = None,
        capability_report: Optional[
            "capo_iot_managed_integrations.types.capability_report.CapabilityReport"
        ] = None,
        capability_schemas: Optional[
            "capo_iot_managed_integrations.types.capability_schemas.CapabilitySchemas"
        ] = None,
        capabilities: Optional[
            "capo_iot_managed_integrations.types.capabilities.Capabilities"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        classification: Optional[
            "capo_iot_managed_integrations.types.classification.Classification"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
        meta_data: Optional[
            "capo_iot_managed_integrations.types.meta_data.MetaData"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_managed_thing_response.CreateManagedThingResponse":
        """<p>Creates a managed thing. A managed thing contains the device identifier, protocol supported, and capabilities of the device in a data model format defined by Managed integrations.</p>

        Args:
            role: <p>The type of device used. This will be the hub controller, cloud device, or AWS IoT device.</p>
            owner: <p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>
            credential_locker_id: <p>The identifier of the credential for the managed thing.</p>
            authentication_material: <p>The authentication material defining the device connectivity setup requests. The authorization materials used are the device bar code.</p>
            authentication_material_type: <p>The type of authentication material used for device connectivity setup requests.</p>
            wi_fi_simple_setup_configuration: <p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>
            serial_number: <p>The serial number of the device.</p>
            brand: <p>The brand of the device.</p>
            model: <p>The model of the device.</p>
            name: <p>The name of the managed thing representing the physical device.</p>
            capability_report: <p>A report of the capabilities for the managed thing.</p>
            capability_schemas: <p>The capability schemas that define the functionality and features supported by the managed thing, including device capabilities and their associated properties.</p>
            capabilities: <p>The capabilities of the device such as light bulb.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            classification: <p>The classification of the managed thing such as light bulb or thermostat.</p>
            tags: <p>A set of key/value pairs that are used to manage the managed thing.</p>
            meta_data: <p>The metadata for the managed thing.</p> <note> <p>The <code>managedThing</code> <code>metadata</code> parameter is used for associating attributes with a <code>managedThing</code> that can be used for grouping over-the-air (OTA) tasks. Name value pairs in <code>metadata</code> can be used in the <code>OtaTargetQueryString</code> parameter for the <code>CreateOtaTask</code> API operation.</p> </note>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.create_managed_thing_request.CreateManagedThingRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.create_managed_thing_response.CreateManagedThingResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_managed_thing

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.create_managed_thing.create_managed_thing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_managed_thing_request.CreateManagedThingRequest = {
            "role": role,
            "authentication_material": authentication_material,
            "authentication_material_type": authentication_material_type,
        }
        if owner is not None:
            input_["owner"] = owner
        if credential_locker_id is not None:
            input_["credential_locker_id"] = credential_locker_id
        if wi_fi_simple_setup_configuration is not None:
            input_["wi_fi_simple_setup_configuration"] = (
                wi_fi_simple_setup_configuration
            )
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if brand is not None:
            input_["brand"] = brand
        if model is not None:
            input_["model"] = model
        if name is not None:
            input_["name"] = name
        if capability_report is not None:
            input_["capability_report"] = capability_report
        if capability_schemas is not None:
            input_["capability_schemas"] = capability_schemas
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if classification is not None:
            input_["classification"] = classification
        if tags is not None:
            input_["tags"] = tags
        if meta_data is not None:
            input_["meta_data"] = meta_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_response.GetManagedThingResponse":
        """<p> Get details of a managed thing including its attributes and capabilities.</p>

        Args:
            identifier: <p>The id of the managed thing.</p>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.get_managed_thing_request.GetManagedThingRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_response.GetManagedThingResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing.get_managed_thing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_request.GetManagedThingRequest = {
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
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        owner: Optional["capo_iot_managed_integrations.types.owner.Owner"] = None,
        credential_locker_id: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        serial_number: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        wi_fi_simple_setup_configuration: Optional[
            "capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
        ] = None,
        brand: Optional["capo_iot_managed_integrations.types.brand.Brand"] = None,
        model: Optional["capo_iot_managed_integrations.types.model.Model"] = None,
        name: Optional["capo_iot_managed_integrations.types.name.Name"] = None,
        capability_report: Optional[
            "capo_iot_managed_integrations.types.capability_report.CapabilityReport"
        ] = None,
        capability_schemas: Optional[
            "capo_iot_managed_integrations.types.capability_schemas.CapabilitySchemas"
        ] = None,
        capabilities: Optional[
            "capo_iot_managed_integrations.types.capabilities.Capabilities"
        ] = None,
        classification: Optional[
            "capo_iot_managed_integrations.types.classification.Classification"
        ] = None,
        hub_network_mode: Optional[
            "capo_iot_managed_integrations.types.hub_network_mode.HubNetworkMode"
        ] = None,
        meta_data: Optional[
            "capo_iot_managed_integrations.types.meta_data.MetaData"
        ] = None,
    ) -> None:
        """<p>Update the attributes and capabilities associated with a managed thing.</p>

        Args:
            identifier: <p>The id of the managed thing.</p>
            owner: <p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>
            credential_locker_id: <p>The identifier of the credential for the managed thing.</p>
            serial_number: <p>The serial number of the device.</p>
            wi_fi_simple_setup_configuration: <p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>
            brand: <p>The brand of the device.</p>
            model: <p>The model of the device.</p>
            name: <p>The name of the managed thing representing the physical device.</p>
            capability_report: <p>A report of the capabilities for the managed thing.</p>
            capability_schemas: <p>The updated capability schemas that define the functionality and features supported by the managed thing.</p>
            capabilities: <p>The capabilities of the device such as light bulb.</p>
            classification: <p>The classification of the managed thing such as light bulb or thermostat.</p>
            hub_network_mode: <p>The network mode for the hub-connected device.</p>
            meta_data: <p>The metadata for the managed thing.</p>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.update_managed_thing_request.UpdateManagedThingRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_managed_thing

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.update_managed_thing.update_managed_thing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_managed_thing_request.UpdateManagedThingRequest = {
            "identifier": identifier
        }
        if owner is not None:
            input_["owner"] = owner
        if credential_locker_id is not None:
            input_["credential_locker_id"] = credential_locker_id
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if wi_fi_simple_setup_configuration is not None:
            input_["wi_fi_simple_setup_configuration"] = (
                wi_fi_simple_setup_configuration
            )
        if brand is not None:
            input_["brand"] = brand
        if model is not None:
            input_["model"] = model
        if name is not None:
            input_["name"] = name
        if capability_report is not None:
            input_["capability_report"] = capability_report
        if capability_schemas is not None:
            input_["capability_schemas"] = capability_schemas
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if classification is not None:
            input_["classification"] = classification
        if hub_network_mode is not None:
            input_["hub_network_mode"] = hub_network_mode
        if meta_data is not None:
            input_["meta_data"] = meta_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> None:
        """<p>Delete a managed thing. For direct-connected and hub-connected devices connecting with Managed integrations via a controller, all of the devices connected to it will have their status changed to <code>PENDING</code>. It is not possible to remove a cloud-to-cloud device.</p>

        Args:
            identifier: <p>The id of the managed thing.</p>
            force: <p>When set to <code>TRUE</code>, a forceful deteletion of the managed thing will occur. When set to <code>FALSE</code>, a non-forceful deletion of the managed thing will occur.</p>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.delete_managed_thing_request.DeleteManagedThingRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_managed_thing

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.delete_managed_thing.delete_managed_thing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_managed_thing_request.DeleteManagedThingRequest = {
            "identifier": identifier
        }
        if force is not None:
            input_["force"] = force

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
        owner_filter: Optional[
            "capo_iot_managed_integrations.types.owner.Owner"
        ] = None,
        credential_locker_filter: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        role_filter: Optional["capo_iot_managed_integrations.types.role.Role"] = None,
        parent_controller_identifier_filter: Optional[
            "capo_iot_managed_integrations.types.parent_controller_id.ParentControllerId"
        ] = None,
        connector_policy_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_policy_id.ConnectorPolicyId"
        ] = None,
        connector_destination_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        connector_device_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
        ] = None,
        serial_number_filter: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        provisioning_status_filter: Optional[
            "capo_iot_managed_integrations.types.provisioning_status.ProvisioningStatus"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse":
        """<p>Listing all managed things with provision for filters.</p>

        Args:
            owner_filter: <p>Filter on device owners when listing managed things.</p>
            credential_locker_filter: <p>Filter on a credential locker for a managed thing.</p>
            role_filter: <p>Filter on the type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.</p>
            parent_controller_identifier_filter: <p>Filter on a parent controller id for a managed thing.</p>
            connector_policy_id_filter: <p>Filter on a connector policy id for a managed thing.</p>
            connector_destination_id_filter: <p>Filter managed things by the connector destination ID they are associated with.</p>
            connector_device_id_filter: <p>Filter managed things by the connector device ID they are associated with. When specified, only managed things with this connector device ID will be returned.</p>
            serial_number_filter: <p>Filter on the serial number of the device.</p>
            provisioning_status_filter: <p>Filter on the status of the device. For more information, see <a href="https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html">Device Provisioning</a>.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.list_managed_things_request.ListManagedThingsRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_things

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_things.list_managed_things(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_managed_things_request.ListManagedThingsRequest = {}
        if owner_filter is not None:
            input_["owner_filter"] = owner_filter
        if credential_locker_filter is not None:
            input_["credential_locker_filter"] = credential_locker_filter
        if role_filter is not None:
            input_["role_filter"] = role_filter
        if parent_controller_identifier_filter is not None:
            input_["parent_controller_identifier_filter"] = (
                parent_controller_identifier_filter
            )
        if connector_policy_id_filter is not None:
            input_["connector_policy_id_filter"] = connector_policy_id_filter
        if connector_destination_id_filter is not None:
            input_["connector_destination_id_filter"] = connector_destination_id_filter
        if connector_device_id_filter is not None:
            input_["connector_device_id_filter"] = connector_device_id_filter
        if serial_number_filter is not None:
            input_["serial_number_filter"] = serial_number_filter
        if provisioning_status_filter is not None:
            input_["provisioning_status_filter"] = provisioning_status_filter
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

    def get_managed_thing_capabilities(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_capabilities_response.GetManagedThingCapabilitiesResponse":
        """<p>Get the capabilities for a managed thing using the device ID.</p>

        Args:
            identifier: <p>The id of the device.</p>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.get_managed_thing_capabilities_request.GetManagedThingCapabilitiesRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_capabilities_response.GetManagedThingCapabilitiesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_capabilities

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_capabilities.get_managed_thing_capabilities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_capabilities_request.GetManagedThingCapabilitiesRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_managed_thing_certificate(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_certificate_response.GetManagedThingCertificateResponse":
        """<p>Retrieves the certificate PEM for a managed IoT thing.</p>

        Args:
            identifier: <p>The identifier of the managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get managed thing certificate

            >>> client.get_managed_thing_certificate(identifier='example-managed-thing-id')
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_managed_thing_certificate_request.GetManagedThingCertificateRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_certificate_response.GetManagedThingCertificateResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_certificate

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_certificate.get_managed_thing_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_certificate_request.GetManagedThingCertificateRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_managed_thing_connectivity_data(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_response.GetManagedThingConnectivityDataResponse":
        """<p>Get the connectivity status of a managed thing.</p>

        Args:
            identifier: <p>The identifier of a managed thing.</p>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_request.GetManagedThingConnectivityDataRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_response.GetManagedThingConnectivityDataResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_connectivity_data

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_connectivity_data.get_managed_thing_connectivity_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_request.GetManagedThingConnectivityDataRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_managed_thing_meta_data(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_meta_data_response.GetManagedThingMetaDataResponse":
        """<p>Get the metadata information for a managed thing.</p> <note> <p>The <code>managedThing</code> <code>metadata</code> parameter is used for associating attributes with a <code>managedThing</code> that can be used for grouping over-the-air (OTA) tasks. Name value pairs in <code>metadata</code> can be used in the <code>OtaTargetQueryString</code> parameter for the <code>CreateOtaTask</code> API operation.</p> </note>

        Args:
            identifier: <p>The managed thing id.</p>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.get_managed_thing_meta_data_request.GetManagedThingMetaDataRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_meta_data_response.GetManagedThingMetaDataResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_meta_data

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_meta_data.get_managed_thing_meta_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_meta_data_request.GetManagedThingMetaDataRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_managed_thing_schemas(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        endpoint_id_filter: Optional[
            "capo_iot_managed_integrations.types.endpoint_id.EndpointId"
        ] = None,
        capability_id_filter: Optional[
            "capo_iot_managed_integrations.types.capability_id.CapabilityId"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_managed_thing_schemas_response.ListManagedThingSchemasResponse":
        """<p>List schemas associated with a managed thing.</p>

        Args:
            identifier: <p>The managed thing id.</p>
            endpoint_id_filter: <p>Filter on an endpoint id.</p>
            capability_id_filter: <p>Filter on a capability id.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.list_managed_thing_schemas_request.ListManagedThingSchemasRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_managed_thing_schemas_response.ListManagedThingSchemasResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_schemas

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_schemas.list_managed_thing_schemas(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_managed_thing_schemas_request.ListManagedThingSchemasRequest = {
            "identifier": identifier
        }
        if endpoint_id_filter is not None:
            input_["endpoint_id_filter"] = endpoint_id_filter
        if capability_id_filter is not None:
            input_["capability_id_filter"] = capability_id_filter
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


class AsyncManagedThingResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        role: "capo_iot_managed_integrations.types.role.Role",
        authentication_material: "capo_iot_managed_integrations.types.auth_material_string.AuthMaterialString",
        authentication_material_type: "capo_iot_managed_integrations.types.auth_material_type.AuthMaterialType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        owner: Optional["capo_iot_managed_integrations.types.owner.Owner"] = None,
        credential_locker_id: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        wi_fi_simple_setup_configuration: Optional[
            "capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
        ] = None,
        serial_number: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        brand: Optional["capo_iot_managed_integrations.types.brand.Brand"] = None,
        model: Optional["capo_iot_managed_integrations.types.model.Model"] = None,
        name: Optional["capo_iot_managed_integrations.types.name.Name"] = None,
        capability_report: Optional[
            "capo_iot_managed_integrations.types.capability_report.CapabilityReport"
        ] = None,
        capability_schemas: Optional[
            "capo_iot_managed_integrations.types.capability_schemas.CapabilitySchemas"
        ] = None,
        capabilities: Optional[
            "capo_iot_managed_integrations.types.capabilities.Capabilities"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        classification: Optional[
            "capo_iot_managed_integrations.types.classification.Classification"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
        meta_data: Optional[
            "capo_iot_managed_integrations.types.meta_data.MetaData"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_managed_thing_response.CreateManagedThingResponse":
        """<p>Creates a managed thing. A managed thing contains the device identifier, protocol supported, and capabilities of the device in a data model format defined by Managed integrations.</p>

        Args:
            role: <p>The type of device used. This will be the hub controller, cloud device, or AWS IoT device.</p>
            owner: <p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>
            credential_locker_id: <p>The identifier of the credential for the managed thing.</p>
            authentication_material: <p>The authentication material defining the device connectivity setup requests. The authorization materials used are the device bar code.</p>
            authentication_material_type: <p>The type of authentication material used for device connectivity setup requests.</p>
            wi_fi_simple_setup_configuration: <p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>
            serial_number: <p>The serial number of the device.</p>
            brand: <p>The brand of the device.</p>
            model: <p>The model of the device.</p>
            name: <p>The name of the managed thing representing the physical device.</p>
            capability_report: <p>A report of the capabilities for the managed thing.</p>
            capability_schemas: <p>The capability schemas that define the functionality and features supported by the managed thing, including device capabilities and their associated properties.</p>
            capabilities: <p>The capabilities of the device such as light bulb.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            classification: <p>The classification of the managed thing such as light bulb or thermostat.</p>
            tags: <p>A set of key/value pairs that are used to manage the managed thing.</p>
            meta_data: <p>The metadata for the managed thing.</p> <note> <p>The <code>managedThing</code> <code>metadata</code> parameter is used for associating attributes with a <code>managedThing</code> that can be used for grouping over-the-air (OTA) tasks. Name value pairs in <code>metadata</code> can be used in the <code>OtaTargetQueryString</code> parameter for the <code>CreateOtaTask</code> API operation.</p> </note>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_managed_thing_request.CreateManagedThingRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_managed_thing_response.CreateManagedThingResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_managed_thing

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_managed_thing.async_create_managed_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_managed_thing_request.CreateManagedThingRequest = {
            "role": role,
            "authentication_material": authentication_material,
            "authentication_material_type": authentication_material_type,
        }
        if owner is not None:
            input_["owner"] = owner
        if credential_locker_id is not None:
            input_["credential_locker_id"] = credential_locker_id
        if wi_fi_simple_setup_configuration is not None:
            input_["wi_fi_simple_setup_configuration"] = (
                wi_fi_simple_setup_configuration
            )
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if brand is not None:
            input_["brand"] = brand
        if model is not None:
            input_["model"] = model
        if name is not None:
            input_["name"] = name
        if capability_report is not None:
            input_["capability_report"] = capability_report
        if capability_schemas is not None:
            input_["capability_schemas"] = capability_schemas
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if classification is not None:
            input_["classification"] = classification
        if tags is not None:
            input_["tags"] = tags
        if meta_data is not None:
            input_["meta_data"] = meta_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_response.GetManagedThingResponse":
        """<p> Get details of a managed thing including its attributes and capabilities.</p>

        Args:
            identifier: <p>The id of the managed thing.</p>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_request.GetManagedThingRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_response.GetManagedThingResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing.async_get_managed_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_request.GetManagedThingRequest = {
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
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        owner: Optional["capo_iot_managed_integrations.types.owner.Owner"] = None,
        credential_locker_id: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        serial_number: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        wi_fi_simple_setup_configuration: Optional[
            "capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
        ] = None,
        brand: Optional["capo_iot_managed_integrations.types.brand.Brand"] = None,
        model: Optional["capo_iot_managed_integrations.types.model.Model"] = None,
        name: Optional["capo_iot_managed_integrations.types.name.Name"] = None,
        capability_report: Optional[
            "capo_iot_managed_integrations.types.capability_report.CapabilityReport"
        ] = None,
        capability_schemas: Optional[
            "capo_iot_managed_integrations.types.capability_schemas.CapabilitySchemas"
        ] = None,
        capabilities: Optional[
            "capo_iot_managed_integrations.types.capabilities.Capabilities"
        ] = None,
        classification: Optional[
            "capo_iot_managed_integrations.types.classification.Classification"
        ] = None,
        hub_network_mode: Optional[
            "capo_iot_managed_integrations.types.hub_network_mode.HubNetworkMode"
        ] = None,
        meta_data: Optional[
            "capo_iot_managed_integrations.types.meta_data.MetaData"
        ] = None,
    ) -> None:
        """<p>Update the attributes and capabilities associated with a managed thing.</p>

        Args:
            identifier: <p>The id of the managed thing.</p>
            owner: <p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>
            credential_locker_id: <p>The identifier of the credential for the managed thing.</p>
            serial_number: <p>The serial number of the device.</p>
            wi_fi_simple_setup_configuration: <p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>
            brand: <p>The brand of the device.</p>
            model: <p>The model of the device.</p>
            name: <p>The name of the managed thing representing the physical device.</p>
            capability_report: <p>A report of the capabilities for the managed thing.</p>
            capability_schemas: <p>The updated capability schemas that define the functionality and features supported by the managed thing.</p>
            capabilities: <p>The capabilities of the device such as light bulb.</p>
            classification: <p>The classification of the managed thing such as light bulb or thermostat.</p>
            hub_network_mode: <p>The network mode for the hub-connected device.</p>
            meta_data: <p>The metadata for the managed thing.</p>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_managed_thing_request.UpdateManagedThingRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_managed_thing

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_managed_thing.async_update_managed_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_managed_thing_request.UpdateManagedThingRequest = {
            "identifier": identifier
        }
        if owner is not None:
            input_["owner"] = owner
        if credential_locker_id is not None:
            input_["credential_locker_id"] = credential_locker_id
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if wi_fi_simple_setup_configuration is not None:
            input_["wi_fi_simple_setup_configuration"] = (
                wi_fi_simple_setup_configuration
            )
        if brand is not None:
            input_["brand"] = brand
        if model is not None:
            input_["model"] = model
        if name is not None:
            input_["name"] = name
        if capability_report is not None:
            input_["capability_report"] = capability_report
        if capability_schemas is not None:
            input_["capability_schemas"] = capability_schemas
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if classification is not None:
            input_["classification"] = classification
        if hub_network_mode is not None:
            input_["hub_network_mode"] = hub_network_mode
        if meta_data is not None:
            input_["meta_data"] = meta_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> None:
        """<p>Delete a managed thing. For direct-connected and hub-connected devices connecting with Managed integrations via a controller, all of the devices connected to it will have their status changed to <code>PENDING</code>. It is not possible to remove a cloud-to-cloud device.</p>

        Args:
            identifier: <p>The id of the managed thing.</p>
            force: <p>When set to <code>TRUE</code>, a forceful deteletion of the managed thing will occur. When set to <code>FALSE</code>, a non-forceful deletion of the managed thing will occur.</p>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_managed_thing_request.DeleteManagedThingRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_managed_thing

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_managed_thing.async_delete_managed_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_managed_thing_request.DeleteManagedThingRequest = {
            "identifier": identifier
        }
        if force is not None:
            input_["force"] = force

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
        owner_filter: Optional[
            "capo_iot_managed_integrations.types.owner.Owner"
        ] = None,
        credential_locker_filter: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        role_filter: Optional["capo_iot_managed_integrations.types.role.Role"] = None,
        parent_controller_identifier_filter: Optional[
            "capo_iot_managed_integrations.types.parent_controller_id.ParentControllerId"
        ] = None,
        connector_policy_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_policy_id.ConnectorPolicyId"
        ] = None,
        connector_destination_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        connector_device_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
        ] = None,
        serial_number_filter: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        provisioning_status_filter: Optional[
            "capo_iot_managed_integrations.types.provisioning_status.ProvisioningStatus"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse":
        """<p>Listing all managed things with provision for filters.</p>

        Args:
            owner_filter: <p>Filter on device owners when listing managed things.</p>
            credential_locker_filter: <p>Filter on a credential locker for a managed thing.</p>
            role_filter: <p>Filter on the type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.</p>
            parent_controller_identifier_filter: <p>Filter on a parent controller id for a managed thing.</p>
            connector_policy_id_filter: <p>Filter on a connector policy id for a managed thing.</p>
            connector_destination_id_filter: <p>Filter managed things by the connector destination ID they are associated with.</p>
            connector_device_id_filter: <p>Filter managed things by the connector device ID they are associated with. When specified, only managed things with this connector device ID will be returned.</p>
            serial_number_filter: <p>Filter on the serial number of the device.</p>
            provisioning_status_filter: <p>Filter on the status of the device. For more information, see <a href="https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html">Device Provisioning</a>.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_managed_things_request.ListManagedThingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_things

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_things.async_list_managed_things(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_managed_things_request.ListManagedThingsRequest = {}
        if owner_filter is not None:
            input_["owner_filter"] = owner_filter
        if credential_locker_filter is not None:
            input_["credential_locker_filter"] = credential_locker_filter
        if role_filter is not None:
            input_["role_filter"] = role_filter
        if parent_controller_identifier_filter is not None:
            input_["parent_controller_identifier_filter"] = (
                parent_controller_identifier_filter
            )
        if connector_policy_id_filter is not None:
            input_["connector_policy_id_filter"] = connector_policy_id_filter
        if connector_destination_id_filter is not None:
            input_["connector_destination_id_filter"] = connector_destination_id_filter
        if connector_device_id_filter is not None:
            input_["connector_device_id_filter"] = connector_device_id_filter
        if serial_number_filter is not None:
            input_["serial_number_filter"] = serial_number_filter
        if provisioning_status_filter is not None:
            input_["provisioning_status_filter"] = provisioning_status_filter
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

    async def get_managed_thing_capabilities(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_capabilities_response.GetManagedThingCapabilitiesResponse":
        """<p>Get the capabilities for a managed thing using the device ID.</p>

        Args:
            identifier: <p>The id of the device.</p>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_capabilities_request.GetManagedThingCapabilitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_capabilities_response.GetManagedThingCapabilitiesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_capabilities

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_capabilities.async_get_managed_thing_capabilities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_capabilities_request.GetManagedThingCapabilitiesRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_managed_thing_certificate(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_certificate_response.GetManagedThingCertificateResponse":
        """<p>Retrieves the certificate PEM for a managed IoT thing.</p>

        Args:
            identifier: <p>The identifier of the managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get managed thing certificate

            >>> await client.get_managed_thing_certificate(identifier='example-managed-thing-id')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_certificate_request.GetManagedThingCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_certificate_response.GetManagedThingCertificateResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_certificate

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_certificate.async_get_managed_thing_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_certificate_request.GetManagedThingCertificateRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_managed_thing_connectivity_data(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_response.GetManagedThingConnectivityDataResponse":
        """<p>Get the connectivity status of a managed thing.</p>

        Args:
            identifier: <p>The identifier of a managed thing.</p>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_request.GetManagedThingConnectivityDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_response.GetManagedThingConnectivityDataResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_connectivity_data

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_connectivity_data.async_get_managed_thing_connectivity_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_request.GetManagedThingConnectivityDataRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_managed_thing_meta_data(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_meta_data_response.GetManagedThingMetaDataResponse":
        """<p>Get the metadata information for a managed thing.</p> <note> <p>The <code>managedThing</code> <code>metadata</code> parameter is used for associating attributes with a <code>managedThing</code> that can be used for grouping over-the-air (OTA) tasks. Name value pairs in <code>metadata</code> can be used in the <code>OtaTargetQueryString</code> parameter for the <code>CreateOtaTask</code> API operation.</p> </note>

        Args:
            identifier: <p>The managed thing id.</p>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_meta_data_request.GetManagedThingMetaDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_meta_data_response.GetManagedThingMetaDataResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_meta_data

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_meta_data.async_get_managed_thing_meta_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_meta_data_request.GetManagedThingMetaDataRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_thing_schemas(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        endpoint_id_filter: Optional[
            "capo_iot_managed_integrations.types.endpoint_id.EndpointId"
        ] = None,
        capability_id_filter: Optional[
            "capo_iot_managed_integrations.types.capability_id.CapabilityId"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_managed_thing_schemas_response.ListManagedThingSchemasResponse":
        """<p>List schemas associated with a managed thing.</p>

        Args:
            identifier: <p>The managed thing id.</p>
            endpoint_id_filter: <p>Filter on an endpoint id.</p>
            capability_id_filter: <p>Filter on a capability id.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_managed_thing_schemas_request.ListManagedThingSchemasRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_managed_thing_schemas_response.ListManagedThingSchemasResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_schemas

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_schemas.async_list_managed_thing_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_managed_thing_schemas_request.ListManagedThingSchemasRequest = {
            "identifier": identifier
        }
        if endpoint_id_filter is not None:
            input_["endpoint_id_filter"] = endpoint_id_filter
        if capability_id_filter is not None:
            input_["capability_id_filter"] = capability_id_filter
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
