from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock._auth._signers
import capo_bedrock._auth._sigv4
from capo_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock.types.get_foundation_model_identifier
    import capo_bedrock.types.get_foundation_model_request
    import capo_bedrock.types.get_foundation_model_response
    import capo_bedrock.types.inference_type
    import capo_bedrock.types.list_foundation_models_request
    import capo_bedrock.types.list_foundation_models_response
    import capo_bedrock.types.model_customization
    import capo_bedrock.types.model_modality
    import capo_bedrock.types.provider
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class ModelResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def get_foundation_model(
        self,
        model_identifier: "capo_bedrock.types.get_foundation_model_identifier.GetFoundationModelIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_foundation_model_response.GetFoundationModelResponse":
        """<p>Get details about a Amazon Bedrock foundation model.</p>

        Args:
            model_identifier: <p>The model identifier. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_foundation_model_request.GetFoundationModelRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_foundation_model_response.GetFoundationModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model.get_foundation_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_foundation_model_request.GetFoundationModelRequest = {
            "model_identifier": model_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_foundation_models(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        by_provider: Optional["capo_bedrock.types.provider.Provider"] = None,
        by_customization_type: Optional[
            "capo_bedrock.types.model_customization.ModelCustomization"
        ] = None,
        by_output_modality: Optional[
            "capo_bedrock.types.model_modality.ModelModality"
        ] = None,
        by_inference_type: Optional[
            "capo_bedrock.types.inference_type.InferenceType"
        ] = None,
    ) -> "capo_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse":
        """<p>Lists Amazon Bedrock foundation models that you can use. You can filter the results with the request parameters. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models.html">Foundation models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            by_provider: <p>Return models belonging to the model provider that you specify.</p>
            by_customization_type: <p>Return models that support the customization type that you specify. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            by_output_modality: <p>Return models that support the output modality that you specify.</p>
            by_inference_type: <p>Return models that support the inference type that you specify. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models.list_foundation_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest = {}
        if by_provider is not None:
            input_["by_provider"] = by_provider
        if by_customization_type is not None:
            input_["by_customization_type"] = by_customization_type
        if by_output_modality is not None:
            input_["by_output_modality"] = by_output_modality
        if by_inference_type is not None:
            input_["by_inference_type"] = by_inference_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncModelResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def get_foundation_model(
        self,
        model_identifier: "capo_bedrock.types.get_foundation_model_identifier.GetFoundationModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_foundation_model_response.GetFoundationModelResponse":
        """<p>Get details about a Amazon Bedrock foundation model.</p>

        Args:
            model_identifier: <p>The model identifier. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_foundation_model_request.GetFoundationModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_foundation_model_response.GetFoundationModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model.async_get_foundation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_foundation_model_request.GetFoundationModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_foundation_models(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        by_provider: Optional["capo_bedrock.types.provider.Provider"] = None,
        by_customization_type: Optional[
            "capo_bedrock.types.model_customization.ModelCustomization"
        ] = None,
        by_output_modality: Optional[
            "capo_bedrock.types.model_modality.ModelModality"
        ] = None,
        by_inference_type: Optional[
            "capo_bedrock.types.inference_type.InferenceType"
        ] = None,
    ) -> "capo_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse":
        """<p>Lists Amazon Bedrock foundation models that you can use. You can filter the results with the request parameters. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models.html">Foundation models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            by_provider: <p>Return models belonging to the model provider that you specify.</p>
            by_customization_type: <p>Return models that support the customization type that you specify. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            by_output_modality: <p>Return models that support the output modality that you specify.</p>
            by_inference_type: <p>Return models that support the inference type that you specify. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models.async_list_foundation_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest = {}
        if by_provider is not None:
            input_["by_provider"] = by_provider
        if by_customization_type is not None:
            input_["by_customization_type"] = by_customization_type
        if by_output_modality is not None:
            input_["by_output_modality"] = by_output_modality
        if by_inference_type is not None:
            input_["by_inference_type"] = by_inference_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
