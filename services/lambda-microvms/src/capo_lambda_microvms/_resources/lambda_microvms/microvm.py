from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_lambda_microvms._auth._signers
import capo_lambda_microvms._auth._sigv4
from capo_lambda_microvms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda_microvms.types.create_microvm_auth_token_request
    import capo_lambda_microvms.types.create_microvm_auth_token_response
    import capo_lambda_microvms.types.create_microvm_shell_auth_token_request
    import capo_lambda_microvms.types.create_microvm_shell_auth_token_response
    import capo_lambda_microvms.types.get_microvm_request
    import capo_lambda_microvms.types.get_microvm_response
    import capo_lambda_microvms.types.idle_policy
    import capo_lambda_microvms.types.list_microvms_request
    import capo_lambda_microvms.types.list_microvms_response
    import capo_lambda_microvms.types.list_of_port_specification
    import capo_lambda_microvms.types.logging
    import capo_lambda_microvms.types.microvm_identifier
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.microvm_item
    import capo_lambda_microvms.types.network_connector_list
    import capo_lambda_microvms.types.positive_integer
    import capo_lambda_microvms.types.resume_microvm_request
    import capo_lambda_microvms.types.resume_microvm_response
    import capo_lambda_microvms.types.role_arn
    import capo_lambda_microvms.types.run_hook_payload
    import capo_lambda_microvms.types.run_microvm_request
    import capo_lambda_microvms.types.run_microvm_response
    import capo_lambda_microvms.types.string
    import capo_lambda_microvms.types.suspend_microvm_request
    import capo_lambda_microvms.types.suspend_microvm_response
    import capo_lambda_microvms.types.terminate_microvm_request
    import capo_lambda_microvms.types.terminate_microvm_response
    import capo_lambda_microvms.types.version
    from capo_lambda_microvms._services.async_lambda_microvms import (
        AsyncLambdaMicrovmsClient,
        AsyncLambdaMicrovmsClientConfig,
    )
    from capo_lambda_microvms._services.lambda_microvms import (
        LambdaMicrovmsClient,
        LambdaMicrovmsClientConfig,
    )


