from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock_data_automation._auth._signers
import capo_bedrock_data_automation._auth._sigv4
from capo_bedrock_data_automation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_optimization_invocation_arn
    import capo_bedrock_data_automation.types.blueprint_optimization_object
    import capo_bedrock_data_automation.types.blueprint_optimization_output_configuration
    import capo_bedrock_data_automation.types.blueprint_optimization_samples
    import capo_bedrock_data_automation.types.data_automation_profile_arn
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.get_blueprint_optimization_status_request
    import capo_bedrock_data_automation.types.get_blueprint_optimization_status_response
    import capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_request
    import capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_response
    import capo_bedrock_data_automation.types.tag_list
    from capo_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from capo_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class BlueprintOptimizationJobResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        blueprint: "capo_bedrock_data_automation.types.blueprint_optimization_object.BlueprintOptimizationObject",
        samples: "capo_bedrock_data_automation.types.blueprint_optimization_samples.BlueprintOptimizationSamples",
        output_configuration: "capo_bedrock_data_automation.types.blueprint_optimization_output_configuration.BlueprintOptimizationOutputConfiguration",
        data_automation_profile_arn: "capo_bedrock_data_automation.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse":
        """Invoke an async job to perform Blueprint Optimization

        Args:
            blueprint: Blueprint to be optimized
            samples: List of Blueprint Optimization Samples
            output_configuration: Output configuration where the results should be placed
            data_automation_profile_arn: Data automation profile ARN
            encryption_configuration: Encryption configuration.
            tags: List of tags.

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async.invoke_blueprint_optimization_async(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("InvokeBlueprintOptimizationAsync")
        )
        input_: capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest = {
            "blueprint": blueprint,
            "samples": samples,
            "output_configuration": output_configuration,
            "data_automation_profile_arn": data_automation_profile_arn,
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
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
        invocation_arn: "capo_bedrock_data_automation.types.blueprint_optimization_invocation_arn.BlueprintOptimizationInvocationArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse":
        """API used to get blueprint optimization status.

        Args:
            invocation_arn: Invocation arn.

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status.get_blueprint_optimization_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBlueprintOptimizationStatus")
        )
        input_: capo_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest = {
            "invocation_arn": invocation_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncBlueprintOptimizationJobResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        blueprint: "capo_bedrock_data_automation.types.blueprint_optimization_object.BlueprintOptimizationObject",
        samples: "capo_bedrock_data_automation.types.blueprint_optimization_samples.BlueprintOptimizationSamples",
        output_configuration: "capo_bedrock_data_automation.types.blueprint_optimization_output_configuration.BlueprintOptimizationOutputConfiguration",
        data_automation_profile_arn: "capo_bedrock_data_automation.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse":
        """Invoke an async job to perform Blueprint Optimization

        Args:
            blueprint: Blueprint to be optimized
            samples: List of Blueprint Optimization Samples
            output_configuration: Output configuration where the results should be placed
            data_automation_profile_arn: Data automation profile ARN
            encryption_configuration: Encryption configuration.
            tags: List of tags.

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async.async_invoke_blueprint_optimization_async(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("InvokeBlueprintOptimizationAsync")
        )
        input_: capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest = {
            "blueprint": blueprint,
            "samples": samples,
            "output_configuration": output_configuration,
            "data_automation_profile_arn": data_automation_profile_arn,
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
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
        invocation_arn: "capo_bedrock_data_automation.types.blueprint_optimization_invocation_arn.BlueprintOptimizationInvocationArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse":
        """API used to get blueprint optimization status.

        Args:
            invocation_arn: Invocation arn.

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status.async_get_blueprint_optimization_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBlueprintOptimizationStatus")
        )
        input_: capo_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest = {
            "invocation_arn": invocation_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
