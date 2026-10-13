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
    import capo_bedrock_agentcore_control.types.browser_enterprise_policies
    import capo_bedrock_agentcore_control.types.browser_id
    import capo_bedrock_agentcore_control.types.browser_network_configuration
    import capo_bedrock_agentcore_control.types.browser_signing_config_input
    import capo_bedrock_agentcore_control.types.browser_summary
    import capo_bedrock_agentcore_control.types.certificates
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.create_browser_request
    import capo_bedrock_agentcore_control.types.create_browser_response
    import capo_bedrock_agentcore_control.types.delete_browser_request
    import capo_bedrock_agentcore_control.types.delete_browser_response
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.get_browser_request
    import capo_bedrock_agentcore_control.types.get_browser_response
    import capo_bedrock_agentcore_control.types.list_browsers_request
    import capo_bedrock_agentcore_control.types.list_browsers_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.recording_config
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


class BrowserResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName",
        network_configuration: "capo_bedrock_agentcore_control.types.browser_network_configuration.BrowserNetworkConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        recording: Optional[
            "capo_bedrock_agentcore_control.types.recording_config.RecordingConfig"
        ] = None,
        browser_signing: Optional[
            "capo_bedrock_agentcore_control.types.browser_signing_config_input.BrowserSigningConfigInput"
        ] = None,
        enterprise_policies: Optional[
            "capo_bedrock_agentcore_control.types.browser_enterprise_policies.BrowserEnterprisePolicies"
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
    ) -> "capo_bedrock_agentcore_control.types.create_browser_response.CreateBrowserResponse":
        """<p>Creates a custom browser.</p>

        Args:
            name: <p>The name of the browser. The name must be unique within your account.</p>
            description: <p>The description of the browser.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the browser to access Amazon Web Services services.</p>
            network_configuration: <p>The network configuration for the browser. This configuration specifies the network mode for the browser.</p>
            recording: <p>The recording configuration for the browser. When enabled, browser sessions are recorded and stored in the specified Amazon S3 location.</p>
            browser_signing: <p>The browser signing configuration that enables cryptographic agent identification using HTTP message signatures for web bot authentication.</p>
            enterprise_policies: <p>A list of enterprise policy files for the browser.</p>
            certificates: <p>A list of certificates to install in the browser.</p>
            filesystem_configurations: <p>The file system configurations to mount into the browser. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your sessions can then access your data. If you don't specify this field, no file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>
            tags: <p>A map of tag keys and values to assign to the browser. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_browser_request.CreateBrowserRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_browser_response.CreateBrowserResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_browser

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_browser.create_browser(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_browser_request.CreateBrowserRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_browser_request

            return capo_bedrock_agentcore_control.types.create_browser_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateBrowser", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.create_browser_request.CreateBrowserRequest = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            input_["description"] = description
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if recording is not None:
            input_["recording"] = recording
        if browser_signing is not None:
            input_["browser_signing"] = browser_signing
        if enterprise_policies is not None:
            input_["enterprise_policies"] = enterprise_policies
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
        browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_browser_response.GetBrowserResponse":
        """<p>Gets information about a custom browser.</p>

        Args:
            browser_id: <p>The unique identifier of the browser to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_browser_request.GetBrowserRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_browser_response.GetBrowserResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_browser

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_browser.get_browser(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_browser_response.GetBrowserResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_browser_response

            return capo_bedrock_agentcore_control.types.get_browser_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetBrowser", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_browser_request.GetBrowserRequest = {
            "browser_id": browser_id
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
        browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_browser_response.DeleteBrowserResponse":
        """<p>Deletes a custom browser.</p>

        Args:
            browser_id: <p>The unique identifier of the browser to delete.</p>
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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_browser_request.DeleteBrowserRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_browser_response.DeleteBrowserResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_browser

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_browser.delete_browser(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBrowser")
        )
        input_: capo_bedrock_agentcore_control.types.delete_browser_request.DeleteBrowserRequest = {
            "browser_id": browser_id
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
    ) -> "capo_bedrock_agentcore_control.types.list_browsers_response.ListBrowsersResponse":
        """<p>Lists all custom browsers in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            type: <p>The type of browsers to list. If not specified, all browser types are returned.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_browsers_request.ListBrowsersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_browsers_response.ListBrowsersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_browsers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_browsers.list_browsers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_browsers_response.ListBrowsersResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_browsers_response

            return capo_bedrock_agentcore_control.types.list_browsers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListBrowsers", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_browsers_request.ListBrowsersRequest = {}
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


class AsyncBrowserResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName",
        network_configuration: "capo_bedrock_agentcore_control.types.browser_network_configuration.BrowserNetworkConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        recording: Optional[
            "capo_bedrock_agentcore_control.types.recording_config.RecordingConfig"
        ] = None,
        browser_signing: Optional[
            "capo_bedrock_agentcore_control.types.browser_signing_config_input.BrowserSigningConfigInput"
        ] = None,
        enterprise_policies: Optional[
            "capo_bedrock_agentcore_control.types.browser_enterprise_policies.BrowserEnterprisePolicies"
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
    ) -> "capo_bedrock_agentcore_control.types.create_browser_response.CreateBrowserResponse":
        """<p>Creates a custom browser.</p>

        Args:
            name: <p>The name of the browser. The name must be unique within your account.</p>
            description: <p>The description of the browser.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the browser to access Amazon Web Services services.</p>
            network_configuration: <p>The network configuration for the browser. This configuration specifies the network mode for the browser.</p>
            recording: <p>The recording configuration for the browser. When enabled, browser sessions are recorded and stored in the specified Amazon S3 location.</p>
            browser_signing: <p>The browser signing configuration that enables cryptographic agent identification using HTTP message signatures for web bot authentication.</p>
            enterprise_policies: <p>A list of enterprise policy files for the browser.</p>
            certificates: <p>A list of certificates to install in the browser.</p>
            filesystem_configurations: <p>The file system configurations to mount into the browser. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your sessions can then access your data. If you don't specify this field, no file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>
            tags: <p>A map of tag keys and values to assign to the browser. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_browser_request.CreateBrowserRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_browser_response.CreateBrowserResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_browser

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_browser.async_create_browser(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_browser_request.CreateBrowserRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_browser_request

            return capo_bedrock_agentcore_control.types.create_browser_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateBrowser", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.create_browser_request.CreateBrowserRequest = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            input_["description"] = description
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if recording is not None:
            input_["recording"] = recording
        if browser_signing is not None:
            input_["browser_signing"] = browser_signing
        if enterprise_policies is not None:
            input_["enterprise_policies"] = enterprise_policies
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
        browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_browser_response.GetBrowserResponse":
        """<p>Gets information about a custom browser.</p>

        Args:
            browser_id: <p>The unique identifier of the browser to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_browser_request.GetBrowserRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_browser_response.GetBrowserResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_browser

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_browser.async_get_browser(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_browser_response.GetBrowserResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_browser_response

            return capo_bedrock_agentcore_control.types.get_browser_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetBrowser", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_browser_request.GetBrowserRequest = {
            "browser_id": browser_id
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
        browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_browser_response.DeleteBrowserResponse":
        """<p>Deletes a custom browser.</p>

        Args:
            browser_id: <p>The unique identifier of the browser to delete.</p>
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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_browser_request.DeleteBrowserRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_browser_response.DeleteBrowserResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_browser

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_browser.async_delete_browser(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBrowser")
        )
        input_: capo_bedrock_agentcore_control.types.delete_browser_request.DeleteBrowserRequest = {
            "browser_id": browser_id
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
    ) -> "capo_bedrock_agentcore_control.types.list_browsers_response.ListBrowsersResponse":
        """<p>Lists all custom browsers in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            type: <p>The type of browsers to list. If not specified, all browser types are returned.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_browsers_request.ListBrowsersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_browsers_response.ListBrowsersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_browsers

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_browsers.async_list_browsers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_browsers_response.ListBrowsersResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_browsers_response

            return capo_bedrock_agentcore_control.types.list_browsers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListBrowsers", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_browsers_request.ListBrowsersRequest = {}
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
