from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.certificates
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.code_interpreter_id
    import capo_bedrock_agentcore_control.types.code_interpreter_network_configuration
    import capo_bedrock_agentcore_control.types.code_interpreter_summary
    import capo_bedrock_agentcore_control.types.create_code_interpreter_request
    import capo_bedrock_agentcore_control.types.create_code_interpreter_response
    import capo_bedrock_agentcore_control.types.delete_code_interpreter_request
    import capo_bedrock_agentcore_control.types.delete_code_interpreter_response
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.get_code_interpreter_request
    import capo_bedrock_agentcore_control.types.get_code_interpreter_response
    import capo_bedrock_agentcore_control.types.list_code_interpreters_request
    import capo_bedrock_agentcore_control.types.list_code_interpreters_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.resource_type
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.sandbox_name
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.tools_file_system_configurations
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class CodeInterpreterResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName",
        network_configuration: "capo_bedrock_agentcore_control.types.code_interpreter_network_configuration.CodeInterpreterNetworkConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore_control.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse":
        """<p>Creates a custom code interpreter.</p>

        Args:
            name: <p>The name of the code interpreter. The name must be unique within your account.</p>
            description: <p>The description of the code interpreter.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the code interpreter to access Amazon Web Services services.</p>
            network_configuration: <p>The network configuration for the code interpreter. This configuration specifies the network mode for the code interpreter.</p>
            certificates: <p>A list of certificates to install in the code interpreter.</p>
            filesystem_configurations: <p>The file system configurations to mount into the code interpreter. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your sessions can then access your data. If you don't specify this field, no file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>
            tags: <p>A map of tag keys and values to assign to the code interpreter. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter.create_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_code_interpreter_request

            return capo_bedrock_agentcore_control.types.create_code_interpreter_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCodeInterpreter", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            input_["description"] = description
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    def read(
        self,
        code_interpreter_id: "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse":
        """<p>Gets information about a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter.get_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_code_interpreter_response

            return capo_bedrock_agentcore_control.types.get_code_interpreter_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCodeInterpreter", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest = {
            "code_interpreter_id": code_interpreter_id
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
        code_interpreter_id: "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse":
        """<p>Deletes a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter.delete_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCodeInterpreter")
        )
        input_: capo_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest = {
            "code_interpreter_id": code_interpreter_id
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

    def list(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        type: Optional[
            "capo_bedrock_agentcore_control.types.resource_type.ResourceType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse":
        """<p>Lists all custom code interpreters in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
            type: <p>The type of code interpreters to list.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters.list_code_interpreters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_code_interpreters_response

            return capo_bedrock_agentcore_control.types.list_code_interpreters_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCodeInterpreters", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCodeInterpreterResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName",
        network_configuration: "capo_bedrock_agentcore_control.types.code_interpreter_network_configuration.CodeInterpreterNetworkConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore_control.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse":
        """<p>Creates a custom code interpreter.</p>

        Args:
            name: <p>The name of the code interpreter. The name must be unique within your account.</p>
            description: <p>The description of the code interpreter.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the code interpreter to access Amazon Web Services services.</p>
            network_configuration: <p>The network configuration for the code interpreter. This configuration specifies the network mode for the code interpreter.</p>
            certificates: <p>A list of certificates to install in the code interpreter.</p>
            filesystem_configurations: <p>The file system configurations to mount into the code interpreter. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your sessions can then access your data. If you don't specify this field, no file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>
            tags: <p>A map of tag keys and values to assign to the code interpreter. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter.async_create_code_interpreter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_code_interpreter_request

            return capo_bedrock_agentcore_control.types.create_code_interpreter_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCodeInterpreter", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            input_["description"] = description
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    async def read(
        self,
        code_interpreter_id: "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse":
        """<p>Gets information about a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter.async_get_code_interpreter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_code_interpreter_response

            return capo_bedrock_agentcore_control.types.get_code_interpreter_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCodeInterpreter", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest = {
            "code_interpreter_id": code_interpreter_id
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
        code_interpreter_id: "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse":
        """<p>Deletes a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter.async_delete_code_interpreter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCodeInterpreter")
        )
        input_: capo_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest = {
            "code_interpreter_id": code_interpreter_id
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

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        type: Optional[
            "capo_bedrock_agentcore_control.types.resource_type.ResourceType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse":
        """<p>Lists all custom code interpreters in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
            type: <p>The type of code interpreters to list.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters.async_list_code_interpreters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_code_interpreters_response

            return capo_bedrock_agentcore_control.types.list_code_interpreters_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCodeInterpreters", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
