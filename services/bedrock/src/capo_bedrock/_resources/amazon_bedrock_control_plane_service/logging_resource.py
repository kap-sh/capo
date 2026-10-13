from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock._auth._signers
import capo_bedrock._auth._sigv4
from capo_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock.types.delete_model_invocation_logging_configuration_request
    import capo_bedrock.types.delete_model_invocation_logging_configuration_response
    import capo_bedrock.types.get_model_invocation_logging_configuration_request
    import capo_bedrock.types.get_model_invocation_logging_configuration_response
    import capo_bedrock.types.logging_config
    import capo_bedrock.types.put_model_invocation_logging_configuration_request
    import capo_bedrock.types.put_model_invocation_logging_configuration_response
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class LoggingResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def delete_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[BedrockClientConfig] = None
    ) -> "capo_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse":
        """<p>Delete the invocation logging. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration.delete_model_invocation_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteModelInvocationLoggingConfiguration"),
        )
        input_: capo_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[BedrockClientConfig] = None
    ) -> "capo_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse":
        """<p>Get the current configuration values for model invocation logging.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration.get_model_invocation_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetModelInvocationLoggingConfiguration")
        )
        input_: capo_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_model_invocation_logging_configuration(
        self,
        logging_config: "capo_bedrock.types.logging_config.LoggingConfig",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse":
        """<p>Set the configuration values for model invocation logging.</p>

        Args:
            logging_config: <p>The logging configuration values to set.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration.put_model_invocation_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutModelInvocationLoggingConfiguration")
        )
        input_: capo_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest = {
            "logging_config": logging_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncLoggingResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def delete_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "capo_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse":
        """<p>Delete the invocation logging. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration.async_delete_model_invocation_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteModelInvocationLoggingConfiguration"),
        )
        input_: capo_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "capo_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse":
        """<p>Get the current configuration values for model invocation logging.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration.async_get_model_invocation_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetModelInvocationLoggingConfiguration")
        )
        input_: capo_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_model_invocation_logging_configuration(
        self,
        logging_config: "capo_bedrock.types.logging_config.LoggingConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse":
        """<p>Set the configuration values for model invocation logging.</p>

        Args:
            logging_config: <p>The logging configuration values to set.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration.async_put_model_invocation_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutModelInvocationLoggingConfiguration")
        )
        input_: capo_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest = {
            "logging_config": logging_config
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
