"""Generated from Smithy shape ``com.amazonaws.socialmessaging#SocialMessaging``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_socialmessaging._auth._signers
import capo_socialmessaging._auth._sigv4
from capo_socialmessaging._auth._identity import Credentials
from capo_socialmessaging._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_socialmessaging._auth._zapros_handler import AuthMiddleware
from capo_socialmessaging._resources.social_messaging.linked_whats_app_business_account_resource import (
    AsyncLinkedWhatsAppBusinessAccountResource,
)
from capo_socialmessaging._resources.social_messaging.linked_whats_app_phone_number_resource import (
    AsyncLinkedWhatsAppPhoneNumberResource,
)
from capo_socialmessaging._services._aws_config import aaws_config
from capo_socialmessaging._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_socialmessaging.types.arn
    import capo_socialmessaging.types.associate_whats_app_business_account_input
    import capo_socialmessaging.types.associate_whats_app_business_account_output
    import capo_socialmessaging.types.business_public_key_pem
    import capo_socialmessaging.types.create_whats_app_dataset_input
    import capo_socialmessaging.types.create_whats_app_dataset_output
    import capo_socialmessaging.types.create_whats_app_flow_input
    import capo_socialmessaging.types.create_whats_app_flow_output
    import capo_socialmessaging.types.create_whats_app_message_template_from_library_input
    import capo_socialmessaging.types.create_whats_app_message_template_from_library_output
    import capo_socialmessaging.types.create_whats_app_message_template_input
    import capo_socialmessaging.types.create_whats_app_message_template_media_input
    import capo_socialmessaging.types.create_whats_app_message_template_media_output
    import capo_socialmessaging.types.create_whats_app_message_template_output
    import capo_socialmessaging.types.delete_all_languages
    import capo_socialmessaging.types.delete_whats_app_flow_input
    import capo_socialmessaging.types.delete_whats_app_flow_output
    import capo_socialmessaging.types.delete_whats_app_message_media_input
    import capo_socialmessaging.types.delete_whats_app_message_media_output
    import capo_socialmessaging.types.delete_whats_app_message_template_input
    import capo_socialmessaging.types.delete_whats_app_message_template_output
    import capo_socialmessaging.types.deprecate_whats_app_flow_input
    import capo_socialmessaging.types.deprecate_whats_app_flow_output
    import capo_socialmessaging.types.disassociate_whats_app_business_account_input
    import capo_socialmessaging.types.disassociate_whats_app_business_account_output
    import capo_socialmessaging.types.filter
    import capo_socialmessaging.types.get_linked_whats_app_business_account_input
    import capo_socialmessaging.types.get_linked_whats_app_business_account_output
    import capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input
    import capo_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output
    import capo_socialmessaging.types.get_whats_app_business_public_key_input
    import capo_socialmessaging.types.get_whats_app_business_public_key_output
    import capo_socialmessaging.types.get_whats_app_call_permission_input
    import capo_socialmessaging.types.get_whats_app_call_permission_output
    import capo_socialmessaging.types.get_whats_app_flow_input
    import capo_socialmessaging.types.get_whats_app_flow_output
    import capo_socialmessaging.types.get_whats_app_flow_preview_input
    import capo_socialmessaging.types.get_whats_app_flow_preview_output
    import capo_socialmessaging.types.get_whats_app_message_media_input
    import capo_socialmessaging.types.get_whats_app_message_media_output
    import capo_socialmessaging.types.get_whats_app_message_template_input
    import capo_socialmessaging.types.get_whats_app_message_template_output
    import capo_socialmessaging.types.kms_key_arn
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.list_linked_whats_app_business_accounts_input
    import capo_socialmessaging.types.list_linked_whats_app_business_accounts_output
    import capo_socialmessaging.types.list_tags_for_resource_input
    import capo_socialmessaging.types.list_tags_for_resource_output
    import capo_socialmessaging.types.list_whats_app_flow_assets_input
    import capo_socialmessaging.types.list_whats_app_flow_assets_output
    import capo_socialmessaging.types.list_whats_app_flows_input
    import capo_socialmessaging.types.list_whats_app_flows_output
    import capo_socialmessaging.types.list_whats_app_message_templates_input
    import capo_socialmessaging.types.list_whats_app_message_templates_output
    import capo_socialmessaging.types.list_whats_app_template_library_input
    import capo_socialmessaging.types.list_whats_app_template_library_output
    import capo_socialmessaging.types.max_results
    import capo_socialmessaging.types.meta_flow_application_id
    import capo_socialmessaging.types.meta_flow_category_list
    import capo_socialmessaging.types.meta_flow_endpoint_uri
    import capo_socialmessaging.types.meta_flow_id
    import capo_socialmessaging.types.meta_flow_json_blob
    import capo_socialmessaging.types.meta_flow_name
    import capo_socialmessaging.types.meta_library_template
    import capo_socialmessaging.types.meta_parameter_format
    import capo_socialmessaging.types.meta_template_category
    import capo_socialmessaging.types.meta_template_components
    import capo_socialmessaging.types.meta_template_cta_link_tracking_opted_out
    import capo_socialmessaging.types.meta_template_definition
    import capo_socialmessaging.types.meta_template_id
    import capo_socialmessaging.types.meta_template_language
    import capo_socialmessaging.types.meta_template_name
    import capo_socialmessaging.types.next_token
    import capo_socialmessaging.types.post_whats_app_message_media_input
    import capo_socialmessaging.types.post_whats_app_message_media_output
    import capo_socialmessaging.types.publish_whats_app_flow_input
    import capo_socialmessaging.types.publish_whats_app_flow_output
    import capo_socialmessaging.types.put_whats_app_business_account_event_destinations_input
    import capo_socialmessaging.types.put_whats_app_business_account_event_destinations_output
    import capo_socialmessaging.types.put_whats_app_business_public_key_input
    import capo_socialmessaging.types.put_whats_app_business_public_key_output
    import capo_socialmessaging.types.s3_file
    import capo_socialmessaging.types.s3_presigned_url
    import capo_socialmessaging.types.send_whats_app_call_event_input
    import capo_socialmessaging.types.send_whats_app_call_event_output
    import capo_socialmessaging.types.send_whats_app_conversion_event_input
    import capo_socialmessaging.types.send_whats_app_conversion_event_output
    import capo_socialmessaging.types.send_whats_app_message_input
    import capo_socialmessaging.types.send_whats_app_message_output
    import capo_socialmessaging.types.string_list
    import capo_socialmessaging.types.tag_list
    import capo_socialmessaging.types.tag_resource_input
    import capo_socialmessaging.types.tag_resource_output
    import capo_socialmessaging.types.untag_resource_input
    import capo_socialmessaging.types.untag_resource_output
    import capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_input
    import capo_socialmessaging.types.update_linked_whats_app_business_account_phone_number_output
    import capo_socialmessaging.types.update_whats_app_flow_assets_input
    import capo_socialmessaging.types.update_whats_app_flow_assets_output
    import capo_socialmessaging.types.update_whats_app_flow_input
    import capo_socialmessaging.types.update_whats_app_flow_output
    import capo_socialmessaging.types.update_whats_app_message_template_input
    import capo_socialmessaging.types.update_whats_app_message_template_output
    import capo_socialmessaging.types.whats_app_business_account_event_destinations
    import capo_socialmessaging.types.whats_app_business_scoped_user_id
    import capo_socialmessaging.types.whats_app_call_event_blob
    import capo_socialmessaging.types.whats_app_call_settings
    import capo_socialmessaging.types.whats_app_conversion_event_blob
    import capo_socialmessaging.types.whats_app_dataset_id
    import capo_socialmessaging.types.whats_app_destination_phone_number
    import capo_socialmessaging.types.whats_app_media_id
    import capo_socialmessaging.types.whats_app_message_blob
    import capo_socialmessaging.types.whats_app_phone_number_id
    import capo_socialmessaging.types.whats_app_setup_finalization
    import capo_socialmessaging.types.whats_app_signup_callback


class AsyncSocialMessagingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSocialMessagingClient:
    """A client for the ``SocialMessaging`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncSocialMessagingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.linked_whats_app_business_account_resource = (
            AsyncLinkedWhatsAppBusinessAccountResource(self)
        )
        self.linked_whats_app_phone_number_resource = (
            AsyncLinkedWhatsAppPhoneNumberResource(self)
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSocialMessagingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSocialMessagingClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_socialmessaging.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List all tags associated with a resource, such as a phone number or WABA.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to retrieve the tags from.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_socialmessaging.types.arn.Arn",
        tags: "capo_socialmessaging.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.tag_resource_output.TagResourceOutput":
        """<p>Adds or overwrites only the specified tags for the specified resource. When you specify an existing tag key, the value is overwritten with the new value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>The tags to add to the resource.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.tag_resource

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_socialmessaging.types.arn.Arn",
        tag_keys: "capo_socialmessaging.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes the specified tags from a resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The keys of the tags to remove from the resource.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.untag_resource

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_whats_app_business_account(
        self,
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        signup_callback: Optional[
            "capo_socialmessaging.types.whats_app_signup_callback.WhatsAppSignupCallback"
        ] = None,
        setup_finalization: Optional[
            "capo_socialmessaging.types.whats_app_setup_finalization.WhatsAppSetupFinalization"
        ] = None,
    ) -> "capo_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput":
        """<p>This is only used through the Amazon Web Services console during sign-up to associate your WhatsApp Business Account to your Amazon Web Services account.</p>

        Args:
            signup_callback: <p>Contains the callback access token.</p>
            setup_finalization: <p>A JSON object that contains the phone numbers and WhatsApp Business Account to link to your account.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.limit_exceeded_exception.LimitExceededException: <p>The request was denied because it would exceed one or more service quotas or limits.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.associate_whats_app_business_account_input.AssociateWhatsAppBusinessAccountInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.associate_whats_app_business_account

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.associate_whats_app_business_account.async_associate_whats_app_business_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.associate_whats_app_business_account_input.AssociateWhatsAppBusinessAccountInput = {}
        if signup_callback is not None:
            input_["signup_callback"] = signup_callback
        if setup_finalization is not None:
            input_["setup_finalization"] = setup_finalization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_linked_whats_app_business_account(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.get_linked_whats_app_business_account_output.GetLinkedWhatsAppBusinessAccountOutput":
        """<p>Get the details of your linked WhatsApp Business Account.</p>

        Args:
            id: <p>The unique identifier, from Amazon Web Services, of the linked WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.get_linked_whats_app_business_account_input.GetLinkedWhatsAppBusinessAccountInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.get_linked_whats_app_business_account_output.GetLinkedWhatsAppBusinessAccountOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account.async_get_linked_whats_app_business_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_linked_whats_app_business_account_input.GetLinkedWhatsAppBusinessAccountInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_whats_app_business_account(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.disassociate_whats_app_business_account_output.DisassociateWhatsAppBusinessAccountOutput":
        """<p>Disassociate a WhatsApp Business Account (WABA) from your Amazon Web Services account.</p>

        Args:
            id: <p>The unique identifier of your WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.dependency_exception.DependencyException: <p>Thrown when performing an action because a dependency would be broken.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.disassociate_whats_app_business_account_input.DisassociateWhatsAppBusinessAccountInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.disassociate_whats_app_business_account_output.DisassociateWhatsAppBusinessAccountOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.disassociate_whats_app_business_account

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.disassociate_whats_app_business_account.async_disassociate_whats_app_business_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.disassociate_whats_app_business_account_input.DisassociateWhatsAppBusinessAccountInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_linked_whats_app_business_accounts(
        self,
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional["capo_socialmessaging.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_socialmessaging.types.list_linked_whats_app_business_accounts_output.ListLinkedWhatsAppBusinessAccountsOutput":
        """<p>List all WhatsApp Business Accounts linked to your Amazon Web Services account.</p>

        Args:
            next_token: <p>The next token for pagination.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.list_linked_whats_app_business_accounts_input.ListLinkedWhatsAppBusinessAccountsInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.list_linked_whats_app_business_accounts_output.ListLinkedWhatsAppBusinessAccountsOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.list_linked_whats_app_business_accounts

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.list_linked_whats_app_business_accounts.async_list_linked_whats_app_business_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.list_linked_whats_app_business_accounts_input.ListLinkedWhatsAppBusinessAccountsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_whats_app_dataset(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.create_whats_app_dataset_output.CreateWhatsAppDatasetOutput":
        """<p>Creates a Meta Conversions API dataset for a WhatsApp Business Account.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to create a dataset for, formatted as <code>waba-01234567890123456789012345678901</code>.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.create_whats_app_dataset_input.CreateWhatsAppDatasetInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.create_whats_app_dataset_output.CreateWhatsAppDatasetOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.create_whats_app_dataset

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.create_whats_app_dataset.async_create_whats_app_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.create_whats_app_dataset_input.CreateWhatsAppDatasetInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_whats_app_flow(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_name: "capo_socialmessaging.types.meta_flow_name.MetaFlowName",
        categories: "capo_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        flow_json: Optional[
            "capo_socialmessaging.types.meta_flow_json_blob.MetaFlowJsonBlob"
        ] = None,
        publish: Optional[bool] = None,
        clone_flow_id: Optional[
            "capo_socialmessaging.types.meta_flow_id.MetaFlowId"
        ] = None,
        endpoint_uri: Optional[
            "capo_socialmessaging.types.meta_flow_endpoint_uri.MetaFlowEndpointUri"
        ] = None,
    ) -> "capo_socialmessaging.types.create_whats_app_flow_output.CreateWhatsAppFlowOutput":
        """<p>Creates a new WhatsApp Flow. Flows enable businesses to create rich, interactive forms and experiences that users can complete without leaving WhatsApp. The Flow is created in DRAFT status. If <code>publish</code> is set to <code>true</code> and a valid <code>flowJson</code> is provided, the Flow is published immediately.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to associate with this Flow.</p>
            flow_name: <p>The name of the Flow. Must be unique within the WhatsApp Business Account.</p>
            categories: <p>The categories that classify the business purpose of the Flow. At least one category is required.</p>
            flow_json: <p>The Flow JSON definition that describes the screens, components, and logic of the Flow. Maximum size is 10 MB.</p>
            publish: <p>Set to <code>true</code> to publish the Flow immediately after creation. Requires a valid <code>flowJson</code> that passes Meta's validation.</p>
            clone_flow_id: <p>The ID of an existing Flow within the same WhatsApp Business Account to clone.</p>
            endpoint_uri: <p>The HTTPS endpoint that Meta calls for a data exchange Flow.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.create_whats_app_flow_input.CreateWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.create_whats_app_flow_output.CreateWhatsAppFlowOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.create_whats_app_flow

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.create_whats_app_flow.async_create_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.create_whats_app_flow_input.CreateWhatsAppFlowInput = {
            "id": id,
            "flow_name": flow_name,
            "categories": categories,
        }
        if flow_json is not None:
            input_["flow_json"] = flow_json
        if publish is not None:
            input_["publish"] = publish
        if clone_flow_id is not None:
            input_["clone_flow_id"] = clone_flow_id
        if endpoint_uri is not None:
            input_["endpoint_uri"] = endpoint_uri

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_whats_app_message_template(
        self,
        template_definition: "capo_socialmessaging.types.meta_template_definition.MetaTemplateDefinition",
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.create_whats_app_message_template_output.CreateWhatsAppMessageTemplateOutput":
        """<p>Creates a new WhatsApp message template from a custom definition.</p> <note> <p>Amazon Web Services End User Messaging Social does not store any WhatsApp message template content.</p> </note>

        Args:
            template_definition: <p>The complete template definition as a JSON blob.</p>
            id: <p>The ID of the WhatsApp Business Account to associate with this template.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.create_whats_app_message_template_input.CreateWhatsAppMessageTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.create_whats_app_message_template_output.CreateWhatsAppMessageTemplateOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.create_whats_app_message_template

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.create_whats_app_message_template.async_create_whats_app_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.create_whats_app_message_template_input.CreateWhatsAppMessageTemplateInput = {
            "template_definition": template_definition,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_whats_app_message_template_from_library(
        self,
        meta_library_template: "capo_socialmessaging.types.meta_library_template.MetaLibraryTemplate",
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.create_whats_app_message_template_from_library_output.CreateWhatsAppMessageTemplateFromLibraryOutput":
        """<p>Creates a new WhatsApp message template using a template from Meta's template library.</p>

        Args:
            meta_library_template: <p>The template configuration from Meta's library, including customizations for buttons and body text.</p>
            id: <p>The ID of the WhatsApp Business Account to associate with this template.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.create_whats_app_message_template_from_library_input.CreateWhatsAppMessageTemplateFromLibraryInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.create_whats_app_message_template_from_library_output.CreateWhatsAppMessageTemplateFromLibraryOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.create_whats_app_message_template_from_library

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.create_whats_app_message_template_from_library.async_create_whats_app_message_template_from_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.create_whats_app_message_template_from_library_input.CreateWhatsAppMessageTemplateFromLibraryInput = {
            "meta_library_template": meta_library_template,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_whats_app_message_template_media(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        source_s3_file: Optional["capo_socialmessaging.types.s3_file.S3File"] = None,
    ) -> "capo_socialmessaging.types.create_whats_app_message_template_media_output.CreateWhatsAppMessageTemplateMediaOutput":
        """<p>Uploads media for use in a WhatsApp message template.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this media upload.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.create_whats_app_message_template_media_input.CreateWhatsAppMessageTemplateMediaInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.create_whats_app_message_template_media_output.CreateWhatsAppMessageTemplateMediaOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.create_whats_app_message_template_media

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.create_whats_app_message_template_media.async_create_whats_app_message_template_media(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.create_whats_app_message_template_media_input.CreateWhatsAppMessageTemplateMediaInput = {
            "id": id
        }
        if source_s3_file is not None:
            input_["source_s3_file"] = source_s3_file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_whats_app_flow(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.delete_whats_app_flow_output.DeleteWhatsAppFlowOutput":
        """<p>Deletes a WhatsApp Flow permanently. Only Flows in DRAFT status can be deleted. Published or deprecated Flows cannot be deleted.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to delete.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.delete_whats_app_flow_input.DeleteWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.delete_whats_app_flow_output.DeleteWhatsAppFlowOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.delete_whats_app_flow

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.delete_whats_app_flow.async_delete_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.delete_whats_app_flow_input.DeleteWhatsAppFlowInput = {
            "id": id,
            "flow_id": flow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_whats_app_message_template(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        template_name: "capo_socialmessaging.types.meta_template_name.MetaTemplateName",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        meta_template_id: Optional[
            "capo_socialmessaging.types.meta_template_id.MetaTemplateId"
        ] = None,
        delete_all_languages: Optional[
            "capo_socialmessaging.types.delete_all_languages.DeleteAllLanguages"
        ] = None,
    ) -> "capo_socialmessaging.types.delete_whats_app_message_template_output.DeleteWhatsAppMessageTemplateOutput":
        """<p>Deletes a WhatsApp message template.</p>

        Args:
            meta_template_id: <p>The numeric ID of the template assigned by Meta.</p>
            delete_all_languages: <p>If true, deletes all language versions of the template.</p>
            id: <p>The ID of the WhatsApp Business Account associated with this template.</p>
            template_name: <p>The name of the template to delete.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.delete_whats_app_message_template_input.DeleteWhatsAppMessageTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.delete_whats_app_message_template_output.DeleteWhatsAppMessageTemplateOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.delete_whats_app_message_template

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.delete_whats_app_message_template.async_delete_whats_app_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.delete_whats_app_message_template_input.DeleteWhatsAppMessageTemplateInput = {
            "id": id,
            "template_name": template_name,
        }
        if meta_template_id is not None:
            input_["meta_template_id"] = meta_template_id
        if delete_all_languages is not None:
            input_["delete_all_languages"] = delete_all_languages

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deprecate_whats_app_flow(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.deprecate_whats_app_flow_output.DeprecateWhatsAppFlowOutput":
        """<p>Deprecates a published WhatsApp Flow, marking it as no longer recommended for use. The Flow must be in PUBLISHED status. This is an irreversible operation.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to deprecate.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.deprecate_whats_app_flow_input.DeprecateWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.deprecate_whats_app_flow_output.DeprecateWhatsAppFlowOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.deprecate_whats_app_flow

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.deprecate_whats_app_flow.async_deprecate_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.deprecate_whats_app_flow_input.DeprecateWhatsAppFlowInput = {
            "id": id,
            "flow_id": flow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_whats_app_flow(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.get_whats_app_flow_output.GetWhatsAppFlowOutput":
        """<p>Retrieves the metadata and status of a WhatsApp Flow, including validation errors, preview information, and health status.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to retrieve.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.get_whats_app_flow_input.GetWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.get_whats_app_flow_output.GetWhatsAppFlowOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_whats_app_flow

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.get_whats_app_flow.async_get_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_whats_app_flow_input.GetWhatsAppFlowInput = {
            "id": id,
            "flow_id": flow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_whats_app_flow_preview(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        invalidate: Optional[bool] = None,
    ) -> "capo_socialmessaging.types.get_whats_app_flow_preview_output.GetWhatsAppFlowPreviewOutput":
        """<p>Generates a web preview URL for testing a WhatsApp Flow before publishing. Preview URLs expire in 30 days and can be shared with stakeholders for review.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to preview.</p>
            invalidate: <p>Set to <code>true</code> to force generation of a new preview URL. Use this if the previous URL has been compromised or you want a fresh expiration period.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.get_whats_app_flow_preview_input.GetWhatsAppFlowPreviewInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.get_whats_app_flow_preview_output.GetWhatsAppFlowPreviewOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_whats_app_flow_preview

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.get_whats_app_flow_preview.async_get_whats_app_flow_preview(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_whats_app_flow_preview_input.GetWhatsAppFlowPreviewInput = {
            "id": id,
            "flow_id": flow_id,
        }
        if invalidate is not None:
            input_["invalidate"] = invalidate

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_whats_app_message_template(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        meta_template_id: Optional[
            "capo_socialmessaging.types.meta_template_id.MetaTemplateId"
        ] = None,
        template_name: Optional[
            "capo_socialmessaging.types.meta_template_name.MetaTemplateName"
        ] = None,
        template_language_code: Optional[
            "capo_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
        ] = None,
    ) -> "capo_socialmessaging.types.get_whats_app_message_template_output.GetWhatsAppMessageTemplateOutput":
        """<p>Retrieves a specific WhatsApp message template.</p>

        Args:
            meta_template_id: <p>The numeric ID of the template assigned by Meta.</p>
            id: <p>The ID of the WhatsApp Business Account associated with this template.</p>
            template_name: <p>The name of the message template. Use together with <code>templateLanguageCode</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
            template_language_code: <p>The language code of the message template (for example, <code>en</code> or <code>en_US</code>). Use together with <code>templateName</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.get_whats_app_message_template_input.GetWhatsAppMessageTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.get_whats_app_message_template_output.GetWhatsAppMessageTemplateOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.get_whats_app_message_template

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.get_whats_app_message_template.async_get_whats_app_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.get_whats_app_message_template_input.GetWhatsAppMessageTemplateInput = {
            "id": id
        }
        if meta_template_id is not None:
            input_["meta_template_id"] = meta_template_id
        if template_name is not None:
            input_["template_name"] = template_name
        if template_language_code is not None:
            input_["template_language_code"] = template_language_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_whats_app_flow_assets(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional["capo_socialmessaging.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_socialmessaging.types.list_whats_app_flow_assets_output.ListWhatsAppFlowAssetsOutput":
        """<p>Lists the assets (Flow JSON definition) of a WhatsApp Flow with presigned download URLs. Download URLs are generated by Meta and expire after a short period.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow whose assets to list.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.list_whats_app_flow_assets_input.ListWhatsAppFlowAssetsInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.list_whats_app_flow_assets_output.ListWhatsAppFlowAssetsOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.list_whats_app_flow_assets

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.list_whats_app_flow_assets.async_list_whats_app_flow_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.list_whats_app_flow_assets_input.ListWhatsAppFlowAssetsInput = {
            "id": id,
            "flow_id": flow_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_whats_app_flows(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional["capo_socialmessaging.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "capo_socialmessaging.types.list_whats_app_flows_output.ListWhatsAppFlowsOutput"
    ):
        """<p>Lists all WhatsApp Flows for a WhatsApp Business Account. Returns summary information including Flow ID, name, status, and categories.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to list Flows for.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.list_whats_app_flows_input.ListWhatsAppFlowsInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.list_whats_app_flows_output.ListWhatsAppFlowsOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.list_whats_app_flows

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.list_whats_app_flows.async_list_whats_app_flows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.list_whats_app_flows_input.ListWhatsAppFlowsInput = {
            "id": id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_whats_app_message_templates(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional["capo_socialmessaging.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_socialmessaging.types.list_whats_app_message_templates_output.ListWhatsAppMessageTemplatesOutput":
        """<p>Lists WhatsApp message templates for a specific WhatsApp Business Account.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to list templates for.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page (1-100).</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.list_whats_app_message_templates_input.ListWhatsAppMessageTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.list_whats_app_message_templates_output.ListWhatsAppMessageTemplatesOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.list_whats_app_message_templates

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.list_whats_app_message_templates.async_list_whats_app_message_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.list_whats_app_message_templates_input.ListWhatsAppMessageTemplatesInput = {
            "id": id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_whats_app_template_library(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional["capo_socialmessaging.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_socialmessaging.types.max_results.MaxResults"
        ] = None,
        filters: Optional["capo_socialmessaging.types.filter.Filter"] = None,
    ) -> "capo_socialmessaging.types.list_whats_app_template_library_output.ListWhatsAppTemplateLibraryOutput":
        """<p>Lists templates available in Meta's template library for WhatsApp messaging.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page (1-100).</p>
            id: <p>The ID of the WhatsApp Business Account to list library templates for.</p>
            filters: <p>Map of filters to apply (searchKey, topic, usecase, industry, language).</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.list_whats_app_template_library_input.ListWhatsAppTemplateLibraryInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.list_whats_app_template_library_output.ListWhatsAppTemplateLibraryOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.list_whats_app_template_library

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.list_whats_app_template_library.async_list_whats_app_template_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.list_whats_app_template_library_input.ListWhatsAppTemplateLibraryInput = {
            "id": id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def publish_whats_app_flow(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.publish_whats_app_flow_output.PublishWhatsAppFlowOutput":
        """<p>Publishes a WhatsApp Flow, making it available for use in template messages. The Flow must be in DRAFT status with valid Flow JSON that passes Meta's validation. This is an irreversible operation.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to publish.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.publish_whats_app_flow_input.PublishWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.publish_whats_app_flow_output.PublishWhatsAppFlowOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.publish_whats_app_flow

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.publish_whats_app_flow.async_publish_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.publish_whats_app_flow_input.PublishWhatsAppFlowInput = {
            "id": id,
            "flow_id": flow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_whats_app_business_account_event_destinations(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        event_destinations: "capo_socialmessaging.types.whats_app_business_account_event_destinations.WhatsAppBusinessAccountEventDestinations",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.put_whats_app_business_account_event_destinations_output.PutWhatsAppBusinessAccountEventDestinationsOutput":
        """<p>Add an event destination to log event data from WhatsApp for a WhatsApp Business Account (WABA). A WABA can only have one event destination at a time. All resources associated with the WABA use the same event destination.</p>

        Args:
            id: <p>The unique identifier of your WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>
            event_destinations: <p>An array of <code>WhatsAppBusinessAccountEventDestination</code> event destinations.</p>

        Raises:
            capo_socialmessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_socialmessaging.errors.validation_exception.ValidationException: <p>The request contains an invalid parameter value. </p>
            capo_socialmessaging.errors.internal_service_exception.InternalServiceException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the action are not valid.</p>
            capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException: <p>The request was denied due to request throttling.</p>
            capo_socialmessaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_socialmessaging.types.put_whats_app_business_account_event_destinations_input.PutWhatsAppBusinessAccountEventDestinationsInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.put_whats_app_business_account_event_destinations_output.PutWhatsAppBusinessAccountEventDestinationsOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.put_whats_app_business_account_event_destinations

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.put_whats_app_business_account_event_destinations.async_put_whats_app_business_account_event_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.put_whats_app_business_account_event_destinations_input.PutWhatsAppBusinessAccountEventDestinationsInput = {
            "id": id,
            "event_destinations": event_destinations,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_whats_app_conversion_event(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        dataset_id: "capo_socialmessaging.types.whats_app_dataset_id.WhatsAppDatasetId",
        event_data: "capo_socialmessaging.types.whats_app_conversion_event_blob.WhatsAppConversionEventBlob",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.send_whats_app_conversion_event_output.SendWhatsAppConversionEventOutput":
        """<p>Sends a conversion event to Meta's Conversions API for the specified WhatsApp Business Account dataset.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with the dataset, formatted as <code>waba-01234567890123456789012345678901</code>.</p>
            dataset_id: <p>The Meta-generated dataset ID to send the event to.</p>
            event_data: <p>The raw Meta Conversions API event payload as a JSON blob. See <a href="https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event">Meta's server event parameters</a> for the supported format.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.send_whats_app_conversion_event_input.SendWhatsAppConversionEventInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.send_whats_app_conversion_event_output.SendWhatsAppConversionEventOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.send_whats_app_conversion_event

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.send_whats_app_conversion_event.async_send_whats_app_conversion_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.send_whats_app_conversion_event_input.SendWhatsAppConversionEventInput = {
            "id": id,
            "dataset_id": dataset_id,
            "event_data": event_data,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_whats_app_flow(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        flow_name: Optional[
            "capo_socialmessaging.types.meta_flow_name.MetaFlowName"
        ] = None,
        categories: Optional[
            "capo_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList"
        ] = None,
        endpoint_uri: Optional[
            "capo_socialmessaging.types.meta_flow_endpoint_uri.MetaFlowEndpointUri"
        ] = None,
        meta_app_id: Optional[
            "capo_socialmessaging.types.meta_flow_application_id.MetaFlowApplicationId"
        ] = None,
    ) -> "capo_socialmessaging.types.update_whats_app_flow_output.UpdateWhatsAppFlowOutput":
        """<p>Updates the metadata of a WhatsApp Flow, such as its name or categories. This does not update the Flow JSON definition. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UpdateWhatsAppFlowAssets.html">UpdateWhatsAppFlowAssets</a> to update the Flow JSON.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to update.</p>
            flow_name: <p>The updated name for the Flow.</p>
            categories: <p>The updated categories for the Flow.</p>
            endpoint_uri: <p>The updated HTTPS endpoint for a data exchange Flow.</p>
            meta_app_id: <p>The ID of the Meta application to attach to the Flow.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.update_whats_app_flow_input.UpdateWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.update_whats_app_flow_output.UpdateWhatsAppFlowOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.update_whats_app_flow

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.update_whats_app_flow.async_update_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.update_whats_app_flow_input.UpdateWhatsAppFlowInput = {
            "id": id,
            "flow_id": flow_id,
        }
        if flow_name is not None:
            input_["flow_name"] = flow_name
        if categories is not None:
            input_["categories"] = categories
        if endpoint_uri is not None:
            input_["endpoint_uri"] = endpoint_uri
        if meta_app_id is not None:
            input_["meta_app_id"] = meta_app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_whats_app_flow_assets(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId",
        flow_json: "capo_socialmessaging.types.meta_flow_json_blob.MetaFlowJsonBlob",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "capo_socialmessaging.types.update_whats_app_flow_assets_output.UpdateWhatsAppFlowAssetsOutput":
        """<p>Updates the Flow JSON definition (assets) of a WhatsApp Flow. Updating a published Flow's assets reverts it to DRAFT status, requiring re-publishing.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow whose assets to update.</p>
            flow_json: <p>The updated Flow JSON definition. Maximum size is 10 MB.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.update_whats_app_flow_assets_input.UpdateWhatsAppFlowAssetsInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.update_whats_app_flow_assets_output.UpdateWhatsAppFlowAssetsOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.update_whats_app_flow_assets

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.update_whats_app_flow_assets.async_update_whats_app_flow_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.update_whats_app_flow_assets_input.UpdateWhatsAppFlowAssetsInput = {
            "id": id,
            "flow_id": flow_id,
            "flow_json": flow_json,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_whats_app_message_template(
        self,
        id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        meta_template_id: Optional[
            "capo_socialmessaging.types.meta_template_id.MetaTemplateId"
        ] = None,
        template_name: Optional[
            "capo_socialmessaging.types.meta_template_name.MetaTemplateName"
        ] = None,
        template_language_code: Optional[
            "capo_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
        ] = None,
        parameter_format: Optional[
            "capo_socialmessaging.types.meta_parameter_format.MetaParameterFormat"
        ] = None,
        template_category: Optional[
            "capo_socialmessaging.types.meta_template_category.MetaTemplateCategory"
        ] = None,
        template_components: Optional[
            "capo_socialmessaging.types.meta_template_components.MetaTemplateComponents"
        ] = None,
        cta_url_link_tracking_opted_out: Optional[
            "capo_socialmessaging.types.meta_template_cta_link_tracking_opted_out.MetaTemplateCtaLinkTrackingOptedOut"
        ] = None,
    ) -> "capo_socialmessaging.types.update_whats_app_message_template_output.UpdateWhatsAppMessageTemplateOutput":
        """<p>Updates an existing WhatsApp message template.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this template.</p>
            meta_template_id: <p>The numeric ID of the template assigned by Meta.</p>
            template_name: <p>The name of the message template. Use together with <code>templateLanguageCode</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
            template_language_code: <p>The language code of the message template (for example, <code>en</code> or <code>en_US</code>). Use together with <code>templateName</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
            parameter_format: <p>The format specification for parameters in the template, this can be either 'named' or 'positional'.</p>
            template_category: <p>The new category for the template (for example, UTILITY or MARKETING).</p>
            template_components: <p>The updated components of the template as a JSON blob (maximum 3000 characters).</p>
            cta_url_link_tracking_opted_out: <p>When true, disables click tracking for call-to-action URL buttons in the template.</p>

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
            req: "AsyncOperationRequest[capo_socialmessaging.types.update_whats_app_message_template_input.UpdateWhatsAppMessageTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_socialmessaging.types.update_whats_app_message_template_output.UpdateWhatsAppMessageTemplateOutput"
        ]:
            import capo_socialmessaging._operations.social_messaging.update_whats_app_message_template

            (
                output,
                http_response,
            ) = await capo_socialmessaging._operations.social_messaging.update_whats_app_message_template.async_update_whats_app_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_socialmessaging.types.update_whats_app_message_template_input.UpdateWhatsAppMessageTemplateInput = {
            "id": id
        }
        if meta_template_id is not None:
            input_["meta_template_id"] = meta_template_id
        if template_name is not None:
            input_["template_name"] = template_name
        if template_language_code is not None:
            input_["template_language_code"] = template_language_code
        if parameter_format is not None:
            input_["parameter_format"] = parameter_format
        if template_category is not None:
            input_["template_category"] = template_category
        if template_components is not None:
            input_["template_components"] = template_components
        if cta_url_link_tracking_opted_out is not None:
            input_["cta_url_link_tracking_opted_out"] = cta_url_link_tracking_opted_out

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_linked_whats_app_business_account_phone_number(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
