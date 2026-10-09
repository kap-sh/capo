"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#CodeStarNotifications_20191015``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_codestar_notifications._auth._signers
import capo_codestar_notifications._auth._sigv4
from capo_codestar_notifications._auth._identity import Credentials
from capo_codestar_notifications._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_codestar_notifications._auth._zapros_handler import AuthMiddleware
from capo_codestar_notifications._pagination import resolve_path as _resolve_path
from capo_codestar_notifications._services._aws_config import aws_config
from capo_codestar_notifications._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_codestar_notifications.types.client_request_token
    import capo_codestar_notifications.types.create_notification_rule_request
    import capo_codestar_notifications.types.create_notification_rule_result
    import capo_codestar_notifications.types.delete_notification_rule_request
    import capo_codestar_notifications.types.delete_notification_rule_result
    import capo_codestar_notifications.types.delete_target_request
    import capo_codestar_notifications.types.delete_target_result
    import capo_codestar_notifications.types.describe_notification_rule_request
    import capo_codestar_notifications.types.describe_notification_rule_result
    import capo_codestar_notifications.types.detail_type
    import capo_codestar_notifications.types.event_type_ids
    import capo_codestar_notifications.types.event_type_summary
    import capo_codestar_notifications.types.force_unsubscribe_all
    import capo_codestar_notifications.types.list_event_types_filters
    import capo_codestar_notifications.types.list_event_types_request
    import capo_codestar_notifications.types.list_event_types_result
    import capo_codestar_notifications.types.list_notification_rules_filters
    import capo_codestar_notifications.types.list_notification_rules_request
    import capo_codestar_notifications.types.list_notification_rules_result
    import capo_codestar_notifications.types.list_tags_for_resource_request
    import capo_codestar_notifications.types.list_tags_for_resource_result
    import capo_codestar_notifications.types.list_targets_filters
    import capo_codestar_notifications.types.list_targets_request
    import capo_codestar_notifications.types.list_targets_result
    import capo_codestar_notifications.types.max_results
    import capo_codestar_notifications.types.next_token
    import capo_codestar_notifications.types.notification_rule_arn
    import capo_codestar_notifications.types.notification_rule_name
    import capo_codestar_notifications.types.notification_rule_resource
    import capo_codestar_notifications.types.notification_rule_status
    import capo_codestar_notifications.types.notification_rule_summary
    import capo_codestar_notifications.types.subscribe_request
    import capo_codestar_notifications.types.subscribe_result
    import capo_codestar_notifications.types.tag_keys
    import capo_codestar_notifications.types.tag_resource_request
    import capo_codestar_notifications.types.tag_resource_result
    import capo_codestar_notifications.types.tags
    import capo_codestar_notifications.types.target
    import capo_codestar_notifications.types.target_address
    import capo_codestar_notifications.types.target_summary
    import capo_codestar_notifications.types.targets
    import capo_codestar_notifications.types.unsubscribe_request
    import capo_codestar_notifications.types.unsubscribe_result
    import capo_codestar_notifications.types.untag_resource_request
    import capo_codestar_notifications.types.untag_resource_result
    import capo_codestar_notifications.types.update_notification_rule_request
    import capo_codestar_notifications.types.update_notification_rule_result


class codestarnotificationsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class codestarnotificationsClient:
    """A client for the ``codestarnotifications`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = codestarnotificationsClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[codestarnotificationsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: codestarnotificationsClientConfig = config_overrides or {}
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

    def create_notification_rule(
        self,
        name: "capo_codestar_notifications.types.notification_rule_name.NotificationRuleName",
        event_type_ids: "capo_codestar_notifications.types.event_type_ids.EventTypeIds",
        resource: "capo_codestar_notifications.types.notification_rule_resource.NotificationRuleResource",
        targets: "capo_codestar_notifications.types.targets.Targets",
        detail_type: "capo_codestar_notifications.types.detail_type.DetailType",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        client_request_token: Optional[
            "capo_codestar_notifications.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_codestar_notifications.types.tags.Tags"] = None,
        status: Optional[
            "capo_codestar_notifications.types.notification_rule_status.NotificationRuleStatus"
        ] = None,
    ) -> "capo_codestar_notifications.types.create_notification_rule_result.CreateNotificationRuleResult":
        """<p>Creates a notification rule for a resource. The rule specifies the events you want notifications about and the targets (such as Amazon Q Developer in chat applications topics or Amazon Q Developer in chat applications clients configured for Slack) where you want to receive them.</p>

        Args:
            name: <p>The name for the notification rule. Notification rule names must be unique in your Amazon Web Services account.</p>
            event_type_ids: <p>A list of event types associated with this notification rule. For a list of allowed events, see <a>EventTypeSummary</a>.</p>
            resource: <p>The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported resources include pipelines in CodePipeline, repositories in CodeCommit, and build projects in CodeBuild.</p>
            targets: <p>A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and Amazon Q Developer in chat applications clients to associate with the notification rule.</p>
            detail_type: <p>The level of detail to include in the notifications for this resource. <code>BASIC</code> will include only the contents of the event as it would appear in Amazon CloudWatch. <code>FULL</code> will include any supplemental information provided by CodeStar Notifications and/or the service for the resource for which the notification is created.</p>
            client_request_token: <p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request with the same parameters is received and a token is included, the request returns information about the initial request that used that token.</p> <note> <p>The Amazon Web Services SDKs prepopulate client request tokens. If you are using an Amazon Web Services SDK, an idempotency token is created for you.</p> </note>
            tags: <p>A list of tags to apply to this notification rule. Key names cannot start with "<code>aws</code>". </p>
            status: <p>The status of the notification rule. The default value is <code>ENABLED</code>. If the status is set to <code>DISABLED</code>, notifications aren't sent for the notification rule.</p>

        Raises:
            capo_codestar_notifications.errors.access_denied_exception.AccessDeniedException: <p>CodeStar Notifications can't create the notification rule because you do not have sufficient permissions.</p>
            capo_codestar_notifications.errors.concurrent_modification_exception.ConcurrentModificationException: <p>CodeStar Notifications can't complete the request because the resource is being modified by another process. Wait a few minutes and try again.</p>
            capo_codestar_notifications.errors.configuration_exception.ConfigurationException: <p>Some or all of the configuration is incomplete, missing, or not valid.</p>
            capo_codestar_notifications.errors.limit_exceeded_exception.LimitExceededException: <p>One of the CodeStar Notifications limits has been exceeded. Limits apply to accounts, notification rules, notifications, resources, and targets. For more information, see Limits.</p>
            capo_codestar_notifications.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>A resource with the same name or ID already exists. Notification rule names must be unique in your Amazon Web Services account.</p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.create_notification_rule_request.CreateNotificationRuleRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.create_notification_rule_result.CreateNotificationRuleResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.create_notification_rule

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.create_notification_rule.create_notification_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.create_notification_rule_request.CreateNotificationRuleRequest = {
            "name": name,
            "event_type_ids": event_type_ids,
            "resource": resource,
            "targets": targets,
            "detail_type": detail_type,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_notification_rule(
        self,
        arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
    ) -> "capo_codestar_notifications.types.delete_notification_rule_result.DeleteNotificationRuleResult":
        """<p>Deletes a notification rule for a resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the notification rule you want to delete.</p>

        Raises:
            capo_codestar_notifications.errors.concurrent_modification_exception.ConcurrentModificationException: <p>CodeStar Notifications can't complete the request because the resource is being modified by another process. Wait a few minutes and try again.</p>
            capo_codestar_notifications.errors.limit_exceeded_exception.LimitExceededException: <p>One of the CodeStar Notifications limits has been exceeded. Limits apply to accounts, notification rules, notifications, resources, and targets. For more information, see Limits.</p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.delete_notification_rule_request.DeleteNotificationRuleRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.delete_notification_rule_result.DeleteNotificationRuleResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.delete_notification_rule

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.delete_notification_rule.delete_notification_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.delete_notification_rule_request.DeleteNotificationRuleRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_target(
        self,
        target_address: "capo_codestar_notifications.types.target_address.TargetAddress",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        force_unsubscribe_all: Optional[
            "capo_codestar_notifications.types.force_unsubscribe_all.ForceUnsubscribeAll"
        ] = None,
    ) -> "capo_codestar_notifications.types.delete_target_result.DeleteTargetResult":
        """<p>Deletes a specified target for notifications.</p>

        Args:
            target_address: <p>The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client to delete.</p>
            force_unsubscribe_all: <p>A Boolean value that can be used to delete all associations with this Amazon Q Developer in chat applications topic. The default value is FALSE. If set to TRUE, all associations between that target and every notification rule in your Amazon Web Services account are deleted.</p>

        Raises:
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.delete_target_request.DeleteTargetRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.delete_target_result.DeleteTargetResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.delete_target

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.delete_target.delete_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.delete_target_request.DeleteTargetRequest = {
            "target_address": target_address
        }
        if force_unsubscribe_all is not None:
            input_["force_unsubscribe_all"] = force_unsubscribe_all

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_notification_rule(
        self,
        arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
    ) -> "capo_codestar_notifications.types.describe_notification_rule_result.DescribeNotificationRuleResult":
        """<p>Returns information about a specified notification rule.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the notification rule.</p>

        Raises:
            capo_codestar_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>CodeStar Notifications can't find a resource that matches the provided ARN. </p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.describe_notification_rule_request.DescribeNotificationRuleRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.describe_notification_rule_result.DescribeNotificationRuleResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.describe_notification_rule

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.describe_notification_rule.describe_notification_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.describe_notification_rule_request.DescribeNotificationRuleRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_event_types(
        self,
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        filters: Optional[
            "capo_codestar_notifications.types.list_event_types_filters.ListEventTypesFilters"
        ] = None,
        next_token: Optional[
            "capo_codestar_notifications.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codestar_notifications.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "capo_codestar_notifications.types.list_event_types_result.ListEventTypesResult"
    ):
        """<p>Returns information about the event types available for configuring notifications.</p>

        Args:
            filters: <p>The filters to use to return information by service or resource type.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
            max_results: <p>A non-negative integer used to limit the number of returned results. The default number is 50. The maximum number of results that can be returned is 100.</p>

        Raises:
            capo_codestar_notifications.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value for the enumeration token used in the request to return the next batch of the results is not valid. </p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.list_event_types_request.ListEventTypesRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.list_event_types_result.ListEventTypesResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.list_event_types

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.list_event_types.list_event_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.list_event_types_request.ListEventTypesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_event_types(
        self,
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        filters: Optional[
            "capo_codestar_notifications.types.list_event_types_filters.ListEventTypesFilters"
        ] = None,
        next_token: Optional[
            "capo_codestar_notifications.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codestar_notifications.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_codestar_notifications.types.event_type_summary.EventTypeSummary]":
        _token = next_token
        while True:
            _response = self.list_event_types(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_notification_rules(
        self,
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        filters: Optional[
            "capo_codestar_notifications.types.list_notification_rules_filters.ListNotificationRulesFilters"
        ] = None,
        next_token: Optional[
            "capo_codestar_notifications.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codestar_notifications.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_codestar_notifications.types.list_notification_rules_result.ListNotificationRulesResult":
        """<p>Returns a list of the notification rules for an Amazon Web Services account.</p>

        Args:
            filters: <p>The filters to use to return information by service or resource type. For valid values, see <a>ListNotificationRulesFilter</a>.</p> <note> <p>A filter with the same name can appear more than once when used with OR statements. Filters with different names should be applied with AND statements.</p> </note>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
            max_results: <p>A non-negative integer used to limit the number of returned results. The maximum number of results that can be returned is 100.</p>

        Raises:
            capo_codestar_notifications.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value for the enumeration token used in the request to return the next batch of the results is not valid. </p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.list_notification_rules_request.ListNotificationRulesRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.list_notification_rules_result.ListNotificationRulesResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.list_notification_rules

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.list_notification_rules.list_notification_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.list_notification_rules_request.ListNotificationRulesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_notification_rules(
        self,
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        filters: Optional[
            "capo_codestar_notifications.types.list_notification_rules_filters.ListNotificationRulesFilters"
        ] = None,
        next_token: Optional[
            "capo_codestar_notifications.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codestar_notifications.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_codestar_notifications.types.notification_rule_summary.NotificationRuleSummary]":
        _token = next_token
        while True:
            _response = self.list_notification_rules(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("notification_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
    ) -> "capo_codestar_notifications.types.list_tags_for_resource_result.ListTagsForResourceResult":
        """<p>Returns a list of the tags associated with a notification rule.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for the notification rule.</p>

        Raises:
            capo_codestar_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>CodeStar Notifications can't find a resource that matches the provided ARN. </p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.list_tags_for_resource

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_targets(
        self,
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        filters: Optional[
            "capo_codestar_notifications.types.list_targets_filters.ListTargetsFilters"
        ] = None,
        next_token: Optional[
            "capo_codestar_notifications.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codestar_notifications.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_codestar_notifications.types.list_targets_result.ListTargetsResult":
        """<p>Returns a list of the notification rule targets for an Amazon Web Services account.</p>

        Args:
            filters: <p>The filters to use to return information by service or resource type. Valid filters include target type, target address, and target status.</p> <note> <p>A filter with the same name can appear more than once when used with OR statements. Filters with different names should be applied with AND statements.</p> </note>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
            max_results: <p>A non-negative integer used to limit the number of returned results. The maximum number of results that can be returned is 100.</p>

        Raises:
            capo_codestar_notifications.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value for the enumeration token used in the request to return the next batch of the results is not valid. </p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.list_targets_request.ListTargetsRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.list_targets_result.ListTargetsResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.list_targets

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.list_targets.list_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.list_targets_request.ListTargetsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_targets(
        self,
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        filters: Optional[
            "capo_codestar_notifications.types.list_targets_filters.ListTargetsFilters"
        ] = None,
        next_token: Optional[
            "capo_codestar_notifications.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codestar_notifications.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_codestar_notifications.types.target_summary.TargetSummary]":
        _token = next_token
        while True:
            _response = self.list_targets(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def subscribe(
        self,
        arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn",
        target: "capo_codestar_notifications.types.target.Target",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        client_request_token: Optional[
            "capo_codestar_notifications.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_codestar_notifications.types.subscribe_result.SubscribeResult":
        """<p>Creates an association between a notification rule and an Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client so that the associated target can receive notifications when the events described in the rule are triggered.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the notification rule for which you want to create the association.</p>
            client_request_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>

        Raises:
            capo_codestar_notifications.errors.configuration_exception.ConfigurationException: <p>Some or all of the configuration is incomplete, missing, or not valid.</p>
            capo_codestar_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>CodeStar Notifications can't find a resource that matches the provided ARN. </p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.subscribe_request.SubscribeRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.subscribe_result.SubscribeResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.subscribe

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.subscribe.subscribe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.subscribe_request.SubscribeRequest = {
            "arn": arn,
            "target": target,
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn",
        tags: "capo_codestar_notifications.types.tags.Tags",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
    ) -> "capo_codestar_notifications.types.tag_resource_result.TagResourceResult":
        """<p>Associates a set of provided tags with a notification rule.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the notification rule to tag.</p>
            tags: <p>The list of tags to associate with the resource. Tag key names cannot start with "<code>aws</code>".</p>

        Raises:
            capo_codestar_notifications.errors.concurrent_modification_exception.ConcurrentModificationException: <p>CodeStar Notifications can't complete the request because the resource is being modified by another process. Wait a few minutes and try again.</p>
            capo_codestar_notifications.errors.limit_exceeded_exception.LimitExceededException: <p>One of the CodeStar Notifications limits has been exceeded. Limits apply to accounts, notification rules, notifications, resources, and targets. For more information, see Limits.</p>
            capo_codestar_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>CodeStar Notifications can't find a resource that matches the provided ARN. </p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.tag_resource_result.TagResourceResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.tag_resource

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.tag_resource_request.TagResourceRequest = {
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

    def unsubscribe(
        self,
        arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn",
        target_address: "capo_codestar_notifications.types.target_address.TargetAddress",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
    ) -> "capo_codestar_notifications.types.unsubscribe_result.UnsubscribeResult":
        """<p>Removes an association between a notification rule and an Amazon Q Developer in chat applications topic so that subscribers to that topic stop receiving notifications when the events described in the rule are triggered.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the notification rule.</p>
            target_address: <p>The ARN of the Amazon Q Developer in chat applications topic to unsubscribe from the notification rule.</p>

        Raises:
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.unsubscribe_request.UnsubscribeRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.unsubscribe_result.UnsubscribeResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.unsubscribe

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.unsubscribe.unsubscribe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.unsubscribe_request.UnsubscribeRequest = {
            "arn": arn,
            "target_address": target_address,
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
        arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn",
        tag_keys: "capo_codestar_notifications.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
    ) -> "capo_codestar_notifications.types.untag_resource_result.UntagResourceResult":
        """<p>Removes the association between one or more provided tags and a notification rule.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the notification rule from which to remove the tags.</p>
            tag_keys: <p>The key names of the tags to remove.</p>

        Raises:
            capo_codestar_notifications.errors.concurrent_modification_exception.ConcurrentModificationException: <p>CodeStar Notifications can't complete the request because the resource is being modified by another process. Wait a few minutes and try again.</p>
            capo_codestar_notifications.errors.limit_exceeded_exception.LimitExceededException: <p>One of the CodeStar Notifications limits has been exceeded. Limits apply to accounts, notification rules, notifications, resources, and targets. For more information, see Limits.</p>
            capo_codestar_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>CodeStar Notifications can't find a resource that matches the provided ARN. </p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.untag_resource_result.UntagResourceResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.untag_resource

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.untag_resource_request.UntagResourceRequest = {
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

    def update_notification_rule(
        self,
        arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn",
        *,
        config_overrides: Optional[codestarnotificationsClientConfig] = None,
        name: Optional[
            "capo_codestar_notifications.types.notification_rule_name.NotificationRuleName"
        ] = None,
        status: Optional[
            "capo_codestar_notifications.types.notification_rule_status.NotificationRuleStatus"
        ] = None,
        event_type_ids: Optional[
            "capo_codestar_notifications.types.event_type_ids.EventTypeIds"
        ] = None,
        targets: Optional["capo_codestar_notifications.types.targets.Targets"] = None,
        detail_type: Optional[
            "capo_codestar_notifications.types.detail_type.DetailType"
        ] = None,
    ) -> "capo_codestar_notifications.types.update_notification_rule_result.UpdateNotificationRuleResult":
        """<p>Updates a notification rule for a resource. You can change the events that trigger the notification rule, the status of the rule, and the targets that receive the notifications.</p> <note> <p>To add or remove tags for a notification rule, you must use <a>TagResource</a> and <a>UntagResource</a>.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the notification rule.</p>
            name: <p>The name of the notification rule.</p>
            status: <p>The status of the notification rule. Valid statuses include enabled (sending notifications) or disabled (not sending notifications).</p>
            event_type_ids: <p>A list of event types associated with this notification rule. For a complete list of event types and IDs, see <a href="https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api">Notification concepts</a> in the <i>Developer Tools Console User Guide</i>.</p>
            targets: <p>The address and type of the targets to receive notifications from this notification rule.</p>
            detail_type: <p>The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in Amazon CloudWatch. FULL will include any supplemental information provided by CodeStar Notifications and/or the service for the resource for which the notification is created.</p>

        Raises:
            capo_codestar_notifications.errors.configuration_exception.ConfigurationException: <p>Some or all of the configuration is incomplete, missing, or not valid.</p>
            capo_codestar_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>CodeStar Notifications can't find a resource that matches the provided ARN. </p>
            capo_codestar_notifications.errors.validation_exception.ValidationException: <p>One or more parameter values are not valid.</p>
            capo_codestar_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codestar_notifications.types.update_notification_rule_request.UpdateNotificationRuleRequest]",
        ) -> OperationResponse[
            "capo_codestar_notifications.types.update_notification_rule_result.UpdateNotificationRuleResult"
        ]:
            import capo_codestar_notifications._operations.code_star_notifications_20191015.update_notification_rule

            output, http_response = (
                capo_codestar_notifications._operations.code_star_notifications_20191015.update_notification_rule.update_notification_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codestar_notifications.types.update_notification_rule_request.UpdateNotificationRuleRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if event_type_ids is not None:
            input_["event_type_ids"] = event_type_ids
        if targets is not None:
            input_["targets"] = targets
        if detail_type is not None:
            input_["detail_type"] = detail_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
