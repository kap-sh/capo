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
    import capo_bedrock.types.bedrock_model_id
    import capo_bedrock.types.create_foundation_model_agreement_request
    import capo_bedrock.types.create_foundation_model_agreement_response
    import capo_bedrock.types.delete_foundation_model_agreement_request
    import capo_bedrock.types.delete_foundation_model_agreement_response
    import capo_bedrock.types.get_foundation_model_availability_request
    import capo_bedrock.types.get_foundation_model_availability_response
    import capo_bedrock.types.list_foundation_model_agreement_offers_request
    import capo_bedrock.types.list_foundation_model_agreement_offers_response
    import capo_bedrock.types.offer_token
    import capo_bedrock.types.offer_type
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class SubscriptionResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_foundation_model_agreement(
        self,
        offer_token: "capo_bedrock.types.offer_token.OfferToken",
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse":
        """<p>Request a model access agreement for the specified model.</p>

        Args:
            offer_token: <p>An offer token encapsulates the information for an offer.</p>
            model_id: <p>Model Id of the model for the access request.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement.create_foundation_model_agreement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFoundationModelAgreement")
        )
        input_: capo_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest = {
            "offer_token": offer_token,
            "model_id": model_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_foundation_model_agreement(
        self,
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse":
        """<p>Delete the model access agreement for the specified model.</p>

        Args:
            model_id: <p>Model Id of the model access to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement.delete_foundation_model_agreement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFoundationModelAgreement")
        )
        input_: capo_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest = {
            "model_id": model_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_foundation_model_availability(
        self,
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse":
        """<p>Get information about the Foundation model availability.</p>

        Args:
            model_id: <p>The model Id of the foundation model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability.get_foundation_model_availability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFoundationModelAvailability")
        )
        input_: capo_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest = {
            "model_id": model_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_foundation_model_agreement_offers(
        self,
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        offer_type: Optional["capo_bedrock.types.offer_type.OfferType"] = None,
    ) -> "capo_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse":
        """<p>Get the offers associated with the specified model.</p>

        Args:
            model_id: <p>Model Id of the foundation model.</p>
            offer_type: <p>Type of offer associated with the model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers.list_foundation_model_agreement_offers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFoundationModelAgreementOffers")
        )
        input_: capo_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest = {
            "model_id": model_id
        }
        if offer_type is not None:
            input_["offer_type"] = offer_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSubscriptionResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_foundation_model_agreement(
        self,
        offer_token: "capo_bedrock.types.offer_token.OfferToken",
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse":
        """<p>Request a model access agreement for the specified model.</p>

        Args:
            offer_token: <p>An offer token encapsulates the information for an offer.</p>
            model_id: <p>Model Id of the model for the access request.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement.async_create_foundation_model_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFoundationModelAgreement")
        )
        input_: capo_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest = {
            "offer_token": offer_token,
            "model_id": model_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_foundation_model_agreement(
        self,
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse":
        """<p>Delete the model access agreement for the specified model.</p>

        Args:
            model_id: <p>Model Id of the model access to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement.async_delete_foundation_model_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFoundationModelAgreement")
        )
        input_: capo_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest = {
            "model_id": model_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_foundation_model_availability(
        self,
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse":
        """<p>Get information about the Foundation model availability.</p>

        Args:
            model_id: <p>The model Id of the foundation model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability.async_get_foundation_model_availability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFoundationModelAvailability")
        )
        input_: capo_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest = {
            "model_id": model_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_foundation_model_agreement_offers(
        self,
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        offer_type: Optional["capo_bedrock.types.offer_type.OfferType"] = None,
    ) -> "capo_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse":
        """<p>Get the offers associated with the specified model.</p>

        Args:
            model_id: <p>Model Id of the foundation model.</p>
            offer_type: <p>Type of offer associated with the model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers.async_list_foundation_model_agreement_offers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFoundationModelAgreementOffers")
        )
        input_: capo_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest = {
            "model_id": model_id
        }
        if offer_type is not None:
            input_["offer_type"] = offer_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
