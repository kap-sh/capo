"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#Route53RecoveryControlConfig``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_route53_recovery_control_config._auth._signers
import capo_route53_recovery_control_config._auth._sigv4
from capo_route53_recovery_control_config._auth._identity import Credentials
from capo_route53_recovery_control_config._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_route53_recovery_control_config._auth._zapros_handler import AuthMiddleware
from capo_route53_recovery_control_config._pagination import (
    resolve_path as _resolve_path,
)
from capo_route53_recovery_control_config._services._aws_config import aaws_config
from capo_route53_recovery_control_config._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__list_of__string
    import capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s
    import capo_route53_recovery_control_config.types.__string
    import capo_route53_recovery_control_config.types.__string_max36_pattern_s
    import capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09
    import capo_route53_recovery_control_config.types.assertion_rule_update
    import capo_route53_recovery_control_config.types.cluster
    import capo_route53_recovery_control_config.types.control_panel
    import capo_route53_recovery_control_config.types.create_cluster_request
    import capo_route53_recovery_control_config.types.create_cluster_response
    import capo_route53_recovery_control_config.types.create_control_panel_request
    import capo_route53_recovery_control_config.types.create_control_panel_response
    import capo_route53_recovery_control_config.types.create_routing_control_request
    import capo_route53_recovery_control_config.types.create_routing_control_response
    import capo_route53_recovery_control_config.types.create_safety_rule_request
    import capo_route53_recovery_control_config.types.create_safety_rule_response
    import capo_route53_recovery_control_config.types.delete_cluster_request
    import capo_route53_recovery_control_config.types.delete_cluster_response
    import capo_route53_recovery_control_config.types.delete_control_panel_request
    import capo_route53_recovery_control_config.types.delete_control_panel_response
    import capo_route53_recovery_control_config.types.delete_routing_control_request
    import capo_route53_recovery_control_config.types.delete_routing_control_response
    import capo_route53_recovery_control_config.types.delete_safety_rule_request
    import capo_route53_recovery_control_config.types.delete_safety_rule_response
    import capo_route53_recovery_control_config.types.describe_cluster_request
    import capo_route53_recovery_control_config.types.describe_cluster_response
    import capo_route53_recovery_control_config.types.describe_control_panel_request
    import capo_route53_recovery_control_config.types.describe_control_panel_response
    import capo_route53_recovery_control_config.types.describe_routing_control_request
    import capo_route53_recovery_control_config.types.describe_routing_control_response
    import capo_route53_recovery_control_config.types.describe_safety_rule_request
    import capo_route53_recovery_control_config.types.describe_safety_rule_response
    import capo_route53_recovery_control_config.types.gating_rule_update
    import capo_route53_recovery_control_config.types.get_resource_policy_request
    import capo_route53_recovery_control_config.types.get_resource_policy_response
    import capo_route53_recovery_control_config.types.list_associated_route53_health_checks_request
    import capo_route53_recovery_control_config.types.list_associated_route53_health_checks_response
    import capo_route53_recovery_control_config.types.list_clusters_request
    import capo_route53_recovery_control_config.types.list_clusters_response
    import capo_route53_recovery_control_config.types.list_control_panels_request
    import capo_route53_recovery_control_config.types.list_control_panels_response
    import capo_route53_recovery_control_config.types.list_routing_controls_request
    import capo_route53_recovery_control_config.types.list_routing_controls_response
    import capo_route53_recovery_control_config.types.list_safety_rules_request
    import capo_route53_recovery_control_config.types.list_safety_rules_response
    import capo_route53_recovery_control_config.types.list_tags_for_resource_request
    import capo_route53_recovery_control_config.types.list_tags_for_resource_response
    import capo_route53_recovery_control_config.types.max_results
    import capo_route53_recovery_control_config.types.network_type
    import capo_route53_recovery_control_config.types.new_assertion_rule
    import capo_route53_recovery_control_config.types.new_gating_rule
    import capo_route53_recovery_control_config.types.routing_control
    import capo_route53_recovery_control_config.types.rule
    import capo_route53_recovery_control_config.types.tag_resource_request
    import capo_route53_recovery_control_config.types.tag_resource_response
    import capo_route53_recovery_control_config.types.untag_resource_request
    import capo_route53_recovery_control_config.types.untag_resource_response
    import capo_route53_recovery_control_config.types.update_cluster_request
    import capo_route53_recovery_control_config.types.update_cluster_response
    import capo_route53_recovery_control_config.types.update_control_panel_request
    import capo_route53_recovery_control_config.types.update_control_panel_response
    import capo_route53_recovery_control_config.types.update_routing_control_request
    import capo_route53_recovery_control_config.types.update_routing_control_response
    import capo_route53_recovery_control_config.types.update_safety_rule_request
    import capo_route53_recovery_control_config.types.update_safety_rule_response


