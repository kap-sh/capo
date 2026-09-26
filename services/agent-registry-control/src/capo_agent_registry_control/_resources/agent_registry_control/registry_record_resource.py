from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_agent_registry_control._auth._signers
import capo_agent_registry_control._auth._sigv4
from capo_agent_registry_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_agent_registry_control.types.client_token
    import capo_agent_registry_control.types.create_registry_record_request
    import capo_agent_registry_control.types.create_registry_record_response
    import capo_agent_registry_control.types.delete_registry_record_request
    import capo_agent_registry_control.types.delete_registry_record_response
    import capo_agent_registry_control.types.description
    import capo_agent_registry_control.types.descriptors
    import capo_agent_registry_control.types.get_registry_record_request
    import capo_agent_registry_control.types.get_registry_record_response
    import capo_agent_registry_control.types.list_registry_records_request
    import capo_agent_registry_control.types.list_registry_records_response
    import capo_agent_registry_control.types.max_results
    import capo_agent_registry_control.types.next_token
    import capo_agent_registry_control.types.provenance_list
    import capo_agent_registry_control.types.record_identifier
    import capo_agent_registry_control.types.record_type
    import capo_agent_registry_control.types.registry_identifier
    import capo_agent_registry_control.types.registry_record_display_name
    import capo_agent_registry_control.types.registry_record_filter_list
    import capo_agent_registry_control.types.registry_record_name
    import capo_agent_registry_control.types.registry_record_status
    import capo_agent_registry_control.types.registry_record_summary
    import capo_agent_registry_control.types.registry_record_version
    import capo_agent_registry_control.types.submit_registry_record_for_approval_request
    import capo_agent_registry_control.types.submit_registry_record_for_approval_response
    import capo_agent_registry_control.types.tags_map
    import capo_agent_registry_control.types.update_registry_record_request
    import capo_agent_registry_control.types.update_registry_record_response
    import capo_agent_registry_control.types.update_registry_record_status_request
    import capo_agent_registry_control.types.update_registry_record_status_response
    import capo_agent_registry_control.types.updated_description
    import capo_agent_registry_control.types.updated_descriptors
    import capo_agent_registry_control.types.updated_display_name
    from capo_agent_registry_control._services.agent_registry_control import (
        AgentRegistryControlClient,
        AgentRegistryControlClientConfig,
    )
    from capo_agent_registry_control._services.async_agent_registry_control import (
        AsyncAgentRegistryControlClient,
        AsyncAgentRegistryControlClientConfig,
    )


