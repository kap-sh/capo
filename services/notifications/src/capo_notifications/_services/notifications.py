"""Generated from Smithy shape ``com.amazonaws.notifications#Notifications``."""

import datetime
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_notifications._auth._signers
import capo_notifications._auth._sigv4
from capo_notifications._auth._identity import Credentials
from capo_notifications._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_notifications._auth._zapros_handler import AuthMiddleware
from capo_notifications._pagination import resolve_path as _resolve_path
from capo_notifications._resources.notifications.channel import Channel
from capo_notifications._resources.notifications.event_rule import EventRule
from capo_notifications._resources.notifications.managed_notification_account_contact_association import (
    ManagedNotificationAccountContactAssociation,
)
from capo_notifications._resources.notifications.managed_notification_additional_channel_association import (
    ManagedNotificationAdditionalChannelAssociation,
)
from capo_notifications._resources.notifications.managed_notification_child_event_resource import (
    ManagedNotificationChildEventResource,
)
from capo_notifications._resources.notifications.managed_notification_configuration import (
    ManagedNotificationConfiguration,
)
from capo_notifications._resources.notifications.managed_notification_event_resource import (
    ManagedNotificationEventResource,
)
from capo_notifications._resources.notifications.notification_configuration import (
    NotificationConfiguration,
)
from capo_notifications._resources.notifications.notification_event_resource import (
    NotificationEventResource,
)
from capo_notifications._resources.notifications.notification_hub import NotificationHub
from capo_notifications._resources.notifications.organization_access import (
    OrganizationAccess,
)
from capo_notifications._resources.notifications.organizational_unit import (
    OrganizationalUnit,
)
from capo_notifications._services._aws_config import aws_config
from capo_notifications._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_notifications.types.account_contact_type
    import capo_notifications.types.account_id
    import capo_notifications.types.aggregation_duration
    import capo_notifications.types.associate_channel_request
    import capo_notifications.types.associate_channel_response
    import capo_notifications.types.associate_managed_notification_account_contact_request
    import capo_notifications.types.associate_managed_notification_account_contact_response
    import capo_notifications.types.associate_managed_notification_additional_channel_request
    import capo_notifications.types.associate_managed_notification_additional_channel_response
    import capo_notifications.types.associate_organizational_unit_request
    import capo_notifications.types.associate_organizational_unit_response
    import capo_notifications.types.channel_arn
    import capo_notifications.types.channel_identifier
    import capo_notifications.types.create_event_rule_request
    import capo_notifications.types.create_event_rule_response
    import capo_notifications.types.create_notification_configuration_request
    import capo_notifications.types.create_notification_configuration_response
    import capo_notifications.types.delete_event_rule_request
    import capo_notifications.types.delete_event_rule_response
    import capo_notifications.types.delete_notification_configuration_request
    import capo_notifications.types.delete_notification_configuration_response
    import capo_notifications.types.deregister_notification_hub_request
    import capo_notifications.types.deregister_notification_hub_response
    import capo_notifications.types.disable_notifications_access_for_organization_request
    import capo_notifications.types.disable_notifications_access_for_organization_response
    import capo_notifications.types.disassociate_channel_request
    import capo_notifications.types.disassociate_channel_response
    import capo_notifications.types.disassociate_managed_notification_account_contact_request
    import capo_notifications.types.disassociate_managed_notification_account_contact_response
    import capo_notifications.types.disassociate_managed_notification_additional_channel_request
    import capo_notifications.types.disassociate_managed_notification_additional_channel_response
    import capo_notifications.types.disassociate_organizational_unit_request
    import capo_notifications.types.disassociate_organizational_unit_response
    import capo_notifications.types.enable_notifications_access_for_organization_request
    import capo_notifications.types.enable_notifications_access_for_organization_response
    import capo_notifications.types.event_rule_arn
    import capo_notifications.types.event_rule_event_pattern
    import capo_notifications.types.event_rule_structure
    import capo_notifications.types.event_type
    import capo_notifications.types.get_event_rule_request
    import capo_notifications.types.get_event_rule_response
    import capo_notifications.types.get_managed_notification_child_event_request
    import capo_notifications.types.get_managed_notification_child_event_response
    import capo_notifications.types.get_managed_notification_configuration_request
    import capo_notifications.types.get_managed_notification_configuration_response
    import capo_notifications.types.get_managed_notification_event_request
    import capo_notifications.types.get_managed_notification_event_response
    import capo_notifications.types.get_notification_configuration_request
    import capo_notifications.types.get_notification_configuration_response
    import capo_notifications.types.get_notification_event_request
    import capo_notifications.types.get_notification_event_response
    import capo_notifications.types.get_notifications_access_for_organization_request
    import capo_notifications.types.get_notifications_access_for_organization_response
    import capo_notifications.types.list_channels_request
    import capo_notifications.types.list_channels_response
    import capo_notifications.types.list_event_rules_request
    import capo_notifications.types.list_event_rules_response
    import capo_notifications.types.list_managed_notification_channel_associations_request
    import capo_notifications.types.list_managed_notification_channel_associations_response
    import capo_notifications.types.list_managed_notification_child_events_request
    import capo_notifications.types.list_managed_notification_child_events_response
    import capo_notifications.types.list_managed_notification_configurations_request
    import capo_notifications.types.list_managed_notification_configurations_response
    import capo_notifications.types.list_managed_notification_events_request
    import capo_notifications.types.list_managed_notification_events_response
    import capo_notifications.types.list_member_accounts_request
    import capo_notifications.types.list_member_accounts_response
    import capo_notifications.types.list_notification_configurations_request
    import capo_notifications.types.list_notification_configurations_response
    import capo_notifications.types.list_notification_events_request
    import capo_notifications.types.list_notification_events_response
    import capo_notifications.types.list_notification_hubs_request
    import capo_notifications.types.list_notification_hubs_response
    import capo_notifications.types.list_organizational_units_request
    import capo_notifications.types.list_organizational_units_response
    import capo_notifications.types.list_tags_for_resource_request
    import capo_notifications.types.list_tags_for_resource_response
    import capo_notifications.types.locale_code
    import capo_notifications.types.managed_notification_channel_association_summary
    import capo_notifications.types.managed_notification_channel_identifier
    import capo_notifications.types.managed_notification_child_event_arn
    import capo_notifications.types.managed_notification_child_event_overview
    import capo_notifications.types.managed_notification_configuration_os_arn
    import capo_notifications.types.managed_notification_configuration_structure
    import capo_notifications.types.managed_notification_event_arn
    import capo_notifications.types.managed_notification_event_overview
    import capo_notifications.types.member_account
    import capo_notifications.types.member_account_notification_configuration_status
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.notification_configuration_description
    import capo_notifications.types.notification_configuration_name
    import capo_notifications.types.notification_configuration_status
    import capo_notifications.types.notification_configuration_structure
    import capo_notifications.types.notification_configuration_subtype
    import capo_notifications.types.notification_event_arn
    import capo_notifications.types.notification_event_overview
    import capo_notifications.types.notification_hub_overview
    import capo_notifications.types.organizational_unit_id
    import capo_notifications.types.region
    import capo_notifications.types.regions
    import capo_notifications.types.register_notification_hub_request
    import capo_notifications.types.register_notification_hub_response
    import capo_notifications.types.source
    import capo_notifications.types.tag_keys
    import capo_notifications.types.tag_map
    import capo_notifications.types.tag_resource_request
    import capo_notifications.types.tag_resource_response
    import capo_notifications.types.untag_resource_request
    import capo_notifications.types.untag_resource_response
    import capo_notifications.types.update_event_rule_request
    import capo_notifications.types.update_event_rule_response
    import capo_notifications.types.update_managed_notification_channel_association_request
    import capo_notifications.types.update_managed_notification_channel_association_response
    import capo_notifications.types.update_notification_configuration_request
    import capo_notifications.types.update_notification_configuration_response


class NotificationsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class NotificationsClient:
    """A client for the ``Notifications`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = NotificationsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.channel = Channel(self)
        self.event_rule = EventRule(self)
        self.managed_notification_account_contact_association = (
            ManagedNotificationAccountContactAssociation(self)
        )
        self.managed_notification_additional_channel_association = (
            ManagedNotificationAdditionalChannelAssociation(self)
        )
        self.managed_notification_child_event_resource = (
            ManagedNotificationChildEventResource(self)
        )
        self.managed_notification_configuration = ManagedNotificationConfiguration(self)
        self.managed_notification_event_resource = ManagedNotificationEventResource(
            self
        )
        self.notification_configuration = NotificationConfiguration(self)
        self.notification_event_resource = NotificationEventResource(self)
        self.notification_hub = NotificationHub(self)
        self.organization_access = OrganizationAccess(self)
        self.organizational_unit = OrganizationalUnit(self)

    def operation_options(
        self, config_overrides: Optional[NotificationsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: NotificationsClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_managed_notification_channel_associations(
        self,
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_managed_notification_channel_associations_response.ListManagedNotificationChannelAssociationsResponse":
        """<p>Returns a list of Account contacts and Channels associated with a <code>ManagedNotificationConfiguration</code>, in paginated format.</p>

        Args:
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to match.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListManagedNotificationChannelAssociations</code> call.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_managed_notification_channel_associations_request.ListManagedNotificationChannelAssociationsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_managed_notification_channel_associations_response.ListManagedNotificationChannelAssociationsResponse"
        ]:
            import capo_notifications._operations.notifications.list_managed_notification_channel_associations

            output, http_response = (
                capo_notifications._operations.notifications.list_managed_notification_channel_associations.list_managed_notification_channel_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_managed_notification_channel_associations_request.ListManagedNotificationChannelAssociationsRequest = {
            "managed_notification_configuration_arn": managed_notification_configuration_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_managed_notification_channel_associations(
        self,
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_notifications.types.managed_notification_channel_association_summary.ManagedNotificationChannelAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_managed_notification_channel_associations(
                managed_notification_configuration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channel_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_member_accounts(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        member_account: Optional[
            "capo_notifications.types.account_id.AccountId"
        ] = None,
        status: Optional[
            "capo_notifications.types.member_account_notification_configuration_status.MemberAccountNotificationConfigurationStatus"
        ] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
    ) -> "capo_notifications.types.list_member_accounts_response.ListMemberAccountsResponse":
        """<p>Returns a list of member accounts associated with a notification configuration.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration used to filter the member accounts.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid values are 1-100.</p>
            next_token: <p>The token for the next page of results. Use the value returned in the previous response.</p>
            member_account: <p>The member account identifier used to filter the results.</p>
            status: <p>The status used to filter the member accounts.</p>
            organizational_unit_id: <p>The organizational unit ID used to filter the member accounts.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_member_accounts_request.ListMemberAccountsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_member_accounts_response.ListMemberAccountsResponse"
        ]:
            import capo_notifications._operations.notifications.list_member_accounts

            output, http_response = (
                capo_notifications._operations.notifications.list_member_accounts.list_member_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_member_accounts_request.ListMemberAccountsRequest = {
            "notification_configuration_arn": notification_configuration_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if member_account is not None:
            input_["member_account"] = member_account
        if status is not None:
            input_["status"] = status
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_member_accounts(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        member_account: Optional[
            "capo_notifications.types.account_id.AccountId"
        ] = None,
        status: Optional[
            "capo_notifications.types.member_account_notification_configuration_status.MemberAccountNotificationConfigurationStatus"
        ] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
    ) -> "Iterator[capo_notifications.types.member_account.MemberAccount]":
        _token = next_token
        while True:
            _response = self.list_member_accounts(
                notification_configuration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                member_account=member_account,
                status=status,
                organizational_unit_id=organizational_unit_id,
            )
            _page = _resolve_path(_response, ("member_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a specified Amazon Resource Name (ARN).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html">Tagging your Amazon Web Services resources</a> in the <i>Tagging Amazon Web Services Resources User Guide</i>.</p> <note> <p>This is only supported for <code>NotificationConfigurations</code>.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) to use to list tags.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_notifications._operations.notifications.list_tags_for_resource

            output, http_response = (
                capo_notifications._operations.notifications.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        tags: "capo_notifications.types.tag_map.TagMap",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.tag_resource_response.TagResourceResponse":
        """<p>Tags the resource with a tag key and value.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html">Tagging your Amazon Web Services resources</a> in the <i>Tagging Amazon Web Services Resources User Guide</i>.</p> <note> <p>This is only supported for <code>NotificationConfigurations</code>.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) to use to tag a resource.</p>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_notifications._operations.notifications.tag_resource

            output, http_response = (
                capo_notifications._operations.notifications.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.tag_resource_request.TagResourceRequest = {
            "arn": arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        tag_keys: "capo_notifications.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.untag_resource_response.UntagResourceResponse":
        """<p>Untags a resource with a specified Amazon Resource Name (ARN).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html">Tagging your Amazon Web Services resources</a> in the <i>Tagging Amazon Web Services Resources User Guide</i>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) to use to untag a resource.</p>
            tag_keys: <p>The tag keys to use to untag a resource.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_notifications._operations.notifications.untag_resource

            output, http_response = (
                capo_notifications._operations.notifications.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.untag_resource_request.UntagResourceRequest = {
            "arn": arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_managed_notification_channel_association(
        self,
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        channel_identifier: "capo_notifications.types.managed_notification_channel_identifier.ManagedNotificationChannelIdentifier",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        is_sensitive_events_subscribed: Optional[bool] = None,
    ) -> "capo_notifications.types.update_managed_notification_channel_association_response.UpdateManagedNotificationChannelAssociationResponse":
        """<p>Updates the <code>isSensitiveEventsSubscribed</code> property of a particular ManagedNotification channel association.</p>

        Args:
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> whose Channel association property you want to update.</p>
            channel_identifier: <p>The identifier of the channel association to update. You can specify one of the following:</p> <ul> <li> <p>An Account contact identifier.</p> </li> <li> <p>A Channel ARN.</p> </li> </ul>
            is_sensitive_events_subscribed: <p>Specifies whether the association is subscribed to sensitive events. The <code>notifications:SubscribeSensitiveEvents</code> permission controls access to sensitive events.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.update_managed_notification_channel_association_request.UpdateManagedNotificationChannelAssociationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.update_managed_notification_channel_association_response.UpdateManagedNotificationChannelAssociationResponse"
        ]:
            import capo_notifications._operations.notifications.update_managed_notification_channel_association

            output, http_response = (
                capo_notifications._operations.notifications.update_managed_notification_channel_association.update_managed_notification_channel_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.update_managed_notification_channel_association_request.UpdateManagedNotificationChannelAssociationRequest = {
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
            "channel_identifier": channel_identifier,
        }
        if is_sensitive_events_subscribed is not None:
            input_["is_sensitive_events_subscribed"] = is_sensitive_events_subscribed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_channel(
        self,
        arn: "capo_notifications.types.channel_arn.ChannelArn",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.associate_channel_response.AssociateChannelResponse":
        """<p>Associates a delivery <a href="https://docs.aws.amazon.com/notifications/latest/userguide/managing-delivery-channels.html">Channel</a> with a particular <code>NotificationConfiguration</code>. Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>NotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and notifications-contacts.</p>
            notification_configuration_arn: <p>The ARN of the <code>NotificationConfiguration</code> to associate with the Channel.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.associate_channel_request.AssociateChannelRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.associate_channel_response.AssociateChannelResponse"
        ]:
            import capo_notifications._operations.notifications.associate_channel

            output, http_response = (
                capo_notifications._operations.notifications.associate_channel.associate_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.associate_channel_request.AssociateChannelRequest = {
            "arn": arn,
            "notification_configuration_arn": notification_configuration_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_channel(
        self,
        arn: "capo_notifications.types.channel_arn.ChannelArn",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_channel_response.DisassociateChannelResponse":
        """<p>Disassociates a Channel from a specified <code>NotificationConfiguration</code>. Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Channel to disassociate.</p>
            notification_configuration_arn: <p>The ARN of the <code>NotificationConfiguration</code> to disassociate.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.disassociate_channel_request.DisassociateChannelRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.disassociate_channel_response.DisassociateChannelResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_channel

            output, http_response = (
                capo_notifications._operations.notifications.disassociate_channel.disassociate_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.disassociate_channel_request.DisassociateChannelRequest = {
            "arn": arn,
            "notification_configuration_arn": notification_configuration_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_channels(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_channels_response.ListChannelsResponse":
        """<p>Returns a list of Channels for a <code>NotificationConfiguration</code>.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code>.</p>
            max_results: <p>The maximum number of results to be returned in this call. The default value is 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous ListNotificationEvents call. <code>NextToken</code> uses Base64 encoding.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_notifications._operations.notifications.list_channels

            output, http_response = (
                capo_notifications._operations.notifications.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_channels_request.ListChannelsRequest = {
            "notification_configuration_arn": notification_configuration_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_channels(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_notifications.types.channel_arn.ChannelArn]":
        _token = next_token
        while True:
            _response = self.list_channels(
                notification_configuration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_event_rule(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        source: "capo_notifications.types.source.Source",
        event_type: "capo_notifications.types.event_type.EventType",
        regions: "capo_notifications.types.regions.Regions",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        event_pattern: Optional[
            "capo_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
        ] = None,
    ) -> "capo_notifications.types.create_event_rule_response.CreateEventRuleResponse":
        """<p>Creates an <a href="https://docs.aws.amazon.com/notifications/latest/userguide/glossary.html"> <code>EventRule</code> </a> that is associated with a specified <code>NotificationConfiguration</code>.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> associated with this <code>EventRule</code>.</p>
            source: <p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            event_type: <p>The event type to match.</p> <p>Must match one of the valid Amazon EventBridge event types. For example, EC2 Instance State-change Notification and Amazon CloudWatch Alarm State Change. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            event_pattern: <p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>
            regions: <p>A list of Amazon Web Services Regions that send events to this <code>EventRule</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.create_event_rule_request.CreateEventRuleRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.create_event_rule_response.CreateEventRuleResponse"
        ]:
            import capo_notifications._operations.notifications.create_event_rule

            output, http_response = (
                capo_notifications._operations.notifications.create_event_rule.create_event_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.create_event_rule_request.CreateEventRuleRequest = {
            "notification_configuration_arn": notification_configuration_arn,
            "source": source,
            "event_type": event_type,
            "regions": regions,
        }
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_event_rule(
        self,
        arn: "capo_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        event_pattern: Optional[
            "capo_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
        ] = None,
        regions: Optional["capo_notifications.types.regions.Regions"] = None,
    ) -> "capo_notifications.types.update_event_rule_response.UpdateEventRuleResponse":
        """<p>Updates an existing <code>EventRule</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) to use to update the <code>EventRule</code>.</p>
            event_pattern: <p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>
            regions: <p>A list of Amazon Web Services Regions that sends events to this <code>EventRule</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.update_event_rule_request.UpdateEventRuleRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.update_event_rule_response.UpdateEventRuleResponse"
        ]:
            import capo_notifications._operations.notifications.update_event_rule

            output, http_response = (
                capo_notifications._operations.notifications.update_event_rule.update_event_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.update_event_rule_request.UpdateEventRuleRequest = {
            "arn": arn
        }
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern
        if regions is not None:
            input_["regions"] = regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_rule(
        self,
        arn: "capo_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.get_event_rule_response.GetEventRuleResponse":
        """<p>Returns a specified <code>EventRule</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>EventRule</code> to return.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_event_rule_request.GetEventRuleRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_event_rule_response.GetEventRuleResponse"
        ]:
            import capo_notifications._operations.notifications.get_event_rule

            output, http_response = (
                capo_notifications._operations.notifications.get_event_rule.get_event_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.get_event_rule_request.GetEventRuleRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_rule(
        self,
        arn: "capo_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.delete_event_rule_response.DeleteEventRuleResponse":
        """<p>Deletes an <code>EventRule</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>EventRule</code> to delete.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.delete_event_rule_request.DeleteEventRuleRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.delete_event_rule_response.DeleteEventRuleResponse"
        ]:
            import capo_notifications._operations.notifications.delete_event_rule

            output, http_response = (
                capo_notifications._operations.notifications.delete_event_rule.delete_event_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.delete_event_rule_request.DeleteEventRuleRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_event_rules(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_event_rules_response.ListEventRulesResponse":
        """<p>Returns a list of <code>EventRules</code> according to specified filters, in reverse chronological order (newest first).</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code>.</p>
            max_results: <p>The maximum number of results to be returned in this call. The default value is 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_event_rules_request.ListEventRulesRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_event_rules_response.ListEventRulesResponse"
        ]:
            import capo_notifications._operations.notifications.list_event_rules

            output, http_response = (
                capo_notifications._operations.notifications.list_event_rules.list_event_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_event_rules_request.ListEventRulesRequest = {
            "notification_configuration_arn": notification_configuration_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_event_rules(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_notifications.types.event_rule_structure.EventRuleStructure]":
        _token = next_token
        while True:
            _response = self.list_event_rules(
                notification_configuration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("event_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_managed_notification_account_contact(
        self,
        contact_identifier: "capo_notifications.types.account_contact_type.AccountContactType",
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        is_sensitive_events_subscribed: Optional[bool] = None,
    ) -> "capo_notifications.types.associate_managed_notification_account_contact_response.AssociateManagedNotificationAccountContactResponse":
        """<p>Associates an Account Contact with a particular <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            contact_identifier: <p>A unique value of an Account Contact Type to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the Account Contact.</p>
            is_sensitive_events_subscribed: <p>Specifies whether this contact is subscribed to sensitive events. The <code>notifications:SubscribeSensitiveEvents</code> permission controls access to sensitive events. Defaults to false.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.associate_managed_notification_account_contact_request.AssociateManagedNotificationAccountContactRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.associate_managed_notification_account_contact_response.AssociateManagedNotificationAccountContactResponse"
        ]:
            import capo_notifications._operations.notifications.associate_managed_notification_account_contact

            output, http_response = (
                capo_notifications._operations.notifications.associate_managed_notification_account_contact.associate_managed_notification_account_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.associate_managed_notification_account_contact_request.AssociateManagedNotificationAccountContactRequest = {
            "contact_identifier": contact_identifier,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }
        if is_sensitive_events_subscribed is not None:
            input_["is_sensitive_events_subscribed"] = is_sensitive_events_subscribed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_managed_notification_account_contact(
        self,
        contact_identifier: "capo_notifications.types.account_contact_type.AccountContactType",
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_managed_notification_account_contact_response.DisassociateManagedNotificationAccountContactResponse":
        """<p>Disassociates an Account Contact with a particular <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            contact_identifier: <p>The unique value of an Account Contact Type to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the Account Contact.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.disassociate_managed_notification_account_contact_request.DisassociateManagedNotificationAccountContactRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.disassociate_managed_notification_account_contact_response.DisassociateManagedNotificationAccountContactResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_managed_notification_account_contact

            output, http_response = (
                capo_notifications._operations.notifications.disassociate_managed_notification_account_contact.disassociate_managed_notification_account_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.disassociate_managed_notification_account_contact_request.DisassociateManagedNotificationAccountContactRequest = {
            "contact_identifier": contact_identifier,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_managed_notification_additional_channel(
        self,
        channel_arn: "capo_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        is_sensitive_events_subscribed: Optional[bool] = None,
    ) -> "capo_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse":
        """<p>Associates an additional Channel with a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and email (notifications-contacts).</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the additional Channel.</p>
            is_sensitive_events_subscribed: <p>Specifies whether this channel is subscribed to sensitive events. The <code>notifications:SubscribeSensitiveEvents</code> permission controls access to sensitive events. Defaults to false.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse"
        ]:
            import capo_notifications._operations.notifications.associate_managed_notification_additional_channel

            output, http_response = (
                capo_notifications._operations.notifications.associate_managed_notification_additional_channel.associate_managed_notification_additional_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest = {
            "channel_arn": channel_arn,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }
        if is_sensitive_events_subscribed is not None:
            input_["is_sensitive_events_subscribed"] = is_sensitive_events_subscribed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_managed_notification_additional_channel(
        self,
        channel_arn: "capo_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse":
        """<p>Disassociates an additional Channel from a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the Managed Notification Configuration to associate with the additional Channel.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_managed_notification_additional_channel

            output, http_response = (
                capo_notifications._operations.notifications.disassociate_managed_notification_additional_channel.disassociate_managed_notification_additional_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest = {
            "channel_arn": channel_arn,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_managed_notification_child_event(
        self,
        arn: "capo_notifications.types.managed_notification_child_event_arn.ManagedNotificationChildEventArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
    ) -> "capo_notifications.types.get_managed_notification_child_event_response.GetManagedNotificationChildEventResponse":
        """<p>Returns the child event of a specific given <code>ManagedNotificationEvent</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationChildEvent</code> to return.</p>
            locale: <p>The locale code of the language used for the retrieved <code>ManagedNotificationChildEvent</code>. The default locale is English <code>en_US</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_managed_notification_child_event_request.GetManagedNotificationChildEventRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_managed_notification_child_event_response.GetManagedNotificationChildEventResponse"
        ]:
            import capo_notifications._operations.notifications.get_managed_notification_child_event

            output, http_response = (
                capo_notifications._operations.notifications.get_managed_notification_child_event.get_managed_notification_child_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.get_managed_notification_child_event_request.GetManagedNotificationChildEventRequest = {
            "arn": arn
        }
        if locale is not None:
            input_["locale"] = locale

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_managed_notification_child_events(
        self,
        aggregate_managed_notification_event_arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
        max_results: Optional[int] = None,
        related_account: Optional[
            "capo_notifications.types.account_id.AccountId"
        ] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_managed_notification_child_events_response.ListManagedNotificationChildEventsResponse":
        """<p>Returns a list of <code>ManagedNotificationChildEvents</code> for a specified aggregate <code>ManagedNotificationEvent</code>, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            aggregate_managed_notification_event_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationEvent</code>.</p>
            start_time: <p>The earliest time of events to return from this call.</p>
            end_time: <p>Latest time of events to return from this call.</p>
            locale: <p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English.<code>en_US</code>.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            related_account: <p>The Amazon Web Services account ID associated with the Managed Notification Child Events.</p>
            organizational_unit_id: <p>The identifier of the Amazon Web Services Organizations organizational unit (OU) associated with the Managed Notification Child Events.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous ListManagedNotificationChannelAssociations call. Next token uses Base64 encoding.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_managed_notification_child_events_request.ListManagedNotificationChildEventsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_managed_notification_child_events_response.ListManagedNotificationChildEventsResponse"
        ]:
            import capo_notifications._operations.notifications.list_managed_notification_child_events

            output, http_response = (
                capo_notifications._operations.notifications.list_managed_notification_child_events.list_managed_notification_child_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_managed_notification_child_events_request.ListManagedNotificationChildEventsRequest = {
            "aggregate_managed_notification_event_arn": aggregate_managed_notification_event_arn
        }
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if locale is not None:
            input_["locale"] = locale
        if max_results is not None:
            input_["max_results"] = max_results
        if related_account is not None:
            input_["related_account"] = related_account
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_managed_notification_child_events(
        self,
        aggregate_managed_notification_event_arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
        max_results: Optional[int] = None,
        related_account: Optional[
            "capo_notifications.types.account_id.AccountId"
        ] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_notifications.types.managed_notification_child_event_overview.ManagedNotificationChildEventOverview]":
        _token = next_token
        while True:
            _response = self.list_managed_notification_child_events(
                aggregate_managed_notification_event_arn,
                config_overrides=config_overrides,
                start_time=start_time,
                end_time=end_time,
                locale=locale,
                max_results=max_results,
                related_account=related_account,
                organizational_unit_id=organizational_unit_id,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("managed_notification_child_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_managed_notification_configuration(
        self,
        arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse":
        """<p>Returns a specified <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to return.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.get_managed_notification_configuration

            output, http_response = (
                capo_notifications._operations.notifications.get_managed_notification_configuration.get_managed_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_managed_notification_configurations(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        channel_identifier: Optional[
            "capo_notifications.types.channel_identifier.ChannelIdentifier"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse":
        """<p>Returns a list of Managed Notification Configurations according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            channel_identifier: <p>The identifier or ARN of the notification channel to filter configurations by.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous ListManagedNotificationChannelAssociations call. Next token uses Base64 encoding.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse"
        ]:
            import capo_notifications._operations.notifications.list_managed_notification_configurations

            output, http_response = (
                capo_notifications._operations.notifications.list_managed_notification_configurations.list_managed_notification_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest = {}
        if channel_identifier is not None:
            input_["channel_identifier"] = channel_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_managed_notification_configurations(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        channel_identifier: Optional[
            "capo_notifications.types.channel_identifier.ChannelIdentifier"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_notifications.types.managed_notification_configuration_structure.ManagedNotificationConfigurationStructure]":
        _token = next_token
        while True:
            _response = self.list_managed_notification_configurations(
                config_overrides=config_overrides,
                channel_identifier=channel_identifier,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("managed_notification_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_managed_notification_event(
        self,
        arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
    ) -> "capo_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse":
        """<p>Returns a specified <code>ManagedNotificationEvent</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationEvent</code> to return.</p>
            locale: <p>The locale code of the language used for the retrieved <code>ManagedNotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse"
        ]:
            import capo_notifications._operations.notifications.get_managed_notification_event

            output, http_response = (
                capo_notifications._operations.notifications.get_managed_notification_event.get_managed_notification_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest = {
            "arn": arn
        }
        if locale is not None:
            input_["locale"] = locale

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_managed_notification_events(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
        source: Optional["capo_notifications.types.source.Source"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
        related_account: Optional[
            "capo_notifications.types.account_id.AccountId"
        ] = None,
        include_sensitive_events: Optional[bool] = None,
    ) -> "capo_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse":
        """<p>Returns a list of Managed Notification Events according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            start_time: <p>The earliest time of events to return from this call.</p>
            end_time: <p>Latest time of events to return from this call.</p>
            locale: <p>The locale code of the language used for the retrieved NotificationEvent. The default locale is English (en_US).</p>
            source: <p>The Amazon Web Services service the event originates from. For example aws.cloudwatch.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListManagedNotificationChannelAssociations</code> call. Next token uses Base64 encoding.</p>
            organizational_unit_id: <p>The Organizational Unit Id that an Amazon Web Services account belongs to.</p>
            related_account: <p>The Amazon Web Services account ID associated with the Managed Notification Events.</p>
            include_sensitive_events: <p>Specifies whether to include sensitive events in the result. By default, only non-sensitive events are returned. The <code>notifications:AccessSensitiveEvents</code> permission controls access to sensitive events.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse"
        ]:
            import capo_notifications._operations.notifications.list_managed_notification_events

            output, http_response = (
                capo_notifications._operations.notifications.list_managed_notification_events.list_managed_notification_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest = {}
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if locale is not None:
            input_["locale"] = locale
        if source is not None:
            input_["source"] = source
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id
        if related_account is not None:
            input_["related_account"] = related_account
        if include_sensitive_events is not None:
            input_["include_sensitive_events"] = include_sensitive_events

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_managed_notification_events(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
        source: Optional["capo_notifications.types.source.Source"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
        related_account: Optional[
            "capo_notifications.types.account_id.AccountId"
        ] = None,
        include_sensitive_events: Optional[bool] = None,
    ) -> "Iterator[capo_notifications.types.managed_notification_event_overview.ManagedNotificationEventOverview]":
        _token = next_token
        while True:
            _response = self.list_managed_notification_events(
                config_overrides=config_overrides,
                start_time=start_time,
                end_time=end_time,
                locale=locale,
                source=source,
                max_results=max_results,
                next_token=_token,
                organizational_unit_id=organizational_unit_id,
                related_account=related_account,
                include_sensitive_events=include_sensitive_events,
            )
            _page = _resolve_path(_response, ("managed_notification_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_notification_configuration(
        self,
        name: "capo_notifications.types.notification_configuration_name.NotificationConfigurationName",
        description: "capo_notifications.types.notification_configuration_description.NotificationConfigurationDescription",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        aggregation_duration: Optional[
            "capo_notifications.types.aggregation_duration.AggregationDuration"
        ] = None,
        tags: Optional["capo_notifications.types.tag_map.TagMap"] = None,
    ) -> "capo_notifications.types.create_notification_configuration_response.CreateNotificationConfigurationResponse":
        """<p>Creates a new <code>NotificationConfiguration</code>.</p>

        Args:
            name: <p>The name of the <code>NotificationConfiguration</code>. Supports RFC 3986's unreserved characters.</p>
            description: <p>The description of the <code>NotificationConfiguration</code>.</p>
            aggregation_duration: <p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.create_notification_configuration_request.CreateNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.create_notification_configuration_response.CreateNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.create_notification_configuration

            output, http_response = (
                capo_notifications._operations.notifications.create_notification_configuration.create_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.create_notification_configuration_request.CreateNotificationConfigurationRequest = {
            "name": name,
            "description": description,
        }
        if aggregation_duration is not None:
            input_["aggregation_duration"] = aggregation_duration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_notification_configuration(
        self,
        arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        name: Optional[
            "capo_notifications.types.notification_configuration_name.NotificationConfigurationName"
        ] = None,
        description: Optional[
            "capo_notifications.types.notification_configuration_description.NotificationConfigurationDescription"
        ] = None,
        aggregation_duration: Optional[
            "capo_notifications.types.aggregation_duration.AggregationDuration"
        ] = None,
    ) -> "capo_notifications.types.update_notification_configuration_response.UpdateNotificationConfigurationResponse":
        """<p>Updates a <code>NotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) used to update the <code>NotificationConfiguration</code>.</p>
            name: <p>The name of the <code>NotificationConfiguration</code>.</p>
            description: <p>The description of the <code>NotificationConfiguration</code>.</p>
            aggregation_duration: <p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.update_notification_configuration_response.UpdateNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.update_notification_configuration

            output, http_response = (
                capo_notifications._operations.notifications.update_notification_configuration.update_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if aggregation_duration is not None:
            input_["aggregation_duration"] = aggregation_duration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_notification_configuration(
        self,
        arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.get_notification_configuration_response.GetNotificationConfigurationResponse":
        """<p>Returns a specified <code>NotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> to return.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.get_notification_configuration

            output, http_response = (
                capo_notifications._operations.notifications.get_notification_configuration.get_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_notification_configuration(
        self,
        arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.delete_notification_configuration_response.DeleteNotificationConfigurationResponse":
        """<p>Deletes a <code>NotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> to delete.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.delete_notification_configuration_response.DeleteNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.delete_notification_configuration

            output, http_response = (
                capo_notifications._operations.notifications.delete_notification_configuration.delete_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_notification_configurations(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        event_rule_source: Optional["capo_notifications.types.source.Source"] = None,
        channel_arn: Optional["capo_notifications.types.channel_arn.ChannelArn"] = None,
        status: Optional[
            "capo_notifications.types.notification_configuration_status.NotificationConfigurationStatus"
        ] = None,
        subtype: Optional[
            "capo_notifications.types.notification_configuration_subtype.NotificationConfigurationSubtype"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse":
        """<p>Returns a list of abbreviated <code>NotificationConfigurations</code> according to specified filters, in reverse chronological order (newest first).</p>

        Args:
            event_rule_source: <p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to match.</p>
            status: <p>The <code>NotificationConfiguration</code> status to match.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ACTIVE</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>ACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>PARTIALLY_ACTIVE</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> <li> <p>Any call can be run.</p> </li> </ul> </li> <li> <p> <code>INACTIVE</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>INACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>DELETING</code> </p> <ul> <li> <p>This <code>NotificationConfiguration</code> is being deleted.</p> </li> <li> <p>Only <code>GET</code> and <code>LIST</code> calls can be run.</p> </li> </ul> </li> </ul> </li> </ul>
            subtype: <p>The subtype used to filter the notification configurations in the request.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse"
        ]:
            import capo_notifications._operations.notifications.list_notification_configurations

            output, http_response = (
                capo_notifications._operations.notifications.list_notification_configurations.list_notification_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest = {}
        if event_rule_source is not None:
            input_["event_rule_source"] = event_rule_source
        if channel_arn is not None:
            input_["channel_arn"] = channel_arn
        if status is not None:
            input_["status"] = status
        if subtype is not None:
            input_["subtype"] = subtype
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_notification_configurations(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        event_rule_source: Optional["capo_notifications.types.source.Source"] = None,
        channel_arn: Optional["capo_notifications.types.channel_arn.ChannelArn"] = None,
        status: Optional[
            "capo_notifications.types.notification_configuration_status.NotificationConfigurationStatus"
        ] = None,
        subtype: Optional[
            "capo_notifications.types.notification_configuration_subtype.NotificationConfigurationSubtype"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_notifications.types.notification_configuration_structure.NotificationConfigurationStructure]":
        _token = next_token
        while True:
            _response = self.list_notification_configurations(
                config_overrides=config_overrides,
                event_rule_source=event_rule_source,
                channel_arn=channel_arn,
                status=status,
                subtype=subtype,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("notification_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_notification_event(
        self,
        arn: "capo_notifications.types.notification_event_arn.NotificationEventArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
    ) -> "capo_notifications.types.get_notification_event_response.GetNotificationEventResponse":
        """<p>Returns a specified <code>NotificationEvent</code>.</p> <important> <p>User Notifications stores notifications in the individual Regions you register as notification hubs and the Region of the source event rule. <code>GetNotificationEvent</code> only returns notifications stored in the same Region in which the action is called. User Notifications doesn't backfill notifications to new Regions selected as notification hubs. For this reason, we recommend that you make calls in your oldest registered notification hub. For more information, see <a href="https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html">Notification hubs</a> in the <i>Amazon Web Services User Notifications User Guide</i>.</p> </important>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationEvent</code> to return.</p>
            locale: <p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English <code>en_US</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_notification_event_request.GetNotificationEventRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_notification_event_response.GetNotificationEventResponse"
        ]:
            import capo_notifications._operations.notifications.get_notification_event

            output, http_response = (
                capo_notifications._operations.notifications.get_notification_event.get_notification_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.get_notification_event_request.GetNotificationEventRequest = {
            "arn": arn
        }
        if locale is not None:
            input_["locale"] = locale

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_notification_events(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
        source: Optional["capo_notifications.types.source.Source"] = None,
        include_child_events: Optional[bool] = None,
        aggregate_notification_event_arn: Optional[
            "capo_notifications.types.notification_event_arn.NotificationEventArn"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
    ) -> "capo_notifications.types.list_notification_events_response.ListNotificationEventsResponse":
        """<p>Returns a list of <code>NotificationEvents</code> according to specified filters, in reverse chronological order (newest first).</p> <important> <p>User Notifications stores notifications in the individual Regions you register as notification hubs and the Region of the source event rule. ListNotificationEvents only returns notifications stored in the same Region in which the action is called. User Notifications doesn't backfill notifications to new Regions selected as notification hubs. For this reason, we recommend that you make calls in your oldest registered notification hub. For more information, see <a href="https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html">Notification hubs</a> in the <i>Amazon Web Services User Notifications User Guide</i>.</p> </important>

        Args:
            start_time: <p>The earliest time of events to return from this call.</p>
            end_time: <p>Latest time of events to return from this call.</p>
            locale: <p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>
            source: <p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            include_child_events: <p>Include aggregated child events in the result.</p>
            aggregate_notification_event_arn: <p>The Amazon Resource Name (ARN) of the <code>aggregatedNotificationEventArn</code> to match.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>
            organizational_unit_id: <p>The unique identifier of the organizational unit used to filter notification events.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_notification_events_request.ListNotificationEventsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_notification_events_response.ListNotificationEventsResponse"
        ]:
            import capo_notifications._operations.notifications.list_notification_events

            output, http_response = (
                capo_notifications._operations.notifications.list_notification_events.list_notification_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_notification_events_request.ListNotificationEventsRequest = {}
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if locale is not None:
            input_["locale"] = locale
        if source is not None:
            input_["source"] = source
        if include_child_events is not None:
            input_["include_child_events"] = include_child_events
        if aggregate_notification_event_arn is not None:
            input_["aggregate_notification_event_arn"] = (
                aggregate_notification_event_arn
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_notification_events(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
        source: Optional["capo_notifications.types.source.Source"] = None,
        include_child_events: Optional[bool] = None,
        aggregate_notification_event_arn: Optional[
            "capo_notifications.types.notification_event_arn.NotificationEventArn"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
    ) -> "Iterator[capo_notifications.types.notification_event_overview.NotificationEventOverview]":
        _token = next_token
        while True:
            _response = self.list_notification_events(
                config_overrides=config_overrides,
                start_time=start_time,
                end_time=end_time,
                locale=locale,
                source=source,
                include_child_events=include_child_events,
                aggregate_notification_event_arn=aggregate_notification_event_arn,
                max_results=max_results,
                next_token=_token,
                organizational_unit_id=organizational_unit_id,
            )
            _page = _resolve_path(_response, ("notification_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def register_notification_hub(
        self,
        notification_hub_region: "capo_notifications.types.region.Region",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse":
        """<p>Registers a <code>NotificationHub</code> in the specified Region.</p> <p>There is a maximum of one <code>NotificationHub</code> per Region. You can have a maximum of 3 <code>NotificationHub</code> resources at a time.</p>

        Args:
            notification_hub_region: <p>The Region of the <code>NotificationHub</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse"
        ]:
            import capo_notifications._operations.notifications.register_notification_hub

            output, http_response = (
                capo_notifications._operations.notifications.register_notification_hub.register_notification_hub(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest = {
            "notification_hub_region": notification_hub_region
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_notification_hub(
        self,
        notification_hub_region: "capo_notifications.types.region.Region",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse":
        """<p>Deregisters a <code>NotificationHub</code> in the specified Region.</p> <note> <p>You can't deregister the last <code>NotificationHub</code> in the account. <code>NotificationEvents</code> stored in the deregistered <code>NotificationHub</code> are no longer visible. Recreating a new <code>NotificationHub</code> in the same Region restores access to those <code>NotificationEvents</code>.</p> </note>

        Args:
            notification_hub_region: <p>The <code>NotificationHub</code> Region.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse"
        ]:
            import capo_notifications._operations.notifications.deregister_notification_hub

            output, http_response = (
                capo_notifications._operations.notifications.deregister_notification_hub.deregister_notification_hub(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest = {
            "notification_hub_region": notification_hub_region
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_notification_hubs(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse":
        """<p>Returns a list of <code>NotificationHubs</code>.</p>

        Args:
            max_results: <p>The maximum number of records to list in a single response.</p>
            next_token: <p>A pagination token. Set to null to start listing notification hubs from the start.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse"
        ]:
            import capo_notifications._operations.notifications.list_notification_hubs

            output, http_response = (
                capo_notifications._operations.notifications.list_notification_hubs.list_notification_hubs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_notification_hubs(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_notifications.types.notification_hub_overview.NotificationHubOverview]":
        _token = next_token
        while True:
            _response = self.list_notification_hubs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("notification_hubs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def enable_notifications_access_for_organization(
        self, *, config_overrides: Optional[NotificationsClientConfig] = None
    ) -> "capo_notifications.types.enable_notifications_access_for_organization_response.EnableNotificationsAccessForOrganizationResponse":
        """<p>Enables service trust between User Notifications and Amazon Web Services Organizations.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.enable_notifications_access_for_organization_request.EnableNotificationsAccessForOrganizationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.enable_notifications_access_for_organization_response.EnableNotificationsAccessForOrganizationResponse"
        ]:
            import capo_notifications._operations.notifications.enable_notifications_access_for_organization

            output, http_response = (
                capo_notifications._operations.notifications.enable_notifications_access_for_organization.enable_notifications_access_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.enable_notifications_access_for_organization_request.EnableNotificationsAccessForOrganizationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_notifications_access_for_organization(
        self, *, config_overrides: Optional[NotificationsClientConfig] = None
    ) -> "capo_notifications.types.get_notifications_access_for_organization_response.GetNotificationsAccessForOrganizationResponse":
        """<p>Returns the AccessStatus of Service Trust Enablement for User Notifications and Amazon Web Services Organizations.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_notifications_access_for_organization_request.GetNotificationsAccessForOrganizationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_notifications_access_for_organization_response.GetNotificationsAccessForOrganizationResponse"
        ]:
            import capo_notifications._operations.notifications.get_notifications_access_for_organization

            output, http_response = (
                capo_notifications._operations.notifications.get_notifications_access_for_organization.get_notifications_access_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.get_notifications_access_for_organization_request.GetNotificationsAccessForOrganizationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_notifications_access_for_organization(
        self, *, config_overrides: Optional[NotificationsClientConfig] = None
    ) -> "capo_notifications.types.disable_notifications_access_for_organization_response.DisableNotificationsAccessForOrganizationResponse":
        """<p>Disables service trust between User Notifications and Amazon Web Services Organizations.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.disable_notifications_access_for_organization_request.DisableNotificationsAccessForOrganizationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.disable_notifications_access_for_organization_response.DisableNotificationsAccessForOrganizationResponse"
        ]:
            import capo_notifications._operations.notifications.disable_notifications_access_for_organization

            output, http_response = (
                capo_notifications._operations.notifications.disable_notifications_access_for_organization.disable_notifications_access_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.disable_notifications_access_for_organization_request.DisableNotificationsAccessForOrganizationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_organizational_unit(
        self,
        organizational_unit_id: "capo_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse":
        """<p>Associates an organizational unit with a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to associate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to associate with the organizational unit.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse"
        ]:
            import capo_notifications._operations.notifications.associate_organizational_unit

            output, http_response = (
                capo_notifications._operations.notifications.associate_organizational_unit.associate_organizational_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest = {
            "organizational_unit_id": organizational_unit_id,
            "notification_configuration_arn": notification_configuration_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_organizational_unit(
        self,
        organizational_unit_id: "capo_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse":
        """<p>Removes the association between an organizational unit and a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to disassociate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to disassociate from the organizational unit.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_organizational_unit

            output, http_response = (
                capo_notifications._operations.notifications.disassociate_organizational_unit.disassociate_organizational_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest = {
            "organizational_unit_id": organizational_unit_id,
            "notification_configuration_arn": notification_configuration_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_organizational_units(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse":
        """<p>Returns a list of organizational units associated with a notification configuration.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration used to filter the organizational units.</p>
            max_results: <p>The maximum number of organizational units to return in a single call. Valid values are 1-100.</p>
            next_token: <p>The token for the next page of results. Use the value returned in the previous response.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse"
        ]:
            import capo_notifications._operations.notifications.list_organizational_units

            output, http_response = (
                capo_notifications._operations.notifications.list_organizational_units.list_organizational_units(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest = {
            "notification_configuration_arn": notification_configuration_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_organizational_units(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> (
        "Iterator[capo_notifications.types.organizational_unit_id.OrganizationalUnitId]"
    ):
        _token = next_token
        while True:
            _response = self.list_organizational_units(
                notification_configuration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("organizational_units",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
