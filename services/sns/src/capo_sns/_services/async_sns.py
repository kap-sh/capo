"""Generated from Smithy shape ``com.amazonaws.sns#AmazonSimpleNotificationService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_sns._auth._signers
import capo_sns._auth._sigv4
from capo_sns._auth._identity import Credentials
from capo_sns._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sns._auth._zapros_handler import AuthMiddleware
from capo_sns._pagination import resolve_path as _resolve_path
from capo_sns._services._aws_config import aaws_config
from capo_sns._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_sns.types.actions_list
    import capo_sns.types.add_permission_input
    import capo_sns.types.amazon_resource_name
    import capo_sns.types.attribute_name
    import capo_sns.types.attribute_value
    import capo_sns.types.authenticate_on_unsubscribe
    import capo_sns.types.boolean
    import capo_sns.types.check_if_phone_number_is_opted_out_input
    import capo_sns.types.check_if_phone_number_is_opted_out_response
    import capo_sns.types.confirm_subscription_input
    import capo_sns.types.confirm_subscription_response
    import capo_sns.types.create_endpoint_response
    import capo_sns.types.create_platform_application_input
    import capo_sns.types.create_platform_application_response
    import capo_sns.types.create_platform_endpoint_input
    import capo_sns.types.create_sms_sandbox_phone_number_input
    import capo_sns.types.create_sms_sandbox_phone_number_result
    import capo_sns.types.create_topic_input
    import capo_sns.types.create_topic_response
    import capo_sns.types.delegates_list
    import capo_sns.types.delete_endpoint_input
    import capo_sns.types.delete_platform_application_input
    import capo_sns.types.delete_sms_sandbox_phone_number_input
    import capo_sns.types.delete_sms_sandbox_phone_number_result
    import capo_sns.types.delete_topic_input
    import capo_sns.types.endpoint
    import capo_sns.types.endpoint2
    import capo_sns.types.get_data_protection_policy_input
    import capo_sns.types.get_data_protection_policy_response
    import capo_sns.types.get_endpoint_attributes_input
    import capo_sns.types.get_endpoint_attributes_response
    import capo_sns.types.get_platform_application_attributes_input
    import capo_sns.types.get_platform_application_attributes_response
    import capo_sns.types.get_sms_attributes_input
    import capo_sns.types.get_sms_attributes_response
    import capo_sns.types.get_sms_sandbox_account_status_input
    import capo_sns.types.get_sms_sandbox_account_status_result
    import capo_sns.types.get_subscription_attributes_input
    import capo_sns.types.get_subscription_attributes_response
    import capo_sns.types.get_topic_attributes_input
    import capo_sns.types.get_topic_attributes_response
    import capo_sns.types.label
    import capo_sns.types.language_code_string
    import capo_sns.types.list_endpoints_by_platform_application_input
    import capo_sns.types.list_endpoints_by_platform_application_response
    import capo_sns.types.list_origination_numbers_request
    import capo_sns.types.list_origination_numbers_result
    import capo_sns.types.list_phone_numbers_opted_out_input
    import capo_sns.types.list_phone_numbers_opted_out_response
    import capo_sns.types.list_platform_applications_input
    import capo_sns.types.list_platform_applications_response
    import capo_sns.types.list_sms_sandbox_phone_numbers_input
    import capo_sns.types.list_sms_sandbox_phone_numbers_result
    import capo_sns.types.list_string
    import capo_sns.types.list_subscriptions_by_topic_input
    import capo_sns.types.list_subscriptions_by_topic_response
    import capo_sns.types.list_subscriptions_input
    import capo_sns.types.list_subscriptions_response
    import capo_sns.types.list_tags_for_resource_request
    import capo_sns.types.list_tags_for_resource_response
    import capo_sns.types.list_topics_input
    import capo_sns.types.list_topics_response
    import capo_sns.types.map_string_to_string
    import capo_sns.types.max_items
    import capo_sns.types.max_items_list_origination_numbers
    import capo_sns.types.message
    import capo_sns.types.message_attribute_map
    import capo_sns.types.message_structure
    import capo_sns.types.next_token
    import capo_sns.types.opt_in_phone_number_input
    import capo_sns.types.opt_in_phone_number_response
    import capo_sns.types.otp_code
    import capo_sns.types.phone_number
    import capo_sns.types.phone_number_information
    import capo_sns.types.phone_number_string
    import capo_sns.types.platform_application
    import capo_sns.types.protocol
    import capo_sns.types.publish_batch_input
    import capo_sns.types.publish_batch_request_entry_list
    import capo_sns.types.publish_batch_response
    import capo_sns.types.publish_input
    import capo_sns.types.publish_response
    import capo_sns.types.put_data_protection_policy_input
    import capo_sns.types.remove_permission_input
    import capo_sns.types.set_endpoint_attributes_input
    import capo_sns.types.set_platform_application_attributes_input
    import capo_sns.types.set_sms_attributes_input
    import capo_sns.types.set_sms_attributes_response
    import capo_sns.types.set_subscription_attributes_input
    import capo_sns.types.set_topic_attributes_input
    import capo_sns.types.sms_sandbox_phone_number
    import capo_sns.types.string
    import capo_sns.types.subject
    import capo_sns.types.subscribe_input
    import capo_sns.types.subscribe_response
    import capo_sns.types.subscription
    import capo_sns.types.subscription_arn
    import capo_sns.types.subscription_attributes_map
    import capo_sns.types.tag_key_list
    import capo_sns.types.tag_list
    import capo_sns.types.tag_resource_request
    import capo_sns.types.tag_resource_response
    import capo_sns.types.token
    import capo_sns.types.topic
    import capo_sns.types.topic_arn
    import capo_sns.types.topic_attributes_map
    import capo_sns.types.topic_name
    import capo_sns.types.unsubscribe_input
    import capo_sns.types.untag_resource_request
    import capo_sns.types.untag_resource_response
    import capo_sns.types.verify_sms_sandbox_phone_number_input
    import capo_sns.types.verify_sms_sandbox_phone_number_result


class AsyncSNSClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSNSClient:
    """A client for the ``SNS`` service.

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
        self._config = AsyncSNSClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSNSClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSNSClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def add_permission(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        label: "capo_sns.types.label.label",
        aws_account_id: "capo_sns.types.delegates_list.DelegatesList",
        action_name: "capo_sns.types.actions_list.ActionsList",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> None:
        """<p>Adds a statement to a topic's access control policy, granting access for the specified Amazon Web Services accounts to the specified actions.</p> <note> <p>To remove the ability to change topic permissions, you must deny permissions to the <code>AddPermission</code>, <code>RemovePermission</code>, and <code>SetTopicAttributes</code> actions in your IAM policy.</p> </note>

        Args:
            topic_arn: <p>The ARN of the topic whose access control policy you wish to modify.</p>
            label: <p>A unique identifier for the new policy statement.</p>
            aws_account_id: <p>The Amazon Web Services account IDs of the users (principals) who will be given access to the specified actions. The users must have Amazon Web Services account, but do not need to be signed up for this service.</p>
            action_name: <p>The action you want to allow for the specified principal(s).</p> <p>Valid values: Any Amazon SNS action name, for example <code>Publish</code>.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.add_permission_input.AddPermissionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.add_permission

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.add_permission.async_add_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.add_permission_input.AddPermissionInput = {
            "topic_arn": topic_arn,
            "label": label,
            "aws_account_id": aws_account_id,
            "action_name": action_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def check_if_phone_number_is_opted_out(
        self,
        phone_number: "capo_sns.types.phone_number.PhoneNumber",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.check_if_phone_number_is_opted_out_response.CheckIfPhoneNumberIsOptedOutResponse":
        """<p>Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your Amazon Web Services account. You cannot send SMS messages to a number that is opted out.</p> <p>To resume sending messages, you can opt in the number by using the <code>OptInPhoneNumber</code> action.</p>

        Args:
            phone_number: <p>The phone number for which you want to check the opt out status.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.check_if_phone_number_is_opted_out_input.CheckIfPhoneNumberIsOptedOutInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.check_if_phone_number_is_opted_out_response.CheckIfPhoneNumberIsOptedOutResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.check_if_phone_number_is_opted_out

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.check_if_phone_number_is_opted_out.async_check_if_phone_number_is_opted_out(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.check_if_phone_number_is_opted_out_input.CheckIfPhoneNumberIsOptedOutInput = {
            "phone_number": phone_number
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def confirm_subscription(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        token: "capo_sns.types.token.token",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        authenticate_on_unsubscribe: Optional[
            "capo_sns.types.authenticate_on_unsubscribe.authenticateOnUnsubscribe"
        ] = None,
    ) -> "capo_sns.types.confirm_subscription_response.ConfirmSubscriptionResponse":
        """<p>Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier <code>Subscribe</code> action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the <code>AuthenticateOnUnsubscribe</code> flag is set to "true".</p>

        Args:
            topic_arn: <p>The ARN of the topic for which you wish to confirm a subscription.</p>
            token: <p>Short-lived token sent to an endpoint during the <code>Subscribe</code> action.</p>
            authenticate_on_unsubscribe: <p>Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is <code>true</code> and the request has an Amazon Web Services signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires Amazon Web Services authentication. </p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.filter_policy_limit_exceeded_exception.FilterPolicyLimitExceededException: <p>Indicates that the number of filter polices in your Amazon Web Services account exceeds the limit. To add more filter polices, submit an Amazon SNS Limit Increase case in the Amazon Web Services Support Center.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.replay_limit_exceeded_exception.ReplayLimitExceededException: <p>Indicates that the request parameter has exceeded the maximum number of concurrent message replays.</p>
            capo_sns.errors.subscription_limit_exceeded_exception.SubscriptionLimitExceededException: <p>Indicates that the customer already owns the maximum allowed number of subscriptions.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.confirm_subscription_input.ConfirmSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.confirm_subscription_response.ConfirmSubscriptionResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.confirm_subscription

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.confirm_subscription.async_confirm_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.confirm_subscription_input.ConfirmSubscriptionInput = {
            "topic_arn": topic_arn,
            "token": token,
        }
        if authenticate_on_unsubscribe is not None:
            input_["authenticate_on_unsubscribe"] = authenticate_on_unsubscribe

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_platform_application(
        self,
        name: "capo_sns.types.string.String",
        platform: "capo_sns.types.string.String",
        attributes: "capo_sns.types.map_string_to_string.MapStringToString",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.create_platform_application_response.CreatePlatformApplicationResponse":
        """<p>Creates a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging), to which devices and mobile apps may register. You must specify <code>PlatformPrincipal</code> and <code>PlatformCredential</code> attributes when using the <code>CreatePlatformApplication</code> action.</p> <p> <code>PlatformPrincipal</code> and <code>PlatformCredential</code> are received from the notification service.</p> <ul> <li> <p>For ADM, <code>PlatformPrincipal</code> is <code>client id</code> and <code>PlatformCredential</code> is <code>client secret</code>.</p> </li> <li> <p>For APNS and <code>APNS_SANDBOX</code> using certificate credentials, <code>PlatformPrincipal</code> is <code>SSL certificate</code> and <code>PlatformCredential</code> is <code>private key</code>.</p> </li> <li> <p>For APNS and <code>APNS_SANDBOX</code> using token credentials, <code>PlatformPrincipal</code> is <code>signing key ID</code> and <code>PlatformCredential</code> is <code>signing key</code>.</p> </li> <li> <p>For Baidu, <code>PlatformPrincipal</code> is <code>API key</code> and <code>PlatformCredential</code> is <code>secret key</code>.</p> </li> <li> <p>For GCM (Firebase Cloud Messaging) using key credentials, there is no <code>PlatformPrincipal</code>. The <code>PlatformCredential</code> is <code>API key</code>.</p> </li> <li> <p>For GCM (Firebase Cloud Messaging) using token credentials, there is no <code>PlatformPrincipal</code>. The <code>PlatformCredential</code> is a JSON formatted private key file. When using the Amazon Web Services CLI or Amazon Web Services SDKs, the file must be in string format and special characters must be ignored. To format the file correctly, Amazon SNS recommends using the following command: <code>SERVICE_JSON=$(jq @json < service.json)</code>.</p> </li> <li> <p>For MPNS, <code>PlatformPrincipal</code> is <code>TLS certificate</code> and <code>PlatformCredential</code> is <code>private key</code>.</p> </li> <li> <p>For WNS, <code>PlatformPrincipal</code> is <code>Package Security Identifier</code> and <code>PlatformCredential</code> is <code>secret key</code>.</p> </li> </ul> <p>You can use the returned <code>PlatformApplicationArn</code> as an attribute for the <code>CreatePlatformEndpoint</code> action.</p>

        Args:
            name: <p>Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.</p>
            platform: <p>The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Firebase Cloud Messaging).</p>
            attributes: <p>For a list of attributes, see <a href="https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html"> <code>SetPlatformApplicationAttributes</code> </a>.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.create_platform_application_input.CreatePlatformApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.create_platform_application_response.CreatePlatformApplicationResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.create_platform_application

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.create_platform_application.async_create_platform_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.create_platform_application_input.CreatePlatformApplicationInput = {
            "name": name,
            "platform": platform,
            "attributes": attributes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_platform_endpoint(
        self,
        platform_application_arn: "capo_sns.types.string.String",
        token: "capo_sns.types.string.String",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        custom_user_data: Optional["capo_sns.types.string.String"] = None,
        attributes: Optional[
            "capo_sns.types.map_string_to_string.MapStringToString"
        ] = None,
    ) -> "capo_sns.types.create_endpoint_response.CreateEndpointResponse":
        """<p>Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. <code>CreatePlatformEndpoint</code> requires the <code>PlatformApplicationArn</code> that is returned from <code>CreatePlatformApplication</code>. You can use the returned <code>EndpointArn</code> to send a message to a mobile app or by the <code>Subscribe</code> action for subscription to a topic. The <code>CreatePlatformEndpoint</code> action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint's ARN is returned without creating a new endpoint. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html">Using Amazon SNS Mobile Push Notifications</a>. </p> <p>When using <code>CreatePlatformEndpoint</code> with Baidu, two attributes must be provided: ChannelId and UserId. The token field must also contain the ChannelId. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePushBaiduEndpoint.html">Creating an Amazon SNS Endpoint for Baidu</a>. </p>

        Args:
            platform_application_arn: <p> <code>PlatformApplicationArn</code> returned from CreatePlatformApplication is used to create a an endpoint.</p>
            token: <p>Unique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using GCM (Firebase Cloud Messaging) or ADM, the device token equivalent is called the registration ID.</p>
            custom_user_data: <p>Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.</p>
            attributes: <p>For a list of attributes, see <a href="https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html"> <code>SetEndpointAttributes</code> </a>.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.create_platform_endpoint_input.CreatePlatformEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.create_endpoint_response.CreateEndpointResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.create_platform_endpoint

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.create_platform_endpoint.async_create_platform_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.create_platform_endpoint_input.CreatePlatformEndpointInput = {
            "platform_application_arn": platform_application_arn,
            "token": token,
        }
        if custom_user_data is not None:
            input_["custom_user_data"] = custom_user_data
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_sms_sandbox_phone_number(
        self,
        phone_number: "capo_sns.types.phone_number_string.PhoneNumberString",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        language_code: Optional[
            "capo_sns.types.language_code_string.LanguageCodeString"
        ] = None,
    ) -> "capo_sns.types.create_sms_sandbox_phone_number_result.CreateSMSSandboxPhoneNumberResult":
        """<p>Adds a destination phone number to an Amazon Web Services account in the SMS sandbox and sends a one-time password (OTP) to that phone number.</p> <p>When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the <i>SMS sandbox</i>. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html">SMS sandbox</a> in the <i>Amazon SNS Developer Guide</i>.</p>

        Args:
            phone_number: <p>The destination phone number to verify. On verification, Amazon SNS adds this phone number to the list of verified phone numbers that you can send SMS messages to.</p>
            language_code: <p>The language to use for sending the OTP. The default value is <code>en-US</code>.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.opted_out_exception.OptedOutException: <p>Indicates that the specified phone number opted out of receiving SMS messages from your Amazon Web Services account. You can't send SMS messages to phone numbers that opt out.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.user_error_exception.UserErrorException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.create_sms_sandbox_phone_number_input.CreateSMSSandboxPhoneNumberInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.create_sms_sandbox_phone_number_result.CreateSMSSandboxPhoneNumberResult"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.create_sms_sandbox_phone_number

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.create_sms_sandbox_phone_number.async_create_sms_sandbox_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.create_sms_sandbox_phone_number_input.CreateSMSSandboxPhoneNumberInput = {
            "phone_number": phone_number
        }
        if language_code is not None:
            input_["language_code"] = language_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_topic(
        self,
        name: "capo_sns.types.topic_name.topicName",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        attributes: Optional[
            "capo_sns.types.topic_attributes_map.TopicAttributesMap"
        ] = None,
        tags: Optional["capo_sns.types.tag_list.TagList"] = None,
        data_protection_policy: Optional[
            "capo_sns.types.attribute_value.attributeValue"
        ] = None,
    ) -> "capo_sns.types.create_topic_response.CreateTopicResponse":
        """<p>Creates a topic to which notifications can be published. Users can create at most 100,000 standard topics (at most 1,000 FIFO topics). For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html">Creating an Amazon SNS topic</a> in the <i>Amazon SNS Developer Guide</i>. This action is idempotent, so if the requester already owns a topic with the specified name, that topic's ARN is returned without creating a new topic.</p>

        Args:
            name: <p>The name of the topic you want to create.</p> <p>Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.</p> <p>For a FIFO (first-in-first-out) topic, the name must end with the <code>.fifo</code> suffix. </p>
            attributes: <p>A map of attributes with their corresponding values.</p> <p>The following lists names, descriptions, and values of the special request parameters that the <code>CreateTopic</code> action uses:</p> <ul> <li> <p> <code>DeliveryPolicy</code> – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.</p> </li> <li> <p> <code>DisplayName</code> – The display name to use for a topic with SMS, <code>email</code>, and <code>email-json</code> subscriptions. For <code>email</code> and <code>email-json</code> subscriptions, the display name is used as the sender name for regular notification messages. Subscription confirmation and unsubscribe confirmation emails always use "Amazon Web Services Notifications" as the sender name.</p> </li> <li> <p> <code>MaximumMessageSize</code> – The maximum size, in bytes, of a message that can be published to the topic. Valid values are <code>1024</code> to <code>1048576</code> (1 MiB). The default is <code>262144</code> (256 KiB).</p> <p>A topic with a <code>MaximumMessageSize</code> above 256 KiB must have 100 or fewer subscriptions, and each subscription must be an Amazon SQS, Amazon Data Firehose, or Lambda subscription.</p> </li> <li> <p> <code>Policy</code> – The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.</p> </li> <li> <p> <code>TracingConfig</code> – Tracing mode of an Amazon SNS topic. By default <code>TracingConfig</code> is set to <code>PassThrough</code>, and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to <code>Active</code>, Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. This is only supported on standard topics.</p> </li> <li> <p>HTTP</p> <ul> <li> <p> <code>HTTPSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint. </p> </li> <li> <p> <code>HTTPSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an HTTP endpoint.</p> </li> <li> <p> <code>HTTPFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint.</p> </li> </ul> </li> <li> <p>Amazon Data Firehose</p> <ul> <li> <p> <code>FirehoseSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint.</p> </li> <li> <p> <code>FirehoseSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint.</p> </li> <li> <p> <code>FirehoseFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint. </p> </li> </ul> </li> <li> <p>Lambda</p> <ul> <li> <p> <code>LambdaSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Lambda endpoint.</p> </li> <li> <p> <code>LambdaSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Lambda endpoint.</p> </li> <li> <p> <code>LambdaFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Lambda endpoint. </p> </li> </ul> </li> <li> <p>Platform application endpoint</p> <ul> <li> <p> <code>ApplicationSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to a platform application endpoint.</p> </li> <li> <p> <code>ApplicationSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an platform application endpoint.</p> </li> <li> <p> <code>ApplicationFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an platform application endpoint.</p> </li> </ul> <note> <p>In addition to being able to configure topic attributes for message delivery status of notification messages sent to Amazon SNS application endpoints, you can also configure application attributes for the delivery status of push notification messages sent to push notification services.</p> <p>For example, For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html">Using Amazon SNS Application Attributes for Message Delivery Status</a>. </p> </note> </li> <li> <p>Amazon SQS</p> <ul> <li> <p> <code>SQSSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p> </li> <li> <p> <code>SQSSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p> </li> <li> <p> <code>SQSFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p> </li> </ul> </li> </ul> <note> <p>The <ENDPOINT>SuccessFeedbackRoleArn and <ENDPOINT>FailureFeedbackRoleArn attributes are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The <ENDPOINT>SuccessFeedbackSampleRate attribute is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the <ENDPOINT>FailureFeedbackRoleArn attribute, then all failed message deliveries generate CloudWatch Logs. </p> </note> <p>The following attribute applies only to <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html">server-side encryption</a>:</p> <ul> <li> <p> <code>KmsMasterKeyId</code> – The ID of an Amazon Web Services managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms">Key Terms</a>. For more examples, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters">KeyId</a> in the <i>Key Management Service API Reference</i>. </p> </li> </ul> <p>The following attributes apply only to <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html">FIFO topics</a>:</p> <ul> <li> <p> <code>ArchivePolicy</code> – The policy that sets the retention period for messages stored in the message archive of an Amazon SNS FIFO topic.</p> </li> <li> <p> <code>ContentBasedDeduplication</code> – Enables content-based deduplication for FIFO topics.</p> <ul> <li> <p>By default, <code>ContentBasedDeduplication</code> is set to <code>false</code>. If you create a FIFO topic and this attribute is <code>false</code>, you must specify a value for the <code>MessageDeduplicationId</code> parameter for the <a href="https://docs.aws.amazon.com/sns/latest/api/API_Publish.html">Publish</a> action. </p> </li> <li> <p>When you set <code>ContentBasedDeduplication</code> to <code>true</code>, Amazon SNS uses a SHA-256 hash to generate the <code>MessageDeduplicationId</code> using the body of the message (but not the attributes of the message).</p> <p>(Optional) To override the generated value, you can specify a value for the <code>MessageDeduplicationId</code> parameter for the <code>Publish</code> action.</p> </li> </ul> </li> </ul> <ul> <li> <p> <code>FifoThroughputScope</code> – Enables higher throughput for your FIFO topic by adjusting the scope of deduplication. This attribute has two possible values:</p> <ul> <li> <p> <code>Topic</code> – The scope of message deduplication is across the entire topic. This is the default value and maintains existing behavior, with a maximum throughput of 3000 messages per second or 20MB per second, whichever comes first.</p> </li> <li> <p> <code>MessageGroup</code> – The scope of deduplication is within each individual message group, which enables higher throughput per topic subject to regional quotas. For more information on quotas or to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/sns.html">Amazon SNS service quotas</a> in the Amazon Web Services General Reference.</p> </li> </ul> </li> </ul>
            tags: <p>The list of tags to add to a new topic.</p> <note> <p>To be able to tag a topic on creation, you must have the <code>sns:CreateTopic</code> and <code>sns:TagResource</code> permissions.</p> </note>
            data_protection_policy: <important> <p>Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html">Amazon SNS message data protection availability change</a>.</p> </important> <p>The body of the policy document you want to use for this topic.</p> <p>You can only add one policy per topic.</p> <p>The policy must be in JSON string format.</p> <p>Length Constraints: Maximum length of 30,720.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.concurrent_access_exception.ConcurrentAccessException: <p>Can't perform multiple operations on a tag simultaneously. Perform the operations sequentially.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_security_exception.InvalidSecurityException: <p>The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.</p>
            capo_sns.errors.stale_tag_exception.StaleTagException: <p>A tag has been added to a resource with the same ARN as a deleted resource. Wait a short while and then retry the operation.</p>
            capo_sns.errors.tag_limit_exceeded_exception.TagLimitExceededException: <p>Can't add more than 50 tags to a topic.</p>
            capo_sns.errors.tag_policy_exception.TagPolicyException: <p>The request doesn't comply with the IAM tag policy. Correct your request and then retry it.</p>
            capo_sns.errors.topic_limit_exceeded_exception.TopicLimitExceededException: <p>Indicates that the customer already owns the maximum allowed number of topics.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.create_topic_input.CreateTopicInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.create_topic_response.CreateTopicResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.create_topic

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.create_topic.async_create_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.create_topic_input.CreateTopicInput = {"name": name}
        if attributes is not None:
            input_["attributes"] = attributes
        if tags is not None:
            input_["tags"] = tags
        if data_protection_policy is not None:
            input_["data_protection_policy"] = data_protection_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_endpoint(
        self,
        endpoint_arn: "capo_sns.types.string.String",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> None:
        """<p>Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html">Using Amazon SNS Mobile Push Notifications</a>. </p> <p>When you delete an endpoint that is also subscribed to a topic, then you must also unsubscribe the endpoint from the topic.</p>

        Args:
            endpoint_arn: <p> <code>EndpointArn</code> of endpoint to delete.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.delete_endpoint_input.DeleteEndpointInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.delete_endpoint

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.delete_endpoint.async_delete_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.delete_endpoint_input.DeleteEndpointInput = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_platform_application(
        self,
        platform_application_arn: "capo_sns.types.string.String",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> None:
        """<p>Deletes a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html">Using Amazon SNS Mobile Push Notifications</a>. </p>

        Args:
            platform_application_arn: <p> <code>PlatformApplicationArn</code> of platform application object to delete.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.delete_platform_application_input.DeletePlatformApplicationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.delete_platform_application

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.delete_platform_application.async_delete_platform_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.delete_platform_application_input.DeletePlatformApplicationInput = {
            "platform_application_arn": platform_application_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_sms_sandbox_phone_number(
        self,
        phone_number: "capo_sns.types.phone_number_string.PhoneNumberString",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.delete_sms_sandbox_phone_number_result.DeleteSMSSandboxPhoneNumberResult":
        """<p>Deletes an Amazon Web Services account's verified or pending phone number from the SMS sandbox.</p> <p>When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the <i>SMS sandbox</i>. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html">SMS sandbox</a> in the <i>Amazon SNS Developer Guide</i>.</p>

        Args:
            phone_number: <p>The destination phone number to delete.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.resource_not_found_exception.ResourceNotFoundException: <p>Can’t perform the action on the specified resource. Make sure that the resource exists.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.user_error_exception.UserErrorException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.delete_sms_sandbox_phone_number_input.DeleteSMSSandboxPhoneNumberInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.delete_sms_sandbox_phone_number_result.DeleteSMSSandboxPhoneNumberResult"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.delete_sms_sandbox_phone_number

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.delete_sms_sandbox_phone_number.async_delete_sms_sandbox_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.delete_sms_sandbox_phone_number_input.DeleteSMSSandboxPhoneNumberInput = {
            "phone_number": phone_number
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_topic(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> None:
        """<p>Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.</p>

        Args:
            topic_arn: <p>The ARN of the topic you want to delete.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.concurrent_access_exception.ConcurrentAccessException: <p>Can't perform multiple operations on a tag simultaneously. Perform the operations sequentially.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_state_exception.InvalidStateException: <p>Indicates that the specified state is not a valid state for an event source.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.stale_tag_exception.StaleTagException: <p>A tag has been added to a resource with the same ARN as a deleted resource. Wait a short while and then retry the operation.</p>
            capo_sns.errors.tag_policy_exception.TagPolicyException: <p>The request doesn't comply with the IAM tag policy. Correct your request and then retry it.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.delete_topic_input.DeleteTopicInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.delete_topic

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.delete_topic.async_delete_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.delete_topic_input.DeleteTopicInput = {
            "topic_arn": topic_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_protection_policy(
        self,
        resource_arn: "capo_sns.types.topic_arn.topicARN",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.get_data_protection_policy_response.GetDataProtectionPolicyResponse":
        """<important> <p>Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html">Amazon SNS message data protection availability change</a>.</p> </important> <p>Retrieves the specified inline <code>DataProtectionPolicy</code> document that is stored in the specified Amazon SNS topic. </p>

        Args:
            resource_arn: <p>The ARN of the topic whose <code>DataProtectionPolicy</code> you want to get.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the Amazon Web Services General Reference.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_security_exception.InvalidSecurityException: <p>The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.get_data_protection_policy_input.GetDataProtectionPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.get_data_protection_policy_response.GetDataProtectionPolicyResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.get_data_protection_policy

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.get_data_protection_policy.async_get_data_protection_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.get_data_protection_policy_input.GetDataProtectionPolicyInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_endpoint_attributes(
        self,
        endpoint_arn: "capo_sns.types.string.String",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> (
        "capo_sns.types.get_endpoint_attributes_response.GetEndpointAttributesResponse"
    ):
        """<p>Retrieves the endpoint attributes for a device on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html">Using Amazon SNS Mobile Push Notifications</a>. </p>

        Args:
            endpoint_arn: <p> <code>EndpointArn</code> for <code>GetEndpointAttributes</code> input.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.get_endpoint_attributes_input.GetEndpointAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.get_endpoint_attributes_response.GetEndpointAttributesResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.get_endpoint_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.get_endpoint_attributes.async_get_endpoint_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.get_endpoint_attributes_input.GetEndpointAttributesInput = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_platform_application_attributes(
        self,
        platform_application_arn: "capo_sns.types.string.String",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.get_platform_application_attributes_response.GetPlatformApplicationAttributesResponse":
        """<p>Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html">Using Amazon SNS Mobile Push Notifications</a>. </p>

        Args:
            platform_application_arn: <p> <code>PlatformApplicationArn</code> for GetPlatformApplicationAttributesInput.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.get_platform_application_attributes_input.GetPlatformApplicationAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.get_platform_application_attributes_response.GetPlatformApplicationAttributesResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.get_platform_application_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.get_platform_application_attributes.async_get_platform_application_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.get_platform_application_attributes_input.GetPlatformApplicationAttributesInput = {
            "platform_application_arn": platform_application_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_sms_attributes(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        attributes: Optional["capo_sns.types.list_string.ListString"] = None,
    ) -> "capo_sns.types.get_sms_attributes_response.GetSMSAttributesResponse":
        """<p>Returns the settings for sending SMS messages from your Amazon Web Services account.</p> <p>These settings are set with the <code>SetSMSAttributes</code> action.</p>

        Args:
            attributes: <p>A list of the individual attribute names, such as <code>MonthlySpendLimit</code>, for which you want values.</p> <p>For all attribute names, see <a href="https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html">SetSMSAttributes</a>.</p> <p>If you don't use this parameter, Amazon SNS returns all SMS attributes.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.get_sms_attributes_input.GetSMSAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.get_sms_attributes_response.GetSMSAttributesResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.get_sms_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.get_sms_attributes.async_get_sms_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.get_sms_attributes_input.GetSMSAttributesInput = {}
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_sms_sandbox_account_status(
        self, *, config_overrides: Optional[AsyncSNSClientConfig] = None
    ) -> "capo_sns.types.get_sms_sandbox_account_status_result.GetSMSSandboxAccountStatusResult":
        """<p>Retrieves the SMS sandbox status for the calling Amazon Web Services account in the target Amazon Web Services Region.</p> <p>When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the <i>SMS sandbox</i>. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html">SMS sandbox</a> in the <i>Amazon SNS Developer Guide</i>.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.get_sms_sandbox_account_status_input.GetSMSSandboxAccountStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.get_sms_sandbox_account_status_result.GetSMSSandboxAccountStatusResult"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.get_sms_sandbox_account_status

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.get_sms_sandbox_account_status.async_get_sms_sandbox_account_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.get_sms_sandbox_account_status_input.GetSMSSandboxAccountStatusInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subscription_attributes(
        self,
        subscription_arn: "capo_sns.types.subscription_arn.subscriptionARN",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.get_subscription_attributes_response.GetSubscriptionAttributesResponse":
        """<p>Returns all of the properties of a subscription.</p>

        Args:
            subscription_arn: <p>The ARN of the subscription whose properties you want to get.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.get_subscription_attributes_input.GetSubscriptionAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.get_subscription_attributes_response.GetSubscriptionAttributesResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.get_subscription_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.get_subscription_attributes.async_get_subscription_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.get_subscription_attributes_input.GetSubscriptionAttributesInput = {
            "subscription_arn": subscription_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_topic_attributes(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.get_topic_attributes_response.GetTopicAttributesResponse":
        """<p>Returns all of the properties of a topic. Topic properties returned might differ based on the authorization of the user.</p>

        Args:
            topic_arn: <p>The ARN of the topic whose properties you want to get.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_security_exception.InvalidSecurityException: <p>The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.get_topic_attributes_input.GetTopicAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.get_topic_attributes_response.GetTopicAttributesResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.get_topic_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.get_topic_attributes.async_get_topic_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.get_topic_attributes_input.GetTopicAttributesInput = {
            "topic_arn": topic_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_endpoints_by_platform_application(
        self,
        platform_application_arn: "capo_sns.types.string.String",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.string.String"] = None,
    ) -> "capo_sns.types.list_endpoints_by_platform_application_response.ListEndpointsByPlatformApplicationResponse":
        """<p>Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM (Firebase Cloud Messaging) and APNS. The results for <code>ListEndpointsByPlatformApplication</code> are paginated and return a limited list of endpoints, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call <code>ListEndpointsByPlatformApplication</code> again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html">Using Amazon SNS Mobile Push Notifications</a>. </p> <p>This action is throttled at 30 transactions per second (TPS).</p>

        Args:
            platform_application_arn: <p> <code>PlatformApplicationArn</code> for <code>ListEndpointsByPlatformApplicationInput</code> action.</p>
            next_token: <p> <code>NextToken</code> string is used when calling <code>ListEndpointsByPlatformApplication</code> action to retrieve additional records that are available after the first page results.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.list_endpoints_by_platform_application_input.ListEndpointsByPlatformApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.list_endpoints_by_platform_application_response.ListEndpointsByPlatformApplicationResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.list_endpoints_by_platform_application

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.list_endpoints_by_platform_application.async_list_endpoints_by_platform_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.list_endpoints_by_platform_application_input.ListEndpointsByPlatformApplicationInput = {
            "platform_application_arn": platform_application_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_endpoints_by_platform_application(
        self,
        platform_application_arn: "capo_sns.types.string.String",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.string.String"] = None,
    ) -> "AsyncIterator[capo_sns.types.endpoint.Endpoint]":
        _token = next_token
        while True:
            _response = await self.list_endpoints_by_platform_application(
                platform_application_arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_origination_numbers(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_sns.types.max_items_list_origination_numbers.MaxItemsListOriginationNumbers"
        ] = None,
    ) -> "capo_sns.types.list_origination_numbers_result.ListOriginationNumbersResult":
        """<p>Lists the calling Amazon Web Services account's dedicated origination numbers and their metadata. For more information about origination numbers, see <a href="https://docs.aws.amazon.com/sns/latest/dg/channels-sms-originating-identities-origination-numbers.html">Origination numbers</a> in the <i>Amazon SNS Developer Guide</i>.</p>

        Args:
            next_token: <p>Token that the previous <code>ListOriginationNumbers</code> request returns.</p>
            max_results: <p>The maximum number of origination numbers to return.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.validation_exception.ValidationException: <p>Indicates that a parameter in the request is invalid.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.list_origination_numbers_request.ListOriginationNumbersRequest]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.list_origination_numbers_result.ListOriginationNumbersResult"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.list_origination_numbers

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.list_origination_numbers.async_list_origination_numbers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.list_origination_numbers_request.ListOriginationNumbersRequest = {}
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

    async def iter_list_origination_numbers(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_sns.types.max_items_list_origination_numbers.MaxItemsListOriginationNumbers"
        ] = None,
    ) -> (
        "AsyncIterator[capo_sns.types.phone_number_information.PhoneNumberInformation]"
    ):
        _token = next_token
        while True:
            _response = await self.list_origination_numbers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("phone_numbers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_phone_numbers_opted_out(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.string.String"] = None,
    ) -> "capo_sns.types.list_phone_numbers_opted_out_response.ListPhoneNumbersOptedOutResponse":
        """<p>Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them.</p> <p>The results for <code>ListPhoneNumbersOptedOut</code> are paginated, and each page returns up to 100 phone numbers. If additional phone numbers are available after the first page of results, then a <code>NextToken</code> string will be returned. To receive the next page, you call <code>ListPhoneNumbersOptedOut</code> again using the <code>NextToken</code> string received from the previous call. When there are no more records to return, <code>NextToken</code> will be null.</p>

        Args:
            next_token: <p>A <code>NextToken</code> string is used when you call the <code>ListPhoneNumbersOptedOut</code> action to retrieve additional records that are available after the first page of results.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.list_phone_numbers_opted_out_input.ListPhoneNumbersOptedOutInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.list_phone_numbers_opted_out_response.ListPhoneNumbersOptedOutResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.list_phone_numbers_opted_out

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.list_phone_numbers_opted_out.async_list_phone_numbers_opted_out(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.list_phone_numbers_opted_out_input.ListPhoneNumbersOptedOutInput = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_phone_numbers_opted_out(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.string.String"] = None,
    ) -> "AsyncIterator[capo_sns.types.phone_number.PhoneNumber]":
        _token = next_token
        while True:
            _response = await self.list_phone_numbers_opted_out(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("phone_numbers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_platform_applications(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.string.String"] = None,
    ) -> "capo_sns.types.list_platform_applications_response.ListPlatformApplicationsResponse":
        """<p>Lists the platform application objects for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). The results for <code>ListPlatformApplications</code> are paginated and return a limited list of applications, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call <code>ListPlatformApplications</code> using the NextToken string received from the previous call. When there are no more records to return, <code>NextToken</code> will be null. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html">Using Amazon SNS Mobile Push Notifications</a>. </p> <p>This action is throttled at 15 transactions per second (TPS).</p>

        Args:
            next_token: <p> <code>NextToken</code> string is used when calling <code>ListPlatformApplications</code> action to retrieve additional records that are available after the first page results.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.list_platform_applications_input.ListPlatformApplicationsInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.list_platform_applications_response.ListPlatformApplicationsResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.list_platform_applications

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.list_platform_applications.async_list_platform_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.list_platform_applications_input.ListPlatformApplicationsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_platform_applications(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.string.String"] = None,
    ) -> "AsyncIterator[capo_sns.types.platform_application.PlatformApplication]":
        _token = next_token
        while True:
            _response = await self.list_platform_applications(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("platform_applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sms_sandbox_phone_numbers(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
        max_results: Optional["capo_sns.types.max_items.MaxItems"] = None,
    ) -> "capo_sns.types.list_sms_sandbox_phone_numbers_result.ListSMSSandboxPhoneNumbersResult":
        """<p>Lists the calling Amazon Web Services account's current verified and pending destination phone numbers in the SMS sandbox.</p> <p>When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the <i>SMS sandbox</i>. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html">SMS sandbox</a> in the <i>Amazon SNS Developer Guide</i>.</p>

        Args:
            next_token: <p>Token that the previous <code>ListSMSSandboxPhoneNumbersInput</code> request returns.</p>
            max_results: <p>The maximum number of phone numbers to return.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.resource_not_found_exception.ResourceNotFoundException: <p>Can’t perform the action on the specified resource. Make sure that the resource exists.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.list_sms_sandbox_phone_numbers_input.ListSMSSandboxPhoneNumbersInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.list_sms_sandbox_phone_numbers_result.ListSMSSandboxPhoneNumbersResult"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.list_sms_sandbox_phone_numbers

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.list_sms_sandbox_phone_numbers.async_list_sms_sandbox_phone_numbers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.list_sms_sandbox_phone_numbers_input.ListSMSSandboxPhoneNumbersInput = {}
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

    async def iter_list_sms_sandbox_phone_numbers(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
        max_results: Optional["capo_sns.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sns.types.sms_sandbox_phone_number.SMSSandboxPhoneNumber]":
        _token = next_token
        while True:
            _response = await self.list_sms_sandbox_phone_numbers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("phone_numbers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
    ) -> "capo_sns.types.list_subscriptions_response.ListSubscriptionsResponse":
        """<p>Returns a list of the requester's subscriptions. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a <code>NextToken</code> is also returned. Use the <code>NextToken</code> parameter in a new <code>ListSubscriptions</code> call to get further results.</p> <p>This action is throttled at 30 transactions per second (TPS).</p>

        Args:
            next_token: <p>Token returned by the previous <code>ListSubscriptions</code> request.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.list_subscriptions_input.ListSubscriptionsInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.list_subscriptions_response.ListSubscriptionsResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.list_subscriptions

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.list_subscriptions.async_list_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.list_subscriptions_input.ListSubscriptionsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
    ) -> "AsyncIterator[capo_sns.types.subscription.Subscription]":
        _token = next_token
        while True:
            _response = await self.list_subscriptions(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscriptions_by_topic(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
    ) -> "capo_sns.types.list_subscriptions_by_topic_response.ListSubscriptionsByTopicResponse":
        """<p>Returns a list of the subscriptions to a specific topic. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a <code>NextToken</code> is also returned. Use the <code>NextToken</code> parameter in a new <code>ListSubscriptionsByTopic</code> call to get further results.</p> <p>This action is throttled at 30 transactions per second (TPS).</p>

        Args:
            topic_arn: <p>The ARN of the topic for which you wish to find subscriptions.</p>
            next_token: <p>Token returned by the previous <code>ListSubscriptionsByTopic</code> request.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.list_subscriptions_by_topic_input.ListSubscriptionsByTopicInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.list_subscriptions_by_topic_response.ListSubscriptionsByTopicResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.list_subscriptions_by_topic

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.list_subscriptions_by_topic.async_list_subscriptions_by_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.list_subscriptions_by_topic_input.ListSubscriptionsByTopicInput = {
            "topic_arn": topic_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_subscriptions_by_topic(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
    ) -> "AsyncIterator[capo_sns.types.subscription.Subscription]":
        _token = next_token
        while True:
            _response = await self.list_subscriptions_by_topic(
                topic_arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_sns.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all tags added to the specified Amazon SNS topic. For an overview, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html">Amazon SNS Tags</a> in the <i>Amazon Simple Notification Service Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The ARN of the topic for which to list tags.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.concurrent_access_exception.ConcurrentAccessException: <p>Can't perform multiple operations on a tag simultaneously. Perform the operations sequentially.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.resource_not_found_exception.ResourceNotFoundException: <p>Can’t perform the action on the specified resource. Make sure that the resource exists.</p>
            capo_sns.errors.tag_policy_exception.TagPolicyException: <p>The request doesn't comply with the IAM tag policy. Correct your request and then retry it.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_topics(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
    ) -> "capo_sns.types.list_topics_response.ListTopicsResponse":
        """<p>Returns a list of the requester's topics. Each call returns a limited list of topics, up to 100. If there are more topics, a <code>NextToken</code> is also returned. Use the <code>NextToken</code> parameter in a new <code>ListTopics</code> call to get further results.</p> <p>This action is throttled at 30 transactions per second (TPS).</p>

        Args:
            next_token: <p>Token returned by the previous <code>ListTopics</code> request.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.list_topics_input.ListTopicsInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.list_topics_response.ListTopicsResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.list_topics

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.list_topics.async_list_topics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.list_topics_input.ListTopicsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_topics(
        self,
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        next_token: Optional["capo_sns.types.next_token.nextToken"] = None,
    ) -> "AsyncIterator[capo_sns.types.topic.Topic]":
        _token = next_token
        while True:
            _response = await self.list_topics(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("topics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def opt_in_phone_number(
        self,
        phone_number: "capo_sns.types.phone_number.PhoneNumber",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.opt_in_phone_number_response.OptInPhoneNumberResponse":
        """<p>Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number.</p> <p>You can opt in a phone number only once every 30 days.</p>

        Args:
            phone_number: <p>The phone number to opt in. Use E.164 format.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.opt_in_phone_number_input.OptInPhoneNumberInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.opt_in_phone_number_response.OptInPhoneNumberResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.opt_in_phone_number

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.opt_in_phone_number.async_opt_in_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.opt_in_phone_number_input.OptInPhoneNumberInput = {
            "phone_number": phone_number
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def publish(
        self,
        message: "capo_sns.types.message.message",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        topic_arn: Optional["capo_sns.types.topic_arn.topicARN"] = None,
        target_arn: Optional["capo_sns.types.string.String"] = None,
        phone_number: Optional["capo_sns.types.phone_number.PhoneNumber"] = None,
        subject: Optional["capo_sns.types.subject.subject"] = None,
        message_structure: Optional[
            "capo_sns.types.message_structure.messageStructure"
        ] = None,
        message_attributes: Optional[
            "capo_sns.types.message_attribute_map.MessageAttributeMap"
        ] = None,
        message_deduplication_id: Optional["capo_sns.types.string.String"] = None,
        message_group_id: Optional["capo_sns.types.string.String"] = None,
    ) -> "capo_sns.types.publish_response.PublishResponse":
        r"""<p>Sends a message to an Amazon SNS topic, a text message (SMS message) directly to a phone number, or a message to a mobile platform endpoint (when you specify the <code>TargetArn</code>).</p> <p>If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint.</p> <p>When a <code>messageId</code> is returned, the message is saved and Amazon SNS immediately delivers it to subscribers.</p> <p>To use the <code>Publish</code> action for publishing a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the <code>CreatePlatformEndpoint</code> action. </p> <p>For more information about formatting messages, see <a href="https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-custommessage.html">Send Custom Platform-Specific Payloads in Messages to Mobile Devices</a>. </p> <important> <p>You can publish messages only to topics and endpoints in the same Amazon Web Services Region.</p> </important>

        Args:
            topic_arn: <p>The topic you want to publish to.</p> <p>If you don't specify a value for the <code>TopicArn</code> parameter, you must specify a value for the <code>PhoneNumber</code> or <code>TargetArn</code> parameters.</p>
            target_arn: <p>If you don't specify a value for the <code>TargetArn</code> parameter, you must specify a value for the <code>PhoneNumber</code> or <code>TopicArn</code> parameters.</p>
            phone_number: <p>The phone number to which you want to deliver an SMS message. Use E.164 format.</p> <p>If you don't specify a value for the <code>PhoneNumber</code> parameter, you must specify a value for the <code>TargetArn</code> or <code>TopicArn</code> parameters.</p>
            message: <p>The message you want to send.</p> <p>If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the <code>MessageStructure</code> parameter to <code>json</code> and use a JSON object for the <code>Message</code> parameter. </p> <p></p> <p>Constraints:</p> <ul> <li> <p>With the exception of SMS, messages must be UTF-8 encoded strings. By default, a message can be at most 256 KiB in size (262,144 bytes, not 262,144 characters).</p> <p>When you publish to a topic, the maximum size is determined by the topic's <code>MaximumMessageSize</code> attribute, which supports values up to 1 MiB (1,048,576 bytes). Amazon SNS validates the combined size of the message body and message attributes against this value and returns an <code>InvalidParameter</code> error if the limit is exceeded.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html">Large message payloads</a> in the <i>Amazon SNS Developer Guide.</i> </p> </li> <li> <p>For SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters.</p> <p>If you publish a message that exceeds this size limit, Amazon SNS sends the message as multiple messages, each fitting within the size limit. Messages aren't truncated mid-word but are cut off at whole-word boundaries.</p> <p>The total size limit for a single SMS <code>Publish</code> action is 1,600 characters.</p> </li> </ul> <p>JSON-specific constraints:</p> <ul> <li> <p>Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.</p> </li> <li> <p>The values will be parsed (unescaped) before they are used in outgoing messages.</p> </li> <li> <p>Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).</p> </li> <li> <p>Values have a minimum length of 0 (the empty string, "", is allowed).</p> </li> <li> <p>Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).</p> </li> <li> <p>Non-string values will cause the key to be ignored.</p> </li> <li> <p>Keys that do not correspond to supported transport protocols are ignored.</p> </li> <li> <p>Duplicate keys are not allowed.</p> </li> <li> <p>Failure to parse or validate any key or value in the message will cause the <code>Publish</code> call to return an error (no partial delivery).</p> </li> </ul>
            subject: <p>Optional parameter to be used as the "Subject" line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.</p> <p>Constraints: Subjects must be UTF-8 text with no line breaks or control characters, and less than 100 characters long.</p>
            message_structure: <p>Set <code>MessageStructure</code> to <code>json</code> if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set <code>MessageStructure</code> to <code>json</code>, the value of the <code>Message</code> parameter must: </p> <ul> <li> <p>be a syntactically valid JSON object; and</p> </li> <li> <p>contain at least a top-level JSON key of "default" with a value that is a string.</p> </li> </ul> <p>You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., "http").</p> <p>Valid value: <code>json</code> </p>
            message_attributes: <p>Message attributes for Publish action.</p>
            message_deduplication_id: <ul> <li> <p>This parameter applies only to FIFO (first-in-first-out) topics. The <code>MessageDeduplicationId</code> can contain up to 128 alphanumeric characters <code>(a-z, A-Z, 0-9)</code> and punctuation <code>(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)</code>.</p> </li> <li> <p>Every message must have a unique <code>MessageDeduplicationId</code>, which is a token used for deduplication of sent messages within the 5 minute minimum deduplication interval.</p> </li> <li> <p>The scope of deduplication depends on the <code>FifoThroughputScope</code> attribute, when set to <code>Topic</code> the message deduplication scope is across the entire topic, when set to <code>MessageGroup</code> the message deduplication scope is within each individual message group.</p> </li> <li> <p>If a message with a particular <code>MessageDeduplicationId</code> is sent successfully, subsequent messages within the deduplication scope and interval, with the same <code>MessageDeduplicationId</code>, are accepted successfully but aren't delivered.</p> </li> <li> <p>Every message must have a unique <code>MessageDeduplicationId</code>:</p> <ul> <li> <p>You may provide a <code>MessageDeduplicationId</code> explicitly.</p> </li> <li> <p>If you aren't able to provide a <code>MessageDeduplicationId</code> and you enable <code>ContentBasedDeduplication</code> for your topic, Amazon SNS uses a SHA-256 hash to generate the <code>MessageDeduplicationId</code> using the body of the message (but not the attributes of the message).</p> </li> <li> <p>If you don't provide a <code>MessageDeduplicationId</code> and the topic doesn't have <code>ContentBasedDeduplication</code> set, the action fails with an error.</p> </li> <li> <p>If the topic has a <code>ContentBasedDeduplication</code> set, your <code>MessageDeduplicationId</code> overrides the generated one. </p> </li> </ul> </li> <li> <p>When <code>ContentBasedDeduplication</code> is in effect, messages with identical content sent within the deduplication scope and interval are treated as duplicates and only one copy of the message is delivered.</p> </li> <li> <p>If you send one message with <code>ContentBasedDeduplication</code> enabled, and then another message with a <code>MessageDeduplicationId</code> that is the same as the one generated for the first <code>MessageDeduplicationId</code>, the two messages are treated as duplicates, within the deduplication scope and interval, and only one copy of the message is delivered.</p> </li> </ul>
            message_group_id: <p>The <code>MessageGroupId</code> can contain up to 128 alphanumeric characters <code>(a-z, A-Z, 0-9)</code> and punctuation <code>(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)</code>.</p> <p> For FIFO topics: The <code>MessageGroupId</code> is a tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). Every message must include a <code>MessageGroupId</code>. </p> <p> For standard topics: The <code>MessageGroupId</code> is optional and is forwarded only to Amazon SQS standard subscriptions to activate <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fair-queues.html">fair queues</a>. The <code>MessageGroupId</code> is not used for, or sent to, any other endpoint types. When provided, the same validation rules apply as for FIFO topics. </p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.endpoint_disabled_exception.EndpointDisabledException: <p>Exception error indicating endpoint disabled.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_security_exception.InvalidSecurityException: <p>The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.</p>
            capo_sns.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>The ciphertext references a key that doesn't exist or that you don't have access to.</p>
            capo_sns.errors.kms_disabled_exception.KMSDisabledException: <p>The request was rejected because the specified Amazon Web Services KMS key isn't enabled.</p>
            capo_sns.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>The request was rejected because the state of the specified resource isn't valid for this request. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">Key states of Amazon Web Services KMS keys</a> in the <i>Key Management Service Developer Guide</i>.</p>
            capo_sns.errors.kms_not_found_exception.KMSNotFoundException: <p>The request was rejected because the specified entity or resource can't be found.</p>
            capo_sns.errors.kms_opt_in_required.KMSOptInRequired: <p>The Amazon Web Services access key ID needs a subscription for the service.</p>
            capo_sns.errors.kms_throttling_exception.KMSThrottlingException: <p>The request was denied due to request throttling. For more information about throttling, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second">Limits</a> in the <i>Key Management Service Developer Guide.</i> </p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.platform_application_disabled_exception.PlatformApplicationDisabledException: <p>Exception error indicating platform application disabled.</p>
            capo_sns.errors.validation_exception.ValidationException: <p>Indicates that a parameter in the request is invalid.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.publish_input.PublishInput]",
        ) -> AsyncOperationResponse["capo_sns.types.publish_response.PublishResponse"]:
            import capo_sns._operations.amazon_simple_notification_service.publish

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.publish.async_publish(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.publish_input.PublishInput = {"message": message}
        if topic_arn is not None:
            input_["topic_arn"] = topic_arn
        if target_arn is not None:
            input_["target_arn"] = target_arn
        if phone_number is not None:
            input_["phone_number"] = phone_number
        if subject is not None:
            input_["subject"] = subject
        if message_structure is not None:
            input_["message_structure"] = message_structure
        if message_attributes is not None:
            input_["message_attributes"] = message_attributes
        if message_deduplication_id is not None:
            input_["message_deduplication_id"] = message_deduplication_id
        if message_group_id is not None:
            input_["message_group_id"] = message_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def publish_batch(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        publish_batch_request_entries: "capo_sns.types.publish_batch_request_entry_list.PublishBatchRequestEntryList",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.publish_batch_response.PublishBatchResponse":
        """<p>Publishes up to 10 messages to the specified topic in a single batch. This is a batch version of the <code>Publish</code> API. If you try to send more than 10 messages in a single batch request, you will receive a <code>TooManyEntriesInBatchRequest</code> exception.</p> <p>For FIFO topics, multiple messages within a single batch are published in the order they are sent, and messages are deduplicated within the batch and across batches for five minutes.</p> <p>The result of publishing each message is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p> <p>By default, the maximum allowed individual message size and the maximum total payload size (the sum of the individual lengths of all of the batched messages) are both 256 KiB (262,144 bytes). To publish larger batches, set the topic's <code>MaximumMessageSize</code> attribute, which supports values up to 1 MiB (1,048,576 bytes). The combined size of all messages in the batch, including each message's body and attributes, must not exceed the topic's <code>MaximumMessageSize</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html">Large message payloads</a> in the <i>Amazon SNS Developer Guide.</i> </p> <important> <p>The <code>PublishBatch</code> API can send up to 10 messages at a time. If you attempt to send more than 10 messages in one request, you will encounter a <code>TooManyEntriesInBatchRequest</code> exception. In such cases, split your messages into multiple requests, each containing no more than 10 messages.</p> </important> <p>Some actions take lists of parameters. These lists are specified using the <code>param.n</code> notation. Values of <code>n</code> are integers starting from <b>1</b>. For example, a parameter list with two elements looks like this:</p> <p> <code>&AttributeName.1=first</code> </p> <p> <code>&AttributeName.2=second</code> </p> <p>If you send a batch message to a topic, Amazon SNS publishes the batch message to each endpoint that is subscribed to the topic. The format of the batch message depends on the notification protocol for each subscribed endpoint.</p> <p>When a <code>messageId</code> is returned, the batch message is saved, and Amazon SNS immediately delivers the message to subscribers.</p>

        Args:
            topic_arn: <p>The Amazon resource name (ARN) of the topic you want to batch publish to.</p>
            publish_batch_request_entries: <p>A list of <code>PublishBatch</code> request entries to be sent to the SNS topic.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.batch_entry_ids_not_distinct_exception.BatchEntryIdsNotDistinctException: <p>Two or more batch entries in the request have the same <code>Id</code>.</p>
            capo_sns.errors.batch_request_too_long_exception.BatchRequestTooLongException: <p>The length of all the batch messages put together is more than the limit.</p>
            capo_sns.errors.empty_batch_request_exception.EmptyBatchRequestException: <p>The batch request doesn't contain any entries.</p>
            capo_sns.errors.endpoint_disabled_exception.EndpointDisabledException: <p>Exception error indicating endpoint disabled.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_batch_entry_id_exception.InvalidBatchEntryIdException: <p>The <code>Id</code> of a batch entry in a batch request doesn't abide by the specification. </p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_security_exception.InvalidSecurityException: <p>The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.</p>
            capo_sns.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>The ciphertext references a key that doesn't exist or that you don't have access to.</p>
            capo_sns.errors.kms_disabled_exception.KMSDisabledException: <p>The request was rejected because the specified Amazon Web Services KMS key isn't enabled.</p>
            capo_sns.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>The request was rejected because the state of the specified resource isn't valid for this request. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">Key states of Amazon Web Services KMS keys</a> in the <i>Key Management Service Developer Guide</i>.</p>
            capo_sns.errors.kms_not_found_exception.KMSNotFoundException: <p>The request was rejected because the specified entity or resource can't be found.</p>
            capo_sns.errors.kms_opt_in_required.KMSOptInRequired: <p>The Amazon Web Services access key ID needs a subscription for the service.</p>
            capo_sns.errors.kms_throttling_exception.KMSThrottlingException: <p>The request was denied due to request throttling. For more information about throttling, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second">Limits</a> in the <i>Key Management Service Developer Guide.</i> </p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.platform_application_disabled_exception.PlatformApplicationDisabledException: <p>Exception error indicating platform application disabled.</p>
            capo_sns.errors.too_many_entries_in_batch_request_exception.TooManyEntriesInBatchRequestException: <p> The batch request contains more entries than permissible (more than 10).</p>
            capo_sns.errors.validation_exception.ValidationException: <p>Indicates that a parameter in the request is invalid.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.publish_batch_input.PublishBatchInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.publish_batch_response.PublishBatchResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.publish_batch

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.publish_batch.async_publish_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.publish_batch_input.PublishBatchInput = {
            "topic_arn": topic_arn,
            "publish_batch_request_entries": publish_batch_request_entries,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_data_protection_policy(
        self,
        resource_arn: "capo_sns.types.topic_arn.topicARN",
        data_protection_policy: "capo_sns.types.attribute_value.attributeValue",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> None:
        """<important> <p>Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html">Amazon SNS message data protection availability change</a>.</p> </important> <p>Adds or updates an inline policy document that is stored in the specified Amazon SNS topic.</p>

        Args:
            resource_arn: <p>The ARN of the topic whose <code>DataProtectionPolicy</code> you want to add or update.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the Amazon Web Services General Reference.</p>
            data_protection_policy: <p>The JSON serialization of the topic's <code>DataProtectionPolicy</code>.</p> <p>The <code>DataProtectionPolicy</code> must be in JSON string format.</p> <p>Length Constraints: Maximum length of 30,720.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_security_exception.InvalidSecurityException: <p>The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.put_data_protection_policy_input.PutDataProtectionPolicyInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.put_data_protection_policy

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.put_data_protection_policy.async_put_data_protection_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.put_data_protection_policy_input.PutDataProtectionPolicyInput = {
            "resource_arn": resource_arn,
            "data_protection_policy": data_protection_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_permission(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        label: "capo_sns.types.label.label",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> None:
        """<p>Removes a statement from a topic's access control policy.</p> <note> <p>To remove the ability to change topic permissions, you must deny permissions to the <code>AddPermission</code>, <code>RemovePermission</code>, and <code>SetTopicAttributes</code> actions in your IAM policy.</p> </note>

        Args:
            topic_arn: <p>The ARN of the topic whose access control policy you wish to modify.</p>
            label: <p>The unique label of the statement you want to remove.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.remove_permission_input.RemovePermissionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.remove_permission

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.remove_permission.async_remove_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.remove_permission_input.RemovePermissionInput = {
            "topic_arn": topic_arn,
            "label": label,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_endpoint_attributes(
        self,
        endpoint_arn: "capo_sns.types.string.String",
        attributes: "capo_sns.types.map_string_to_string.MapStringToString",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> None:
        """<p>Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html">Using Amazon SNS Mobile Push Notifications</a>. </p>

        Args:
            endpoint_arn: <p>EndpointArn used for <code>SetEndpointAttributes</code> action.</p>
            attributes: <p>A map of the endpoint attributes. Attributes in this map include the following:</p> <ul> <li> <p> <code>CustomUserData</code> – arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.</p> </li> <li> <p> <code>Enabled</code> – flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.</p> </li> <li> <p> <code>Token</code> – device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.</p> </li> </ul>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.set_endpoint_attributes_input.SetEndpointAttributesInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.set_endpoint_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.set_endpoint_attributes.async_set_endpoint_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.set_endpoint_attributes_input.SetEndpointAttributesInput = {
            "endpoint_arn": endpoint_arn,
            "attributes": attributes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_platform_application_attributes(
        self,
        platform_application_arn: "capo_sns.types.string.String",
        attributes: "capo_sns.types.map_string_to_string.MapStringToString",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> None:
        """<p>Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html">Using Amazon SNS Mobile Push Notifications</a>. For information on configuring attributes for message delivery status, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html">Using Amazon SNS Application Attributes for Message Delivery Status</a>. </p>

        Args:
            platform_application_arn: <p> <code>PlatformApplicationArn</code> for <code>SetPlatformApplicationAttributes</code> action.</p>
            attributes: <p>A map of the platform application attributes. Attributes in this map include the following:</p> <ul> <li> <p> <code>PlatformCredential</code> – The credential received from the notification service.</p> <ul> <li> <p>For ADM, <code>PlatformCredential</code>is client secret.</p> </li> <li> <p>For Apple Services using certificate credentials, <code>PlatformCredential</code> is private key.</p> </li> <li> <p>For Apple Services using token credentials, <code>PlatformCredential</code> is signing key.</p> </li> <li> <p>For GCM (Firebase Cloud Messaging) using key credentials, there is no <code>PlatformPrincipal</code>. The <code>PlatformCredential</code> is <code>API key</code>.</p> </li> <li> <p>For GCM (Firebase Cloud Messaging) using token credentials, there is no <code>PlatformPrincipal</code>. The <code>PlatformCredential</code> is a JSON formatted private key file. When using the Amazon Web Services CLI, the file must be in string format and special characters must be ignored. To format the file correctly, Amazon SNS recommends using the following command: <code>SERVICE_JSON=`jq @json <<< cat service.json`</code>.</p> </li> </ul> </li> </ul> <ul> <li> <p> <code>PlatformPrincipal</code> – The principal received from the notification service.</p> <ul> <li> <p>For ADM, <code>PlatformPrincipal</code>is client id.</p> </li> <li> <p>For Apple Services using certificate credentials, <code>PlatformPrincipal</code> is SSL certificate.</p> </li> <li> <p>For Apple Services using token credentials, <code>PlatformPrincipal</code> is signing key ID.</p> </li> <li> <p>For GCM (Firebase Cloud Messaging), there is no <code>PlatformPrincipal</code>. </p> </li> </ul> </li> </ul> <ul> <li> <p> <code>EventEndpointCreated</code> – Topic ARN to which <code>EndpointCreated</code> event notifications are sent.</p> </li> <li> <p> <code>EventEndpointDeleted</code> – Topic ARN to which <code>EndpointDeleted</code> event notifications are sent.</p> </li> <li> <p> <code>EventEndpointUpdated</code> – Topic ARN to which <code>EndpointUpdate</code> event notifications are sent.</p> </li> <li> <p> <code>EventDeliveryFailure</code> – Topic ARN to which <code>DeliveryFailure</code> event notifications are sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.</p> </li> <li> <p> <code>SuccessFeedbackRoleArn</code> – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.</p> </li> <li> <p> <code>FailureFeedbackRoleArn</code> – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.</p> </li> <li> <p> <code>SuccessFeedbackSampleRate</code> – Sample rate percentage (0-100) of successfully delivered messages.</p> </li> </ul> <p>The following attributes only apply to <code>APNs</code> token-based authentication:</p> <ul> <li> <p> <code>ApplePlatformTeamID</code> – The identifier that's assigned to your Apple developer account team.</p> </li> <li> <p> <code>ApplePlatformBundleID</code> – The bundle identifier that's assigned to your iOS app.</p> </li> </ul>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.set_platform_application_attributes_input.SetPlatformApplicationAttributesInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.set_platform_application_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.set_platform_application_attributes.async_set_platform_application_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.set_platform_application_attributes_input.SetPlatformApplicationAttributesInput = {
            "platform_application_arn": platform_application_arn,
            "attributes": attributes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_sms_attributes(
        self,
        attributes: "capo_sns.types.map_string_to_string.MapStringToString",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.set_sms_attributes_response.SetSMSAttributesResponse":
        """<p>Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports.</p> <p>You can override some of these settings for a single message when you use the <code>Publish</code> action with the <code>MessageAttributes.entry.N</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html">Publishing to a mobile phone</a> in the <i>Amazon SNS Developer Guide</i>.</p> <note> <p>To use this operation, you must grant the Amazon SNS service principal (<code>sns.amazonaws.com</code>) permission to perform the <code>s3:ListBucket</code> action. </p> </note>

        Args:
            attributes: <p>The default settings for sending SMS messages from your Amazon Web Services account. You can set values for the following attribute names:</p> <p> <code>MonthlySpendLimit</code> – The maximum amount in USD that you are willing to spend each month to send SMS messages. When Amazon SNS determines that sending an SMS message would incur a cost that exceeds this limit, it stops sending SMS messages within minutes.</p> <important> <p>Amazon SNS stops sending SMS messages within minutes of the limit being crossed. During that interval, if you continue to send SMS messages, you will incur costs that exceed your limit.</p> </important> <p>By default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to raise the limit, submit an <a href="https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-sns">SNS Limit Increase case</a>. For <b>New limit value</b>, enter your desired monthly spend limit. In the <b>Use Case Description</b> field, explain that you are requesting an SMS monthly spend limit increase.</p> <p> <code>DeliveryStatusIAMRole</code> – The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS writes a log that includes the message price, the success or failure status, the reason for failure (if the message failed), the message dwell time, and other information.</p> <p> <code>DeliveryStatusSuccessSamplingRate</code> – The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 - 100. For example, to write logs only for failed deliveries, set this value to <code>0</code>. To write logs for 10% of your successful deliveries, set it to <code>10</code>.</p> <p> <code>DefaultSenderID</code> – A string, such as your business brand, that is displayed as the sender on the receiving device. Support for sender IDs varies by country. The sender ID can be 1 - 11 alphanumeric characters, and it must contain at least one letter.</p> <p> <code>DefaultSMSType</code> – The type of SMS message that you will send by default. You can assign the following values:</p> <ul> <li> <p> <code>Promotional</code> – (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost.</p> </li> <li> <p> <code>Transactional</code> – Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability.</p> </li> </ul> <p> <code>UsageReportS3Bucket</code> – The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file to the bucket. The report includes the following information for each SMS message that was successfully delivered by your Amazon Web Services account:</p> <ul> <li> <p>Time that the message was published (in UTC)</p> </li> <li> <p>Message ID</p> </li> <li> <p>Destination phone number</p> </li> <li> <p>Message type</p> </li> <li> <p>Delivery status</p> </li> <li> <p>Message price (in USD)</p> </li> <li> <p>Part number (a message is split into multiple parts if it is too long for a single message)</p> </li> <li> <p>Total number of parts</p> </li> </ul> <p>To receive the report, the bucket must have a policy that allows the Amazon SNS service principal to perform the <code>s3:PutObject</code> and <code>s3:GetBucketLocation</code> actions.</p> <p>For an example bucket policy and usage report, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sms_stats.html">Monitoring SMS Activity</a> in the <i>Amazon SNS Developer Guide</i>.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.set_sms_attributes_input.SetSMSAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.set_sms_attributes_response.SetSMSAttributesResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.set_sms_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.set_sms_attributes.async_set_sms_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.set_sms_attributes_input.SetSMSAttributesInput = {
            "attributes": attributes
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_subscription_attributes(
        self,
        subscription_arn: "capo_sns.types.subscription_arn.subscriptionARN",
        attribute_name: "capo_sns.types.attribute_name.attributeName",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        attribute_value: Optional[
            "capo_sns.types.attribute_value.attributeValue"
        ] = None,
    ) -> None:
        """<p>Allows a subscription owner to set an attribute of the subscription to a new value.</p>

        Args:
            subscription_arn: <p>The ARN of the subscription to modify.</p>
            attribute_name: <p>A map of attributes with their corresponding values.</p> <p>The following lists the names, descriptions, and values of the special request parameters that this action uses:</p> <ul> <li> <p> <code>DeliveryPolicy</code> – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.</p> </li> <li> <p> <code>FilterPolicy</code> – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.</p> </li> <li> <p> <code>FilterPolicyScope</code> – This attribute lets you choose the filtering scope by using one of the following string value types:</p> <ul> <li> <p> <code>MessageAttributes</code> (default) – The filter is applied on the message attributes.</p> </li> <li> <p> <code>MessageBody</code> – The filter is applied on the message body.</p> </li> </ul> </li> <li> <p> <code>RawMessageDelivery</code> – When set to <code>true</code>, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.</p> </li> <li> <p> <code>RedrivePolicy</code> – When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.</p> </li> </ul> <p>The following attribute applies only to Amazon Data Firehose delivery stream subscriptions:</p> <ul> <li> <p> <code>SubscriptionRoleArn</code> – The ARN of the IAM role that has the following:</p> <ul> <li> <p>Permission to write to the Firehose delivery stream</p> </li> <li> <p>Amazon SNS listed as a trusted entity</p> </li> </ul> <p>Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html">Fanout to Firehose delivery streams</a> in the <i>Amazon SNS Developer Guide</i>.</p> </li> </ul>
            attribute_value: <p>The new value for the attribute in JSON format.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.filter_policy_limit_exceeded_exception.FilterPolicyLimitExceededException: <p>Indicates that the number of filter polices in your Amazon Web Services account exceeds the limit. To add more filter polices, submit an Amazon SNS Limit Increase case in the Amazon Web Services Support Center.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.replay_limit_exceeded_exception.ReplayLimitExceededException: <p>Indicates that the request parameter has exceeded the maximum number of concurrent message replays.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.set_subscription_attributes_input.SetSubscriptionAttributesInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.set_subscription_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.set_subscription_attributes.async_set_subscription_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.set_subscription_attributes_input.SetSubscriptionAttributesInput = {
            "subscription_arn": subscription_arn,
            "attribute_name": attribute_name,
        }
        if attribute_value is not None:
            input_["attribute_value"] = attribute_value

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_topic_attributes(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        attribute_name: "capo_sns.types.attribute_name.attributeName",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        attribute_value: Optional[
            "capo_sns.types.attribute_value.attributeValue"
        ] = None,
    ) -> None:
        """<p>Allows a topic owner to set an attribute of the topic to a new value.</p> <note> <p>To remove the ability to change topic permissions, you must deny permissions to the <code>AddPermission</code>, <code>RemovePermission</code>, and <code>SetTopicAttributes</code> actions in your IAM policy.</p> </note>

        Args:
            topic_arn: <p>The ARN of the topic to modify.</p>
            attribute_name: <p>A map of attributes with their corresponding values.</p> <p>The following lists the names, descriptions, and values of the special request parameters that the <code>SetTopicAttributes</code> action uses:</p> <ul> <li> <p> <code>DeliveryPolicy</code> – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.</p> </li> <li> <p> <code>DisplayName</code> – The display name to use for a topic with SMS, <code>email</code>, and <code>email-json</code> subscriptions. For <code>email</code> and <code>email-json</code> subscriptions, the display name is used as the sender name for regular notification messages. Subscription confirmation and unsubscribe confirmation emails always use "Amazon Web Services Notifications" as the sender name.</p> </li> <li> <p> <code>MaximumMessageSize</code> – The maximum size, in bytes, of a message that can be published to the topic. Valid values are <code>1024</code> to <code>1048576</code> (1 MiB). The default is <code>262144</code> (256 KiB).</p> <p>A topic with a <code>MaximumMessageSize</code> above 256 KiB must have 100 or fewer subscriptions, and each subscription must be an Amazon SQS, Amazon Data Firehose, or Lambda subscription.</p> <p>You can increase or decrease this value at any time. If the topic doesn't meet these requirements when you set a value above 256 KiB, Amazon SNS returns an <code>InvalidParameter</code> error. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html">Large message payloads</a> in the <i>Amazon SNS Developer Guide.</i> </p> </li> <li> <p> <code>Policy</code> – The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.</p> </li> <li> <p> <code>TracingConfig</code> – Tracing mode of an Amazon SNS topic. By default <code>TracingConfig</code> is set to <code>PassThrough</code>, and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to <code>Active</code>, Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. This is only supported on standard topics.</p> </li> <li> <p>HTTP</p> <ul> <li> <p> <code>HTTPSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint. </p> </li> <li> <p> <code>HTTPSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an HTTP endpoint.</p> </li> <li> <p> <code>HTTPFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint.</p> </li> </ul> </li> <li> <p>Amazon Data Firehose</p> <ul> <li> <p> <code>FirehoseSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint.</p> </li> <li> <p> <code>FirehoseSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint.</p> </li> <li> <p> <code>FirehoseFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint. </p> </li> </ul> </li> <li> <p>Lambda</p> <ul> <li> <p> <code>LambdaSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Lambda endpoint.</p> </li> <li> <p> <code>LambdaSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Lambda endpoint.</p> </li> <li> <p> <code>LambdaFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Lambda endpoint. </p> </li> </ul> </li> <li> <p>Platform application endpoint</p> <ul> <li> <p> <code>ApplicationSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an platform application endpoint.</p> </li> <li> <p> <code>ApplicationSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an platform application endpoint.</p> </li> <li> <p> <code>ApplicationFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an platform application endpoint.</p> </li> </ul> <note> <p>In addition to being able to configure topic attributes for message delivery status of notification messages sent to Amazon SNS application endpoints, you can also configure application attributes for the delivery status of push notification messages sent to push notification services.</p> <p>For example, For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html">Using Amazon SNS Application Attributes for Message Delivery Status</a>. </p> </note> </li> <li> <p>Amazon SQS</p> <ul> <li> <p> <code>SQSSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p> </li> <li> <p> <code>SQSSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p> </li> <li> <p> <code>SQSFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p> </li> </ul> </li> </ul> <note> <p>The <ENDPOINT>SuccessFeedbackRoleArn and <ENDPOINT>FailureFeedbackRoleArn attributes are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The <ENDPOINT>SuccessFeedbackSampleRate attribute is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the <ENDPOINT>FailureFeedbackRoleArn attribute, then all failed message deliveries generate CloudWatch Logs. </p> </note> <p>The following attribute applies only to <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html">server-side-encryption</a>:</p> <ul> <li> <p> <code>KmsMasterKeyId</code> – The ID of an Amazon Web Services managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms">Key Terms</a>. For more examples, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters">KeyId</a> in the <i>Key Management Service API Reference</i>. </p> </li> <li> <p> <code>SignatureVersion</code> – The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, <code>SignatureVersion</code> is set to <code>1</code>.</p> </li> </ul> <p>The following attribute applies only to <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html">FIFO topics</a>:</p> <ul> <li> <p> <code>ArchivePolicy</code> – The policy that sets the retention period for messages stored in the message archive of an Amazon SNS FIFO topic.</p> </li> <li> <p> <code>ContentBasedDeduplication</code> – Enables content-based deduplication for FIFO topics.</p> <ul> <li> <p>By default, <code>ContentBasedDeduplication</code> is set to <code>false</code>. If you create a FIFO topic and this attribute is <code>false</code>, you must specify a value for the <code>MessageDeduplicationId</code> parameter for the <a href="https://docs.aws.amazon.com/sns/latest/api/API_Publish.html">Publish</a> action. </p> </li> <li> <p>When you set <code>ContentBasedDeduplication</code> to <code>true</code>, Amazon SNS uses a SHA-256 hash to generate the <code>MessageDeduplicationId</code> using the body of the message (but not the attributes of the message).</p> <p>(Optional) To override the generated value, you can specify a value for the <code>MessageDeduplicationId</code> parameter for the <code>Publish</code> action.</p> </li> </ul> </li> </ul> <ul> <li> <p> <code>FifoThroughputScope</code> – Enables higher throughput for your FIFO topic by adjusting the scope of deduplication. This attribute has two possible values:</p> <ul> <li> <p> <code>Topic</code> – The scope of message deduplication is across the entire topic. This is the default value and maintains existing behavior, with a maximum throughput of 3000 messages per second or 20MB per second, whichever comes first.</p> </li> <li> <p> <code>MessageGroup</code> – The scope of deduplication is within each individual message group, which enables higher throughput per topic subject to regional quotas. For more information on quotas or to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/sns.html">Amazon SNS service quotas</a> in the Amazon Web Services General Reference.</p> </li> </ul> </li> </ul>
            attribute_value: <p>The new value for the attribute.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_security_exception.InvalidSecurityException: <p>The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.set_topic_attributes_input.SetTopicAttributesInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.set_topic_attributes

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.set_topic_attributes.async_set_topic_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.set_topic_attributes_input.SetTopicAttributesInput = {
            "topic_arn": topic_arn,
            "attribute_name": attribute_name,
        }
        if attribute_value is not None:
            input_["attribute_value"] = attribute_value

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def subscribe(
        self,
        topic_arn: "capo_sns.types.topic_arn.topicARN",
        protocol: "capo_sns.types.protocol.protocol",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
        endpoint: Optional["capo_sns.types.endpoint2.Endpoint2"] = None,
        attributes: Optional[
            "capo_sns.types.subscription_attributes_map.SubscriptionAttributesMap"
        ] = None,
        return_subscription_arn: Optional["capo_sns.types.boolean.boolean"] = None,
    ) -> "capo_sns.types.subscribe_response.SubscribeResponse":
        """<p>Subscribes an endpoint to an Amazon SNS topic. If the endpoint type is HTTP/S or email, or if the endpoint and the topic are not in the same Amazon Web Services account, the endpoint owner must run the <code>ConfirmSubscription</code> action to confirm the subscription.</p> <p>You call the <code>ConfirmSubscription</code> action with the token from the subscription response. Confirmation tokens are valid for two days.</p> <p>This action is throttled at 100 transactions per second (TPS).</p>

        Args:
            topic_arn: <p>The ARN of the topic you want to subscribe to.</p>
            protocol: <p>The protocol that you want to use. Supported protocols include:</p> <ul> <li> <p> <code>http</code> – delivery of JSON-encoded message via HTTP POST</p> </li> <li> <p> <code>https</code> – delivery of JSON-encoded message via HTTPS POST</p> </li> <li> <p> <code>email</code> – delivery of message via SMTP</p> </li> <li> <p> <code>email-json</code> – delivery of JSON-encoded message via SMTP</p> </li> <li> <p> <code>sms</code> – delivery of message via SMS</p> </li> <li> <p> <code>sqs</code> – delivery of JSON-encoded message to an Amazon SQS queue</p> </li> <li> <p> <code>application</code> – delivery of JSON-encoded message to an EndpointArn for a mobile app and device</p> </li> <li> <p> <code>lambda</code> – delivery of JSON-encoded message to an Lambda function</p> </li> <li> <p> <code>firehose</code> – delivery of JSON-encoded message to an Amazon Data Firehose delivery stream.</p> </li> </ul>
            endpoint: <p>The endpoint that you want to receive notifications. Endpoints vary by protocol:</p> <ul> <li> <p>For the <code>http</code> protocol, the (public) endpoint is a URL beginning with <code>http://</code>.</p> </li> <li> <p>For the <code>https</code> protocol, the (public) endpoint is a URL beginning with <code>https://</code>.</p> </li> <li> <p>For the <code>email</code> protocol, the endpoint is an email address.</p> </li> <li> <p>For the <code>email-json</code> protocol, the endpoint is an email address.</p> </li> <li> <p>For the <code>sms</code> protocol, the endpoint is a phone number of an SMS-enabled device.</p> </li> <li> <p>For the <code>sqs</code> protocol, the endpoint is the ARN of an Amazon SQS queue.</p> </li> <li> <p>For the <code>application</code> protocol, the endpoint is the EndpointArn of a mobile app and device.</p> </li> <li> <p>For the <code>lambda</code> protocol, the endpoint is the ARN of an Lambda function.</p> </li> <li> <p>For the <code>firehose</code> protocol, the endpoint is the ARN of an Amazon Data Firehose delivery stream.</p> </li> </ul>
            attributes: <p>A map of attributes with their corresponding values.</p> <p>The following lists the names, descriptions, and values of the special request parameters that the <code>Subscribe</code> action uses:</p> <ul> <li> <p> <code>DeliveryPolicy</code> – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.</p> </li> <li> <p> <code>FilterPolicy</code> – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.</p> </li> <li> <p> <code>FilterPolicyScope</code> – This attribute lets you choose the filtering scope by using one of the following string value types:</p> <ul> <li> <p> <code>MessageAttributes</code> (default) – The filter is applied on the message attributes.</p> </li> <li> <p> <code>MessageBody</code> – The filter is applied on the message body.</p> </li> </ul> </li> <li> <p> <code>RawMessageDelivery</code> – When set to <code>true</code>, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.</p> </li> <li> <p> <code>RedrivePolicy</code> – When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.</p> </li> </ul> <p>The following attribute applies only to Amazon Data Firehose delivery stream subscriptions:</p> <ul> <li> <p> <code>SubscriptionRoleArn</code> – The ARN of the IAM role that has the following:</p> <ul> <li> <p>Permission to write to the Firehose delivery stream</p> </li> <li> <p>Amazon SNS listed as a trusted entity</p> </li> </ul> <p>Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html">Fanout to Firehose delivery streams</a> in the <i>Amazon SNS Developer Guide</i>.</p> </li> </ul> <p>The following attributes apply only to <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html">FIFO topics</a>:</p> <ul> <li> <p> <code>ReplayPolicy</code> – Adds or updates an inline policy document for a subscription to replay messages stored in the specified Amazon SNS topic.</p> </li> <li> <p> <code>ReplayStatus</code> – Retrieves the status of the subscription message replay, which can be one of the following:</p> <ul> <li> <p> <code>Completed</code> – The replay has successfully redelivered all messages, and is now delivering newly published messages. If an ending point was specified in the <code>ReplayPolicy</code> then the subscription will no longer receive newly published messages.</p> </li> <li> <p> <code>In progress</code> – The replay is currently replaying the selected messages.</p> </li> <li> <p> <code>Failed</code> – The replay was unable to complete.</p> </li> <li> <p> <code>Pending</code> – The default state while the replay initiates.</p> </li> </ul> </li> </ul>
            return_subscription_arn: <p>Sets whether the response from the <code>Subscribe</code> request includes the subscription ARN, even if the subscription is not yet confirmed.</p> <p>If you set this parameter to <code>true</code>, the response includes the ARN in all cases, even if the subscription is not yet confirmed. In addition to the ARN for confirmed subscriptions, the response also includes the <code>pending subscription</code> ARN value for subscriptions that aren't yet confirmed. A subscription becomes confirmed when the subscriber calls the <code>ConfirmSubscription</code> action with a confirmation token.</p> <p></p> <p>The default value is <code>false</code>.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.filter_policy_limit_exceeded_exception.FilterPolicyLimitExceededException: <p>Indicates that the number of filter polices in your Amazon Web Services account exceeds the limit. To add more filter polices, submit an Amazon SNS Limit Increase case in the Amazon Web Services Support Center.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_security_exception.InvalidSecurityException: <p>The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.replay_limit_exceeded_exception.ReplayLimitExceededException: <p>Indicates that the request parameter has exceeded the maximum number of concurrent message replays.</p>
            capo_sns.errors.subscription_limit_exceeded_exception.SubscriptionLimitExceededException: <p>Indicates that the customer already owns the maximum allowed number of subscriptions.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.subscribe_input.SubscribeInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.subscribe_response.SubscribeResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.subscribe

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.subscribe.async_subscribe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.subscribe_input.SubscribeInput = {
            "topic_arn": topic_arn,
            "protocol": protocol,
        }
        if endpoint is not None:
            input_["endpoint"] = endpoint
        if attributes is not None:
            input_["attributes"] = attributes
        if return_subscription_arn is not None:
            input_["return_subscription_arn"] = return_subscription_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_sns.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_sns.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.tag_resource_response.TagResourceResponse":
        """<p>Add tags to the specified Amazon SNS topic. For an overview, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html">Amazon SNS Tags</a> in the <i>Amazon SNS Developer Guide</i>.</p> <p>When you use topic tags, keep the following guidelines in mind:</p> <ul> <li> <p>Adding more than 50 tags to a topic isn't recommended.</p> </li> <li> <p>Tags don't have any semantic meaning. Amazon SNS interprets tags as character strings.</p> </li> <li> <p>Tags are case-sensitive.</p> </li> <li> <p>A new tag with a key identical to that of an existing tag overwrites the existing tag.</p> </li> <li> <p>Tagging actions are limited to 10 TPS per Amazon Web Services account, per Amazon Web Services Region. If your application requires a higher throughput, file a <a href="https://console.aws.amazon.com/support/home#/case/create?issueType=technical">technical support request</a>.</p> </li> </ul>

        Args:
            resource_arn: <p>The ARN of the topic to which to add tags.</p>
            tags: <p>The tags to be added to the specified topic. A tag consists of a required key and an optional value.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.concurrent_access_exception.ConcurrentAccessException: <p>Can't perform multiple operations on a tag simultaneously. Perform the operations sequentially.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.resource_not_found_exception.ResourceNotFoundException: <p>Can’t perform the action on the specified resource. Make sure that the resource exists.</p>
            capo_sns.errors.stale_tag_exception.StaleTagException: <p>A tag has been added to a resource with the same ARN as a deleted resource. Wait a short while and then retry the operation.</p>
            capo_sns.errors.tag_limit_exceeded_exception.TagLimitExceededException: <p>Can't add more than 50 tags to a topic.</p>
            capo_sns.errors.tag_policy_exception.TagPolicyException: <p>The request doesn't comply with the IAM tag policy. Correct your request and then retry it.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.tag_resource_request.TagResourceRequest = {
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

    async def unsubscribe(
        self,
        subscription_arn: "capo_sns.types.subscription_arn.subscriptionARN",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> None:
        """<p>Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic's owner can unsubscribe, and an Amazon Web Services signature is required. If the <code>Unsubscribe</code> call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the <code>Unsubscribe</code> request was unintended.</p> <p>This action is throttled at 100 transactions per second (TPS).</p>

        Args:
            subscription_arn: <p>The ARN of the subscription to be deleted.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.invalid_security_exception.InvalidSecurityException: <p>The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.</p>
            capo_sns.errors.not_found_exception.NotFoundException: <p>Indicates that the requested resource does not exist.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.unsubscribe_input.UnsubscribeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_sns._operations.amazon_simple_notification_service.unsubscribe

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.unsubscribe.async_unsubscribe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.unsubscribe_input.UnsubscribeInput = {
            "subscription_arn": subscription_arn
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
        resource_arn: "capo_sns.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_sns.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from the specified Amazon SNS topic. For an overview, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html">Amazon SNS Tags</a> in the <i>Amazon SNS Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The ARN of the topic from which to remove tags.</p>
            tag_keys: <p>The list of tag keys to remove from the specified topic.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.concurrent_access_exception.ConcurrentAccessException: <p>Can't perform multiple operations on a tag simultaneously. Perform the operations sequentially.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.resource_not_found_exception.ResourceNotFoundException: <p>Can’t perform the action on the specified resource. Make sure that the resource exists.</p>
            capo_sns.errors.stale_tag_exception.StaleTagException: <p>A tag has been added to a resource with the same ARN as a deleted resource. Wait a short while and then retry the operation.</p>
            capo_sns.errors.tag_limit_exceeded_exception.TagLimitExceededException: <p>Can't add more than 50 tags to a topic.</p>
            capo_sns.errors.tag_policy_exception.TagPolicyException: <p>The request doesn't comply with the IAM tag policy. Correct your request and then retry it.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.untag_resource_request.UntagResourceRequest = {
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

    async def verify_sms_sandbox_phone_number(
        self,
        phone_number: "capo_sns.types.phone_number_string.PhoneNumberString",
        one_time_password: "capo_sns.types.otp_code.OTPCode",
        *,
        config_overrides: Optional[AsyncSNSClientConfig] = None,
    ) -> "capo_sns.types.verify_sms_sandbox_phone_number_result.VerifySMSSandboxPhoneNumberResult":
        """<p>Verifies a destination phone number with a one-time password (OTP) for the calling Amazon Web Services account.</p> <p>When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the <i>SMS sandbox</i>. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html">SMS sandbox</a> in the <i>Amazon SNS Developer Guide</i>.</p>

        Args:
            phone_number: <p>The destination phone number to verify.</p>
            one_time_password: <p>The OTP sent to the destination number from the <code>CreateSMSSandBoxPhoneNumber</code> call.</p>

        Raises:
            capo_sns.errors.authorization_error_exception.AuthorizationErrorException: <p>Indicates that the user has been denied access to the requested resource.</p>
            capo_sns.errors.internal_error_exception.InternalErrorException: <p>Indicates an internal service error.</p>
            capo_sns.errors.invalid_parameter_exception.InvalidParameterException: <p>Indicates that a request parameter does not comply with the associated constraints.</p>
            capo_sns.errors.resource_not_found_exception.ResourceNotFoundException: <p>Can’t perform the action on the specified resource. Make sure that the resource exists.</p>
            capo_sns.errors.throttled_exception.ThrottledException: <p>Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.</p>
            capo_sns.errors.verification_exception.VerificationException: <p>Indicates that the one-time password (OTP) used for verification is invalid.</p>
            capo_sns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sns.types.verify_sms_sandbox_phone_number_input.VerifySMSSandboxPhoneNumberInput]",
        ) -> AsyncOperationResponse[
            "capo_sns.types.verify_sms_sandbox_phone_number_result.VerifySMSSandboxPhoneNumberResult"
        ]:
            import capo_sns._operations.amazon_simple_notification_service.verify_sms_sandbox_phone_number

            (
                output,
                http_response,
            ) = await capo_sns._operations.amazon_simple_notification_service.verify_sms_sandbox_phone_number.async_verify_sms_sandbox_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sns.types.verify_sms_sandbox_phone_number_input.VerifySMSSandboxPhoneNumberInput = {
            "phone_number": phone_number,
            "one_time_password": one_time_password,
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
