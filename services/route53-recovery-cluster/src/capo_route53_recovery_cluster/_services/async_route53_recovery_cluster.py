"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#ToggleCustomerAPI``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_route53_recovery_cluster._auth._signers
import capo_route53_recovery_cluster._auth._sigv4
from capo_route53_recovery_cluster._auth._identity import Credentials
from capo_route53_recovery_cluster._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_route53_recovery_cluster._auth._zapros_handler import AuthMiddleware
from capo_route53_recovery_cluster._pagination import resolve_path as _resolve_path
from capo_route53_recovery_cluster._services._aws_config import aaws_config
from capo_route53_recovery_cluster._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.arn
    import capo_route53_recovery_cluster.types.arns
    import capo_route53_recovery_cluster.types.get_routing_control_state_request
    import capo_route53_recovery_cluster.types.get_routing_control_state_response
    import capo_route53_recovery_cluster.types.list_routing_controls_request
    import capo_route53_recovery_cluster.types.list_routing_controls_response
    import capo_route53_recovery_cluster.types.max_results
    import capo_route53_recovery_cluster.types.page_token
    import capo_route53_recovery_cluster.types.routing_control
    import capo_route53_recovery_cluster.types.routing_control_state
    import capo_route53_recovery_cluster.types.update_routing_control_state_entries
    import capo_route53_recovery_cluster.types.update_routing_control_state_request
    import capo_route53_recovery_cluster.types.update_routing_control_state_response
    import capo_route53_recovery_cluster.types.update_routing_control_states_request
    import capo_route53_recovery_cluster.types.update_routing_control_states_response


