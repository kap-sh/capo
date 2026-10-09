"""Generated from Smithy shape ``com.amazonaws.networkmonitor#NetworkMonitor``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_networkmonitor._auth._signers
import capo_networkmonitor._auth._sigv4
from capo_networkmonitor._auth._identity import Credentials
from capo_networkmonitor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_networkmonitor._auth._zapros_handler import AuthMiddleware
from capo_networkmonitor._pagination import resolve_path as _resolve_path
from capo_networkmonitor._resources.network_monitor.monitor_resource import (
    MonitorResource,
)
from capo_networkmonitor._resources.network_monitor.probe_resource import ProbeResource
from capo_networkmonitor._services._aws_config import aws_config
from capo_networkmonitor._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_networkmonitor.types.aggregation_period
    import capo_networkmonitor.types.arn
    import capo_networkmonitor.types.create_monitor_input
    import capo_networkmonitor.types.create_monitor_output
    import capo_networkmonitor.types.create_monitor_probe_input_list
    import capo_networkmonitor.types.create_probe_input
    import capo_networkmonitor.types.create_probe_output
    import capo_networkmonitor.types.delete_monitor_input
    import capo_networkmonitor.types.delete_monitor_output
    import capo_networkmonitor.types.delete_probe_input
    import capo_networkmonitor.types.delete_probe_output
    import capo_networkmonitor.types.destination
    import capo_networkmonitor.types.get_monitor_input
    import capo_networkmonitor.types.get_monitor_output
    import capo_networkmonitor.types.get_probe_input
    import capo_networkmonitor.types.get_probe_output
    import capo_networkmonitor.types.list_monitors_input
    import capo_networkmonitor.types.list_monitors_output
    import capo_networkmonitor.types.list_tags_for_resource_input
    import capo_networkmonitor.types.list_tags_for_resource_output
    import capo_networkmonitor.types.max_results
    import capo_networkmonitor.types.monitor_summary
    import capo_networkmonitor.types.packet_size
    import capo_networkmonitor.types.pagination_token
    import capo_networkmonitor.types.port
    import capo_networkmonitor.types.probe_id
    import capo_networkmonitor.types.probe_input
    import capo_networkmonitor.types.probe_state
    import capo_networkmonitor.types.protocol
    import capo_networkmonitor.types.resource_name
    import capo_networkmonitor.types.tag_key_list
    import capo_networkmonitor.types.tag_map
    import capo_networkmonitor.types.tag_resource_input
    import capo_networkmonitor.types.tag_resource_output
    import capo_networkmonitor.types.untag_resource_input
    import capo_networkmonitor.types.untag_resource_output
    import capo_networkmonitor.types.update_monitor_input
    import capo_networkmonitor.types.update_monitor_output
    import capo_networkmonitor.types.update_probe_input
    import capo_networkmonitor.types.update_probe_output


class NetworkMonitorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class NetworkMonitorClient:
    """A client for the ``NetworkMonitor`` service.

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
        self._config = NetworkMonitorClientConfig(
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
        self.monitor_resource = MonitorResource(self)
        self.probe_resource = ProbeResource(self)

    def operation_options(
        self, config_overrides: Optional[NetworkMonitorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: NetworkMonitorClientConfig = config_overrides or {}
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
        resource_arn: "capo_networkmonitor.types.arn.Arn",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags assigned to this resource.</p>

        Args:
            resource_arn: <p>The </p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.list_tags_for_resource

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_networkmonitor.types.arn.Arn",
        tags: "capo_networkmonitor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.tag_resource_output.TagResourceOutput":
        """<p>Adds key-value pairs to a monitor or probe.</p>

        Args:
            resource_arn: <p>The ARN of the monitor or probe to tag.</p>
            tags: <p>The list of key-value pairs assigned to the monitor or probe.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.tag_resource

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_networkmonitor.types.arn.Arn",
        tag_keys: "capo_networkmonitor.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a key-value pair from a monitor or probe.</p>

        Args:
            resource_arn: <p>The ARN of the monitor or probe that the tag should be removed from. </p>
            tag_keys: <p>The key-value pa</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.untag_resource

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.untag_resource_input.UntagResourceInput = {
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

    def create_monitor(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        probes: Optional[
            "capo_networkmonitor.types.create_monitor_probe_input_list.CreateMonitorProbeInputList"
        ] = None,
        aggregation_period: Optional[
            "capo_networkmonitor.types.aggregation_period.AggregationPeriod"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkmonitor.types.create_monitor_output.CreateMonitorOutput":
        """<p>Creates a monitor between a source subnet and destination IP address. Within a monitor you'll create one or more probes that monitor network traffic between your source Amazon Web Services VPC subnets and your destination IP addresses. Each probe then aggregates and sends metrics to Amazon CloudWatch.</p> <p>You can also create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>source</code>—The subnet IDs where the probes will be created.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name identifying the monitor. It can contain only letters, underscores (_), or dashes (-), and can be up to 200 characters.</p>
            probes: <p>Displays a list of all of the probes created for a monitor.</p>
            aggregation_period: <p>The time, in seconds, that metrics are aggregated and sent to Amazon CloudWatch. Valid values are either <code>30</code> or <code>60</code>. <code>60</code> is the default if no period is chosen.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the monitor.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.create_monitor_input.CreateMonitorInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.create_monitor_output.CreateMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.create_monitor

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.create_monitor.create_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.create_monitor_input.CreateMonitorInput = {
            "monitor_name": monitor_name
        }
        if probes is not None:
            input_["probes"] = probes
        if aggregation_period is not None:
            input_["aggregation_period"] = aggregation_period
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_monitor(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.get_monitor_output.GetMonitorOutput":
        """<p>Returns details about a specific monitor. </p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor that details are returned for.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.get_monitor_input.GetMonitorInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.get_monitor_output.GetMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.get_monitor

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.get_monitor.get_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.get_monitor_input.GetMonitorInput = {
            "monitor_name": monitor_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_monitor(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        aggregation_period: "capo_networkmonitor.types.aggregation_period.AggregationPeriod",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.update_monitor_output.UpdateMonitorOutput":
        """<p>Updates the <code>aggregationPeriod</code> for a monitor. Monitors support an <code>aggregationPeriod</code> of either <code>30</code> or <code>60</code> seconds. This action requires the <code>monitorName</code> and <code>probeId</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to update. </p>
            aggregation_period: <p>The aggregation time, in seconds, to change to. This must be either <code>30</code> or <code>60</code>. </p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.update_monitor_input.UpdateMonitorInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.update_monitor_output.UpdateMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.update_monitor

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.update_monitor.update_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.update_monitor_input.UpdateMonitorInput = {
            "monitor_name": monitor_name,
            "aggregation_period": aggregation_period,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_monitor(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput":
        """<p>Deletes a specified monitor.</p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.delete_monitor_input.DeleteMonitorInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.delete_monitor

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.delete_monitor.delete_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.delete_monitor_input.DeleteMonitorInput = {
            "monitor_name": monitor_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_monitors(
        self,
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        next_token: Optional[
            "capo_networkmonitor.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_networkmonitor.types.max_results.MaxResults"
        ] = None,
        state: Optional[str] = None,
    ) -> "capo_networkmonitor.types.list_monitors_output.ListMonitorsOutput":
        """<p>Returns a list of all of your monitors.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            state: <p>The list of all monitors and their states.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.list_monitors_input.ListMonitorsInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.list_monitors_output.ListMonitorsOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.list_monitors

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.list_monitors.list_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.list_monitors_input.ListMonitorsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if state is not None:
            input_["state"] = state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_monitors(
        self,
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        next_token: Optional[
            "capo_networkmonitor.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_networkmonitor.types.max_results.MaxResults"
        ] = None,
        state: Optional[str] = None,
    ) -> "Iterator[capo_networkmonitor.types.monitor_summary.MonitorSummary]":
        _token = next_token
        while True:
            _response = self.list_monitors(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                state=state,
            )
            _page = _resolve_path(_response, ("monitors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_probe(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        probe: "capo_networkmonitor.types.probe_input.ProbeInput",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkmonitor.types.create_probe_output.CreateProbeOutput":
        """<p>Create a probe within a monitor. Once you create a probe, and it begins monitoring your network traffic, you'll incur billing charges for that probe. This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. Note the name of the <code>monitorName</code> you want to create the probe for.</p>

        Args:
            monitor_name: <p>The name of the monitor to associated with the probe. </p>
            probe: <p>Describes the details of an individual probe for a monitor.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the probe.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.create_probe_input.CreateProbeInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.create_probe_output.CreateProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.create_probe

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.create_probe.create_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.create_probe_input.CreateProbeInput = {
            "monitor_name": monitor_name,
            "probe": probe,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_probe(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        probe_id: "capo_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.get_probe_output.GetProbeOutput":
        """<p>Returns the details about a probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p>

        Args:
            monitor_name: <p>The name of the monitor associated with the probe. Run <code>ListMonitors</code> to get a list of monitor names.</p>
            probe_id: <p>The ID of the probe to get information about. Run <code>GetMonitor</code> action to get a list of probes and probe IDs for the monitor.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.get_probe_input.GetProbeInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.get_probe_output.GetProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.get_probe

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.get_probe.get_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.get_probe_input.GetProbeInput = {
            "monitor_name": monitor_name,
            "probe_id": probe_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_probe(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        probe_id: "capo_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        state: Optional["capo_networkmonitor.types.probe_state.ProbeState"] = None,
        destination: Optional[
            "capo_networkmonitor.types.destination.Destination"
        ] = None,
        destination_port: Optional["capo_networkmonitor.types.port.Port"] = None,
        protocol: Optional["capo_networkmonitor.types.protocol.Protocol"] = None,
        packet_size: Optional[
            "capo_networkmonitor.types.packet_size.PacketSize"
        ] = None,
    ) -> "capo_networkmonitor.types.update_probe_output.UpdateProbeOutput":
        """<p>Updates a monitor probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p> <p>You can update the following para create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>state</code>—The state of the probe.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name of the monitor that the probe was updated for.</p>
            probe_id: <p>The ID of the probe to update.</p>
            state: <p>The state of the probe update.</p>
            destination: <p>The updated IP address for the probe destination. This must be either an IPv4 or IPv6 address.</p>
            destination_port: <p>The updated port for the probe destination. This is required only if the <code>protocol</code> is <code>TCP</code> and must be a number between <code>1</code> and <code>65536</code>.</p>
            protocol: <p>The updated network protocol for the destination. This can be either <code>TCP</code> or <code>ICMP</code>. If the protocol is <code>TCP</code>, then <code>port</code> is also required.</p>
            packet_size: <p>he updated packets size for network traffic between the source and destination. This must be a number between <code>56</code> and <code>8500</code>.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.update_probe_input.UpdateProbeInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.update_probe_output.UpdateProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.update_probe

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.update_probe.update_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.update_probe_input.UpdateProbeInput = {
            "monitor_name": monitor_name,
            "probe_id": probe_id,
        }
        if state is not None:
            input_["state"] = state
        if destination is not None:
            input_["destination"] = destination
        if destination_port is not None:
            input_["destination_port"] = destination_port
        if protocol is not None:
            input_["protocol"] = protocol
        if packet_size is not None:
            input_["packet_size"] = packet_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_probe(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        probe_id: "capo_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.delete_probe_output.DeleteProbeOutput":
        """<p>Deletes the specified probe. Once a probe is deleted you'll no longer incur any billing fees for that probe.</p> <p>This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. You can only delete a single probe at a time using this action. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>
            probe_id: <p>The ID of the probe to delete. </p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.delete_probe_input.DeleteProbeInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.delete_probe_output.DeleteProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.delete_probe

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.delete_probe.delete_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmonitor.types.delete_probe_input.DeleteProbeInput = {
            "monitor_name": monitor_name,
            "probe_id": probe_id,
        }

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