class Microvm:
    def __init__(self, service: LambdaMicrovmsClient) -> None:
        self._service = service

    def create(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
        ingress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        egress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        image_version: Optional["capo_lambda_microvms.types.version.Version"] = None,
        execution_role_arn: Optional[
            "capo_lambda_microvms.types.role_arn.RoleArn"
        ] = None,
        idle_policy: Optional[
            "capo_lambda_microvms.types.idle_policy.IdlePolicy"
        ] = None,
        logging: Optional["capo_lambda_microvms.types.logging.Logging"] = None,
        run_hook_payload: Optional[
            "capo_lambda_microvms.types.run_hook_payload.RunHookPayload"
        ] = None,
        maximum_duration_in_seconds: Optional[int] = None,
        client_token: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse":
        r"""<p>Runs a new MicroVM from the specified image. The MicroVM starts in PENDING state and transitions to RUNNING once provisioning completes. To connect, generate an authentication token using CreateMicrovmAuthToken.</p>

        Args:
            ingress_network_connectors: <p>The list of ingress network connectors to configure for the MicroVM.</p>
            egress_network_connectors: <p>The list of egress network connectors to configure for the MicroVM.</p>
            image_identifier: <p>The identifier (ARN or ID) of the MicroVM image to run.</p>
            image_version: <p>The version of the MicroVM image to run.</p>
            execution_role_arn: <p>The ARN of the IAM role to be assumed by the MicroVM during execution.</p>
            idle_policy: <p>Configuration to control auto-suspend and auto-resume behavior.</p>
            logging: <p>The logging configuration for this MicroVM instance. Specify {\"cloudWatch\": {\"logGroup\": \"...\"}} to stream application logs to a custom CloudWatch log group, or {\"disabled\": {}} to turn off logging.</p>
            run_hook_payload: <p>Per-MicroVM initialization data delivered as the request body of the /run lifecycle hook. Use to pass tenant-specific configuration such as session IDs or secret references. Maximum: 16,384 bytes.</p>
            maximum_duration_in_seconds: <p>The maximum duration in seconds that the MicroVM can exist before being terminated by the platform. Valid range: 1–28,800 (8 hours).</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is insufficient capacity to fulfill the request. Retry the request later.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota for Lambda MicroVMs.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.run_microvm_request.RunMicrovmRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.run_microvm

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.run_microvm.run_microvm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.run_microvm_request.RunMicrovmRequest = {
            "image_identifier": image_identifier
        }
        if ingress_network_connectors is not None:
            input_["ingress_network_connectors"] = ingress_network_connectors
        if egress_network_connectors is not None:
            input_["egress_network_connectors"] = egress_network_connectors
        if image_version is not None:
            input_["image_version"] = image_version
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if idle_policy is not None:
            input_["idle_policy"] = idle_policy
        if logging is not None:
            input_["logging"] = logging
        if run_hook_payload is not None:
            input_["run_hook_payload"] = run_hook_payload
        if maximum_duration_in_seconds is not None:
            input_["maximum_duration_in_seconds"] = maximum_duration_in_seconds
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
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_response.GetMicrovmResponse":
        """<p>Retrieves the details of a specific MicroVM, including its state, endpoint, image information, and configuration. The state field is eventually consistent — determine readiness by connecting to the endpoint.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.get_microvm_request.GetMicrovmRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.get_microvm_response.GetMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.get_microvm.get_microvm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_request.GetMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> (
        "capo_lambda_microvms.types.terminate_microvm_response.TerminateMicrovmResponse"
    ):
        """<p>Terminates a MicroVM. This operation is idempotent; terminating a MicroVM that has already been terminated succeeds without error.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to terminate.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.terminate_microvm_request.TerminateMicrovmRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.terminate_microvm_response.TerminateMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.terminate_microvm

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.terminate_microvm.terminate_microvm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.terminate_microvm_request.TerminateMicrovmRequest = {
            "microvm_identifier": microvm_identifier
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
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        image_identifier: Optional[
            "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
        ] = None,
        image_version: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.list_microvms_response.ListMicrovmsResponse":
        """<p>Lists MicroVMs in the account with optional filtering by image and version. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>Optional filter to list only MicroVMs running the specified image.</p>
            image_version: <p>Optional filter to list only MicroVMs running the specified image version.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.list_microvms_request.ListMicrovmsRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.list_microvms_response.ListMicrovmsResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvms

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.list_microvms.list_microvms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvms_request.ListMicrovmsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if image_identifier is not None:
            input_["image_identifier"] = image_identifier
        if image_version is not None:
            input_["image_version"] = image_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_microvm_auth_token(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        expiration_in_minutes: "capo_lambda_microvms.types.positive_integer.PositiveInteger",
        allowed_ports: "capo_lambda_microvms.types.list_of_port_specification.ListOfPortSpecification",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.create_microvm_auth_token_response.CreateMicrovmAuthTokenResponse":
        """<p>Creates an authentication token for accessing a running MicroVM. The token grants access to the specified ports on the MicroVM endpoint.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to create an authentication token for.</p>
            expiration_in_minutes: <p>The duration in minutes before the authentication token expires. Maximum: 60 minutes.</p>
            allowed_ports: <p>The list of port specifications that the authentication token grants access to on the MicroVM.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.create_microvm_auth_token_request.CreateMicrovmAuthTokenRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.create_microvm_auth_token_response.CreateMicrovmAuthTokenResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.create_microvm_auth_token

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.create_microvm_auth_token.create_microvm_auth_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.create_microvm_auth_token_request.CreateMicrovmAuthTokenRequest = {
            "microvm_identifier": microvm_identifier,
            "expiration_in_minutes": expiration_in_minutes,
            "allowed_ports": allowed_ports,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_microvm_shell_auth_token(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        expiration_in_minutes: "capo_lambda_microvms.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.create_microvm_shell_auth_token_response.CreateMicrovmShellAuthTokenResponse":
        """<p>Creates a shell authentication token for interactive shell access to a running MicroVM. The MicroVM must have been run with the SHELL_INGRESS network connector attached.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to create a shell authentication token for.</p>
            expiration_in_minutes: <p>The duration in minutes before the shell authentication token expires.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.create_microvm_shell_auth_token_request.CreateMicrovmShellAuthTokenRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.create_microvm_shell_auth_token_response.CreateMicrovmShellAuthTokenResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.create_microvm_shell_auth_token

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.create_microvm_shell_auth_token.create_microvm_shell_auth_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.create_microvm_shell_auth_token_request.CreateMicrovmShellAuthTokenRequest = {
            "microvm_identifier": microvm_identifier,
            "expiration_in_minutes": expiration_in_minutes,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def resume_microvm(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse":
        """<p>Resumes a suspended MicroVM, restoring it to RUNNING state with all state intact. The MicroVM must be in SUSPENDED state.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to resume.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.resume_microvm_request.ResumeMicrovmRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.resume_microvm

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.resume_microvm.resume_microvm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.resume_microvm_request.ResumeMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def suspend_microvm(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[LambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.suspend_microvm_response.SuspendMicrovmResponse":
        """<p>Suspends a running MicroVM, preserving its full memory and disk state. The MicroVM transitions through SUSPENDING to SUSPENDED. To restore, call ResumeMicrovm or send traffic to the endpoint if autoResumeEnabled is true.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to suspend.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_microvms.types.suspend_microvm_request.SuspendMicrovmRequest]",
        ) -> OperationResponse[
            "capo_lambda_microvms.types.suspend_microvm_response.SuspendMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.suspend_microvm

            output, http_response = (
                capo_lambda_microvms._operations.lambda_microvms.suspend_microvm.suspend_microvm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.suspend_microvm_request.SuspendMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMicrovm:
    def __init__(self, service: AsyncLambdaMicrovmsClient) -> None:
        self._service = service

    async def create(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        ingress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        egress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        image_version: Optional["capo_lambda_microvms.types.version.Version"] = None,
        execution_role_arn: Optional[
            "capo_lambda_microvms.types.role_arn.RoleArn"
        ] = None,
        idle_policy: Optional[
            "capo_lambda_microvms.types.idle_policy.IdlePolicy"
        ] = None,
        logging: Optional["capo_lambda_microvms.types.logging.Logging"] = None,
        run_hook_payload: Optional[
            "capo_lambda_microvms.types.run_hook_payload.RunHookPayload"
        ] = None,
        maximum_duration_in_seconds: Optional[int] = None,
        client_token: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse":
        r"""<p>Runs a new MicroVM from the specified image. The MicroVM starts in PENDING state and transitions to RUNNING once provisioning completes. To connect, generate an authentication token using CreateMicrovmAuthToken.</p>

        Args:
            ingress_network_connectors: <p>The list of ingress network connectors to configure for the MicroVM.</p>
            egress_network_connectors: <p>The list of egress network connectors to configure for the MicroVM.</p>
            image_identifier: <p>The identifier (ARN or ID) of the MicroVM image to run.</p>
            image_version: <p>The version of the MicroVM image to run.</p>
            execution_role_arn: <p>The ARN of the IAM role to be assumed by the MicroVM during execution.</p>
            idle_policy: <p>Configuration to control auto-suspend and auto-resume behavior.</p>
            logging: <p>The logging configuration for this MicroVM instance. Specify {\"cloudWatch\": {\"logGroup\": \"...\"}} to stream application logs to a custom CloudWatch log group, or {\"disabled\": {}} to turn off logging.</p>
            run_hook_payload: <p>Per-MicroVM initialization data delivered as the request body of the /run lifecycle hook. Use to pass tenant-specific configuration such as session IDs or secret references. Maximum: 16,384 bytes.</p>
            maximum_duration_in_seconds: <p>The maximum duration in seconds that the MicroVM can exist before being terminated by the platform. Valid range: 1–28,800 (8 hours).</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is insufficient capacity to fulfill the request. Retry the request later.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota for Lambda MicroVMs.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.run_microvm_request.RunMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.run_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.run_microvm.async_run_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.run_microvm_request.RunMicrovmRequest = {
            "image_identifier": image_identifier
        }
        if ingress_network_connectors is not None:
            input_["ingress_network_connectors"] = ingress_network_connectors
        if egress_network_connectors is not None:
            input_["egress_network_connectors"] = egress_network_connectors
        if image_version is not None:
            input_["image_version"] = image_version
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if idle_policy is not None:
            input_["idle_policy"] = idle_policy
        if logging is not None:
            input_["logging"] = logging
        if run_hook_payload is not None:
            input_["run_hook_payload"] = run_hook_payload
        if maximum_duration_in_seconds is not None:
            input_["maximum_duration_in_seconds"] = maximum_duration_in_seconds
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
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_response.GetMicrovmResponse":
        """<p>Retrieves the details of a specific MicroVM, including its state, endpoint, image information, and configuration. The state field is eventually consistent — determine readiness by connecting to the endpoint.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.get_microvm_request.GetMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.get_microvm_response.GetMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.get_microvm.async_get_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_request.GetMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> (
        "capo_lambda_microvms.types.terminate_microvm_response.TerminateMicrovmResponse"
    ):
        """<p>Terminates a MicroVM. This operation is idempotent; terminating a MicroVM that has already been terminated succeeds without error.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to terminate.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.terminate_microvm_request.TerminateMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.terminate_microvm_response.TerminateMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.terminate_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.terminate_microvm.async_terminate_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.terminate_microvm_request.TerminateMicrovmRequest = {
            "microvm_identifier": microvm_identifier
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
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        image_identifier: Optional[
            "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
        ] = None,
        image_version: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.list_microvms_response.ListMicrovmsResponse":
        """<p>Lists MicroVMs in the account with optional filtering by image and version. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>Optional filter to list only MicroVMs running the specified image.</p>
            image_version: <p>Optional filter to list only MicroVMs running the specified image version.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_microvms_request.ListMicrovmsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_microvms_response.ListMicrovmsResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvms

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_microvms.async_list_microvms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvms_request.ListMicrovmsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if image_identifier is not None:
            input_["image_identifier"] = image_identifier
        if image_version is not None:
            input_["image_version"] = image_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_microvm_auth_token(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        expiration_in_minutes: "capo_lambda_microvms.types.positive_integer.PositiveInteger",
        allowed_ports: "capo_lambda_microvms.types.list_of_port_specification.ListOfPortSpecification",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.create_microvm_auth_token_response.CreateMicrovmAuthTokenResponse":
        """<p>Creates an authentication token for accessing a running MicroVM. The token grants access to the specified ports on the MicroVM endpoint.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to create an authentication token for.</p>
            expiration_in_minutes: <p>The duration in minutes before the authentication token expires. Maximum: 60 minutes.</p>
            allowed_ports: <p>The list of port specifications that the authentication token grants access to on the MicroVM.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.create_microvm_auth_token_request.CreateMicrovmAuthTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.create_microvm_auth_token_response.CreateMicrovmAuthTokenResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.create_microvm_auth_token

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.create_microvm_auth_token.async_create_microvm_auth_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.create_microvm_auth_token_request.CreateMicrovmAuthTokenRequest = {
            "microvm_identifier": microvm_identifier,
            "expiration_in_minutes": expiration_in_minutes,
            "allowed_ports": allowed_ports,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_microvm_shell_auth_token(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        expiration_in_minutes: "capo_lambda_microvms.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.create_microvm_shell_auth_token_response.CreateMicrovmShellAuthTokenResponse":
        """<p>Creates a shell authentication token for interactive shell access to a running MicroVM. The MicroVM must have been run with the SHELL_INGRESS network connector attached.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to create a shell authentication token for.</p>
            expiration_in_minutes: <p>The duration in minutes before the shell authentication token expires.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.create_microvm_shell_auth_token_request.CreateMicrovmShellAuthTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.create_microvm_shell_auth_token_response.CreateMicrovmShellAuthTokenResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.create_microvm_shell_auth_token

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.create_microvm_shell_auth_token.async_create_microvm_shell_auth_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.create_microvm_shell_auth_token_request.CreateMicrovmShellAuthTokenRequest = {
            "microvm_identifier": microvm_identifier,
            "expiration_in_minutes": expiration_in_minutes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resume_microvm(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse":
        """<p>Resumes a suspended MicroVM, restoring it to RUNNING state with all state intact. The MicroVM must be in SUSPENDED state.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to resume.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.resume_microvm_request.ResumeMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.resume_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.resume_microvm.async_resume_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.resume_microvm_request.ResumeMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def suspend_microvm(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.suspend_microvm_response.SuspendMicrovmResponse":
        """<p>Suspends a running MicroVM, preserving its full memory and disk state. The MicroVM transitions through SUSPENDING to SUSPENDED. To restore, call ResumeMicrovm or send traffic to the endpoint if autoResumeEnabled is true.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to suspend.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.suspend_microvm_request.SuspendMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.suspend_microvm_response.SuspendMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.suspend_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.suspend_microvm.async_suspend_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.suspend_microvm_request.SuspendMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
