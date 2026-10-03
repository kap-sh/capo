from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_securitylake._auth._signers
import capo_securitylake._auth._sigv4
from capo_securitylake._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_securitylake.types.access_type_list
    import capo_securitylake.types.aws_identity
    import capo_securitylake.types.create_subscriber_notification_request
    import capo_securitylake.types.create_subscriber_notification_response
    import capo_securitylake.types.create_subscriber_request
    import capo_securitylake.types.create_subscriber_response
    import capo_securitylake.types.delete_subscriber_notification_request
    import capo_securitylake.types.delete_subscriber_notification_response
    import capo_securitylake.types.delete_subscriber_request
    import capo_securitylake.types.delete_subscriber_response
    import capo_securitylake.types.description_string
    import capo_securitylake.types.get_subscriber_request
    import capo_securitylake.types.get_subscriber_response
    import capo_securitylake.types.list_subscribers_request
    import capo_securitylake.types.list_subscribers_response
    import capo_securitylake.types.log_source_resource_list
    import capo_securitylake.types.max_results
    import capo_securitylake.types.next_token
    import capo_securitylake.types.notification_configuration
    import capo_securitylake.types.safe_string
    import capo_securitylake.types.subscriber_resource
    import capo_securitylake.types.tag_list
    import capo_securitylake.types.update_subscriber_notification_request
    import capo_securitylake.types.update_subscriber_notification_response
    import capo_securitylake.types.update_subscriber_request
    import capo_securitylake.types.update_subscriber_response
    import capo_securitylake.types.uuid
    from capo_securitylake._services.async_security_lake import (
        AsyncSecurityLakeClient,
        AsyncSecurityLakeClientConfig,
    )
    from capo_securitylake._services.security_lake import (
        SecurityLakeClient,
        SecurityLakeClientConfig,
    )