class RegistryRecordResource:
    def __init__(self, service: AgentRegistryControlClient) -> None:
        self._service = service

    def create(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        name: "capo_agent_registry_control.types.registry_record_name.RegistryRecordName",
        record_type: "capo_agent_registry_control.types.record_type.RecordType",
        descriptors: "capo_agent_registry_control.types.descriptors.Descriptors",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        display_name: Optional[
            "capo_agent_registry_control.types.registry_record_display_name.RegistryRecordDisplayName"
        ] = None,
        description: Optional[
            "capo_agent_registry_control.types.description.Description"
        ] = None,
        record_version: Optional[
            "capo_agent_registry_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        client_token: Optional[
            "capo_agent_registry_control.types.client_token.ClientToken"
        ] = None,
        provenance: Optional[
            "capo_agent_registry_control.types.provenance_list.ProvenanceList"
        ] = None,
        tags: Optional["capo_agent_registry_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_agent_registry_control.types.create_registry_record_response.CreateRegistryRecordResponse":
        """<p>Creates a registry record within a registry. A registry record describes a discoverable resource, such as an MCP server, an agent, an agent skill, or a custom resource. Creation is asynchronous: the record is returned with the CREATING status while it is processed.</p>

        Args:
            registry_id: <p>The identifier of the registry in which to create the record (ARN or ID)</p>
            name: <p>The name of the registry record</p>
            display_name: <p>The human-readable display name of the registry record</p>
            description: <p>The description of the registry record</p>
            record_type: <p>The type of the registry record, which determines the descriptor format</p>
            descriptors: <p>The typed descriptor content for the registry record</p>
            record_version: <p>The version of the registry record</p>
            client_token: <p>Client token for idempotency</p>
            tags: <p>Tags to associate with the registry record</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.create_registry_record_request.CreateRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.create_registry_record_response.CreateRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.create_registry_record

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.create_registry_record.create_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.create_registry_record_request.CreateRegistryRecordRequest = {
            "registry_id": registry_id,
            "name": name,
            "record_type": record_type,
            "descriptors": descriptors,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if record_version is not None:
            input_["record_version"] = record_version
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if provenance is not None:
            input_["provenance"] = provenance
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
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.get_registry_record_response.GetRegistryRecordResponse":
        """<p>Retrieves the details of a registry record</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to retrieve (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.get_registry_record_request.GetRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.get_registry_record_response.GetRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.get_registry_record

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.get_registry_record.get_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.get_registry_record_request.GetRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
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
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        name: Optional[
            "capo_agent_registry_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        display_name: Optional[
            "capo_agent_registry_control.types.updated_display_name.UpdatedDisplayName"
        ] = None,
        description: Optional[
            "capo_agent_registry_control.types.updated_description.UpdatedDescription"
        ] = None,
        record_type: Optional[
            "capo_agent_registry_control.types.record_type.RecordType"
        ] = None,
        descriptors: Optional[
            "capo_agent_registry_control.types.updated_descriptors.UpdatedDescriptors"
        ] = None,
        record_version: Optional[
            "capo_agent_registry_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        trigger_synchronization: Optional[bool] = None,
        provenance: Optional[
            "capo_agent_registry_control.types.provenance_list.ProvenanceList"
        ] = None,
    ) -> "capo_agent_registry_control.types.update_registry_record_response.UpdateRegistryRecordResponse":
        """<p>Updates a registry record. The update is asynchronous: the record is returned with the UPDATING status while it is processed. Fields that use update wrappers follow PATCH semantics: omit the field to leave it unchanged.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to update (ARN or ID)</p>
            name: <p>The updated name of the registry record. Omit to leave the name unchanged.</p>
            display_name: <p>The updated display name of the registry record. Omit to leave the display name unchanged; provide an empty wrapper to unset it.</p>
            description: <p>The updated description of the registry record. Omit to leave the description unchanged; provide an empty wrapper to unset it.</p>
            record_type: <p>The updated type of the registry record. Omit to leave the record type unchanged.</p>
            descriptors: <p>The updated typed descriptor content for the registry record. Omit to leave the descriptors unchanged.</p>
            record_version: <p>The updated version of the registry record. Omit to leave the version unchanged.</p>
            trigger_synchronization: <p>Whether to trigger synchronization of the record's descriptor content from its source</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.update_registry_record_request.UpdateRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.update_registry_record_response.UpdateRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.update_registry_record

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.update_registry_record.update_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.update_registry_record_request.UpdateRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }
        if name is not None:
            input_["name"] = name
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if record_type is not None:
            input_["record_type"] = record_type
        if descriptors is not None:
            input_["descriptors"] = descriptors
        if record_version is not None:
            input_["record_version"] = record_version
        if trigger_synchronization is not None:
            input_["trigger_synchronization"] = trigger_synchronization
        if provenance is not None:
            input_["provenance"] = provenance

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.delete_registry_record_response.DeleteRegistryRecordResponse":
        """<p>Deletes a registry record</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to delete (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.delete_registry_record_request.DeleteRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.delete_registry_record_response.DeleteRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.delete_registry_record

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.delete_registry_record.delete_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.delete_registry_record_request.DeleteRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
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
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        max_results: Optional[
            "capo_agent_registry_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_agent_registry_control.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "capo_agent_registry_control.types.registry_record_filter_list.RegistryRecordFilterList"
        ] = None,
    ) -> "capo_agent_registry_control.types.list_registry_records_response.ListRegistryRecordsResponse":
        """<p>Lists the registry records within a registry, with optional filtering by name, status, and record type</p>

        Args:
            registry_id: <p>The identifier of the registry to list records from (ARN or ID)</p>
            max_results: <p>Maximum number of records to return</p>
            next_token: <p>Token for pagination</p>
            filters: <p>Filters to apply to the registry record list</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.list_registry_records_request.ListRegistryRecordsRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.list_registry_records_response.ListRegistryRecordsResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.list_registry_records

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.list_registry_records.list_registry_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.list_registry_records_request.ListRegistryRecordsRequest = {
            "registry_id": registry_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def submit_registry_record_for_approval(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse":
        """<p>Submits a DRAFT registry record for approval, moving it into the registry's approval workflow. Depending on the registry's approval configuration, the record is either auto-approved or set to PENDING_APPROVAL for a curator to approve or reject.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to submit for approval (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.submit_registry_record_for_approval

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.submit_registry_record_for_approval.submit_registry_record_for_approval(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_registry_record_status(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        status: "capo_agent_registry_control.types.registry_record_status.RegistryRecordStatus",
        status_reason: str,
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse":
        """<p>Updates the status of a registry record as part of the registry's curation workflow, for example to approve or reject a record that is pending approval, or to deprecate an approved record so that it is no longer discoverable</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to update the status of (ARN or ID)</p>
            status: <p>The target status for the registry record</p>
            status_reason: <p>The reason for the status change, for example why the record was approved, rejected, or deprecated</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.update_registry_record_status

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.update_registry_record_status.update_registry_record_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
            "status": status,
            "status_reason": status_reason,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRegistryRecordResource:
    def __init__(self, service: AsyncAgentRegistryControlClient) -> None:
        self._service = service

    async def create(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        name: "capo_agent_registry_control.types.registry_record_name.RegistryRecordName",
        record_type: "capo_agent_registry_control.types.record_type.RecordType",
        descriptors: "capo_agent_registry_control.types.descriptors.Descriptors",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
        display_name: Optional[
            "capo_agent_registry_control.types.registry_record_display_name.RegistryRecordDisplayName"
        ] = None,
        description: Optional[
            "capo_agent_registry_control.types.description.Description"
        ] = None,
        record_version: Optional[
            "capo_agent_registry_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        client_token: Optional[
            "capo_agent_registry_control.types.client_token.ClientToken"
        ] = None,
        provenance: Optional[
            "capo_agent_registry_control.types.provenance_list.ProvenanceList"
        ] = None,
        tags: Optional["capo_agent_registry_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_agent_registry_control.types.create_registry_record_response.CreateRegistryRecordResponse":
        """<p>Creates a registry record within a registry. A registry record describes a discoverable resource, such as an MCP server, an agent, an agent skill, or a custom resource. Creation is asynchronous: the record is returned with the CREATING status while it is processed.</p>

        Args:
            registry_id: <p>The identifier of the registry in which to create the record (ARN or ID)</p>
            name: <p>The name of the registry record</p>
            display_name: <p>The human-readable display name of the registry record</p>
            description: <p>The description of the registry record</p>
            record_type: <p>The type of the registry record, which determines the descriptor format</p>
            descriptors: <p>The typed descriptor content for the registry record</p>
            record_version: <p>The version of the registry record</p>
            client_token: <p>Client token for idempotency</p>
            tags: <p>Tags to associate with the registry record</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.create_registry_record_request.CreateRegistryRecordRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.create_registry_record_response.CreateRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.create_registry_record

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.create_registry_record.async_create_registry_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.create_registry_record_request.CreateRegistryRecordRequest = {
            "registry_id": registry_id,
            "name": name,
            "record_type": record_type,
            "descriptors": descriptors,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if record_version is not None:
            input_["record_version"] = record_version
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if provenance is not None:
            input_["provenance"] = provenance
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
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.get_registry_record_response.GetRegistryRecordResponse":
        """<p>Retrieves the details of a registry record</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to retrieve (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.get_registry_record_request.GetRegistryRecordRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.get_registry_record_response.GetRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.get_registry_record

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.get_registry_record.async_get_registry_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.get_registry_record_request.GetRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
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
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
        name: Optional[
            "capo_agent_registry_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        display_name: Optional[
            "capo_agent_registry_control.types.updated_display_name.UpdatedDisplayName"
        ] = None,
        description: Optional[
            "capo_agent_registry_control.types.updated_description.UpdatedDescription"
        ] = None,
        record_type: Optional[
            "capo_agent_registry_control.types.record_type.RecordType"
        ] = None,
        descriptors: Optional[
            "capo_agent_registry_control.types.updated_descriptors.UpdatedDescriptors"
        ] = None,
        record_version: Optional[
            "capo_agent_registry_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        trigger_synchronization: Optional[bool] = None,
        provenance: Optional[
            "capo_agent_registry_control.types.provenance_list.ProvenanceList"
        ] = None,
    ) -> "capo_agent_registry_control.types.update_registry_record_response.UpdateRegistryRecordResponse":
        """<p>Updates a registry record. The update is asynchronous: the record is returned with the UPDATING status while it is processed. Fields that use update wrappers follow PATCH semantics: omit the field to leave it unchanged.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to update (ARN or ID)</p>
            name: <p>The updated name of the registry record. Omit to leave the name unchanged.</p>
            display_name: <p>The updated display name of the registry record. Omit to leave the display name unchanged; provide an empty wrapper to unset it.</p>
            description: <p>The updated description of the registry record. Omit to leave the description unchanged; provide an empty wrapper to unset it.</p>
            record_type: <p>The updated type of the registry record. Omit to leave the record type unchanged.</p>
            descriptors: <p>The updated typed descriptor content for the registry record. Omit to leave the descriptors unchanged.</p>
            record_version: <p>The updated version of the registry record. Omit to leave the version unchanged.</p>
            trigger_synchronization: <p>Whether to trigger synchronization of the record's descriptor content from its source</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.update_registry_record_request.UpdateRegistryRecordRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.update_registry_record_response.UpdateRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.update_registry_record

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.update_registry_record.async_update_registry_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.update_registry_record_request.UpdateRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }
        if name is not None:
            input_["name"] = name
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if record_type is not None:
            input_["record_type"] = record_type
        if descriptors is not None:
            input_["descriptors"] = descriptors
        if record_version is not None:
            input_["record_version"] = record_version
        if trigger_synchronization is not None:
            input_["trigger_synchronization"] = trigger_synchronization
        if provenance is not None:
            input_["provenance"] = provenance

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.delete_registry_record_response.DeleteRegistryRecordResponse":
        """<p>Deletes a registry record</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to delete (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.delete_registry_record_request.DeleteRegistryRecordRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.delete_registry_record_response.DeleteRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.delete_registry_record

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.delete_registry_record.async_delete_registry_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.delete_registry_record_request.DeleteRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
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
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
        max_results: Optional[
            "capo_agent_registry_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_agent_registry_control.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "capo_agent_registry_control.types.registry_record_filter_list.RegistryRecordFilterList"
        ] = None,
    ) -> "capo_agent_registry_control.types.list_registry_records_response.ListRegistryRecordsResponse":
        """<p>Lists the registry records within a registry, with optional filtering by name, status, and record type</p>

        Args:
            registry_id: <p>The identifier of the registry to list records from (ARN or ID)</p>
            max_results: <p>Maximum number of records to return</p>
            next_token: <p>Token for pagination</p>
            filters: <p>Filters to apply to the registry record list</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.list_registry_records_request.ListRegistryRecordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.list_registry_records_response.ListRegistryRecordsResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.list_registry_records

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.list_registry_records.async_list_registry_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.list_registry_records_request.ListRegistryRecordsRequest = {
            "registry_id": registry_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_registry_record_for_approval(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse":
        """<p>Submits a DRAFT registry record for approval, moving it into the registry's approval workflow. Depending on the registry's approval configuration, the record is either auto-approved or set to PENDING_APPROVAL for a curator to approve or reject.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to submit for approval (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.submit_registry_record_for_approval

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.submit_registry_record_for_approval.async_submit_registry_record_for_approval(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_registry_record_status(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        status: "capo_agent_registry_control.types.registry_record_status.RegistryRecordStatus",
        status_reason: str,
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse":
        """<p>Updates the status of a registry record as part of the registry's curation workflow, for example to approve or reject a record that is pending approval, or to deprecate an approved record so that it is no longer discoverable</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to update the status of (ARN or ID)</p>
            status: <p>The target status for the registry record</p>
            status_reason: <p>The reason for the status change, for example why the record was approved, rejected, or deprecated</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.update_registry_record_status

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.update_registry_record_status.async_update_registry_record_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
            "status": status,
            "status_reason": status_reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
