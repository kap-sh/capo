"""Generated from Smithy shape ``com.amazonaws.vpclattice#MercuryControlPlane``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_vpc_lattice._auth._signers
import capo_vpc_lattice._auth._sigv4
from capo_vpc_lattice._auth._identity import Credentials
from capo_vpc_lattice._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_vpc_lattice._auth._zapros_handler import AuthMiddleware
from capo_vpc_lattice._pagination import resolve_path as _resolve_path
from capo_vpc_lattice._resources.mercury_control_plane.access_log_subscription import (
    AccessLogSubscription,
)
from capo_vpc_lattice._resources.mercury_control_plane.domain_verification import (
    DomainVerification,
)
from capo_vpc_lattice._resources.mercury_control_plane.listener import Listener
from capo_vpc_lattice._resources.mercury_control_plane.resource_configuration import (
    ResourceConfiguration,
)
from capo_vpc_lattice._resources.mercury_control_plane.resource_endpoint_association import (
    ResourceEndpointAssociation,
)
from capo_vpc_lattice._resources.mercury_control_plane.resource_gateway import (
    ResourceGateway,
)
from capo_vpc_lattice._resources.mercury_control_plane.rule import Rule
from capo_vpc_lattice._resources.mercury_control_plane.service import Service
from capo_vpc_lattice._resources.mercury_control_plane.service_load_balancer_association import (
    ServiceLoadBalancerAssociation,
)
from capo_vpc_lattice._resources.mercury_control_plane.service_network import (
    ServiceNetwork,
)
from capo_vpc_lattice._resources.mercury_control_plane.service_network_resource_association import (
    ServiceNetworkResourceAssociation,
)
from capo_vpc_lattice._resources.mercury_control_plane.service_network_service_association import (
    ServiceNetworkServiceAssociation,
)
from capo_vpc_lattice._resources.mercury_control_plane.service_network_vpc_association import (
    ServiceNetworkVpcAssociation,
)
from capo_vpc_lattice._resources.mercury_control_plane.target_group import TargetGroup
from capo_vpc_lattice._services._aws_config import aws_config
from capo_vpc_lattice._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_vpc_lattice.types.access_log_destination_arn
    import capo_vpc_lattice.types.access_log_subscription_identifier
    import capo_vpc_lattice.types.access_log_subscription_summary
    import capo_vpc_lattice.types.arn
    import capo_vpc_lattice.types.auth_policy_string
    import capo_vpc_lattice.types.auth_type
    import capo_vpc_lattice.types.batch_update_rule_request
    import capo_vpc_lattice.types.batch_update_rule_response
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.certificate_arn
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.create_access_log_subscription_request
    import capo_vpc_lattice.types.create_access_log_subscription_response
    import capo_vpc_lattice.types.create_listener_request
    import capo_vpc_lattice.types.create_listener_response
    import capo_vpc_lattice.types.create_resource_configuration_request
    import capo_vpc_lattice.types.create_resource_configuration_response
    import capo_vpc_lattice.types.create_resource_gateway_request
    import capo_vpc_lattice.types.create_resource_gateway_response
    import capo_vpc_lattice.types.create_rule_request
    import capo_vpc_lattice.types.create_rule_response
    import capo_vpc_lattice.types.create_service_network_request
    import capo_vpc_lattice.types.create_service_network_resource_association_request
    import capo_vpc_lattice.types.create_service_network_resource_association_response
    import capo_vpc_lattice.types.create_service_network_response
    import capo_vpc_lattice.types.create_service_network_service_association_request
    import capo_vpc_lattice.types.create_service_network_service_association_response
    import capo_vpc_lattice.types.create_service_network_vpc_association_request
    import capo_vpc_lattice.types.create_service_network_vpc_association_response
    import capo_vpc_lattice.types.create_service_request
    import capo_vpc_lattice.types.create_service_response
    import capo_vpc_lattice.types.create_target_group_request
    import capo_vpc_lattice.types.create_target_group_response
    import capo_vpc_lattice.types.delete_access_log_subscription_request
    import capo_vpc_lattice.types.delete_access_log_subscription_response
    import capo_vpc_lattice.types.delete_auth_policy_request
    import capo_vpc_lattice.types.delete_auth_policy_response
    import capo_vpc_lattice.types.delete_domain_verification_request
    import capo_vpc_lattice.types.delete_domain_verification_response
    import capo_vpc_lattice.types.delete_listener_request
    import capo_vpc_lattice.types.delete_listener_response
    import capo_vpc_lattice.types.delete_resource_configuration_request
    import capo_vpc_lattice.types.delete_resource_configuration_response
    import capo_vpc_lattice.types.delete_resource_endpoint_association_request
    import capo_vpc_lattice.types.delete_resource_endpoint_association_response
    import capo_vpc_lattice.types.delete_resource_gateway_request
    import capo_vpc_lattice.types.delete_resource_gateway_response
    import capo_vpc_lattice.types.delete_resource_policy_request
    import capo_vpc_lattice.types.delete_resource_policy_response
    import capo_vpc_lattice.types.delete_rule_request
    import capo_vpc_lattice.types.delete_rule_response
    import capo_vpc_lattice.types.delete_service_network_request
    import capo_vpc_lattice.types.delete_service_network_resource_association_request
    import capo_vpc_lattice.types.delete_service_network_resource_association_response
    import capo_vpc_lattice.types.delete_service_network_response
    import capo_vpc_lattice.types.delete_service_network_service_association_request
    import capo_vpc_lattice.types.delete_service_network_service_association_response
    import capo_vpc_lattice.types.delete_service_network_vpc_association_request
    import capo_vpc_lattice.types.delete_service_network_vpc_association_response
    import capo_vpc_lattice.types.delete_service_request
    import capo_vpc_lattice.types.delete_service_response
    import capo_vpc_lattice.types.delete_target_group_request
    import capo_vpc_lattice.types.delete_target_group_response
    import capo_vpc_lattice.types.deregister_targets_request
    import capo_vpc_lattice.types.deregister_targets_response
    import capo_vpc_lattice.types.dns_options
    import capo_vpc_lattice.types.domain_name
    import capo_vpc_lattice.types.domain_verification_identifier
    import capo_vpc_lattice.types.domain_verification_summary
    import capo_vpc_lattice.types.get_access_log_subscription_request
    import capo_vpc_lattice.types.get_access_log_subscription_response
    import capo_vpc_lattice.types.get_auth_policy_request
    import capo_vpc_lattice.types.get_auth_policy_response
    import capo_vpc_lattice.types.get_domain_verification_request
    import capo_vpc_lattice.types.get_domain_verification_response
    import capo_vpc_lattice.types.get_listener_request
    import capo_vpc_lattice.types.get_listener_response
    import capo_vpc_lattice.types.get_resource_configuration_request
    import capo_vpc_lattice.types.get_resource_configuration_response
    import capo_vpc_lattice.types.get_resource_gateway_request
    import capo_vpc_lattice.types.get_resource_gateway_response
    import capo_vpc_lattice.types.get_resource_policy_request
    import capo_vpc_lattice.types.get_resource_policy_response
    import capo_vpc_lattice.types.get_rule_request
    import capo_vpc_lattice.types.get_rule_response
    import capo_vpc_lattice.types.get_service_network_request
    import capo_vpc_lattice.types.get_service_network_resource_association_request
    import capo_vpc_lattice.types.get_service_network_resource_association_response
    import capo_vpc_lattice.types.get_service_network_response
    import capo_vpc_lattice.types.get_service_network_service_association_request
    import capo_vpc_lattice.types.get_service_network_service_association_response
    import capo_vpc_lattice.types.get_service_network_vpc_association_request
    import capo_vpc_lattice.types.get_service_network_vpc_association_response
    import capo_vpc_lattice.types.get_service_request
    import capo_vpc_lattice.types.get_service_response
    import capo_vpc_lattice.types.get_target_group_request
    import capo_vpc_lattice.types.get_target_group_response
    import capo_vpc_lattice.types.health_check_config
    import capo_vpc_lattice.types.idle_timeout_seconds
    import capo_vpc_lattice.types.ipv4_addresses_per_eni
    import capo_vpc_lattice.types.list_access_log_subscriptions_request
    import capo_vpc_lattice.types.list_access_log_subscriptions_response
    import capo_vpc_lattice.types.list_domain_verifications_request
    import capo_vpc_lattice.types.list_domain_verifications_response
    import capo_vpc_lattice.types.list_listeners_request
    import capo_vpc_lattice.types.list_listeners_response
    import capo_vpc_lattice.types.list_resource_configurations_request
    import capo_vpc_lattice.types.list_resource_configurations_response
    import capo_vpc_lattice.types.list_resource_endpoint_associations_request
    import capo_vpc_lattice.types.list_resource_endpoint_associations_response
    import capo_vpc_lattice.types.list_resource_gateways_request
    import capo_vpc_lattice.types.list_resource_gateways_response
    import capo_vpc_lattice.types.list_rules_request
    import capo_vpc_lattice.types.list_rules_response
    import capo_vpc_lattice.types.list_service_network_resource_associations_request
    import capo_vpc_lattice.types.list_service_network_resource_associations_response
    import capo_vpc_lattice.types.list_service_network_service_associations_request
    import capo_vpc_lattice.types.list_service_network_service_associations_response
    import capo_vpc_lattice.types.list_service_network_vpc_associations_request
    import capo_vpc_lattice.types.list_service_network_vpc_associations_response
    import capo_vpc_lattice.types.list_service_network_vpc_endpoint_associations_request
    import capo_vpc_lattice.types.list_service_network_vpc_endpoint_associations_response
    import capo_vpc_lattice.types.list_service_networks_request
    import capo_vpc_lattice.types.list_service_networks_response
    import capo_vpc_lattice.types.list_services_request
    import capo_vpc_lattice.types.list_services_response
    import capo_vpc_lattice.types.list_tags_for_resource_request
    import capo_vpc_lattice.types.list_tags_for_resource_response
    import capo_vpc_lattice.types.list_target_groups_request
    import capo_vpc_lattice.types.list_target_groups_response
    import capo_vpc_lattice.types.list_targets_request
    import capo_vpc_lattice.types.list_targets_response
    import capo_vpc_lattice.types.listener_identifier
    import capo_vpc_lattice.types.listener_name
    import capo_vpc_lattice.types.listener_protocol
    import capo_vpc_lattice.types.listener_summary
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.policy_string
    import capo_vpc_lattice.types.port
    import capo_vpc_lattice.types.port_range_list
    import capo_vpc_lattice.types.protocol_type
    import capo_vpc_lattice.types.put_auth_policy_request
    import capo_vpc_lattice.types.put_auth_policy_response
    import capo_vpc_lattice.types.put_resource_policy_request
    import capo_vpc_lattice.types.put_resource_policy_response
    import capo_vpc_lattice.types.register_targets_request
    import capo_vpc_lattice.types.register_targets_response
    import capo_vpc_lattice.types.resource_arn
    import capo_vpc_lattice.types.resource_config_dns_resolution
    import capo_vpc_lattice.types.resource_configuration_definition
    import capo_vpc_lattice.types.resource_configuration_identifier
    import capo_vpc_lattice.types.resource_configuration_name
    import capo_vpc_lattice.types.resource_configuration_summary
    import capo_vpc_lattice.types.resource_configuration_type
    import capo_vpc_lattice.types.resource_endpoint_association_identifier
    import capo_vpc_lattice.types.resource_endpoint_association_summary
    import capo_vpc_lattice.types.resource_gateway_identifier
    import capo_vpc_lattice.types.resource_gateway_ip_address_type
    import capo_vpc_lattice.types.resource_gateway_name
    import capo_vpc_lattice.types.resource_gateway_summary
    import capo_vpc_lattice.types.resource_identifier
    import capo_vpc_lattice.types.rule_action
    import capo_vpc_lattice.types.rule_identifier
    import capo_vpc_lattice.types.rule_match
    import capo_vpc_lattice.types.rule_name
    import capo_vpc_lattice.types.rule_priority
    import capo_vpc_lattice.types.rule_summary
    import capo_vpc_lattice.types.rule_update_list
    import capo_vpc_lattice.types.security_group_list
    import capo_vpc_lattice.types.service_custom_domain_name
    import capo_vpc_lattice.types.service_identifier
    import capo_vpc_lattice.types.service_name
    import capo_vpc_lattice.types.service_network_endpoint_association
    import capo_vpc_lattice.types.service_network_identifier
    import capo_vpc_lattice.types.service_network_identifier_without_regex
    import capo_vpc_lattice.types.service_network_log_type
    import capo_vpc_lattice.types.service_network_name
    import capo_vpc_lattice.types.service_network_resource_association_identifier
    import capo_vpc_lattice.types.service_network_resource_association_summary
    import capo_vpc_lattice.types.service_network_service_association_identifier
    import capo_vpc_lattice.types.service_network_service_association_summary
    import capo_vpc_lattice.types.service_network_summary
    import capo_vpc_lattice.types.service_network_vpc_association_identifier
    import capo_vpc_lattice.types.service_network_vpc_association_summary
    import capo_vpc_lattice.types.service_summary
    import capo_vpc_lattice.types.sharing_config
    import capo_vpc_lattice.types.start_domain_verification_request
    import capo_vpc_lattice.types.start_domain_verification_response
    import capo_vpc_lattice.types.subnet_list
    import capo_vpc_lattice.types.tag_keys
    import capo_vpc_lattice.types.tag_map
    import capo_vpc_lattice.types.tag_resource_request
    import capo_vpc_lattice.types.tag_resource_response
    import capo_vpc_lattice.types.target_group_config
    import capo_vpc_lattice.types.target_group_identifier
    import capo_vpc_lattice.types.target_group_name
    import capo_vpc_lattice.types.target_group_summary
    import capo_vpc_lattice.types.target_group_type
    import capo_vpc_lattice.types.target_list
    import capo_vpc_lattice.types.target_summary
    import capo_vpc_lattice.types.untag_resource_request
    import capo_vpc_lattice.types.untag_resource_response
    import capo_vpc_lattice.types.update_access_log_subscription_request
    import capo_vpc_lattice.types.update_access_log_subscription_response
    import capo_vpc_lattice.types.update_listener_request
    import capo_vpc_lattice.types.update_listener_response
    import capo_vpc_lattice.types.update_resource_configuration_request
    import capo_vpc_lattice.types.update_resource_configuration_response
    import capo_vpc_lattice.types.update_resource_gateway_request
    import capo_vpc_lattice.types.update_resource_gateway_response
    import capo_vpc_lattice.types.update_rule_request
    import capo_vpc_lattice.types.update_rule_response
    import capo_vpc_lattice.types.update_service_network_request
    import capo_vpc_lattice.types.update_service_network_response
    import capo_vpc_lattice.types.update_service_network_vpc_association_request
    import capo_vpc_lattice.types.update_service_network_vpc_association_response
    import capo_vpc_lattice.types.update_service_request
    import capo_vpc_lattice.types.update_service_response
    import capo_vpc_lattice.types.update_target_group_request
    import capo_vpc_lattice.types.update_target_group_response
    import capo_vpc_lattice.types.vpc_endpoint_id
    import capo_vpc_lattice.types.vpc_endpoint_owner
    import capo_vpc_lattice.types.vpc_id


class VPCLatticeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class VPCLatticeClient:
    """A client for the ``VPCLattice`` service.

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
        self._config = VPCLatticeClientConfig(
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
        self.access_log_subscription = AccessLogSubscription(self)
        self.domain_verification = DomainVerification(self)
        self.listener = Listener(self)
        self.resource_configuration = ResourceConfiguration(self)
        self.resource_endpoint_association = ResourceEndpointAssociation(self)
        self.resource_gateway = ResourceGateway(self)
        self.rule = Rule(self)
        self.service = Service(self)
        self.service_load_balancer_association = ServiceLoadBalancerAssociation(self)
        self.service_network = ServiceNetwork(self)
        self.service_network_resource_association = ServiceNetworkResourceAssociation(
            self
        )
        self.service_network_service_association = ServiceNetworkServiceAssociation(
            self
        )
        self.service_network_vpc_association = ServiceNetworkVpcAssociation(self)
        self.target_group = TargetGroup(self)

    def operation_options(
        self, config_overrides: Optional[VPCLatticeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: VPCLatticeClientConfig = config_overrides or {}
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

    def batch_update_rule(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rules: "capo_vpc_lattice.types.rule_update_list.RuleUpdateList",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.batch_update_rule_response.BatchUpdateRuleResponse":
        """<p>Updates the listener rules in a batch. You can use this operation to change the priority of listener rules. This can be useful when bulk updating or swapping rule priority.</p> <p> <b>Required permissions:</b> <code>vpc-lattice:UpdateRule</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/security_iam_service-with-iam.html">How Amazon VPC Lattice works with IAM</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rules: <p>The rules for the specified listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.batch_update_rule_request.BatchUpdateRuleRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.batch_update_rule_response.BatchUpdateRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.batch_update_rule

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.batch_update_rule.batch_update_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.batch_update_rule_request.BatchUpdateRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rules": rules,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_auth_policy(
        self,
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_auth_policy_response.DeleteAuthPolicyResponse":
        """<p>Deletes the specified auth policy. If an auth is set to <code>AWS_IAM</code> and the auth policy is deleted, all requests are denied. If you are trying to remove the auth policy completely, you must set the auth type to <code>NONE</code>. If auth is enabled on the resource, but no auth policy is set, all requests are denied.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the resource.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_auth_policy_request.DeleteAuthPolicyRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_auth_policy_response.DeleteAuthPolicyResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_auth_policy

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_auth_policy.delete_auth_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_auth_policy_request.DeleteAuthPolicyRequest = {
            "resource_identifier": resource_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "capo_vpc_lattice.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the specified resource policy.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_resource_policy

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_auth_policy(
        self,
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_auth_policy_response.GetAuthPolicyResponse":
        """<p>Retrieves information about the auth policy for the specified service or service network.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_auth_policy_request.GetAuthPolicyRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_auth_policy_response.GetAuthPolicyResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_auth_policy

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_auth_policy.get_auth_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_auth_policy_request.GetAuthPolicyRequest = {
            "resource_identifier": resource_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "capo_vpc_lattice.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> (
        "capo_vpc_lattice.types.get_resource_policy_response.GetResourcePolicyResponse"
    ):
        """<p>Retrieves information about the specified resource policy. The resource policy is an IAM policy created on behalf of the resource owner when they share a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the service network or service.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_resource_policy

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_service_network_vpc_endpoint_associations(
        self,
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_service_network_vpc_endpoint_associations_response.ListServiceNetworkVpcEndpointAssociationsResponse":
        """<p>Lists the associations between a service network and a VPC endpoint.</p>

        Args:
            service_network_identifier: <p>The ID of the service network associated with the VPC endpoint.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>If there are additional results, a pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_service_network_vpc_endpoint_associations_request.ListServiceNetworkVpcEndpointAssociationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_service_network_vpc_endpoint_associations_response.ListServiceNetworkVpcEndpointAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_endpoint_associations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_endpoint_associations.list_service_network_vpc_endpoint_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_service_network_vpc_endpoint_associations_request.ListServiceNetworkVpcEndpointAssociationsRequest = {
            "service_network_identifier": service_network_identifier
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

    def iter_list_service_network_vpc_endpoint_associations(
        self,
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.service_network_endpoint_association.ServiceNetworkEndpointAssociation]":
        _token = next_token
        while True:
            _response = self.list_service_network_vpc_endpoint_associations(
                service_network_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_vpc_lattice.types.arn.Arn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_tags_for_resource

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_auth_policy(
        self,
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        policy: "capo_vpc_lattice.types.auth_policy_string.AuthPolicyString",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.put_auth_policy_response.PutAuthPolicyResponse":
        """<p>Creates or updates the auth policy. The policy string in JSON must not contain newlines or blank lines.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html">Auth policies</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service for which the policy is created.</p>
            policy: <p>The auth policy. The policy string in JSON must not contain newlines or blank lines.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.put_auth_policy_request.PutAuthPolicyRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.put_auth_policy_response.PutAuthPolicyResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.put_auth_policy

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.put_auth_policy.put_auth_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.put_auth_policy_request.PutAuthPolicyRequest = {
            "resource_identifier": resource_identifier,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "capo_vpc_lattice.types.resource_arn.ResourceArn",
        policy: "capo_vpc_lattice.types.policy_string.PolicyString",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> (
        "capo_vpc_lattice.types.put_resource_policy_response.PutResourcePolicyResponse"
    ):
        """<p>Attaches a resource-based permission policy to a service or service network. The policy must contain the same actions and condition statements as the Amazon Web Services Resource Access Manager permission for sharing services and service networks.</p>

        Args:
            resource_arn: <p>The ID or ARN of the service network or service for which the policy is created.</p>
            policy: <p>An IAM policy. The policy string in JSON must not contain newlines or blank lines.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.put_resource_policy

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
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
        resource_arn: "capo_vpc_lattice.types.arn.Arn",
        tags: "capo_vpc_lattice.types.tag_map.TagMap",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags for the resource.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.tag_resource

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_vpc_lattice.types.arn.Arn",
        tag_keys: "capo_vpc_lattice.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys of the tags to remove.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.untag_resource

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.untag_resource_request.UntagResourceRequest = {
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

    def create_access_log_subscription(
        self,
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        destination_arn: "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        service_network_log_type: Optional[
            "capo_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse":
        """<p>Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner can only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html">Access logs</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.</p>
            service_network_log_type: <p>The type of log that monitors your Amazon VPC Lattice service networks.</p>
            tags: <p>The tags for the access log subscription.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription.create_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest = {
            "resource_identifier": resource_identifier,
            "destination_arn": destination_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if service_network_log_type is not None:
            input_["service_network_log_type"] = service_network_log_type
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_access_log_subscription(
        self,
        access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse":
        """<p>Retrieves information about the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription.get_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest = {
            "access_log_subscription_identifier": access_log_subscription_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_access_log_subscription(
        self,
        access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        destination_arn: "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse":
        """<p>Updates the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the access log destination.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription.update_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest = {
            "access_log_subscription_identifier": access_log_subscription_identifier,
            "destination_arn": destination_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_access_log_subscription(
        self,
        access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse":
        """<p>Deletes the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription.delete_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest = {
            "access_log_subscription_identifier": access_log_subscription_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_access_log_subscriptions(
        self,
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse":
        """<p>Lists the access log subscriptions for the specified service network or service.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions.list_access_log_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest = {
            "resource_identifier": resource_identifier
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

    def iter_list_access_log_subscriptions(
        self,
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.access_log_subscription_summary.AccessLogSubscriptionSummary]":
        _token = next_token
        while True:
            _response = self.list_access_log_subscriptions(
                resource_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_domain_verification(
        self,
        domain_name: "capo_vpc_lattice.types.domain_name.DomainName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse":
        """<p> Starts the domain verification process for a custom domain name. </p>

        Args:
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails. </p>
            domain_name: <p> The domain name to verify ownership for. </p>
            tags: <p> The tags for the domain verification. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.start_domain_verification

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.start_domain_verification.start_domain_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest = {
            "domain_name": domain_name
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

    def get_domain_verification(
        self,
        domain_verification_identifier: "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse":
        """<p> Retrieves information about a domain verification.ß </p>

        Args:
            domain_verification_identifier: <p> The ID or ARN of the domain verification to retrieve. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_domain_verification

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_domain_verification.get_domain_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest = {
            "domain_verification_identifier": domain_verification_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain_verification(
        self,
        domain_verification_identifier: "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse":
        """<p> Deletes the specified domain verification. </p>

        Args:
            domain_verification_identifier: <p> The ID of the domain verification to delete. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_domain_verification

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_domain_verification.delete_domain_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest = {
            "domain_verification_identifier": domain_verification_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_domain_verifications(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse":
        """<p> Lists the domain verifications. </p>

        Args:
            max_results: <p> The maximum number of results to return. </p>
            next_token: <p> A pagination token for the next page of results. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_domain_verifications

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_domain_verifications.list_domain_verifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest = {}
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

    def iter_list_domain_verifications(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.domain_verification_summary.DomainVerificationSummary]":
        _token = next_token
        while True:
            _response = self.list_domain_verifications(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_listener(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        name: "capo_vpc_lattice.types.listener_name.ListenerName",
        protocol: "capo_vpc_lattice.types.listener_protocol.ListenerProtocol",
        default_action: "capo_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        port: Optional["capo_vpc_lattice.types.port.Port"] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_listener_response.CreateListenerResponse":
        """<p>Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html">Listeners</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            name: <p>The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            protocol: <p>The listener protocol.</p>
            port: <p>The listener port. You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.</p>
            default_action: <p>The action for the default rule. Each listener has a default rule. The default rule is used if no other rules match.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_listener_request.CreateListenerRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_listener_response.CreateListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_listener

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_listener.create_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_listener_request.CreateListenerRequest = {
            "service_identifier": service_identifier,
            "name": name,
            "protocol": protocol,
            "default_action": default_action,
        }
        if port is not None:
            input_["port"] = port
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

    def get_listener(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_listener_response.GetListenerResponse":
        """<p>Retrieves information about the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_listener_request.GetListenerRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_listener_response.GetListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_listener

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_listener.get_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_listener_request.GetListenerRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_listener(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        default_action: "capo_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.update_listener_response.UpdateListenerResponse":
        """<p>Updates the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            default_action: <p>The action for the default rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_listener_request.UpdateListenerRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_listener_response.UpdateListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_listener

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_listener.update_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_listener_request.UpdateListenerRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "default_action": default_action,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_listener(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_listener_response.DeleteListenerResponse":
        """<p>Deletes the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_listener_request.DeleteListenerRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_listener_response.DeleteListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_listener

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_listener.delete_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_listener_request.DeleteListenerRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_listeners(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_listeners_response.ListListenersResponse":
        """<p>Lists the listeners for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_listeners_request.ListListenersRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_listeners_response.ListListenersResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_listeners

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_listeners.list_listeners(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_listeners_request.ListListenersRequest = {
            "service_identifier": service_identifier
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

    def iter_list_listeners(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.listener_summary.ListenerSummary]":
        _token = next_token
        while True:
            _response = self.list_listeners(
                service_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_resource_configuration(
        self,
        name: "capo_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName",
        type: "capo_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        port_ranges: Optional[
            "capo_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
        protocol: Optional["capo_vpc_lattice.types.protocol_type.ProtocolType"] = None,
        resource_gateway_identifier: Optional[
            "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        resource_configuration_definition: Optional[
            "capo_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "capo_vpc_lattice.types.boolean.Boolean"
        ] = None,
        custom_domain_name: Optional[
            "capo_vpc_lattice.types.domain_name.DomainName"
        ] = None,
        group_domain: Optional["capo_vpc_lattice.types.domain_name.DomainName"] = None,
        domain_verification_identifier: Optional[
            "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse":
        """<p>Creates a resource configuration. A resource configuration defines a specific resource. You can associate a resource configuration with a service network or a VPC endpoint.</p>

        Args:
            name: <p>The name of the resource configuration. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            type: <p>The type of resource configuration. A resource configuration can be one of the following types:</p> <ul> <li> <p> <b>SINGLE</b> - A single resource.</p> </li> <li> <p> <b>GROUP</b> - A group of resources. You must create a group resource configuration before you create a child resource configuration.</p> </li> <li> <p> <b>CHILD</b> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <b>ARN</b> - An Amazon Web Services resource.</p> </li> <li> <p> <b>CIDR</b> - A network segment, expressed as a range of IP addresses (a CIDR block). Use this type to share a portion of your network rather than an individual resource. A consumer accesses the resources within the CIDR range through a <code>Tunnel</code> VPC endpoint. You can't add a CIDR resource configuration to a service network. A CIDR resource configuration must be associated with a resource gateway whose DNS resolution is set to <code>IN_VPC</code>.</p> </li> </ul>
            port_ranges: <p>(SINGLE, GROUP, CHILD, CIDR) The port ranges that a consumer can use to access a resource configuration (for example: 1-65535). You can separate port ranges using commas (for example: 1,2,22-30). To resolve DNS through a CIDR resource configuration, include port 53 in the port ranges.</p>
            protocol: <p>(SINGLE, GROUP, CIDR) The protocol accepted by the resource configuration. The default is <code>TCP</code>. <code>TCP_UDP</code> is supported only for CIDR resource configurations; specify it for a CIDR resource configuration to allow DNS resolution, which uses UDP.</p>
            resource_gateway_identifier: <p>(SINGLE, GROUP, ARN, CIDR) The ID or ARN of the resource gateway used to connect to the resource configuration. For a child resource configuration, this value is inherited from the parent resource configuration. For a CIDR resource configuration, the associated resource gateway must have its DNS resolution set to <code>IN_VPC</code> so that DNS queries resolve in the context of your VPC.</p>
            resource_configuration_group_identifier: <p>(CHILD) The ID or ARN of the parent resource configuration of type <code>GROUP</code>. This is used to associate a child resource configuration with a group resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> <li> <p> <b>CIDR range</b> - For a resource configuration of type CIDR, specify a <code>cidrResource</code> with one or more <code>cidrRanges</code> (for example, <code>10.0.0.0/16</code>) that cover the IP addresses of the resources you want to make accessible. You can specify up to 10 ranges, using IPv4, IPv6, or both, and each range must include a prefix length. To represent your entire network, specify <code>0.0.0.0/0</code> (IPv4) or <code>::/0</code> (IPv6) as the only range. You can't use reserved ranges such as <code>169.254.0.0/16</code>, <code>100.64.0.0/10</code>, <code>224.0.0.0/4</code>, <code>fe80::/10</code>, or <code>ff00::/8</code>.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>(SINGLE, GROUP, ARN) Specifies whether the resource configuration can be associated with a sharable service network. The default is false.</p>
            custom_domain_name: <p> A custom domain name for your resource configuration. Additionally, provide a DomainVerificationID to prove your ownership of a domain. </p>
            group_domain: <p> (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain. </p>
            domain_verification_identifier: <p> The domain verification ID of your verified custom domain name. If you don't provide an ID, you must configure the DNS settings yourself. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the resource configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_resource_configuration

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_resource_configuration.create_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest = {
            "name": name,
            "type": type,
        }
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges
        if protocol is not None:
            input_["protocol"] = protocol
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if group_domain is not None:
            input_["group_domain"] = group_domain
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
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

    def get_resource_configuration(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse":
        """<p>Retrieves information about the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_resource_configuration

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_resource_configuration.get_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resource_configuration(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_configuration_definition: Optional[
            "capo_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "capo_vpc_lattice.types.boolean.Boolean"
        ] = None,
        port_ranges: Optional[
            "capo_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
    ) -> "capo_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse":
        """<p>Updates the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>Indicates whether to add the resource configuration to service networks that are shared with other accounts.</p>
            port_ranges: <p>The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_resource_configuration

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_resource_configuration.update_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
        }
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_configuration(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse":
        """<p>Deletes the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID or ARN of the resource configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration.delete_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_resource_configurations(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_gateway_identifier: Optional[
            "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        domain_verification_identifier: Optional[
            "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse":
        """<p>Lists the resource configurations owned by or shared with this account.</p>

        Args:
            resource_gateway_identifier: <p>The ID of the resource gateway for the resource configuration.</p>
            resource_configuration_group_identifier: <p>The ID of the resource configuration of type <code>Group</code>.</p>
            domain_verification_identifier: <p> The domain verification ID. </p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_resource_configurations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_resource_configurations.list_resource_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest = {}
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
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

    def iter_list_resource_configurations(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_gateway_identifier: Optional[
            "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        domain_verification_identifier: Optional[
            "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.resource_configuration_summary.ResourceConfigurationSummary]":
        _token = next_token
        while True:
            _response = self.list_resource_configurations(
                config_overrides=config_overrides,
                resource_gateway_identifier=resource_gateway_identifier,
                resource_configuration_group_identifier=resource_configuration_group_identifier,
                domain_verification_identifier=domain_verification_identifier,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def delete_resource_endpoint_association(
        self,
        resource_endpoint_association_identifier: "capo_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse":
        """<p>Disassociates the resource configuration from the resource VPC endpoint.</p>

        Args:
            resource_endpoint_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association.delete_resource_endpoint_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest = {
            "resource_endpoint_association_identifier": resource_endpoint_association_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_resource_endpoint_associations(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_endpoint_association_identifier: Optional[
            "capo_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_vpc_lattice.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        vpc_endpoint_owner: Optional[
            "capo_vpc_lattice.types.vpc_endpoint_owner.VpcEndpointOwner"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse":
        """<p>Lists the associations for the specified VPC endpoint.</p>

        Args:
            resource_configuration_identifier: <p>The ID for the resource configuration associated with the VPC endpoint.</p>
            resource_endpoint_association_identifier: <p>The ID of the association.</p>
            vpc_endpoint_id: <p>The ID of the VPC endpoint in the association.</p>
            vpc_endpoint_owner: <p>The owner of the VPC endpoint in the association.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations.list_resource_endpoint_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
        }
        if resource_endpoint_association_identifier is not None:
            input_["resource_endpoint_association_identifier"] = (
                resource_endpoint_association_identifier
            )
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if vpc_endpoint_owner is not None:
            input_["vpc_endpoint_owner"] = vpc_endpoint_owner
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

    def iter_list_resource_endpoint_associations(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_endpoint_association_identifier: Optional[
            "capo_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_vpc_lattice.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        vpc_endpoint_owner: Optional[
            "capo_vpc_lattice.types.vpc_endpoint_owner.VpcEndpointOwner"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.resource_endpoint_association_summary.ResourceEndpointAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_resource_endpoint_associations(
                resource_configuration_identifier,
                config_overrides=config_overrides,
                resource_endpoint_association_identifier=resource_endpoint_association_identifier,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_endpoint_owner=vpc_endpoint_owner,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_resource_gateway(
        self,
        name: "capo_vpc_lattice.types.resource_gateway_name.ResourceGatewayName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        vpc_identifier: Optional["capo_vpc_lattice.types.vpc_id.VpcId"] = None,
        subnet_ids: Optional["capo_vpc_lattice.types.subnet_list.SubnetList"] = None,
        security_group_ids: Optional[
            "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
        ip_address_type: Optional[
            "capo_vpc_lattice.types.resource_gateway_ip_address_type.ResourceGatewayIpAddressType"
        ] = None,
        ipv4_addresses_per_eni: Optional[
            "capo_vpc_lattice.types.ipv4_addresses_per_eni.Ipv4AddressesPerEni"
        ] = None,
        resource_config_dns_resolution: Optional[
            "capo_vpc_lattice.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_resource_gateway_response.CreateResourceGatewayResponse":
        """<p>A resource gateway is a point of ingress into the VPC where a resource resides. It spans multiple Availability Zones. For your resource to be accessible from all Availability Zones, you should create your resource gateways to span as many Availability Zones as possible. A VPC can have multiple resource gateways.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the resource gateway.</p>
            vpc_identifier: <p>The ID of the VPC for the resource gateway.</p>
            subnet_ids: <p>The IDs of the VPC subnets in which to create the resource gateway.</p>
            security_group_ids: <p>The IDs of the security groups to apply to the resource gateway. The security groups must be in the same VPC.</p>
            ip_address_type: <p>A resource gateway can have IPv4, IPv6 or dualstack addresses. The IP address type of a resource gateway must be compatible with the subnets of the resource gateway and the IP address type of the resource, as described here: </p> <ul> <li> <p> <b>IPv4</b>Assign IPv4 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have IPv4 address ranges, and the resource also has an IPv4 address.</p> </li> <li> <p> <b>IPv6</b>Assign IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets are IPv6 only subnets, and the resource also has an IPv6 address.</p> </li> <li> <p> <b>Dualstack</b>Assign both IPv4 and IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges, and the resource either has an IPv4 or IPv6 address.</p> </li> </ul> <p>The IP address type of the resource gateway is independent of the IP address type of the client or the VPC endpoint through which the resource is accessed.</p>
            ipv4_addresses_per_eni: <p>The number of IPv4 addresses in each ENI for the resource gateway.</p>
            resource_config_dns_resolution: <p>Indicates how DNS is resolved for resource configurations associated with this resource gateway. This value is set when you create the resource gateway and can't be changed afterward. The default is <code>PUBLIC</code>.</p> <ul> <li> <p> <code>IN_VPC</code> - DNS resolution occurs privately within the resource gateway's VPC. DNS queries for resources behind this resource gateway resolve using the DNS resolvers defined in the VPC's DHCP option sets. Use this when your resource domain names are hosted in private Route 53 hosted zones or on-premises DNS servers reachable from the VPC. A CIDR resource configuration requires a resource gateway that uses <code>IN_VPC</code>, and an <code>IN_VPC</code> resource gateway can't be used for ARN resource configurations, so a single resource gateway can't serve both ARN and CIDR resource configurations.</p> </li> <li> <p> <code>PUBLIC</code> - DNS resolution occurs against public DNS resolvers. DNS queries for resources behind this resource gateway resolve using standard public DNS. Use this when your resource domain names are publicly resolvable.</p> </li> </ul>
            tags: <p>The tags for the resource gateway.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_resource_gateway_request.CreateResourceGatewayRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_resource_gateway_response.CreateResourceGatewayResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_resource_gateway

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_resource_gateway.create_resource_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_resource_gateway_request.CreateResourceGatewayRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if vpc_identifier is not None:
            input_["vpc_identifier"] = vpc_identifier
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if ipv4_addresses_per_eni is not None:
            input_["ipv4_addresses_per_eni"] = ipv4_addresses_per_eni
        if resource_config_dns_resolution is not None:
            input_["resource_config_dns_resolution"] = resource_config_dns_resolution
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_gateway(
        self,
        resource_gateway_identifier: "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_resource_gateway_response.GetResourceGatewayResponse":
        """<p>Retrieves information about the specified resource gateway.</p>

        Args:
            resource_gateway_identifier: <p>The ID of the resource gateway.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_resource_gateway_request.GetResourceGatewayRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_resource_gateway_response.GetResourceGatewayResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_resource_gateway

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_resource_gateway.get_resource_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_resource_gateway_request.GetResourceGatewayRequest = {
            "resource_gateway_identifier": resource_gateway_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resource_gateway(
        self,
        resource_gateway_identifier: "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        security_group_ids: Optional[
            "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
    ) -> "capo_vpc_lattice.types.update_resource_gateway_response.UpdateResourceGatewayResponse":
        """<p>Updates the specified resource gateway.</p>

        Args:
            resource_gateway_identifier: <p>The ID or ARN of the resource gateway.</p>
            security_group_ids: <p>The IDs of the security groups associated with the resource gateway.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_resource_gateway_request.UpdateResourceGatewayRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_resource_gateway_response.UpdateResourceGatewayResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_resource_gateway

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_resource_gateway.update_resource_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_resource_gateway_request.UpdateResourceGatewayRequest = {
            "resource_gateway_identifier": resource_gateway_identifier
        }
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_gateway(
        self,
        resource_gateway_identifier: "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_resource_gateway_response.DeleteResourceGatewayResponse":
        """<p>Deletes the specified resource gateway.</p>

        Args:
            resource_gateway_identifier: <p>The ID or ARN of the resource gateway.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_resource_gateway_request.DeleteResourceGatewayRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_resource_gateway_response.DeleteResourceGatewayResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_resource_gateway

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_resource_gateway.delete_resource_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_resource_gateway_request.DeleteResourceGatewayRequest = {
            "resource_gateway_identifier": resource_gateway_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_resource_gateways(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_resource_gateways_response.ListResourceGatewaysResponse":
        """<p>Lists the resource gateways that you own or that were shared with you.</p>

        Args:
            max_results: <p>The maximum page size.</p>
            next_token: <p>If there are additional results, a pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_resource_gateways_request.ListResourceGatewaysRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_resource_gateways_response.ListResourceGatewaysResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_resource_gateways

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_resource_gateways.list_resource_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_resource_gateways_request.ListResourceGatewaysRequest = {}
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

    def iter_list_resource_gateways(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.resource_gateway_summary.ResourceGatewaySummary]":
        _token = next_token
        while True:
            _response = self.list_resource_gateways(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_rule(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        name: "capo_vpc_lattice.types.rule_name.RuleName",
        match: "capo_vpc_lattice.types.rule_match.RuleMatch",
        priority: "capo_vpc_lattice.types.rule_priority.RulePriority",
        action: "capo_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_rule_response.CreateRuleResponse":
        """<p>Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            name: <p>The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            match: <p>The rule match.</p>
            priority: <p>The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.</p>
            action: <p>The action for the default rule.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_rule_request.CreateRuleRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_rule_response.CreateRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_rule

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_rule.create_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_rule_request.CreateRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "name": name,
            "match": match,
            "priority": priority,
            "action": action,
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

    def get_rule(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_rule_response.GetRuleResponse":
        """<p>Retrieves information about the specified listener rules. You can also retrieve information about the default listener rule. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the listener rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_rule_request.GetRuleRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_rule_response.GetRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_rule

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_rule.get_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_rule_request.GetRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rule_identifier": rule_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rule(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        match: Optional["capo_vpc_lattice.types.rule_match.RuleMatch"] = None,
        priority: Optional["capo_vpc_lattice.types.rule_priority.RulePriority"] = None,
        action: Optional["capo_vpc_lattice.types.rule_action.RuleAction"] = None,
    ) -> "capo_vpc_lattice.types.update_rule_response.UpdateRuleResponse":
        """<p>Updates a specified rule for the listener. You can't modify a default listener rule. To modify a default listener rule, use <code>UpdateListener</code>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>
            match: <p>The rule match.</p>
            priority: <p>The rule priority. A listener can't have multiple rules with the same priority.</p>
            action: <p>Information about the action for the specified listener rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_rule_request.UpdateRuleRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_rule_response.UpdateRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_rule

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_rule.update_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_rule_request.UpdateRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rule_identifier": rule_identifier,
        }
        if match is not None:
            input_["match"] = match
        if priority is not None:
            input_["priority"] = priority
        if action is not None:
            input_["action"] = action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_rule(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_rule_response.DeleteRuleResponse":
        """<p>Deletes a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. You can delete additional listener rules, but you cannot delete the default rule.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_rule_request.DeleteRuleRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_rule_response.DeleteRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_rule

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_rule.delete_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_rule_request.DeleteRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rule_identifier": rule_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_rules(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_rules_response.ListRulesResponse":
        """<p>Lists the rules for the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_rules_request.ListRulesRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_rules_response.ListRulesResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_rules

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_rules.list_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_rules_request.ListRulesRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
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

    def iter_list_rules(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.rule_summary.RuleSummary]":
        _token = next_token
        while True:
            _response = self.list_rules(
                service_identifier,
                listener_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_service(
        self,
        name: "capo_vpc_lattice.types.service_name.ServiceName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
        custom_domain_name: Optional[
            "capo_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
        ] = None,
        certificate_arn: Optional[
            "capo_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["capo_vpc_lattice.types.auth_type.AuthType"] = None,
        idle_timeout_seconds: Optional[
            "capo_vpc_lattice.types.idle_timeout_seconds.IdleTimeoutSeconds"
        ] = None,
    ) -> "capo_vpc_lattice.types.create_service_response.CreateServiceResponse":
        """<p>Creates a service. A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html">Services</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            tags: <p>The tags for the service.</p>
            custom_domain_name: <p>The custom domain name of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
            idle_timeout_seconds: <p>The amount of time, in seconds, that a connection can remain idle (no data sent) before VPC Lattice closes it. The valid range is 60 to 600 seconds. If you don't specify a value, the default is 60 seconds. This setting does not change the maximum connection duration of 10 minutes; connections are still closed when they reach that limit.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_service_request.CreateServiceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_service_request.CreateServiceRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if idle_timeout_seconds is not None:
            input_["idle_timeout_seconds"] = idle_timeout_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_response.GetServiceResponse":
        """<p>Retrieves information about the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_service_request.GetServiceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_service_response.GetServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_service_request.GetServiceRequest = {
            "service_identifier": service_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        certificate_arn: Optional[
            "capo_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["capo_vpc_lattice.types.auth_type.AuthType"] = None,
        idle_timeout_seconds: Optional[
            "capo_vpc_lattice.types.idle_timeout_seconds.IdleTimeoutSeconds"
        ] = None,
    ) -> "capo_vpc_lattice.types.update_service_response.UpdateServiceResponse":
        """<p>Updates the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
            idle_timeout_seconds: <p>The amount of time, in seconds, that a connection can remain idle (no data sent) before VPC Lattice closes it. The valid range is 60 to 600 seconds. If you don't specify a value, the default is 60 seconds. This setting does not change the maximum connection duration of 10 minutes; connections are still closed when they reach that limit.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_service_request.UpdateServiceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_service_response.UpdateServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_service

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_service.update_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_service_request.UpdateServiceRequest = {
            "service_identifier": service_identifier
        }
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if idle_timeout_seconds is not None:
            input_["idle_timeout_seconds"] = idle_timeout_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes a service. A service can't be deleted if it's associated with a service network. If you delete a service, all resources related to the service, such as the resource policy, auth policy, listeners, listener rules, and access log subscriptions, are also deleted. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html#delete-service">Delete a service</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_service_request.DeleteServiceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_service_request.DeleteServiceRequest = {
            "service_identifier": service_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_services(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_services_response.ListServicesResponse":
        """<p>Lists the services owned by the caller account or shared with the caller account.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_services_request.ListServicesRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_services_response.ListServicesResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_services

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_services_request.ListServicesRequest = {}
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

    def iter_list_services(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.service_summary.ServiceSummary]":
        _token = next_token
        while True:
            _response = self.list_services(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_service_network(
        self,
        name: "capo_vpc_lattice.types.service_network_name.ServiceNetworkName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        auth_type: Optional["capo_vpc_lattice.types.auth_type.AuthType"] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
        sharing_config: Optional[
            "capo_vpc_lattice.types.sharing_config.SharingConfig"
        ] = None,
    ) -> "capo_vpc_lattice.types.create_service_network_response.CreateServiceNetworkResponse":
        """<p>Creates a service network. A service network is a logical boundary for a collection of services. You can associate services and VPCs with a service network.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html">Service networks</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the service network. The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
            tags: <p>The tags for the service network.</p>
            sharing_config: <p>Specify if the service network should be enabled for sharing.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_service_network_request.CreateServiceNetworkRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_service_network_response.CreateServiceNetworkResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service_network

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_service_network.create_service_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_service_network_request.CreateServiceNetworkRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if tags is not None:
            input_["tags"] = tags
        if sharing_config is not None:
            input_["sharing_config"] = sharing_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service_network(
        self,
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> (
        "capo_vpc_lattice.types.get_service_network_response.GetServiceNetworkResponse"
    ):
        """<p>Retrieves information about the specified service network.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_service_network_request.GetServiceNetworkRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_service_network_response.GetServiceNetworkResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service_network

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_service_network.get_service_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_service_network_request.GetServiceNetworkRequest = {
            "service_network_identifier": service_network_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_network(
        self,
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        auth_type: "capo_vpc_lattice.types.auth_type.AuthType",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.update_service_network_response.UpdateServiceNetworkResponse":
        """<p>Updates the specified service network.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_service_network_request.UpdateServiceNetworkRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_service_network_response.UpdateServiceNetworkResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_service_network

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_service_network.update_service_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_service_network_request.UpdateServiceNetworkRequest = {
            "service_network_identifier": service_network_identifier,
            "auth_type": auth_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_network(
        self,
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_network_response.DeleteServiceNetworkResponse":
        """<p>Deletes a service network. You can only delete the service network if there is no service or VPC associated with it. If you delete a service network, all resources related to the service network, such as the resource policy, auth policy, and access log subscriptions, are also deleted. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html#delete-service-network">Delete a service network</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_service_network_request.DeleteServiceNetworkRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_service_network_response.DeleteServiceNetworkResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service_network

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_service_network.delete_service_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_service_network_request.DeleteServiceNetworkRequest = {
            "service_network_identifier": service_network_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_service_networks(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_service_networks_response.ListServiceNetworksResponse":
        """<p>Lists the service networks owned by or shared with this account. The account ID in the ARN shows which account owns the service network.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_service_networks_request.ListServiceNetworksRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_service_networks_response.ListServiceNetworksResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_service_networks

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_service_networks.list_service_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_service_networks_request.ListServiceNetworksRequest = {}
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

    def iter_list_service_networks(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> (
        "Iterator[capo_vpc_lattice.types.service_network_summary.ServiceNetworkSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_service_networks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_service_network_resource_association(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier_without_regex.ServiceNetworkIdentifierWithoutRegex",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        private_dns_enabled: Optional["capo_vpc_lattice.types.boolean.Boolean"] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_service_network_resource_association_response.CreateServiceNetworkResourceAssociationResponse":
        """<p>Associates the specified service network with the specified resource configuration. This allows the resource configuration to receive connections through the service network, including through a service network VPC endpoint.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            resource_configuration_identifier: <p>The ID of the resource configuration to associate with the service network.</p>
            service_network_identifier: <p>The ID of the service network to associate with the resource configuration.</p>
            private_dns_enabled: <p> Indicates if private DNS is enabled for the service network resource association. </p>
            tags: <p>A key-value pair to associate with a resource.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_service_network_resource_association_request.CreateServiceNetworkResourceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_service_network_resource_association_response.CreateServiceNetworkResourceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service_network_resource_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_service_network_resource_association.create_service_network_resource_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_service_network_resource_association_request.CreateServiceNetworkResourceAssociationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier,
            "service_network_identifier": service_network_identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if private_dns_enabled is not None:
            input_["private_dns_enabled"] = private_dns_enabled
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service_network_resource_association(
        self,
        service_network_resource_association_identifier: "capo_vpc_lattice.types.service_network_resource_association_identifier.ServiceNetworkResourceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_network_resource_association_response.GetServiceNetworkResourceAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a resource configuration.</p>

        Args:
            service_network_resource_association_identifier: <p>The ID of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_service_network_resource_association_request.GetServiceNetworkResourceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_service_network_resource_association_response.GetServiceNetworkResourceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service_network_resource_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_service_network_resource_association.get_service_network_resource_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_service_network_resource_association_request.GetServiceNetworkResourceAssociationRequest = {
            "service_network_resource_association_identifier": service_network_resource_association_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_network_resource_association(
        self,
        service_network_resource_association_identifier: "capo_vpc_lattice.types.service_network_resource_association_identifier.ServiceNetworkResourceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_network_resource_association_response.DeleteServiceNetworkResourceAssociationResponse":
        """<p>Deletes the association between a service network and a resource configuration.</p>

        Args:
            service_network_resource_association_identifier: <p>The ID of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_service_network_resource_association_request.DeleteServiceNetworkResourceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_service_network_resource_association_response.DeleteServiceNetworkResourceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_resource_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_resource_association.delete_service_network_resource_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_service_network_resource_association_request.DeleteServiceNetworkResourceAssociationRequest = {
            "service_network_resource_association_identifier": service_network_resource_association_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_service_network_resource_associations(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        service_network_identifier: Optional[
            "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        resource_configuration_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
        include_children: Optional[bool] = None,
    ) -> "capo_vpc_lattice.types.list_service_network_resource_associations_response.ListServiceNetworkResourceAssociationsResponse":
        """<p>Lists the associations between a service network and a resource configuration.</p>

        Args:
            service_network_identifier: <p>The ID of the service network.</p>
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>If there are additional results, a pagination token for the next page of results.</p>
            include_children: <p>Include service network resource associations of the child resource configuration with the grouped resource configuration.</p> <p>The type is boolean and the default value is false.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_service_network_resource_associations_request.ListServiceNetworkResourceAssociationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_service_network_resource_associations_response.ListServiceNetworkResourceAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_service_network_resource_associations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_service_network_resource_associations.list_service_network_resource_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_service_network_resource_associations_request.ListServiceNetworkResourceAssociationsRequest = {}
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if resource_configuration_identifier is not None:
            input_["resource_configuration_identifier"] = (
                resource_configuration_identifier
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_children is not None:
            input_["include_children"] = include_children

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_service_network_resource_associations(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        service_network_identifier: Optional[
            "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        resource_configuration_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
        include_children: Optional[bool] = None,
    ) -> "Iterator[capo_vpc_lattice.types.service_network_resource_association_summary.ServiceNetworkResourceAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_service_network_resource_associations(
                config_overrides=config_overrides,
                service_network_identifier=service_network_identifier,
                resource_configuration_identifier=resource_configuration_identifier,
                max_results=max_results,
                next_token=_token,
                include_children=include_children,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_service_network_service_association(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse":
        """<p>Associates the specified service with the specified service network. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations">Manage service associations</a> in the <i>Amazon VPC Lattice User Guide</i>.</p> <p>You can't use this operation if the service and service network are already associated or if there is a disassociation or deletion in progress. If the association fails, you can retry the operation by deleting the association and recreating it.</p> <p>You cannot associate a service and service network that are shared with a caller. The caller must own either the service or the service network.</p> <p>As a result of this operation, the association is created in the service network account and the association owner account.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
            service_network_identifier: <p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>
            tags: <p>The tags for the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association.create_service_network_service_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest = {
            "service_identifier": service_identifier,
            "service_network_identifier": service_network_identifier,
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

    def get_service_network_service_association(
        self,
        service_network_service_association_identifier: "capo_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a service.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association.get_service_network_service_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest = {
            "service_network_service_association_identifier": service_network_service_association_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_network_service_association(
        self,
        service_network_service_association_identifier: "capo_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse":
        """<p>Deletes the association between a service and a service network. This operation fails if an association is still in progress.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association.delete_service_network_service_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest = {
            "service_network_service_association_identifier": service_network_service_association_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_service_network_service_associations(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        service_network_identifier: Optional[
            "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        service_identifier: Optional[
            "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse":
        """<p>Lists the associations between a service network and a service. You can filter the list either by service or service network. You must provide either the service network identifier or the service identifier.</p> <p>Every association in Amazon VPC Lattice has a unique Amazon Resource Name (ARN), such as when a service network is associated with a VPC or when a service is associated with a service network. If the association is for a resource is shared with another account, the association includes the local account ID as the prefix in the ARN.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations.list_service_network_service_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest = {}
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if service_identifier is not None:
            input_["service_identifier"] = service_identifier
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

    def iter_list_service_network_service_associations(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        service_network_identifier: Optional[
            "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        service_identifier: Optional[
            "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.service_network_service_association_summary.ServiceNetworkServiceAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_service_network_service_associations(
                config_overrides=config_overrides,
                service_network_identifier=service_network_identifier,
                service_identifier=service_identifier,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_service_network_vpc_association(
        self,
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier_without_regex.ServiceNetworkIdentifierWithoutRegex",
        vpc_identifier: "capo_vpc_lattice.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        private_dns_enabled: Optional["capo_vpc_lattice.types.boolean.Boolean"] = None,
        security_group_ids: Optional[
            "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
        dns_options: Optional["capo_vpc_lattice.types.dns_options.DnsOptions"] = None,
    ) -> "capo_vpc_lattice.types.create_service_network_vpc_association_response.CreateServiceNetworkVpcAssociationResponse":
        """<p>Associates a VPC with a service network. When you associate a VPC with the service network, it enables all the resources within that VPC to be clients and communicate with other services in the service network. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations">Manage VPC associations</a> in the <i>Amazon VPC Lattice User Guide</i>.</p> <p>You can't use this operation if there is a disassociation in progress. If the association fails, retry by deleting the association and recreating it.</p> <p>As a result of this operation, the association gets created in the service network account and the VPC owner account.</p> <p>If you add a security group to the service network and VPC association, the association must continue to always have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and recreate it without security groups.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            service_network_identifier: <p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>
            vpc_identifier: <p>The ID of the VPC.</p>
            private_dns_enabled: <p> Indicates if private DNS is enabled for the VPC association. </p>
            security_group_ids: <p>The IDs of the security groups. Security groups aren't added by default. You can add a security group to apply network level controls to control which resources in a VPC are allowed to access the service network and its services. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html">Control traffic to resources using security groups</a> in the <i>Amazon VPC User Guide</i>.</p>
            tags: <p>The tags for the association.</p>
            dns_options: <p> DNS options for the service network VPC association. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_service_network_vpc_association_request.CreateServiceNetworkVpcAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_service_network_vpc_association_response.CreateServiceNetworkVpcAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service_network_vpc_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_service_network_vpc_association.create_service_network_vpc_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_service_network_vpc_association_request.CreateServiceNetworkVpcAssociationRequest = {
            "service_network_identifier": service_network_identifier,
            "vpc_identifier": vpc_identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if private_dns_enabled is not None:
            input_["private_dns_enabled"] = private_dns_enabled
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if dns_options is not None:
            input_["dns_options"] = dns_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service_network_vpc_association(
        self,
        service_network_vpc_association_identifier: "capo_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_network_vpc_association_response.GetServiceNetworkVpcAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a VPC.</p>

        Args:
            service_network_vpc_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_service_network_vpc_association_request.GetServiceNetworkVpcAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_service_network_vpc_association_response.GetServiceNetworkVpcAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service_network_vpc_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_service_network_vpc_association.get_service_network_vpc_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_service_network_vpc_association_request.GetServiceNetworkVpcAssociationRequest = {
            "service_network_vpc_association_identifier": service_network_vpc_association_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_network_vpc_association(
        self,
        service_network_vpc_association_identifier: "capo_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        security_group_ids: Optional[
            "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
        private_dns_enabled: Optional["capo_vpc_lattice.types.boolean.Boolean"] = None,
        dns_options: Optional["capo_vpc_lattice.types.dns_options.DnsOptions"] = None,
    ) -> "capo_vpc_lattice.types.update_service_network_vpc_association_response.UpdateServiceNetworkVpcAssociationResponse":
        """<p>Updates the service network and VPC association. If you add a security group to the service network and VPC association, the association must continue to have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and then recreate it without security groups.</p>

        Args:
            service_network_vpc_association_identifier: <p>The ID or ARN of the association.</p>
            security_group_ids: <p>The IDs of the security groups.</p>
            private_dns_enabled: <p> Indicates if private DNS is enabled for the VPC association. </p>
            dns_options: <p> DNS options for the service network VPC association. </p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_service_network_vpc_association_request.UpdateServiceNetworkVpcAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_service_network_vpc_association_response.UpdateServiceNetworkVpcAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_service_network_vpc_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_service_network_vpc_association.update_service_network_vpc_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_service_network_vpc_association_request.UpdateServiceNetworkVpcAssociationRequest = {
            "service_network_vpc_association_identifier": service_network_vpc_association_identifier
        }
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if private_dns_enabled is not None:
            input_["private_dns_enabled"] = private_dns_enabled
        if dns_options is not None:
            input_["dns_options"] = dns_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_network_vpc_association(
        self,
        service_network_vpc_association_identifier: "capo_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_network_vpc_association_response.DeleteServiceNetworkVpcAssociationResponse":
        """<p>Disassociates the VPC from the service network. You can't disassociate the VPC if there is a create or update association in progress.</p>

        Args:
            service_network_vpc_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_service_network_vpc_association_request.DeleteServiceNetworkVpcAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_service_network_vpc_association_response.DeleteServiceNetworkVpcAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_vpc_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_vpc_association.delete_service_network_vpc_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_service_network_vpc_association_request.DeleteServiceNetworkVpcAssociationRequest = {
            "service_network_vpc_association_identifier": service_network_vpc_association_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_service_network_vpc_associations(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        service_network_identifier: Optional[
            "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        vpc_identifier: Optional["capo_vpc_lattice.types.vpc_id.VpcId"] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_service_network_vpc_associations_response.ListServiceNetworkVpcAssociationsResponse":
        """<p>Lists the associations between a service network and a VPC. You can filter the list either by VPC or service network. You must provide either the ID of the service network identifier or the ID of the VPC.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            vpc_identifier: <p>The ID or ARN of the VPC.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_service_network_vpc_associations_request.ListServiceNetworkVpcAssociationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_service_network_vpc_associations_response.ListServiceNetworkVpcAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_associations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_associations.list_service_network_vpc_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_service_network_vpc_associations_request.ListServiceNetworkVpcAssociationsRequest = {}
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if vpc_identifier is not None:
            input_["vpc_identifier"] = vpc_identifier
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

    def iter_list_service_network_vpc_associations(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        service_network_identifier: Optional[
            "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        vpc_identifier: Optional["capo_vpc_lattice.types.vpc_id.VpcId"] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.service_network_vpc_association_summary.ServiceNetworkVpcAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_service_network_vpc_associations(
                config_overrides=config_overrides,
                service_network_identifier=service_network_identifier,
                vpc_identifier=vpc_identifier,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_target_group(
        self,
        name: "capo_vpc_lattice.types.target_group_name.TargetGroupName",
        type: "capo_vpc_lattice.types.target_group_type.TargetGroupType",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        config: Optional[
            "capo_vpc_lattice.types.target_group_config.TargetGroupConfig"
        ] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_vpc_lattice.types.create_target_group_response.CreateTargetGroupResponse"
    ):
        """<p>Creates a target group. A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html">Target groups</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            name: <p>The name of the target group. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            type: <p>The type of target group.</p>
            config: <p>The target group configuration.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the target group.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_target_group_request.CreateTargetGroupRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_target_group_response.CreateTargetGroupResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_target_group

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_target_group.create_target_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_target_group_request.CreateTargetGroupRequest = {
            "name": name,
            "type": type,
        }
        if config is not None:
            input_["config"] = config
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

    def get_target_group(
        self,
        target_group_identifier: "capo_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_target_group_response.GetTargetGroupResponse":
        """<p>Retrieves information about the specified target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_target_group_request.GetTargetGroupRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_target_group_response.GetTargetGroupResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_target_group

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_target_group.get_target_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_target_group_request.GetTargetGroupRequest = {
            "target_group_identifier": target_group_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_target_group(
        self,
        target_group_identifier: "capo_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        health_check: "capo_vpc_lattice.types.health_check_config.HealthCheckConfig",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> (
        "capo_vpc_lattice.types.update_target_group_response.UpdateTargetGroupResponse"
    ):
        """<p>Updates the specified target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            health_check: <p>The health check configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_target_group_request.UpdateTargetGroupRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_target_group_response.UpdateTargetGroupResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_target_group

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_target_group.update_target_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_target_group_request.UpdateTargetGroupRequest = {
            "target_group_identifier": target_group_identifier,
            "health_check": health_check,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_target_group(
        self,
        target_group_identifier: "capo_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> (
        "capo_vpc_lattice.types.delete_target_group_response.DeleteTargetGroupResponse"
    ):
        """<p>Deletes a target group. You can't delete a target group if it is used in a listener rule or if the target group creation is in progress.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>

        Raises:
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_target_group_request.DeleteTargetGroupRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_target_group_response.DeleteTargetGroupResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_target_group

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_target_group.delete_target_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_target_group_request.DeleteTargetGroupRequest = {
            "target_group_identifier": target_group_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_target_groups(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
        vpc_identifier: Optional["capo_vpc_lattice.types.vpc_id.VpcId"] = None,
        target_group_type: Optional[
            "capo_vpc_lattice.types.target_group_type.TargetGroupType"
        ] = None,
    ) -> "capo_vpc_lattice.types.list_target_groups_response.ListTargetGroupsResponse":
        """<p>Lists your target groups. You can narrow your search by using the filters below in your request.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
            vpc_identifier: <p>The ID or ARN of the VPC.</p>
            target_group_type: <p>The target group type.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_target_groups_request.ListTargetGroupsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_target_groups_response.ListTargetGroupsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_target_groups

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_target_groups.list_target_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_target_groups_request.ListTargetGroupsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if vpc_identifier is not None:
            input_["vpc_identifier"] = vpc_identifier
        if target_group_type is not None:
            input_["target_group_type"] = target_group_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_target_groups(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
        vpc_identifier: Optional["capo_vpc_lattice.types.vpc_id.VpcId"] = None,
        target_group_type: Optional[
            "capo_vpc_lattice.types.target_group_type.TargetGroupType"
        ] = None,
    ) -> "Iterator[capo_vpc_lattice.types.target_group_summary.TargetGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_target_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                vpc_identifier=vpc_identifier,
                target_group_type=target_group_type,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def deregister_targets(
        self,
        target_group_identifier: "capo_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        targets: "capo_vpc_lattice.types.target_list.TargetList",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.deregister_targets_response.DeregisterTargetsResponse":
        """<p>Deregisters the specified targets from the specified target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            targets: <p>The targets to deregister.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.deregister_targets_request.DeregisterTargetsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.deregister_targets_response.DeregisterTargetsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.deregister_targets

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.deregister_targets.deregister_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.deregister_targets_request.DeregisterTargetsRequest = {
            "target_group_identifier": target_group_identifier,
            "targets": targets,
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
        target_group_identifier: "capo_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
        targets: Optional["capo_vpc_lattice.types.target_list.TargetList"] = None,
    ) -> "capo_vpc_lattice.types.list_targets_response.ListTargetsResponse":
        """<p>Lists the targets for the target group. By default, all targets are included. You can use this API to check the health status of targets. You can also ﬁlter the results by target.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
            targets: <p>The targets.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_targets_request.ListTargetsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_targets_response.ListTargetsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_targets

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_targets.list_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_targets_request.ListTargetsRequest = {
            "target_group_identifier": target_group_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if targets is not None:
            input_["targets"] = targets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_targets(
        self,
        target_group_identifier: "capo_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
        targets: Optional["capo_vpc_lattice.types.target_list.TargetList"] = None,
    ) -> "Iterator[capo_vpc_lattice.types.target_summary.TargetSummary]":
        _token = next_token
        while True:
            _response = self.list_targets(
                target_group_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                targets=targets,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def register_targets(
        self,
        target_group_identifier: "capo_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        targets: "capo_vpc_lattice.types.target_list.TargetList",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.register_targets_response.RegisterTargetsResponse":
        """<p>Registers the targets with the target group. If it's a Lambda target, you can only have one target in a target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            targets: <p>The targets.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.register_targets_request.RegisterTargetsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.register_targets_response.RegisterTargetsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.register_targets

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.register_targets.register_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.register_targets_request.RegisterTargetsRequest = {
            "target_group_identifier": target_group_identifier,
            "targets": targets,
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
