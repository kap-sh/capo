from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_socialmessaging._auth._signers
import capo_socialmessaging._auth._sigv4
from capo_socialmessaging._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_socialmessaging.types.business_public_key_pem
    import capo_socialmessaging.types.delete_whats_app_message_media_input
    import capo_socialmessaging.types.delete_whats_app_message_media_output
    import capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input
    import capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output
    import capo_socialmessaging.types.get_whats_app_business_public_key_input
    import capo_socialmessaging.types.get_whats_app_business_public_key_output
    import capo_socialmessaging.types.get_whats_app_call_permission_input
    import capo_socialmessaging.types.get_whats_app_call_permission_output
    import capo_socialmessaging.types.get_whats_app_message_media_input
    import capo_socialmessaging.types.get_whats_app_message_media_output
    import capo_socialmessaging.types.kms_key_arn
    import capo_socialmessaging.types.post_whats_app_message_media_input
    import capo_socialmessaging.types.post_whats_app_message_media_output
    import capo_socialmessaging.types.put_whats_app_business_public_key_input
    import capo_socialmessaging.types.put_whats_app_business_public_key_output
    import capo_socialmessaging.types.s3_file
    import capo_socialmessaging.types.s3_presigned_url
    import capo_socialmessaging.types.send_whats_app_call_event_input
    import capo_socialmessaging.types.send_whats_app_call_event_output
    import capo_socialmessaging.types.send_whats_app_message_input
    import capo_socialmessaging.types.send_whats_app_message_output
    import capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_input
    import capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_output
    import capo_socialmessaging.types.whats_app_business_scoped_user_id
    import capo_socialmessaging.types.whats_app_call_event_blob
    import capo_socialmessaging.types.whats_app_call_settings
    import capo_socialmessaging.types.whats_app_destination_phone_number
    import capo_socialmessaging.types.whats_app_media_id
    import capo_socialmessaging.types.whats_app_message_blob
    import capo_socialmessaging.types.whats_app_phone_number_id
    from capo_socialmessaging._services.async_social_messaging import (
        AsyncSocialMessagingClient,
        AsyncSocialMessagingClientConfig,
    )
    from capo_socialmessaging._services.social_messaging import (
        SocialMessagingClient,
        SocialMessagingClientConfig,
    )


