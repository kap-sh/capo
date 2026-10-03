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
    import capo_notifications.types.aggregation_duration
    import capo_notifications.types.channel_arn
    import capo_notifications.types.create_notification_configuration_request
    import capo_notifications.types.create_notification_configuration_response
    import capo_notifications.types.delete_notification_configuration_request
    import capo_notifications.types.delete_notification_configuration_response
    import capo_notifications.types.get_notification_configuration_request
    import capo_notifications.types.get_notification_configuration_response
    import capo_notifications.types.list_notification_configurations_request
    import capo_notifications.types.list_notification_configurations_response
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.notification_configuration_description
    import capo_notifications.types.notification_configuration_name
    import capo_notifications.types.notification_configuration_status
    import capo_notifications.types.notification_configuration_structure
    import capo_notifications.types.notification_configuration_subtype
    import capo_notifications.types.source
    import capo_notifications.types.tag_map
    import capo_notifications.types.update_notification_configuration_request
    import capo_notifications.types.update_notification_configuration_response
    from capo_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from capo_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class NotificationConfiguration:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def create(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def put(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncNotificationConfiguration:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_notifications.types.notification_configuration_name.NotificationConfigurationName",
        description: "capo_notifications.types.notification_configuration_description.NotificationConfigurationDescription",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.create_notification_configuration_request.CreateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.create_notification_configuration_response.CreateNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.create_notification_configuration

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.create_notification_configuration.async_create_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.create_notification_configuration_request.CreateNotificationConfigurationRequest = {
            "name": name,
            "description": description,
        }
        if aggregation_duration is not None:
            input_["aggregation_duration"] = aggregation_duration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put(
        self,
        arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.update_notification_configuration_response.UpdateNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.update_notification_configuration

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.update_notification_configuration.async_update_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if aggregation_duration is not None:
            input_["aggregation_duration"] = aggregation_duration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.get_notification_configuration

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.get_notification_configuration.async_get_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {
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
        arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.delete_notification_configuration_response.DeleteNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.delete_notification_configuration

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.delete_notification_configuration.async_delete_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest = {
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
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse"
        ]:
            import capo_notifications._operations.notifications.list_notification_configurations

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.list_notification_configurations.async_list_notification_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
