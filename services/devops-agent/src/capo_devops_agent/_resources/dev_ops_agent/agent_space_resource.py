from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_devops_agent._auth._signers
import capo_devops_agent._auth._sigv4
from capo_devops_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.agent_space_name
    import capo_devops_agent.types.agent_space_preferences
    import capo_devops_agent.types.auth_flow
    import capo_devops_agent.types.create_agent_space_input
    import capo_devops_agent.types.create_agent_space_output
    import capo_devops_agent.types.delete_agent_space_input
    import capo_devops_agent.types.delete_agent_space_output
    import capo_devops_agent.types.description
    import capo_devops_agent.types.disable_operator_app_input
    import capo_devops_agent.types.enable_operator_app_input
    import capo_devops_agent.types.enable_operator_app_output
    import capo_devops_agent.types.get_agent_space_input
    import capo_devops_agent.types.get_agent_space_output
    import capo_devops_agent.types.get_operator_app_input
    import capo_devops_agent.types.get_operator_app_output
    import capo_devops_agent.types.idp_client_id
    import capo_devops_agent.types.idp_client_secret
    import capo_devops_agent.types.kms_key_arn
    import capo_devops_agent.types.list_agent_spaces_input
    import capo_devops_agent.types.list_agent_spaces_output
    import capo_devops_agent.types.locale
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.role_arn
    import capo_devops_agent.types.tags
    import capo_devops_agent.types.update_agent_space_input
    import capo_devops_agent.types.update_agent_space_output
    import capo_devops_agent.types.update_operator_app_idp_config_input
    import capo_devops_agent.types.update_operator_app_idp_config_output
    from capo_devops_agent._services.async_dev_ops_agent import (
        AsyncDevOpsAgentClient,
        AsyncDevOpsAgentClientConfig,
    )
    from capo_devops_agent._services.dev_ops_agent import (
        DevOpsAgentClient,
        DevOpsAgentClientConfig,
    )


