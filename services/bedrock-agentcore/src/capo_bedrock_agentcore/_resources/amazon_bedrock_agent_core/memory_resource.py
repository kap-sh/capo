from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
from capo_bedrock_agentcore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.actor_id
    import capo_bedrock_agentcore.types.actor_summary
    import capo_bedrock_agentcore.types.batch_create_memory_records_input
    import capo_bedrock_agentcore.types.batch_create_memory_records_output
    import capo_bedrock_agentcore.types.batch_delete_memory_records_input
    import capo_bedrock_agentcore.types.batch_delete_memory_records_output
    import capo_bedrock_agentcore.types.batch_update_memory_records_input
    import capo_bedrock_agentcore.types.batch_update_memory_records_output
    import capo_bedrock_agentcore.types.branch
    import capo_bedrock_agentcore.types.content_source
    import capo_bedrock_agentcore.types.create_event_input
    import capo_bedrock_agentcore.types.create_event_output
    import capo_bedrock_agentcore.types.delete_event_input
    import capo_bedrock_agentcore.types.delete_event_output
    import capo_bedrock_agentcore.types.delete_memory_record_input
    import capo_bedrock_agentcore.types.delete_memory_record_output
    import capo_bedrock_agentcore.types.event
    import capo_bedrock_agentcore.types.event_id
    import capo_bedrock_agentcore.types.extraction_config
    import capo_bedrock_agentcore.types.extraction_job
    import capo_bedrock_agentcore.types.extraction_job_filter_input
    import capo_bedrock_agentcore.types.extraction_job_metadata
    import capo_bedrock_agentcore.types.extraction_mode
    import capo_bedrock_agentcore.types.filter_input
    import capo_bedrock_agentcore.types.get_event_input
    import capo_bedrock_agentcore.types.get_event_output
    import capo_bedrock_agentcore.types.get_memory_record_input
    import capo_bedrock_agentcore.types.get_memory_record_output
    import capo_bedrock_agentcore.types.ingest_data_input
    import capo_bedrock_agentcore.types.ingest_data_output
    import capo_bedrock_agentcore.types.list_actors_input
    import capo_bedrock_agentcore.types.list_actors_output
    import capo_bedrock_agentcore.types.list_events_input
    import capo_bedrock_agentcore.types.list_events_output
    import capo_bedrock_agentcore.types.list_memory_extraction_jobs_input
    import capo_bedrock_agentcore.types.list_memory_extraction_jobs_output
    import capo_bedrock_agentcore.types.list_memory_records_input
    import capo_bedrock_agentcore.types.list_memory_records_output
    import capo_bedrock_agentcore.types.list_sessions_input
    import capo_bedrock_agentcore.types.list_sessions_output
    import capo_bedrock_agentcore.types.max_results
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.memory_metadata_filter_list
    import capo_bedrock_agentcore.types.memory_record_id
    import capo_bedrock_agentcore.types.memory_record_summary
    import capo_bedrock_agentcore.types.memory_records_create_input_list
    import capo_bedrock_agentcore.types.memory_records_delete_input_list
    import capo_bedrock_agentcore.types.memory_records_update_input_list
    import capo_bedrock_agentcore.types.memory_strategy_id
    import capo_bedrock_agentcore.types.metadata_map
    import capo_bedrock_agentcore.types.namespace
    import capo_bedrock_agentcore.types.pagination_token
    import capo_bedrock_agentcore.types.payload_type_list
    import capo_bedrock_agentcore.types.retrieve_memory_records_input
    import capo_bedrock_agentcore.types.retrieve_memory_records_output
    import capo_bedrock_agentcore.types.search_criteria
    import capo_bedrock_agentcore.types.session_filter
    import capo_bedrock_agentcore.types.session_id
    import capo_bedrock_agentcore.types.session_summary
    import capo_bedrock_agentcore.types.start_memory_extraction_job_input
    import capo_bedrock_agentcore.types.start_memory_extraction_job_output
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class MemoryResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def batch_create_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        records: "capo_bedrock_agentcore.types.memory_records_create_input_list.MemoryRecordsCreateInputList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput":
        """<p>Creates multiple memory records in a single batch operation for the specified memory with custom content.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be created.</p>
            records: <p>A list of memory record creation inputs to be processed in the batch operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the batch request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records.batch_create_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.batch_create_memory_records_input

            return capo_bedrock_agentcore.types.batch_create_memory_records_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchCreateMemoryRecords", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput = {
            "memory_id": memory_id,
            "records": records,
        }
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

    def batch_delete_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        records: "capo_bedrock_agentcore.types.memory_records_delete_input_list.MemoryRecordsDeleteInputList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput":
        """<p>Deletes multiple memory records in a single batch operation from the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be deleted.</p>
            records: <p>A list of memory record deletion inputs to be processed in the batch operation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records.batch_delete_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchDeleteMemoryRecords")
        )
        input_: capo_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput = {
            "memory_id": memory_id,
            "records": records,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        records: "capo_bedrock_agentcore.types.memory_records_update_input_list.MemoryRecordsUpdateInputList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput":
        """<p>Updates multiple memory records with custom content in a single batch operation within the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be updated.</p>
            records: <p>A list of memory record update inputs to be processed in the batch operation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records.batch_update_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.batch_update_memory_records_input

            return capo_bedrock_agentcore.types.batch_update_memory_records_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchUpdateMemoryRecords", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput = {
            "memory_id": memory_id,
            "records": records,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        event_timestamp: datetime.datetime,
        payload: "capo_bedrock_agentcore.types.payload_type_list.PayloadTypeList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agentcore.types.session_id.SessionId"
        ] = None,
        branch: Optional["capo_bedrock_agentcore.types.branch.Branch"] = None,
        client_token: Optional[str] = None,
        metadata: Optional[
            "capo_bedrock_agentcore.types.metadata_map.MetadataMap"
        ] = None,
        extraction_mode: Optional[
            "capo_bedrock_agentcore.types.extraction_mode.ExtractionMode"
        ] = None,
        extraction_config: Optional[
            "capo_bedrock_agentcore.types.extraction_config.ExtractionConfig"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.create_event_output.CreateEventOutput":
        """<p>Creates an event in an AgentCore Memory resource. Events represent interactions or activities that occur within a session and are associated with specific actors.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:CreateEvent</code> permission.</p> <p>This operation is subject to request rate limiting.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource in which to create the event.</p>
            actor_id: <p>The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.</p>
            session_id: <p>The identifier of the session in which this event occurs. A session represents a sequence of related events.</p>
            event_timestamp: <p>The timestamp when the event occurred. If not specified, the current time is used.</p>
            payload: <p>The content payload of the event. This can include conversational data, JSON data, or binary content.</p>
            branch: <p>The branch information for this event. Branches allow for organizing events into different conversation threads or paths.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>
            metadata: <p>The key-value metadata to attach to the event.</p>
            extraction_mode: <p>Controls long-term memory extraction for this event. When set to <code>SKIP</code>, the event is stored in short-term memory but is excluded from long-term memory extraction. If not specified, the event is processed for extraction as usual.</p>
            extraction_config: <p>The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.create_event_input.CreateEventInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.create_event_output.CreateEventOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event.create_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.create_event_input.CreateEventInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.create_event_input

            return capo_bedrock_agentcore.types.create_event_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.create_event_output.CreateEventOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.create_event_output

            return capo_bedrock_agentcore.types.create_event_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateEvent", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore.types.create_event_input.CreateEventInput = {
            "memory_id": memory_id,
            "actor_id": actor_id,
            "event_timestamp": event_timestamp,
            "payload": payload,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if branch is not None:
            input_["branch"] = branch
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if metadata is not None:
            input_["metadata"] = metadata
        if extraction_mode is not None:
            input_["extraction_mode"] = extraction_mode
        if extraction_config is not None:
            input_["extraction_config"] = extraction_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        event_id: "capo_bedrock_agentcore.types.event_id.EventId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_event_output.DeleteEventOutput":
        """<p>Deletes an event from an AgentCore Memory resource. When you delete an event, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the event.</p>
            session_id: <p>The identifier of the session containing the event to delete.</p>
            event_id: <p>The identifier of the event to delete.</p>
            actor_id: <p>The identifier of the actor associated with the event to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_event_input.DeleteEventInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_event_output.DeleteEventOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event.delete_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEvent")
        )
        input_: capo_bedrock_agentcore.types.delete_event_input.DeleteEventInput = {
            "memory_id": memory_id,
            "session_id": session_id,
            "event_id": event_id,
            "actor_id": actor_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_memory_record(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
    ) -> "capo_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput":
        """<p>Deletes a memory record from an AgentCore Memory resource. When you delete a memory record, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to delete.</p>
            namespace: <p>The namespace of the memory record to delete. This value is used for IAM condition key authorization.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record.delete_memory_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMemoryRecord")
        )
        input_: capo_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput = {
            "memory_id": memory_id,
            "memory_record_id": memory_record_id,
        }
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        event_id: "capo_bedrock_agentcore.types.event_id.EventId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_event_output.GetEventOutput":
        """<p>Retrieves information about a specific event in an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the event.</p>
            session_id: <p>The identifier of the session containing the event.</p>
            actor_id: <p>The identifier of the actor associated with the event.</p>
            event_id: <p>The identifier of the event to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_event_input.GetEventInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_event_output.GetEventOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event.get_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_event_output.GetEventOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_event_output

            return capo_bedrock_agentcore.types.get_event_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEvent", redact_output=_redact_output)
        )
        input_: capo_bedrock_agentcore.types.get_event_input.GetEventInput = {
            "memory_id": memory_id,
            "session_id": session_id,
            "actor_id": actor_id,
            "event_id": event_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_memory_record(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
    ) -> "capo_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput":
        """<p>Retrieves a specific memory record from an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to retrieve.</p>
            namespace: <p>The namespace of the memory record to retrieve. This value is used for IAM condition key authorization.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record.get_memory_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_memory_record_output

            return (
                capo_bedrock_agentcore.types.get_memory_record_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetMemoryRecord", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput = {
            "memory_id": memory_id,
            "memory_record_id": memory_record_id,
        }
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def ingest_data(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        source: "capo_bedrock_agentcore.types.content_source.ContentSource",
        content_timestamp: datetime.datetime,
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agentcore.types.session_id.SessionId"
        ] = None,
        extraction_config: Optional[
            "capo_bedrock_agentcore.types.extraction_config.ExtractionConfig"
        ] = None,
        metadata: Optional[
            "capo_bedrock_agentcore.types.metadata_map.MetadataMap"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.ingest_data_output.IngestDataOutput":
        """<p>Submits content directly for ingestion to generate long-term memory records in a AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:IngestData</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource to ingest content into.</p>
            source: <p>The content to ingest. Only inline content is supported.</p>
            content_timestamp: <p>The timestamp of when the content occurred.</p>
            actor_id: <p>The identifier of the actor associated with this content. An actor represents an entity that participates in sessions and generates content.</p>
            session_id: <p>The identifier of the session that the content belongs to. If not provided, a session identifier is generated and returned in the response.</p>
            extraction_config: <p>The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.</p>
            metadata: <p>The key-value metadata to attach to the content.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.ingest_data_input.IngestDataInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.ingest_data_output.IngestDataOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.ingest_data

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.ingest_data.ingest_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.ingest_data_input.IngestDataInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.ingest_data_input

            return capo_bedrock_agentcore.types.ingest_data_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("IngestData", redact_input=_redact_input)
        )
        input_: capo_bedrock_agentcore.types.ingest_data_input.IngestDataInput = {
            "memory_id": memory_id,
            "source": source,
            "content_timestamp": content_timestamp,
            "actor_id": actor_id,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if extraction_config is not None:
            input_["extraction_config"] = extraction_config
        if metadata is not None:
            input_["metadata"] = metadata
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

    def list_actors(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_actors_output.ListActorsOutput":
        """<p>Lists all actors in an AgentCore Memory resource. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListActors</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list actors.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_actors_input.ListActorsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_actors_output.ListActorsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors.list_actors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListActors")
        )
        input_: capo_bedrock_agentcore.types.list_actors_input.ListActorsInput = {
            "memory_id": memory_id
        }
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

    def list_events(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        include_payloads: Optional[bool] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.filter_input.FilterInput"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_events_output.ListEventsOutput":
        """<p>Lists events in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListEvents</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list events.</p>
            session_id: <p>The identifier of the session for which to list events.</p>
            actor_id: <p>The identifier of the actor for which to list events.</p>
            include_payloads: <p>Specifies whether to include event payloads in the response. Set to true to include payloads, or false to exclude them.</p>
            filter: <p>Filter criteria to apply when listing events.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_events_input.ListEventsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_events_output.ListEventsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events.list_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.list_events_output.ListEventsOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.list_events_output

            return capo_bedrock_agentcore.types.list_events_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListEvents", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.list_events_input.ListEventsInput = {
            "memory_id": memory_id,
            "session_id": session_id,
            "actor_id": actor_id,
        }
        if include_payloads is not None:
            input_["include_payloads"] = include_payloads
        if filter is not None:
            input_["filter"] = filter
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

    def list_memory_extraction_jobs(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.extraction_job_filter_input.ExtractionJobFilterInput"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput":
        """<p>Lists all long-term memory extraction jobs that are eligible to be started with optional filtering.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryExtractionJobs</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to list extraction jobs for.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            filter: <p>Filter criteria to apply when listing extraction jobs.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs.list_memory_extraction_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMemoryExtractionJobs")
        )
        input_: capo_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput = {
            "memory_id": memory_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
        namespace_path: Optional[
            "capo_bedrock_agentcore.types.namespace.Namespace"
        ] = None,
        memory_strategy_id: Optional[
            "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        metadata_filters: Optional[
            "capo_bedrock_agentcore.types.memory_metadata_filter_list.MemoryMetadataFilterList"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput":
        """<p>Lists memory records in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Returns all memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            memory_strategy_id: <p>The memory strategy identifier to filter memory records by. If specified, only memory records with this strategy ID are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            metadata_filters: <p>A list of metadata filter expressions to scope the returned memory records.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records.list_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.list_memory_records_output

            return capo_bedrock_agentcore.types.list_memory_records_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListMemoryRecords", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput = {
            "memory_id": memory_id
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if namespace_path is not None:
            input_["namespace_path"] = namespace_path
        if memory_strategy_id is not None:
            input_["memory_strategy_id"] = memory_strategy_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if metadata_filters is not None:
            input_["metadata_filters"] = metadata_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_sessions(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.session_filter.SessionFilter"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput":
        """<p>Lists sessions in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>Empty sessions are automatically deleted after one day.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListSessions</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list sessions.</p>
            actor_id: <p>The identifier of the actor for which to list sessions. </p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filter: <p>Filter criteria to apply when listing sessions.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_sessions_input.ListSessionsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSessions")
        )
        input_: capo_bedrock_agentcore.types.list_sessions_input.ListSessionsInput = {
            "memory_id": memory_id,
            "actor_id": actor_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def retrieve_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        search_criteria: "capo_bedrock_agentcore.types.search_criteria.SearchCriteria",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
        namespace_path: Optional[
            "capo_bedrock_agentcore.types.namespace.Namespace"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput":
        """<p>Searches for and retrieves memory records from an AgentCore Memory resource based on specified search criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:RetrieveMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to retrieve memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Searches for memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            search_criteria: <p>The search criteria to use for finding relevant memory records. This includes the search query, memory strategy ID, and other search parameters.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records.retrieve_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.retrieve_memory_records_input

            return capo_bedrock_agentcore.types.retrieve_memory_records_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.retrieve_memory_records_output

            return capo_bedrock_agentcore.types.retrieve_memory_records_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "RetrieveMemoryRecords",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput = {
            "memory_id": memory_id,
            "search_criteria": search_criteria,
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if namespace_path is not None:
            input_["namespace_path"] = namespace_path
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

    def start_memory_extraction_job(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        extraction_job: "capo_bedrock_agentcore.types.extraction_job.ExtractionJob",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput":
        """<p> Starts a memory extraction job that processes events that failed extraction previously in an AgentCore Memory resource and produces structured memory records. When earlier extraction attempts have left events unprocessed, this job will pick up and extract those as well. </p> <p>To use this operation, you must have the <code>bedrock-agentcore:StartMemoryExtractionJob</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory for which to start extraction jobs.</p>
            extraction_job: <p>Extraction job to start in this operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job.start_memory_extraction_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartMemoryExtractionJob")
        )
        input_: capo_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput = {
            "memory_id": memory_id,
            "extraction_job": extraction_job,
        }
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


class AsyncMemoryResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def batch_create_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        records: "capo_bedrock_agentcore.types.memory_records_create_input_list.MemoryRecordsCreateInputList",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput":
        """<p>Creates multiple memory records in a single batch operation for the specified memory with custom content.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be created.</p>
            records: <p>A list of memory record creation inputs to be processed in the batch operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the batch request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records.async_batch_create_memory_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.batch_create_memory_records_input

            return capo_bedrock_agentcore.types.batch_create_memory_records_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchCreateMemoryRecords", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput = {
            "memory_id": memory_id,
            "records": records,
        }
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

    async def batch_delete_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        records: "capo_bedrock_agentcore.types.memory_records_delete_input_list.MemoryRecordsDeleteInputList",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput":
        """<p>Deletes multiple memory records in a single batch operation from the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be deleted.</p>
            records: <p>A list of memory record deletion inputs to be processed in the batch operation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records.async_batch_delete_memory_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchDeleteMemoryRecords")
        )
        input_: capo_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput = {
            "memory_id": memory_id,
            "records": records,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        records: "capo_bedrock_agentcore.types.memory_records_update_input_list.MemoryRecordsUpdateInputList",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput":
        """<p>Updates multiple memory records with custom content in a single batch operation within the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be updated.</p>
            records: <p>A list of memory record update inputs to be processed in the batch operation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records.async_batch_update_memory_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.batch_update_memory_records_input

            return capo_bedrock_agentcore.types.batch_update_memory_records_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchUpdateMemoryRecords", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput = {
            "memory_id": memory_id,
            "records": records,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_event(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        event_timestamp: datetime.datetime,
        payload: "capo_bedrock_agentcore.types.payload_type_list.PayloadTypeList",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agentcore.types.session_id.SessionId"
        ] = None,
        branch: Optional["capo_bedrock_agentcore.types.branch.Branch"] = None,
        client_token: Optional[str] = None,
        metadata: Optional[
            "capo_bedrock_agentcore.types.metadata_map.MetadataMap"
        ] = None,
        extraction_mode: Optional[
            "capo_bedrock_agentcore.types.extraction_mode.ExtractionMode"
        ] = None,
        extraction_config: Optional[
            "capo_bedrock_agentcore.types.extraction_config.ExtractionConfig"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.create_event_output.CreateEventOutput":
        """<p>Creates an event in an AgentCore Memory resource. Events represent interactions or activities that occur within a session and are associated with specific actors.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:CreateEvent</code> permission.</p> <p>This operation is subject to request rate limiting.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource in which to create the event.</p>
            actor_id: <p>The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.</p>
            session_id: <p>The identifier of the session in which this event occurs. A session represents a sequence of related events.</p>
            event_timestamp: <p>The timestamp when the event occurred. If not specified, the current time is used.</p>
            payload: <p>The content payload of the event. This can include conversational data, JSON data, or binary content.</p>
            branch: <p>The branch information for this event. Branches allow for organizing events into different conversation threads or paths.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>
            metadata: <p>The key-value metadata to attach to the event.</p>
            extraction_mode: <p>Controls long-term memory extraction for this event. When set to <code>SKIP</code>, the event is stored in short-term memory but is excluded from long-term memory extraction. If not specified, the event is processed for extraction as usual.</p>
            extraction_config: <p>The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.create_event_input.CreateEventInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.create_event_output.CreateEventOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event.async_create_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.create_event_input.CreateEventInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.create_event_input

            return capo_bedrock_agentcore.types.create_event_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.create_event_output.CreateEventOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.create_event_output

            return capo_bedrock_agentcore.types.create_event_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateEvent", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore.types.create_event_input.CreateEventInput = {
            "memory_id": memory_id,
            "actor_id": actor_id,
            "event_timestamp": event_timestamp,
            "payload": payload,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if branch is not None:
            input_["branch"] = branch
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if metadata is not None:
            input_["metadata"] = metadata
        if extraction_mode is not None:
            input_["extraction_mode"] = extraction_mode
        if extraction_config is not None:
            input_["extraction_config"] = extraction_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_event(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        event_id: "capo_bedrock_agentcore.types.event_id.EventId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_event_output.DeleteEventOutput":
        """<p>Deletes an event from an AgentCore Memory resource. When you delete an event, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the event.</p>
            session_id: <p>The identifier of the session containing the event to delete.</p>
            event_id: <p>The identifier of the event to delete.</p>
            actor_id: <p>The identifier of the actor associated with the event to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.delete_event_input.DeleteEventInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.delete_event_output.DeleteEventOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event.async_delete_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEvent")
        )
        input_: capo_bedrock_agentcore.types.delete_event_input.DeleteEventInput = {
            "memory_id": memory_id,
            "session_id": session_id,
            "event_id": event_id,
            "actor_id": actor_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_memory_record(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
    ) -> "capo_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput":
        """<p>Deletes a memory record from an AgentCore Memory resource. When you delete a memory record, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to delete.</p>
            namespace: <p>The namespace of the memory record to delete. This value is used for IAM condition key authorization.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record.async_delete_memory_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMemoryRecord")
        )
        input_: capo_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput = {
            "memory_id": memory_id,
            "memory_record_id": memory_record_id,
        }
        if namespace is not None:
            input_["namespace"] = namespace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_event(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        event_id: "capo_bedrock_agentcore.types.event_id.EventId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_event_output.GetEventOutput":
        """<p>Retrieves information about a specific event in an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the event.</p>
            session_id: <p>The identifier of the session containing the event.</p>
            actor_id: <p>The identifier of the actor associated with the event.</p>
            event_id: <p>The identifier of the event to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_event_input.GetEventInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_event_output.GetEventOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event.async_get_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_event_output.GetEventOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_event_output

            return capo_bedrock_agentcore.types.get_event_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEvent", redact_output=_redact_output)
        )
        input_: capo_bedrock_agentcore.types.get_event_input.GetEventInput = {
            "memory_id": memory_id,
            "session_id": session_id,
            "actor_id": actor_id,
            "event_id": event_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_memory_record(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
    ) -> "capo_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput":
        """<p>Retrieves a specific memory record from an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to retrieve.</p>
            namespace: <p>The namespace of the memory record to retrieve. This value is used for IAM condition key authorization.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record.async_get_memory_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_memory_record_output

            return (
                capo_bedrock_agentcore.types.get_memory_record_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetMemoryRecord", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput = {
            "memory_id": memory_id,
            "memory_record_id": memory_record_id,
        }
        if namespace is not None:
            input_["namespace"] = namespace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def ingest_data(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        source: "capo_bedrock_agentcore.types.content_source.ContentSource",
        content_timestamp: datetime.datetime,
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agentcore.types.session_id.SessionId"
        ] = None,
        extraction_config: Optional[
            "capo_bedrock_agentcore.types.extraction_config.ExtractionConfig"
        ] = None,
        metadata: Optional[
            "capo_bedrock_agentcore.types.metadata_map.MetadataMap"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.ingest_data_output.IngestDataOutput":
        """<p>Submits content directly for ingestion to generate long-term memory records in a AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:IngestData</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource to ingest content into.</p>
            source: <p>The content to ingest. Only inline content is supported.</p>
            content_timestamp: <p>The timestamp of when the content occurred.</p>
            actor_id: <p>The identifier of the actor associated with this content. An actor represents an entity that participates in sessions and generates content.</p>
            session_id: <p>The identifier of the session that the content belongs to. If not provided, a session identifier is generated and returned in the response.</p>
            extraction_config: <p>The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.</p>
            metadata: <p>The key-value metadata to attach to the content.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.ingest_data_input.IngestDataInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.ingest_data_output.IngestDataOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.ingest_data

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.ingest_data.async_ingest_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.ingest_data_input.IngestDataInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.ingest_data_input

            return capo_bedrock_agentcore.types.ingest_data_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("IngestData", redact_input=_redact_input)
        )
        input_: capo_bedrock_agentcore.types.ingest_data_input.IngestDataInput = {
            "memory_id": memory_id,
            "source": source,
            "content_timestamp": content_timestamp,
            "actor_id": actor_id,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if extraction_config is not None:
            input_["extraction_config"] = extraction_config
        if metadata is not None:
            input_["metadata"] = metadata
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

    async def list_actors(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_actors_output.ListActorsOutput":
        """<p>Lists all actors in an AgentCore Memory resource. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListActors</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list actors.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_actors_input.ListActorsInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_actors_output.ListActorsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors.async_list_actors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListActors")
        )
        input_: capo_bedrock_agentcore.types.list_actors_input.ListActorsInput = {
            "memory_id": memory_id
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

    async def list_events(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        include_payloads: Optional[bool] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.filter_input.FilterInput"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_events_output.ListEventsOutput":
        """<p>Lists events in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListEvents</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list events.</p>
            session_id: <p>The identifier of the session for which to list events.</p>
            actor_id: <p>The identifier of the actor for which to list events.</p>
            include_payloads: <p>Specifies whether to include event payloads in the response. Set to true to include payloads, or false to exclude them.</p>
            filter: <p>Filter criteria to apply when listing events.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_events_input.ListEventsInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_events_output.ListEventsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events.async_list_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.list_events_output.ListEventsOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.list_events_output

            return capo_bedrock_agentcore.types.list_events_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListEvents", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.list_events_input.ListEventsInput = {
            "memory_id": memory_id,
            "session_id": session_id,
            "actor_id": actor_id,
        }
        if include_payloads is not None:
            input_["include_payloads"] = include_payloads
        if filter is not None:
            input_["filter"] = filter
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

    async def list_memory_extraction_jobs(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.extraction_job_filter_input.ExtractionJobFilterInput"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput":
        """<p>Lists all long-term memory extraction jobs that are eligible to be started with optional filtering.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryExtractionJobs</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to list extraction jobs for.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            filter: <p>Filter criteria to apply when listing extraction jobs.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs.async_list_memory_extraction_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMemoryExtractionJobs")
        )
        input_: capo_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput = {
            "memory_id": memory_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
        namespace_path: Optional[
            "capo_bedrock_agentcore.types.namespace.Namespace"
        ] = None,
        memory_strategy_id: Optional[
            "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        metadata_filters: Optional[
            "capo_bedrock_agentcore.types.memory_metadata_filter_list.MemoryMetadataFilterList"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput":
        """<p>Lists memory records in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Returns all memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            memory_strategy_id: <p>The memory strategy identifier to filter memory records by. If specified, only memory records with this strategy ID are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            metadata_filters: <p>A list of metadata filter expressions to scope the returned memory records.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records.async_list_memory_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.list_memory_records_output

            return capo_bedrock_agentcore.types.list_memory_records_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListMemoryRecords", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput = {
            "memory_id": memory_id
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if namespace_path is not None:
            input_["namespace_path"] = namespace_path
        if memory_strategy_id is not None:
            input_["memory_strategy_id"] = memory_strategy_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if metadata_filters is not None:
            input_["metadata_filters"] = metadata_filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_sessions(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.session_filter.SessionFilter"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput":
        """<p>Lists sessions in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>Empty sessions are automatically deleted after one day.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListSessions</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list sessions.</p>
            actor_id: <p>The identifier of the actor for which to list sessions. </p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filter: <p>Filter criteria to apply when listing sessions.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_sessions_input.ListSessionsInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSessions")
        )
        input_: capo_bedrock_agentcore.types.list_sessions_input.ListSessionsInput = {
            "memory_id": memory_id,
            "actor_id": actor_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retrieve_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        search_criteria: "capo_bedrock_agentcore.types.search_criteria.SearchCriteria",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
        namespace_path: Optional[
            "capo_bedrock_agentcore.types.namespace.Namespace"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput":
        """<p>Searches for and retrieves memory records from an AgentCore Memory resource based on specified search criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:RetrieveMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to retrieve memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Searches for memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            search_criteria: <p>The search criteria to use for finding relevant memory records. This includes the search query, memory strategy ID, and other search parameters.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records.async_retrieve_memory_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.retrieve_memory_records_input

            return capo_bedrock_agentcore.types.retrieve_memory_records_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.retrieve_memory_records_output

            return capo_bedrock_agentcore.types.retrieve_memory_records_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "RetrieveMemoryRecords",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput = {
            "memory_id": memory_id,
            "search_criteria": search_criteria,
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if namespace_path is not None:
            input_["namespace_path"] = namespace_path
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

    async def start_memory_extraction_job(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        extraction_job: "capo_bedrock_agentcore.types.extraction_job.ExtractionJob",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput":
        """<p> Starts a memory extraction job that processes events that failed extraction previously in an AgentCore Memory resource and produces structured memory records. When earlier extraction attempts have left events unprocessed, this job will pick up and extract those as well. </p> <p>To use this operation, you must have the <code>bedrock-agentcore:StartMemoryExtractionJob</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory for which to start extraction jobs.</p>
            extraction_job: <p>Extraction job to start in this operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job.async_start_memory_extraction_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartMemoryExtractionJob")
        )
        input_: capo_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput = {
            "memory_id": memory_id,
            "extraction_job": extraction_job,
        }
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