class Subscriber:
    def __init__(self, service: SecurityLakeClient) -> None:
        self._service = service

    def create(
        self,
        subscriber_identity: "capo_securitylake.types.aws_identity.AwsIdentity",
        subscriber_name: str,
        sources: "capo_securitylake.types.log_source_resource_list.LogSourceResourceList",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        subscriber_description: Optional[
            "capo_securitylake.types.description_string.DescriptionString"
        ] = None,
        access_types: Optional[
            "capo_securitylake.types.access_type_list.AccessTypeList"
        ] = None,
        tags: Optional["capo_securitylake.types.tag_list.TagList"] = None,
    ) -> "capo_securitylake.types.create_subscriber_response.CreateSubscriberResponse":
        """<p>Creates a subscriber for accounts that are already enabled in Amazon Security Lake. You can create a subscriber with access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of your Security Lake subscriber account.</p>
            subscriber_description: <p>The description for your subscriber account in Security Lake.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. Security Lake supports log and event collection for natively supported Amazon Web Services services.</p>
            access_types: <p>The Amazon S3 or Lake Formation access type.</p>
            tags: <p>An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.create_subscriber_request.CreateSubscriberRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.create_subscriber_response.CreateSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_subscriber

            output, http_response = (
                capo_securitylake._operations.security_lake.create_subscriber.create_subscriber(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_subscriber_request.CreateSubscriberRequest = {
            "subscriber_identity": subscriber_identity,
            "subscriber_name": subscriber_name,
            "sources": sources,
        }
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        if access_types is not None:
            input_["access_types"] = access_types
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.get_subscriber_response.GetSubscriberResponse":
        """<p>Retrieves the subscription information for the specified subscription ID. You can get information about a specific subscriber.</p>

        Args:
            subscriber_id: <p>A value created by Amazon Security Lake that uniquely identifies your <code>GetSubscriber</code> API request.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.get_subscriber_request.GetSubscriberRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.get_subscriber_response.GetSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_subscriber

            output, http_response = (
                capo_securitylake._operations.security_lake.get_subscriber.get_subscriber(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.get_subscriber_request.GetSubscriberRequest = {
            "subscriber_id": subscriber_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        subscriber_identity: Optional[
            "capo_securitylake.types.aws_identity.AwsIdentity"
        ] = None,
        subscriber_name: Optional[
            "capo_securitylake.types.safe_string.SafeString"
        ] = None,
        subscriber_description: Optional[
            "capo_securitylake.types.description_string.DescriptionString"
        ] = None,
        sources: Optional[
            "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
        ] = None,
    ) -> "capo_securitylake.types.update_subscriber_response.UpdateSubscriberResponse":
        """<p>Updates an existing subscription for the given Amazon Security Lake account ID. You can update a subscriber by changing the sources that the subscriber consumes data from.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your subscription.</p>
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of the Security Lake account subscriber.</p>
            subscriber_description: <p>The description of the Security Lake account subscriber.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. For the list of supported Amazon Web Services services, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Amazon Security Lake User Guide</a>.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.update_subscriber_request.UpdateSubscriberRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.update_subscriber_response.UpdateSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_subscriber

            output, http_response = (
                capo_securitylake._operations.security_lake.update_subscriber.update_subscriber(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.update_subscriber_request.UpdateSubscriberRequest = {
            "subscriber_id": subscriber_id
        }
        if subscriber_identity is not None:
            input_["subscriber_identity"] = subscriber_identity
        if subscriber_name is not None:
            input_["subscriber_name"] = subscriber_name
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        if sources is not None:
            input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse":
        """<p>Deletes the subscription permission and all notification settings for accounts that are already enabled in Amazon Security Lake. When you run <code>DeleteSubscriber</code>, the subscriber will no longer consume data from Security Lake and the subscriber is removed. This operation deletes the subscriber and removes access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your <code>DeleteSubscriber</code> API request.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_subscriber

            output, http_response = (
                capo_securitylake._operations.security_lake.delete_subscriber.delete_subscriber(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest = {
            "subscriber_id": subscriber_id
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
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
    ) -> "capo_securitylake.types.list_subscribers_response.ListSubscribersResponse":
        """<p>Lists all subscribers for the specific Amazon Security Lake account ID. You can retrieve a list of subscriptions associated with a specific organization or Amazon Web Services account.</p>

        Args:
            next_token: <p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>
            max_results: <p>The maximum number of accounts for which the configuration is displayed.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.list_subscribers_request.ListSubscribersRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.list_subscribers_response.ListSubscribersResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_subscribers

            output, http_response = (
                capo_securitylake._operations.security_lake.list_subscribers.list_subscribers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.list_subscribers_request.ListSubscribersRequest = {}
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

    def create_subscriber_notification(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        configuration: "capo_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse":
        """<p>Notifies the subscriber when new data is written to the data lake for the sources that the subscriber consumes in Security Lake. You can create only one subscriber notification per subscriber.</p>

        Args:
            subscriber_id: <p>The subscriber ID for the notification subscription.</p>
            configuration: <p>Specify the configuration using which you want to create the subscriber notification.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_subscriber_notification

            output, http_response = (
                capo_securitylake._operations.security_lake.create_subscriber_notification.create_subscriber_notification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest = {
            "subscriber_id": subscriber_id,
            "configuration": configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_subscriber_notification(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse":
        """<p>Deletes the specified subscription notification in Amazon Security Lake for the organization you specify.</p>

        Args:
            subscriber_id: <p>The ID of the Security Lake subscriber account.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_subscriber_notification

            output, http_response = (
                capo_securitylake._operations.security_lake.delete_subscriber_notification.delete_subscriber_notification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest = {
            "subscriber_id": subscriber_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_subscriber_notification(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        configuration: "capo_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse":
        """<p>Updates an existing notification method for the subscription (SQS or HTTPs endpoint) or switches the notification subscription endpoint for a subscriber.</p>

        Args:
            subscriber_id: <p>The subscription ID for which the subscription notification is specified.</p>
            configuration: <p>The configuration for subscriber notification.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_subscriber_notification

            output, http_response = (
                capo_securitylake._operations.security_lake.update_subscriber_notification.update_subscriber_notification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest = {
            "subscriber_id": subscriber_id,
            "configuration": configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSubscriber:
    def __init__(self, service: AsyncSecurityLakeClient) -> None:
        self._service = service

    async def create(
        self,
        subscriber_identity: "capo_securitylake.types.aws_identity.AwsIdentity",
        subscriber_name: str,
        sources: "capo_securitylake.types.log_source_resource_list.LogSourceResourceList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        subscriber_description: Optional[
            "capo_securitylake.types.description_string.DescriptionString"
        ] = None,
        access_types: Optional[
            "capo_securitylake.types.access_type_list.AccessTypeList"
        ] = None,
        tags: Optional["capo_securitylake.types.tag_list.TagList"] = None,
    ) -> "capo_securitylake.types.create_subscriber_response.CreateSubscriberResponse":
        """<p>Creates a subscriber for accounts that are already enabled in Amazon Security Lake. You can create a subscriber with access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of your Security Lake subscriber account.</p>
            subscriber_description: <p>The description for your subscriber account in Security Lake.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. Security Lake supports log and event collection for natively supported Amazon Web Services services.</p>
            access_types: <p>The Amazon S3 or Lake Formation access type.</p>
            tags: <p>An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_subscriber_request.CreateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_subscriber_response.CreateSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_subscriber

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_subscriber.async_create_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_subscriber_request.CreateSubscriberRequest = {
            "subscriber_identity": subscriber_identity,
            "subscriber_name": subscriber_name,
            "sources": sources,
        }
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        if access_types is not None:
            input_["access_types"] = access_types
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.get_subscriber_response.GetSubscriberResponse":
        """<p>Retrieves the subscription information for the specified subscription ID. You can get information about a specific subscriber.</p>

        Args:
            subscriber_id: <p>A value created by Amazon Security Lake that uniquely identifies your <code>GetSubscriber</code> API request.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.get_subscriber_request.GetSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.get_subscriber_response.GetSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_subscriber

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.get_subscriber.async_get_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.get_subscriber_request.GetSubscriberRequest = {
            "subscriber_id": subscriber_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        subscriber_identity: Optional[
            "capo_securitylake.types.aws_identity.AwsIdentity"
        ] = None,
        subscriber_name: Optional[
            "capo_securitylake.types.safe_string.SafeString"
        ] = None,
        subscriber_description: Optional[
            "capo_securitylake.types.description_string.DescriptionString"
        ] = None,
        sources: Optional[
            "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
        ] = None,
    ) -> "capo_securitylake.types.update_subscriber_response.UpdateSubscriberResponse":
        """<p>Updates an existing subscription for the given Amazon Security Lake account ID. You can update a subscriber by changing the sources that the subscriber consumes data from.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your subscription.</p>
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of the Security Lake account subscriber.</p>
            subscriber_description: <p>The description of the Security Lake account subscriber.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. For the list of supported Amazon Web Services services, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Amazon Security Lake User Guide</a>.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.update_subscriber_request.UpdateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.update_subscriber_response.UpdateSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_subscriber

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.update_subscriber.async_update_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.update_subscriber_request.UpdateSubscriberRequest = {
            "subscriber_id": subscriber_id
        }
        if subscriber_identity is not None:
            input_["subscriber_identity"] = subscriber_identity
        if subscriber_name is not None:
            input_["subscriber_name"] = subscriber_name
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        if sources is not None:
            input_["sources"] = sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse":
        """<p>Deletes the subscription permission and all notification settings for accounts that are already enabled in Amazon Security Lake. When you run <code>DeleteSubscriber</code>, the subscriber will no longer consume data from Security Lake and the subscriber is removed. This operation deletes the subscriber and removes access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your <code>DeleteSubscriber</code> API request.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_subscriber

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_subscriber.async_delete_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest = {
            "subscriber_id": subscriber_id
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
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
    ) -> "capo_securitylake.types.list_subscribers_response.ListSubscribersResponse":
        """<p>Lists all subscribers for the specific Amazon Security Lake account ID. You can retrieve a list of subscriptions associated with a specific organization or Amazon Web Services account.</p>

        Args:
            next_token: <p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>
            max_results: <p>The maximum number of accounts for which the configuration is displayed.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.list_subscribers_request.ListSubscribersRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.list_subscribers_response.ListSubscribersResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_subscribers

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.list_subscribers.async_list_subscribers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.list_subscribers_request.ListSubscribersRequest = {}
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

    async def create_subscriber_notification(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        configuration: "capo_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse":
        """<p>Notifies the subscriber when new data is written to the data lake for the sources that the subscriber consumes in Security Lake. You can create only one subscriber notification per subscriber.</p>

        Args:
            subscriber_id: <p>The subscriber ID for the notification subscription.</p>
            configuration: <p>Specify the configuration using which you want to create the subscriber notification.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_subscriber_notification

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_subscriber_notification.async_create_subscriber_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest = {
            "subscriber_id": subscriber_id,
            "configuration": configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_subscriber_notification(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse":
        """<p>Deletes the specified subscription notification in Amazon Security Lake for the organization you specify.</p>

        Args:
            subscriber_id: <p>The ID of the Security Lake subscriber account.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_subscriber_notification

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_subscriber_notification.async_delete_subscriber_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest = {
            "subscriber_id": subscriber_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_subscriber_notification(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        configuration: "capo_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse":
        """<p>Updates an existing notification method for the subscription (SQS or HTTPs endpoint) or switches the notification subscription endpoint for a subscriber.</p>

        Args:
            subscriber_id: <p>The subscription ID for which the subscription notification is specified.</p>
            configuration: <p>The configuration for subscriber notification.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_subscriber_notification

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.update_subscriber_notification.async_update_subscriber_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest = {
            "subscriber_id": subscriber_id,
            "configuration": configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
