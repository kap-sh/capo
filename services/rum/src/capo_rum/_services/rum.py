"""Generated from Smithy shape ``com.amazonaws.rum#RUM``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_rum._auth._signers
import capo_rum._auth._sigv4
from capo_rum._auth._identity import Credentials
from capo_rum._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_rum._auth._zapros_handler import AuthMiddleware
from capo_rum._pagination import resolve_path as _resolve_path
from capo_rum._resources.rum.app_monitor_resource import AppMonitorResource
from capo_rum._services._aws_config import aws_config
from capo_rum._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_rum.types.alias
    import capo_rum.types.app_monitor_configuration
    import capo_rum.types.app_monitor_details
    import capo_rum.types.app_monitor_domain
    import capo_rum.types.app_monitor_domain_list
    import capo_rum.types.app_monitor_id
    import capo_rum.types.app_monitor_name
    import capo_rum.types.app_monitor_platform
    import capo_rum.types.app_monitor_summary
    import capo_rum.types.arn
    import capo_rum.types.batch_create_rum_metric_definitions_request
    import capo_rum.types.batch_create_rum_metric_definitions_response
    import capo_rum.types.batch_delete_rum_metric_definitions_request
    import capo_rum.types.batch_delete_rum_metric_definitions_response
    import capo_rum.types.batch_get_rum_metric_definitions_request
    import capo_rum.types.batch_get_rum_metric_definitions_response
    import capo_rum.types.create_app_monitor_request
    import capo_rum.types.create_app_monitor_response
    import capo_rum.types.custom_events
    import capo_rum.types.delete_app_monitor_request
    import capo_rum.types.delete_app_monitor_response
    import capo_rum.types.delete_resource_policy_request
    import capo_rum.types.delete_resource_policy_response
    import capo_rum.types.delete_rum_metrics_destination_request
    import capo_rum.types.delete_rum_metrics_destination_response
    import capo_rum.types.deobfuscation_configuration
    import capo_rum.types.destination_arn
    import capo_rum.types.event_data
    import capo_rum.types.get_app_monitor_data_request
    import capo_rum.types.get_app_monitor_data_response
    import capo_rum.types.get_app_monitor_request
    import capo_rum.types.get_app_monitor_response
    import capo_rum.types.get_resource_policy_request
    import capo_rum.types.get_resource_policy_response
    import capo_rum.types.iam_role_arn
    import capo_rum.types.list_app_monitors_request
    import capo_rum.types.list_app_monitors_response
    import capo_rum.types.list_rum_metrics_destinations_request
    import capo_rum.types.list_rum_metrics_destinations_response
    import capo_rum.types.list_tags_for_resource_request
    import capo_rum.types.list_tags_for_resource_response
    import capo_rum.types.max_query_results
    import capo_rum.types.max_results_integer
    import capo_rum.types.metric_definition
    import capo_rum.types.metric_definition_id
    import capo_rum.types.metric_definition_ids
    import capo_rum.types.metric_definition_request
    import capo_rum.types.metric_definitions_request
    import capo_rum.types.metric_destination
    import capo_rum.types.metric_destination_summary
    import capo_rum.types.policy_revision_id
    import capo_rum.types.put_resource_policy_request
    import capo_rum.types.put_resource_policy_response
    import capo_rum.types.put_rum_events_request
    import capo_rum.types.put_rum_events_response
    import capo_rum.types.put_rum_metrics_destination_request
    import capo_rum.types.put_rum_metrics_destination_response
    import capo_rum.types.query_filters
    import capo_rum.types.rum_event_list
    import capo_rum.types.tag_key_list
    import capo_rum.types.tag_map
    import capo_rum.types.tag_resource_request
    import capo_rum.types.tag_resource_response
    import capo_rum.types.time_range
    import capo_rum.types.token
    import capo_rum.types.untag_resource_request
    import capo_rum.types.untag_resource_response
    import capo_rum.types.update_app_monitor_request
    import capo_rum.types.update_app_monitor_response
    import capo_rum.types.update_rum_metric_definition_request
    import capo_rum.types.update_rum_metric_definition_response
    import capo_rum.types.user_details


class RUMClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class RUMClient:
    """A client for the ``RUM`` service.

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
        self._config = RUMClientConfig(
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
        self.app_monitor_resource = AppMonitorResource(self)

    def operation_options(
        self, config_overrides: Optional[RUMClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: RUMClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_rum.types.arn.Arn",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
    ) -> "capo_rum.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Displays the tags associated with a CloudWatch RUM resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you want to see the tags of.</p>

        Raises:
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_rum.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_rum._operations.rum.list_tags_for_resource

            output, http_response = (
                capo_rum._operations.rum.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_rum_events(
        self,
        id: "capo_rum.types.app_monitor_id.AppMonitorId",
        batch_id: str,
        app_monitor_details: "capo_rum.types.app_monitor_details.AppMonitorDetails",
        user_details: "capo_rum.types.user_details.UserDetails",
        rum_events: "capo_rum.types.rum_event_list.RumEventList",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        alias: Optional["capo_rum.types.alias.Alias"] = None,
    ) -> "capo_rum.types.put_rum_events_response.PutRumEventsResponse":
        """<p>Sends telemetry events about your application performance and user behavior to CloudWatch RUM. The code snippet that RUM generates for you to add to your application includes <code>PutRumEvents</code> operations to send this data to RUM.</p> <p>Each <code>PutRumEvents</code> operation can send a batch of events from one user session.</p>

        Args:
            id: <p>The ID of the app monitor that is sending this data.</p>
            batch_id: <p>A unique identifier for this batch of RUM event data.</p>
            app_monitor_details: <p>A structure that contains information about the app monitor that collected this telemetry information.</p>
            user_details: <p>A structure that contains information about the user session that this batch of events was collected from.</p>
            rum_events: <p>An array of structures that contain the telemetry event data.</p>
            alias: <p>If the app monitor uses a resource-based policy that requires <code>PutRumEvents</code> requests to specify a certain alias, specify that alias here. This alias will be compared to the <code>rum:alias</code> context key in the resource-based policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html">Using resource-based policies with CloudWatch RUM</a>.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.put_rum_events_request.PutRumEventsRequest]",
        ) -> OperationResponse[
            "capo_rum.types.put_rum_events_response.PutRumEventsResponse"
        ]:
            import capo_rum._operations.rum.put_rum_events

            output, http_response = (
                capo_rum._operations.rum.put_rum_events.put_rum_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.put_rum_events_request.PutRumEventsRequest = {
            "id": id,
            "batch_id": batch_id,
            "app_monitor_details": app_monitor_details,
            "user_details": user_details,
            "rum_events": rum_events,
        }
        if alias is not None:
            input_["alias"] = alias

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_rum.types.arn.Arn",
        tags: "capo_rum.types.tag_map.TagMap",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
    ) -> "capo_rum.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified CloudWatch RUM resource. Currently, the only resources that can be tagged app monitors.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a resource.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch RUM resource that you're adding tags to.</p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>

        Raises:
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_rum.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_rum._operations.rum.tag_resource

            output, http_response = capo_rum._operations.rum.tag_resource.tag_resource(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
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
        resource_arn: "capo_rum.types.arn.Arn",
        tag_keys: "capo_rum.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
    ) -> "capo_rum.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch RUM resource that you're removing tags from.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_rum.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_rum._operations.rum.untag_resource

            output, http_response = (
                capo_rum._operations.rum.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_app_monitor(
        self,
        name: "capo_rum.types.app_monitor_name.AppMonitorName",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
    ) -> "capo_rum.types.get_app_monitor_response.GetAppMonitorResponse":
        """<p>Retrieves the complete configuration information for one app monitor.</p>

        Args:
            name: <p>The app monitor to retrieve information for.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.get_app_monitor_request.GetAppMonitorRequest]",
        ) -> OperationResponse[
            "capo_rum.types.get_app_monitor_response.GetAppMonitorResponse"
        ]:
            import capo_rum._operations.rum.get_app_monitor

            output, http_response = (
                capo_rum._operations.rum.get_app_monitor.get_app_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.get_app_monitor_request.GetAppMonitorRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_app_monitor(
        self,
        name: "capo_rum.types.app_monitor_name.AppMonitorName",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        domain: Optional["capo_rum.types.app_monitor_domain.AppMonitorDomain"] = None,
        domain_list: Optional[
            "capo_rum.types.app_monitor_domain_list.AppMonitorDomainList"
        ] = None,
        app_monitor_configuration: Optional[
            "capo_rum.types.app_monitor_configuration.AppMonitorConfiguration"
        ] = None,
        cw_log_enabled: Optional[bool] = None,
        custom_events: Optional["capo_rum.types.custom_events.CustomEvents"] = None,
        deobfuscation_configuration: Optional[
            "capo_rum.types.deobfuscation_configuration.DeobfuscationConfiguration"
        ] = None,
    ) -> "capo_rum.types.update_app_monitor_response.UpdateAppMonitorResponse":
        """<p>Updates the configuration of an existing app monitor. When you use this operation, only the parts of the app monitor configuration that you specify in this operation are changed. For any parameters that you omit, the existing values are kept.</p> <p>You can't use this operation to change the tags of an existing app monitor. To change the tags of an existing app monitor, use <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TagResource.html">TagResource</a>.</p> <p>To create a new app monitor, use <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html">CreateAppMonitor</a>.</p> <p>After you update an app monitor, sign in to the CloudWatch RUM console to get the updated JavaScript code snippet to add to your web application. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html">How do I find a code snippet that I've already generated?</a> </p>

        Args:
            name: <p>The name of the app monitor to update.</p>
            domain: <p>The top-level internet domain name for which your application has administrative authority.</p>
            domain_list: <p> List the domain names for which your application has administrative authority. The <code>UpdateAppMonitor</code> allows either the domain or the domain list. </p>
            app_monitor_configuration: <p>A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include <code>AppMonitorConfiguration</code>, you must set up your own authorization method. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html">Authorize your application to send data to Amazon Web Services</a>.</p>
            cw_log_enabled: <p>Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.</p>
            custom_events: <p>Specifies whether this app monitor allows the web client to define and send custom events. The default is for custom events to be <code>DISABLED</code>.</p> <p>For more information about custom events, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html">Send custom events</a>.</p>
            deobfuscation_configuration: <p> A structure that contains the configuration for how an app monitor can deobfuscate stack traces. </p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.update_app_monitor_request.UpdateAppMonitorRequest]",
        ) -> OperationResponse[
            "capo_rum.types.update_app_monitor_response.UpdateAppMonitorResponse"
        ]:
            import capo_rum._operations.rum.update_app_monitor

            output, http_response = (
                capo_rum._operations.rum.update_app_monitor.update_app_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.update_app_monitor_request.UpdateAppMonitorRequest = {
            "name": name
        }
        if domain is not None:
            input_["domain"] = domain
        if domain_list is not None:
            input_["domain_list"] = domain_list
        if app_monitor_configuration is not None:
            input_["app_monitor_configuration"] = app_monitor_configuration
        if cw_log_enabled is not None:
            input_["cw_log_enabled"] = cw_log_enabled
        if custom_events is not None:
            input_["custom_events"] = custom_events
        if deobfuscation_configuration is not None:
            input_["deobfuscation_configuration"] = deobfuscation_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_app_monitor(
        self,
        name: "capo_rum.types.app_monitor_name.AppMonitorName",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
    ) -> "capo_rum.types.delete_app_monitor_response.DeleteAppMonitorResponse":
        """<p>Deletes an existing app monitor. This immediately stops the collection of data.</p>

        Args:
            name: <p>The name of the app monitor to delete.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.delete_app_monitor_request.DeleteAppMonitorRequest]",
        ) -> OperationResponse[
            "capo_rum.types.delete_app_monitor_response.DeleteAppMonitorResponse"
        ]:
            import capo_rum._operations.rum.delete_app_monitor

            output, http_response = (
                capo_rum._operations.rum.delete_app_monitor.delete_app_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.delete_app_monitor_request.DeleteAppMonitorRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_app_monitors(
        self,
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        max_results: Optional[
            "capo_rum.types.max_results_integer.MaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_rum.types.list_app_monitors_response.ListAppMonitorsResponse":
        """<p>Returns a list of the Amazon CloudWatch RUM app monitors in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.</p>
            next_token: <p>Use the token returned by the previous operation to request the next page of results.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.list_app_monitors_request.ListAppMonitorsRequest]",
        ) -> OperationResponse[
            "capo_rum.types.list_app_monitors_response.ListAppMonitorsResponse"
        ]:
            import capo_rum._operations.rum.list_app_monitors

            output, http_response = (
                capo_rum._operations.rum.list_app_monitors.list_app_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.list_app_monitors_request.ListAppMonitorsRequest = {}
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

    def iter_list_app_monitors(
        self,
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        max_results: Optional[
            "capo_rum.types.max_results_integer.MaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_rum.types.app_monitor_summary.AppMonitorSummary]":
        _token = next_token
        while True:
            _response = self.list_app_monitors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("app_monitor_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def batch_create_rum_metric_definitions(
        self,
        app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName",
        destination: "capo_rum.types.metric_destination.MetricDestination",
        metric_definitions: "capo_rum.types.metric_definitions_request.MetricDefinitionsRequest",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        destination_arn: Optional[
            "capo_rum.types.destination_arn.DestinationArn"
        ] = None,
    ) -> "capo_rum.types.batch_create_rum_metric_definitions_response.BatchCreateRumMetricDefinitionsResponse":
        """<p>Specifies the extended metrics and custom metrics that you want a CloudWatch RUM app monitor to send to a destination. Valid destinations include CloudWatch and Evidently.</p> <p>By default, RUM app monitors send some metrics to CloudWatch. These default metrics are listed in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-metrics.html">CloudWatch metrics that you can collect with CloudWatch RUM</a>.</p> <p>In addition to these default metrics, you can choose to send extended metrics, custom metrics, or both.</p> <ul> <li> <p>Extended metrics let you send metrics with additional dimensions that aren't included in the default metrics. You can also send extended metrics to both Evidently and CloudWatch. The valid dimension names for the additional dimensions for extended metrics are <code>BrowserName</code>, <code>CountryCode</code>, <code>DeviceType</code>, <code>FileType</code>, <code>OSName</code>, and <code>PageId</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-vended-metrics.html"> Extended metrics that you can send to CloudWatch and CloudWatch Evidently</a>.</p> </li> <li> <p>Custom metrics are metrics that you define. You can send custom metrics to CloudWatch. CloudWatch Evidently, or both. With custom metrics, you can use any metric name and namespace. To derive the metrics, you can use any custom events, built-in events, custom attributes, or default attributes. </p> <p>You can't send custom metrics to the <code>AWS/RUM</code> namespace. You must send custom metrics to a custom namespace that you define. The namespace that you use can't start with <code>AWS/</code>. CloudWatch RUM prepends <code>RUM/CustomMetrics/</code> to the custom namespace that you define, so the final namespace for your metrics in CloudWatch is <code>RUM/CustomMetrics/<i>your-custom-namespace</i> </code>.</p> </li> </ul> <p>The maximum number of metric definitions that you can specify in one <code>BatchCreateRumMetricDefinitions</code> operation is 200.</p> <p>The maximum number of metric definitions that one destination can contain is 2000.</p> <p>Extended metrics sent to CloudWatch and RUM custom metrics are charged as CloudWatch custom metrics. Each combination of additional dimension name and dimension value counts as a custom metric. For more information, see <a href="https://aws.amazon.com/cloudwatch/pricing/">Amazon CloudWatch Pricing</a>.</p> <p>You must have already created a destination for the metrics before you send them. For more information, see <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html">PutRumMetricsDestination</a>.</p> <p>If some metric definitions specified in a <code>BatchCreateRumMetricDefinitions</code> operations are not valid, those metric definitions fail and return errors, but all valid metric definitions in the same operation still succeed.</p>

        Args:
            app_monitor_name: <p>The name of the CloudWatch RUM app monitor that is to send the metrics.</p>
            destination: <p>The destination to send the metrics to. Valid values are <code>CloudWatch</code> and <code>Evidently</code>. If you specify <code>Evidently</code>, you must also specify the Amazon Resource Name (ARN) of the CloudWatchEvidently experiment that will receive the metrics and an IAM role that has permission to write to the experiment.</p>
            destination_arn: <p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter.</p> <p>This parameter specifies the ARN of the Evidently experiment that is to receive the metrics. You must have already defined this experiment as a valid destination. For more information, see <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html">PutRumMetricsDestination</a>.</p>
            metric_definitions: <p>An array of structures which define the metrics that you want to send.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.batch_create_rum_metric_definitions_request.BatchCreateRumMetricDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_rum.types.batch_create_rum_metric_definitions_response.BatchCreateRumMetricDefinitionsResponse"
        ]:
            import capo_rum._operations.rum.batch_create_rum_metric_definitions

            output, http_response = (
                capo_rum._operations.rum.batch_create_rum_metric_definitions.batch_create_rum_metric_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.batch_create_rum_metric_definitions_request.BatchCreateRumMetricDefinitionsRequest = {
            "app_monitor_name": app_monitor_name,
            "destination": destination,
            "metric_definitions": metric_definitions,
        }
        if destination_arn is not None:
            input_["destination_arn"] = destination_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_rum_metric_definitions(
        self,
        app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName",
        destination: "capo_rum.types.metric_destination.MetricDestination",
        metric_definition_ids: "capo_rum.types.metric_definition_ids.MetricDefinitionIds",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        destination_arn: Optional[
            "capo_rum.types.destination_arn.DestinationArn"
        ] = None,
    ) -> "capo_rum.types.batch_delete_rum_metric_definitions_response.BatchDeleteRumMetricDefinitionsResponse":
        """<p>Removes the specified metrics from being sent to an extended metrics destination.</p> <p>If some metric definition IDs specified in a <code>BatchDeleteRumMetricDefinitions</code> operations are not valid, those metric definitions fail and return errors, but all valid metric definition IDs in the same operation are still deleted.</p> <p>The maximum number of metric definitions that you can specify in one <code>BatchDeleteRumMetricDefinitions</code> operation is 200.</p>

        Args:
            app_monitor_name: <p>The name of the CloudWatch RUM app monitor that is sending these metrics.</p>
            destination: <p>Defines the destination where you want to stop sending the specified metrics. Valid values are <code>CloudWatch</code> and <code>Evidently</code>. If you specify <code>Evidently</code>, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.</p>
            destination_arn: <p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter. </p> <p>This parameter specifies the ARN of the Evidently experiment that was receiving the metrics that are being deleted.</p>
            metric_definition_ids: <p>An array of structures which define the metrics that you want to stop sending.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.batch_delete_rum_metric_definitions_request.BatchDeleteRumMetricDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_rum.types.batch_delete_rum_metric_definitions_response.BatchDeleteRumMetricDefinitionsResponse"
        ]:
            import capo_rum._operations.rum.batch_delete_rum_metric_definitions

            output, http_response = (
                capo_rum._operations.rum.batch_delete_rum_metric_definitions.batch_delete_rum_metric_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.batch_delete_rum_metric_definitions_request.BatchDeleteRumMetricDefinitionsRequest = {
            "app_monitor_name": app_monitor_name,
            "destination": destination,
            "metric_definition_ids": metric_definition_ids,
        }
        if destination_arn is not None:
            input_["destination_arn"] = destination_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_rum_metric_definitions(
        self,
        app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName",
        destination: "capo_rum.types.metric_destination.MetricDestination",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        destination_arn: Optional[
            "capo_rum.types.destination_arn.DestinationArn"
        ] = None,
        max_results: Optional[
            "capo_rum.types.max_results_integer.MaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_rum.types.batch_get_rum_metric_definitions_response.BatchGetRumMetricDefinitionsResponse":
        """<p>Retrieves the list of metrics and dimensions that a RUM app monitor is sending to a single destination.</p>

        Args:
            app_monitor_name: <p>The name of the CloudWatch RUM app monitor that is sending the metrics.</p>
            destination: <p>The type of destination that you want to view metrics for. Valid values are <code>CloudWatch</code> and <code>Evidently</code>.</p>
            destination_arn: <p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter.</p> <p>This parameter specifies the ARN of the Evidently experiment that corresponds to the destination.</p>
            max_results: <p>The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.</p> <p>To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. </p>
            next_token: <p>Use the token returned by the previous operation to request the next page of results.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.batch_get_rum_metric_definitions_request.BatchGetRumMetricDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_rum.types.batch_get_rum_metric_definitions_response.BatchGetRumMetricDefinitionsResponse"
        ]:
            import capo_rum._operations.rum.batch_get_rum_metric_definitions

            output, http_response = (
                capo_rum._operations.rum.batch_get_rum_metric_definitions.batch_get_rum_metric_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.batch_get_rum_metric_definitions_request.BatchGetRumMetricDefinitionsRequest = {
            "app_monitor_name": app_monitor_name,
            "destination": destination,
        }
        if destination_arn is not None:
            input_["destination_arn"] = destination_arn
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

    def iter_batch_get_rum_metric_definitions(
        self,
        app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName",
        destination: "capo_rum.types.metric_destination.MetricDestination",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        destination_arn: Optional[
            "capo_rum.types.destination_arn.DestinationArn"
        ] = None,
        max_results: Optional[
            "capo_rum.types.max_results_integer.MaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_rum.types.metric_definition.MetricDefinition]":
        _token = next_token
        while True:
            _response = self.batch_get_rum_metric_definitions(
                app_monitor_name,
                destination,
                config_overrides=config_overrides,
                destination_arn=destination_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("metric_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_app_monitor(
        self,
        name: "capo_rum.types.app_monitor_name.AppMonitorName",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        domain: Optional["capo_rum.types.app_monitor_domain.AppMonitorDomain"] = None,
        domain_list: Optional[
            "capo_rum.types.app_monitor_domain_list.AppMonitorDomainList"
        ] = None,
        tags: Optional["capo_rum.types.tag_map.TagMap"] = None,
        app_monitor_configuration: Optional[
            "capo_rum.types.app_monitor_configuration.AppMonitorConfiguration"
        ] = None,
        cw_log_enabled: Optional[bool] = None,
        custom_events: Optional["capo_rum.types.custom_events.CustomEvents"] = None,
        deobfuscation_configuration: Optional[
            "capo_rum.types.deobfuscation_configuration.DeobfuscationConfiguration"
        ] = None,
        platform: Optional[
            "capo_rum.types.app_monitor_platform.AppMonitorPlatform"
        ] = None,
    ) -> "capo_rum.types.create_app_monitor_response.CreateAppMonitorResponse":
        """<p>Creates a Amazon CloudWatch RUM app monitor, which collects telemetry data from your application and sends that data to RUM. The data includes performance and reliability information such as page load time, client-side errors, and user behavior.</p> <p>You use this operation only to create a new app monitor. To update an existing app monitor, use <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.html">UpdateAppMonitor</a> instead.</p> <p>After you create an app monitor, sign in to the CloudWatch RUM console to get the JavaScript code snippet to add to your web application. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html">How do I find a code snippet that I've already generated?</a> </p>

        Args:
            name: <p>A name for the app monitor.</p>
            domain: <p>The top-level internet domain name for which your application has administrative authority.</p>
            domain_list: <p> List the domain names for which your application has administrative authority. The <code>CreateAppMonitor</code> requires either the domain or the domain list. </p>
            tags: <p>Assigns one or more tags (key-value pairs) to the app monitor.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can associate as many as 50 tags with an app monitor.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>.</p>
            app_monitor_configuration: <p>A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include <code>AppMonitorConfiguration</code>, you must set up your own authorization method. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html">Authorize your application to send data to Amazon Web Services</a>.</p> <p>If you omit this argument, the sample rate used for RUM is set to 10% of the user sessions.</p>
            cw_log_enabled: <p>Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.</p> <p>If you omit this parameter, the default is <code>false</code>.</p>
            custom_events: <p>Specifies whether this app monitor allows the web client to define and send custom events. If you omit this parameter, custom events are <code>DISABLED</code>.</p> <p>For more information about custom events, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html">Send custom events</a>.</p>
            deobfuscation_configuration: <p> A structure that contains the configuration for how an app monitor can deobfuscate stack traces. </p>
            platform: <p>The platform type for the app monitor. Valid values are <code>Web</code> for web applications, <code>Android</code> for Android applications, and <code>iOS</code> for IOS applications. If you omit this parameter, the default is <code>Web</code>.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.create_app_monitor_request.CreateAppMonitorRequest]",
        ) -> OperationResponse[
            "capo_rum.types.create_app_monitor_response.CreateAppMonitorResponse"
        ]:
            import capo_rum._operations.rum.create_app_monitor

            output, http_response = (
                capo_rum._operations.rum.create_app_monitor.create_app_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.create_app_monitor_request.CreateAppMonitorRequest = {
            "name": name
        }
        if domain is not None:
            input_["domain"] = domain
        if domain_list is not None:
            input_["domain_list"] = domain_list
        if tags is not None:
            input_["tags"] = tags
        if app_monitor_configuration is not None:
            input_["app_monitor_configuration"] = app_monitor_configuration
        if cw_log_enabled is not None:
            input_["cw_log_enabled"] = cw_log_enabled
        if custom_events is not None:
            input_["custom_events"] = custom_events
        if deobfuscation_configuration is not None:
            input_["deobfuscation_configuration"] = deobfuscation_configuration
        if platform is not None:
            input_["platform"] = platform

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        name: "capo_rum.types.app_monitor_name.AppMonitorName",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        policy_revision_id: Optional[
            "capo_rum.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_rum.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Removes the association of a resource-based policy from an app monitor.</p>

        Args:
            name: <p>The app monitor that you want to remove the resource policy from.</p>
            policy_revision_id: <p>Specifies a specific policy revision to delete. Provide a <code>PolicyRevisionId</code> to ensure an atomic delete operation. If the revision ID that you provide doesn't match the latest policy revision ID, the request will be rejected with an <code>InvalidPolicyRevisionIdException</code> error.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.invalid_policy_revision_id_exception.InvalidPolicyRevisionIdException: <p>The policy revision ID that you provided doeesn't match the latest policy revision ID.</p>
            capo_rum.errors.policy_not_found_exception.PolicyNotFoundException: <p>The resource-based policy doesn't exist on this app monitor.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_rum.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_rum._operations.rum.delete_resource_policy

            output, http_response = (
                capo_rum._operations.rum.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "name": name
        }
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_rum_metrics_destination(
        self,
        app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName",
        destination: "capo_rum.types.metric_destination.MetricDestination",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        destination_arn: Optional[
            "capo_rum.types.destination_arn.DestinationArn"
        ] = None,
    ) -> "capo_rum.types.delete_rum_metrics_destination_response.DeleteRumMetricsDestinationResponse":
        """<p>Deletes a destination for CloudWatch RUM extended metrics, so that the specified app monitor stops sending extended metrics to that destination.</p>

        Args:
            app_monitor_name: <p>The name of the app monitor that is sending metrics to the destination that you want to delete.</p>
            destination: <p>The type of destination to delete. Valid values are <code>CloudWatch</code> and <code>Evidently</code>.</p>
            destination_arn: <p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter. This parameter specifies the ARN of the Evidently experiment that corresponds to the destination to delete.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.delete_rum_metrics_destination_request.DeleteRumMetricsDestinationRequest]",
        ) -> OperationResponse[
            "capo_rum.types.delete_rum_metrics_destination_response.DeleteRumMetricsDestinationResponse"
        ]:
            import capo_rum._operations.rum.delete_rum_metrics_destination

            output, http_response = (
                capo_rum._operations.rum.delete_rum_metrics_destination.delete_rum_metrics_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.delete_rum_metrics_destination_request.DeleteRumMetricsDestinationRequest = {
            "app_monitor_name": app_monitor_name,
            "destination": destination,
        }
        if destination_arn is not None:
            input_["destination_arn"] = destination_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_app_monitor_data(
        self,
        name: "capo_rum.types.app_monitor_name.AppMonitorName",
        time_range: "capo_rum.types.time_range.TimeRange",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        filters: Optional["capo_rum.types.query_filters.QueryFilters"] = None,
        max_results: Optional[
            "capo_rum.types.max_query_results.MaxQueryResults"
        ] = None,
        next_token: Optional["capo_rum.types.token.Token"] = None,
    ) -> "capo_rum.types.get_app_monitor_data_response.GetAppMonitorDataResponse":
        """<p>Retrieves the raw performance events that RUM has collected from your web application, so that you can do your own processing or analysis of this data.</p>

        Args:
            name: <p>The name of the app monitor that collected the data that you want to retrieve.</p>
            time_range: <p>A structure that defines the time range that you want to retrieve results from.</p>
            filters: <p>An array of structures that you can use to filter the results to those that match one or more sets of key-value pairs that you specify.</p>
            max_results: <p>The maximum number of results to return in one operation. </p>
            next_token: <p>Use the token returned by the previous operation to request the next page of results.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.get_app_monitor_data_request.GetAppMonitorDataRequest]",
        ) -> OperationResponse[
            "capo_rum.types.get_app_monitor_data_response.GetAppMonitorDataResponse"
        ]:
            import capo_rum._operations.rum.get_app_monitor_data

            output, http_response = (
                capo_rum._operations.rum.get_app_monitor_data.get_app_monitor_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.get_app_monitor_data_request.GetAppMonitorDataRequest = {
            "name": name,
            "time_range": time_range,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_get_app_monitor_data(
        self,
        name: "capo_rum.types.app_monitor_name.AppMonitorName",
        time_range: "capo_rum.types.time_range.TimeRange",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        filters: Optional["capo_rum.types.query_filters.QueryFilters"] = None,
        max_results: Optional[
            "capo_rum.types.max_query_results.MaxQueryResults"
        ] = None,
        next_token: Optional["capo_rum.types.token.Token"] = None,
    ) -> "Iterator[capo_rum.types.event_data.EventData]":
        _token = next_token
        while True:
            _response = self.get_app_monitor_data(
                name,
                time_range,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_resource_policy(
        self,
        name: "capo_rum.types.app_monitor_name.AppMonitorName",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
    ) -> "capo_rum.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Use this operation to retrieve information about a resource-based policy that is attached to an app monitor.</p>

        Args:
            name: <p>The name of the app monitor that is associated with the resource-based policy that you want to view.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.policy_not_found_exception.PolicyNotFoundException: <p>The resource-based policy doesn't exist on this app monitor.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_rum.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_rum._operations.rum.get_resource_policy

            output, http_response = (
                capo_rum._operations.rum.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_rum_metrics_destinations(
        self,
        app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        max_results: Optional[
            "capo_rum.types.max_results_integer.MaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_rum.types.list_rum_metrics_destinations_response.ListRumMetricsDestinationsResponse":
        """<p>Returns a list of destinations that you have created to receive RUM extended metrics, for the specified app monitor.</p> <p>For more information about extended metrics, see <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AddRumMetrcs.html">AddRumMetrics</a>.</p>

        Args:
            app_monitor_name: <p>The name of the app monitor associated with the destinations that you want to retrieve.</p>
            max_results: <p>The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.</p> <p>To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. </p>
            next_token: <p>Use the token returned by the previous operation to request the next page of results.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.list_rum_metrics_destinations_request.ListRumMetricsDestinationsRequest]",
        ) -> OperationResponse[
            "capo_rum.types.list_rum_metrics_destinations_response.ListRumMetricsDestinationsResponse"
        ]:
            import capo_rum._operations.rum.list_rum_metrics_destinations

            output, http_response = (
                capo_rum._operations.rum.list_rum_metrics_destinations.list_rum_metrics_destinations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.list_rum_metrics_destinations_request.ListRumMetricsDestinationsRequest = {
            "app_monitor_name": app_monitor_name
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

    def iter_list_rum_metrics_destinations(
        self,
        app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        max_results: Optional[
            "capo_rum.types.max_results_integer.MaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_rum.types.metric_destination_summary.MetricDestinationSummary]":
        _token = next_token
        while True:
            _response = self.list_rum_metrics_destinations(
                app_monitor_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("destinations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_resource_policy(
        self,
        name: "capo_rum.types.app_monitor_name.AppMonitorName",
        policy_document: str,
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        policy_revision_id: Optional[
            "capo_rum.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_rum.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Use this operation to assign a resource-based policy to a CloudWatch RUM app monitor to control access to it. Each app monitor can have one resource-based policy. The maximum size of the policy is 4 KB. To learn more about using resource policies with RUM, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html">Using resource-based policies with CloudWatch RUM</a>.</p>

        Args:
            name: <p>The name of the app monitor that you want to apply this resource-based policy to. To find the names of your app monitors, you can use the <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListAppMonitors.html">ListAppMonitors</a> operation.</p>
            policy_document: <p>The JSON to use as the resource policy. The document can be up to 4 KB in size. For more information about the contents and syntax for this policy, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html">Using resource-based policies with CloudWatch RUM</a>.</p>
            policy_revision_id: <p>A string value that you can use to conditionally update your policy. You can provide the revision ID of your existing policy to make mutating requests against that policy.</p> <p>When you assign a policy revision ID, then later requests about that policy will be rejected with an <code>InvalidPolicyRevisionIdException</code> error if they don't provide the correct current revision ID.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.invalid_policy_revision_id_exception.InvalidPolicyRevisionIdException: <p>The policy revision ID that you provided doeesn't match the latest policy revision ID.</p>
            capo_rum.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The policy document that you specified is not formatted correctly.</p>
            capo_rum.errors.policy_size_limit_exceeded_exception.PolicySizeLimitExceededException: <p>The policy document is too large. The limit is 4 KB.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_rum.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_rum._operations.rum.put_resource_policy

            output, http_response = (
                capo_rum._operations.rum.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "name": name,
            "policy_document": policy_document,
        }
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_rum_metrics_destination(
        self,
        app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName",
        destination: "capo_rum.types.metric_destination.MetricDestination",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        destination_arn: Optional[
            "capo_rum.types.destination_arn.DestinationArn"
        ] = None,
        iam_role_arn: Optional["capo_rum.types.iam_role_arn.IamRoleArn"] = None,
    ) -> "capo_rum.types.put_rum_metrics_destination_response.PutRumMetricsDestinationResponse":
        """<p>Creates or updates a destination to receive extended metrics from CloudWatch RUM. You can send extended metrics to CloudWatch or to a CloudWatch Evidently experiment.</p> <p>For more information about extended metrics, see <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.html">BatchCreateRumMetricDefinitions</a>.</p>

        Args:
            app_monitor_name: <p>The name of the CloudWatch RUM app monitor that will send the metrics.</p>
            destination: <p>Defines the destination to send the metrics to. Valid values are <code>CloudWatch</code> and <code>Evidently</code>. If you specify <code>Evidently</code>, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.</p>
            destination_arn: <p>Use this parameter only if <code>Destination</code> is <code>Evidently</code>. This parameter specifies the ARN of the Evidently experiment that will receive the extended metrics.</p>
            iam_role_arn: <p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, don't use this parameter.</p> <p>This parameter specifies the ARN of an IAM role that RUM will assume to write to the Evidently experiment that you are sending metrics to. This role must have permission to write to that experiment.</p> <p>If you specify this parameter, you must be signed on to a role that has <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html">PassRole</a> permissions attached to it, to allow the role to be passed. The <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html#managed-policies-cloudwatch-RUM"> CloudWatchAmazonCloudWatchRUMFullAccess</a> policy doesn't include <code>PassRole</code> permissions.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.put_rum_metrics_destination_request.PutRumMetricsDestinationRequest]",
        ) -> OperationResponse[
            "capo_rum.types.put_rum_metrics_destination_response.PutRumMetricsDestinationResponse"
        ]:
            import capo_rum._operations.rum.put_rum_metrics_destination

            output, http_response = (
                capo_rum._operations.rum.put_rum_metrics_destination.put_rum_metrics_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.put_rum_metrics_destination_request.PutRumMetricsDestinationRequest = {
            "app_monitor_name": app_monitor_name,
            "destination": destination,
        }
        if destination_arn is not None:
            input_["destination_arn"] = destination_arn
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rum_metric_definition(
        self,
        app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName",
        destination: "capo_rum.types.metric_destination.MetricDestination",
        metric_definition: "capo_rum.types.metric_definition_request.MetricDefinitionRequest",
        metric_definition_id: "capo_rum.types.metric_definition_id.MetricDefinitionId",
        *,
        config_overrides: Optional[RUMClientConfig] = None,
        destination_arn: Optional[
            "capo_rum.types.destination_arn.DestinationArn"
        ] = None,
    ) -> "capo_rum.types.update_rum_metric_definition_response.UpdateRumMetricDefinitionResponse":
        """<p>Modifies one existing metric definition for CloudWatch RUM extended metrics. For more information about extended metrics, see <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.html">BatchCreateRumMetricsDefinitions</a>.</p>

        Args:
            app_monitor_name: <p>The name of the CloudWatch RUM app monitor that sends these metrics.</p>
            destination: <p>The destination to send the metrics to. Valid values are <code>CloudWatch</code> and <code>Evidently</code>. If you specify <code>Evidently</code>, you must also specify the ARN of the CloudWatchEvidently experiment that will receive the metrics and an IAM role that has permission to write to the experiment.</p>
            destination_arn: <p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter.</p> <p>This parameter specifies the ARN of the Evidently experiment that is to receive the metrics. You must have already defined this experiment as a valid destination. For more information, see <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html">PutRumMetricsDestination</a>.</p>
            metric_definition: <p>A structure that contains the new definition that you want to use for this metric.</p>
            metric_definition_id: <p>The ID of the metric definition to update.</p>

        Raises:
            capo_rum.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_rum.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_rum.errors.internal_server_exception.InternalServerException: <p>Internal service exception.</p>
            capo_rum.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_rum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_rum.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_rum.errors.validation_exception.ValidationException: <p>One of the arguments for the request is not valid.</p>
            capo_rum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rum.types.update_rum_metric_definition_request.UpdateRumMetricDefinitionRequest]",
        ) -> OperationResponse[
            "capo_rum.types.update_rum_metric_definition_response.UpdateRumMetricDefinitionResponse"
        ]:
            import capo_rum._operations.rum.update_rum_metric_definition

            output, http_response = (
                capo_rum._operations.rum.update_rum_metric_definition.update_rum_metric_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rum.types.update_rum_metric_definition_request.UpdateRumMetricDefinitionRequest = {
            "app_monitor_name": app_monitor_name,
            "destination": destination,
            "metric_definition": metric_definition,
            "metric_definition_id": metric_definition_id,
        }
        if destination_arn is not None:
            input_["destination_arn"] = destination_arn

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