class AsyncRoute53RecoveryControlConfigClientConfig(
    TypedDict, total=False, closed=True
):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncRoute53RecoveryControlConfigClient:
    """A client for the ``Route53RecoveryControlConfig`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = AsyncRoute53RecoveryControlConfigClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRoute53RecoveryControlConfigClientConfig = (
            config_overrides or {}
        )
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def create_cluster(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        client_token: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        cluster_name: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        tags: Optional[
            "capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
        ] = None,
        network_type: Optional[
            "capo_route53_recovery_control_config.types.network_type.NetworkType"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.create_cluster_response.CreateClusterResponse":
        """<p>Create a new cluster. A cluster is a set of redundant Regional endpoints against which you can run API calls to update or get the state of one or more routing controls. Each cluster has a name, status, Amazon Resource Name (ARN), and an array of the five cluster endpoints (one for each supported Amazon Web Services Region) that you can use with API calls to the cluster data plane.</p>

        Args:
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>
            cluster_name: <p>The name of the cluster.</p>
            tags: <p>The tags associated with the cluster.</p>
            network_type: <p>The network type of the cluster. NetworkType can be one of the following: IPV4, DUALSTACK.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>402 response - You attempted to create more resources than the service allows based on service quotas.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.create_cluster_request.CreateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.create_cluster

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.create_cluster_request.CreateClusterRequest = {}
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if tags is not None:
            input_["tags"] = tags
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_control_panel(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        client_token: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        cluster_arn: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
        ] = None,
        control_panel_name: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        tags: Optional[
            "capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.create_control_panel_response.CreateControlPanelResponse":
        """<p>Creates a new control panel. A control panel represents a group of routing controls that can be changed together in a single transaction. You can use a control panel to centrally view the operational status of applications across your organization, and trigger multi-app failovers in a single transaction, for example, to fail over an Availability Zone or Amazon Web Services Region.</p>

        Args:
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster for the control panel.</p>
            control_panel_name: <p>The name of the control panel.</p>
            tags: <p>The tags associated with the control panel.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>402 response - You attempted to create more resources than the service allows based on service quotas.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.create_control_panel_request.CreateControlPanelRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.create_control_panel_response.CreateControlPanelResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.create_control_panel

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.create_control_panel.async_create_control_panel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.create_control_panel_request.CreateControlPanelRequest = {}
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if control_panel_name is not None:
            input_["control_panel_name"] = control_panel_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_routing_control(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        client_token: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        cluster_arn: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
        ] = None,
        control_panel_arn: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
        ] = None,
        routing_control_name: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.create_routing_control_response.CreateRoutingControlResponse":
        """<p>Creates a new routing control.</p> <p>A routing control has one of two states: ON and OFF. You can map the routing control state to the state of an Amazon Route 53 health check, which can be used to control traffic routing.</p> <p>To get or update the routing control state, see the Recovery Cluster (data plane) API actions for Amazon Route 53 Application Recovery Controller.</p>

        Args:
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster that includes the routing control.</p>
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel that includes the routing control.</p>
            routing_control_name: <p>The name of the routing control.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>402 response - You attempted to create more resources than the service allows based on service quotas.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.create_routing_control_request.CreateRoutingControlRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.create_routing_control_response.CreateRoutingControlResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.create_routing_control

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.create_routing_control.async_create_routing_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.create_routing_control_request.CreateRoutingControlRequest = {}
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if control_panel_arn is not None:
            input_["control_panel_arn"] = control_panel_arn
        if routing_control_name is not None:
            input_["routing_control_name"] = routing_control_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_safety_rule(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        assertion_rule: Optional[
            "capo_route53_recovery_control_config.types.new_assertion_rule.NewAssertionRule"
        ] = None,
        client_token: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        gating_rule: Optional[
            "capo_route53_recovery_control_config.types.new_gating_rule.NewGatingRule"
        ] = None,
        tags: Optional[
            "capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.create_safety_rule_response.CreateSafetyRuleResponse":
        """<p>Creates a safety rule in a control panel. Safety rules let you add safeguards around changing routing control states, and for enabling and disabling routing controls, to help prevent unexpected outcomes.</p> <p>There are two types of safety rules: assertion rules and gating rules.</p> <p>Assertion rule: An assertion rule enforces that, when you change a routing control state, that a certain criteria is met. For example, the criteria might be that at least one routing control state is On after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.</p> <p>Gating rule: A gating rule lets you configure a gating routing control as an overall "on/off" switch for a group of routing controls. Or, you can configure more complex gating scenarios, for example by configuring multiple gating routing controls.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.safety-rules.html">Safety rules</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p>

        Args:
            assertion_rule: <p>The assertion rule requested.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>
            gating_rule: <p>The gating rule requested.</p>
            tags: <p>The tags associated with the safety rule.</p>

        Raises:
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.create_safety_rule_request.CreateSafetyRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.create_safety_rule_response.CreateSafetyRuleResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.create_safety_rule

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.create_safety_rule.async_create_safety_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.create_safety_rule_request.CreateSafetyRuleRequest = {}
        if assertion_rule is not None:
            input_["assertion_rule"] = assertion_rule
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if gating_rule is not None:
            input_["gating_rule"] = gating_rule
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster(
        self,
        cluster_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Delete a cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster that you're deleting.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.delete_cluster

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_control_panel(
        self,
        control_panel_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.delete_control_panel_response.DeleteControlPanelResponse":
        """<p>Deletes a control panel.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.delete_control_panel_request.DeleteControlPanelRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.delete_control_panel_response.DeleteControlPanelResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.delete_control_panel

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.delete_control_panel.async_delete_control_panel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.delete_control_panel_request.DeleteControlPanelRequest = {
            "control_panel_arn": control_panel_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_routing_control(
        self,
        routing_control_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.delete_routing_control_response.DeleteRoutingControlResponse":
        """<p>Deletes a routing control.</p>

        Args:
            routing_control_arn: <p>The Amazon Resource Name (ARN) of the routing control that you're deleting.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.delete_routing_control_request.DeleteRoutingControlRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.delete_routing_control_response.DeleteRoutingControlResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.delete_routing_control

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.delete_routing_control.async_delete_routing_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.delete_routing_control_request.DeleteRoutingControlRequest = {
            "routing_control_arn": routing_control_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_safety_rule(
        self,
        safety_rule_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.delete_safety_rule_response.DeleteSafetyRuleResponse":
        """<p>Deletes a safety rule.</p>/&gt;

        Args:
            safety_rule_arn: <p>The ARN of the safety rule.</p>

        Raises:
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.delete_safety_rule_request.DeleteSafetyRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.delete_safety_rule_response.DeleteSafetyRuleResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.delete_safety_rule

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.delete_safety_rule.async_delete_safety_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.delete_safety_rule_request.DeleteSafetyRuleRequest = {
            "safety_rule_arn": safety_rule_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_cluster(
        self,
        cluster_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.describe_cluster_response.DescribeClusterResponse":
        """<p>Display the details about a cluster. The response includes the cluster name, endpoints, status, and Amazon Resource Name (ARN).</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.describe_cluster_request.DescribeClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.describe_cluster_response.DescribeClusterResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.describe_cluster

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.describe_cluster.async_describe_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.describe_cluster_request.DescribeClusterRequest = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_control_panel(
        self,
        control_panel_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.describe_control_panel_response.DescribeControlPanelResponse":
        """<p>Displays details about a control panel.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.describe_control_panel_request.DescribeControlPanelRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.describe_control_panel_response.DescribeControlPanelResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.describe_control_panel

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.describe_control_panel.async_describe_control_panel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.describe_control_panel_request.DescribeControlPanelRequest = {
            "control_panel_arn": control_panel_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_routing_control(
        self,
        routing_control_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.describe_routing_control_response.DescribeRoutingControlResponse":
        """<p>Displays details about a routing control. A routing control has one of two states: ON and OFF. You can map the routing control state to the state of an Amazon Route 53 health check, which can be used to control routing.</p> <p>To get or update the routing control state, see the Recovery Cluster (data plane) API actions for Amazon Route 53 Application Recovery Controller.</p>

        Args:
            routing_control_arn: <p>The Amazon Resource Name (ARN) of the routing control.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.describe_routing_control_request.DescribeRoutingControlRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.describe_routing_control_response.DescribeRoutingControlResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.describe_routing_control

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.describe_routing_control.async_describe_routing_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.describe_routing_control_request.DescribeRoutingControlRequest = {
            "routing_control_arn": routing_control_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_safety_rule(
        self,
        safety_rule_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.describe_safety_rule_response.DescribeSafetyRuleResponse":
        """<p>Returns information about a safety rule.</p>

        Args:
            safety_rule_arn: <p>The ARN of the safety rule.</p>

        Raises:
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.describe_safety_rule_request.DescribeSafetyRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.describe_safety_rule_response.DescribeSafetyRuleResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.describe_safety_rule

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.describe_safety_rule.async_describe_safety_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.describe_safety_rule_request.DescribeSafetyRuleRequest = {
            "safety_rule_arn": safety_rule_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Get information about the resource policy for a cluster.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_associated_route53_health_checks(
        self,
        routing_control_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.list_associated_route53_health_checks_response.ListAssociatedRoute53HealthChecksResponse":
        """<p>Returns an array of all Amazon Route 53 health checks associated with a specific routing control.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            routing_control_arn: <p>The Amazon Resource Name (ARN) of the routing control.</p>

        Raises:
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.list_associated_route53_health_checks_request.ListAssociatedRoute53HealthChecksRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.list_associated_route53_health_checks_response.ListAssociatedRoute53HealthChecksResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_associated_route53_health_checks

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_associated_route53_health_checks.async_list_associated_route53_health_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.list_associated_route53_health_checks_request.ListAssociatedRoute53HealthChecksRequest = {
            "routing_control_arn": routing_control_arn
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

    async def iter_list_associated_route53_health_checks(
        self,
        routing_control_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_route53_recovery_control_config.types.__string_max36_pattern_s.__stringMax36PatternS]":
        _token = next_token
        while True:
            _response = await self.list_associated_route53_health_checks(
                routing_control_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("health_check_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_clusters(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.list_clusters_response.ListClustersResponse":
        """<p>Returns an array of all the clusters in an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.list_clusters_request.ListClustersRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.list_clusters_response.ListClustersResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_clusters

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_clusters.async_list_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.list_clusters_request.ListClustersRequest = {}
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

    async def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_route53_recovery_control_config.types.cluster.Cluster]":
        _token = next_token
        while True:
            _response = await self.list_clusters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_control_panels(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        cluster_arn: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.list_control_panels_response.ListControlPanelsResponse":
        """<p>Returns an array of control panels in an account or in a cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of a cluster.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.list_control_panels_request.ListControlPanelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.list_control_panels_response.ListControlPanelsResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_control_panels

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_control_panels.async_list_control_panels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.list_control_panels_request.ListControlPanelsRequest = {}
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
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

    async def iter_list_control_panels(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        cluster_arn: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_route53_recovery_control_config.types.control_panel.ControlPanel]":
        _token = next_token
        while True:
            _response = await self.list_control_panels(
                config_overrides=config_overrides,
                cluster_arn=cluster_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("control_panels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_routing_controls(
        self,
        control_panel_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.list_routing_controls_response.ListRoutingControlsResponse":
        """<p>Returns an array of routing controls for a control panel. A routing control is an Amazon Route 53 Application Recovery Controller construct that has one of two states: ON and OFF. You can map the routing control state to the state of an Amazon Route 53 health check, which can be used to control routing.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.list_routing_controls_request.ListRoutingControlsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.list_routing_controls_response.ListRoutingControlsResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_routing_controls

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_routing_controls.async_list_routing_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.list_routing_controls_request.ListRoutingControlsRequest = {
            "control_panel_arn": control_panel_arn
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

    async def iter_list_routing_controls(
        self,
        control_panel_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_route53_recovery_control_config.types.routing_control.RoutingControl]":
        _token = next_token
        while True:
            _response = await self.list_routing_controls(
                control_panel_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("routing_controls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_safety_rules(
        self,
        control_panel_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.list_safety_rules_response.ListSafetyRulesResponse":
        """<p>List the safety rules (the assertion rules and gating rules) that you've defined for the routing controls in a control panel.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.list_safety_rules_request.ListSafetyRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.list_safety_rules_response.ListSafetyRulesResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_safety_rules

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_safety_rules.async_list_safety_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.list_safety_rules_request.ListSafetyRulesRequest = {
            "control_panel_arn": control_panel_arn
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

    async def iter_list_safety_rules(
        self,
        control_panel_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "capo_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_route53_recovery_control_config.types.rule.Rule]":
        _token = next_token
        while True:
            _response = await self.list_safety_rules(
                control_panel_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("safety_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource that's tagged.</p>

        Raises:
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        tags: Optional[
            "capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource that's tagged.</p>
            tags: <p>The tags associated with the resource.</p>

        Raises:
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.tag_resource

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
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

    async def untag_resource(
        self,
        resource_arn: "capo_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        tag_keys: Optional[
            "capo_route53_recovery_control_config.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource that's tagged.</p>
            tag_keys: <p>Keys for the tags to be removed.</p>

        Raises:
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.untag_resource

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_cluster(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        cluster_arn: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
        ] = None,
        network_type: Optional[
            "capo_route53_recovery_control_config.types.network_type.NetworkType"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.update_cluster_response.UpdateClusterResponse":
        """<p>Updates an existing cluster. You can only update the network type of a cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>
            network_type: <p>The network type of the cluster. NetworkType can be one of the following: IPV4, DUALSTACK.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.update_cluster_request.UpdateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.update_cluster

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.update_cluster.async_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.update_cluster_request.UpdateClusterRequest = {}
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_control_panel(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        control_panel_arn: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
        ] = None,
        control_panel_name: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.update_control_panel_response.UpdateControlPanelResponse":
        """<p>Updates a control panel. The only update you can make to a control panel is to change the name of the control panel.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>
            control_panel_name: <p>The name of the control panel.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.update_control_panel_request.UpdateControlPanelRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.update_control_panel_response.UpdateControlPanelResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.update_control_panel

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.update_control_panel.async_update_control_panel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.update_control_panel_request.UpdateControlPanelRequest = {}
        if control_panel_arn is not None:
            input_["control_panel_arn"] = control_panel_arn
        if control_panel_name is not None:
            input_["control_panel_name"] = control_panel_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_routing_control(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        routing_control_arn: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
        ] = None,
        routing_control_name: Optional[
            "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.update_routing_control_response.UpdateRoutingControlResponse":
        """<p>Updates a routing control. You can only update the name of the routing control. To get or update the routing control state, see the Recovery Cluster (data plane) API actions for Amazon Route 53 Application Recovery Controller.</p>

        Args:
            routing_control_arn: <p>The Amazon Resource Name (ARN) of the routing control.</p>
            routing_control_name: <p>The name of the routing control.</p>

        Raises:
            capo_route53_recovery_control_config.errors.access_denied_exception.AccessDeniedException: <p>403 response - You do not have sufficient access to perform this action.</p>
            capo_route53_recovery_control_config.errors.conflict_exception.ConflictException: <p>409 response - ConflictException. You might be using a predefined variable.</p>
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.throttling_exception.ThrottlingException: <p>429 response - LimitExceededException or TooManyRequestsException.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.update_routing_control_request.UpdateRoutingControlRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.update_routing_control_response.UpdateRoutingControlResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.update_routing_control

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.update_routing_control.async_update_routing_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.update_routing_control_request.UpdateRoutingControlRequest = {}
        if routing_control_arn is not None:
            input_["routing_control_arn"] = routing_control_arn
        if routing_control_name is not None:
            input_["routing_control_name"] = routing_control_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_safety_rule(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        assertion_rule_update: Optional[
            "capo_route53_recovery_control_config.types.assertion_rule_update.AssertionRuleUpdate"
        ] = None,
        gating_rule_update: Optional[
            "capo_route53_recovery_control_config.types.gating_rule_update.GatingRuleUpdate"
        ] = None,
    ) -> "capo_route53_recovery_control_config.types.update_safety_rule_response.UpdateSafetyRuleResponse":
        """<p>Update a safety rule (an assertion rule or gating rule). You can only update the name and the waiting period for a safety rule. To make other updates, delete the safety rule and create a new one.</p>

        Args:
            assertion_rule_update: <p>The assertion rule to update.</p>
            gating_rule_update: <p>The gating rule to update.</p>

        Raises:
            capo_route53_recovery_control_config.errors.internal_server_exception.InternalServerException: <p>500 response - InternalServiceError. Temporary service error. Retry the request.</p>
            capo_route53_recovery_control_config.errors.resource_not_found_exception.ResourceNotFoundException: <p>404 response - MalformedQueryString. The query string contains a syntax error or resource not found.</p>
            capo_route53_recovery_control_config.errors.validation_exception.ValidationException: <p>400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.</p>
            capo_route53_recovery_control_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53_recovery_control_config.types.update_safety_rule_request.UpdateSafetyRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53_recovery_control_config.types.update_safety_rule_response.UpdateSafetyRuleResponse"
        ]:
            import capo_route53_recovery_control_config._operations.route53_recovery_control_config.update_safety_rule

            (
                output,
                http_response,
            ) = await capo_route53_recovery_control_config._operations.route53_recovery_control_config.update_safety_rule.async_update_safety_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_control_config.types.update_safety_rule_request.UpdateSafetyRuleRequest = {}
        if assertion_rule_update is not None:
            input_["assertion_rule_update"] = assertion_rule_update
        if gating_rule_update is not None:
            input_["gating_rule_update"] = gating_rule_update

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