class AgentSpaceResource:
    def __init__(self, service: DevOpsAgentClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_devops_agent.types.agent_space_name.AgentSpaceName",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        description: Optional["capo_devops_agent.types.description.Description"] = None,
        locale: Optional["capo_devops_agent.types.locale.Locale"] = None,
        kms_key_arn: Optional["capo_devops_agent.types.kms_key_arn.KmsKeyArn"] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_devops_agent.types.tags.Tags"] = None,
        preferences: Optional[
            "capo_devops_agent.types.agent_space_preferences.AgentSpacePreferences"
        ] = None,
    ) -> "capo_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput":
        """<p>Creates a new AgentSpace with the specified name and description. Duplicate space names are allowed.</p>

        Args:
            name: <p>The name of the AgentSpace.</p>
            description: <p>The description of the AgentSpace.</p>
            locale: <p>The locale for the AgentSpace, which determines the language used in agent responses.</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            client_token: <p>Client-provided token to ensure request idempotency. When the same token is provided in subsequent calls, the same response is returned within a 8-hour window.</p>
            tags: <p>Tags to add to the AgentSpace at creation time.</p>
            preferences: <p>The preferences to configure on the agent space. Preferences not provided take their default values.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_agent_space

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.create_agent_space.create_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.create_agent_space_input

            return capo_devops_agent.types.create_agent_space_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.create_agent_space_output

            return capo_devops_agent.types.create_agent_space_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAgentSpace",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if preferences is not None:
            input_["preferences"] = preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput":
        """<p>Retrieves detailed information about a specific AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.get_agent_space_input.GetAgentSpaceInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_agent_space

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.get_agent_space.get_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.get_agent_space_output

            return capo_devops_agent.types.get_agent_space_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentSpace", redact_output=_redact_output),
        )
        input_: capo_devops_agent.types.get_agent_space_input.GetAgentSpaceInput = {
            "agent_space_id": agent_space_id
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
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        name: Optional[
            "capo_devops_agent.types.agent_space_name.AgentSpaceName"
        ] = None,
        description: Optional["capo_devops_agent.types.description.Description"] = None,
        locale: Optional["capo_devops_agent.types.locale.Locale"] = None,
        preferences: Optional[
            "capo_devops_agent.types.agent_space_preferences.AgentSpacePreferences"
        ] = None,
    ) -> "capo_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput":
        """<p>Updates the information of an existing AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            name: <p>The updated name of the AgentSpace.</p>
            description: <p>The updated description of the AgentSpace.</p>
            locale: <p>The updated locale for the AgentSpace, which determines the language used in agent responses.</p>
            preferences: <p>The preferences to configure on the agent space. When provided, this replaces the full set of configured preferences; preferences not included revert to their default values. When omitted, the current preferences are left unchanged.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_agent_space

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.update_agent_space.update_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.update_agent_space_input

            return capo_devops_agent.types.update_agent_space_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.update_agent_space_output

            return capo_devops_agent.types.update_agent_space_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAgentSpace",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput = {
            "agent_space_id": agent_space_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale
        if preferences is not None:
            input_["preferences"] = preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput":
        """<p>Deletes an AgentSpace. This operation is idempotent and returns a 204 No Content response on success.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.delete_agent_space

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.delete_agent_space.delete_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAgentSpace")
        )
        input_: capo_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput = {
            "agent_space_id": agent_space_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_operator_app(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        auth_flow: Optional["capo_devops_agent.types.auth_flow.AuthFlow"] = None,
    ) -> None:
        """<p>Disable the Operator App for the specified AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. idc</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.identity_center_service_exception.IdentityCenterServiceException: <p>Calls to the customer Identity Center have failed</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput]",
        ) -> OperationResponse[None]:
            import capo_devops_agent._operations.dev_ops_agent.disable_operator_app

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.disable_operator_app.disable_operator_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisableOperatorApp")
        )
        input_: capo_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput = {
            "agent_space_id": agent_space_id
        }
        if auth_flow is not None:
            input_["auth_flow"] = auth_flow

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_operator_app(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        auth_flow: "capo_devops_agent.types.auth_flow.AuthFlow",
        operator_app_role_arn: "capo_devops_agent.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        idc_instance_arn: Optional[str] = None,
        issuer_url: Optional[str] = None,
        idp_client_id: Optional[
            "capo_devops_agent.types.idp_client_id.IdpClientId"
        ] = None,
        idp_client_secret: Optional[
            "capo_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
        provider: Optional[str] = None,
    ) -> "capo_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput":
        """<p>Enable the Operator App to access the given AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. iam or idc</p>
            operator_app_role_arn: <p>The IAM role end users assume to access AIDevOps APIs</p>
            idc_instance_arn: <p>The IdC instance Arn used to create an IdC auth application</p>
            issuer_url: <p>The OIDC issuer URL of the external Identity Provider</p>
            idp_client_id: <p>The OIDC client ID for the IdP application</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>
            provider: <p>The Identity Provider name (e.g., Entra, Okta, Google)</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.identity_center_service_exception.IdentityCenterServiceException: <p>Calls to the customer Identity Center have failed</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.enable_operator_app

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.enable_operator_app.enable_operator_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.enable_operator_app_input

            return capo_devops_agent.types.enable_operator_app_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("EnableOperatorApp", redact_input=_redact_input),
        )
        input_: capo_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput = {
            "agent_space_id": agent_space_id,
            "auth_flow": auth_flow,
            "operator_app_role_arn": operator_app_role_arn,
        }
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if issuer_url is not None:
            input_["issuer_url"] = issuer_url
        if idp_client_id is not None:
            input_["idp_client_id"] = idp_client_id
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret
        if provider is not None:
            input_["provider"] = provider

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_operator_app(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_operator_app_output.GetOperatorAppOutput":
        """<p>Get the full auth configuration of operator including any enabled auth flow</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.get_operator_app_input.GetOperatorAppInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.get_operator_app_output.GetOperatorAppOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_operator_app

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.get_operator_app.get_operator_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetOperatorApp")
        )
        input_: capo_devops_agent.types.get_operator_app_input.GetOperatorAppInput = {
            "agent_space_id": agent_space_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_operator_app_idp_config(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        idp_client_secret: Optional[
            "capo_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
    ) -> "capo_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput":
        """<p>Update the external Identity Provider configuration for the Operator App</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config.update_operator_app_idp_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.update_operator_app_idp_config_input

            return capo_devops_agent.types.update_operator_app_idp_config_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateOperatorAppIdpConfig", redact_input=_redact_input),
        )
        input_: capo_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput = {
            "agent_space_id": agent_space_id
        }
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_spaces(
        self,
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "capo_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput":
        """<p>Lists all AgentSpaces with optional pagination.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_agent_spaces

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.list_agent_spaces.list_agent_spaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.list_agent_spaces_output

            return capo_devops_agent.types.list_agent_spaces_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentSpaces", redact_output=_redact_output),
        )
        input_: capo_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput = {}
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


class AsyncAgentSpaceResource:
    def __init__(self, service: AsyncDevOpsAgentClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_devops_agent.types.agent_space_name.AgentSpaceName",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        description: Optional["capo_devops_agent.types.description.Description"] = None,
        locale: Optional["capo_devops_agent.types.locale.Locale"] = None,
        kms_key_arn: Optional["capo_devops_agent.types.kms_key_arn.KmsKeyArn"] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_devops_agent.types.tags.Tags"] = None,
        preferences: Optional[
            "capo_devops_agent.types.agent_space_preferences.AgentSpacePreferences"
        ] = None,
    ) -> "capo_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput":
        """<p>Creates a new AgentSpace with the specified name and description. Duplicate space names are allowed.</p>

        Args:
            name: <p>The name of the AgentSpace.</p>
            description: <p>The description of the AgentSpace.</p>
            locale: <p>The locale for the AgentSpace, which determines the language used in agent responses.</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            client_token: <p>Client-provided token to ensure request idempotency. When the same token is provided in subsequent calls, the same response is returned within a 8-hour window.</p>
            tags: <p>Tags to add to the AgentSpace at creation time.</p>
            preferences: <p>The preferences to configure on the agent space. Preferences not provided take their default values.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_agent_space

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.create_agent_space.async_create_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.create_agent_space_input

            return capo_devops_agent.types.create_agent_space_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.create_agent_space_output

            return capo_devops_agent.types.create_agent_space_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAgentSpace",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if preferences is not None:
            input_["preferences"] = preferences

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput":
        """<p>Retrieves detailed information about a specific AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_agent_space_input.GetAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_agent_space

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_agent_space.async_get_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.get_agent_space_output

            return capo_devops_agent.types.get_agent_space_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentSpace", redact_output=_redact_output),
        )
        input_: capo_devops_agent.types.get_agent_space_input.GetAgentSpaceInput = {
            "agent_space_id": agent_space_id
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
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        name: Optional[
            "capo_devops_agent.types.agent_space_name.AgentSpaceName"
        ] = None,
        description: Optional["capo_devops_agent.types.description.Description"] = None,
        locale: Optional["capo_devops_agent.types.locale.Locale"] = None,
        preferences: Optional[
            "capo_devops_agent.types.agent_space_preferences.AgentSpacePreferences"
        ] = None,
    ) -> "capo_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput":
        """<p>Updates the information of an existing AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            name: <p>The updated name of the AgentSpace.</p>
            description: <p>The updated description of the AgentSpace.</p>
            locale: <p>The updated locale for the AgentSpace, which determines the language used in agent responses.</p>
            preferences: <p>The preferences to configure on the agent space. When provided, this replaces the full set of configured preferences; preferences not included revert to their default values. When omitted, the current preferences are left unchanged.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_agent_space

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_agent_space.async_update_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.update_agent_space_input

            return capo_devops_agent.types.update_agent_space_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.update_agent_space_output

            return capo_devops_agent.types.update_agent_space_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAgentSpace",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput = {
            "agent_space_id": agent_space_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale
        if preferences is not None:
            input_["preferences"] = preferences

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput":
        """<p>Deletes an AgentSpace. This operation is idempotent and returns a 204 No Content response on success.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.delete_agent_space

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.delete_agent_space.async_delete_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAgentSpace")
        )
        input_: capo_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput = {
            "agent_space_id": agent_space_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_operator_app(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        auth_flow: Optional["capo_devops_agent.types.auth_flow.AuthFlow"] = None,
    ) -> None:
        """<p>Disable the Operator App for the specified AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. idc</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.identity_center_service_exception.IdentityCenterServiceException: <p>Calls to the customer Identity Center have failed</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_devops_agent._operations.dev_ops_agent.disable_operator_app

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.disable_operator_app.async_disable_operator_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisableOperatorApp")
        )
        input_: capo_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput = {
            "agent_space_id": agent_space_id
        }
        if auth_flow is not None:
            input_["auth_flow"] = auth_flow

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_operator_app(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        auth_flow: "capo_devops_agent.types.auth_flow.AuthFlow",
        operator_app_role_arn: "capo_devops_agent.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        idc_instance_arn: Optional[str] = None,
        issuer_url: Optional[str] = None,
        idp_client_id: Optional[
            "capo_devops_agent.types.idp_client_id.IdpClientId"
        ] = None,
        idp_client_secret: Optional[
            "capo_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
        provider: Optional[str] = None,
    ) -> "capo_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput":
        """<p>Enable the Operator App to access the given AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. iam or idc</p>
            operator_app_role_arn: <p>The IAM role end users assume to access AIDevOps APIs</p>
            idc_instance_arn: <p>The IdC instance Arn used to create an IdC auth application</p>
            issuer_url: <p>The OIDC issuer URL of the external Identity Provider</p>
            idp_client_id: <p>The OIDC client ID for the IdP application</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>
            provider: <p>The Identity Provider name (e.g., Entra, Okta, Google)</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.identity_center_service_exception.IdentityCenterServiceException: <p>Calls to the customer Identity Center have failed</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.enable_operator_app

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.enable_operator_app.async_enable_operator_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.enable_operator_app_input

            return capo_devops_agent.types.enable_operator_app_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("EnableOperatorApp", redact_input=_redact_input),
        )
        input_: capo_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput = {
            "agent_space_id": agent_space_id,
            "auth_flow": auth_flow,
            "operator_app_role_arn": operator_app_role_arn,
        }
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if issuer_url is not None:
            input_["issuer_url"] = issuer_url
        if idp_client_id is not None:
            input_["idp_client_id"] = idp_client_id
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret
        if provider is not None:
            input_["provider"] = provider

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_operator_app(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_operator_app_output.GetOperatorAppOutput":
        """<p>Get the full auth configuration of operator including any enabled auth flow</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_operator_app_input.GetOperatorAppInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_operator_app_output.GetOperatorAppOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_operator_app

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_operator_app.async_get_operator_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetOperatorApp")
        )
        input_: capo_devops_agent.types.get_operator_app_input.GetOperatorAppInput = {
            "agent_space_id": agent_space_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_operator_app_idp_config(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        idp_client_secret: Optional[
            "capo_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
    ) -> "capo_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput":
        """<p>Update the external Identity Provider configuration for the Operator App</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config.async_update_operator_app_idp_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.update_operator_app_idp_config_input

            return capo_devops_agent.types.update_operator_app_idp_config_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateOperatorAppIdpConfig", redact_input=_redact_input),
        )
        input_: capo_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput = {
            "agent_space_id": agent_space_id
        }
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agent_spaces(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "capo_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput":
        """<p>Lists all AgentSpaces with optional pagination.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_agent_spaces

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_agent_spaces.async_list_agent_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput",
        ) -> dict[str, Any]:
            import capo_devops_agent.types.list_agent_spaces_output

            return capo_devops_agent.types.list_agent_spaces_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentSpaces", redact_output=_redact_output),
        )
        input_: capo_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput = {}
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
