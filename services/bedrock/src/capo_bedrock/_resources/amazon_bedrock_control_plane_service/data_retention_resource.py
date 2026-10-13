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
    import capo_bedrock.types.data_retention_mode
    import capo_bedrock.types.get_account_data_retention_request
    import capo_bedrock.types.get_account_data_retention_response
    import capo_bedrock.types.put_account_data_retention_request
    import capo_bedrock.types.put_account_data_retention_response
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class DataRetentionResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def get_account_data_retention(
        self, *, config_overrides: Optional[BedrockClientConfig] = None
    ) -> "capo_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse":
        """<p>Returns the account-wide data retention mode for Amazon Bedrock.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention.get_account_data_retention(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAccountDataRetention")
        )
        input_: capo_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_account_data_retention(
        self,
        mode: "capo_bedrock.types.data_retention_mode.DataRetentionMode",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse":
        """<p>Sets the account-wide data retention mode for Amazon Bedrock.</p>

        Args:
            mode: <p>The data retention mode to set for the account.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention.put_account_data_retention(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutAccountDataRetention")
        )
        input_: capo_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest = {
            "mode": mode
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDataRetentionResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def get_account_data_retention(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "capo_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse":
        """<p>Returns the account-wide data retention mode for Amazon Bedrock.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention.async_get_account_data_retention(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAccountDataRetention")
        )
        input_: capo_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_data_retention(
        self,
        mode: "capo_bedrock.types.data_retention_mode.DataRetentionMode",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse":
        """<p>Sets the account-wide data retention mode for Amazon Bedrock.</p>

        Args:
            mode: <p>The data retention mode to set for the account.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention.async_put_account_data_retention(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutAccountDataRetention")
        )
        input_: capo_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest = {
            "mode": mode
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