class AsyncRoute53RecoveryClusterClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncRoute53RecoveryClusterClient:
    """A client for the ``Route53RecoveryCluster`` service.

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
        self._config = AsyncRoute53RecoveryClusterClientConfig(
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
        self, config_overrides: Optional[AsyncRoute53RecoveryClusterClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRoute53RecoveryClusterClientConfig = config_overrides or {}
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

    async def get_routing_control_state(
        self,
        routing_control_arn: "capo_route53_recovery_cluster.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryClusterClientConfig] = None,
    ) -> "capo_route53_recovery_cluster.types.get_routing_control_state_response.GetRoutingControlStateResponse":
        """<p>Get the state for a routing control. A routing control is a simple on/off switch that you can use to route traffic to cells. When a routing control state is set to ON, traffic flows to a cell. When the state is set to OFF, traffic does not flow. </p> <p>Before you can create a routing control, you must first create a cluster, and then host the control in a control panel on the cluster. For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create.html"> Create routing control structures</a> in the Amazon Route 53 Application Recovery Controller Developer Guide. You access one of the endpoints for the cluster to get or update the routing control state to redirect traffic for your application. </p> <p> <i>You must specify Regional endpoints when you work with API cluster operations to get or update routing control states in Route 53 ARC.</i> </p> <p>To see a code example for getting a routing control state, including accessing Regional cluster endpoints in sequence, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples_actions.html">API examples</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p> <p>Learn more about working with routing controls in the following topics in the Amazon Route 53 Application Recovery Controller Developer Guide:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.html"> Viewing and updating routing control states</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html">Working with routing controls in Route 53 ARC</a> </p> </li> </ul>

        Args:
            routing_control_arn: <p>The Amazon Resource Name (ARN) for the routing control that you want to get the state for.</p>

        Raises:
            capo_route53_recovery_cluster.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_route53_recovery_cluster.errors.endpoint_temporarily_unavailable_exception.EndpointTemporarilyUnavailableException: <p>The cluster endpoint isn't available. Try another cluster endpoint.</p>
            capo_route53_recovery_cluster.errors.internal_server_exception.InternalServerException: <p>There was an unexpected error during processing of the request.</p>
            capo_route53_recovery_cluster.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a routing control or control panel that was not found.</p>
            capo_route53_recovery_cluster.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_route53_recovery_cluster.errors.validation_exception.ValidationException: <p>There was a validation error on the request.</p>
            capo_route53_recovery_cluster.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_cluster.types.get_routing_control_state_request.GetRoutingControlStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_cluster.types.get_routing_control_state_response.GetRoutingControlStateResponse"
        ]:
            import capo_route53_recovery_cluster._operations.toggle_customer_api.get_routing_control_state

            (
                output,
                http_response,
            ) = await capo_route53_recovery_cluster._operations.toggle_customer_api.get_routing_control_state.async_get_routing_control_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_cluster.types.get_routing_control_state_request.GetRoutingControlStateRequest = {
            "routing_control_arn": routing_control_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_routing_controls(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryClusterClientConfig] = None,
        control_panel_arn: Optional[
            "capo_route53_recovery_cluster.types.arn.Arn"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_cluster.types.page_token.PageToken"
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_cluster.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_route53_recovery_cluster.types.list_routing_controls_response.ListRoutingControlsResponse":
        """<p>List routing control names and Amazon Resource Names (ARNs), as well as the routing control state for each routing control, along with the control panel name and control panel ARN for the routing controls. If you specify a control panel ARN, this call lists the routing controls in the control panel. Otherwise, it lists all the routing controls in the cluster.</p> <p>A routing control is a simple on/off switch in Route 53 ARC that you can use to route traffic to cells. When a routing control state is set to ON, traffic flows to a cell. When the state is set to OFF, traffic does not flow.</p> <p>Before you can create a routing control, you must first create a cluster, and then host the control in a control panel on the cluster. For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create.html"> Create routing control structures</a> in the Amazon Route 53 Application Recovery Controller Developer Guide. You access one of the endpoints for the cluster to get or update the routing control state to redirect traffic for your application. </p> <p> <i>You must specify Regional endpoints when you work with API cluster operations to use this API operation to list routing controls in Route 53 ARC.</i> </p> <p>Learn more about working with routing controls in the following topics in the Amazon Route 53 Application Recovery Controller Developer Guide:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.html"> Viewing and updating routing control states</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html">Working with routing controls in Route 53 ARC</a> </p> </li> </ul>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel of the routing controls to list.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of routing controls objects that you want to return with this call. The default value is 500.</p>

        Raises:
            capo_route53_recovery_cluster.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_route53_recovery_cluster.errors.endpoint_temporarily_unavailable_exception.EndpointTemporarilyUnavailableException: <p>The cluster endpoint isn't available. Try another cluster endpoint.</p>
            capo_route53_recovery_cluster.errors.internal_server_exception.InternalServerException: <p>There was an unexpected error during processing of the request.</p>
            capo_route53_recovery_cluster.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a routing control or control panel that was not found.</p>
            capo_route53_recovery_cluster.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_route53_recovery_cluster.errors.validation_exception.ValidationException: <p>There was a validation error on the request.</p>
            capo_route53_recovery_cluster.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_cluster.types.list_routing_controls_request.ListRoutingControlsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_cluster.types.list_routing_controls_response.ListRoutingControlsResponse"
        ]:
            import capo_route53_recovery_cluster._operations.toggle_customer_api.list_routing_controls

            (
                output,
                http_response,
            ) = await capo_route53_recovery_cluster._operations.toggle_customer_api.list_routing_controls.async_list_routing_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_cluster.types.list_routing_controls_request.ListRoutingControlsRequest = {}
        if control_panel_arn is not None:
            input_["control_panel_arn"] = control_panel_arn
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

    async def iter_list_routing_controls(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryClusterClientConfig] = None,
        control_panel_arn: Optional[
            "capo_route53_recovery_cluster.types.arn.Arn"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_cluster.types.page_token.PageToken"
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_cluster.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_route53_recovery_cluster.types.routing_control.RoutingControl]":
        _token = next_token
        while True:
            _response = await self.list_routing_controls(
                config_overrides=config_overrides,
                control_panel_arn=control_panel_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("routing_controls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_routing_control_state(
        self,
        routing_control_arn: "capo_route53_recovery_cluster.types.arn.Arn",
        routing_control_state: "capo_route53_recovery_cluster.types.routing_control_state.RoutingControlState",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryClusterClientConfig] = None,
        safety_rules_to_override: Optional[
            "capo_route53_recovery_cluster.types.arns.Arns"
        ] = None,
    ) -> "capo_route53_recovery_cluster.types.update_routing_control_state_response.UpdateRoutingControlStateResponse":
        """<p>Set the state of the routing control to reroute traffic. You can set the value to ON or OFF. When the state is ON, traffic flows to a cell. When the state is OFF, traffic does not flow.</p> <p>With Route 53 ARC, you can add safety rules for routing controls, which are safeguards for routing control state updates that help prevent unexpected outcomes, like fail open traffic routing. However, there are scenarios when you might want to bypass the routing control safeguards that are enforced with safety rules that you've configured. For example, you might want to fail over quickly for disaster recovery, and one or more safety rules might be unexpectedly preventing you from updating a routing control state to reroute traffic. In a "break glass" scenario like this, you can override one or more safety rules to change a routing control state and fail over your application.</p> <p>The <code>SafetyRulesToOverride</code> property enables you override one or more safety rules and update routing control states. For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html"> Override safety rules to reroute traffic</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p> <p> <i>You must specify Regional endpoints when you work with API cluster operations to get or update routing control states in Route 53 ARC.</i> </p> <p>To see a code example for getting a routing control state, including accessing Regional cluster endpoints in sequence, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples_actions.html">API examples</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.html"> Viewing and updating routing control states</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html">Working with routing controls overall</a> </p> </li> </ul>

        Args:
            routing_control_arn: <p>The Amazon Resource Name (ARN) for the routing control that you want to update the state for.</p>
            routing_control_state: <p>The state of the routing control. You can set the value to ON or OFF.</p>
            safety_rules_to_override: <p>The Amazon Resource Names (ARNs) for the safety rules that you want to override when you're updating the state of a routing control. You can override one safety rule or multiple safety rules by including one or more ARNs, separated by commas.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html"> Override safety rules to reroute traffic</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p>

        Raises:
            capo_route53_recovery_cluster.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_route53_recovery_cluster.errors.conflict_exception.ConflictException: <p>There was a conflict with this request. Try again.</p>
            capo_route53_recovery_cluster.errors.endpoint_temporarily_unavailable_exception.EndpointTemporarilyUnavailableException: <p>The cluster endpoint isn't available. Try another cluster endpoint.</p>
            capo_route53_recovery_cluster.errors.internal_server_exception.InternalServerException: <p>There was an unexpected error during processing of the request.</p>
            capo_route53_recovery_cluster.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a routing control or control panel that was not found.</p>
            capo_route53_recovery_cluster.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_route53_recovery_cluster.errors.validation_exception.ValidationException: <p>There was a validation error on the request.</p>
            capo_route53_recovery_cluster.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_cluster.types.update_routing_control_state_request.UpdateRoutingControlStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_cluster.types.update_routing_control_state_response.UpdateRoutingControlStateResponse"
        ]:
            import capo_route53_recovery_cluster._operations.toggle_customer_api.update_routing_control_state

            (
                output,
                http_response,
            ) = await capo_route53_recovery_cluster._operations.toggle_customer_api.update_routing_control_state.async_update_routing_control_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_cluster.types.update_routing_control_state_request.UpdateRoutingControlStateRequest = {
            "routing_control_arn": routing_control_arn,
            "routing_control_state": routing_control_state,
        }
        if safety_rules_to_override is not None:
            input_["safety_rules_to_override"] = safety_rules_to_override

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_routing_control_states(
        self,
        update_routing_control_state_entries: "capo_route53_recovery_cluster.types.update_routing_control_state_entries.UpdateRoutingControlStateEntries",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryClusterClientConfig] = None,
        safety_rules_to_override: Optional[
            "capo_route53_recovery_cluster.types.arns.Arns"
        ] = None,
    ) -> "capo_route53_recovery_cluster.types.update_routing_control_states_response.UpdateRoutingControlStatesResponse":
        """<p>Set multiple routing control states. You can set the value for each state to be ON or OFF. When the state is ON, traffic flows to a cell. When it's OFF, traffic does not flow.</p> <p>With Route 53 ARC, you can add safety rules for routing controls, which are safeguards for routing control state updates that help prevent unexpected outcomes, like fail open traffic routing. However, there are scenarios when you might want to bypass the routing control safeguards that are enforced with safety rules that you've configured. For example, you might want to fail over quickly for disaster recovery, and one or more safety rules might be unexpectedly preventing you from updating a routing control state to reroute traffic. In a "break glass" scenario like this, you can override one or more safety rules to change a routing control state and fail over your application.</p> <p>The <code>SafetyRulesToOverride</code> property enables you override one or more safety rules and update routing control states. For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html"> Override safety rules to reroute traffic</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p> <p> <i>You must specify Regional endpoints when you work with API cluster operations to get or update routing control states in Route 53 ARC.</i> </p> <p>To see a code example for getting a routing control state, including accessing Regional cluster endpoints in sequence, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples_actions.html">API examples</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.html"> Viewing and updating routing control states</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html">Working with routing controls overall</a> </p> </li> </ul>

        Args:
            update_routing_control_state_entries: <p>A set of routing control entries that you want to update.</p>
            safety_rules_to_override: <p>The Amazon Resource Names (ARNs) for the safety rules that you want to override when you're updating routing control states. You can override one safety rule or multiple safety rules by including one or more ARNs, separated by commas.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html"> Override safety rules to reroute traffic</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p>

        Raises:
            capo_route53_recovery_cluster.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_route53_recovery_cluster.errors.conflict_exception.ConflictException: <p>There was a conflict with this request. Try again.</p>
            capo_route53_recovery_cluster.errors.endpoint_temporarily_unavailable_exception.EndpointTemporarilyUnavailableException: <p>The cluster endpoint isn't available. Try another cluster endpoint.</p>
            capo_route53_recovery_cluster.errors.internal_server_exception.InternalServerException: <p>There was an unexpected error during processing of the request.</p>
            capo_route53_recovery_cluster.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a routing control or control panel that was not found.</p>
            capo_route53_recovery_cluster.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request can't update that many routing control states at the same time. Try again with fewer routing control states.</p>
            capo_route53_recovery_cluster.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_route53_recovery_cluster.errors.validation_exception.ValidationException: <p>There was a validation error on the request.</p>
            capo_route53_recovery_cluster.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_cluster.types.update_routing_control_states_request.UpdateRoutingControlStatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_cluster.types.update_routing_control_states_response.UpdateRoutingControlStatesResponse"
        ]:
            import capo_route53_recovery_cluster._operations.toggle_customer_api.update_routing_control_states

            (
                output,
                http_response,
            ) = await capo_route53_recovery_cluster._operations.toggle_customer_api.update_routing_control_states.async_update_routing_control_states(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_cluster.types.update_routing_control_states_request.UpdateRoutingControlStatesRequest = {
            "update_routing_control_state_entries": update_routing_control_state_entries
        }
        if safety_rules_to_override is not None:
            input_["safety_rules_to_override"] = safety_rules_to_override

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
