"""Generated from Smithy shape ``com.amazonaws.pinpointemail#AmazonPinpointEmailService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_pinpoint_email._auth._signers
import capo_pinpoint_email._auth._sigv4
from capo_pinpoint_email._auth._identity import Credentials
from capo_pinpoint_email._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pinpoint_email._auth._zapros_handler import AuthMiddleware
from capo_pinpoint_email._pagination import resolve_path as _resolve_path
from capo_pinpoint_email._services._aws_config import aaws_config
from capo_pinpoint_email._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_pinpoint_email.types.amazon_resource_name
    import capo_pinpoint_email.types.behavior_on_mx_failure
    import capo_pinpoint_email.types.blacklist_item_names
    import capo_pinpoint_email.types.campaign_id
    import capo_pinpoint_email.types.configuration_set_name
    import capo_pinpoint_email.types.create_configuration_set_event_destination_request
    import capo_pinpoint_email.types.create_configuration_set_event_destination_response
    import capo_pinpoint_email.types.create_configuration_set_request
    import capo_pinpoint_email.types.create_configuration_set_response
    import capo_pinpoint_email.types.create_dedicated_ip_pool_request
    import capo_pinpoint_email.types.create_dedicated_ip_pool_response
    import capo_pinpoint_email.types.create_deliverability_test_report_request
    import capo_pinpoint_email.types.create_deliverability_test_report_response
    import capo_pinpoint_email.types.create_email_identity_request
    import capo_pinpoint_email.types.create_email_identity_response
    import capo_pinpoint_email.types.custom_redirect_domain
    import capo_pinpoint_email.types.delete_configuration_set_event_destination_request
    import capo_pinpoint_email.types.delete_configuration_set_event_destination_response
    import capo_pinpoint_email.types.delete_configuration_set_request
    import capo_pinpoint_email.types.delete_configuration_set_response
    import capo_pinpoint_email.types.delete_dedicated_ip_pool_request
    import capo_pinpoint_email.types.delete_dedicated_ip_pool_response
    import capo_pinpoint_email.types.delete_email_identity_request
    import capo_pinpoint_email.types.delete_email_identity_response
    import capo_pinpoint_email.types.delivery_options
    import capo_pinpoint_email.types.destination
    import capo_pinpoint_email.types.domain
    import capo_pinpoint_email.types.domain_deliverability_tracking_options
    import capo_pinpoint_email.types.email_address
    import capo_pinpoint_email.types.email_address_list
    import capo_pinpoint_email.types.email_content
    import capo_pinpoint_email.types.enabled
    import capo_pinpoint_email.types.event_destination_definition
    import capo_pinpoint_email.types.event_destination_name
    import capo_pinpoint_email.types.get_account_request
    import capo_pinpoint_email.types.get_account_response
    import capo_pinpoint_email.types.get_blacklist_reports_request
    import capo_pinpoint_email.types.get_blacklist_reports_response
    import capo_pinpoint_email.types.get_configuration_set_event_destinations_request
    import capo_pinpoint_email.types.get_configuration_set_event_destinations_response
    import capo_pinpoint_email.types.get_configuration_set_request
    import capo_pinpoint_email.types.get_configuration_set_response
    import capo_pinpoint_email.types.get_dedicated_ip_request
    import capo_pinpoint_email.types.get_dedicated_ip_response
    import capo_pinpoint_email.types.get_dedicated_ips_request
    import capo_pinpoint_email.types.get_dedicated_ips_response
    import capo_pinpoint_email.types.get_deliverability_dashboard_options_request
    import capo_pinpoint_email.types.get_deliverability_dashboard_options_response
    import capo_pinpoint_email.types.get_deliverability_test_report_request
    import capo_pinpoint_email.types.get_deliverability_test_report_response
    import capo_pinpoint_email.types.get_domain_deliverability_campaign_request
    import capo_pinpoint_email.types.get_domain_deliverability_campaign_response
    import capo_pinpoint_email.types.get_domain_statistics_report_request
    import capo_pinpoint_email.types.get_domain_statistics_report_response
    import capo_pinpoint_email.types.get_email_identity_request
    import capo_pinpoint_email.types.get_email_identity_response
    import capo_pinpoint_email.types.identity
    import capo_pinpoint_email.types.ip
    import capo_pinpoint_email.types.list_configuration_sets_request
    import capo_pinpoint_email.types.list_configuration_sets_response
    import capo_pinpoint_email.types.list_dedicated_ip_pools_request
    import capo_pinpoint_email.types.list_dedicated_ip_pools_response
    import capo_pinpoint_email.types.list_deliverability_test_reports_request
    import capo_pinpoint_email.types.list_deliverability_test_reports_response
    import capo_pinpoint_email.types.list_domain_deliverability_campaigns_request
    import capo_pinpoint_email.types.list_domain_deliverability_campaigns_response
    import capo_pinpoint_email.types.list_email_identities_request
    import capo_pinpoint_email.types.list_email_identities_response
    import capo_pinpoint_email.types.list_tags_for_resource_request
    import capo_pinpoint_email.types.list_tags_for_resource_response
    import capo_pinpoint_email.types.mail_from_domain_name
    import capo_pinpoint_email.types.max_items
    import capo_pinpoint_email.types.message_tag_list
    import capo_pinpoint_email.types.next_token
    import capo_pinpoint_email.types.percentage100_wrapper
    import capo_pinpoint_email.types.pool_name
    import capo_pinpoint_email.types.put_account_dedicated_ip_warmup_attributes_request
    import capo_pinpoint_email.types.put_account_dedicated_ip_warmup_attributes_response
    import capo_pinpoint_email.types.put_account_sending_attributes_request
    import capo_pinpoint_email.types.put_account_sending_attributes_response
    import capo_pinpoint_email.types.put_configuration_set_delivery_options_request
    import capo_pinpoint_email.types.put_configuration_set_delivery_options_response
    import capo_pinpoint_email.types.put_configuration_set_reputation_options_request
    import capo_pinpoint_email.types.put_configuration_set_reputation_options_response
    import capo_pinpoint_email.types.put_configuration_set_sending_options_request
    import capo_pinpoint_email.types.put_configuration_set_sending_options_response
    import capo_pinpoint_email.types.put_configuration_set_tracking_options_request
    import capo_pinpoint_email.types.put_configuration_set_tracking_options_response
    import capo_pinpoint_email.types.put_dedicated_ip_in_pool_request
    import capo_pinpoint_email.types.put_dedicated_ip_in_pool_response
    import capo_pinpoint_email.types.put_dedicated_ip_warmup_attributes_request
    import capo_pinpoint_email.types.put_dedicated_ip_warmup_attributes_response
    import capo_pinpoint_email.types.put_deliverability_dashboard_option_request
    import capo_pinpoint_email.types.put_deliverability_dashboard_option_response
    import capo_pinpoint_email.types.put_email_identity_dkim_attributes_request
    import capo_pinpoint_email.types.put_email_identity_dkim_attributes_response
    import capo_pinpoint_email.types.put_email_identity_feedback_attributes_request
    import capo_pinpoint_email.types.put_email_identity_feedback_attributes_response
    import capo_pinpoint_email.types.put_email_identity_mail_from_attributes_request
    import capo_pinpoint_email.types.put_email_identity_mail_from_attributes_response
    import capo_pinpoint_email.types.report_id
    import capo_pinpoint_email.types.report_name
    import capo_pinpoint_email.types.reputation_options
    import capo_pinpoint_email.types.send_email_request
    import capo_pinpoint_email.types.send_email_response
    import capo_pinpoint_email.types.sending_options
    import capo_pinpoint_email.types.sending_pool_name
    import capo_pinpoint_email.types.tag_key_list
    import capo_pinpoint_email.types.tag_list
    import capo_pinpoint_email.types.tag_resource_request
    import capo_pinpoint_email.types.tag_resource_response
    import capo_pinpoint_email.types.timestamp
    import capo_pinpoint_email.types.tls_policy
    import capo_pinpoint_email.types.tracking_options
    import capo_pinpoint_email.types.untag_resource_request
    import capo_pinpoint_email.types.untag_resource_response
    import capo_pinpoint_email.types.update_configuration_set_event_destination_request
    import capo_pinpoint_email.types.update_configuration_set_event_destination_response


class AsyncPinpointEmailClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncPinpointEmailClient:
    """A client for the ``PinpointEmail`` service.

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
        self._config = AsyncPinpointEmailClientConfig(
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
        self, config_overrides: Optional[AsyncPinpointEmailClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPinpointEmailClientConfig = config_overrides or {}
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

    async def create_configuration_set(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        tracking_options: Optional[
            "capo_pinpoint_email.types.tracking_options.TrackingOptions"
        ] = None,
        delivery_options: Optional[
            "capo_pinpoint_email.types.delivery_options.DeliveryOptions"
        ] = None,
        reputation_options: Optional[
            "capo_pinpoint_email.types.reputation_options.ReputationOptions"
        ] = None,
        sending_options: Optional[
            "capo_pinpoint_email.types.sending_options.SendingOptions"
        ] = None,
        tags: Optional["capo_pinpoint_email.types.tag_list.TagList"] = None,
    ) -> "capo_pinpoint_email.types.create_configuration_set_response.CreateConfigurationSetResponse":
        """<p>Create a configuration set. <i>Configuration sets</i> are groups of rules that you can apply to the emails you send using Amazon Pinpoint. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email. </p>

        Args:
            configuration_set_name: <p>The name of the configuration set.</p>
            tracking_options: <p>An object that defines the open and click tracking options for emails that you send using the configuration set.</p>
            delivery_options: <p>An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.</p>
            reputation_options: <p>An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.</p>
            sending_options: <p>An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.</p>
            tags: <p>An array of objects that define the tags (keys and values) that you want to associate with the configuration set.</p>

        Raises:
            capo_pinpoint_email.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_pinpoint_email.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.create_configuration_set_request.CreateConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.create_configuration_set_response.CreateConfigurationSetResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_configuration_set

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_configuration_set.async_create_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.create_configuration_set_request.CreateConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }
        if tracking_options is not None:
            input_["tracking_options"] = tracking_options
        if delivery_options is not None:
            input_["delivery_options"] = delivery_options
        if reputation_options is not None:
            input_["reputation_options"] = reputation_options
        if sending_options is not None:
            input_["sending_options"] = sending_options
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        event_destination_name: "capo_pinpoint_email.types.event_destination_name.EventDestinationName",
        event_destination: "capo_pinpoint_email.types.event_destination_definition.EventDestinationDefinition",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.create_configuration_set_event_destination_response.CreateConfigurationSetEventDestinationResponse":
        """<p>Create an event destination. In Amazon Pinpoint, <i>events</i> include message sends, deliveries, opens, clicks, bounces, and complaints. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.</p> <p>A single configuration set can include more than one event destination.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that you want to add an event destination to.</p>
            event_destination_name: <p>A name that identifies the event destination within the configuration set.</p>
            event_destination: <p>An object that defines the event destination.</p>

        Raises:
            capo_pinpoint_email.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.create_configuration_set_event_destination_request.CreateConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.create_configuration_set_event_destination_response.CreateConfigurationSetEventDestinationResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_configuration_set_event_destination.async_create_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.create_configuration_set_event_destination_request.CreateConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
            "event_destination": event_destination,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dedicated_ip_pool(
        self,
        pool_name: "capo_pinpoint_email.types.pool_name.PoolName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        tags: Optional["capo_pinpoint_email.types.tag_list.TagList"] = None,
    ) -> "capo_pinpoint_email.types.create_dedicated_ip_pool_response.CreateDedicatedIpPoolResponse":
        """<p>Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your Amazon Pinpoint account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, Amazon Pinpoint sends it using only the IP addresses in the associated pool.</p>

        Args:
            pool_name: <p>The name of the dedicated IP pool.</p>
            tags: <p>An object that defines the tags (keys and values) that you want to associate with the pool.</p>

        Raises:
            capo_pinpoint_email.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_pinpoint_email.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.create_dedicated_ip_pool_request.CreateDedicatedIpPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.create_dedicated_ip_pool_response.CreateDedicatedIpPoolResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_dedicated_ip_pool

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_dedicated_ip_pool.async_create_dedicated_ip_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.create_dedicated_ip_pool_request.CreateDedicatedIpPoolRequest = {
            "pool_name": pool_name
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_deliverability_test_report(
        self,
        from_email_address: "capo_pinpoint_email.types.email_address.EmailAddress",
        content: "capo_pinpoint_email.types.email_content.EmailContent",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        report_name: Optional[
            "capo_pinpoint_email.types.report_name.ReportName"
        ] = None,
        tags: Optional["capo_pinpoint_email.types.tag_list.TagList"] = None,
    ) -> "capo_pinpoint_email.types.create_deliverability_test_report_response.CreateDeliverabilityTestReportResponse":
        """<p>Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon Pinpoint then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the <code>GetDeliverabilityTestReport</code> operation to view the results of the test.</p>

        Args:
            report_name: <p>A unique name that helps you to identify the predictive inbox placement test when you retrieve the results.</p>
            from_email_address: <p>The email address that the predictive inbox placement test email was sent from.</p>
            content: <p>The HTML body of the message that you sent when you performed the predictive inbox placement test.</p>
            tags: <p>An array of objects that define the tags (keys and values) that you want to associate with the predictive inbox placement test.</p>

        Raises:
            capo_pinpoint_email.errors.account_suspended_exception.AccountSuspendedException: <p>The message can't be sent because the account's ability to send email has been permanently restricted.</p>
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_pinpoint_email.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_pinpoint_email.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p>The message can't be sent because the sending domain isn't verified.</p>
            capo_pinpoint_email.errors.message_rejected.MessageRejected: <p>The message can't be sent because it contains invalid content.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.sending_paused_exception.SendingPausedException: <p>The message can't be sent because the account's ability to send email is currently paused.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.create_deliverability_test_report_request.CreateDeliverabilityTestReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.create_deliverability_test_report_response.CreateDeliverabilityTestReportResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_deliverability_test_report

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_deliverability_test_report.async_create_deliverability_test_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.create_deliverability_test_report_request.CreateDeliverabilityTestReportRequest = {
            "from_email_address": from_email_address,
            "content": content,
        }
        if report_name is not None:
            input_["report_name"] = report_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_email_identity(
        self,
        email_identity: "capo_pinpoint_email.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        tags: Optional["capo_pinpoint_email.types.tag_list.TagList"] = None,
    ) -> "capo_pinpoint_email.types.create_email_identity_response.CreateEmailIdentityResponse":
        """<p>Verifies an email identity for use with Amazon Pinpoint. In Amazon Pinpoint, an identity is an email address or domain that you use when you send email. Before you can use an identity to send email with Amazon Pinpoint, you first have to verify it. By verifying an address, you demonstrate that you're the owner of the address, and that you've given Amazon Pinpoint permission to send email from the address.</p> <p>When you verify an email address, Amazon Pinpoint sends an email to the address. Your email address is verified as soon as you follow the link in the verification email. </p> <p>When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon Pinpoint detects these records in the DNS configuration for your domain. It usually takes around 72 hours to complete the domain verification process.</p>

        Args:
            email_identity: <p>The email address or domain that you want to verify.</p>
            tags: <p>An array of objects that define the tags (keys and values) that you want to associate with the email identity.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_pinpoint_email.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.create_email_identity_request.CreateEmailIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.create_email_identity_response.CreateEmailIdentityResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_email_identity

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.create_email_identity.async_create_email_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.create_email_identity_request.CreateEmailIdentityRequest = {
            "email_identity": email_identity
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_set(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.delete_configuration_set_response.DeleteConfigurationSetResponse":
        """<p>Delete an existing configuration set.</p> <p>In Amazon Pinpoint, <i>configuration sets</i> are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that you want to delete.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.delete_configuration_set_request.DeleteConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.delete_configuration_set_response.DeleteConfigurationSetResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.delete_configuration_set

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.delete_configuration_set.async_delete_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.delete_configuration_set_request.DeleteConfigurationSetRequest = {
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
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        event_destination_name: "capo_pinpoint_email.types.event_destination_name.EventDestinationName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.delete_configuration_set_event_destination_response.DeleteConfigurationSetEventDestinationResponse":
        """<p>Delete an event destination.</p> <p>In Amazon Pinpoint, <i>events</i> include message sends, deliveries, opens, clicks, bounces, and complaints. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that contains the event destination that you want to delete.</p>
            event_destination_name: <p>The name of the event destination that you want to delete.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.delete_configuration_set_event_destination_request.DeleteConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.delete_configuration_set_event_destination_response.DeleteConfigurationSetEventDestinationResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.delete_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.delete_configuration_set_event_destination.async_delete_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.delete_configuration_set_event_destination_request.DeleteConfigurationSetEventDestinationRequest = {
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

    async def delete_dedicated_ip_pool(
        self,
        pool_name: "capo_pinpoint_email.types.pool_name.PoolName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.delete_dedicated_ip_pool_response.DeleteDedicatedIpPoolResponse":
        """<p>Delete a dedicated IP pool.</p>

        Args:
            pool_name: <p>The name of the dedicated IP pool that you want to delete.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.delete_dedicated_ip_pool_request.DeleteDedicatedIpPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.delete_dedicated_ip_pool_response.DeleteDedicatedIpPoolResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.delete_dedicated_ip_pool

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.delete_dedicated_ip_pool.async_delete_dedicated_ip_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.delete_dedicated_ip_pool_request.DeleteDedicatedIpPoolRequest = {
            "pool_name": pool_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_email_identity(
        self,
        email_identity: "capo_pinpoint_email.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.delete_email_identity_response.DeleteEmailIdentityResponse":
        """<p>Deletes an email identity that you previously verified for use with Amazon Pinpoint. An identity can be either an email address or a domain name.</p>

        Args:
            email_identity: <p>The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.delete_email_identity_request.DeleteEmailIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.delete_email_identity_response.DeleteEmailIdentityResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.delete_email_identity

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.delete_email_identity.async_delete_email_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.delete_email_identity_request.DeleteEmailIdentityRequest = {
            "email_identity": email_identity
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account(
        self, *, config_overrides: Optional[AsyncPinpointEmailClientConfig] = None
    ) -> "capo_pinpoint_email.types.get_account_response.GetAccountResponse":
        """<p>Obtain information about the email-sending status and capabilities of your Amazon Pinpoint account in the current AWS Region.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_account_request.GetAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_account_response.GetAccountResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_account

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_account.async_get_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_account_request.GetAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_blacklist_reports(
        self,
        blacklist_item_names: "capo_pinpoint_email.types.blacklist_item_names.BlacklistItemNames",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.get_blacklist_reports_response.GetBlacklistReportsResponse":
        """<p>Retrieve a list of the blacklists that your dedicated IP addresses appear on.</p>

        Args:
            blacklist_item_names: <p>A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon Pinpoint or Amazon SES.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_blacklist_reports_request.GetBlacklistReportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_blacklist_reports_response.GetBlacklistReportsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_blacklist_reports

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_blacklist_reports.async_get_blacklist_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_blacklist_reports_request.GetBlacklistReportsRequest = {
            "blacklist_item_names": blacklist_item_names
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration_set(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.get_configuration_set_response.GetConfigurationSetResponse":
        """<p>Get information about an existing configuration set, including the dedicated IP pool that it's associated with, whether or not it's enabled for sending email, and more.</p> <p>In Amazon Pinpoint, <i>configuration sets</i> are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that you want to obtain more information about.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_configuration_set_request.GetConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_configuration_set_response.GetConfigurationSetResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_configuration_set

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_configuration_set.async_get_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_configuration_set_request.GetConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration_set_event_destinations(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.get_configuration_set_event_destinations_response.GetConfigurationSetEventDestinationsResponse":
        """<p>Retrieve a list of event destinations that are associated with a configuration set.</p> <p>In Amazon Pinpoint, <i>events</i> include message sends, deliveries, opens, clicks, bounces, and complaints. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that contains the event destination.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_configuration_set_event_destinations_request.GetConfigurationSetEventDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_configuration_set_event_destinations_response.GetConfigurationSetEventDestinationsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_configuration_set_event_destinations

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_configuration_set_event_destinations.async_get_configuration_set_event_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_configuration_set_event_destinations_request.GetConfigurationSetEventDestinationsRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dedicated_ip(
        self,
        ip: "capo_pinpoint_email.types.ip.Ip",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.get_dedicated_ip_response.GetDedicatedIpResponse":
        """<p>Get information about a dedicated IP address, including the name of the dedicated IP pool that it's associated with, as well information about the automatic warm-up process for the address.</p>

        Args:
            ip: <p>The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that's assocaited with your Amazon Pinpoint account.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_dedicated_ip_request.GetDedicatedIpRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_dedicated_ip_response.GetDedicatedIpResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_dedicated_ip

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_dedicated_ip.async_get_dedicated_ip(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_dedicated_ip_request.GetDedicatedIpRequest = {
            "ip": ip
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dedicated_ips(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        pool_name: Optional["capo_pinpoint_email.types.pool_name.PoolName"] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "capo_pinpoint_email.types.get_dedicated_ips_response.GetDedicatedIpsResponse":
        """<p>List the dedicated IP addresses that are associated with your Amazon Pinpoint account.</p>

        Args:
            pool_name: <p>The name of the IP pool that the dedicated IP address is associated with.</p>
            next_token: <p>A token returned from a previous call to <code>GetDedicatedIps</code> to indicate the position of the dedicated IP pool in the list of IP pools.</p>
            page_size: <p>The number of results to show in a single call to <code>GetDedicatedIpsRequest</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_dedicated_ips_request.GetDedicatedIpsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_dedicated_ips_response.GetDedicatedIpsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_dedicated_ips

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_dedicated_ips.async_get_dedicated_ips(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_dedicated_ips_request.GetDedicatedIpsRequest = {}
        if pool_name is not None:
            input_["pool_name"] = pool_name
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_dedicated_ips(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        pool_name: Optional["capo_pinpoint_email.types.pool_name.PoolName"] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_pinpoint_email.types.get_dedicated_ips_response.GetDedicatedIpsResponse]":
        _token = next_token
        while True:
            _response = await self.get_dedicated_ips(
                config_overrides=config_overrides,
                pool_name=pool_name,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_deliverability_dashboard_options(
        self, *, config_overrides: Optional[AsyncPinpointEmailClientConfig] = None
    ) -> "capo_pinpoint_email.types.get_deliverability_dashboard_options_response.GetDeliverabilityDashboardOptionsResponse":
        """<p>Retrieve information about the status of the Deliverability dashboard for your Amazon Pinpoint account. When the Deliverability dashboard is enabled, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.</p> <p>When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon Pinpoint. For more information about the features and cost of a Deliverability dashboard subscription, see <a href="http://aws.amazon.com/pinpoint/pricing/">Amazon Pinpoint Pricing</a>.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_deliverability_dashboard_options_request.GetDeliverabilityDashboardOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_deliverability_dashboard_options_response.GetDeliverabilityDashboardOptionsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_deliverability_dashboard_options

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_deliverability_dashboard_options.async_get_deliverability_dashboard_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_deliverability_dashboard_options_request.GetDeliverabilityDashboardOptionsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_deliverability_test_report(
        self,
        report_id: "capo_pinpoint_email.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.get_deliverability_test_report_response.GetDeliverabilityTestReportResponse":
        """<p>Retrieve the results of a predictive inbox placement test.</p>

        Args:
            report_id: <p>A unique string that identifies the predictive inbox placement test.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_deliverability_test_report_request.GetDeliverabilityTestReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_deliverability_test_report_response.GetDeliverabilityTestReportResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_deliverability_test_report

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_deliverability_test_report.async_get_deliverability_test_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_deliverability_test_report_request.GetDeliverabilityTestReportRequest = {
            "report_id": report_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain_deliverability_campaign(
        self,
        campaign_id: "capo_pinpoint_email.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.get_domain_deliverability_campaign_response.GetDomainDeliverabilityCampaignResponse":
        """<p>Retrieve all the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for (<code>PutDeliverabilityDashboardOption</code> operation).</p>

        Args:
            campaign_id: <p>The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns this identifier to a campaign. This value is not the same as the campaign identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon Pinpoint API or the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_domain_deliverability_campaign_request.GetDomainDeliverabilityCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_domain_deliverability_campaign_response.GetDomainDeliverabilityCampaignResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_domain_deliverability_campaign

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_domain_deliverability_campaign.async_get_domain_deliverability_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_domain_deliverability_campaign_request.GetDomainDeliverabilityCampaignRequest = {
            "campaign_id": campaign_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain_statistics_report(
        self,
        domain: "capo_pinpoint_email.types.identity.Identity",
        start_date: "capo_pinpoint_email.types.timestamp.Timestamp",
        end_date: "capo_pinpoint_email.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.get_domain_statistics_report_response.GetDomainStatisticsReportResponse":
        """<p>Retrieve inbox placement and engagement rates for the domains that you use to send email.</p>

        Args:
            domain: <p>The domain that you want to obtain deliverability metrics for.</p>
            start_date: <p>The first day (in Unix time) that you want to obtain domain deliverability metrics for.</p>
            end_date: <p>The last day (in Unix time) that you want to obtain domain deliverability metrics for. The <code>EndDate</code> that you specify has to be less than or equal to 30 days after the <code>StartDate</code>.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_domain_statistics_report_request.GetDomainStatisticsReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_domain_statistics_report_response.GetDomainStatisticsReportResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_domain_statistics_report

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_domain_statistics_report.async_get_domain_statistics_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_domain_statistics_report_request.GetDomainStatisticsReportRequest = {
            "domain": domain,
            "start_date": start_date,
            "end_date": end_date,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_email_identity(
        self,
        email_identity: "capo_pinpoint_email.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> (
        "capo_pinpoint_email.types.get_email_identity_response.GetEmailIdentityResponse"
    ):
        """<p>Provides information about a specific identity associated with your Amazon Pinpoint account, including the identity's verification status, its DKIM authentication status, and its custom Mail-From settings.</p>

        Args:
            email_identity: <p>The email identity that you want to retrieve details for.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.get_email_identity_request.GetEmailIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.get_email_identity_response.GetEmailIdentityResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_email_identity

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.get_email_identity.async_get_email_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.get_email_identity_request.GetEmailIdentityRequest = {
            "email_identity": email_identity
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
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "capo_pinpoint_email.types.list_configuration_sets_response.ListConfigurationSetsResponse":
        """<p>List all of the configuration sets associated with your Amazon Pinpoint account in the current region.</p> <p>In Amazon Pinpoint, <i>configuration sets</i> are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListConfigurationSets</code> to indicate the position in the list of configuration sets.</p>
            page_size: <p>The number of results to show in a single call to <code>ListConfigurationSets</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.list_configuration_sets_request.ListConfigurationSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.list_configuration_sets_response.ListConfigurationSetsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_configuration_sets

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_configuration_sets.async_list_configuration_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.list_configuration_sets_request.ListConfigurationSetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_configuration_sets(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_pinpoint_email.types.list_configuration_sets_response.ListConfigurationSetsResponse]":
        _token = next_token
        while True:
            _response = await self.list_configuration_sets(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dedicated_ip_pools(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "capo_pinpoint_email.types.list_dedicated_ip_pools_response.ListDedicatedIpPoolsResponse":
        """<p>List all of the dedicated IP pools that exist in your Amazon Pinpoint account in the current AWS Region.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListDedicatedIpPools</code> to indicate the position in the list of dedicated IP pools.</p>
            page_size: <p>The number of results to show in a single call to <code>ListDedicatedIpPools</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.list_dedicated_ip_pools_request.ListDedicatedIpPoolsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.list_dedicated_ip_pools_response.ListDedicatedIpPoolsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_dedicated_ip_pools

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_dedicated_ip_pools.async_list_dedicated_ip_pools(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.list_dedicated_ip_pools_request.ListDedicatedIpPoolsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_dedicated_ip_pools(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_pinpoint_email.types.list_dedicated_ip_pools_response.ListDedicatedIpPoolsResponse]":
        _token = next_token
        while True:
            _response = await self.list_dedicated_ip_pools(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_deliverability_test_reports(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "capo_pinpoint_email.types.list_deliverability_test_reports_response.ListDeliverabilityTestReportsResponse":
        """<p>Show a list of the predictive inbox placement tests that you've performed, regardless of their statuses. For predictive inbox placement tests that are complete, you can use the <code>GetDeliverabilityTestReport</code> operation to view the results.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListDeliverabilityTestReports</code> to indicate the position in the list of predictive inbox placement tests.</p>
            page_size: <p>The number of results to show in a single call to <code>ListDeliverabilityTestReports</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 0, and can be no more than 1000.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.list_deliverability_test_reports_request.ListDeliverabilityTestReportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.list_deliverability_test_reports_response.ListDeliverabilityTestReportsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_deliverability_test_reports

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_deliverability_test_reports.async_list_deliverability_test_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.list_deliverability_test_reports_request.ListDeliverabilityTestReportsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_deliverability_test_reports(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_pinpoint_email.types.list_deliverability_test_reports_response.ListDeliverabilityTestReportsResponse]":
        _token = next_token
        while True:
            _response = await self.list_deliverability_test_reports(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_domain_deliverability_campaigns(
        self,
        start_date: "capo_pinpoint_email.types.timestamp.Timestamp",
        end_date: "capo_pinpoint_email.types.timestamp.Timestamp",
        subscribed_domain: "capo_pinpoint_email.types.domain.Domain",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "capo_pinpoint_email.types.list_domain_deliverability_campaigns_response.ListDomainDeliverabilityCampaignsResponse":
        """<p>Retrieve deliverability data for all the campaigns that used a specific domain to send email during a specified time range. This data is available for a domain only if you enabled the Deliverability dashboard (<code>PutDeliverabilityDashboardOption</code> operation) for the domain.</p>

        Args:
            start_date: <p>The first day, in Unix time format, that you want to obtain deliverability data for.</p>
            end_date: <p>The last day, in Unix time format, that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the <code>StartDate</code> parameter.</p>
            subscribed_domain: <p>The domain to obtain deliverability data for.</p>
            next_token: <p>A token that’s returned from a previous call to the <code>ListDomainDeliverabilityCampaigns</code> operation. This token indicates the position of a campaign in the list of campaigns.</p>
            page_size: <p>The maximum number of results to include in response to a single call to the <code>ListDomainDeliverabilityCampaigns</code> operation. If the number of results is larger than the number that you specify in this parameter, the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.list_domain_deliverability_campaigns_request.ListDomainDeliverabilityCampaignsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.list_domain_deliverability_campaigns_response.ListDomainDeliverabilityCampaignsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_domain_deliverability_campaigns

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_domain_deliverability_campaigns.async_list_domain_deliverability_campaigns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.list_domain_deliverability_campaigns_request.ListDomainDeliverabilityCampaignsRequest = {
            "start_date": start_date,
            "end_date": end_date,
            "subscribed_domain": subscribed_domain,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_domain_deliverability_campaigns(
        self,
        start_date: "capo_pinpoint_email.types.timestamp.Timestamp",
        end_date: "capo_pinpoint_email.types.timestamp.Timestamp",
        subscribed_domain: "capo_pinpoint_email.types.domain.Domain",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_pinpoint_email.types.list_domain_deliverability_campaigns_response.ListDomainDeliverabilityCampaignsResponse]":
        _token = next_token
        while True:
            _response = await self.list_domain_deliverability_campaigns(
                start_date,
                end_date,
                subscribed_domain,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_email_identities(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "capo_pinpoint_email.types.list_email_identities_response.ListEmailIdentitiesResponse":
        """<p>Returns a list of all of the email identities that are associated with your Amazon Pinpoint account. An identity can be either an email address or a domain. This operation returns identities that are verified as well as those that aren't.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListEmailIdentities</code> to indicate the position in the list of identities.</p>
            page_size: <p>The number of results to show in a single call to <code>ListEmailIdentities</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 0, and can be no more than 1000.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.list_email_identities_request.ListEmailIdentitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.list_email_identities_response.ListEmailIdentitiesResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_email_identities

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_email_identities.async_list_email_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.list_email_identities_request.ListEmailIdentitiesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_email_identities(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        next_token: Optional["capo_pinpoint_email.types.next_token.NextToken"] = None,
        page_size: Optional["capo_pinpoint_email.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_pinpoint_email.types.list_email_identities_response.ListEmailIdentitiesResponse]":
        _token = next_token
        while True:
            _response = await self.list_email_identities(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_pinpoint_email.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieve a list of the tags (keys and values) that are associated with a specified resource. A <i>tag</i> is a label that you optionally define and associate with a resource in Amazon Pinpoint. Each tag consists of a required <i>tag key</i> and an optional associated <i>tag value</i>. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to retrieve tag information for.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_dedicated_ip_warmup_attributes(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        auto_warmup_enabled: Optional[
            "capo_pinpoint_email.types.enabled.Enabled"
        ] = None,
    ) -> "capo_pinpoint_email.types.put_account_dedicated_ip_warmup_attributes_response.PutAccountDedicatedIpWarmupAttributesResponse":
        """<p>Enable or disable the automatic warm-up feature for dedicated IP addresses.</p>

        Args:
            auto_warmup_enabled: <p>Enables or disables the automatic warm-up feature for dedicated IP addresses that are associated with your Amazon Pinpoint account in the current AWS Region. Set to <code>true</code> to enable the automatic warm-up feature, or set to <code>false</code> to disable it.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_account_dedicated_ip_warmup_attributes_request.PutAccountDedicatedIpWarmupAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_account_dedicated_ip_warmup_attributes_response.PutAccountDedicatedIpWarmupAttributesResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_account_dedicated_ip_warmup_attributes

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_account_dedicated_ip_warmup_attributes.async_put_account_dedicated_ip_warmup_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_account_dedicated_ip_warmup_attributes_request.PutAccountDedicatedIpWarmupAttributesRequest = {}
        if auto_warmup_enabled is not None:
            input_["auto_warmup_enabled"] = auto_warmup_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_sending_attributes(
        self,
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        sending_enabled: Optional["capo_pinpoint_email.types.enabled.Enabled"] = None,
    ) -> "capo_pinpoint_email.types.put_account_sending_attributes_response.PutAccountSendingAttributesResponse":
        """<p>Enable or disable the ability of your account to send email.</p>

        Args:
            sending_enabled: <p>Enables or disables your account's ability to send email. Set to <code>true</code> to enable email sending, or set to <code>false</code> to disable email sending.</p> <note> <p>If AWS paused your account's ability to send email, you can't use this operation to resume your account's ability to send email.</p> </note>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_account_sending_attributes_request.PutAccountSendingAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_account_sending_attributes_response.PutAccountSendingAttributesResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_account_sending_attributes

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_account_sending_attributes.async_put_account_sending_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_account_sending_attributes_request.PutAccountSendingAttributesRequest = {}
        if sending_enabled is not None:
            input_["sending_enabled"] = sending_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_delivery_options(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        tls_policy: Optional["capo_pinpoint_email.types.tls_policy.TlsPolicy"] = None,
        sending_pool_name: Optional[
            "capo_pinpoint_email.types.sending_pool_name.SendingPoolName"
        ] = None,
    ) -> "capo_pinpoint_email.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse":
        """<p>Associate a configuration set with a dedicated IP pool. You can use dedicated IP pools to create groups of dedicated IP addresses for sending specific types of email.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that you want to associate with a dedicated IP pool.</p>
            tls_policy: <p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is <code>Require</code>, messages are only delivered if a TLS connection can be established. If the value is <code>Optional</code>, messages can be delivered in plain text if a TLS connection can't be established.</p>
            sending_pool_name: <p>The name of the dedicated IP pool that you want to associate with the configuration set.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_configuration_set_delivery_options_request.PutConfigurationSetDeliveryOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_configuration_set_delivery_options

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_configuration_set_delivery_options.async_put_configuration_set_delivery_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_configuration_set_delivery_options_request.PutConfigurationSetDeliveryOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if tls_policy is not None:
            input_["tls_policy"] = tls_policy
        if sending_pool_name is not None:
            input_["sending_pool_name"] = sending_pool_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_reputation_options(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        reputation_metrics_enabled: Optional[
            "capo_pinpoint_email.types.enabled.Enabled"
        ] = None,
    ) -> "capo_pinpoint_email.types.put_configuration_set_reputation_options_response.PutConfigurationSetReputationOptionsResponse":
        """<p>Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific AWS Region.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that you want to enable or disable reputation metric tracking for.</p>
            reputation_metrics_enabled: <p>If <code>true</code>, tracking of reputation metrics is enabled for the configuration set. If <code>false</code>, tracking of reputation metrics is disabled for the configuration set.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_configuration_set_reputation_options_request.PutConfigurationSetReputationOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_configuration_set_reputation_options_response.PutConfigurationSetReputationOptionsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_configuration_set_reputation_options

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_configuration_set_reputation_options.async_put_configuration_set_reputation_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_configuration_set_reputation_options_request.PutConfigurationSetReputationOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if reputation_metrics_enabled is not None:
            input_["reputation_metrics_enabled"] = reputation_metrics_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_sending_options(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        sending_enabled: Optional["capo_pinpoint_email.types.enabled.Enabled"] = None,
    ) -> "capo_pinpoint_email.types.put_configuration_set_sending_options_response.PutConfigurationSetSendingOptionsResponse":
        """<p>Enable or disable email sending for messages that use a particular configuration set in a specific AWS Region.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that you want to enable or disable email sending for.</p>
            sending_enabled: <p>If <code>true</code>, email sending is enabled for the configuration set. If <code>false</code>, email sending is disabled for the configuration set.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_configuration_set_sending_options_request.PutConfigurationSetSendingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_configuration_set_sending_options_response.PutConfigurationSetSendingOptionsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_configuration_set_sending_options

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_configuration_set_sending_options.async_put_configuration_set_sending_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_configuration_set_sending_options_request.PutConfigurationSetSendingOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if sending_enabled is not None:
            input_["sending_enabled"] = sending_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_tracking_options(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        custom_redirect_domain: Optional[
            "capo_pinpoint_email.types.custom_redirect_domain.CustomRedirectDomain"
        ] = None,
    ) -> "capo_pinpoint_email.types.put_configuration_set_tracking_options_response.PutConfigurationSetTrackingOptionsResponse":
        """<p>Specify a custom domain to use for open and click tracking elements in email that you send using Amazon Pinpoint.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that you want to add a custom tracking domain to.</p>
            custom_redirect_domain: <p>The domain that you want to use to track open and click events.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_configuration_set_tracking_options_request.PutConfigurationSetTrackingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_configuration_set_tracking_options_response.PutConfigurationSetTrackingOptionsResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_configuration_set_tracking_options

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_configuration_set_tracking_options.async_put_configuration_set_tracking_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_configuration_set_tracking_options_request.PutConfigurationSetTrackingOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if custom_redirect_domain is not None:
            input_["custom_redirect_domain"] = custom_redirect_domain

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_dedicated_ip_in_pool(
        self,
        ip: "capo_pinpoint_email.types.ip.Ip",
        destination_pool_name: "capo_pinpoint_email.types.pool_name.PoolName",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.put_dedicated_ip_in_pool_response.PutDedicatedIpInPoolResponse":
        """<p>Move a dedicated IP address to an existing dedicated IP pool.</p> <note> <p>The dedicated IP address that you specify must already exist, and must be associated with your Amazon Pinpoint account. </p> <p>The dedicated IP pool you specify must already exist. You can create a new pool by using the <code>CreateDedicatedIpPool</code> operation.</p> </note>

        Args:
            ip: <p>The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that's associated with your Amazon Pinpoint account.</p>
            destination_pool_name: <p>The name of the IP pool that you want to add the dedicated IP address to. You have to specify an IP pool that already exists.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_dedicated_ip_in_pool_request.PutDedicatedIpInPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_dedicated_ip_in_pool_response.PutDedicatedIpInPoolResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_dedicated_ip_in_pool

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_dedicated_ip_in_pool.async_put_dedicated_ip_in_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_dedicated_ip_in_pool_request.PutDedicatedIpInPoolRequest = {
            "ip": ip,
            "destination_pool_name": destination_pool_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_dedicated_ip_warmup_attributes(
        self,
        ip: "capo_pinpoint_email.types.ip.Ip",
        warmup_percentage: "capo_pinpoint_email.types.percentage100_wrapper.Percentage100Wrapper",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.put_dedicated_ip_warmup_attributes_response.PutDedicatedIpWarmupAttributesResponse":
        """<p></p>

        Args:
            ip: <p>The dedicated IP address that you want to update the warm-up attributes for.</p>
            warmup_percentage: <p>The warm-up percentage that you want to associate with the dedicated IP address.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_dedicated_ip_warmup_attributes_request.PutDedicatedIpWarmupAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_dedicated_ip_warmup_attributes_response.PutDedicatedIpWarmupAttributesResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_dedicated_ip_warmup_attributes

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_dedicated_ip_warmup_attributes.async_put_dedicated_ip_warmup_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_dedicated_ip_warmup_attributes_request.PutDedicatedIpWarmupAttributesRequest = {
            "ip": ip,
            "warmup_percentage": warmup_percentage,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_deliverability_dashboard_option(
        self,
        dashboard_enabled: "capo_pinpoint_email.types.enabled.Enabled",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        subscribed_domains: Optional[
            "capo_pinpoint_email.types.domain_deliverability_tracking_options.DomainDeliverabilityTrackingOptions"
        ] = None,
    ) -> "capo_pinpoint_email.types.put_deliverability_dashboard_option_response.PutDeliverabilityDashboardOptionResponse":
        """<p>Enable or disable the Deliverability dashboard for your Amazon Pinpoint account. When you enable the Deliverability dashboard, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.</p> <p>When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon Pinpoint. For more information about the features and cost of a Deliverability dashboard subscription, see <a href="http://aws.amazon.com/pinpoint/pricing/">Amazon Pinpoint Pricing</a>.</p>

        Args:
            dashboard_enabled: <p>Specifies whether to enable the Deliverability dashboard for your Amazon Pinpoint account. To enable the dashboard, set this value to <code>true</code>.</p>
            subscribed_domains: <p>An array of objects, one for each verified domain that you use to send email and enabled the Deliverability dashboard for.</p>

        Raises:
            capo_pinpoint_email.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_deliverability_dashboard_option_request.PutDeliverabilityDashboardOptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_deliverability_dashboard_option_response.PutDeliverabilityDashboardOptionResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_deliverability_dashboard_option

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_deliverability_dashboard_option.async_put_deliverability_dashboard_option(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_deliverability_dashboard_option_request.PutDeliverabilityDashboardOptionRequest = {
            "dashboard_enabled": dashboard_enabled
        }
        if subscribed_domains is not None:
            input_["subscribed_domains"] = subscribed_domains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_email_identity_dkim_attributes(
        self,
        email_identity: "capo_pinpoint_email.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        signing_enabled: Optional["capo_pinpoint_email.types.enabled.Enabled"] = None,
    ) -> "capo_pinpoint_email.types.put_email_identity_dkim_attributes_response.PutEmailIdentityDkimAttributesResponse":
        """<p>Used to enable or disable DKIM authentication for an email identity.</p>

        Args:
            email_identity: <p>The email identity that you want to change the DKIM settings for.</p>
            signing_enabled: <p>Sets the DKIM signing configuration for the identity.</p> <p>When you set this value <code>true</code>, then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. When you set this value to <code>false</code>, then the messages that Amazon Pinpoint sends from the identity aren't DKIM-signed.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_email_identity_dkim_attributes_request.PutEmailIdentityDkimAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_email_identity_dkim_attributes_response.PutEmailIdentityDkimAttributesResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_email_identity_dkim_attributes

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_email_identity_dkim_attributes.async_put_email_identity_dkim_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_email_identity_dkim_attributes_request.PutEmailIdentityDkimAttributesRequest = {
            "email_identity": email_identity
        }
        if signing_enabled is not None:
            input_["signing_enabled"] = signing_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_email_identity_feedback_attributes(
        self,
        email_identity: "capo_pinpoint_email.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        email_forwarding_enabled: Optional[
            "capo_pinpoint_email.types.enabled.Enabled"
        ] = None,
    ) -> "capo_pinpoint_email.types.put_email_identity_feedback_attributes_response.PutEmailIdentityFeedbackAttributesResponse":
        """<p>Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.</p> <p>When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.</p> <p>When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).</p>

        Args:
            email_identity: <p>The email identity that you want to configure bounce and complaint feedback forwarding for.</p>
            email_forwarding_enabled: <p>Sets the feedback forwarding configuration for the identity.</p> <p>If the value is <code>true</code>, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.</p> <p>When you set this value to <code>false</code>, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_email_identity_feedback_attributes_request.PutEmailIdentityFeedbackAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_email_identity_feedback_attributes_response.PutEmailIdentityFeedbackAttributesResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_email_identity_feedback_attributes

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_email_identity_feedback_attributes.async_put_email_identity_feedback_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_email_identity_feedback_attributes_request.PutEmailIdentityFeedbackAttributesRequest = {
            "email_identity": email_identity
        }
        if email_forwarding_enabled is not None:
            input_["email_forwarding_enabled"] = email_forwarding_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_email_identity_mail_from_attributes(
        self,
        email_identity: "capo_pinpoint_email.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        mail_from_domain: Optional[
            "capo_pinpoint_email.types.mail_from_domain_name.MailFromDomainName"
        ] = None,
        behavior_on_mx_failure: Optional[
            "capo_pinpoint_email.types.behavior_on_mx_failure.BehaviorOnMxFailure"
        ] = None,
    ) -> "capo_pinpoint_email.types.put_email_identity_mail_from_attributes_response.PutEmailIdentityMailFromAttributesResponse":
        """<p>Used to enable or disable the custom Mail-From domain configuration for an email identity.</p>

        Args:
            email_identity: <p>The verified email identity that you want to set up the custom MAIL FROM domain for.</p>
            mail_from_domain: <p> The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria:</p> <ul> <li> <p>It has to be a subdomain of the verified identity.</p> </li> <li> <p>It can't be used to receive email.</p> </li> <li> <p>It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails.</p> </li> </ul>
            behavior_on_mx_failure: <p>The action that you want Amazon Pinpoint to take if it can't read the required MX record when you send an email. When you set this value to <code>UseDefaultValue</code>, Amazon Pinpoint uses <i>amazonses.com</i> as the MAIL FROM domain. When you set this value to <code>RejectMessage</code>, Amazon Pinpoint returns a <code>MailFromDomainNotVerified</code> error, and doesn't attempt to deliver the email.</p> <p>These behaviors are taken when the custom MAIL FROM domain configuration is in the <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code> states.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.put_email_identity_mail_from_attributes_request.PutEmailIdentityMailFromAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.put_email_identity_mail_from_attributes_response.PutEmailIdentityMailFromAttributesResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_email_identity_mail_from_attributes

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.put_email_identity_mail_from_attributes.async_put_email_identity_mail_from_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.put_email_identity_mail_from_attributes_request.PutEmailIdentityMailFromAttributesRequest = {
            "email_identity": email_identity
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

    async def send_email(
        self,
        destination: "capo_pinpoint_email.types.destination.Destination",
        content: "capo_pinpoint_email.types.email_content.EmailContent",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
        from_email_address: Optional[
            "capo_pinpoint_email.types.email_address.EmailAddress"
        ] = None,
        reply_to_addresses: Optional[
            "capo_pinpoint_email.types.email_address_list.EmailAddressList"
        ] = None,
        feedback_forwarding_email_address: Optional[
            "capo_pinpoint_email.types.email_address.EmailAddress"
        ] = None,
        email_tags: Optional[
            "capo_pinpoint_email.types.message_tag_list.MessageTagList"
        ] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
        ] = None,
    ) -> "capo_pinpoint_email.types.send_email_response.SendEmailResponse":
        """<p>Sends an email message. You can use the Amazon Pinpoint Email API to send two types of messages:</p> <ul> <li> <p> <b>Simple</b> – A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon Pinpoint assembles the message for you.</p> </li> <li> <p> <b>Raw</b> – A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message.</p> </li> </ul>

        Args:
            from_email_address: <p>The email address that you want to use as the "From" address for the email. The address that you specify has to be verified. </p>
            destination: <p>An object that contains the recipients of the email message.</p>
            reply_to_addresses: <p>The "Reply-to" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.</p>
            feedback_forwarding_email_address: <p>The address that Amazon Pinpoint should send bounce and complaint notifications to.</p>
            content: <p>An object that contains the body of the message. You can send either a Simple message or a Raw message.</p>
            email_tags: <p>A list of tags, in the form of name/value pairs, to apply to an email that you send using the <code>SendEmail</code> operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. </p>
            configuration_set_name: <p>The name of the configuration set that you want to use when sending the email.</p>

        Raises:
            capo_pinpoint_email.errors.account_suspended_exception.AccountSuspendedException: <p>The message can't be sent because the account's ability to send email has been permanently restricted.</p>
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_pinpoint_email.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p>The message can't be sent because the sending domain isn't verified.</p>
            capo_pinpoint_email.errors.message_rejected.MessageRejected: <p>The message can't be sent because it contains invalid content.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.sending_paused_exception.SendingPausedException: <p>The message can't be sent because the account's ability to send email is currently paused.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.send_email_request.SendEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.send_email_response.SendEmailResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.send_email

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.send_email.async_send_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.send_email_request.SendEmailRequest = {
            "destination": destination,
            "content": content,
        }
        if from_email_address is not None:
            input_["from_email_address"] = from_email_address
        if reply_to_addresses is not None:
            input_["reply_to_addresses"] = reply_to_addresses
        if feedback_forwarding_email_address is not None:
            input_["feedback_forwarding_email_address"] = (
                feedback_forwarding_email_address
            )
        if email_tags is not None:
            input_["email_tags"] = email_tags
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_pinpoint_email.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_pinpoint_email.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.tag_resource_response.TagResourceResponse":
        """<p>Add one or more tags (keys and values) to a specified resource. A <i>tag</i> is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.</p> <p>Each tag consists of a required <i>tag key</i> and an associated <i>tag value</i>, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to add one or more tags to.</p>
            tags: <p>A list of the tags that you want to add to the resource. A tag consists of a required tag key (<code>Key</code>) and an associated tag value (<code>Value</code>). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_pinpoint_email.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_pinpoint_email.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove one or more tags (keys and values) from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove one or more tags from.</p>
            tag_keys: <p>The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.</p> <p>To remove more than one tag from the resource, append the <code>TagKeys</code> parameter and argument for each additional tag to remove, separated by an ampersand. For example: <code>/v1/email/tags?ResourceArn=ResourceArn&TagKeys=Key1&TagKeys=Key2</code> </p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName",
        event_destination_name: "capo_pinpoint_email.types.event_destination_name.EventDestinationName",
        event_destination: "capo_pinpoint_email.types.event_destination_definition.EventDestinationDefinition",
        *,
        config_overrides: Optional[AsyncPinpointEmailClientConfig] = None,
    ) -> "capo_pinpoint_email.types.update_configuration_set_event_destination_response.UpdateConfigurationSetEventDestinationResponse":
        """<p>Update the configuration of an event destination for a configuration set.</p> <p>In Amazon Pinpoint, <i>events</i> include message sends, deliveries, opens, clicks, bounces, and complaints. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that contains the event destination that you want to modify.</p>
            event_destination_name: <p>The name of the event destination that you want to modify.</p>
            event_destination: <p>An object that defines the event destination.</p>

        Raises:
            capo_pinpoint_email.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_pinpoint_email.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_pinpoint_email.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_email.types.update_configuration_set_event_destination_request.UpdateConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_email.types.update_configuration_set_event_destination_response.UpdateConfigurationSetEventDestinationResponse"
        ]:
            import capo_pinpoint_email._operations.amazon_pinpoint_email_service.update_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_pinpoint_email._operations.amazon_pinpoint_email_service.update_configuration_set_event_destination.async_update_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_email.types.update_configuration_set_event_destination_request.UpdateConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
            "event_destination": event_destination,
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
