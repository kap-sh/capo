from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_drs._auth._signers
import capo_drs._auth._sigv4
from capo_drs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_drs.types.client_idempotency_token
    import capo_drs.types.create_recovery_plan_request
    import capo_drs.types.create_recovery_plan_response
    import capo_drs.types.recovery_plan_description
    import capo_drs.types.recovery_plan_execution_mode
    import capo_drs.types.recovery_plan_execution_source_server_list
    import capo_drs.types.recovery_plan_name
    import capo_drs.types.start_recovery_plan_execution_request
    import capo_drs.types.start_recovery_plan_execution_response
    import capo_drs.types.strict_drsarn
    import capo_drs.types.tags_map
    from capo_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from capo_drs._services.drs import drsClient, drsClientConfig


class RecoveryPlanResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_drs.types.recovery_plan_name.RecoveryPlanName",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        description: Optional[
            "capo_drs.types.recovery_plan_description.RecoveryPlanDescription"
        ] = None,
        client_token: Optional[
            "capo_drs.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.create_recovery_plan_response.CreateRecoveryPlanResponse":
        """<p>Creates a Recovery Plan to orchestrate multi-server disaster recovery.</p>

        Args:
            client_token: <p>A unique string provided to ensure request idempotency.</p>
            tags: <p>The tags to apply to the Recovery Plan.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.create_recovery_plan_request.CreateRecoveryPlanRequest]",
        ) -> OperationResponse[
            "capo_drs.types.create_recovery_plan_response.CreateRecoveryPlanResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_recovery_plan

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.create_recovery_plan.create_recovery_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.create_recovery_plan_request.CreateRecoveryPlanRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.create_recovery_plan_request

            return capo_drs.types.create_recovery_plan_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_drs.types.create_recovery_plan_response.CreateRecoveryPlanResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.create_recovery_plan_response

            return capo_drs.types.create_recovery_plan_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRecoveryPlan",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.create_recovery_plan_request.CreateRecoveryPlanRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_recovery_plan_execution(
        self,
        recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN",
        mode: "capo_drs.types.recovery_plan_execution_mode.RecoveryPlanExecutionMode",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        client_token: Optional[
            "capo_drs.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        source_servers: Optional[
            "capo_drs.types.recovery_plan_execution_source_server_list.RecoveryPlanExecutionSourceServerList"
        ] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_recovery_plan_execution_response.StartRecoveryPlanExecutionResponse":
        """<p>Starts executing a Recovery Plan in <code>DRILL</code> or <code>RECOVERY</code> mode. A plan cannot have more than one execution in a non-terminal status at a time.</p>

        Args:
            recovery_plan_arn: <p>The ARN of the Recovery Plan to execute.</p>
            mode: <p>The execution mode (<code>DRILL</code> or <code>RECOVERY</code>).</p>
            client_token: <p>A unique string provided to ensure request idempotency.</p>
            source_servers: <p>Optional list of source servers with specific recovery snapshots. If not provided, the latest snapshot is used for each server.</p>
            tags: <p>The tags to apply to the Recovery Plan execution.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.start_recovery_plan_execution_request.StartRecoveryPlanExecutionRequest]",
        ) -> OperationResponse[
            "capo_drs.types.start_recovery_plan_execution_response.StartRecoveryPlanExecutionResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_recovery_plan_execution

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.start_recovery_plan_execution.start_recovery_plan_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.start_recovery_plan_execution_request.StartRecoveryPlanExecutionRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.start_recovery_plan_execution_request

            return (
                capo_drs.types.start_recovery_plan_execution_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_drs.types.start_recovery_plan_execution_response.StartRecoveryPlanExecutionResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_recovery_plan_execution_response

            return (
                capo_drs.types.start_recovery_plan_execution_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartRecoveryPlanExecution",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.start_recovery_plan_execution_request.StartRecoveryPlanExecutionRequest = {
            "recovery_plan_arn": recovery_plan_arn,
            "mode": mode,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if source_servers is not None:
            input_["source_servers"] = source_servers
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRecoveryPlanResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_drs.types.recovery_plan_name.RecoveryPlanName",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        description: Optional[
            "capo_drs.types.recovery_plan_description.RecoveryPlanDescription"
        ] = None,
        client_token: Optional[
            "capo_drs.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.create_recovery_plan_response.CreateRecoveryPlanResponse":
        """<p>Creates a Recovery Plan to orchestrate multi-server disaster recovery.</p>

        Args:
            client_token: <p>A unique string provided to ensure request idempotency.</p>
            tags: <p>The tags to apply to the Recovery Plan.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.create_recovery_plan_request.CreateRecoveryPlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.create_recovery_plan_response.CreateRecoveryPlanResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_recovery_plan

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.create_recovery_plan.async_create_recovery_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.create_recovery_plan_request.CreateRecoveryPlanRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.create_recovery_plan_request

            return capo_drs.types.create_recovery_plan_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_drs.types.create_recovery_plan_response.CreateRecoveryPlanResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.create_recovery_plan_response

            return capo_drs.types.create_recovery_plan_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRecoveryPlan",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.create_recovery_plan_request.CreateRecoveryPlanRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_recovery_plan_execution(
        self,
        recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN",
        mode: "capo_drs.types.recovery_plan_execution_mode.RecoveryPlanExecutionMode",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        client_token: Optional[
            "capo_drs.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        source_servers: Optional[
            "capo_drs.types.recovery_plan_execution_source_server_list.RecoveryPlanExecutionSourceServerList"
        ] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_recovery_plan_execution_response.StartRecoveryPlanExecutionResponse":
        """<p>Starts executing a Recovery Plan in <code>DRILL</code> or <code>RECOVERY</code> mode. A plan cannot have more than one execution in a non-terminal status at a time.</p>

        Args:
            recovery_plan_arn: <p>The ARN of the Recovery Plan to execute.</p>
            mode: <p>The execution mode (<code>DRILL</code> or <code>RECOVERY</code>).</p>
            client_token: <p>A unique string provided to ensure request idempotency.</p>
            source_servers: <p>Optional list of source servers with specific recovery snapshots. If not provided, the latest snapshot is used for each server.</p>
            tags: <p>The tags to apply to the Recovery Plan execution.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_recovery_plan_execution_request.StartRecoveryPlanExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_recovery_plan_execution_response.StartRecoveryPlanExecutionResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_recovery_plan_execution

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_recovery_plan_execution.async_start_recovery_plan_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.start_recovery_plan_execution_request.StartRecoveryPlanExecutionRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.start_recovery_plan_execution_request

            return (
                capo_drs.types.start_recovery_plan_execution_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_drs.types.start_recovery_plan_execution_response.StartRecoveryPlanExecutionResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_recovery_plan_execution_response

            return (
                capo_drs.types.start_recovery_plan_execution_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartRecoveryPlanExecution",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.start_recovery_plan_execution_request.StartRecoveryPlanExecutionRequest = {
            "recovery_plan_arn": recovery_plan_arn,
            "mode": mode,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if source_servers is not None:
            input_["source_servers"] = source_servers
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
