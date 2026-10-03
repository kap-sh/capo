from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_notifications._auth._signers
import capo_notifications._auth._sigv4
from capo_notifications._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_notifications.types.create_event_rule_request
    import capo_notifications.types.create_event_rule_response
    import capo_notifications.types.delete_event_rule_request
    import capo_notifications.types.delete_event_rule_response
    import capo_notifications.types.event_rule_arn
    import capo_notifications.types.event_rule_event_pattern
    import capo_notifications.types.event_rule_structure
    import capo_notifications.types.event_type
    import capo_notifications.types.get_event_rule_request
    import capo_notifications.types.get_event_rule_response
    import capo_notifications.types.list_event_rules_request
    import capo_notifications.types.list_event_rules_response
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.regions
    import capo_notifications.types.source
    import capo_notifications.types.update_event_rule_request
    import capo_notifications.types.update_event_rule_response
    from capo_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from capo_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class EventRule:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def create(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def put(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncEventRule:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def create(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        source: "capo_notifications.types.source.Source",
        event_type: "capo_notifications.types.event_type.EventType",
        regions: "capo_notifications.types.regions.Regions",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.create_event_rule_request.CreateEventRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.create_event_rule_response.CreateEventRuleResponse"
        ]:
            import capo_notifications._operations.notifications.create_event_rule

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.create_event_rule.async_create_event_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.create_event_rule_request.CreateEventRuleRequest = {
            "notification_configuration_arn": notification_configuration_arn,
            "source": source,
            "event_type": event_type,
            "regions": regions,
        }
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put(
        self,
        arn: "capo_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.update_event_rule_request.UpdateEventRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.update_event_rule_response.UpdateEventRuleResponse"
        ]:
            import capo_notifications._operations.notifications.update_event_rule

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.update_event_rule.async_update_event_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.update_event_rule_request.UpdateEventRuleRequest = {
            "arn": arn
        }
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern
        if regions is not None:
            input_["regions"] = regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        arn: "capo_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.get_event_rule_request.GetEventRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.get_event_rule_response.GetEventRuleResponse"
        ]:
            import capo_notifications._operations.notifications.get_event_rule

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.get_event_rule.async_get_event_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.get_event_rule_request.GetEventRuleRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: "capo_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.delete_event_rule_request.DeleteEventRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.delete_event_rule_response.DeleteEventRuleResponse"
        ]:
            import capo_notifications._operations.notifications.delete_event_rule

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.delete_event_rule.async_delete_event_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.delete_event_rule_request.DeleteEventRuleRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.list_event_rules_request.ListEventRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.list_event_rules_response.ListEventRulesResponse"
        ]:
            import capo_notifications._operations.notifications.list_event_rules

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.list_event_rules.async_list_event_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.list_event_rules_request.ListEventRulesRequest = {
            "notification_configuration_arn": notification_configuration_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
