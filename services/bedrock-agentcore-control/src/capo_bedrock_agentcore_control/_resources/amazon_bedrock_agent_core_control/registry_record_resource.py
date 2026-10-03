from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.create_registry_record_request
    import capo_bedrock_agentcore_control.types.create_registry_record_response
    import capo_bedrock_agentcore_control.types.delete_registry_record_request
    import capo_bedrock_agentcore_control.types.delete_registry_record_response
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.descriptor_type
    import capo_bedrock_agentcore_control.types.descriptors
    import capo_bedrock_agentcore_control.types.get_registry_record_request
    import capo_bedrock_agentcore_control.types.get_registry_record_response
    import capo_bedrock_agentcore_control.types.list_registry_records_request
    import capo_bedrock_agentcore_control.types.list_registry_records_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.record_identifier
    import capo_bedrock_agentcore_control.types.registry_identifier
    import capo_bedrock_agentcore_control.types.registry_record_name
    import capo_bedrock_agentcore_control.types.registry_record_status
    import capo_bedrock_agentcore_control.types.registry_record_summary
    import capo_bedrock_agentcore_control.types.registry_record_version
    import capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_request
    import capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_response
    import capo_bedrock_agentcore_control.types.synchronization_configuration
    import capo_bedrock_agentcore_control.types.synchronization_type
    import capo_bedrock_agentcore_control.types.update_registry_record_request
    import capo_bedrock_agentcore_control.types.update_registry_record_response
    import capo_bedrock_agentcore_control.types.update_registry_record_status_request
    import capo_bedrock_agentcore_control.types.update_registry_record_status_response
    import capo_bedrock_agentcore_control.types.updated_description
    import capo_bedrock_agentcore_control.types.updated_descriptors
    import capo_bedrock_agentcore_control.types.updated_synchronization_configuration
    import capo_bedrock_agentcore_control.types.updated_synchronization_type
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class RegistryRecordResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        name: "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName",
        descriptor_type: "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        descriptors: Optional[
            "capo_bedrock_agentcore_control.types.descriptors.Descriptors"
        ] = None,
        record_version: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        synchronization_type: Optional[
            "capo_bedrock_agentcore_control.types.synchronization_type.SynchronizationType"
        ] = None,
        synchronization_configuration: Optional[
            "capo_bedrock_agentcore_control.types.synchronization_configuration.SynchronizationConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_registry_record_response.CreateRegistryRecordResponse":
        """<p>Creates a new registry record within the specified registry. A registry record represents an individual AI resource's metadata in the registry. This could be an MCP server (and associated tools), A2A agent, agent skill, or a custom resource with a custom schema.</p> <p>The record is processed asynchronously and returns HTTP 202 Accepted.</p>

        Args:
            registry_id: <p>The identifier of the registry where the record will be created. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            name: <p>The name of the registry record.</p>
            description: <p>A description of the registry record.</p>
            descriptor_type: <p>The descriptor type of the registry record.</p> <ul> <li> <p> <code>MCP</code> - Model Context Protocol descriptor for MCP-compatible servers and tools.</p> </li> <li> <p> <code>A2A</code> - Agent-to-Agent protocol descriptor.</p> </li> <li> <p> <code>CUSTOM</code> - Custom descriptor type for resources such as APIs, Lambda functions, or servers not conforming to a standard protocol.</p> </li> <li> <p> <code>AGENT_SKILLS</code> - Agent skills descriptor for defining agent skill definitions.</p> </li> </ul>
            descriptors: <p>The descriptor-type-specific configuration containing the resource schema and metadata. The structure of this field depends on the <code>descriptorType</code> you specify.</p>
            record_version: <p>The version of the registry record. Use this to track different versions of the record's content.</p>
            synchronization_type: <p>The type of synchronization to use for keeping the record metadata up to date from an external source. Possible values include <code>FROM_URL</code> and <code>NONE</code>.</p>
            synchronization_configuration: <p>The configuration for synchronizing registry record metadata from an external source, such as a URL-based MCP server.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_registry_record_request.CreateRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_registry_record_response.CreateRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry_record

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry_record.create_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_registry_record_request.CreateRegistryRecordRequest = {
            "registry_id": registry_id,
            "name": name,
            "descriptor_type": descriptor_type,
        }
        if description is not None:
            input_["description"] = description
        if descriptors is not None:
            input_["descriptors"] = descriptors
        if record_version is not None:
            input_["record_version"] = record_version
        if synchronization_type is not None:
            input_["synchronization_type"] = synchronization_type
        if synchronization_configuration is not None:
            input_["synchronization_configuration"] = synchronization_configuration
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
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_registry_record_response.GetRegistryRecordResponse":
        """<p>Retrieves information about a specific registry record.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to retrieve. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_registry_record_request.GetRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_registry_record_response.GetRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry_record

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry_record.get_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_registry_record_request.GetRegistryRecordRequest = {
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
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
        ] = None,
        descriptor_type: Optional[
            "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
        ] = None,
        descriptors: Optional[
            "capo_bedrock_agentcore_control.types.updated_descriptors.UpdatedDescriptors"
        ] = None,
        record_version: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        synchronization_type: Optional[
            "capo_bedrock_agentcore_control.types.updated_synchronization_type.UpdatedSynchronizationType"
        ] = None,
        synchronization_configuration: Optional[
            "capo_bedrock_agentcore_control.types.updated_synchronization_configuration.UpdatedSynchronizationConfiguration"
        ] = None,
        trigger_synchronization: Optional[bool] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_registry_record_response.UpdateRegistryRecordResponse":
        """<p>Updates an existing registry record. This operation uses PATCH semantics, so you only need to specify the fields you want to change. The update is processed asynchronously and returns HTTP 202 Accepted.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to update. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>
            name: <p>The updated name for the registry record.</p>
            description: <p>The updated description for the registry record. To clear the description, include the <code>UpdatedDescription</code> wrapper with <code>optionalValue</code> not specified.</p>
            descriptor_type: <p>The updated descriptor type for the registry record. Changing the descriptor type may require updating the <code>descriptors</code> field to match the new type's schema requirements.</p>
            descriptors: <p>The updated descriptor-type-specific configuration containing the resource schema and metadata. Uses PATCH semantics where individual descriptor fields can be updated independently.</p>
            record_version: <p>The version of the registry record for optimistic locking. If provided, it must match the current version of the record. The service automatically increments the version after a successful update.</p>
            synchronization_type: <p>The updated synchronization type for the registry record.</p>
            synchronization_configuration: <p>The updated synchronization configuration for the registry record.</p>
            trigger_synchronization: <p>Whether to trigger synchronization using the stored or provided configuration. When set to <code>true</code>, the service will synchronize the record metadata from the configured external source.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_registry_record_request.UpdateRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_registry_record_response.UpdateRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record.update_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_registry_record_request.UpdateRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if descriptor_type is not None:
            input_["descriptor_type"] = descriptor_type
        if descriptors is not None:
            input_["descriptors"] = descriptors
        if record_version is not None:
            input_["record_version"] = record_version
        if synchronization_type is not None:
            input_["synchronization_type"] = synchronization_type
        if synchronization_configuration is not None:
            input_["synchronization_configuration"] = synchronization_configuration
        if trigger_synchronization is not None:
            input_["trigger_synchronization"] = trigger_synchronization

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_registry_record_response.DeleteRegistryRecordResponse":
        """<p>Deletes a registry record. The record's status transitions to <code>DELETING</code> and the record is removed asynchronously.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to delete. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_registry_record_request.DeleteRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_registry_record_response.DeleteRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry_record

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry_record.delete_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_registry_record_request.DeleteRegistryRecordRequest = {
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
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus"
        ] = None,
        descriptor_type: Optional[
            "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_registry_records_response.ListRegistryRecordsResponse":
        """<p>Lists registry records within a registry. You can optionally filter results using the <code>name</code>, <code>status</code>, and <code>descriptorType</code> parameters. When multiple filters are specified, they are combined using AND logic.</p>

        Args:
            registry_id: <p>The identifier of the registry to list records from. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            name: <p>Filter registry records by name.</p>
            status: <p>Filter registry records by their current status. Possible values include <code>CREATING</code>, <code>DRAFT</code>, <code>APPROVED</code>, <code>PENDING_APPROVAL</code>, <code>REJECTED</code>, <code>DEPRECATED</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, and <code>UPDATE_FAILED</code>.</p>
            descriptor_type: <p>Filter registry records by their descriptor type. Possible values are <code>MCP</code>, <code>A2A</code>, <code>CUSTOM</code>, and <code>AGENT_SKILLS</code>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_registry_records_request.ListRegistryRecordsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_registry_records_response.ListRegistryRecordsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registry_records

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registry_records.list_registry_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_registry_records_request.ListRegistryRecordsRequest = {
            "registry_id": registry_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if descriptor_type is not None:
            input_["descriptor_type"] = descriptor_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def submit_registry_record_for_approval(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse":
        """<p>Submits a registry record for approval. This transitions the record from <code>DRAFT</code> status to <code>PENDING_APPROVAL</code> status. If the registry has auto-approval enabled, the record is automatically approved.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to submit for approval. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.submit_registry_record_for_approval

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.submit_registry_record_for_approval.submit_registry_record_for_approval(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest = {
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
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        status: "capo_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus",
        status_reason: str,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse":
        """<p>Updates the status of a registry record. Use this operation to approve, reject, or deprecate a registry record.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to update the status for. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>
            status: <p>The target status for the registry record.</p>
            status_reason: <p>The reason for the status change, such as why the record was approved or rejected.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record_status

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record_status.update_registry_record_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest = {
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
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        name: "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName",
        descriptor_type: "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        descriptors: Optional[
            "capo_bedrock_agentcore_control.types.descriptors.Descriptors"
        ] = None,
        record_version: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        synchronization_type: Optional[
            "capo_bedrock_agentcore_control.types.synchronization_type.SynchronizationType"
        ] = None,
        synchronization_configuration: Optional[
            "capo_bedrock_agentcore_control.types.synchronization_configuration.SynchronizationConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_registry_record_response.CreateRegistryRecordResponse":
        """<p>Creates a new registry record within the specified registry. A registry record represents an individual AI resource's metadata in the registry. This could be an MCP server (and associated tools), A2A agent, agent skill, or a custom resource with a custom schema.</p> <p>The record is processed asynchronously and returns HTTP 202 Accepted.</p>

        Args:
            registry_id: <p>The identifier of the registry where the record will be created. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            name: <p>The name of the registry record.</p>
            description: <p>A description of the registry record.</p>
            descriptor_type: <p>The descriptor type of the registry record.</p> <ul> <li> <p> <code>MCP</code> - Model Context Protocol descriptor for MCP-compatible servers and tools.</p> </li> <li> <p> <code>A2A</code> - Agent-to-Agent protocol descriptor.</p> </li> <li> <p> <code>CUSTOM</code> - Custom descriptor type for resources such as APIs, Lambda functions, or servers not conforming to a standard protocol.</p> </li> <li> <p> <code>AGENT_SKILLS</code> - Agent skills descriptor for defining agent skill definitions.</p> </li> </ul>
            descriptors: <p>The descriptor-type-specific configuration containing the resource schema and metadata. The structure of this field depends on the <code>descriptorType</code> you specify.</p>
            record_version: <p>The version of the registry record. Use this to track different versions of the record's content.</p>
            synchronization_type: <p>The type of synchronization to use for keeping the record metadata up to date from an external source. Possible values include <code>FROM_URL</code> and <code>NONE</code>.</p>
            synchronization_configuration: <p>The configuration for synchronizing registry record metadata from an external source, such as a URL-based MCP server.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_registry_record_request.CreateRegistryRecordRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_registry_record_response.CreateRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry_record

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry_record.async_create_registry_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_registry_record_request.CreateRegistryRecordRequest = {
            "registry_id": registry_id,
            "name": name,
            "descriptor_type": descriptor_type,
        }
        if description is not None:
            input_["description"] = description
        if descriptors is not None:
            input_["descriptors"] = descriptors
        if record_version is not None:
            input_["record_version"] = record_version
        if synchronization_type is not None:
            input_["synchronization_type"] = synchronization_type
        if synchronization_configuration is not None:
            input_["synchronization_configuration"] = synchronization_configuration
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
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_registry_record_response.GetRegistryRecordResponse":
        """<p>Retrieves information about a specific registry record.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to retrieve. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_registry_record_request.GetRegistryRecordRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_registry_record_response.GetRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry_record

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry_record.async_get_registry_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_registry_record_request.GetRegistryRecordRequest = {
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
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
        ] = None,
        descriptor_type: Optional[
            "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
        ] = None,
        descriptors: Optional[
            "capo_bedrock_agentcore_control.types.updated_descriptors.UpdatedDescriptors"
        ] = None,
        record_version: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        synchronization_type: Optional[
            "capo_bedrock_agentcore_control.types.updated_synchronization_type.UpdatedSynchronizationType"
        ] = None,
        synchronization_configuration: Optional[
            "capo_bedrock_agentcore_control.types.updated_synchronization_configuration.UpdatedSynchronizationConfiguration"
        ] = None,
        trigger_synchronization: Optional[bool] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_registry_record_response.UpdateRegistryRecordResponse":
        """<p>Updates an existing registry record. This operation uses PATCH semantics, so you only need to specify the fields you want to change. The update is processed asynchronously and returns HTTP 202 Accepted.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to update. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>
            name: <p>The updated name for the registry record.</p>
            description: <p>The updated description for the registry record. To clear the description, include the <code>UpdatedDescription</code> wrapper with <code>optionalValue</code> not specified.</p>
            descriptor_type: <p>The updated descriptor type for the registry record. Changing the descriptor type may require updating the <code>descriptors</code> field to match the new type's schema requirements.</p>
            descriptors: <p>The updated descriptor-type-specific configuration containing the resource schema and metadata. Uses PATCH semantics where individual descriptor fields can be updated independently.</p>
            record_version: <p>The version of the registry record for optimistic locking. If provided, it must match the current version of the record. The service automatically increments the version after a successful update.</p>
            synchronization_type: <p>The updated synchronization type for the registry record.</p>
            synchronization_configuration: <p>The updated synchronization configuration for the registry record.</p>
            trigger_synchronization: <p>Whether to trigger synchronization using the stored or provided configuration. When set to <code>true</code>, the service will synchronize the record metadata from the configured external source.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_registry_record_request.UpdateRegistryRecordRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_registry_record_response.UpdateRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record.async_update_registry_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_registry_record_request.UpdateRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if descriptor_type is not None:
            input_["descriptor_type"] = descriptor_type
        if descriptors is not None:
            input_["descriptors"] = descriptors
        if record_version is not None:
            input_["record_version"] = record_version
        if synchronization_type is not None:
            input_["synchronization_type"] = synchronization_type
        if synchronization_configuration is not None:
            input_["synchronization_configuration"] = synchronization_configuration
        if trigger_synchronization is not None:
            input_["trigger_synchronization"] = trigger_synchronization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_registry_record_response.DeleteRegistryRecordResponse":
        """<p>Deletes a registry record. The record's status transitions to <code>DELETING</code> and the record is removed asynchronously.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to delete. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_registry_record_request.DeleteRegistryRecordRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_registry_record_response.DeleteRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry_record

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry_record.async_delete_registry_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_registry_record_request.DeleteRegistryRecordRequest = {
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
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus"
        ] = None,
        descriptor_type: Optional[
            "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_registry_records_response.ListRegistryRecordsResponse":
        """<p>Lists registry records within a registry. You can optionally filter results using the <code>name</code>, <code>status</code>, and <code>descriptorType</code> parameters. When multiple filters are specified, they are combined using AND logic.</p>

        Args:
            registry_id: <p>The identifier of the registry to list records from. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            name: <p>Filter registry records by name.</p>
            status: <p>Filter registry records by their current status. Possible values include <code>CREATING</code>, <code>DRAFT</code>, <code>APPROVED</code>, <code>PENDING_APPROVAL</code>, <code>REJECTED</code>, <code>DEPRECATED</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, and <code>UPDATE_FAILED</code>.</p>
            descriptor_type: <p>Filter registry records by their descriptor type. Possible values are <code>MCP</code>, <code>A2A</code>, <code>CUSTOM</code>, and <code>AGENT_SKILLS</code>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_registry_records_request.ListRegistryRecordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_registry_records_response.ListRegistryRecordsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registry_records

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registry_records.async_list_registry_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_registry_records_request.ListRegistryRecordsRequest = {
            "registry_id": registry_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if descriptor_type is not None:
            input_["descriptor_type"] = descriptor_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_registry_record_for_approval(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse":
        """<p>Submits a registry record for approval. This transitions the record from <code>DRAFT</code> status to <code>PENDING_APPROVAL</code> status. If the registry has auto-approval enabled, the record is automatically approved.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to submit for approval. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.submit_registry_record_for_approval

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.submit_registry_record_for_approval.async_submit_registry_record_for_approval(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest = {
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
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        status: "capo_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus",
        status_reason: str,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse":
        """<p>Updates the status of a registry record. Use this operation to approve, reject, or deprecate a registry record.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to update the status for. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>
            status: <p>The target status for the registry record.</p>
            status_reason: <p>The reason for the status change, such as why the record was approved or rejected.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record_status

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record_status.async_update_registry_record_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest = {
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