class LinkedWhatsAppPhoneNumberResource:
    def __init__(self, service: SocialMessagingClient) -> None:
        self._service = service

    def read(
        self,
        id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output.GetLinkedWhatsAppBusinessAccountPhoneNumberOutput":
        """<p>Retrieve the WABA account id and phone number details of a WhatsApp business account phone number.</p>

        Args:
            id: <p>The unique identifier of the phone number. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input.GetLinkedWhatsAppBusinessAccountPhoneNumberInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output.GetLinkedWhatsAppBusinessAccountPhoneNumberOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account_phone_number

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account_phone_number.get_linked_whats_app_business_account_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input.GetLinkedWhatsAppBusinessAccountPhoneNumberInput = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_whats_app_message_media(
        self,
        media_id: "capo_socialmessaging.types.whats_app_media_id.WhatsAppMediaId",
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput":
        """<p>Delete a media object from the WhatsApp service. If the object is still in an Amazon S3 bucket you should delete it from there too.</p>

        Args:
            media_id: <p>The unique identifier of the media file to delete. Use the <code>mediaId</code> returned from <a href="https://console.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html">PostWhatsAppMessageMedia</a>.</p>
            origination_phone_number_id: <p>The unique identifier of the originating phone number associated with the media. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.delete_whats_app_message_media

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.delete_whats_app_message_media.delete_whats_app_message_media(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput = {
            "media_id": media_id,
            "origination_phone_number_id": origination_phone_number_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_whats_app_business_public_key(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.get_whats_app_business_public_key_output.GetWhatsAppBusinessPublicKeyOutput":
        """<p>Retrieves the business public key for a phone number and its signature status.</p>

        Args:
            origination_phone_number_id: <p>The unique identifier of the phone number whose business public key to retrieve.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.get_whats_app_business_public_key_input.GetWhatsAppBusinessPublicKeyInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.get_whats_app_business_public_key_output.GetWhatsAppBusinessPublicKeyOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_whats_app_business_public_key

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.get_whats_app_business_public_key.get_whats_app_business_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_whats_app_business_public_key_input.GetWhatsAppBusinessPublicKeyInput = {
            "origination_phone_number_id": origination_phone_number_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_whats_app_call_permission(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        destination_phone_number: Optional[
            "capo_socialmessaging.types.whats_app_destination_phone_number.WhatsAppDestinationPhoneNumber"
        ] = None,
        end_user_bsuid: Optional[
            "capo_socialmessaging.types.whats_app_business_scoped_user_id.WhatsAppBusinessScopedUserId"
        ] = None,
    ) -> "capo_socialmessaging.types.get_whats_app_call_permission_output.GetWhatsAppCallPermissionOutput":
        """<p>Retrieves the current calling permission for a WhatsApp end user, along with the calling actions the business is allowed to take with that user. Provide the destination phone number or the business-scoped user ID to identify the end user.</p>

        Args:
            origination_phone_number_id: <p>The unique identifier of the business phone number for which to retrieve the calling permission. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>.</p>
            destination_phone_number: <p>The end user's phone number, in E.164 format, for which to retrieve the calling permission.</p>
            end_user_bsuid: <p>The business-scoped user identifier (BSUID) of the end user for which to retrieve the calling permission.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.get_whats_app_call_permission_input.GetWhatsAppCallPermissionInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.get_whats_app_call_permission_output.GetWhatsAppCallPermissionOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_whats_app_call_permission

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.get_whats_app_call_permission.get_whats_app_call_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_whats_app_call_permission_input.GetWhatsAppCallPermissionInput = {
            "origination_phone_number_id": origination_phone_number_id
        }
        if destination_phone_number is not None:
            input_["destination_phone_number"] = destination_phone_number
        if end_user_bsuid is not None:
            input_["end_user_bsuid"] = end_user_bsuid

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_whats_app_message_media(
        self,
        media_id: "capo_socialmessaging.types.whats_app_media_id.WhatsAppMediaId",
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        metadata_only: Optional[bool] = None,
        destination_s3_presigned_url: Optional[
            "capo_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
        ] = None,
        destination_s3_file: Optional[
            "capo_socialmessaging.types.s3_file.S3File"
        ] = None,
    ) -> "capo_socialmessaging.types.get_whats_app_message_media_output.GetWhatsAppMessageMediaOutput":
        """<p>Get a media file from the WhatsApp service. On successful completion the media file is retrieved from Meta and stored in the specified Amazon S3 bucket. Use either <code>destinationS3File</code> or <code>destinationS3PresignedUrl</code> for the destination. If both are used then an <code>InvalidParameterException</code> is returned.</p>

        Args:
            media_id: <p>The unique identifier for the media file.</p>
            origination_phone_number_id: <p>The unique identifier of the originating phone number for the WhatsApp message media. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            metadata_only: <p>Set to <code>True</code> to get only the metadata for the file.</p>
            destination_s3_presigned_url: <p>The presign url of the media file.</p>
            destination_s3_file: <p>The <code>bucketName</code> and <code>key</code> of the S3 media file.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.get_whats_app_message_media_input.GetWhatsAppMessageMediaInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.get_whats_app_message_media_output.GetWhatsAppMessageMediaOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_whats_app_message_media

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.get_whats_app_message_media.get_whats_app_message_media(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_whats_app_message_media_input.GetWhatsAppMessageMediaInput = {
            "media_id": media_id,
            "origination_phone_number_id": origination_phone_number_id,
        }
        if metadata_only is not None:
            input_["metadata_only"] = metadata_only
        if destination_s3_presigned_url is not None:
            input_["destination_s3_presigned_url"] = destination_s3_presigned_url
        if destination_s3_file is not None:
            input_["destination_s3_file"] = destination_s3_file

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def post_whats_app_message_media(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        source_s3_presigned_url: Optional[
            "capo_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
        ] = None,
        source_s3_file: Optional["capo_socialmessaging.types.s3_file.S3File"] = None,
    ) -> "capo_socialmessaging.types.post_whats_app_message_media_output.PostWhatsAppMessageMediaOutput":
        """<p>Upload a media file to the WhatsApp service. Only the specified <code>originationPhoneNumberId</code> has the permissions to send the media file when using <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html">SendWhatsAppMessage</a>. You must use either <code>sourceS3File</code> or <code>sourceS3PresignedUrl</code> for the source. If both or neither are specified then an <code>InvalidParameterException</code> is returned.</p>

        Args:
            origination_phone_number_id: <p>The ID of the phone number to associate with the WhatsApp media file. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            source_s3_presigned_url: <p>The source presign url of the media file.</p>
            source_s3_file: <p>The source S3 url for the media file.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.post_whats_app_message_media_input.PostWhatsAppMessageMediaInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.post_whats_app_message_media_output.PostWhatsAppMessageMediaOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.post_whats_app_message_media

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.post_whats_app_message_media.post_whats_app_message_media(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.post_whats_app_message_media_input.PostWhatsAppMessageMediaInput = {
            "origination_phone_number_id": origination_phone_number_id
        }
        if source_s3_presigned_url is not None:
            input_["source_s3_presigned_url"] = source_s3_presigned_url
        if source_s3_file is not None:
            input_["source_s3_file"] = source_s3_file

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_whats_app_business_public_key(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        business_public_key: Optional[
            "capo_socialmessaging.types.business_public_key_pem.BusinessPublicKeyPem"
        ] = None,
        kms_key_arn: Optional[
            "capo_socialmessaging.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_socialmessaging.types.put_whats_app_business_public_key_output.PutWhatsAppBusinessPublicKeyOutput":
        """<p>Sets the business public key used to encrypt the data exchanged with the endpoint of a data exchange Flow.</p>

        Args:
            origination_phone_number_id: <p>The unique identifier of the phone number to associate with the business public key.</p>
            business_public_key: <p>The PEM-encoded 2048-bit RSA public key to set. Mutually exclusive with <code>kmsKeyArn</code>.</p>
            kms_key_arn: <p>The ARN of a customer managed asymmetric RSA key in Amazon Web Services KMS. Mutually exclusive with <code>businessPublicKey</code>.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.put_whats_app_business_public_key_input.PutWhatsAppBusinessPublicKeyInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.put_whats_app_business_public_key_output.PutWhatsAppBusinessPublicKeyOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.put_whats_app_business_public_key

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.put_whats_app_business_public_key.put_whats_app_business_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.put_whats_app_business_public_key_input.PutWhatsAppBusinessPublicKeyInput = {
            "origination_phone_number_id": origination_phone_number_id
        }
        if business_public_key is not None:
            input_["business_public_key"] = business_public_key
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_whats_app_call_event(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        meta_api_version: str,
        call_event: "capo_socialmessaging.types.whats_app_call_event_blob.WhatsAppCallEventBlob",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.send_whats_app_call_event_output.SendWhatsAppCallEventOutput":
        """<p>Sends a WhatsApp calling event, such as connecting or terminating a call, for a business phone number. This operation passes the event through to Meta. To use this operation, the origination phone number must belong to a WhatsApp Business Account that is linked to your Amazon Web Services account.</p>

        Args:
            origination_phone_number_id: <p>The unique identifier of the origination phone number for the call. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <code>GetLinkedWhatsAppBusinessAccount</code> to find a phone number's ID.</p>
            meta_api_version: <p>The version of the Meta Graph API to use for the request.</p>
            call_event: <p>The call event payload to send, as a JSON blob in the format defined by the Meta calling API.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.send_whats_app_call_event_input.SendWhatsAppCallEventInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.send_whats_app_call_event_output.SendWhatsAppCallEventOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.send_whats_app_call_event

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.send_whats_app_call_event.send_whats_app_call_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.send_whats_app_call_event_input.SendWhatsAppCallEventInput = {
            "origination_phone_number_id": origination_phone_number_id,
            "meta_api_version": meta_api_version,
            "call_event": call_event,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_whats_app_message(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        message: "capo_socialmessaging.types.whats_app_message_blob.WhatsAppMessageBlob",
        meta_api_version: str,
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.send_whats_app_message_output.SendWhatsAppMessageOutput":
        """<p>Send a WhatsApp message. For examples of sending a message using the Amazon Web Services CLI, see <a href="https://docs.aws.amazon.com/social-messaging/latest/userguide/send-message.html">Sending messages</a> in the <i> <i>Amazon Web Services End User Messaging Social User Guide</i> </i>.</p>

        Args:
            origination_phone_number_id: <p>The ID of the phone number used to send the WhatsApp message. If you are sending a media file only the <code>originationPhoneNumberId</code> used to upload the file can be used. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            message: <p>The message to send through WhatsApp. The length is in KB. The message field passes through a WhatsApp Message object, see <a href="https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages">Messages</a> in the <i>WhatsApp Business Platform Cloud API Reference</i>.</p>
            meta_api_version: <p>The API version for the request formatted as <code>v{VersionNumber}</code>. For a list of supported API versions and Amazon Web Services Regions, see <a href="https://docs.aws.amazon.com/general/latest/gr/end-user-messaging.html"> <i>Amazon Web Services End User Messaging Social API</i> Service Endpoints</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.send_whats_app_message_input.SendWhatsAppMessageInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.send_whats_app_message_output.SendWhatsAppMessageOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.send_whats_app_message

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.send_whats_app_message.send_whats_app_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.send_whats_app_message_input.SendWhatsAppMessageInput = {
            "origination_phone_number_id": origination_phone_number_id,
            "message": message,
            "meta_api_version": meta_api_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_linked_whats_app_business_account_phone_number(
        self,
        id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        call_settings: "capo_socialmessaging.types.whats_app_call_settings.WhatsAppCallSettings",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_output.UpdateLinkedWhatsAppBusinessAccountPhoneNumberOutput":
        """<p>Updates the calling settings for a linked WhatsApp business phone number, such as whether calling is enabled and the hours during which the business accepts calls.</p>

        Args:
            id: <p>The unique identifier of the phone number to update. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>.</p>
            call_settings: <p>The calling settings to apply to the phone number.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_input.UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput]",
        ) -> OperationResponse[
            "capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_output.UpdateLinkedWhatsAppBusinessAccountPhoneNumberOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.update_linked_whats_app_business_account_phone_number

            output, http_response = (
                capo_socialmessaging._operations.social_messaging.update_linked_whats_app_business_account_phone_number.update_linked_whats_app_business_account_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_input.UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput = {
            "id": id,
            "call_settings": call_settings,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncLinkedWhatsAppPhoneNumberResource:
    def __init__(self, service: AsyncSocialMessagingClient) -> None:
        self._service = service

    async def read(
        self,
        id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output.GetLinkedWhatsAppBusinessAccountPhoneNumberOutput":
        """<p>Retrieve the WABA account id and phone number details of a WhatsApp business account phone number.</p>

        Args:
            id: <p>The unique identifier of the phone number. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input.GetLinkedWhatsAppBusinessAccountPhoneNumberInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output.GetLinkedWhatsAppBusinessAccountPhoneNumberOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account_phone_number

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account_phone_number.async_get_linked_whats_app_business_account_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input.GetLinkedWhatsAppBusinessAccountPhoneNumberInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_whats_app_message_media(
        self,
        media_id: "capo_socialmessaging.types.whats_app_media_id.WhatsAppMediaId",
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput":
        """<p>Delete a media object from the WhatsApp service. If the object is still in an Amazon S3 bucket you should delete it from there too.</p>

        Args:
            media_id: <p>The unique identifier of the media file to delete. Use the <code>mediaId</code> returned from <a href="https://console.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html">PostWhatsAppMessageMedia</a>.</p>
            origination_phone_number_id: <p>The unique identifier of the originating phone number associated with the media. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.delete_whats_app_message_media

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.delete_whats_app_message_media.async_delete_whats_app_message_media(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput = {
            "media_id": media_id,
            "origination_phone_number_id": origination_phone_number_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_whats_app_business_public_key(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.get_whats_app_business_public_key_output.GetWhatsAppBusinessPublicKeyOutput":
        """<p>Retrieves the business public key for a phone number and its signature status.</p>

        Args:
            origination_phone_number_id: <p>The unique identifier of the phone number whose business public key to retrieve.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.get_whats_app_business_public_key_input.GetWhatsAppBusinessPublicKeyInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.get_whats_app_business_public_key_output.GetWhatsAppBusinessPublicKeyOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_whats_app_business_public_key

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.get_whats_app_business_public_key.async_get_whats_app_business_public_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_whats_app_business_public_key_input.GetWhatsAppBusinessPublicKeyInput = {
            "origination_phone_number_id": origination_phone_number_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_whats_app_call_permission(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        destination_phone_number: Optional[
            "capo_socialmessaging.types.whats_app_destination_phone_number.WhatsAppDestinationPhoneNumber"
        ] = None,
        end_user_bsuid: Optional[
            "capo_socialmessaging.types.whats_app_business_scoped_user_id.WhatsAppBusinessScopedUserId"
        ] = None,
    ) -> "capo_socialmessaging.types.get_whats_app_call_permission_output.GetWhatsAppCallPermissionOutput":
        """<p>Retrieves the current calling permission for a WhatsApp end user, along with the calling actions the business is allowed to take with that user. Provide the destination phone number or the business-scoped user ID to identify the end user.</p>

        Args:
            origination_phone_number_id: <p>The unique identifier of the business phone number for which to retrieve the calling permission. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>.</p>
            destination_phone_number: <p>The end user's phone number, in E.164 format, for which to retrieve the calling permission.</p>
            end_user_bsuid: <p>The business-scoped user identifier (BSUID) of the end user for which to retrieve the calling permission.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.get_whats_app_call_permission_input.GetWhatsAppCallPermissionInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.get_whats_app_call_permission_output.GetWhatsAppCallPermissionOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_whats_app_call_permission

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.get_whats_app_call_permission.async_get_whats_app_call_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_whats_app_call_permission_input.GetWhatsAppCallPermissionInput = {
            "origination_phone_number_id": origination_phone_number_id
        }
        if destination_phone_number is not None:
            input_["destination_phone_number"] = destination_phone_number
        if end_user_bsuid is not None:
            input_["end_user_bsuid"] = end_user_bsuid

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_whats_app_message_media(
        self,
        media_id: "capo_socialmessaging.types.whats_app_media_id.WhatsAppMediaId",
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        metadata_only: Optional[bool] = None,
        destination_s3_presigned_url: Optional[
            "capo_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
        ] = None,
        destination_s3_file: Optional[
            "capo_socialmessaging.types.s3_file.S3File"
        ] = None,
    ) -> "capo_socialmessaging.types.get_whats_app_message_media_output.GetWhatsAppMessageMediaOutput":
        """<p>Get a media file from the WhatsApp service. On successful completion the media file is retrieved from Meta and stored in the specified Amazon S3 bucket. Use either <code>destinationS3File</code> or <code>destinationS3PresignedUrl</code> for the destination. If both are used then an <code>InvalidParameterException</code> is returned.</p>

        Args:
            media_id: <p>The unique identifier for the media file.</p>
            origination_phone_number_id: <p>The unique identifier of the originating phone number for the WhatsApp message media. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            metadata_only: <p>Set to <code>True</code> to get only the metadata for the file.</p>
            destination_s3_presigned_url: <p>The presign url of the media file.</p>
            destination_s3_file: <p>The <code>bucketName</code> and <code>key</code> of the S3 media file.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.get_whats_app_message_media_input.GetWhatsAppMessageMediaInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.get_whats_app_message_media_output.GetWhatsAppMessageMediaOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_whats_app_message_media

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.get_whats_app_message_media.async_get_whats_app_message_media(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_whats_app_message_media_input.GetWhatsAppMessageMediaInput = {
            "media_id": media_id,
            "origination_phone_number_id": origination_phone_number_id,
        }
        if metadata_only is not None:
            input_["metadata_only"] = metadata_only
        if destination_s3_presigned_url is not None:
            input_["destination_s3_presigned_url"] = destination_s3_presigned_url
        if destination_s3_file is not None:
            input_["destination_s3_file"] = destination_s3_file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def post_whats_app_message_media(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        source_s3_presigned_url: Optional[
            "capo_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
        ] = None,
        source_s3_file: Optional["capo_socialmessaging.types.s3_file.S3File"] = None,
    ) -> "capo_socialmessaging.types.post_whats_app_message_media_output.PostWhatsAppMessageMediaOutput":
        """<p>Upload a media file to the WhatsApp service. Only the specified <code>originationPhoneNumberId</code> has the permissions to send the media file when using <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html">SendWhatsAppMessage</a>. You must use either <code>sourceS3File</code> or <code>sourceS3PresignedUrl</code> for the source. If both or neither are specified then an <code>InvalidParameterException</code> is returned.</p>

        Args:
            origination_phone_number_id: <p>The ID of the phone number to associate with the WhatsApp media file. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            source_s3_presigned_url: <p>The source presign url of the media file.</p>
            source_s3_file: <p>The source S3 url for the media file.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.post_whats_app_message_media_input.PostWhatsAppMessageMediaInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.post_whats_app_message_media_output.PostWhatsAppMessageMediaOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.post_whats_app_message_media

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.post_whats_app_message_media.async_post_whats_app_message_media(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.post_whats_app_message_media_input.PostWhatsAppMessageMediaInput = {
            "origination_phone_number_id": origination_phone_number_id
        }
        if source_s3_presigned_url is not None:
            input_["source_s3_presigned_url"] = source_s3_presigned_url
        if source_s3_file is not None:
            input_["source_s3_file"] = source_s3_file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_whats_app_business_public_key(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        business_public_key: Optional[
            "capo_socialmessaging.types.business_public_key_pem.BusinessPublicKeyPem"
        ] = None,
        kms_key_arn: Optional[
            "capo_socialmessaging.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_socialmessaging.types.put_whats_app_business_public_key_output.PutWhatsAppBusinessPublicKeyOutput":
        """<p>Sets the business public key used to encrypt the data exchanged with the endpoint of a data exchange Flow.</p>

        Args:
            origination_phone_number_id: <p>The unique identifier of the phone number to associate with the business public key.</p>
            business_public_key: <p>The PEM-encoded 2048-bit RSA public key to set. Mutually exclusive with <code>kmsKeyArn</code>.</p>
            kms_key_arn: <p>The ARN of a customer managed asymmetric RSA key in Amazon Web Services KMS. Mutually exclusive with <code>businessPublicKey</code>.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.put_whats_app_business_public_key_input.PutWhatsAppBusinessPublicKeyInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.put_whats_app_business_public_key_output.PutWhatsAppBusinessPublicKeyOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.put_whats_app_business_public_key

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.put_whats_app_business_public_key.async_put_whats_app_business_public_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.put_whats_app_business_public_key_input.PutWhatsAppBusinessPublicKeyInput = {
            "origination_phone_number_id": origination_phone_number_id
        }
        if business_public_key is not None:
            input_["business_public_key"] = business_public_key
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_whats_app_call_event(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        meta_api_version: str,
        call_event: "capo_socialmessaging.types.whats_app_call_event_blob.WhatsAppCallEventBlob",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.send_whats_app_call_event_output.SendWhatsAppCallEventOutput":
        """<p>Sends a WhatsApp calling event, such as connecting or terminating a call, for a business phone number. This operation passes the event through to Meta. To use this operation, the origination phone number must belong to a WhatsApp Business Account that is linked to your Amazon Web Services account.</p>

        Args:
            origination_phone_number_id: <p>The unique identifier of the origination phone number for the call. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <code>GetLinkedWhatsAppBusinessAccount</code> to find a phone number's ID.</p>
            meta_api_version: <p>The version of the Meta Graph API to use for the request.</p>
            call_event: <p>The call event payload to send, as a JSON blob in the format defined by the Meta calling API.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.send_whats_app_call_event_input.SendWhatsAppCallEventInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.send_whats_app_call_event_output.SendWhatsAppCallEventOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.send_whats_app_call_event

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.send_whats_app_call_event.async_send_whats_app_call_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.send_whats_app_call_event_input.SendWhatsAppCallEventInput = {
            "origination_phone_number_id": origination_phone_number_id,
            "meta_api_version": meta_api_version,
            "call_event": call_event,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_whats_app_message(
        self,
        origination_phone_number_id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        message: "capo_socialmessaging.types.whats_app_message_blob.WhatsAppMessageBlob",
        meta_api_version: str,
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.send_whats_app_message_output.SendWhatsAppMessageOutput":
        """<p>Send a WhatsApp message. For examples of sending a message using the Amazon Web Services CLI, see <a href="https://docs.aws.amazon.com/social-messaging/latest/userguide/send-message.html">Sending messages</a> in the <i> <i>Amazon Web Services End User Messaging Social User Guide</i> </i>.</p>

        Args:
            origination_phone_number_id: <p>The ID of the phone number used to send the WhatsApp message. If you are sending a media file only the <code>originationPhoneNumberId</code> used to upload the file can be used. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            message: <p>The message to send through WhatsApp. The length is in KB. The message field passes through a WhatsApp Message object, see <a href="https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages">Messages</a> in the <i>WhatsApp Business Platform Cloud API Reference</i>.</p>
            meta_api_version: <p>The API version for the request formatted as <code>v{VersionNumber}</code>. For a list of supported API versions and Amazon Web Services Regions, see <a href="https://docs.aws.amazon.com/general/latest/gr/end-user-messaging.html"> <i>Amazon Web Services End User Messaging Social API</i> Service Endpoints</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.send_whats_app_message_input.SendWhatsAppMessageInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.send_whats_app_message_output.SendWhatsAppMessageOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.send_whats_app_message

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.send_whats_app_message.async_send_whats_app_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.send_whats_app_message_input.SendWhatsAppMessageInput = {
            "origination_phone_number_id": origination_phone_number_id,
            "message": message,
            "meta_api_version": meta_api_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_linked_whats_app_business_account_phone_number(
        self,
        id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        call_settings: "capo_socialmessaging.types.whats_app_call_settings.WhatsAppCallSettings",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_output.UpdateLinkedWhatsAppBusinessAccountPhoneNumberOutput":
        """<p>Updates the calling settings for a linked WhatsApp business phone number, such as whether calling is enabled and the hours during which the business accepts calls.</p>

        Args:
            id: <p>The unique identifier of the phone number to update. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>.</p>
            call_settings: <p>The calling settings to apply to the phone number.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_input.UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_output.UpdateLinkedWhatsAppBusinessAccountPhoneNumberOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.update_linked_whats_app_business_account_phone_number

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.update_linked_whats_app_business_account_phone_number.async_update_linked_whats_app_business_account_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_input.UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput = {
            "id": id,
            "call_settings": call_settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
