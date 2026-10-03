"""Generated from Smithy shape ``com.amazonaws.ses#SimpleEmailService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_ses._auth._signers
import capo_ses._auth._sigv4
from capo_ses._auth._identity import Credentials
from capo_ses._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ses._auth._zapros_handler import AuthMiddleware
from capo_ses._pagination import resolve_path as _resolve_path
from capo_ses._services._aws_config import aaws_config
from capo_ses._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_ses.types.address
    import capo_ses.types.address_list
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.behavior_on_mx_failure
    import capo_ses.types.bounced_recipient_info_list
    import capo_ses.types.bulk_email_destination_list
    import capo_ses.types.clone_receipt_rule_set_request
    import capo_ses.types.clone_receipt_rule_set_response
    import capo_ses.types.configuration_set
    import capo_ses.types.configuration_set_attribute_list
    import capo_ses.types.configuration_set_name
    import capo_ses.types.create_configuration_set_event_destination_request
    import capo_ses.types.create_configuration_set_event_destination_response
    import capo_ses.types.create_configuration_set_request
    import capo_ses.types.create_configuration_set_response
    import capo_ses.types.create_configuration_set_tracking_options_request
    import capo_ses.types.create_configuration_set_tracking_options_response
    import capo_ses.types.create_custom_verification_email_template_request
    import capo_ses.types.create_receipt_filter_request
    import capo_ses.types.create_receipt_filter_response
    import capo_ses.types.create_receipt_rule_request
    import capo_ses.types.create_receipt_rule_response
    import capo_ses.types.create_receipt_rule_set_request
    import capo_ses.types.create_receipt_rule_set_response
    import capo_ses.types.create_template_request
    import capo_ses.types.create_template_response
    import capo_ses.types.delete_configuration_set_event_destination_request
    import capo_ses.types.delete_configuration_set_event_destination_response
    import capo_ses.types.delete_configuration_set_request
    import capo_ses.types.delete_configuration_set_response
    import capo_ses.types.delete_configuration_set_tracking_options_request
    import capo_ses.types.delete_configuration_set_tracking_options_response
    import capo_ses.types.delete_custom_verification_email_template_request
    import capo_ses.types.delete_identity_policy_request
    import capo_ses.types.delete_identity_policy_response
    import capo_ses.types.delete_identity_request
    import capo_ses.types.delete_identity_response
    import capo_ses.types.delete_receipt_filter_request
    import capo_ses.types.delete_receipt_filter_response
    import capo_ses.types.delete_receipt_rule_request
    import capo_ses.types.delete_receipt_rule_response
    import capo_ses.types.delete_receipt_rule_set_request
    import capo_ses.types.delete_receipt_rule_set_response
    import capo_ses.types.delete_template_request
    import capo_ses.types.delete_template_response
    import capo_ses.types.delete_verified_email_address_request
    import capo_ses.types.delivery_options
    import capo_ses.types.describe_active_receipt_rule_set_request
    import capo_ses.types.describe_active_receipt_rule_set_response
    import capo_ses.types.describe_configuration_set_request
    import capo_ses.types.describe_configuration_set_response
    import capo_ses.types.describe_receipt_rule_request
    import capo_ses.types.describe_receipt_rule_response
    import capo_ses.types.describe_receipt_rule_set_request
    import capo_ses.types.describe_receipt_rule_set_response
    import capo_ses.types.destination
    import capo_ses.types.domain
    import capo_ses.types.enabled
    import capo_ses.types.event_destination
    import capo_ses.types.event_destination_name
    import capo_ses.types.explanation
    import capo_ses.types.failure_redirection_url
    import capo_ses.types.from_address
    import capo_ses.types.get_account_sending_enabled_response
    import capo_ses.types.get_custom_verification_email_template_request
    import capo_ses.types.get_custom_verification_email_template_response
    import capo_ses.types.get_identity_dkim_attributes_request
    import capo_ses.types.get_identity_dkim_attributes_response
    import capo_ses.types.get_identity_mail_from_domain_attributes_request
    import capo_ses.types.get_identity_mail_from_domain_attributes_response
    import capo_ses.types.get_identity_notification_attributes_request
    import capo_ses.types.get_identity_notification_attributes_response
    import capo_ses.types.get_identity_policies_request
    import capo_ses.types.get_identity_policies_response
    import capo_ses.types.get_identity_verification_attributes_request
    import capo_ses.types.get_identity_verification_attributes_response
    import capo_ses.types.get_send_quota_response
    import capo_ses.types.get_send_statistics_response
    import capo_ses.types.get_template_request
    import capo_ses.types.get_template_response
    import capo_ses.types.identity
    import capo_ses.types.identity_list
    import capo_ses.types.identity_type
    import capo_ses.types.list_configuration_sets_request
    import capo_ses.types.list_configuration_sets_response
    import capo_ses.types.list_custom_verification_email_templates_request
    import capo_ses.types.list_custom_verification_email_templates_response
    import capo_ses.types.list_identities_request
    import capo_ses.types.list_identities_response
    import capo_ses.types.list_identity_policies_request
    import capo_ses.types.list_identity_policies_response
    import capo_ses.types.list_receipt_filters_request
    import capo_ses.types.list_receipt_filters_response
    import capo_ses.types.list_receipt_rule_sets_request
    import capo_ses.types.list_receipt_rule_sets_response
    import capo_ses.types.list_templates_request
    import capo_ses.types.list_templates_response
    import capo_ses.types.list_verified_email_addresses_response
    import capo_ses.types.mail_from_domain_name
    import capo_ses.types.max_items
    import capo_ses.types.max_results
    import capo_ses.types.message
    import capo_ses.types.message_dsn
    import capo_ses.types.message_id
    import capo_ses.types.message_tag_list
    import capo_ses.types.next_token
    import capo_ses.types.notification_topic
    import capo_ses.types.notification_type
    import capo_ses.types.policy
    import capo_ses.types.policy_name
    import capo_ses.types.policy_name_list
    import capo_ses.types.put_configuration_set_delivery_options_request
    import capo_ses.types.put_configuration_set_delivery_options_response
    import capo_ses.types.put_identity_policy_request
    import capo_ses.types.put_identity_policy_response
    import capo_ses.types.raw_message
    import capo_ses.types.receipt_filter
    import capo_ses.types.receipt_filter_name
    import capo_ses.types.receipt_rule
    import capo_ses.types.receipt_rule_name
    import capo_ses.types.receipt_rule_names_list
    import capo_ses.types.receipt_rule_set_name
    import capo_ses.types.reorder_receipt_rule_set_request
    import capo_ses.types.reorder_receipt_rule_set_response
    import capo_ses.types.send_bounce_request
    import capo_ses.types.send_bounce_response
    import capo_ses.types.send_bulk_templated_email_request
    import capo_ses.types.send_bulk_templated_email_response
    import capo_ses.types.send_custom_verification_email_request
    import capo_ses.types.send_custom_verification_email_response
    import capo_ses.types.send_email_request
    import capo_ses.types.send_email_response
    import capo_ses.types.send_raw_email_request
    import capo_ses.types.send_raw_email_response
    import capo_ses.types.send_templated_email_request
    import capo_ses.types.send_templated_email_response
    import capo_ses.types.set_active_receipt_rule_set_request
    import capo_ses.types.set_active_receipt_rule_set_response
    import capo_ses.types.set_identity_dkim_enabled_request
    import capo_ses.types.set_identity_dkim_enabled_response
    import capo_ses.types.set_identity_feedback_forwarding_enabled_request
    import capo_ses.types.set_identity_feedback_forwarding_enabled_response
    import capo_ses.types.set_identity_headers_in_notifications_enabled_request
    import capo_ses.types.set_identity_headers_in_notifications_enabled_response
    import capo_ses.types.set_identity_mail_from_domain_request
    import capo_ses.types.set_identity_mail_from_domain_response
    import capo_ses.types.set_identity_notification_topic_request
    import capo_ses.types.set_identity_notification_topic_response
    import capo_ses.types.set_receipt_rule_position_request
    import capo_ses.types.set_receipt_rule_position_response
    import capo_ses.types.subject
    import capo_ses.types.success_redirection_url
    import capo_ses.types.template
    import capo_ses.types.template_content
    import capo_ses.types.template_data
    import capo_ses.types.template_name
    import capo_ses.types.test_render_template_request
    import capo_ses.types.test_render_template_response
    import capo_ses.types.tracking_options
    import capo_ses.types.update_account_sending_enabled_request
    import capo_ses.types.update_configuration_set_event_destination_request
    import capo_ses.types.update_configuration_set_event_destination_response
    import capo_ses.types.update_configuration_set_reputation_metrics_enabled_request
    import capo_ses.types.update_configuration_set_sending_enabled_request
    import capo_ses.types.update_configuration_set_tracking_options_request
    import capo_ses.types.update_configuration_set_tracking_options_response
    import capo_ses.types.update_custom_verification_email_template_request
    import capo_ses.types.update_receipt_rule_request
    import capo_ses.types.update_receipt_rule_response
    import capo_ses.types.update_template_request
    import capo_ses.types.update_template_response
    import capo_ses.types.verify_domain_dkim_request
    import capo_ses.types.verify_domain_dkim_response
    import capo_ses.types.verify_domain_identity_request
    import capo_ses.types.verify_domain_identity_response
    import capo_ses.types.verify_email_address_request
    import capo_ses.types.verify_email_identity_request
    import capo_ses.types.verify_email_identity_response


class AsyncSESClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSESClient:
    """A client for the ``SES`` service.

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
        self._config = AsyncSESClientConfig(
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
        self, config_overrides: Optional[AsyncSESClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSESClientConfig = config_overrides or {}
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

    async def clone_receipt_rule_set(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        original_rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.clone_receipt_rule_set_response.CloneReceiptRuleSetResponse":
        """<p>Creates a receipt rule set by cloning an existing one. All receipt rules and configurations are copied to the new receipt rule set and are completely independent of the source rule set.</p> <p>For information about setting up rule sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-concepts-rules">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the rule set to create. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Start and end with a letter or number.</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>
            original_rule_set_name: <p>The name of the rule set to clone.</p>

        Raises:
            capo_ses.errors.already_exists_exception.AlreadyExistsException: <p>Indicates that a resource could not be created because of a naming conflict.</p>
            capo_ses.errors.limit_exceeded_exception.LimitExceededException: <p>Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException: <p>Indicates that the provided receipt rule set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CloneReceiptRuleSet
            The following example creates a receipt rule set by cloning an existing one:

            >>> await client.clone_receipt_rule_set(rule_set_name='RuleSetToCreate', original_rule_set_name='RuleSetToClone')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.clone_receipt_rule_set_request.CloneReceiptRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.clone_receipt_rule_set_response.CloneReceiptRuleSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.clone_receipt_rule_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.clone_receipt_rule_set.async_clone_receipt_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.clone_receipt_rule_set_request.CloneReceiptRuleSetRequest = {
            "rule_set_name": rule_set_name,
            "original_rule_set_name": original_rule_set_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration_set(
        self,
        configuration_set: "capo_ses.types.configuration_set.ConfigurationSet",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.create_configuration_set_response.CreateConfigurationSetResponse":
        """<p>Creates a configuration set.</p> <p>Configuration sets enable you to publish email sending events. For information about using configuration sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            configuration_set: <p>A data structure that contains the name of the configuration set.</p>

        Raises:
            capo_ses.errors.configuration_set_already_exists_exception.ConfigurationSetAlreadyExistsException: <p>Indicates that the configuration set could not be created because of a naming conflict.</p>
            capo_ses.errors.invalid_configuration_set_exception.InvalidConfigurationSetException: <p>Indicates that the configuration set is invalid. See the error message for details.</p>
            capo_ses.errors.limit_exceeded_exception.LimitExceededException: <p>Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.create_configuration_set_request.CreateConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.create_configuration_set_response.CreateConfigurationSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.create_configuration_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.create_configuration_set.async_create_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.create_configuration_set_request.CreateConfigurationSetRequest = {
            "configuration_set": configuration_set
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        event_destination: "capo_ses.types.event_destination.EventDestination",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.create_configuration_set_event_destination_response.CreateConfigurationSetEventDestinationResponse":
        """<p>Creates a configuration set event destination.</p> <note> <p>When you create or update an event destination, you must provide one, and only one, destination. The destination can be CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).</p> </note> <p>An event destination is the Amazon Web Services service to which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that the event destination should be associated with.</p>
            event_destination: <p>An object that describes the Amazon Web Services service that email sending event where information is published.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.event_destination_already_exists_exception.EventDestinationAlreadyExistsException: <p>Indicates that the event destination could not be created because of a naming conflict.</p>
            capo_ses.errors.invalid_cloud_watch_destination_exception.InvalidCloudWatchDestinationException: <p>Indicates that the Amazon CloudWatch destination is invalid. See the error message for details.</p>
            capo_ses.errors.invalid_firehose_destination_exception.InvalidFirehoseDestinationException: <p>Indicates that the Amazon Kinesis Firehose destination is invalid. See the error message for details.</p>
            capo_ses.errors.invalid_sns_destination_exception.InvalidSNSDestinationException: <p>Indicates that the Amazon Simple Notification Service (Amazon SNS) destination is invalid. See the error message for details.</p>
            capo_ses.errors.limit_exceeded_exception.LimitExceededException: <p>Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.create_configuration_set_event_destination_request.CreateConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.create_configuration_set_event_destination_response.CreateConfigurationSetEventDestinationResponse"
        ]:
            import capo_ses._operations.simple_email_service.create_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.create_configuration_set_event_destination.async_create_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.create_configuration_set_event_destination_request.CreateConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination": event_destination,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration_set_tracking_options(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        tracking_options: "capo_ses.types.tracking_options.TrackingOptions",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.create_configuration_set_tracking_options_response.CreateConfigurationSetTrackingOptionsResponse":
        """<p>Creates an association between a configuration set and a custom domain for open and click event tracking. </p> <p>By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html">Amazon SES Developer Guide</a>.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that the tracking options should be associated with.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.invalid_tracking_options_exception.InvalidTrackingOptionsException: <p>Indicates that the custom domain to be used for open and click tracking redirects is invalid. This error appears most often in the following situations:</p> <ul> <li> <p>When the tracking domain you specified is not verified in Amazon SES.</p> </li> <li> <p>When the tracking domain you specified is not a valid domain or subdomain.</p> </li> </ul>
            capo_ses.errors.tracking_options_already_exists_exception.TrackingOptionsAlreadyExistsException: <p>Indicates that the configuration set you specified already contains a TrackingOptions object.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.create_configuration_set_tracking_options_request.CreateConfigurationSetTrackingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.create_configuration_set_tracking_options_response.CreateConfigurationSetTrackingOptionsResponse"
        ]:
            import capo_ses._operations.simple_email_service.create_configuration_set_tracking_options

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.create_configuration_set_tracking_options.async_create_configuration_set_tracking_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.create_configuration_set_tracking_options_request.CreateConfigurationSetTrackingOptionsRequest = {
            "configuration_set_name": configuration_set_name,
            "tracking_options": tracking_options,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_verification_email_template(
        self,
        template_name: "capo_ses.types.template_name.TemplateName",
        from_email_address: "capo_ses.types.from_address.FromAddress",
        template_subject: "capo_ses.types.subject.Subject",
        template_content: "capo_ses.types.template_content.TemplateContent",
        success_redirection_url: "capo_ses.types.success_redirection_url.SuccessRedirectionURL",
        failure_redirection_url: "capo_ses.types.failure_redirection_url.FailureRedirectionURL",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> None:
        """<p>Creates a new custom verification email template.</p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using Custom Verification Email Templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the custom verification email template.</p>
            from_email_address: <p>The email address that the custom verification email is sent from.</p>
            template_subject: <p>The subject line of the custom verification email.</p>
            template_content: <p>The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Custom Verification Email Frequently Asked Questions</a> in the <i>Amazon SES Developer Guide</i>.</p>
            success_redirection_url: <p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>
            failure_redirection_url: <p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>

        Raises:
            capo_ses.errors.custom_verification_email_invalid_content_exception.CustomVerificationEmailInvalidContentException: <p>Indicates that custom verification email template provided content is invalid.</p>
            capo_ses.errors.custom_verification_email_template_already_exists_exception.CustomVerificationEmailTemplateAlreadyExistsException: <p>Indicates that a custom verification email template with the name you specified already exists.</p>
            capo_ses.errors.from_email_address_not_verified_exception.FromEmailAddressNotVerifiedException: <p>Indicates that the sender address specified for a custom verification email is not verified, and is therefore not eligible to send the custom verification email. </p>
            capo_ses.errors.limit_exceeded_exception.LimitExceededException: <p>Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.create_custom_verification_email_template_request.CreateCustomVerificationEmailTemplateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ses._operations.simple_email_service.create_custom_verification_email_template

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.create_custom_verification_email_template.async_create_custom_verification_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.create_custom_verification_email_template_request.CreateCustomVerificationEmailTemplateRequest = {
            "template_name": template_name,
            "from_email_address": from_email_address,
            "template_subject": template_subject,
            "template_content": template_content,
            "success_redirection_url": success_redirection_url,
            "failure_redirection_url": failure_redirection_url,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_receipt_filter(
        self,
        filter: "capo_ses.types.receipt_filter.ReceiptFilter",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.create_receipt_filter_response.CreateReceiptFilterResponse":
        """<p>Creates a new IP address filter.</p> <p>For information about setting up IP address filters, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-ip-filtering-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            filter: <p>A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.</p>

        Raises:
            capo_ses.errors.already_exists_exception.AlreadyExistsException: <p>Indicates that a resource could not be created because of a naming conflict.</p>
            capo_ses.errors.limit_exceeded_exception.LimitExceededException: <p>Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateReceiptFilter
            The following example creates a new IP address filter:

            >>> await client.create_receipt_filter(filter={'Name': 'MyFilter', 'IpFilter': {'Policy': 'Allow', 'Cidr': '1.2.3.4/24'}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.create_receipt_filter_request.CreateReceiptFilterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.create_receipt_filter_response.CreateReceiptFilterResponse"
        ]:
            import capo_ses._operations.simple_email_service.create_receipt_filter

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.create_receipt_filter.async_create_receipt_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.create_receipt_filter_request.CreateReceiptFilterRequest = {
            "filter": filter
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_receipt_rule(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        rule: "capo_ses.types.receipt_rule.ReceiptRule",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        after: Optional["capo_ses.types.receipt_rule_name.ReceiptRuleName"] = None,
    ) -> "capo_ses.types.create_receipt_rule_response.CreateReceiptRuleResponse":
        """<p>Creates a receipt rule.</p> <p>For information about setting up receipt rules, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the rule set where the receipt rule is added.</p>
            after: <p>The name of an existing rule after which the new rule is placed. If this parameter is null, the new rule is inserted at the beginning of the rule list.</p>
            rule: <p>A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.</p>

        Raises:
            capo_ses.errors.already_exists_exception.AlreadyExistsException: <p>Indicates that a resource could not be created because of a naming conflict.</p>
            capo_ses.errors.invalid_lambda_function_exception.InvalidLambdaFunctionException: <p>Indicates that the provided Amazon Web Services Lambda function is invalid, or that Amazon SES could not execute the provided function, possibly due to permissions issues. For information about giving permissions, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.invalid_s3_configuration_exception.InvalidS3ConfigurationException: <p>Indicates that the provided Amazon S3 bucket or Amazon Web Services KMS encryption key is invalid, or that Amazon SES could not publish to the bucket, possibly due to permissions issues. For information about giving permissions, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.invalid_sns_topic_exception.InvalidSnsTopicException: <p>Indicates that the provided Amazon SNS topic is invalid, or that Amazon SES could not publish to the topic, possibly due to permissions issues. For information about giving permissions, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.limit_exceeded_exception.LimitExceededException: <p>Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.rule_does_not_exist_exception.RuleDoesNotExistException: <p>Indicates that the provided receipt rule does not exist.</p>
            capo_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException: <p>Indicates that the provided receipt rule set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateReceiptRule
            The following example creates a new receipt rule:

            >>> await client.create_receipt_rule(rule_set_name='MyRuleSet', after='', rule={'TlsPolicy': 'Optional', 'Enabled': True, 'Name': 'MyRule', 'Actions': [{'S3Action': {'ObjectKeyPrefix': 'email', 'BucketName': 'MyBucket'}}], 'ScanEnabled': True})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.create_receipt_rule_request.CreateReceiptRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.create_receipt_rule_response.CreateReceiptRuleResponse"
        ]:
            import capo_ses._operations.simple_email_service.create_receipt_rule

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.create_receipt_rule.async_create_receipt_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.create_receipt_rule_request.CreateReceiptRuleRequest = {
            "rule_set_name": rule_set_name,
            "rule": rule,
        }
        if after is not None:
            input_["after"] = after

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_receipt_rule_set(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.create_receipt_rule_set_response.CreateReceiptRuleSetResponse":
        """<p>Creates an empty receipt rule set.</p> <p>For information about setting up receipt rule sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-concepts-rules">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the rule set to create. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Start and end with a letter or number.</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>

        Raises:
            capo_ses.errors.already_exists_exception.AlreadyExistsException: <p>Indicates that a resource could not be created because of a naming conflict.</p>
            capo_ses.errors.limit_exceeded_exception.LimitExceededException: <p>Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateReceiptRuleSet
            The following example creates an empty receipt rule set:

            >>> await client.create_receipt_rule_set(rule_set_name='MyRuleSet')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.create_receipt_rule_set_request.CreateReceiptRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.create_receipt_rule_set_response.CreateReceiptRuleSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.create_receipt_rule_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.create_receipt_rule_set.async_create_receipt_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.create_receipt_rule_set_request.CreateReceiptRuleSetRequest = {
            "rule_set_name": rule_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_template(
        self,
        template: "capo_ses.types.template.Template",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.create_template_response.CreateTemplateResponse":
        """<p>Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single operation. For more information, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-api.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template: <p>The content of the email, composed of a subject line and either an HTML part or a text-only part.</p>

        Raises:
            capo_ses.errors.already_exists_exception.AlreadyExistsException: <p>Indicates that a resource could not be created because of a naming conflict.</p>
            capo_ses.errors.invalid_template_exception.InvalidTemplateException: <p>Indicates that the template that you specified could not be rendered. This issue may occur when a template refers to a partial that does not exist.</p>
            capo_ses.errors.limit_exceeded_exception.LimitExceededException: <p>Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.create_template_request.CreateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.create_template_response.CreateTemplateResponse"
        ]:
            import capo_ses._operations.simple_email_service.create_template

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.create_template.async_create_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.create_template_request.CreateTemplateRequest = {
            "template": template
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_set(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.delete_configuration_set_response.DeleteConfigurationSetResponse":
        """<p>Deletes a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set to delete.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_configuration_set_request.DeleteConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.delete_configuration_set_response.DeleteConfigurationSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.delete_configuration_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_configuration_set.async_delete_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_configuration_set_request.DeleteConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        event_destination_name: "capo_ses.types.event_destination_name.EventDestinationName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.delete_configuration_set_event_destination_response.DeleteConfigurationSetEventDestinationResponse":
        """<p>Deletes a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set from which to delete the event destination.</p>
            event_destination_name: <p>The name of the event destination to delete.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.event_destination_does_not_exist_exception.EventDestinationDoesNotExistException: <p>Indicates that the event destination does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_configuration_set_event_destination_request.DeleteConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.delete_configuration_set_event_destination_response.DeleteConfigurationSetEventDestinationResponse"
        ]:
            import capo_ses._operations.simple_email_service.delete_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_configuration_set_event_destination.async_delete_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_configuration_set_event_destination_request.DeleteConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_set_tracking_options(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.delete_configuration_set_tracking_options_response.DeleteConfigurationSetTrackingOptionsResponse":
        """<p>Deletes an association between a configuration set and a custom domain for open and click event tracking.</p> <p>By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html">Amazon SES Developer Guide</a>.</p> <note> <p>Deleting this kind of association results in emails sent using the specified configuration set to capture open and click events using the standard, Amazon SES-operated domains.</p> </note>

        Args:
            configuration_set_name: <p>The name of the configuration set.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.tracking_options_does_not_exist_exception.TrackingOptionsDoesNotExistException: <p>Indicates that the TrackingOptions object you specified does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_configuration_set_tracking_options_request.DeleteConfigurationSetTrackingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.delete_configuration_set_tracking_options_response.DeleteConfigurationSetTrackingOptionsResponse"
        ]:
            import capo_ses._operations.simple_email_service.delete_configuration_set_tracking_options

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_configuration_set_tracking_options.async_delete_configuration_set_tracking_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_configuration_set_tracking_options_request.DeleteConfigurationSetTrackingOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_verification_email_template(
        self,
        template_name: "capo_ses.types.template_name.TemplateName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> None:
        """<p>Deletes an existing custom verification email template. </p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using Custom Verification Email Templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the custom verification email template to delete.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_custom_verification_email_template_request.DeleteCustomVerificationEmailTemplateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ses._operations.simple_email_service.delete_custom_verification_email_template

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_custom_verification_email_template.async_delete_custom_verification_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_custom_verification_email_template_request.DeleteCustomVerificationEmailTemplateRequest = {
            "template_name": template_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_identity(
        self,
        identity: "capo_ses.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.delete_identity_response.DeleteIdentityResponse":
        """<p>Deletes the specified identity (an email address or a domain) from the list of verified identities.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            identity: <p>The identity to be removed from the list of identities for the Amazon Web Services account.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteIdentity
            The following example deletes an identity from the list of identities that have been submitted for verification with Amazon SES:

            >>> await client.delete_identity(identity='user@example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_identity_request.DeleteIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.delete_identity_response.DeleteIdentityResponse"
        ]:
            import capo_ses._operations.simple_email_service.delete_identity

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_identity.async_delete_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_identity_request.DeleteIdentityRequest = {
            "identity": identity
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_identity_policy(
        self,
        identity: "capo_ses.types.identity.Identity",
        policy_name: "capo_ses.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.delete_identity_policy_response.DeleteIdentityPolicyResponse":
        """<p>Deletes the specified sending authorization policy for the given identity (an email address or a domain). This operation returns successfully even if a policy with the specified name does not exist.</p> <note> <p>This operation is for the identity owner only. If you have not verified the identity, it returns an error.</p> </note> <p>Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            identity: <p>The identity that is associated with the policy to delete. You can specify the identity by using its name or by using its Amazon Resource Name (ARN). Examples: <code>user@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p> <p>To successfully call this operation, you must own the identity.</p>
            policy_name: <p>The name of the policy to be deleted.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteIdentityPolicy
            The following example deletes a sending authorization policy for an identity:

            >>> await client.delete_identity_policy(identity='user@example.com', policy_name='MyPolicy')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_identity_policy_request.DeleteIdentityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.delete_identity_policy_response.DeleteIdentityPolicyResponse"
        ]:
            import capo_ses._operations.simple_email_service.delete_identity_policy

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_identity_policy.async_delete_identity_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_identity_policy_request.DeleteIdentityPolicyRequest = {
            "identity": identity,
            "policy_name": policy_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_receipt_filter(
        self,
        filter_name: "capo_ses.types.receipt_filter_name.ReceiptFilterName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.delete_receipt_filter_response.DeleteReceiptFilterResponse":
        """<p>Deletes the specified IP address filter.</p> <p>For information about managing IP address filters, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-ip-filtering-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            filter_name: <p>The name of the IP address filter to delete.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteReceiptFilter
            The following example deletes an IP address filter:

            >>> await client.delete_receipt_filter(filter_name='MyFilter')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_receipt_filter_request.DeleteReceiptFilterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.delete_receipt_filter_response.DeleteReceiptFilterResponse"
        ]:
            import capo_ses._operations.simple_email_service.delete_receipt_filter

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_receipt_filter.async_delete_receipt_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_receipt_filter_request.DeleteReceiptFilterRequest = {
            "filter_name": filter_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_receipt_rule(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        rule_name: "capo_ses.types.receipt_rule_name.ReceiptRuleName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.delete_receipt_rule_response.DeleteReceiptRuleResponse":
        """<p>Deletes the specified receipt rule.</p> <p>For information about managing receipt rules, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the receipt rule set that contains the receipt rule to delete.</p>
            rule_name: <p>The name of the receipt rule to delete.</p>

        Raises:
            capo_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException: <p>Indicates that the provided receipt rule set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteReceiptRule
            The following example deletes a receipt rule:

            >>> await client.delete_receipt_rule(rule_set_name='MyRuleSet', rule_name='MyRule')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_receipt_rule_request.DeleteReceiptRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.delete_receipt_rule_response.DeleteReceiptRuleResponse"
        ]:
            import capo_ses._operations.simple_email_service.delete_receipt_rule

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_receipt_rule.async_delete_receipt_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_receipt_rule_request.DeleteReceiptRuleRequest = {
            "rule_set_name": rule_set_name,
            "rule_name": rule_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_receipt_rule_set(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.delete_receipt_rule_set_response.DeleteReceiptRuleSetResponse":
        """<p>Deletes the specified receipt rule set and all of the receipt rules it contains.</p> <note> <p>The currently active rule set cannot be deleted.</p> </note> <p>For information about managing receipt rule sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the receipt rule set to delete.</p>

        Raises:
            capo_ses.errors.cannot_delete_exception.CannotDeleteException: <p>Indicates that the delete operation could not be completed.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteReceiptRuleSet
            The following example deletes a receipt rule set:

            >>> await client.delete_receipt_rule_set(rule_set_name='MyRuleSet')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_receipt_rule_set_request.DeleteReceiptRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.delete_receipt_rule_set_response.DeleteReceiptRuleSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.delete_receipt_rule_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_receipt_rule_set.async_delete_receipt_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_receipt_rule_set_request.DeleteReceiptRuleSetRequest = {
            "rule_set_name": rule_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_template(
        self,
        template_name: "capo_ses.types.template_name.TemplateName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.delete_template_response.DeleteTemplateResponse":
        """<p>Deletes an email template.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the template to be deleted.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_template_request.DeleteTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.delete_template_response.DeleteTemplateResponse"
        ]:
            import capo_ses._operations.simple_email_service.delete_template

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_template.async_delete_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_template_request.DeleteTemplateRequest = {
            "template_name": template_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_verified_email_address(
        self,
        email_address: "capo_ses.types.address.Address",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> None:
        """<p>Deprecated. Use the <code>DeleteIdentity</code> operation to delete email addresses and domains.</p>

        Args:
            email_address: <p>An email address to be removed from the list of verified addresses.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteVerifiedEmailAddress
            The following example deletes an email address from the list of identities that have been submitted for verification with Amazon SES:

            >>> await client.delete_verified_email_address(email_address='user@example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.delete_verified_email_address_request.DeleteVerifiedEmailAddressRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ses._operations.simple_email_service.delete_verified_email_address

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.delete_verified_email_address.async_delete_verified_email_address(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.delete_verified_email_address_request.DeleteVerifiedEmailAddressRequest = {
            "email_address": email_address
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_active_receipt_rule_set(
        self, *, config_overrides: Optional[AsyncSESClientConfig] = None
    ) -> "capo_ses.types.describe_active_receipt_rule_set_response.DescribeActiveReceiptRuleSetResponse":
        """<p>Returns the metadata and receipt rules for the receipt rule set that is currently active.</p> <p>For information about setting up receipt rule sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-concepts-rules">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeActiveReceiptRuleSet
            The following example returns the metadata and receipt rules for the receipt rule set that is currently active:

            >>> await client.describe_active_receipt_rule_set()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.describe_active_receipt_rule_set_request.DescribeActiveReceiptRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.describe_active_receipt_rule_set_response.DescribeActiveReceiptRuleSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.describe_active_receipt_rule_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.describe_active_receipt_rule_set.async_describe_active_receipt_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.describe_active_receipt_rule_set_request.DescribeActiveReceiptRuleSetRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_configuration_set(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        configuration_set_attribute_names: Optional[
            "capo_ses.types.configuration_set_attribute_list.ConfigurationSetAttributeList"
        ] = None,
    ) -> "capo_ses.types.describe_configuration_set_response.DescribeConfigurationSetResponse":
        """<p>Returns the details of the specified configuration set. For information about using configuration sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set to describe.</p>
            configuration_set_attribute_names: <p>A list of configuration set attributes to return.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.describe_configuration_set_request.DescribeConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.describe_configuration_set_response.DescribeConfigurationSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.describe_configuration_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.describe_configuration_set.async_describe_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.describe_configuration_set_request.DescribeConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }
        if configuration_set_attribute_names is not None:
            input_["configuration_set_attribute_names"] = (
                configuration_set_attribute_names
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_receipt_rule(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        rule_name: "capo_ses.types.receipt_rule_name.ReceiptRuleName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.describe_receipt_rule_response.DescribeReceiptRuleResponse":
        """<p>Returns the details of the specified receipt rule.</p> <p>For information about setting up receipt rules, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the receipt rule set that the receipt rule belongs to.</p>
            rule_name: <p>The name of the receipt rule.</p>

        Raises:
            capo_ses.errors.rule_does_not_exist_exception.RuleDoesNotExistException: <p>Indicates that the provided receipt rule does not exist.</p>
            capo_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException: <p>Indicates that the provided receipt rule set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeReceiptRule
            The following example returns the details of a receipt rule:

            >>> await client.describe_receipt_rule(rule_set_name='MyRuleSet', rule_name='MyRule')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.describe_receipt_rule_request.DescribeReceiptRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.describe_receipt_rule_response.DescribeReceiptRuleResponse"
        ]:
            import capo_ses._operations.simple_email_service.describe_receipt_rule

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.describe_receipt_rule.async_describe_receipt_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.describe_receipt_rule_request.DescribeReceiptRuleRequest = {
            "rule_set_name": rule_set_name,
            "rule_name": rule_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_receipt_rule_set(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.describe_receipt_rule_set_response.DescribeReceiptRuleSetResponse":
        """<p>Returns the details of the specified receipt rule set.</p> <p>For information about managing receipt rule sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the receipt rule set to describe.</p>

        Raises:
            capo_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException: <p>Indicates that the provided receipt rule set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeReceiptRuleSet
            The following example returns the metadata and receipt rules of a receipt rule set:

            >>> await client.describe_receipt_rule_set(rule_set_name='MyRuleSet')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.describe_receipt_rule_set_request.DescribeReceiptRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.describe_receipt_rule_set_response.DescribeReceiptRuleSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.describe_receipt_rule_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.describe_receipt_rule_set.async_describe_receipt_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.describe_receipt_rule_set_request.DescribeReceiptRuleSetRequest = {
            "rule_set_name": rule_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account_sending_enabled(
        self, *, config_overrides: Optional[AsyncSESClientConfig] = None
    ) -> "capo_ses.types.get_account_sending_enabled_response.GetAccountSendingEnabledResponse":
        """<p>Returns the email sending status of the Amazon SES account for the current Region.</p> <p>You can execute this operation no more than once per second.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetAccountSendingEnabled
            The following example returns if sending status for an account is enabled. (true / false):

            >>> await client.get_account_sending_enabled()
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_account_sending_enabled_response.GetAccountSendingEnabledResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_account_sending_enabled

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_account_sending_enabled.async_get_account_sending_enabled(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_custom_verification_email_template(
        self,
        template_name: "capo_ses.types.template_name.TemplateName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.get_custom_verification_email_template_response.GetCustomVerificationEmailTemplateResponse":
        """<p>Returns the custom email verification template for the template name you specify.</p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using Custom Verification Email Templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the custom verification email template to retrieve.</p>

        Raises:
            capo_ses.errors.custom_verification_email_template_does_not_exist_exception.CustomVerificationEmailTemplateDoesNotExistException: <p>Indicates that a custom verification email template with the name you specified does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.get_custom_verification_email_template_request.GetCustomVerificationEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_custom_verification_email_template_response.GetCustomVerificationEmailTemplateResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_custom_verification_email_template

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_custom_verification_email_template.async_get_custom_verification_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.get_custom_verification_email_template_request.GetCustomVerificationEmailTemplateRequest = {
            "template_name": template_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_identity_dkim_attributes(
        self,
        identities: "capo_ses.types.identity_list.IdentityList",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.get_identity_dkim_attributes_response.GetIdentityDkimAttributesResponse":
        """<p>Returns the current status of Easy DKIM signing for an entity. For domain name identities, this operation also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES has successfully verified that these tokens have been published.</p> <p>This operation takes a list of identities as input and returns the following information for each:</p> <ul> <li> <p>Whether Easy DKIM signing is enabled or disabled.</p> </li> <li> <p>A set of DKIM tokens that represent the identity. If the identity is an email address, the tokens represent the domain of that address.</p> </li> <li> <p>Whether Amazon SES has successfully verified the DKIM tokens published in the domain's DNS. This information is only returned for domain name identities, not for email addresses.</p> </li> </ul> <p>This operation is throttled at one request per second and can only get DKIM attributes for up to 100 identities at a time.</p> <p>For more information about creating DNS records using DKIM tokens, go to the <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy-managing.html">Amazon SES Developer Guide</a>.</p>

        Args:
            identities: <p>A list of one or more verified identities - email addresses, domains, or both.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetIdentityDkimAttributes
            The following example retrieves the Amazon SES Easy DKIM attributes for a list of identities:

            >>> await client.get_identity_dkim_attributes(identities=['example.com', 'user@example.com'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.get_identity_dkim_attributes_request.GetIdentityDkimAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_identity_dkim_attributes_response.GetIdentityDkimAttributesResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_identity_dkim_attributes

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_identity_dkim_attributes.async_get_identity_dkim_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.get_identity_dkim_attributes_request.GetIdentityDkimAttributesRequest = {
            "identities": identities
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_identity_mail_from_domain_attributes(
        self,
        identities: "capo_ses.types.identity_list.IdentityList",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.get_identity_mail_from_domain_attributes_response.GetIdentityMailFromDomainAttributesResponse":
        """<p>Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains).</p> <p>This operation is throttled at one request per second and can only get custom MAIL FROM attributes for up to 100 identities at a time.</p>

        Args:
            identities: <p>A list of one or more identities.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetIdentityMailFromDomainAttributes
            The following example returns the custom MAIL FROM attributes for an identity:

            >>> await client.get_identity_mail_from_domain_attributes(identities=['example.com'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.get_identity_mail_from_domain_attributes_request.GetIdentityMailFromDomainAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_identity_mail_from_domain_attributes_response.GetIdentityMailFromDomainAttributesResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_identity_mail_from_domain_attributes

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_identity_mail_from_domain_attributes.async_get_identity_mail_from_domain_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.get_identity_mail_from_domain_attributes_request.GetIdentityMailFromDomainAttributesRequest = {
            "identities": identities
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_identity_notification_attributes(
        self,
        identities: "capo_ses.types.identity_list.IdentityList",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.get_identity_notification_attributes_response.GetIdentityNotificationAttributesResponse":
        """<p>Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes.</p> <p>This operation is throttled at one request per second and can only get notification attributes for up to 100 identities at a time.</p> <p>For more information about using notifications with Amazon SES, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications.html">Amazon SES Developer Guide</a>.</p>

        Args:
            identities: <p>A list of one or more identities. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: <code>user@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetIdentityNotificationAttributes
            The following example returns the notification attributes for an identity:

            >>> await client.get_identity_notification_attributes(identities=['example.com'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.get_identity_notification_attributes_request.GetIdentityNotificationAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_identity_notification_attributes_response.GetIdentityNotificationAttributesResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_identity_notification_attributes

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_identity_notification_attributes.async_get_identity_notification_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.get_identity_notification_attributes_request.GetIdentityNotificationAttributesRequest = {
            "identities": identities
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_identity_policies(
        self,
        identity: "capo_ses.types.identity.Identity",
        policy_names: "capo_ses.types.policy_name_list.PolicyNameList",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.get_identity_policies_response.GetIdentityPoliciesResponse":
        """<p>Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.</p> <note> <p>This operation is for the identity owner only. If you have not verified the identity, it returns an error.</p> </note> <p>Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            identity: <p>The identity for which the policies are retrieved. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: <code>user@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p> <p>To successfully call this operation, you must own the identity.</p>
            policy_names: <p>A list of the names of policies to be retrieved. You can retrieve a maximum of 20 policies at a time. If you do not know the names of the policies that are attached to the identity, you can use <code>ListIdentityPolicies</code>.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetIdentityPolicies
            The following example returns a sending authorization policy for an identity:

            >>> await client.get_identity_policies(identity='example.com', policy_names=['MyPolicy'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.get_identity_policies_request.GetIdentityPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_identity_policies_response.GetIdentityPoliciesResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_identity_policies

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_identity_policies.async_get_identity_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.get_identity_policies_request.GetIdentityPoliciesRequest = {
            "identity": identity,
            "policy_names": policy_names,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_identity_verification_attributes(
        self,
        identities: "capo_ses.types.identity_list.IdentityList",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.get_identity_verification_attributes_response.GetIdentityVerificationAttributesResponse":
        """<p>Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity.</p> <p>The verification status of an email address is "Pending" until the email address owner clicks the link within the verification email that Amazon SES sent to that address. If the email address owner clicks the link within 24 hours, the verification status of the email address changes to "Success". If the link is not clicked within 24 hours, the verification status changes to "Failed." In that case, to verify the email address, you must restart the verification process from the beginning.</p> <p>For domain identities, the domain's verification status is "Pending" as Amazon SES searches for the required TXT record in the DNS settings of the domain. When Amazon SES detects the record, the domain's verification status changes to "Success". If Amazon SES is unable to detect the record within 72 hours, the domain's verification status changes to "Failed." In that case, to verify the domain, you must restart the verification process from the beginning.</p> <p>This operation is throttled at one request per second and can only get verification attributes for up to 100 identities at a time.</p>

        Args:
            identities: <p>A list of identities.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetIdentityVerificationAttributes
            The following example returns the verification status and the verification token for a domain identity:

            >>> await client.get_identity_verification_attributes(identities=['example.com'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.get_identity_verification_attributes_request.GetIdentityVerificationAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_identity_verification_attributes_response.GetIdentityVerificationAttributesResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_identity_verification_attributes

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_identity_verification_attributes.async_get_identity_verification_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.get_identity_verification_attributes_request.GetIdentityVerificationAttributesRequest = {
            "identities": identities
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_send_quota(
        self, *, config_overrides: Optional[AsyncSESClientConfig] = None
    ) -> "capo_ses.types.get_send_quota_response.GetSendQuotaResponse":
        """<p>Provides the sending limits for the Amazon SES account. </p> <p>You can execute this operation no more than once per second.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetSendQuota
            The following example returns the Amazon SES sending limits for an AWS account:

            >>> await client.get_send_quota()
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_send_quota_response.GetSendQuotaResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_send_quota

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_send_quota.async_get_send_quota(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_send_statistics(
        self, *, config_overrides: Optional[AsyncSESClientConfig] = None
    ) -> "capo_ses.types.get_send_statistics_response.GetSendStatisticsResponse":
        """<p>Provides sending statistics for the current Amazon Web Services Region. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute period of time.</p> <p>You can execute this operation no more than once per second.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetSendStatistics
            The following example returns Amazon SES sending statistics:

            >>> await client.get_send_statistics()
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_send_statistics_response.GetSendStatisticsResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_send_statistics

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_send_statistics.async_get_send_statistics(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_template(
        self,
        template_name: "capo_ses.types.template_name.TemplateName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.get_template_response.GetTemplateResponse":
        """<p>Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the template to retrieve.</p>

        Raises:
            capo_ses.errors.template_does_not_exist_exception.TemplateDoesNotExistException: <p>Indicates that the Template object you specified does not exist in your Amazon SES account.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.get_template_request.GetTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.get_template_response.GetTemplateResponse"
        ]:
            import capo_ses._operations.simple_email_service.get_template

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.get_template.async_get_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.get_template_request.GetTemplateRequest = {
            "template_name": template_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configuration_sets(
        self,
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        next_token: Optional["capo_ses.types.next_token.NextToken"] = None,
        max_items: Optional["capo_ses.types.max_items.MaxItems"] = None,
    ) -> (
        "capo_ses.types.list_configuration_sets_response.ListConfigurationSetsResponse"
    ):
        """<p>Provides a list of the configuration sets associated with your Amazon SES account in the current Amazon Web Services Region. For information about using configuration sets, see <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html">Monitoring Your Amazon SES Sending Activity</a> in the <i>Amazon SES Developer Guide.</i> </p> <p>You can execute this operation no more than once per second. This operation returns up to 1,000 configuration sets each time it is run. If your Amazon SES account has more than 1,000 configuration sets, this operation also returns <code>NextToken</code>. You can then execute the <code>ListConfigurationSets</code> operation again, passing the <code>NextToken</code> parameter and the value of the NextToken element to retrieve additional results.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListConfigurationSets</code> to indicate the position of the configuration set in the configuration set list.</p>
            max_items: <p>The number of configuration sets to return.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.list_configuration_sets_request.ListConfigurationSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.list_configuration_sets_response.ListConfigurationSetsResponse"
        ]:
            import capo_ses._operations.simple_email_service.list_configuration_sets

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.list_configuration_sets.async_list_configuration_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.list_configuration_sets_request.ListConfigurationSetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_custom_verification_email_templates(
        self,
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        next_token: Optional["capo_ses.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ses.types.max_results.MaxResults"] = None,
    ) -> "capo_ses.types.list_custom_verification_email_templates_response.ListCustomVerificationEmailTemplatesResponse":
        """<p>Lists the existing custom verification email templates for your account in the current Amazon Web Services Region.</p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using Custom Verification Email Templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            next_token: <p>An array the contains the name and creation time stamp for each template in your Amazon SES account.</p>
            max_results: <p>The maximum number of custom verification email templates to return. This value must be at least 1 and less than or equal to 50. If you do not specify a value, or if you specify a value less than 1 or greater than 50, the operation returns up to 50 results.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.list_custom_verification_email_templates_request.ListCustomVerificationEmailTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.list_custom_verification_email_templates_response.ListCustomVerificationEmailTemplatesResponse"
        ]:
            import capo_ses._operations.simple_email_service.list_custom_verification_email_templates

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.list_custom_verification_email_templates.async_list_custom_verification_email_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.list_custom_verification_email_templates_request.ListCustomVerificationEmailTemplatesRequest = {}
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

    async def iter_list_custom_verification_email_templates(
        self,
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        next_token: Optional["capo_ses.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ses.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ses.types.list_custom_verification_email_templates_response.ListCustomVerificationEmailTemplatesResponse]":
        _token = next_token
        while True:
            _response = await self.list_custom_verification_email_templates(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_identities(
        self,
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        identity_type: Optional["capo_ses.types.identity_type.IdentityType"] = None,
        next_token: Optional["capo_ses.types.next_token.NextToken"] = None,
        max_items: Optional["capo_ses.types.max_items.MaxItems"] = None,
    ) -> "capo_ses.types.list_identities_response.ListIdentitiesResponse":
        """<p>Returns a list containing all of the identities (email addresses and domains) for your Amazon Web Services account in the current Amazon Web Services Region, regardless of verification status.</p> <p>You can execute this operation no more than once per second.</p> <note> <p>It's recommended that for successive pagination calls of this API, you continue to the use the same parameter/value pairs as used in the original call, e.g., if you used <code>IdentityType=Domain</code> in the the original call and received a <code>NextToken</code> in the response, you should continue providing the <code>IdentityType=Domain</code> parameter for further <code>NextToken</code> calls; however, if you didn't provide the <code>IdentityType</code> parameter in the original call, then continue to not provide it for successive pagination calls. Using this protocol will ensure consistent results.</p> </note>

        Args:
            identity_type: <p>The type of the identities to list. Possible values are "EmailAddress" and "Domain". If this parameter is omitted, then all identities are listed.</p>
            next_token: <p>The token to use for pagination.</p>
            max_items: <p>The maximum number of identities per page. Possible values are 1-1000 inclusive.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListIdentities
            The following example lists the email address identities that have been submitted for verification with Amazon SES:

            >>> await client.list_identities(identity_type='EmailAddress', next_token='', max_items=123)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.list_identities_request.ListIdentitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.list_identities_response.ListIdentitiesResponse"
        ]:
            import capo_ses._operations.simple_email_service.list_identities

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.list_identities.async_list_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.list_identities_request.ListIdentitiesRequest = {}
        if identity_type is not None:
            input_["identity_type"] = identity_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_identities(
        self,
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        identity_type: Optional["capo_ses.types.identity_type.IdentityType"] = None,
        next_token: Optional["capo_ses.types.next_token.NextToken"] = None,
        max_items: Optional["capo_ses.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_ses.types.identity.Identity]":
        _token = next_token
        while True:
            _response = await self.list_identities(
                config_overrides=config_overrides,
                identity_type=identity_type,
                next_token=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_identity_policies(
        self,
        identity: "capo_ses.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.list_identity_policies_response.ListIdentityPoliciesResponse":
        """<p>Returns a list of sending authorization policies that are attached to the given identity (an email address or a domain). This operation returns only a list. To get the actual policy content, use <code>GetIdentityPolicies</code>.</p> <note> <p>This operation is for the identity owner only. If you have not verified the identity, it returns an error.</p> </note> <p>Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            identity: <p>The identity that is associated with the policy for which the policies are listed. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: <code>user@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p> <p>To successfully call this operation, you must own the identity.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListIdentityPolicies
            The following example returns a list of sending authorization policies that are attached to an identity:

            >>> await client.list_identity_policies(identity='example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.list_identity_policies_request.ListIdentityPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.list_identity_policies_response.ListIdentityPoliciesResponse"
        ]:
            import capo_ses._operations.simple_email_service.list_identity_policies

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.list_identity_policies.async_list_identity_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.list_identity_policies_request.ListIdentityPoliciesRequest = {
            "identity": identity
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_receipt_filters(
        self, *, config_overrides: Optional[AsyncSESClientConfig] = None
    ) -> "capo_ses.types.list_receipt_filters_response.ListReceiptFiltersResponse":
        """<p>Lists the IP address filters associated with your Amazon Web Services account in the current Amazon Web Services Region.</p> <p>For information about managing IP address filters, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-ip-filtering-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListReceiptFilters
            The following example lists the IP address filters that are associated with an AWS account:

            >>> await client.list_receipt_filters()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.list_receipt_filters_request.ListReceiptFiltersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.list_receipt_filters_response.ListReceiptFiltersResponse"
        ]:
            import capo_ses._operations.simple_email_service.list_receipt_filters

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.list_receipt_filters.async_list_receipt_filters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.list_receipt_filters_request.ListReceiptFiltersRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_receipt_rule_sets(
        self,
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        next_token: Optional["capo_ses.types.next_token.NextToken"] = None,
    ) -> "capo_ses.types.list_receipt_rule_sets_response.ListReceiptRuleSetsResponse":
        """<p>Lists the receipt rule sets that exist under your Amazon Web Services account in the current Amazon Web Services Region. If there are additional receipt rule sets to be retrieved, you receive a <code>NextToken</code> that you can provide to the next call to <code>ListReceiptRuleSets</code> to retrieve the additional entries.</p> <p>For information about managing receipt rule sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListReceiptRuleSets</code> to indicate the position in the receipt rule set list.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListReceiptRuleSets
            The following example lists the receipt rule sets that exist under an AWS account:

            >>> await client.list_receipt_rule_sets(next_token='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.list_receipt_rule_sets_request.ListReceiptRuleSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.list_receipt_rule_sets_response.ListReceiptRuleSetsResponse"
        ]:
            import capo_ses._operations.simple_email_service.list_receipt_rule_sets

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.list_receipt_rule_sets.async_list_receipt_rule_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.list_receipt_rule_sets_request.ListReceiptRuleSetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_templates(
        self,
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        next_token: Optional["capo_ses.types.next_token.NextToken"] = None,
        max_items: Optional["capo_ses.types.max_items.MaxItems"] = None,
    ) -> "capo_ses.types.list_templates_response.ListTemplatesResponse":
        """<p>Lists the email templates present in your Amazon SES account in the current Amazon Web Services Region.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListTemplates</code> to indicate the position in the list of email templates.</p>
            max_items: <p>The maximum number of templates to return. This value must be at least 1 and less than or equal to 100. If more than 100 items are requested, the page size will automatically set to 100. If you do not specify a value, 10 is the default page size. </p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.list_templates_request.ListTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.list_templates_response.ListTemplatesResponse"
        ]:
            import capo_ses._operations.simple_email_service.list_templates

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.list_templates.async_list_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.list_templates_request.ListTemplatesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_verified_email_addresses(
        self, *, config_overrides: Optional[AsyncSESClientConfig] = None
    ) -> "capo_ses.types.list_verified_email_addresses_response.ListVerifiedEmailAddressesResponse":
        """<p>Deprecated. Use the <code>ListIdentities</code> operation to list the email addresses and domains associated with your account.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListVerifiedEmailAddresses
            The following example lists all email addresses that have been submitted for verification with Amazon SES:

            >>> await client.list_verified_email_addresses()
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.list_verified_email_addresses_response.ListVerifiedEmailAddressesResponse"
        ]:
            import capo_ses._operations.simple_email_service.list_verified_email_addresses

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.list_verified_email_addresses.async_list_verified_email_addresses(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_delivery_options(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        delivery_options: Optional[
            "capo_ses.types.delivery_options.DeliveryOptions"
        ] = None,
    ) -> "capo_ses.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse":
        """<p>Adds or updates the delivery options for a configuration set.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set.</p>
            delivery_options: <p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.invalid_delivery_options_exception.InvalidDeliveryOptionsException: <p>Indicates that provided delivery option is invalid.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.put_configuration_set_delivery_options_request.PutConfigurationSetDeliveryOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse"
        ]:
            import capo_ses._operations.simple_email_service.put_configuration_set_delivery_options

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.put_configuration_set_delivery_options.async_put_configuration_set_delivery_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.put_configuration_set_delivery_options_request.PutConfigurationSetDeliveryOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if delivery_options is not None:
            input_["delivery_options"] = delivery_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_identity_policy(
        self,
        identity: "capo_ses.types.identity.Identity",
        policy_name: "capo_ses.types.policy_name.PolicyName",
        policy: "capo_ses.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.put_identity_policy_response.PutIdentityPolicyResponse":
        """<p>Adds or updates a sending authorization policy for the specified identity (an email address or a domain).</p> <note> <p>This operation is for the identity owner only. If you have not verified the identity, it returns an error.</p> </note> <p>Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            identity: <p>The identity to which that the policy applies. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: <code>user@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p> <p>To successfully call this operation, you must own the identity.</p>
            policy_name: <p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>
            policy: <p>The text of the policy in JSON format. The policy cannot exceed 4 KB.</p> <p>For information about the syntax of sending authorization policies, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-policies.html">Amazon SES Developer Guide</a>. </p>

        Raises:
            capo_ses.errors.invalid_policy_exception.InvalidPolicyException: <p>Indicates that the provided policy is invalid. Check the error stack for more information about what caused the error.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            PutIdentityPolicy
            The following example adds a sending authorization policy to an identity:

            >>> await client.put_identity_policy(identity='example.com', policy_name='MyPolicy', policy='{"Version":"2008-10-17","Statement":[{"Sid":"stmt1469123904194","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:root"},"Action":["ses:SendEmail","ses:SendRawEmail"],"Resource":"arn:aws:ses:us-east-1:EXAMPLE65304:identity/example.com"}]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.put_identity_policy_request.PutIdentityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.put_identity_policy_response.PutIdentityPolicyResponse"
        ]:
            import capo_ses._operations.simple_email_service.put_identity_policy

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.put_identity_policy.async_put_identity_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.put_identity_policy_request.PutIdentityPolicyRequest = {
            "identity": identity,
            "policy_name": policy_name,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reorder_receipt_rule_set(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        rule_names: "capo_ses.types.receipt_rule_names_list.ReceiptRuleNamesList",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> (
        "capo_ses.types.reorder_receipt_rule_set_response.ReorderReceiptRuleSetResponse"
    ):
        """<p>Reorders the receipt rules within a receipt rule set.</p> <note> <p>All of the rules in the rule set must be represented in this request. That is, it is error if the reorder request doesn't explicitly position all of the rules.</p> </note> <p>For information about managing receipt rule sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the receipt rule set to reorder.</p>
            rule_names: <p>The specified receipt rule set's receipt rules, in order.</p>

        Raises:
            capo_ses.errors.rule_does_not_exist_exception.RuleDoesNotExistException: <p>Indicates that the provided receipt rule does not exist.</p>
            capo_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException: <p>Indicates that the provided receipt rule set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ReorderReceiptRuleSet
            The following example reorders the receipt rules within a receipt rule set:

            >>> await client.reorder_receipt_rule_set(rule_set_name='MyRuleSet', rule_names=['MyRule', 'MyOtherRule'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.reorder_receipt_rule_set_request.ReorderReceiptRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.reorder_receipt_rule_set_response.ReorderReceiptRuleSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.reorder_receipt_rule_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.reorder_receipt_rule_set.async_reorder_receipt_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.reorder_receipt_rule_set_request.ReorderReceiptRuleSetRequest = {
            "rule_set_name": rule_set_name,
            "rule_names": rule_names,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_bounce(
        self,
        original_message_id: "capo_ses.types.message_id.MessageId",
        bounce_sender: "capo_ses.types.address.Address",
        bounced_recipient_info_list: "capo_ses.types.bounced_recipient_info_list.BouncedRecipientInfoList",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        explanation: Optional["capo_ses.types.explanation.Explanation"] = None,
        message_dsn: Optional["capo_ses.types.message_dsn.MessageDsn"] = None,
        bounce_sender_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
    ) -> "capo_ses.types.send_bounce_response.SendBounceResponse":
        """<p>Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this operation on an email up to 24 hours after you receive it.</p> <note> <p>You cannot use this operation to send generic bounces for mail that was not received by Amazon SES.</p> </note> <p>For information about receiving email through Amazon SES, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            original_message_id: <p>The message ID of the message to be bounced.</p>
            bounce_sender: <p>The address to use in the "From" header of the bounce message. This must be an identity that you have verified with Amazon SES.</p>
            explanation: <p>Human-readable text for the bounce message to explain the failure. If not specified, the text is auto-generated based on the bounced recipient information.</p>
            message_dsn: <p>Message-related DSN fields. If not specified, Amazon SES chooses the values.</p>
            bounced_recipient_info_list: <p>A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one <code>BouncedRecipientInfo</code> in the list.</p>
            bounce_sender_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the "From" header of the bounce. For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>

        Raises:
            capo_ses.errors.message_rejected.MessageRejected: <p>Indicates that the action failed, and the message could not be sent. Check the error stack for more information about what caused the error.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.send_bounce_request.SendBounceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.send_bounce_response.SendBounceResponse"
        ]:
            import capo_ses._operations.simple_email_service.send_bounce

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.send_bounce.async_send_bounce(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.send_bounce_request.SendBounceRequest = {
            "original_message_id": original_message_id,
            "bounce_sender": bounce_sender,
            "bounced_recipient_info_list": bounced_recipient_info_list,
        }
        if explanation is not None:
            input_["explanation"] = explanation
        if message_dsn is not None:
            input_["message_dsn"] = message_dsn
        if bounce_sender_arn is not None:
            input_["bounce_sender_arn"] = bounce_sender_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_bulk_templated_email(
        self,
        source: "capo_ses.types.address.Address",
        template: "capo_ses.types.template_name.TemplateName",
        default_template_data: "capo_ses.types.template_data.TemplateData",
        destinations: "capo_ses.types.bulk_email_destination_list.BulkEmailDestinationList",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        source_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        reply_to_addresses: Optional["capo_ses.types.address_list.AddressList"] = None,
        return_path: Optional["capo_ses.types.address.Address"] = None,
        return_path_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        configuration_set_name: Optional[
            "capo_ses.types.configuration_set_name.ConfigurationSetName"
        ] = None,
        default_tags: Optional["capo_ses.types.message_tag_list.MessageTagList"] = None,
        template_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
    ) -> "capo_ses.types.send_bulk_templated_email_response.SendBulkTemplatedEmailResponse":
        """<p>Composes an email message to multiple destinations. The message body is created using an email template.</p> <p>To send email using this operation, your call must meet the following requirements:</p> <ul> <li> <p>The call must refer to an existing email template. You can create email templates using <a>CreateTemplate</a>.</p> </li> <li> <p>The message must be sent from a verified email address or domain.</p> </li> <li> <p>If your account is still in the Amazon SES sandbox, you may send only to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html">Verifying Email Addresses and Domains</a> in the <i>Amazon SES Developer Guide.</i> </p> </li> <li> <p>The maximum message size is 10 MB.</p> </li> <li> <p>Each <code>Destination</code> parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format <i>UserName@[SubDomain.]Domain.TopLevelDomain</i>), the entire message is rejected, even if the message contains other recipients that are valid.</p> </li> <li> <p>The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the <code>SendBulkTemplatedEmail</code> operation several times to send the message to each group.</p> </li> <li> <p>The number of destinations you can contact in a single call can be limited by your account's maximum sending rate.</p> </li> </ul>

        Args:
            source: <p>The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html">Amazon SES Developer Guide</a>.</p> <p>If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the <code>SourceArn</code> parameter. For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <note> <p>Amazon SES does not support the SMTPUTF8 extension, as described in <a href="https://tools.ietf.org/html/rfc6531">RFC6531</a>. For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html">Sending raw email using the Amazon SES API</a>. For more information about Punycode, see <a href="http://tools.ietf.org/html/rfc3492">RFC 3492</a>.</p> </note>
            source_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the <code>Source</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to send from <code>user@example.com</code>, then you would specify the <code>SourceArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>Source</code> to be <code>user@example.com</code>.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>
            reply_to_addresses: <p>The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply.</p>
            return_path: <p>The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the recipient's ISP; this message is forwarded to the email address specified by the <code>ReturnPath</code> parameter. The <code>ReturnPath</code> parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. </p>
            return_path_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>ReturnPath</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to use <code>feedback@example.com</code>, then you would specify the <code>ReturnPathArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>ReturnPath</code> to be <code>feedback@example.com</code>.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>
            configuration_set_name: <p>The name of the configuration set to use when you send an email using <code>SendBulkTemplatedEmail</code>.</p>
            default_tags: <p>A list of tags, in the form of name/value pairs, to apply to an email that you send to a destination using <code>SendBulkTemplatedEmail</code>.</p>
            template: <p>The template to use when sending this email.</p>
            template_arn: <p>The ARN of the template to use when sending this email.</p>
            default_template_data: <p>A list of replacement values to apply to the template when replacement data is not specified in a Destination object. These values act as a default or fallback option when no other data is available.</p> <p>The template data is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.</p>
            destinations: <p>One or more <code>Destination</code> objects. All of the recipients in a <code>Destination</code> receive the same version of the email. You can specify up to 50 <code>Destination</code> objects within a <code>Destinations</code> array.</p>

        Raises:
            capo_ses.errors.account_sending_paused_exception.AccountSendingPausedException: <p>Indicates that email sending is disabled for your entire Amazon SES account.</p> <p>You can enable or disable email sending for your Amazon SES account using <a>UpdateAccountSendingEnabled</a>.</p>
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.configuration_set_sending_paused_exception.ConfigurationSetSendingPausedException: <p>Indicates that email sending is disabled for the configuration set.</p> <p>You can enable or disable email sending for a configuration set using <a>UpdateConfigurationSetSendingEnabled</a>.</p>
            capo_ses.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p> Indicates that the message could not be sent because Amazon SES could not read the MX record required to use the specified MAIL FROM domain. For information about editing the custom MAIL FROM domain settings for an identity, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-edit.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.message_rejected.MessageRejected: <p>Indicates that the action failed, and the message could not be sent. Check the error stack for more information about what caused the error.</p>
            capo_ses.errors.template_does_not_exist_exception.TemplateDoesNotExistException: <p>Indicates that the Template object you specified does not exist in your Amazon SES account.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.send_bulk_templated_email_request.SendBulkTemplatedEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.send_bulk_templated_email_response.SendBulkTemplatedEmailResponse"
        ]:
            import capo_ses._operations.simple_email_service.send_bulk_templated_email

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.send_bulk_templated_email.async_send_bulk_templated_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.send_bulk_templated_email_request.SendBulkTemplatedEmailRequest = {
            "source": source,
            "template": template,
            "default_template_data": default_template_data,
            "destinations": destinations,
        }
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if reply_to_addresses is not None:
            input_["reply_to_addresses"] = reply_to_addresses
        if return_path is not None:
            input_["return_path"] = return_path
        if return_path_arn is not None:
            input_["return_path_arn"] = return_path_arn
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if default_tags is not None:
            input_["default_tags"] = default_tags
        if template_arn is not None:
            input_["template_arn"] = template_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_custom_verification_email(
        self,
        email_address: "capo_ses.types.address.Address",
        template_name: "capo_ses.types.template_name.TemplateName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        configuration_set_name: Optional[
            "capo_ses.types.configuration_set_name.ConfigurationSetName"
        ] = None,
    ) -> "capo_ses.types.send_custom_verification_email_response.SendCustomVerificationEmailResponse":
        """<p>Adds an email address to the list of identities for your Amazon SES account in the current Amazon Web Services Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address.</p> <p>To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using Custom Verification Email Templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            email_address: <p>The email address to verify.</p>
            template_name: <p>The name of the custom verification email template to use when sending the verification email.</p>
            configuration_set_name: <p>Name of a configuration set to use when sending the verification email.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.custom_verification_email_template_does_not_exist_exception.CustomVerificationEmailTemplateDoesNotExistException: <p>Indicates that a custom verification email template with the name you specified does not exist.</p>
            capo_ses.errors.from_email_address_not_verified_exception.FromEmailAddressNotVerifiedException: <p>Indicates that the sender address specified for a custom verification email is not verified, and is therefore not eligible to send the custom verification email. </p>
            capo_ses.errors.message_rejected.MessageRejected: <p>Indicates that the action failed, and the message could not be sent. Check the error stack for more information about what caused the error.</p>
            capo_ses.errors.production_access_not_granted_exception.ProductionAccessNotGrantedException: <p>Indicates that the account has not been granted production access.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.send_custom_verification_email_request.SendCustomVerificationEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.send_custom_verification_email_response.SendCustomVerificationEmailResponse"
        ]:
            import capo_ses._operations.simple_email_service.send_custom_verification_email

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.send_custom_verification_email.async_send_custom_verification_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.send_custom_verification_email_request.SendCustomVerificationEmailRequest = {
            "email_address": email_address,
            "template_name": template_name,
        }
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_email(
        self,
        source: "capo_ses.types.address.Address",
        destination: "capo_ses.types.destination.Destination",
        message: "capo_ses.types.message.Message",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        reply_to_addresses: Optional["capo_ses.types.address_list.AddressList"] = None,
        return_path: Optional["capo_ses.types.address.Address"] = None,
        source_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        return_path_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        tags: Optional["capo_ses.types.message_tag_list.MessageTagList"] = None,
        configuration_set_name: Optional[
            "capo_ses.types.configuration_set_name.ConfigurationSetName"
        ] = None,
    ) -> "capo_ses.types.send_email_response.SendEmailResponse":
        """<p>Composes an email message and immediately queues it for sending. To send email using this operation, your message must meet the following requirements:</p> <ul> <li> <p>The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation results in an "Email address not verified" error. </p> </li> <li> <p>If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html">Verifying Email Addresses and Domains</a> in the <i>Amazon SES Developer Guide.</i> </p> </li> <li> <p>The maximum message size is 10 MB.</p> </li> <li> <p>The message must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format <i>UserName@[SubDomain.]Domain.TopLevelDomain</i>), the entire message is rejected, even if the message contains other recipients that are valid.</p> </li> <li> <p>The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the <code>SendEmail</code> operation several times to send the message to each group.</p> </li> </ul> <important> <p>For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your <i>sending quota</i>). For more information about sending quotas in Amazon SES, see <a href="https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html">Managing Your Amazon SES Sending Limits</a> in the <i>Amazon SES Developer Guide.</i> </p> </important>

        Args:
            source: <p>The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html">Amazon SES Developer Guide</a>.</p> <p>If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the <code>SourceArn</code> parameter. For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <note> <p>Amazon SES does not support the SMTPUTF8 extension, as described in <a href="https://tools.ietf.org/html/rfc6531">RFC6531</a>. For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html">Sending raw email using the Amazon SES API</a>. For more information about Punycode, see <a href="http://tools.ietf.org/html/rfc3492">RFC 3492</a>.</p> </note>
            destination: <p>The destination for this email, composed of To:, CC:, and BCC: fields.</p>
            message: <p>The message to be sent.</p>
            reply_to_addresses: <p>The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply.</p>
            return_path: <p>The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the recipient's ISP; this message is forwarded to the email address specified by the <code>ReturnPath</code> parameter. The <code>ReturnPath</code> parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. </p>
            source_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the <code>Source</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to send from <code>user@example.com</code>, then you would specify the <code>SourceArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>Source</code> to be <code>user@example.com</code>.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>
            return_path_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>ReturnPath</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to use <code>feedback@example.com</code>, then you would specify the <code>ReturnPathArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>ReturnPath</code> to be <code>feedback@example.com</code>.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>
            tags: <p>A list of tags, in the form of name/value pairs, to apply to an email that you send using <code>SendEmail</code>. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.</p>
            configuration_set_name: <p>The name of the configuration set to use when you send an email using <code>SendEmail</code>.</p>

        Raises:
            capo_ses.errors.account_sending_paused_exception.AccountSendingPausedException: <p>Indicates that email sending is disabled for your entire Amazon SES account.</p> <p>You can enable or disable email sending for your Amazon SES account using <a>UpdateAccountSendingEnabled</a>.</p>
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.configuration_set_sending_paused_exception.ConfigurationSetSendingPausedException: <p>Indicates that email sending is disabled for the configuration set.</p> <p>You can enable or disable email sending for a configuration set using <a>UpdateConfigurationSetSendingEnabled</a>.</p>
            capo_ses.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p> Indicates that the message could not be sent because Amazon SES could not read the MX record required to use the specified MAIL FROM domain. For information about editing the custom MAIL FROM domain settings for an identity, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-edit.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.message_rejected.MessageRejected: <p>Indicates that the action failed, and the message could not be sent. Check the error stack for more information about what caused the error.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SendEmail
            The following example sends a formatted email:

            >>> await client.send_email(source='sender@example.com', destination={'ToAddresses': ['recipient1@example.com', 'recipient2@example.com'], 'CcAddresses': ['recipient3@example.com'], 'BccAddresses': []}, message={'Subject': {'Data': 'Test email', 'Charset': 'UTF-8'}, 'Body': {'Text': {'Data': 'This is the message body in text format.', 'Charset': 'UTF-8'}, 'Html': {'Data': 'This message body contains HTML formatting. It can, for example, contain links like this one: <a class="ulink" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide" target="_blank">Amazon SES Developer Guide</a>.', 'Charset': 'UTF-8'}}}, reply_to_addresses=[], return_path='', source_arn='', return_path_arn='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.send_email_request.SendEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.send_email_response.SendEmailResponse"
        ]:
            import capo_ses._operations.simple_email_service.send_email

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.send_email.async_send_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.send_email_request.SendEmailRequest = {
            "source": source,
            "destination": destination,
            "message": message,
        }
        if reply_to_addresses is not None:
            input_["reply_to_addresses"] = reply_to_addresses
        if return_path is not None:
            input_["return_path"] = return_path
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if return_path_arn is not None:
            input_["return_path_arn"] = return_path_arn
        if tags is not None:
            input_["tags"] = tags
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_raw_email(
        self,
        raw_message: "capo_ses.types.raw_message.RawMessage",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        source: Optional["capo_ses.types.address.Address"] = None,
        destinations: Optional["capo_ses.types.address_list.AddressList"] = None,
        from_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        source_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        return_path_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        tags: Optional["capo_ses.types.message_tag_list.MessageTagList"] = None,
        configuration_set_name: Optional[
            "capo_ses.types.configuration_set_name.ConfigurationSetName"
        ] = None,
    ) -> "capo_ses.types.send_raw_email_response.SendRawEmailResponse":
        r"""<p>Composes an email message and immediately queues it for sending.</p> <p>This operation is more flexible than the <code>SendEmail</code> operation. When you use the <code>SendRawEmail</code> operation, you can specify the headers of the message as well as its content. This flexibility is useful, for example, when you need to send a multipart MIME email (such a message that contains both a text and an HTML version). You can also use this operation to send messages that include attachments.</p> <p>The <code>SendRawEmail</code> operation has the following requirements:</p> <ul> <li> <p>You can only send email from <a href="https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html">verified email addresses or domains</a>. If you try to send email from an address that isn't verified, the operation results in an "Email address not verified" error.</p> </li> <li> <p>If your account is still in the <a href="https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html">Amazon SES sandbox</a>, you can only send email to other verified addresses in your account, or to addresses that are associated with the <a href="https://docs.aws.amazon.com/ses/latest/dg/send-an-email-from-console.html">Amazon SES mailbox simulator</a>.</p> </li> <li> <p>The maximum message size, including attachments, is 10 MB.</p> </li> <li> <p>Each message has to include at least one recipient address. A recipient address includes any address on the To:, CC:, or BCC: lines.</p> </li> <li> <p>If you send a single message to more than one recipient address, and one of the recipient addresses isn't in a valid format (that is, it's not in the format <i>UserName@[SubDomain.]Domain.TopLevelDomain</i>), Amazon SES rejects the entire message, even if the other addresses are valid.</p> </li> <li> <p>Each message can include up to 50 recipient addresses across the To:, CC:, or BCC: lines. If you need to send a single message to more than 50 recipients, you have to split the list of recipient addresses into groups of less than 50 recipients, and send separate messages to each group.</p> </li> <li> <p>Amazon SES allows you to specify 8-bit Content-Transfer-Encoding for MIME message parts. However, if Amazon SES has to modify the contents of your message (for example, if you use open and click tracking), 8-bit content isn't preserved. For this reason, we highly recommend that you encode all content that isn't 7-bit ASCII. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html#send-email-mime-encoding">MIME Encoding</a> in the <i>Amazon SES Developer Guide</i>.</p> </li> </ul> <p>Additionally, keep the following considerations in mind when using the <code>SendRawEmail</code> operation:</p> <ul> <li> <p>Although you can customize the message headers when using the <code>SendRawEmail</code> operation, Amazon SES automatically applies its own <code>Message-ID</code> and <code>Date</code> headers; if you passed these headers when creating the message, they are overwritten by the values that Amazon SES provides.</p> </li> <li> <p>If you are using sending authorization to send on behalf of another user, <code>SendRawEmail</code> enables you to specify the cross-account identity for the email's Source, From, and Return-Path parameters in one of two ways: you can pass optional parameters <code>SourceArn</code>, <code>FromArn</code>, and/or <code>ReturnPathArn</code>, or you can include the following X-headers in the header of your raw email:</p> <ul> <li> <p> <code>X-SES-SOURCE-ARN</code> </p> </li> <li> <p> <code>X-SES-FROM-ARN</code> </p> </li> <li> <p> <code>X-SES-RETURN-PATH-ARN</code> </p> </li> </ul> <important> <p>Don't include these X-headers in the DKIM signature. Amazon SES removes these before it sends the email.</p> </important> <p>If you only specify the <code>SourceIdentityArn</code> parameter, Amazon SES sets the From and Return-Path addresses to the same identity that you specified.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Using Sending Authorization with Amazon SES</a> in the <i>Amazon SES Developer Guide.</i> </p> </li> <li> <p>For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your <i>sending quota</i>). For more information about sending quotas in Amazon SES, see <a href="https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html">Managing Your Amazon SES Sending Limits</a> in the <i>Amazon SES Developer Guide.</i> </p> </li> </ul>

        Args:
            source: <p>The identity's email address. If you do not provide a value for this parameter, you must specify a "From" address in the raw text of the message. (You can also specify both.)</p> <note> <p>Amazon SES does not support the SMTPUTF8 extension, as described in<a href="https://tools.ietf.org/html/rfc6531">RFC6531</a>. For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html">Sending raw email using the Amazon SES API</a>. For more information about Punycode, see <a href="http://tools.ietf.org/html/rfc3492">RFC 3492</a>.</p> </note> <p>If you specify the <code>Source</code> parameter and have feedback forwarding enabled, then bounces and complaints are sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.</p>
            destinations: <p>A list of destinations for the message, consisting of To:, CC:, and BCC: addresses.</p>
            raw_message: <p>The raw email message itself. The message has to meet the following criteria:</p> <ul> <li> <p>The message has to contain a header and a body, separated by a blank line.</p> </li> <li> <p>All of the required header fields must be present in the message.</p> </li> <li> <p>Each part of a multipart MIME message must be formatted properly.</p> </li> <li> <p>Attachments must be of a content type that Amazon SES supports. For a list on unsupported content types, see <a href="https://docs.aws.amazon.com/ses/latest/dg/mime-types.html">Unsupported Attachment Types</a> in the <i>Amazon SES Developer Guide</i>.</p> </li> <li> <p>The entire message must be base64-encoded.</p> </li> <li> <p>If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, we highly recommend that you encode that content. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html">Sending Raw Email</a> in the <i>Amazon SES Developer Guide</i>.</p> </li> <li> <p>Per <a href="https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6">RFC 5321</a>, the maximum length of each line of text, including the <CRLF>, must not exceed 1,000 characters.</p> </li> </ul>
            from_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular "From" address in the header of the raw email.</p> <p>Instead of using this parameter, you can use the X-header <code>X-SES-FROM-ARN</code> in the raw message of the email. If you use both the <code>FromArn</code> parameter and the corresponding X-header, Amazon SES uses the value of the <code>FromArn</code> parameter.</p> <note> <p>For information about when to use this parameter, see the description of <code>SendRawEmail</code> in this guide, or see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html">Amazon SES Developer Guide</a>.</p> </note>
            source_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the <code>Source</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to send from <code>user@example.com</code>, then you would specify the <code>SourceArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>Source</code> to be <code>user@example.com</code>.</p> <p>Instead of using this parameter, you can use the X-header <code>X-SES-SOURCE-ARN</code> in the raw message of the email. If you use both the <code>SourceArn</code> parameter and the corresponding X-header, Amazon SES uses the value of the <code>SourceArn</code> parameter.</p> <note> <p>For information about when to use this parameter, see the description of <code>SendRawEmail</code> in this guide, or see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html">Amazon SES Developer Guide</a>.</p> </note>
            return_path_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>ReturnPath</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to use <code>feedback@example.com</code>, then you would specify the <code>ReturnPathArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>ReturnPath</code> to be <code>feedback@example.com</code>.</p> <p>Instead of using this parameter, you can use the X-header <code>X-SES-RETURN-PATH-ARN</code> in the raw message of the email. If you use both the <code>ReturnPathArn</code> parameter and the corresponding X-header, Amazon SES uses the value of the <code>ReturnPathArn</code> parameter.</p> <note> <p>For information about when to use this parameter, see the description of <code>SendRawEmail</code> in this guide, or see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html">Amazon SES Developer Guide</a>.</p> </note>
            tags: <p>A list of tags, in the form of name/value pairs, to apply to an email that you send using <code>SendRawEmail</code>. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.</p>
            configuration_set_name: <p>The name of the configuration set to use when you send an email using <code>SendRawEmail</code>.</p>

        Raises:
            capo_ses.errors.account_sending_paused_exception.AccountSendingPausedException: <p>Indicates that email sending is disabled for your entire Amazon SES account.</p> <p>You can enable or disable email sending for your Amazon SES account using <a>UpdateAccountSendingEnabled</a>.</p>
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.configuration_set_sending_paused_exception.ConfigurationSetSendingPausedException: <p>Indicates that email sending is disabled for the configuration set.</p> <p>You can enable or disable email sending for a configuration set using <a>UpdateConfigurationSetSendingEnabled</a>.</p>
            capo_ses.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p> Indicates that the message could not be sent because Amazon SES could not read the MX record required to use the specified MAIL FROM domain. For information about editing the custom MAIL FROM domain settings for an identity, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-edit.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.message_rejected.MessageRejected: <p>Indicates that the action failed, and the message could not be sent. Check the error stack for more information about what caused the error.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SendRawEmail
            The following example sends an email with an attachment:

            >>> await client.send_raw_email(source='', destinations=[], raw_message={'Data': 'From: sender@example.com\\nTo: recipient@example.com\\nSubject: Test email (contains an attachment)\\nMIME-Version: 1.0\\nContent-type: Multipart/Mixed; boundary="NextPart"\\n\\n--NextPart\\nContent-Type: text/plain\\n\\nThis is the message body.\\n\\n--NextPart\\nContent-Type: text/plain;\\nContent-Disposition: attachment; filename="attachment.txt"\\n\\nThis is the text in the attachment.\\n\\n--NextPart--'}, from_arn='', source_arn='', return_path_arn='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.send_raw_email_request.SendRawEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.send_raw_email_response.SendRawEmailResponse"
        ]:
            import capo_ses._operations.simple_email_service.send_raw_email

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.send_raw_email.async_send_raw_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.send_raw_email_request.SendRawEmailRequest = {
            "raw_message": raw_message
        }
        if source is not None:
            input_["source"] = source
        if destinations is not None:
            input_["destinations"] = destinations
        if from_arn is not None:
            input_["from_arn"] = from_arn
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if return_path_arn is not None:
            input_["return_path_arn"] = return_path_arn
        if tags is not None:
            input_["tags"] = tags
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_templated_email(
        self,
        source: "capo_ses.types.address.Address",
        destination: "capo_ses.types.destination.Destination",
        template: "capo_ses.types.template_name.TemplateName",
        template_data: "capo_ses.types.template_data.TemplateData",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        reply_to_addresses: Optional["capo_ses.types.address_list.AddressList"] = None,
        return_path: Optional["capo_ses.types.address.Address"] = None,
        source_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        return_path_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        tags: Optional["capo_ses.types.message_tag_list.MessageTagList"] = None,
        configuration_set_name: Optional[
            "capo_ses.types.configuration_set_name.ConfigurationSetName"
        ] = None,
        template_arn: Optional[
            "capo_ses.types.amazon_resource_name.AmazonResourceName"
        ] = None,
    ) -> "capo_ses.types.send_templated_email_response.SendTemplatedEmailResponse":
        """<p>Composes an email message using an email template and immediately queues it for sending.</p> <p>To send email using this operation, your call must meet the following requirements:</p> <ul> <li> <p>The call must refer to an existing email template. You can create email templates using the <a>CreateTemplate</a> operation.</p> </li> <li> <p>The message must be sent from a verified email address or domain.</p> </li> <li> <p>If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html">Verifying Email Addresses and Domains</a> in the <i>Amazon SES Developer Guide.</i> </p> </li> <li> <p>The maximum message size is 10 MB.</p> </li> <li> <p>Calls to the <code>SendTemplatedEmail</code> operation may only include one <code>Destination</code> parameter. A destination is a set of recipients that receives the same version of the email. The <code>Destination</code> parameter can include up to 50 recipients, across the To:, CC: and BCC: fields.</p> </li> <li> <p>The <code>Destination</code> parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format <i>UserName@[SubDomain.]Domain.TopLevelDomain</i>), the entire message is rejected, even if the message contains other recipients that are valid.</p> </li> </ul> <important> <p>If your call to the <code>SendTemplatedEmail</code> operation includes all of the required parameters, Amazon SES accepts it and returns a Message ID. However, if Amazon SES can't render the email because the template contains errors, it doesn't send the email. Additionally, because it already accepted the message, Amazon SES doesn't return a message stating that it was unable to send the email.</p> <p>For these reasons, we highly recommend that you set up Amazon SES to send you notifications when Rendering Failure events occur. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-api.html">Sending Personalized Email Using the Amazon SES API</a> in the <i>Amazon Simple Email Service Developer Guide</i>.</p> </important>

        Args:
            source: <p>The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html">Amazon SES Developer Guide</a>.</p> <p>If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the <code>SourceArn</code> parameter. For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <note> <p>Amazon SES does not support the SMTPUTF8 extension, as described in <a href="https://tools.ietf.org/html/rfc6531">RFC6531</a>. for this reason, The email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html">Sending raw email using the Amazon SES API</a>. For more information about Punycode, see <a href="http://tools.ietf.org/html/rfc3492">RFC 3492</a>.</p> </note>
            destination: <p>The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields.</p>
            reply_to_addresses: <p>The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply.</p>
            return_path: <p>The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the recipient's ISP; this message is forwarded to the email address specified by the <code>ReturnPath</code> parameter. The <code>ReturnPath</code> parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. </p>
            source_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the <code>Source</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to send from <code>user@example.com</code>, then you would specify the <code>SourceArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>Source</code> to be <code>user@example.com</code>.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>
            return_path_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>ReturnPath</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to use <code>feedback@example.com</code>, then you would specify the <code>ReturnPathArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>ReturnPath</code> to be <code>feedback@example.com</code>.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>
            tags: <p>A list of tags, in the form of name/value pairs, to apply to an email that you send using <code>SendTemplatedEmail</code>. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.</p>
            configuration_set_name: <p>The name of the configuration set to use when you send an email using <code>SendTemplatedEmail</code>.</p>
            template: <p>The template to use when sending this email.</p>
            template_arn: <p>The ARN of the template to use when sending this email.</p>
            template_data: <p>A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.</p>

        Raises:
            capo_ses.errors.account_sending_paused_exception.AccountSendingPausedException: <p>Indicates that email sending is disabled for your entire Amazon SES account.</p> <p>You can enable or disable email sending for your Amazon SES account using <a>UpdateAccountSendingEnabled</a>.</p>
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.configuration_set_sending_paused_exception.ConfigurationSetSendingPausedException: <p>Indicates that email sending is disabled for the configuration set.</p> <p>You can enable or disable email sending for a configuration set using <a>UpdateConfigurationSetSendingEnabled</a>.</p>
            capo_ses.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p> Indicates that the message could not be sent because Amazon SES could not read the MX record required to use the specified MAIL FROM domain. For information about editing the custom MAIL FROM domain settings for an identity, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-edit.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.message_rejected.MessageRejected: <p>Indicates that the action failed, and the message could not be sent. Check the error stack for more information about what caused the error.</p>
            capo_ses.errors.template_does_not_exist_exception.TemplateDoesNotExistException: <p>Indicates that the Template object you specified does not exist in your Amazon SES account.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.send_templated_email_request.SendTemplatedEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.send_templated_email_response.SendTemplatedEmailResponse"
        ]:
            import capo_ses._operations.simple_email_service.send_templated_email

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.send_templated_email.async_send_templated_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.send_templated_email_request.SendTemplatedEmailRequest = {
            "source": source,
            "destination": destination,
            "template": template,
            "template_data": template_data,
        }
        if reply_to_addresses is not None:
            input_["reply_to_addresses"] = reply_to_addresses
        if return_path is not None:
            input_["return_path"] = return_path
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if return_path_arn is not None:
            input_["return_path_arn"] = return_path_arn
        if tags is not None:
            input_["tags"] = tags
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if template_arn is not None:
            input_["template_arn"] = template_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_active_receipt_rule_set(
        self,
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        rule_set_name: Optional[
            "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
        ] = None,
    ) -> "capo_ses.types.set_active_receipt_rule_set_response.SetActiveReceiptRuleSetResponse":
        """<p>Sets the specified receipt rule set as the active receipt rule set.</p> <note> <p>To disable your email-receiving through Amazon SES completely, you can call this operation with <code>RuleSetName</code> set to null.</p> </note> <p>For information about managing receipt rule sets, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the receipt rule set to make active. Setting this value to null disables all email receiving.</p>

        Raises:
            capo_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException: <p>Indicates that the provided receipt rule set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SetActiveReceiptRuleSet
            The following example sets the active receipt rule set:

            >>> await client.set_active_receipt_rule_set(rule_set_name='RuleSetToActivate')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.set_active_receipt_rule_set_request.SetActiveReceiptRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.set_active_receipt_rule_set_response.SetActiveReceiptRuleSetResponse"
        ]:
            import capo_ses._operations.simple_email_service.set_active_receipt_rule_set

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.set_active_receipt_rule_set.async_set_active_receipt_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.set_active_receipt_rule_set_request.SetActiveReceiptRuleSetRequest = {}
        if rule_set_name is not None:
            input_["rule_set_name"] = rule_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_identity_dkim_enabled(
        self,
        identity: "capo_ses.types.identity.Identity",
        dkim_enabled: "capo_ses.types.enabled.Enabled",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.set_identity_dkim_enabled_response.SetIdentityDkimEnabledResponse":
        """<p>Enables or disables Easy DKIM signing of email sent from an identity. If Easy DKIM signing is enabled for a domain, then Amazon SES uses DKIM to sign all email that it sends from addresses on that domain. If Easy DKIM signing is enabled for an email address, then Amazon SES uses DKIM to sign all email it sends from that address.</p> <note> <p>For email addresses (for example, <code>user@example.com</code>), you can only enable DKIM signing if the corresponding domain (in this case, <code>example.com</code>) has been set up to use Easy DKIM.</p> </note> <p>You can enable DKIM signing for an identity at any time after you start the verification process for the identity, even if the verification process isn't complete. </p> <p>You can execute this operation no more than once per second.</p> <p>For more information about Easy DKIM signing, go to the <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html">Amazon SES Developer Guide</a>.</p>

        Args:
            identity: <p>The identity for which DKIM signing should be enabled or disabled.</p>
            dkim_enabled: <p>Sets whether DKIM signing is enabled for an identity. Set to <code>true</code> to enable DKIM signing for this identity; <code>false</code> to disable it. </p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SetIdentityDkimEnabled
            The following example configures Amazon SES to Easy DKIM-sign the email sent from an identity:

            >>> await client.set_identity_dkim_enabled(identity='user@example.com', dkim_enabled=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.set_identity_dkim_enabled_request.SetIdentityDkimEnabledRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.set_identity_dkim_enabled_response.SetIdentityDkimEnabledResponse"
        ]:
            import capo_ses._operations.simple_email_service.set_identity_dkim_enabled

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.set_identity_dkim_enabled.async_set_identity_dkim_enabled(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.set_identity_dkim_enabled_request.SetIdentityDkimEnabledRequest = {
            "identity": identity,
            "dkim_enabled": dkim_enabled,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_identity_feedback_forwarding_enabled(
        self,
        identity: "capo_ses.types.identity.Identity",
        forwarding_enabled: "capo_ses.types.enabled.Enabled",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.set_identity_feedback_forwarding_enabled_response.SetIdentityFeedbackForwardingEnabledResponse":
        """<p>Given an identity (an email address or a domain), enables or disables whether Amazon SES forwards bounce and complaint notifications as email. Feedback forwarding can only be disabled when Amazon Simple Notification Service (Amazon SNS) topics are specified for both bounces and complaints.</p> <note> <p>Feedback forwarding does not apply to delivery notifications. Delivery notifications are only available through Amazon SNS.</p> </note> <p>You can execute this operation no more than once per second.</p> <p>For more information about using notifications with Amazon SES, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications.html">Amazon SES Developer Guide</a>.</p>

        Args:
            identity: <p>The identity for which to set bounce and complaint notification forwarding. Examples: <code>user@example.com</code>, <code>example.com</code>.</p>
            forwarding_enabled: <p>Sets whether Amazon SES forwards bounce and complaint notifications as email. <code>true</code> specifies that Amazon SES forwards bounce and complaint notifications as email, in addition to any Amazon SNS topic publishing otherwise specified. <code>false</code> specifies that Amazon SES publishes bounce and complaint notifications only through Amazon SNS. This value can only be set to <code>false</code> when Amazon SNS topics are set for both <code>Bounce</code> and <code>Complaint</code> notification types.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SetIdentityFeedbackForwardingEnabled
            The following example configures Amazon SES to forward an identity's bounces and complaints via email:

            >>> await client.set_identity_feedback_forwarding_enabled(identity='user@example.com', forwarding_enabled=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.set_identity_feedback_forwarding_enabled_request.SetIdentityFeedbackForwardingEnabledRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.set_identity_feedback_forwarding_enabled_response.SetIdentityFeedbackForwardingEnabledResponse"
        ]:
            import capo_ses._operations.simple_email_service.set_identity_feedback_forwarding_enabled

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.set_identity_feedback_forwarding_enabled.async_set_identity_feedback_forwarding_enabled(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.set_identity_feedback_forwarding_enabled_request.SetIdentityFeedbackForwardingEnabledRequest = {
            "identity": identity,
            "forwarding_enabled": forwarding_enabled,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_identity_headers_in_notifications_enabled(
        self,
        identity: "capo_ses.types.identity.Identity",
        notification_type: "capo_ses.types.notification_type.NotificationType",
        enabled: "capo_ses.types.enabled.Enabled",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.set_identity_headers_in_notifications_enabled_response.SetIdentityHeadersInNotificationsEnabledResponse":
        """<p>Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type.</p> <p>You can execute this operation no more than once per second.</p> <p>For more information about using notifications with Amazon SES, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications.html">Amazon SES Developer Guide</a>.</p>

        Args:
            identity: <p>The identity for which to enable or disable headers in notifications. Examples: <code>user@example.com</code>, <code>example.com</code>.</p>
            notification_type: <p>The notification type for which to enable or disable headers in notifications. </p>
            enabled: <p>Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of <code>true</code> specifies that Amazon SES includes headers in notifications, and a value of <code>false</code> specifies that Amazon SES does not include headers in notifications.</p> <p>This value can only be set when <code>NotificationType</code> is already set to use a particular Amazon SNS topic.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SetIdentityHeadersInNotificationsEnabled
            The following example configures Amazon SES to include the original email headers in the Amazon SNS bounce notifications for an identity:

            >>> await client.set_identity_headers_in_notifications_enabled(identity='user@example.com', notification_type='Bounce', enabled=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.set_identity_headers_in_notifications_enabled_request.SetIdentityHeadersInNotificationsEnabledRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.set_identity_headers_in_notifications_enabled_response.SetIdentityHeadersInNotificationsEnabledResponse"
        ]:
            import capo_ses._operations.simple_email_service.set_identity_headers_in_notifications_enabled

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.set_identity_headers_in_notifications_enabled.async_set_identity_headers_in_notifications_enabled(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.set_identity_headers_in_notifications_enabled_request.SetIdentityHeadersInNotificationsEnabledRequest = {
            "identity": identity,
            "notification_type": notification_type,
            "enabled": enabled,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_identity_mail_from_domain(
        self,
        identity: "capo_ses.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        mail_from_domain: Optional[
            "capo_ses.types.mail_from_domain_name.MailFromDomainName"
        ] = None,
        behavior_on_mx_failure: Optional[
            "capo_ses.types.behavior_on_mx_failure.BehaviorOnMXFailure"
        ] = None,
    ) -> "capo_ses.types.set_identity_mail_from_domain_response.SetIdentityMailFromDomainResponse":
        """<p>Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).</p> <important> <p>To send emails using the specified MAIL FROM domain, you must add an MX record to your MAIL FROM domain's DNS settings. To ensure that your emails pass Sender Policy Framework (SPF) checks, you must also add or update an SPF record. For more information, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/mail-from.html">Amazon SES Developer Guide</a>.</p> </important> <p>You can execute this operation no more than once per second.</p>

        Args:
            identity: <p>The verified identity.</p>
            mail_from_domain: <p>The custom MAIL FROM domain for the verified identity to use. The MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be used in a "From" address if the MAIL FROM domain is the destination of email feedback forwarding (for more information, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/mail-from.html">Amazon SES Developer Guide</a>), and 3) not be used to receive emails. A value of <code>null</code> disables the custom MAIL FROM setting for the identity.</p>
            behavior_on_mx_failure: <p>The action for Amazon SES to take if it cannot successfully read the required MX record when you send an email. If you choose <code>UseDefaultValue</code>, Amazon SES uses amazonses.com (or a subdomain of that) as the MAIL FROM domain. If you choose <code>RejectMessage</code>, Amazon SES returns a <code>MailFromDomainNotVerified</code> error and not send the email.</p> <p>The action specified in <code>BehaviorOnMXFailure</code> is taken when the custom MAIL FROM domain setup is in the <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code> states.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SetIdentityMailFromDomain
            The following example configures Amazon SES to use a custom MAIL FROM domain for an identity:

            >>> await client.set_identity_mail_from_domain(identity='user@example.com', mail_from_domain='bounces.example.com', behavior_on_mx_failure='UseDefaultValue')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.set_identity_mail_from_domain_request.SetIdentityMailFromDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.set_identity_mail_from_domain_response.SetIdentityMailFromDomainResponse"
        ]:
            import capo_ses._operations.simple_email_service.set_identity_mail_from_domain

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.set_identity_mail_from_domain.async_set_identity_mail_from_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.set_identity_mail_from_domain_request.SetIdentityMailFromDomainRequest = {
            "identity": identity
        }
        if mail_from_domain is not None:
            input_["mail_from_domain"] = mail_from_domain
        if behavior_on_mx_failure is not None:
            input_["behavior_on_mx_failure"] = behavior_on_mx_failure

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_identity_notification_topic(
        self,
        identity: "capo_ses.types.identity.Identity",
        notification_type: "capo_ses.types.notification_type.NotificationType",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        sns_topic: Optional[
            "capo_ses.types.notification_topic.NotificationTopic"
        ] = None,
    ) -> "capo_ses.types.set_identity_notification_topic_response.SetIdentityNotificationTopicResponse":
        """<p>Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications. When you use this operation, you specify a verified identity, such as an email address or domain. When you send an email that uses the chosen identity in the Source field, Amazon SES sends notifications to the topic you specified. You can send bounce, complaint, or delivery notifications (or any combination of the three) to the Amazon SNS topic that you specify.</p> <p>You can execute this operation no more than once per second.</p> <p>For more information about feedback notification, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications.html">Amazon SES Developer Guide</a>.</p>

        Args:
            identity: <p>The identity (email address or domain) for the Amazon SNS topic.</p> <important> <p>You can only specify a verified identity for this parameter.</p> </important> <p>You can specify an identity by using its name or by using its Amazon Resource Name (ARN). The following examples are all valid identities: <code>sender@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p>
            notification_type: <p>The type of notifications that are published to the specified Amazon SNS topic.</p>
            sns_topic: <p>The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is omitted from the request or a null value is passed, <code>SnsTopic</code> is cleared and publishing is disabled.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SetIdentityNotificationTopic
            The following example sets the Amazon SNS topic to which Amazon SES will publish bounce, complaint, and/or delivery notifications for emails sent with the specified identity as the Source:

            >>> await client.set_identity_notification_topic(identity='user@example.com', notification_type='Bounce', sns_topic='arn:aws:sns:us-west-2:111122223333:MyTopic')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.set_identity_notification_topic_request.SetIdentityNotificationTopicRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.set_identity_notification_topic_response.SetIdentityNotificationTopicResponse"
        ]:
            import capo_ses._operations.simple_email_service.set_identity_notification_topic

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.set_identity_notification_topic.async_set_identity_notification_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.set_identity_notification_topic_request.SetIdentityNotificationTopicRequest = {
            "identity": identity,
            "notification_type": notification_type,
        }
        if sns_topic is not None:
            input_["sns_topic"] = sns_topic

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_receipt_rule_position(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        rule_name: "capo_ses.types.receipt_rule_name.ReceiptRuleName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        after: Optional["capo_ses.types.receipt_rule_name.ReceiptRuleName"] = None,
    ) -> "capo_ses.types.set_receipt_rule_position_response.SetReceiptRulePositionResponse":
        """<p>Sets the position of the specified receipt rule in the receipt rule set.</p> <p>For information about managing receipt rules, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the receipt rule set that contains the receipt rule to reposition.</p>
            rule_name: <p>The name of the receipt rule to reposition.</p>
            after: <p>The name of the receipt rule after which to place the specified receipt rule.</p>

        Raises:
            capo_ses.errors.rule_does_not_exist_exception.RuleDoesNotExistException: <p>Indicates that the provided receipt rule does not exist.</p>
            capo_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException: <p>Indicates that the provided receipt rule set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SetReceiptRulePosition
            The following example sets the position of a receipt rule in a receipt rule set:

            >>> await client.set_receipt_rule_position(rule_set_name='MyRuleSet', rule_name='RuleToReposition', after='PutRuleAfterThisRule')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.set_receipt_rule_position_request.SetReceiptRulePositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.set_receipt_rule_position_response.SetReceiptRulePositionResponse"
        ]:
            import capo_ses._operations.simple_email_service.set_receipt_rule_position

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.set_receipt_rule_position.async_set_receipt_rule_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.set_receipt_rule_position_request.SetReceiptRulePositionRequest = {
            "rule_set_name": rule_set_name,
            "rule_name": rule_name,
        }
        if after is not None:
            input_["after"] = after

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_render_template(
        self,
        template_name: "capo_ses.types.template_name.TemplateName",
        template_data: "capo_ses.types.template_data.TemplateData",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.test_render_template_response.TestRenderTemplateResponse":
        """<p>Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the template to render.</p>
            template_data: <p>A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.</p>

        Raises:
            capo_ses.errors.invalid_rendering_parameter_exception.InvalidRenderingParameterException: <p>Indicates that one or more of the replacement values you provided is invalid. This error may occur when the TemplateData object contains invalid JSON.</p>
            capo_ses.errors.missing_rendering_attribute_exception.MissingRenderingAttributeException: <p>Indicates that one or more of the replacement values for the specified template was not specified. Ensure that the TemplateData object contains references to all of the replacement tags in the specified template.</p>
            capo_ses.errors.template_does_not_exist_exception.TemplateDoesNotExistException: <p>Indicates that the Template object you specified does not exist in your Amazon SES account.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.test_render_template_request.TestRenderTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.test_render_template_response.TestRenderTemplateResponse"
        ]:
            import capo_ses._operations.simple_email_service.test_render_template

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.test_render_template.async_test_render_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.test_render_template_request.TestRenderTemplateRequest = {
            "template_name": template_name,
            "template_data": template_data,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_account_sending_enabled(
        self,
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        enabled: Optional["capo_ses.types.enabled.Enabled"] = None,
    ) -> None:
        """<p>Enables or disables email sending across your entire Amazon SES account in the current Amazon Web Services Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending across your Amazon SES account in a given Amazon Web Services Region when reputation metrics (such as your bounce or complaint rates) reach certain thresholds.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            enabled: <p>Describes whether email sending is enabled or disabled for your Amazon SES account in the current Amazon Web Services Region.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateAccountSendingEnabled
            The following example updated the sending status for this account.

            >>> await client.update_account_sending_enabled(enabled=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.update_account_sending_enabled_request.UpdateAccountSendingEnabledRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ses._operations.simple_email_service.update_account_sending_enabled

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.update_account_sending_enabled.async_update_account_sending_enabled(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.update_account_sending_enabled_request.UpdateAccountSendingEnabledRequest = {}
        if enabled is not None:
            input_["enabled"] = enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        event_destination: "capo_ses.types.event_destination.EventDestination",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.update_configuration_set_event_destination_response.UpdateConfigurationSetEventDestinationResponse":
        """<p>Updates the event destination of a configuration set. Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html">Monitoring Your Amazon SES Sending Activity</a> in the <i>Amazon SES Developer Guide.</i> </p> <note> <p>When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).</p> </note> <p>You can execute this operation no more than once per second.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that contains the event destination.</p>
            event_destination: <p>The event destination object.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.event_destination_does_not_exist_exception.EventDestinationDoesNotExistException: <p>Indicates that the event destination does not exist.</p>
            capo_ses.errors.invalid_cloud_watch_destination_exception.InvalidCloudWatchDestinationException: <p>Indicates that the Amazon CloudWatch destination is invalid. See the error message for details.</p>
            capo_ses.errors.invalid_firehose_destination_exception.InvalidFirehoseDestinationException: <p>Indicates that the Amazon Kinesis Firehose destination is invalid. See the error message for details.</p>
            capo_ses.errors.invalid_sns_destination_exception.InvalidSNSDestinationException: <p>Indicates that the Amazon Simple Notification Service (Amazon SNS) destination is invalid. See the error message for details.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.update_configuration_set_event_destination_request.UpdateConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.update_configuration_set_event_destination_response.UpdateConfigurationSetEventDestinationResponse"
        ]:
            import capo_ses._operations.simple_email_service.update_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.update_configuration_set_event_destination.async_update_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.update_configuration_set_event_destination_request.UpdateConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination": event_destination,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_set_reputation_metrics_enabled(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        enabled: "capo_ses.types.enabled.Enabled",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> None:
        """<p>Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set in a given Amazon Web Services Region. Reputation metrics include bounce and complaint rates. These metrics are published to Amazon CloudWatch. By using CloudWatch, you can create alarms when bounce or complaint rates exceed certain thresholds.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set to update.</p>
            enabled: <p>Describes whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateConfigurationSetReputationMetricsEnabled
            Set the reputationMetricsEnabled flag for a specific configuration set.

            >>> await client.update_configuration_set_reputation_metrics_enabled(configuration_set_name='foo', enabled=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.update_configuration_set_reputation_metrics_enabled_request.UpdateConfigurationSetReputationMetricsEnabledRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ses._operations.simple_email_service.update_configuration_set_reputation_metrics_enabled

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.update_configuration_set_reputation_metrics_enabled.async_update_configuration_set_reputation_metrics_enabled(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.update_configuration_set_reputation_metrics_enabled_request.UpdateConfigurationSetReputationMetricsEnabledRequest = {
            "configuration_set_name": configuration_set_name,
            "enabled": enabled,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_set_sending_enabled(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        enabled: "capo_ses.types.enabled.Enabled",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> None:
        """<p>Enables or disables email sending for messages sent using a specific configuration set in a given Amazon Web Services Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending for a configuration set when the reputation metrics for that configuration set (such as your bounce on complaint rate) exceed certain thresholds.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set to update.</p>
            enabled: <p>Describes whether email sending is enabled or disabled for the configuration set. </p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateConfigurationSetReputationMetricsEnabled
            Set the sending enabled flag for a specific configuration set.

            >>> await client.update_configuration_set_sending_enabled(configuration_set_name='foo', enabled=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.update_configuration_set_sending_enabled_request.UpdateConfigurationSetSendingEnabledRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ses._operations.simple_email_service.update_configuration_set_sending_enabled

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.update_configuration_set_sending_enabled.async_update_configuration_set_sending_enabled(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.update_configuration_set_sending_enabled_request.UpdateConfigurationSetSendingEnabledRequest = {
            "configuration_set_name": configuration_set_name,
            "enabled": enabled,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_set_tracking_options(
        self,
        configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName",
        tracking_options: "capo_ses.types.tracking_options.TrackingOptions",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.update_configuration_set_tracking_options_response.UpdateConfigurationSetTrackingOptionsResponse":
        """<p>Modifies an association between a configuration set and a custom domain for open and click event tracking. </p> <p>By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html">Amazon SES Developer Guide</a>.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set.</p>

        Raises:
            capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException: <p>Indicates that the configuration set does not exist.</p>
            capo_ses.errors.invalid_tracking_options_exception.InvalidTrackingOptionsException: <p>Indicates that the custom domain to be used for open and click tracking redirects is invalid. This error appears most often in the following situations:</p> <ul> <li> <p>When the tracking domain you specified is not verified in Amazon SES.</p> </li> <li> <p>When the tracking domain you specified is not a valid domain or subdomain.</p> </li> </ul>
            capo_ses.errors.tracking_options_does_not_exist_exception.TrackingOptionsDoesNotExistException: <p>Indicates that the TrackingOptions object you specified does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.update_configuration_set_tracking_options_request.UpdateConfigurationSetTrackingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.update_configuration_set_tracking_options_response.UpdateConfigurationSetTrackingOptionsResponse"
        ]:
            import capo_ses._operations.simple_email_service.update_configuration_set_tracking_options

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.update_configuration_set_tracking_options.async_update_configuration_set_tracking_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.update_configuration_set_tracking_options_request.UpdateConfigurationSetTrackingOptionsRequest = {
            "configuration_set_name": configuration_set_name,
            "tracking_options": tracking_options,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_custom_verification_email_template(
        self,
        template_name: "capo_ses.types.template_name.TemplateName",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
        from_email_address: Optional["capo_ses.types.from_address.FromAddress"] = None,
        template_subject: Optional["capo_ses.types.subject.Subject"] = None,
        template_content: Optional[
            "capo_ses.types.template_content.TemplateContent"
        ] = None,
        success_redirection_url: Optional[
            "capo_ses.types.success_redirection_url.SuccessRedirectionURL"
        ] = None,
        failure_redirection_url: Optional[
            "capo_ses.types.failure_redirection_url.FailureRedirectionURL"
        ] = None,
    ) -> None:
        """<p>Updates an existing custom verification email template.</p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using Custom Verification Email Templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the custom verification email template to update.</p>
            from_email_address: <p>The email address that the custom verification email is sent from.</p>
            template_subject: <p>The subject line of the custom verification email.</p>
            template_content: <p>The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Custom Verification Email Frequently Asked Questions</a> in the <i>Amazon SES Developer Guide</i>.</p>
            success_redirection_url: <p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>
            failure_redirection_url: <p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>

        Raises:
            capo_ses.errors.custom_verification_email_invalid_content_exception.CustomVerificationEmailInvalidContentException: <p>Indicates that custom verification email template provided content is invalid.</p>
            capo_ses.errors.custom_verification_email_template_does_not_exist_exception.CustomVerificationEmailTemplateDoesNotExistException: <p>Indicates that a custom verification email template with the name you specified does not exist.</p>
            capo_ses.errors.from_email_address_not_verified_exception.FromEmailAddressNotVerifiedException: <p>Indicates that the sender address specified for a custom verification email is not verified, and is therefore not eligible to send the custom verification email. </p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.update_custom_verification_email_template_request.UpdateCustomVerificationEmailTemplateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ses._operations.simple_email_service.update_custom_verification_email_template

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.update_custom_verification_email_template.async_update_custom_verification_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.update_custom_verification_email_template_request.UpdateCustomVerificationEmailTemplateRequest = {
            "template_name": template_name
        }
        if from_email_address is not None:
            input_["from_email_address"] = from_email_address
        if template_subject is not None:
            input_["template_subject"] = template_subject
        if template_content is not None:
            input_["template_content"] = template_content
        if success_redirection_url is not None:
            input_["success_redirection_url"] = success_redirection_url
        if failure_redirection_url is not None:
            input_["failure_redirection_url"] = failure_redirection_url

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_receipt_rule(
        self,
        rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName",
        rule: "capo_ses.types.receipt_rule.ReceiptRule",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.update_receipt_rule_response.UpdateReceiptRuleResponse":
        """<p>Updates a receipt rule.</p> <p>For information about managing receipt rules, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            rule_set_name: <p>The name of the receipt rule set that the receipt rule belongs to.</p>
            rule: <p>A data structure that contains the updated receipt rule information.</p>

        Raises:
            capo_ses.errors.invalid_lambda_function_exception.InvalidLambdaFunctionException: <p>Indicates that the provided Amazon Web Services Lambda function is invalid, or that Amazon SES could not execute the provided function, possibly due to permissions issues. For information about giving permissions, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.invalid_s3_configuration_exception.InvalidS3ConfigurationException: <p>Indicates that the provided Amazon S3 bucket or Amazon Web Services KMS encryption key is invalid, or that Amazon SES could not publish to the bucket, possibly due to permissions issues. For information about giving permissions, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.invalid_sns_topic_exception.InvalidSnsTopicException: <p>Indicates that the provided Amazon SNS topic is invalid, or that Amazon SES could not publish to the topic, possibly due to permissions issues. For information about giving permissions, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.limit_exceeded_exception.LimitExceededException: <p>Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html">Amazon SES Developer Guide</a>.</p>
            capo_ses.errors.rule_does_not_exist_exception.RuleDoesNotExistException: <p>Indicates that the provided receipt rule does not exist.</p>
            capo_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException: <p>Indicates that the provided receipt rule set does not exist.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateReceiptRule
            The following example updates a receipt rule to use an Amazon S3 action:

            >>> await client.update_receipt_rule(rule_set_name='MyRuleSet', rule={'TlsPolicy': 'Optional', 'Enabled': True, 'Name': 'MyRule', 'Actions': [{'S3Action': {'ObjectKeyPrefix': 'email', 'BucketName': 'MyBucket'}}], 'ScanEnabled': True})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.update_receipt_rule_request.UpdateReceiptRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.update_receipt_rule_response.UpdateReceiptRuleResponse"
        ]:
            import capo_ses._operations.simple_email_service.update_receipt_rule

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.update_receipt_rule.async_update_receipt_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.update_receipt_rule_request.UpdateReceiptRuleRequest = {
            "rule_set_name": rule_set_name,
            "rule": rule,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_template(
        self,
        template: "capo_ses.types.template.Template",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.update_template_response.UpdateTemplateResponse":
        """<p>Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single operation. For more information, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-api.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Raises:
            capo_ses.errors.invalid_template_exception.InvalidTemplateException: <p>Indicates that the template that you specified could not be rendered. This issue may occur when a template refers to a partial that does not exist.</p>
            capo_ses.errors.template_does_not_exist_exception.TemplateDoesNotExistException: <p>Indicates that the Template object you specified does not exist in your Amazon SES account.</p>
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.update_template_request.UpdateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.update_template_response.UpdateTemplateResponse"
        ]:
            import capo_ses._operations.simple_email_service.update_template

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.update_template.async_update_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.update_template_request.UpdateTemplateRequest = {
            "template": template
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_domain_dkim(
        self,
        domain: "capo_ses.types.domain.Domain",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.verify_domain_dkim_response.VerifyDomainDkimResponse":
        """<p>Returns a set of DKIM tokens for a domain identity.</p> <important> <p>When you execute the <code>VerifyDomainDkim</code> operation, the domain that you specify is added to the list of identities that are associated with your account. This is true even if you haven't already associated the domain with your account by using the <code>VerifyDomainIdentity</code> operation. However, you can't send email from the domain until you either successfully <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#verify-domain-procedure">verify it</a> or you successfully <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html">set up DKIM for it</a>.</p> </important> <p>You use the tokens that are generated by this operation to create CNAME records. When Amazon SES detects that you've added these records to the DNS configuration for a domain, you can start sending email from that domain. You can start sending email even if you haven't added the TXT record provided by the VerifyDomainIdentity operation to the DNS configuration for your domain. All email that you send from the domain is authenticated using DKIM.</p> <p>To create the CNAME records for DKIM authentication, use the following values:</p> <ul> <li> <p> <b>Name</b>: <i>token</i>._domainkey.<i>example.com</i> </p> </li> <li> <p> <b>Type</b>: CNAME</p> </li> <li> <p> <b>Value</b>: <i>token</i>.dkim.amazonses.com</p> </li> </ul> <p>In the preceding example, replace <i>token</i> with one of the tokens that are generated when you execute this operation. Replace <i>example.com</i> with your domain. Repeat this process for each token that's generated by this operation.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            domain: <p>The name of the domain to be verified for Easy DKIM signing.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            VerifyDomainDkim
            The following example generates DKIM tokens for a domain that has been verified with Amazon SES:

            >>> await client.verify_domain_dkim(domain='example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.verify_domain_dkim_request.VerifyDomainDkimRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.verify_domain_dkim_response.VerifyDomainDkimResponse"
        ]:
            import capo_ses._operations.simple_email_service.verify_domain_dkim

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.verify_domain_dkim.async_verify_domain_dkim(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.verify_domain_dkim_request.VerifyDomainDkimRequest = {
            "domain": domain
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_domain_identity(
        self,
        domain: "capo_ses.types.domain.Domain",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.verify_domain_identity_response.VerifyDomainIdentityResponse":
        """<p>Adds a domain to the list of identities for your Amazon SES account in the current Amazon Web Services Region and attempts to verify it. For more information about verifying domains, see <a href="https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html">Verifying Email Addresses and Domains</a> in the <i>Amazon SES Developer Guide.</i> </p> <p>You can execute this operation no more than once per second.</p>

        Args:
            domain: <p>The domain to be verified.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            VerifyDomainIdentity
            The following example starts the domain verification process with Amazon SES:

            >>> await client.verify_domain_identity(domain='example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.verify_domain_identity_request.VerifyDomainIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.verify_domain_identity_response.VerifyDomainIdentityResponse"
        ]:
            import capo_ses._operations.simple_email_service.verify_domain_identity

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.verify_domain_identity.async_verify_domain_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.verify_domain_identity_request.VerifyDomainIdentityRequest = {
            "domain": domain
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_email_address(
        self,
        email_address: "capo_ses.types.address.Address",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> None:
        """<p>Deprecated. Use the <code>VerifyEmailIdentity</code> operation to verify a new email address.</p>

        Args:
            email_address: <p>The email address to be verified.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            VerifyEmailAddress
            The following example starts the email address verification process with Amazon SES:

            >>> await client.verify_email_address(email_address='user@example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.verify_email_address_request.VerifyEmailAddressRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ses._operations.simple_email_service.verify_email_address

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.verify_email_address.async_verify_email_address(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.verify_email_address_request.VerifyEmailAddressRequest = {
            "email_address": email_address
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_email_identity(
        self,
        email_address: "capo_ses.types.address.Address",
        *,
        config_overrides: Optional[AsyncSESClientConfig] = None,
    ) -> "capo_ses.types.verify_email_identity_response.VerifyEmailIdentityResponse":
        """<p>Adds an email address to the list of identities for your Amazon SES account in the current Amazon Web Services Region and attempts to verify it. As a result of executing this operation, a verification email is sent to the specified address.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            email_address: <p>The email address to be verified.</p>

        Raises:
            capo_ses.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            VerifyEmailIdentity
            The following example starts the email address verification process with Amazon SES:

            >>> await client.verify_email_identity(email_address='user@example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ses.types.verify_email_identity_request.VerifyEmailIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_ses.types.verify_email_identity_response.VerifyEmailIdentityResponse"
        ]:
            import capo_ses._operations.simple_email_service.verify_email_identity

            (
                output,
                http_response,
            ) = await capo_ses._operations.simple_email_service.verify_email_identity.async_verify_email_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ses.types.verify_email_identity_request.VerifyEmailIdentityRequest = {
            "email_address": email_address
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
