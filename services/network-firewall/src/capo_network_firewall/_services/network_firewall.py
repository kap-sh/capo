"""Generated from Smithy shape ``com.amazonaws.networkfirewall#NetworkFirewall_20201112``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_network_firewall._auth._signers
import capo_network_firewall._auth._sigv4
from capo_network_firewall._auth._identity import Credentials
from capo_network_firewall._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_network_firewall._auth._zapros_handler import AuthMiddleware
from capo_network_firewall._pagination import resolve_path as _resolve_path
from capo_network_firewall._services._aws_config import aws_config
from capo_network_firewall._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_network_firewall.types.accept_network_firewall_transit_gateway_attachment_request
    import capo_network_firewall.types.accept_network_firewall_transit_gateway_attachment_response
    import capo_network_firewall.types.age
    import capo_network_firewall.types.analysis_report
    import capo_network_firewall.types.analysis_report_id
    import capo_network_firewall.types.analysis_report_next_token
    import capo_network_firewall.types.analysis_type_report_result
    import capo_network_firewall.types.associate_availability_zones_request
    import capo_network_firewall.types.associate_availability_zones_response
    import capo_network_firewall.types.associate_firewall_policy_request
    import capo_network_firewall.types.associate_firewall_policy_response
    import capo_network_firewall.types.associate_subnets_request
    import capo_network_firewall.types.associate_subnets_response
    import capo_network_firewall.types.attach_rule_groups_to_proxy_configuration_request
    import capo_network_firewall.types.attach_rule_groups_to_proxy_configuration_response
    import capo_network_firewall.types.availability_zone
    import capo_network_firewall.types.availability_zone_mappings
    import capo_network_firewall.types.az_subnets
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.container_association_summary
    import capo_network_firewall.types.container_monitoring_configurations
    import capo_network_firewall.types.container_monitoring_type
    import capo_network_firewall.types.create_container_association_request
    import capo_network_firewall.types.create_container_association_response
    import capo_network_firewall.types.create_firewall_policy_request
    import capo_network_firewall.types.create_firewall_policy_response
    import capo_network_firewall.types.create_firewall_request
    import capo_network_firewall.types.create_firewall_response
    import capo_network_firewall.types.create_proxy_configuration_request
    import capo_network_firewall.types.create_proxy_configuration_response
    import capo_network_firewall.types.create_proxy_request
    import capo_network_firewall.types.create_proxy_response
    import capo_network_firewall.types.create_proxy_rule_group_request
    import capo_network_firewall.types.create_proxy_rule_group_response
    import capo_network_firewall.types.create_proxy_rules_by_request_phase
    import capo_network_firewall.types.create_proxy_rules_request
    import capo_network_firewall.types.create_proxy_rules_response
    import capo_network_firewall.types.create_rule_group_request
    import capo_network_firewall.types.create_rule_group_response
    import capo_network_firewall.types.create_tls_inspection_configuration_request
    import capo_network_firewall.types.create_tls_inspection_configuration_response
    import capo_network_firewall.types.create_vpc_endpoint_association_request
    import capo_network_firewall.types.create_vpc_endpoint_association_response
    import capo_network_firewall.types.delete_container_association_request
    import capo_network_firewall.types.delete_container_association_response
    import capo_network_firewall.types.delete_firewall_policy_request
    import capo_network_firewall.types.delete_firewall_policy_response
    import capo_network_firewall.types.delete_firewall_request
    import capo_network_firewall.types.delete_firewall_response
    import capo_network_firewall.types.delete_network_firewall_transit_gateway_attachment_request
    import capo_network_firewall.types.delete_network_firewall_transit_gateway_attachment_response
    import capo_network_firewall.types.delete_proxy_configuration_request
    import capo_network_firewall.types.delete_proxy_configuration_response
    import capo_network_firewall.types.delete_proxy_request
    import capo_network_firewall.types.delete_proxy_response
    import capo_network_firewall.types.delete_proxy_rule_group_request
    import capo_network_firewall.types.delete_proxy_rule_group_response
    import capo_network_firewall.types.delete_proxy_rules_request
    import capo_network_firewall.types.delete_proxy_rules_response
    import capo_network_firewall.types.delete_resource_policy_request
    import capo_network_firewall.types.delete_resource_policy_response
    import capo_network_firewall.types.delete_rule_group_request
    import capo_network_firewall.types.delete_rule_group_response
    import capo_network_firewall.types.delete_tls_inspection_configuration_request
    import capo_network_firewall.types.delete_tls_inspection_configuration_response
    import capo_network_firewall.types.delete_vpc_endpoint_association_request
    import capo_network_firewall.types.delete_vpc_endpoint_association_response
    import capo_network_firewall.types.describe_container_association_request
    import capo_network_firewall.types.describe_container_association_response
    import capo_network_firewall.types.describe_firewall_metadata_request
    import capo_network_firewall.types.describe_firewall_metadata_response
    import capo_network_firewall.types.describe_firewall_policy_request
    import capo_network_firewall.types.describe_firewall_policy_response
    import capo_network_firewall.types.describe_firewall_request
    import capo_network_firewall.types.describe_firewall_response
    import capo_network_firewall.types.describe_flow_operation_request
    import capo_network_firewall.types.describe_flow_operation_response
    import capo_network_firewall.types.describe_logging_configuration_request
    import capo_network_firewall.types.describe_logging_configuration_response
    import capo_network_firewall.types.describe_proxy_configuration_request
    import capo_network_firewall.types.describe_proxy_configuration_response
    import capo_network_firewall.types.describe_proxy_request
    import capo_network_firewall.types.describe_proxy_response
    import capo_network_firewall.types.describe_proxy_rule_group_request
    import capo_network_firewall.types.describe_proxy_rule_group_response
    import capo_network_firewall.types.describe_proxy_rule_request
    import capo_network_firewall.types.describe_proxy_rule_response
    import capo_network_firewall.types.describe_resource_policy_request
    import capo_network_firewall.types.describe_resource_policy_response
    import capo_network_firewall.types.describe_rule_group_metadata_request
    import capo_network_firewall.types.describe_rule_group_metadata_response
    import capo_network_firewall.types.describe_rule_group_request
    import capo_network_firewall.types.describe_rule_group_response
    import capo_network_firewall.types.describe_rule_group_summary_request
    import capo_network_firewall.types.describe_rule_group_summary_response
    import capo_network_firewall.types.describe_tls_inspection_configuration_request
    import capo_network_firewall.types.describe_tls_inspection_configuration_response
    import capo_network_firewall.types.describe_vpc_endpoint_association_request
    import capo_network_firewall.types.describe_vpc_endpoint_association_response
    import capo_network_firewall.types.description
    import capo_network_firewall.types.detach_rule_groups_from_proxy_configuration_request
    import capo_network_firewall.types.detach_rule_groups_from_proxy_configuration_response
    import capo_network_firewall.types.disassociate_availability_zones_request
    import capo_network_firewall.types.disassociate_availability_zones_response
    import capo_network_firewall.types.disassociate_subnets_request
    import capo_network_firewall.types.disassociate_subnets_response
    import capo_network_firewall.types.enable_monitoring_dashboard
    import capo_network_firewall.types.enabled_analysis_type
    import capo_network_firewall.types.enabled_analysis_types
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.firewall_metadata
    import capo_network_firewall.types.firewall_policy
    import capo_network_firewall.types.firewall_policy_metadata
    import capo_network_firewall.types.flow
    import capo_network_firewall.types.flow_filters
    import capo_network_firewall.types.flow_operation_id
    import capo_network_firewall.types.flow_operation_metadata
    import capo_network_firewall.types.flow_operation_type
    import capo_network_firewall.types.get_analysis_report_results_request
    import capo_network_firewall.types.get_analysis_report_results_response
    import capo_network_firewall.types.list_analysis_reports_request
    import capo_network_firewall.types.list_analysis_reports_response
    import capo_network_firewall.types.list_container_associations_request
    import capo_network_firewall.types.list_container_associations_response
    import capo_network_firewall.types.list_firewall_policies_request
    import capo_network_firewall.types.list_firewall_policies_response
    import capo_network_firewall.types.list_firewalls_request
    import capo_network_firewall.types.list_firewalls_response
    import capo_network_firewall.types.list_flow_operation_results_request
    import capo_network_firewall.types.list_flow_operation_results_response
    import capo_network_firewall.types.list_flow_operations_request
    import capo_network_firewall.types.list_flow_operations_response
    import capo_network_firewall.types.list_proxies_request
    import capo_network_firewall.types.list_proxies_response
    import capo_network_firewall.types.list_proxy_configurations_request
    import capo_network_firewall.types.list_proxy_configurations_response
    import capo_network_firewall.types.list_proxy_rule_groups_request
    import capo_network_firewall.types.list_proxy_rule_groups_response
    import capo_network_firewall.types.list_rule_groups_request
    import capo_network_firewall.types.list_rule_groups_response
    import capo_network_firewall.types.list_tags_for_resource_request
    import capo_network_firewall.types.list_tags_for_resource_response
    import capo_network_firewall.types.list_tls_inspection_configurations_request
    import capo_network_firewall.types.list_tls_inspection_configurations_response
    import capo_network_firewall.types.list_vpc_endpoint_associations_request
    import capo_network_firewall.types.list_vpc_endpoint_associations_response
    import capo_network_firewall.types.listener_properties_request
    import capo_network_firewall.types.logging_configuration
    import capo_network_firewall.types.nat_gateway_id
    import capo_network_firewall.types.nat_gateway_mappings_list
    import capo_network_firewall.types.pagination_max_results
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.policy_string
    import capo_network_firewall.types.proxy_config_default_rule_phase_actions_request
    import capo_network_firewall.types.proxy_configuration_metadata
    import capo_network_firewall.types.proxy_metadata
    import capo_network_firewall.types.proxy_rule_condition_list
    import capo_network_firewall.types.proxy_rule_group_attachment_list
    import capo_network_firewall.types.proxy_rule_group_metadata
    import capo_network_firewall.types.proxy_rule_group_priority_list
    import capo_network_firewall.types.proxy_rule_phase_action
    import capo_network_firewall.types.proxy_rule_priority_list
    import capo_network_firewall.types.proxy_rules_by_request_phase
    import capo_network_firewall.types.proxy_settings
    import capo_network_firewall.types.put_resource_policy_request
    import capo_network_firewall.types.put_resource_policy_response
    import capo_network_firewall.types.reject_network_firewall_transit_gateway_attachment_request
    import capo_network_firewall.types.reject_network_firewall_transit_gateway_attachment_response
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_arn_list
    import capo_network_firewall.types.resource_managed_status
    import capo_network_firewall.types.resource_managed_type
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.resource_name_list
    import capo_network_firewall.types.rule_capacity
    import capo_network_firewall.types.rule_group
    import capo_network_firewall.types.rule_group_metadata
    import capo_network_firewall.types.rule_group_request_phase
    import capo_network_firewall.types.rule_group_type
    import capo_network_firewall.types.rules_string
    import capo_network_firewall.types.source_metadata
    import capo_network_firewall.types.start_analysis_report_request
    import capo_network_firewall.types.start_analysis_report_response
    import capo_network_firewall.types.start_flow_capture_request
    import capo_network_firewall.types.start_flow_capture_response
    import capo_network_firewall.types.start_flow_flush_request
    import capo_network_firewall.types.start_flow_flush_response
    import capo_network_firewall.types.subnet_mapping
    import capo_network_firewall.types.subnet_mappings
    import capo_network_firewall.types.subscription_status
    import capo_network_firewall.types.summary_configuration
    import capo_network_firewall.types.tag
    import capo_network_firewall.types.tag_key_list
    import capo_network_firewall.types.tag_list
    import capo_network_firewall.types.tag_resource_request
    import capo_network_firewall.types.tag_resource_response
    import capo_network_firewall.types.tags_pagination_max_results
    import capo_network_firewall.types.tls_inspection_configuration
    import capo_network_firewall.types.tls_inspection_configuration_metadata
    import capo_network_firewall.types.tls_intercept_properties_request
    import capo_network_firewall.types.transit_gateway_attachment_id
    import capo_network_firewall.types.transit_gateway_id
    import capo_network_firewall.types.untag_resource_request
    import capo_network_firewall.types.untag_resource_response
    import capo_network_firewall.types.update_availability_zone_change_protection_request
    import capo_network_firewall.types.update_availability_zone_change_protection_response
    import capo_network_firewall.types.update_container_association_request
    import capo_network_firewall.types.update_container_association_response
    import capo_network_firewall.types.update_firewall_analysis_settings_request
    import capo_network_firewall.types.update_firewall_analysis_settings_response
    import capo_network_firewall.types.update_firewall_delete_protection_request
    import capo_network_firewall.types.update_firewall_delete_protection_response
    import capo_network_firewall.types.update_firewall_description_request
    import capo_network_firewall.types.update_firewall_description_response
    import capo_network_firewall.types.update_firewall_encryption_configuration_request
    import capo_network_firewall.types.update_firewall_encryption_configuration_response
    import capo_network_firewall.types.update_firewall_policy_change_protection_request
    import capo_network_firewall.types.update_firewall_policy_change_protection_response
    import capo_network_firewall.types.update_firewall_policy_request
    import capo_network_firewall.types.update_firewall_policy_response
    import capo_network_firewall.types.update_logging_configuration_request
    import capo_network_firewall.types.update_logging_configuration_response
    import capo_network_firewall.types.update_proxy_configuration_request
    import capo_network_firewall.types.update_proxy_configuration_response
    import capo_network_firewall.types.update_proxy_request
    import capo_network_firewall.types.update_proxy_response
    import capo_network_firewall.types.update_proxy_rule_group_priorities_request
    import capo_network_firewall.types.update_proxy_rule_group_priorities_response
    import capo_network_firewall.types.update_proxy_rule_priorities_request
    import capo_network_firewall.types.update_proxy_rule_priorities_response
    import capo_network_firewall.types.update_proxy_rule_request
    import capo_network_firewall.types.update_proxy_rule_response
    import capo_network_firewall.types.update_proxy_settings_request
    import capo_network_firewall.types.update_proxy_settings_response
    import capo_network_firewall.types.update_rule_group_request
    import capo_network_firewall.types.update_rule_group_response
    import capo_network_firewall.types.update_subnet_change_protection_request
    import capo_network_firewall.types.update_subnet_change_protection_response
    import capo_network_firewall.types.update_tls_inspection_configuration_request
    import capo_network_firewall.types.update_tls_inspection_configuration_response
    import capo_network_firewall.types.update_token
    import capo_network_firewall.types.vpc_endpoint
    import capo_network_firewall.types.vpc_endpoint_association_metadata
    import capo_network_firewall.types.vpc_endpoint_id
    import capo_network_firewall.types.vpc_id
    import capo_network_firewall.types.vpc_ids


class NetworkFirewallClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class NetworkFirewallClient:
    """A client for the ``NetworkFirewall`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = NetworkFirewallClientConfig(
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
        self, config_overrides: Optional[NetworkFirewallClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: NetworkFirewallClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def accept_network_firewall_transit_gateway_attachment(
        self,
        transit_gateway_attachment_id: "capo_network_firewall.types.transit_gateway_attachment_id.TransitGatewayAttachmentId",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.accept_network_firewall_transit_gateway_attachment_response.AcceptNetworkFirewallTransitGatewayAttachmentResponse":
        """<p>Accepts a transit gateway attachment request for Network Firewall. When you accept the attachment request, Network Firewall creates the necessary routing components to enable traffic flow between the transit gateway and firewall endpoints.</p> <p>You must accept a transit gateway attachment to complete the creation of a transit gateway-attached firewall, unless auto-accept is enabled on the transit gateway. After acceptance, use <a>DescribeFirewall</a> to verify the firewall status.</p> <p>To reject an attachment instead of accepting it, use <a>RejectNetworkFirewallTransitGatewayAttachment</a>.</p> <note> <p>It can take several minutes for the attachment acceptance to complete and the firewall to become available.</p> </note>

        Args:
            transit_gateway_attachment_id: <p>Required. The unique identifier of the transit gateway attachment to accept. This ID is returned in the response when creating a transit gateway-attached firewall.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.accept_network_firewall_transit_gateway_attachment_request.AcceptNetworkFirewallTransitGatewayAttachmentRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.accept_network_firewall_transit_gateway_attachment_response.AcceptNetworkFirewallTransitGatewayAttachmentResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.accept_network_firewall_transit_gateway_attachment

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.accept_network_firewall_transit_gateway_attachment.accept_network_firewall_transit_gateway_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.accept_network_firewall_transit_gateway_attachment_request.AcceptNetworkFirewallTransitGatewayAttachmentRequest = {
            "transit_gateway_attachment_id": transit_gateway_attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_availability_zones(
        self,
        availability_zone_mappings: "capo_network_firewall.types.availability_zone_mappings.AvailabilityZoneMappings",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.associate_availability_zones_response.AssociateAvailabilityZonesResponse":
        """<p>Associates the specified Availability Zones with a transit gateway-attached firewall. For each Availability Zone, Network Firewall creates a firewall endpoint to process traffic. You can specify one or more Availability Zones where you want to deploy the firewall.</p> <p>After adding Availability Zones, you must update your transit gateway route tables to direct traffic through the new firewall endpoints. Use <a>DescribeFirewall</a> to monitor the status of the new endpoints.</p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            availability_zone_mappings: <p>Required. The Availability Zones where you want to create firewall endpoints. You must specify at least one Availability Zone.</p>

        Raises:
            capo_network_firewall.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>Amazon Web Services doesn't currently have enough available capacity to fulfill your request. Try your request later. </p>
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.associate_availability_zones_request.AssociateAvailabilityZonesRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.associate_availability_zones_response.AssociateAvailabilityZonesResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.associate_availability_zones

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.associate_availability_zones.associate_availability_zones(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.associate_availability_zones_request.AssociateAvailabilityZonesRequest = {
            "availability_zone_mappings": availability_zone_mappings
        }
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_firewall_policy(
        self,
        firewall_policy_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.associate_firewall_policy_response.AssociateFirewallPolicyResponse":
        """<p>Associates a <a>FirewallPolicy</a> to a <a>Firewall</a>. </p> <p>A firewall policy defines how to monitor and manage your VPC network traffic, using a collection of inspection rule groups and other settings. Each firewall requires one firewall policy association, and you can use the same firewall policy for multiple firewalls. </p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_policy_arn: <p>The Amazon Resource Name (ARN) of the firewall policy.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.associate_firewall_policy_request.AssociateFirewallPolicyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.associate_firewall_policy_response.AssociateFirewallPolicyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.associate_firewall_policy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.associate_firewall_policy.associate_firewall_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.associate_firewall_policy_request.AssociateFirewallPolicyRequest = {
            "firewall_policy_arn": firewall_policy_arn
        }
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_subnets(
        self,
        subnet_mappings: "capo_network_firewall.types.subnet_mappings.SubnetMappings",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.associate_subnets_response.AssociateSubnetsResponse":
        """<p>Associates the specified subnets in the Amazon VPC to the firewall. You can specify one subnet for each of the Availability Zones that the VPC spans. </p> <p>This request creates an Network Firewall firewall endpoint in each of the subnets. To enable the firewall's protections, you must also modify the VPC's route tables for each subnet's Availability Zone, to redirect the traffic that's coming into and going out of the zone through the firewall endpoint. </p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            subnet_mappings: <p>The IDs of the subnets that you want to associate with the firewall. </p>

        Raises:
            capo_network_firewall.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>Amazon Web Services doesn't currently have enough available capacity to fulfill your request. Try your request later. </p>
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.associate_subnets_request.AssociateSubnetsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.associate_subnets_response.AssociateSubnetsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.associate_subnets

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.associate_subnets.associate_subnets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.associate_subnets_request.AssociateSubnetsRequest = {
            "subnet_mappings": subnet_mappings
        }
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def attach_rule_groups_to_proxy_configuration(
        self,
        rule_groups: "capo_network_firewall.types.proxy_rule_group_attachment_list.ProxyRuleGroupAttachmentList",
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.attach_rule_groups_to_proxy_configuration_response.AttachRuleGroupsToProxyConfigurationResponse":
        """<p>Attaches <a>ProxyRuleGroup</a> resources to a <a>ProxyConfiguration</a> </p> <p>A Proxy Configuration defines the monitoring and protection behavior for a Proxy. The details of the behavior are defined in the rule groups that you add to your configuration. </p>

        Args:
            proxy_configuration_name: <p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_configuration_arn: <p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_groups: <p>The proxy rule group(s) to attach to the proxy configuration</p>
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request. </p> <p>To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.attach_rule_groups_to_proxy_configuration_request.AttachRuleGroupsToProxyConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.attach_rule_groups_to_proxy_configuration_response.AttachRuleGroupsToProxyConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.attach_rule_groups_to_proxy_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.attach_rule_groups_to_proxy_configuration.attach_rule_groups_to_proxy_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.attach_rule_groups_to_proxy_configuration_request.AttachRuleGroupsToProxyConfigurationRequest = {
            "rule_groups": rule_groups,
            "update_token": update_token,
        }
        if proxy_configuration_name is not None:
            input_["proxy_configuration_name"] = proxy_configuration_name
        if proxy_configuration_arn is not None:
            input_["proxy_configuration_arn"] = proxy_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_container_association(
        self,
        container_association_name: "capo_network_firewall.types.resource_name.ResourceName",
        type: "capo_network_firewall.types.container_monitoring_type.ContainerMonitoringType",
        container_monitoring_configurations: "capo_network_firewall.types.container_monitoring_configurations.ContainerMonitoringConfigurations",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
    ) -> "capo_network_firewall.types.create_container_association_response.CreateContainerAssociationResponse":
        """<p>Creates a Network Firewall container association. The association monitors container lifecycle events in your Amazon ECS or Amazon EKS clusters and resolves running container addresses for use in firewall rules.</p>

        Args:
            container_association_name: <p>The descriptive name of the container association. You can't change the name of a container association after you create it.</p>
            description: <p>A description of the container association.</p>
            type: <p>The type of containers to monitor. You can't change the container type after creation. Valid values:</p> <ul> <li> <p> <code>ECS</code> - Amazon Elastic Container Service</p> </li> <li> <p> <code>EKS</code> - Amazon Elastic Kubernetes Service</p> </li> </ul>
            container_monitoring_configurations: <p>The monitoring configurations for the container association. Each configuration specifies an Amazon ECS or Amazon EKS cluster to monitor and optional attribute filters to narrow which containers are tracked.</p>
            tags: <p>The key:value pairs to associate with the resource.</p>

        Raises:
            capo_network_firewall.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>Amazon Web Services doesn't currently have enough available capacity to fulfill your request. Try your request later. </p>
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.limit_exceeded_exception.LimitExceededException: <p>Unable to perform the operation because doing so would violate a limit setting. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_container_association_request.CreateContainerAssociationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_container_association_response.CreateContainerAssociationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_container_association

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_container_association.create_container_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_container_association_request.CreateContainerAssociationRequest = {
            "container_association_name": container_association_name,
            "type": type,
            "container_monitoring_configurations": container_monitoring_configurations,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_firewall(
        self,
        firewall_name: "capo_network_firewall.types.resource_name.ResourceName",
        firewall_policy_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        vpc_id: Optional["capo_network_firewall.types.vpc_id.VpcId"] = None,
        subnet_mappings: Optional[
            "capo_network_firewall.types.subnet_mappings.SubnetMappings"
        ] = None,
        delete_protection: Optional[
            "capo_network_firewall.types.boolean.Boolean"
        ] = None,
        subnet_change_protection: Optional[
            "capo_network_firewall.types.boolean.Boolean"
        ] = None,
        firewall_policy_change_protection: Optional[
            "capo_network_firewall.types.boolean.Boolean"
        ] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
        encryption_configuration: Optional[
            "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        enabled_analysis_types: Optional[
            "capo_network_firewall.types.enabled_analysis_types.EnabledAnalysisTypes"
        ] = None,
        transit_gateway_id: Optional[
            "capo_network_firewall.types.transit_gateway_id.TransitGatewayId"
        ] = None,
        availability_zone_mappings: Optional[
            "capo_network_firewall.types.availability_zone_mappings.AvailabilityZoneMappings"
        ] = None,
        availability_zone_change_protection: Optional[
            "capo_network_firewall.types.boolean.Boolean"
        ] = None,
        nat_gateway_mappings: Optional[
            "capo_network_firewall.types.nat_gateway_mappings_list.NatGatewayMappingsList"
        ] = None,
        proxy_settings: Optional[
            "capo_network_firewall.types.proxy_settings.ProxySettings"
        ] = None,
        no_source_preservation: Optional[
            "capo_network_firewall.types.boolean.Boolean"
        ] = None,
        vpc_endpoint: Optional[
            "capo_network_firewall.types.vpc_endpoint.VpcEndpoint"
        ] = None,
    ) -> "capo_network_firewall.types.create_firewall_response.CreateFirewallResponse":
        """<p>Creates an Network Firewall <a>Firewall</a> and accompanying <a>FirewallStatus</a> for a VPC. </p> <p>The firewall defines the configuration settings for an Network Firewall firewall. The settings that you can define at creation include the firewall policy, the subnets in your VPC to use for the firewall endpoints, and any tags that are attached to the firewall Amazon Web Services resource. </p> <p>After you create a firewall, you can provide additional settings, like the logging configuration. </p> <p>To update the settings for a firewall, you use the operations that apply to the settings themselves, for example <a>UpdateLoggingConfiguration</a>, <a>AssociateSubnets</a>, and <a>UpdateFirewallDeleteProtection</a>. </p> <p>To manage a firewall's tags, use the standard Amazon Web Services resource tagging operations, <a>ListTagsForResource</a>, <a>TagResource</a>, and <a>UntagResource</a>.</p> <p>To retrieve information about firewalls, use <a>ListFirewalls</a> and <a>DescribeFirewall</a>.</p> <p>To generate a report on the last 30 days of traffic monitored by a firewall, use <a>StartAnalysisReport</a>.</p>

        Args:
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p>
            firewall_policy_arn: <p>The Amazon Resource Name (ARN) of the <a>FirewallPolicy</a> that you want to use for the firewall.</p>
            vpc_id: <p>The unique identifier of the VPC where Network Firewall should create the firewall. </p> <p>You can't change this setting after you create the firewall. </p>
            subnet_mappings: <p>The public subnets to use for your Network Firewall firewalls. Each subnet must belong to a different Availability Zone in the VPC. Network Firewall creates a firewall endpoint in each subnet. </p>
            delete_protection: <p>A flag indicating whether it is possible to delete the firewall. A setting of <code>TRUE</code> indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to <code>TRUE</code>.</p>
            subnet_change_protection: <p>A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>
            firewall_policy_change_protection: <p>A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>
            description: <p>A description of the firewall.</p>
            tags: <p>The key:value pairs to associate with the resource.</p>
            encryption_configuration: <p>A complex type that contains settings for encryption of your firewall resources.</p>
            enabled_analysis_types: <p>An optional setting indicating the specific traffic analysis types to enable on the firewall. </p>
            transit_gateway_id: <p>Required when creating a transit gateway-attached firewall. The unique identifier of the transit gateway to attach to this firewall. You can provide either a transit gateway from your account or one that has been shared with you through Resource Access Manager.</p> <important> <p>After creating the firewall, you cannot change the transit gateway association. To use a different transit gateway, you must create a new firewall.</p> </important> <p>For information about creating firewalls, see <a>CreateFirewall</a>. For specific guidance about transit gateway-attached firewalls, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/tgw-firewall-considerations.html">Considerations for transit gateway-attached firewalls</a> in the <i>Network Firewall Developer Guide</i>.</p>
            availability_zone_mappings: <p>Required. The Availability Zones where you want to create firewall endpoints for a transit gateway-attached firewall. You must specify at least one Availability Zone. Consider enabling the firewall in every Availability Zone where you have workloads to maintain Availability Zone isolation.</p> <p>You can modify Availability Zones later using <a>AssociateAvailabilityZones</a> or <a>DisassociateAvailabilityZones</a>, but this may briefly disrupt traffic. The <code>AvailabilityZoneChangeProtection</code> setting controls whether you can make these modifications.</p>
            availability_zone_change_protection: <p>Optional. A setting indicating whether the firewall is protected against changes to its Availability Zone configuration. When set to <code>TRUE</code>, you cannot add or remove Availability Zones without first disabling this protection using <a>UpdateAvailabilityZoneChangeProtection</a>.</p> <p>Default value: <code>FALSE</code> </p>
            nat_gateway_mappings: <p>The NAT gateways that the firewall uses to proxy traffic when <code>NoSourcePreservation</code> is <code>TRUE</code>. Network Firewall attaches the firewall to each NAT gateway that you specify, so that egress traffic is proxied through the NAT gateway. </p>
            proxy_settings: <p>The listener configuration for a proxy mode firewall, used when <code>NoSourcePreservation</code> is <code>TRUE</code>. This specifies the ports and protocols on which the firewall's proxy listens for traffic. </p>
            no_source_preservation: <p>Optional. Indicates whether the firewall operates in proxy mode, in which the source IP address of the traffic is not preserved. When set to <code>TRUE</code>, the firewall proxies traffic through a NAT gateway and the traffic reaching the destination uses the NAT gateway's IP address as the source. </p> <p>When you set this to <code>TRUE</code>, you must specify <code>NatGatewayMappings</code> and <code>VpcEndpoint</code> instead of a top-level <code>VpcId</code> and <code>SubnetMappings</code>. </p> <p>You can't change this setting after you create the firewall. </p> <p>Default value: <code>FALSE</code> </p>
            vpc_endpoint: <p>The VPC and subnets for the firewall endpoint, used when <code>NoSourcePreservation</code> is <code>TRUE</code>. Network Firewall creates the firewall endpoint in the subnets that you specify here. </p> <p>For proxy mode firewalls, provide the firewall's VPC and endpoint subnets through this parameter instead of the top-level <code>VpcId</code> and <code>SubnetMappings</code>. </p>

        Raises:
            capo_network_firewall.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>Amazon Web Services doesn't currently have enough available capacity to fulfill your request. Try your request later. </p>
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.limit_exceeded_exception.LimitExceededException: <p>Unable to perform the operation because doing so would violate a limit setting. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_firewall_request.CreateFirewallRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_firewall_response.CreateFirewallResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_firewall

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_firewall.create_firewall(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_firewall_request.CreateFirewallRequest = {
            "firewall_name": firewall_name,
            "firewall_policy_arn": firewall_policy_arn,
        }
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if subnet_mappings is not None:
            input_["subnet_mappings"] = subnet_mappings
        if delete_protection is not None:
            input_["delete_protection"] = delete_protection
        if subnet_change_protection is not None:
            input_["subnet_change_protection"] = subnet_change_protection
        if firewall_policy_change_protection is not None:
            input_["firewall_policy_change_protection"] = (
                firewall_policy_change_protection
            )
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if enabled_analysis_types is not None:
            input_["enabled_analysis_types"] = enabled_analysis_types
        if transit_gateway_id is not None:
            input_["transit_gateway_id"] = transit_gateway_id
        if availability_zone_mappings is not None:
            input_["availability_zone_mappings"] = availability_zone_mappings
        if availability_zone_change_protection is not None:
            input_["availability_zone_change_protection"] = (
                availability_zone_change_protection
            )
        if nat_gateway_mappings is not None:
            input_["nat_gateway_mappings"] = nat_gateway_mappings
        if proxy_settings is not None:
            input_["proxy_settings"] = proxy_settings
        if no_source_preservation is not None:
            input_["no_source_preservation"] = no_source_preservation
        if vpc_endpoint is not None:
            input_["vpc_endpoint"] = vpc_endpoint

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_firewall_policy(
        self,
        firewall_policy_name: "capo_network_firewall.types.resource_name.ResourceName",
        firewall_policy: "capo_network_firewall.types.firewall_policy.FirewallPolicy",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
        dry_run: Optional["capo_network_firewall.types.boolean.Boolean"] = None,
        encryption_configuration: Optional[
            "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_network_firewall.types.create_firewall_policy_response.CreateFirewallPolicyResponse":
        """<p>Creates the firewall policy for the firewall according to the specifications. </p> <p>An Network Firewall firewall policy defines the behavior of a firewall, in a collection of stateless and stateful rule groups and other settings. You can use one firewall policy for multiple firewalls. </p>

        Args:
            firewall_policy_name: <p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p>
            firewall_policy: <p>The rule groups and policy actions to use in the firewall policy.</p>
            description: <p>A description of the firewall policy.</p>
            tags: <p>The key:value pairs to associate with the resource.</p>
            dry_run: <p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>
            encryption_configuration: <p>A complex type that contains settings for encryption of your firewall policy resources.</p>

        Raises:
            capo_network_firewall.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>Amazon Web Services doesn't currently have enough available capacity to fulfill your request. Try your request later. </p>
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.limit_exceeded_exception.LimitExceededException: <p>Unable to perform the operation because doing so would violate a limit setting. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_firewall_policy_request.CreateFirewallPolicyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_firewall_policy_response.CreateFirewallPolicyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_firewall_policy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_firewall_policy.create_firewall_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_firewall_policy_request.CreateFirewallPolicyRequest = {
            "firewall_policy_name": firewall_policy_name,
            "firewall_policy": firewall_policy,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_proxy(
        self,
        proxy_name: "capo_network_firewall.types.resource_name.ResourceName",
        nat_gateway_id: "capo_network_firewall.types.nat_gateway_id.NatGatewayId",
        tls_intercept_properties: "capo_network_firewall.types.tls_intercept_properties_request.TlsInterceptPropertiesRequest",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        listener_properties: Optional[
            "capo_network_firewall.types.listener_properties_request.ListenerPropertiesRequest"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
    ) -> "capo_network_firewall.types.create_proxy_response.CreateProxyResponse":
        """<p>Creates an Network Firewall <a>Proxy</a> </p> <p>Attaches a Proxy configuration to a NAT Gateway. </p> <p>To manage a proxy's tags, use the standard Amazon Web Services resource tagging operations, <a>ListTagsForResource</a>, <a>TagResource</a>, and <a>UntagResource</a>.</p> <p>To retrieve information about proxies, use <a>ListProxies</a> and <a>DescribeProxy</a>.</p>

        Args:
            proxy_name: <p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p>
            nat_gateway_id: <p>A unique identifier for the NAT gateway to use with proxy resources.</p>
            proxy_configuration_name: <p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_configuration_arn: <p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            listener_properties: <p>Listener properties for HTTP and HTTPS traffic.</p>
            tls_intercept_properties: <p>TLS decryption on traffic to filter on attributes in the HTTP header. </p>
            tags: <p>The key:value pairs to associate with the resource.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.limit_exceeded_exception.LimitExceededException: <p>Unable to perform the operation because doing so would violate a limit setting. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation you requested isn't supported by Network Firewall. </p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_proxy_request.CreateProxyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_proxy_response.CreateProxyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_proxy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_proxy.create_proxy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_proxy_request.CreateProxyRequest = {
            "proxy_name": proxy_name,
            "nat_gateway_id": nat_gateway_id,
            "tls_intercept_properties": tls_intercept_properties,
        }
        if proxy_configuration_name is not None:
            input_["proxy_configuration_name"] = proxy_configuration_name
        if proxy_configuration_arn is not None:
            input_["proxy_configuration_arn"] = proxy_configuration_arn
        if listener_properties is not None:
            input_["listener_properties"] = listener_properties
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_proxy_configuration(
        self,
        proxy_configuration_name: "capo_network_firewall.types.resource_name.ResourceName",
        default_rule_phase_actions: "capo_network_firewall.types.proxy_config_default_rule_phase_actions_request.ProxyConfigDefaultRulePhaseActionsRequest",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        rule_group_names: Optional[
            "capo_network_firewall.types.resource_name_list.ResourceNameList"
        ] = None,
        rule_group_arns: Optional[
            "capo_network_firewall.types.resource_arn_list.ResourceArnList"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
    ) -> "capo_network_firewall.types.create_proxy_configuration_response.CreateProxyConfigurationResponse":
        """<p>Creates an Network Firewall <a>ProxyConfiguration</a> </p> <p>A Proxy Configuration defines the monitoring and protection behavior for a Proxy. The details of the behavior are defined in the rule groups that you add to your configuration. </p> <p>To manage a proxy configuration's tags, use the standard Amazon Web Services resource tagging operations, <a>ListTagsForResource</a>, <a>TagResource</a>, and <a>UntagResource</a>.</p> <p>To retrieve information about proxies, use <a>ListProxyConfigurations</a> and <a>DescribeProxyConfiguration</a>.</p>

        Args:
            proxy_configuration_name: <p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p>
            description: <p>A description of the proxy configuration. </p>
            rule_group_names: <p>The proxy rule group name(s) to attach to the proxy configuration.</p> <p>You must specify the ARNs or the names, and you can specify both. </p>
            rule_group_arns: <p>The proxy rule group arn(s) to attach to the proxy configuration.</p> <p>You must specify the ARNs or the names, and you can specify both. </p>
            default_rule_phase_actions: <p>Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. </p>
            tags: <p>The key:value pairs to associate with the resource.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.limit_exceeded_exception.LimitExceededException: <p>Unable to perform the operation because doing so would violate a limit setting. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_proxy_configuration_request.CreateProxyConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_proxy_configuration_response.CreateProxyConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_proxy_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_proxy_configuration.create_proxy_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_proxy_configuration_request.CreateProxyConfigurationRequest = {
            "proxy_configuration_name": proxy_configuration_name,
            "default_rule_phase_actions": default_rule_phase_actions,
        }
        if description is not None:
            input_["description"] = description
        if rule_group_names is not None:
            input_["rule_group_names"] = rule_group_names
        if rule_group_arns is not None:
            input_["rule_group_arns"] = rule_group_arns
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_proxy_rule_group(
        self,
        proxy_rule_group_name: "capo_network_firewall.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        rules: Optional[
            "capo_network_firewall.types.proxy_rules_by_request_phase.ProxyRulesByRequestPhase"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
    ) -> "capo_network_firewall.types.create_proxy_rule_group_response.CreateProxyRuleGroupResponse":
        """<p>Creates an Network Firewall <a>ProxyRuleGroup</a> </p> <p>Collections of related proxy filtering rules. Rule groups help you manage and reuse sets of rules across multiple proxy configurations. </p> <p>To manage a proxy rule group's tags, use the standard Amazon Web Services resource tagging operations, <a>ListTagsForResource</a>, <a>TagResource</a>, and <a>UntagResource</a>.</p> <p>To retrieve information about proxy rule groups, use <a>ListProxyRuleGroups</a> and <a>DescribeProxyRuleGroup</a>.</p> <p>To retrieve information about individual proxy rules, use <a>DescribeProxyRuleGroup</a> and <a>DescribeProxyRule</a>.</p>

        Args:
            proxy_rule_group_name: <p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>
            description: <p>A description of the proxy rule group. </p>
            rules: <p>Individual rules that define match conditions and actions for application-layer traffic. Rules specify what to inspect (domains, headers, methods) and what action to take (allow, deny, alert). </p>
            tags: <p>The key:value pairs to associate with the resource.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.limit_exceeded_exception.LimitExceededException: <p>Unable to perform the operation because doing so would violate a limit setting. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_proxy_rule_group_request.CreateProxyRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_proxy_rule_group_response.CreateProxyRuleGroupResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_proxy_rule_group

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_proxy_rule_group.create_proxy_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_proxy_rule_group_request.CreateProxyRuleGroupRequest = {
            "proxy_rule_group_name": proxy_rule_group_name
        }
        if description is not None:
            input_["description"] = description
        if rules is not None:
            input_["rules"] = rules
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_proxy_rules(
        self,
        rules: "capo_network_firewall.types.create_proxy_rules_by_request_phase.CreateProxyRulesByRequestPhase",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        proxy_rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.create_proxy_rules_response.CreateProxyRulesResponse":
        """<p>Creates Network Firewall <a>ProxyRule</a> resources. </p> <p>Attaches new proxy rule(s) to an existing proxy rule group. </p> <p>To retrieve information about individual proxy rules, use <a>DescribeProxyRuleGroup</a> and <a>DescribeProxyRule</a>.</p>

        Args:
            proxy_rule_group_arn: <p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_rule_group_name: <p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rules: <p>Individual rules that define match conditions and actions for application-layer traffic. Rules specify what to inspect (domains, headers, methods) and what action to take (allow, deny, alert). </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_proxy_rules_request.CreateProxyRulesRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_proxy_rules_response.CreateProxyRulesResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_proxy_rules

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_proxy_rules.create_proxy_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_proxy_rules_request.CreateProxyRulesRequest = {
            "rules": rules
        }
        if proxy_rule_group_arn is not None:
            input_["proxy_rule_group_arn"] = proxy_rule_group_arn
        if proxy_rule_group_name is not None:
            input_["proxy_rule_group_name"] = proxy_rule_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_rule_group(
        self,
        rule_group_name: "capo_network_firewall.types.resource_name.ResourceName",
        type: "capo_network_firewall.types.rule_group_type.RuleGroupType",
        capacity: "capo_network_firewall.types.rule_capacity.RuleCapacity",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        rule_group: Optional["capo_network_firewall.types.rule_group.RuleGroup"] = None,
        rules: Optional["capo_network_firewall.types.rules_string.RulesString"] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
        dry_run: Optional["capo_network_firewall.types.boolean.Boolean"] = None,
        encryption_configuration: Optional[
            "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        source_metadata: Optional[
            "capo_network_firewall.types.source_metadata.SourceMetadata"
        ] = None,
        analyze_rule_group: Optional[
            "capo_network_firewall.types.boolean.Boolean"
        ] = None,
        summary_configuration: Optional[
            "capo_network_firewall.types.summary_configuration.SummaryConfiguration"
        ] = None,
    ) -> (
        "capo_network_firewall.types.create_rule_group_response.CreateRuleGroupResponse"
    ):
        """<p>Creates the specified stateless or stateful rule group, which includes the rules for network traffic inspection, a capacity setting, and tags. </p> <p>You provide your rule group specification in your request using either <code>RuleGroup</code> or <code>Rules</code>.</p>

        Args:
            rule_group_name: <p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p>
            rule_group: <p>An object that defines the rule group rules. </p> <note> <p>You must provide either this rule group setting or a <code>Rules</code> setting, but not both. </p> </note>
            rules: <p>A string containing stateful rule group rules specifications in Suricata flat format, with one rule per line. Use this to import your existing Suricata compatible rule groups. </p> <note> <p>You must provide either this rules setting or a populated <code>RuleGroup</code> setting, but not both. </p> </note> <p>You can provide your rule group specification in Suricata flat format through this setting when you create or update your rule group. The call response returns a <a>RuleGroup</a> object that Network Firewall has populated from your string. </p>
            type: <p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p>
            description: <p>A description of the rule group. </p>
            capacity: <p>The maximum operating resources that this rule group can use. Rule group capacity is fixed at creation. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group. </p> <p>You can retrieve the capacity that would be required for a rule group before you create the rule group by calling <a>CreateRuleGroup</a> with <code>DryRun</code> set to <code>TRUE</code>. </p> <note> <p>You can't change or exceed this capacity when you update the rule group, so leave room for your rule group to grow. </p> </note> <p> <b>Capacity for a stateless rule group</b> </p> <p>For a stateless rule group, the capacity required is the sum of the capacity requirements of the individual rules that you expect to have in the rule group. </p> <p>To calculate the capacity requirement of a single rule, multiply the capacity requirement values of each of the rule's match settings:</p> <ul> <li> <p>A match setting with no criteria specified has a value of 1. </p> </li> <li> <p>A match setting with <code>Any</code> specified has a value of 1. </p> </li> <li> <p>All other match settings have a value equal to the number of elements provided in the setting. For example, a protocol setting ["UDP"] and a source setting ["10.0.0.0/24"] each have a value of 1. A protocol setting ["UDP","TCP"] has a value of 2. A source setting ["10.0.0.0/24","10.0.0.1/24","10.0.0.2/24"] has a value of 3. </p> </li> </ul> <p>A rule with no criteria specified in any of its match settings has a capacity requirement of 1. A rule with protocol setting ["UDP","TCP"], source setting ["10.0.0.0/24","10.0.0.1/24","10.0.0.2/24"], and a single specification or no specification for each of the other match settings has a capacity requirement of 6. </p> <p> <b>Capacity for a stateful rule group</b> </p> <p>For a stateful rule group, the minimum capacity required is the number of individual rules that you expect to have in the rule group. </p>
            tags: <p>The key:value pairs to associate with the resource.</p>
            dry_run: <p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>
            encryption_configuration: <p>A complex type that contains settings for encryption of your rule group resources.</p>
            source_metadata: <p>A complex type that contains metadata about the rule group that your own rule group is copied from. You can use the metadata to keep track of updates made to the originating rule group.</p>
            analyze_rule_group: <p>Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to <code>TRUE</code>, Network Firewall runs the analysis and then creates the rule group for you. To run the stateless rule group analyzer without creating the rule group, set <code>DryRun</code> to <code>TRUE</code>.</p>
            summary_configuration: <p>An object that contains a <code>RuleOptions</code> array of strings. You use <code>RuleOptions</code> to determine which of the following <a>RuleSummary</a> values are returned in response to <code>DescribeRuleGroupSummary</code>.</p> <ul> <li> <p> <code>Metadata</code> - returns</p> </li> <li> <p> <code>Msg</code> </p> </li> <li> <p> <code>SID</code> </p> </li> </ul>

        Raises:
            capo_network_firewall.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>Amazon Web Services doesn't currently have enough available capacity to fulfill your request. Try your request later. </p>
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.limit_exceeded_exception.LimitExceededException: <p>Unable to perform the operation because doing so would violate a limit setting. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_rule_group_request.CreateRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_rule_group_response.CreateRuleGroupResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_rule_group

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_rule_group.create_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_rule_group_request.CreateRuleGroupRequest = {
            "rule_group_name": rule_group_name,
            "type": type,
            "capacity": capacity,
        }
        if rule_group is not None:
            input_["rule_group"] = rule_group
        if rules is not None:
            input_["rules"] = rules
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if source_metadata is not None:
            input_["source_metadata"] = source_metadata
        if analyze_rule_group is not None:
            input_["analyze_rule_group"] = analyze_rule_group
        if summary_configuration is not None:
            input_["summary_configuration"] = summary_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_tls_inspection_configuration(
        self,
        tls_inspection_configuration_name: "capo_network_firewall.types.resource_name.ResourceName",
        tls_inspection_configuration: "capo_network_firewall.types.tls_inspection_configuration.TLSInspectionConfiguration",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
        encryption_configuration: Optional[
            "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_network_firewall.types.create_tls_inspection_configuration_response.CreateTLSInspectionConfigurationResponse":
        """<p>Creates an Network Firewall TLS inspection configuration. Network Firewall uses TLS inspection configurations to decrypt your firewall's inbound and outbound SSL/TLS traffic. After decryption, Network Firewall inspects the traffic according to your firewall policy's stateful rules, and then re-encrypts it before sending it to its destination. You can enable inspection of your firewall's inbound traffic, outbound traffic, or both. To use TLS inspection with your firewall, you must first import or provision certificates using ACM, create a TLS inspection configuration, add that configuration to a new firewall policy, and then associate that policy with your firewall.</p> <p>To update the settings for a TLS inspection configuration, use <a>UpdateTLSInspectionConfiguration</a>.</p> <p>To manage a TLS inspection configuration's tags, use the standard Amazon Web Services resource tagging operations, <a>ListTagsForResource</a>, <a>TagResource</a>, and <a>UntagResource</a>.</p> <p>To retrieve information about TLS inspection configurations, use <a>ListTLSInspectionConfigurations</a> and <a>DescribeTLSInspectionConfiguration</a>.</p> <p> For more information about TLS inspection configurations, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html">Inspecting SSL/TLS traffic with TLS inspection configurations</a> in the <i>Network Firewall Developer Guide</i>. </p>

        Args:
            tls_inspection_configuration_name: <p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p>
            tls_inspection_configuration: <p>The object that defines a TLS inspection configuration. This, along with <a>TLSInspectionConfigurationResponse</a>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a>. </p> <p>Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.</p> <p>To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html">Inspecting SSL/TLS traffic with TLS inspection configurations</a> in the <i>Network Firewall Developer Guide</i>.</p>
            description: <p>A description of the TLS inspection configuration. </p>
            tags: <p>The key:value pairs to associate with the resource.</p>

        Raises:
            capo_network_firewall.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>Amazon Web Services doesn't currently have enough available capacity to fulfill your request. Try your request later. </p>
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.limit_exceeded_exception.LimitExceededException: <p>Unable to perform the operation because doing so would violate a limit setting. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_tls_inspection_configuration_request.CreateTLSInspectionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_tls_inspection_configuration_response.CreateTLSInspectionConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_tls_inspection_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_tls_inspection_configuration.create_tls_inspection_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_tls_inspection_configuration_request.CreateTLSInspectionConfigurationRequest = {
            "tls_inspection_configuration_name": tls_inspection_configuration_name,
            "tls_inspection_configuration": tls_inspection_configuration,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_vpc_endpoint_association(
        self,
        firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        vpc_id: "capo_network_firewall.types.vpc_id.VpcId",
        subnet_mapping: "capo_network_firewall.types.subnet_mapping.SubnetMapping",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
    ) -> "capo_network_firewall.types.create_vpc_endpoint_association_response.CreateVpcEndpointAssociationResponse":
        """<p>Creates a firewall endpoint for an Network Firewall firewall. This type of firewall endpoint is independent of the firewall endpoints that you specify in the <code>Firewall</code> itself, and you define it in addition to those endpoints after the firewall has been created. You can define a VPC endpoint association using a different VPC than the one you used in the firewall specifications. </p>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p>
            vpc_id: <p>The unique identifier of the VPC where you want to create a firewall endpoint. </p>
            description: <p>A description of the VPC endpoint association. </p>
            tags: <p>The key:value pairs to associate with the resource.</p>

        Raises:
            capo_network_firewall.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>Amazon Web Services doesn't currently have enough available capacity to fulfill your request. Try your request later. </p>
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.limit_exceeded_exception.LimitExceededException: <p>Unable to perform the operation because doing so would violate a limit setting. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.create_vpc_endpoint_association_request.CreateVpcEndpointAssociationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.create_vpc_endpoint_association_response.CreateVpcEndpointAssociationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.create_vpc_endpoint_association

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.create_vpc_endpoint_association.create_vpc_endpoint_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.create_vpc_endpoint_association_request.CreateVpcEndpointAssociationRequest = {
            "firewall_arn": firewall_arn,
            "vpc_id": vpc_id,
            "subnet_mapping": subnet_mapping,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_container_association(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        container_association_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        container_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.delete_container_association_response.DeleteContainerAssociationResponse":
        """<p>Deletes a container association. The resource transitions to a <code>DELETING</code> state. Deletion is asynchronous - Network Firewall returns immediately while cleanup proceeds in the background. You can't delete a container association while a rule group references it.</p>

        Args:
            container_association_name: <p>The descriptive name of the container association.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            container_association_arn: <p>The Amazon Resource Name (ARN) of the container association.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_container_association_request.DeleteContainerAssociationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_container_association_response.DeleteContainerAssociationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_container_association

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_container_association.delete_container_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_container_association_request.DeleteContainerAssociationRequest = {}
        if container_association_name is not None:
            input_["container_association_name"] = container_association_name
        if container_association_arn is not None:
            input_["container_association_arn"] = container_association_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_firewall(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.delete_firewall_response.DeleteFirewallResponse":
        """<p>Deletes the specified <a>Firewall</a> and its <a>FirewallStatus</a>. This operation requires the firewall's <code>DeleteProtection</code> flag to be <code>FALSE</code>. You can't revert this operation. </p> <p>You can check whether a firewall is in use by reviewing the route tables for the Availability Zones where you have firewall subnet mappings. Retrieve the subnet mappings by calling <a>DescribeFirewall</a>. You define and update the route tables through Amazon VPC. As needed, update the route tables for the zones to remove the firewall endpoints. When the route tables no longer use the firewall endpoints, you can remove the firewall safely.</p> <p>To delete a firewall, remove the delete protection if you need to using <a>UpdateFirewallDeleteProtection</a>, then delete the firewall by calling <a>DeleteFirewall</a>. </p>

        Args:
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation you requested isn't supported by Network Firewall. </p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_firewall_request.DeleteFirewallRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_firewall_response.DeleteFirewallResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_firewall

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_firewall.delete_firewall(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_firewall_request.DeleteFirewallRequest = {}
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_firewall_policy(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_policy_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        firewall_policy_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.delete_firewall_policy_response.DeleteFirewallPolicyResponse":
        """<p>Deletes the specified <a>FirewallPolicy</a>. </p>

        Args:
            firewall_policy_name: <p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_policy_arn: <p>The Amazon Resource Name (ARN) of the firewall policy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation you requested isn't supported by Network Firewall. </p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_firewall_policy_request.DeleteFirewallPolicyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_firewall_policy_response.DeleteFirewallPolicyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_firewall_policy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_firewall_policy.delete_firewall_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_firewall_policy_request.DeleteFirewallPolicyRequest = {}
        if firewall_policy_name is not None:
            input_["firewall_policy_name"] = firewall_policy_name
        if firewall_policy_arn is not None:
            input_["firewall_policy_arn"] = firewall_policy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_network_firewall_transit_gateway_attachment(
        self,
        transit_gateway_attachment_id: "capo_network_firewall.types.transit_gateway_attachment_id.TransitGatewayAttachmentId",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.delete_network_firewall_transit_gateway_attachment_response.DeleteNetworkFirewallTransitGatewayAttachmentResponse":
        """<p>Deletes a transit gateway attachment from a Network Firewall. Either the firewall owner or the transit gateway owner can delete the attachment.</p> <important> <p>After you delete a transit gateway attachment, traffic will no longer flow through the firewall endpoints.</p> </important> <p>After you initiate the delete operation, use <a>DescribeFirewall</a> to monitor the deletion status.</p>

        Args:
            transit_gateway_attachment_id: <p>Required. The unique identifier of the transit gateway attachment to delete.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_network_firewall_transit_gateway_attachment_request.DeleteNetworkFirewallTransitGatewayAttachmentRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_network_firewall_transit_gateway_attachment_response.DeleteNetworkFirewallTransitGatewayAttachmentResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_network_firewall_transit_gateway_attachment

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_network_firewall_transit_gateway_attachment.delete_network_firewall_transit_gateway_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_network_firewall_transit_gateway_attachment_request.DeleteNetworkFirewallTransitGatewayAttachmentRequest = {
            "transit_gateway_attachment_id": transit_gateway_attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_proxy(
        self,
        nat_gateway_id: "capo_network_firewall.types.nat_gateway_id.NatGatewayId",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.delete_proxy_response.DeleteProxyResponse":
        """<p>Deletes the specified <a>Proxy</a>. </p> <p>Detaches a Proxy configuration from a NAT Gateway. </p>

        Args:
            nat_gateway_id: <p>The NAT Gateway the proxy is attached to. </p>
            proxy_name: <p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_arn: <p>The Amazon Resource Name (ARN) of a proxy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation you requested isn't supported by Network Firewall. </p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_proxy_request.DeleteProxyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_proxy_response.DeleteProxyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_proxy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_proxy.delete_proxy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_proxy_request.DeleteProxyRequest = {
            "nat_gateway_id": nat_gateway_id
        }
        if proxy_name is not None:
            input_["proxy_name"] = proxy_name
        if proxy_arn is not None:
            input_["proxy_arn"] = proxy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_proxy_configuration(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.delete_proxy_configuration_response.DeleteProxyConfigurationResponse":
        """<p>Deletes the specified <a>ProxyConfiguration</a>. </p>

        Args:
            proxy_configuration_name: <p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_configuration_arn: <p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_proxy_configuration_request.DeleteProxyConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_proxy_configuration_response.DeleteProxyConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_proxy_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_proxy_configuration.delete_proxy_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_proxy_configuration_request.DeleteProxyConfigurationRequest = {}
        if proxy_configuration_name is not None:
            input_["proxy_configuration_name"] = proxy_configuration_name
        if proxy_configuration_arn is not None:
            input_["proxy_configuration_arn"] = proxy_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_proxy_rule_group(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.delete_proxy_rule_group_response.DeleteProxyRuleGroupResponse":
        """<p>Deletes the specified <a>ProxyRuleGroup</a>. </p>

        Args:
            proxy_rule_group_name: <p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_rule_group_arn: <p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_proxy_rule_group_request.DeleteProxyRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_proxy_rule_group_response.DeleteProxyRuleGroupResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_proxy_rule_group

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_proxy_rule_group.delete_proxy_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_proxy_rule_group_request.DeleteProxyRuleGroupRequest = {}
        if proxy_rule_group_name is not None:
            input_["proxy_rule_group_name"] = proxy_rule_group_name
        if proxy_rule_group_arn is not None:
            input_["proxy_rule_group_arn"] = proxy_rule_group_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_proxy_rules(
        self,
        rules: "capo_network_firewall.types.resource_name_list.ResourceNameList",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        proxy_rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.delete_proxy_rules_response.DeleteProxyRulesResponse":
        """<p>Deletes the specified <a>ProxyRule</a>(s). currently attached to a <a>ProxyRuleGroup</a> </p>

        Args:
            proxy_rule_group_arn: <p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_rule_group_name: <p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rules: <p>The proxy rule(s) to remove from the existing proxy rule group. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_proxy_rules_request.DeleteProxyRulesRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_proxy_rules_response.DeleteProxyRulesResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_proxy_rules

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_proxy_rules.delete_proxy_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_proxy_rules_request.DeleteProxyRulesRequest = {
            "rules": rules
        }
        if proxy_rule_group_arn is not None:
            input_["proxy_rule_group_arn"] = proxy_rule_group_arn
        if proxy_rule_group_name is not None:
            input_["proxy_rule_group_name"] = proxy_rule_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a resource policy that you created in a <a>PutResourcePolicy</a> request. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rule group or firewall policy whose resource policy you want to delete. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_resource_policy_exception.InvalidResourcePolicyException: <p>The policy statement failed validation.</p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_resource_policy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_rule_group(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        type: Optional[
            "capo_network_firewall.types.rule_group_type.RuleGroupType"
        ] = None,
    ) -> (
        "capo_network_firewall.types.delete_rule_group_response.DeleteRuleGroupResponse"
    ):
        """<p>Deletes the specified <a>RuleGroup</a>. </p>

        Args:
            rule_group_name: <p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_group_arn: <p>The Amazon Resource Name (ARN) of the rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            type: <p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p> <note> <p>This setting is required for requests that do not include the <code>RuleGroupARN</code>.</p> </note>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation you requested isn't supported by Network Firewall. </p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_rule_group_request.DeleteRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_rule_group_response.DeleteRuleGroupResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_rule_group

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_rule_group.delete_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_rule_group_request.DeleteRuleGroupRequest = {}
        if rule_group_name is not None:
            input_["rule_group_name"] = rule_group_name
        if rule_group_arn is not None:
            input_["rule_group_arn"] = rule_group_arn
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_tls_inspection_configuration(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        tls_inspection_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        tls_inspection_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.delete_tls_inspection_configuration_response.DeleteTLSInspectionConfigurationResponse":
        """<p>Deletes the specified <a>TLSInspectionConfiguration</a>.</p>

        Args:
            tls_inspection_configuration_arn: <p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            tls_inspection_configuration_name: <p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_tls_inspection_configuration_request.DeleteTLSInspectionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_tls_inspection_configuration_response.DeleteTLSInspectionConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_tls_inspection_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_tls_inspection_configuration.delete_tls_inspection_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_tls_inspection_configuration_request.DeleteTLSInspectionConfigurationRequest = {}
        if tls_inspection_configuration_arn is not None:
            input_["tls_inspection_configuration_arn"] = (
                tls_inspection_configuration_arn
            )
        if tls_inspection_configuration_name is not None:
            input_["tls_inspection_configuration_name"] = (
                tls_inspection_configuration_name
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_endpoint_association(
        self,
        vpc_endpoint_association_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.delete_vpc_endpoint_association_response.DeleteVpcEndpointAssociationResponse":
        """<p>Deletes the specified <a>VpcEndpointAssociation</a>.</p> <p>You can check whether an endpoint association is in use by reviewing the route tables for the Availability Zones where you have the endpoint subnet mapping. You can retrieve the subnet mapping by calling <a>DescribeVpcEndpointAssociation</a>. You define and update the route tables through Amazon VPC. As needed, update the route tables for the Availability Zone to remove the firewall endpoint for the association. When the route tables no longer use the firewall endpoint, you can remove the endpoint association safely.</p>

        Args:
            vpc_endpoint_association_arn: <p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.delete_vpc_endpoint_association_request.DeleteVpcEndpointAssociationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.delete_vpc_endpoint_association_response.DeleteVpcEndpointAssociationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.delete_vpc_endpoint_association

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.delete_vpc_endpoint_association.delete_vpc_endpoint_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.delete_vpc_endpoint_association_request.DeleteVpcEndpointAssociationRequest = {
            "vpc_endpoint_association_arn": vpc_endpoint_association_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_container_association(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        container_association_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        container_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.describe_container_association_response.DescribeContainerAssociationResponse":
        """<p>Retrieves the configuration and status of a container association.</p>

        Args:
            container_association_name: <p>The descriptive name of the container association.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            container_association_arn: <p>The Amazon Resource Name (ARN) of the container association.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_container_association_request.DescribeContainerAssociationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_container_association_response.DescribeContainerAssociationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_container_association

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_container_association.describe_container_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_container_association_request.DescribeContainerAssociationRequest = {}
        if container_association_name is not None:
            input_["container_association_name"] = container_association_name
        if container_association_arn is not None:
            input_["container_association_arn"] = container_association_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_firewall(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.describe_firewall_response.DescribeFirewallResponse":
        """<p>Returns the data objects for the specified firewall. </p>

        Args:
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_firewall_request.DescribeFirewallRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_firewall_response.DescribeFirewallResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_firewall

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_firewall.describe_firewall(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_firewall_request.DescribeFirewallRequest = {}
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_firewall_metadata(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.describe_firewall_metadata_response.DescribeFirewallMetadataResponse":
        """<p>Returns the high-level information about a firewall, including the Availability Zones where the Firewall is currently in use. </p>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_firewall_metadata_request.DescribeFirewallMetadataRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_firewall_metadata_response.DescribeFirewallMetadataResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_firewall_metadata

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_firewall_metadata.describe_firewall_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_firewall_metadata_request.DescribeFirewallMetadataRequest = {}
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_firewall_policy(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_policy_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        firewall_policy_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.describe_firewall_policy_response.DescribeFirewallPolicyResponse":
        """<p>Returns the data objects for the specified firewall policy. </p>

        Args:
            firewall_policy_name: <p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_policy_arn: <p>The Amazon Resource Name (ARN) of the firewall policy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_firewall_policy_request.DescribeFirewallPolicyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_firewall_policy_response.DescribeFirewallPolicyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_firewall_policy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_firewall_policy.describe_firewall_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_firewall_policy_request.DescribeFirewallPolicyRequest = {}
        if firewall_policy_name is not None:
            input_["firewall_policy_name"] = firewall_policy_name
        if firewall_policy_arn is not None:
            input_["firewall_policy_arn"] = firewall_policy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_flow_operation(
        self,
        firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        flow_operation_id: "capo_network_firewall.types.flow_operation_id.FlowOperationId",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        availability_zone: Optional[
            "capo_network_firewall.types.availability_zone.AvailabilityZone"
        ] = None,
        vpc_endpoint_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
    ) -> "capo_network_firewall.types.describe_flow_operation_response.DescribeFlowOperationResponse":
        """<p>Returns key information about a specific flow operation.</p>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p>
            availability_zone: <p>The ID of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>
            vpc_endpoint_association_arn: <p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>
            vpc_endpoint_id: <p>A unique identifier for the primary endpoint associated with a firewall.</p>
            flow_operation_id: <p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_flow_operation_request.DescribeFlowOperationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_flow_operation_response.DescribeFlowOperationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_flow_operation

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_flow_operation.describe_flow_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_flow_operation_request.DescribeFlowOperationRequest = {
            "firewall_arn": firewall_arn,
            "flow_operation_id": flow_operation_id,
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if vpc_endpoint_association_arn is not None:
            input_["vpc_endpoint_association_arn"] = vpc_endpoint_association_arn
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_logging_configuration(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.describe_logging_configuration_response.DescribeLoggingConfigurationResponse":
        """<p>Returns the logging configuration for the specified firewall. </p>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_logging_configuration_request.DescribeLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_logging_configuration_response.DescribeLoggingConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_logging_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_logging_configuration.describe_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_logging_configuration_request.DescribeLoggingConfigurationRequest = {}
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_proxy(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.describe_proxy_response.DescribeProxyResponse":
        """<p>Returns the data objects for the specified proxy. </p>

        Args:
            proxy_name: <p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_arn: <p>The Amazon Resource Name (ARN) of a proxy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_proxy_request.DescribeProxyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_proxy_response.DescribeProxyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_proxy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_proxy.describe_proxy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_proxy_request.DescribeProxyRequest = {}
        if proxy_name is not None:
            input_["proxy_name"] = proxy_name
        if proxy_arn is not None:
            input_["proxy_arn"] = proxy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_proxy_configuration(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.describe_proxy_configuration_response.DescribeProxyConfigurationResponse":
        """<p>Returns the data objects for the specified proxy configuration. </p>

        Args:
            proxy_configuration_name: <p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_configuration_arn: <p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_proxy_configuration_request.DescribeProxyConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_proxy_configuration_response.DescribeProxyConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_proxy_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_proxy_configuration.describe_proxy_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_proxy_configuration_request.DescribeProxyConfigurationRequest = {}
        if proxy_configuration_name is not None:
            input_["proxy_configuration_name"] = proxy_configuration_name
        if proxy_configuration_arn is not None:
            input_["proxy_configuration_arn"] = proxy_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_proxy_rule(
        self,
        proxy_rule_name: "capo_network_firewall.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.describe_proxy_rule_response.DescribeProxyRuleResponse":
        """<p>Returns the data objects for the specified proxy configuration for the specified proxy rule group.</p>

        Args:
            proxy_rule_name: <p>The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.</p>
            proxy_rule_group_name: <p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_rule_group_arn: <p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_proxy_rule_request.DescribeProxyRuleRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_proxy_rule_response.DescribeProxyRuleResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_proxy_rule

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_proxy_rule.describe_proxy_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_proxy_rule_request.DescribeProxyRuleRequest = {
            "proxy_rule_name": proxy_rule_name
        }
        if proxy_rule_group_name is not None:
            input_["proxy_rule_group_name"] = proxy_rule_group_name
        if proxy_rule_group_arn is not None:
            input_["proxy_rule_group_arn"] = proxy_rule_group_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_proxy_rule_group(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.describe_proxy_rule_group_response.DescribeProxyRuleGroupResponse":
        """<p>Returns the data objects for the specified proxy rule group. </p>

        Args:
            proxy_rule_group_name: <p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_rule_group_arn: <p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_proxy_rule_group_request.DescribeProxyRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_proxy_rule_group_response.DescribeProxyRuleGroupResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_proxy_rule_group

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_proxy_rule_group.describe_proxy_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_proxy_rule_group_request.DescribeProxyRuleGroupRequest = {}
        if proxy_rule_group_name is not None:
            input_["proxy_rule_group_name"] = proxy_rule_group_name
        if proxy_rule_group_arn is not None:
            input_["proxy_rule_group_arn"] = proxy_rule_group_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_resource_policy(
        self,
        resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.describe_resource_policy_response.DescribeResourcePolicyResponse":
        """<p>Retrieves a resource policy that you created in a <a>PutResourcePolicy</a> request. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rule group or firewall policy whose resource policy you want to retrieve. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_resource_policy_request.DescribeResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_resource_policy_response.DescribeResourcePolicyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_resource_policy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_resource_policy.describe_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_resource_policy_request.DescribeResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_rule_group(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        type: Optional[
            "capo_network_firewall.types.rule_group_type.RuleGroupType"
        ] = None,
        analyze_rule_group: Optional[
            "capo_network_firewall.types.boolean.Boolean"
        ] = None,
    ) -> "capo_network_firewall.types.describe_rule_group_response.DescribeRuleGroupResponse":
        """<p>Returns the data objects for the specified rule group. </p>

        Args:
            rule_group_name: <p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_group_arn: <p>The Amazon Resource Name (ARN) of the rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            type: <p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p> <note> <p>This setting is required for requests that do not include the <code>RuleGroupARN</code>.</p> </note>
            analyze_rule_group: <p>Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to <code>TRUE</code>, Network Firewall runs the analysis.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_rule_group_request.DescribeRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_rule_group_response.DescribeRuleGroupResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_rule_group

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_rule_group.describe_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_rule_group_request.DescribeRuleGroupRequest = {}
        if rule_group_name is not None:
            input_["rule_group_name"] = rule_group_name
        if rule_group_arn is not None:
            input_["rule_group_arn"] = rule_group_arn
        if type is not None:
            input_["type"] = type
        if analyze_rule_group is not None:
            input_["analyze_rule_group"] = analyze_rule_group

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_rule_group_metadata(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        type: Optional[
            "capo_network_firewall.types.rule_group_type.RuleGroupType"
        ] = None,
    ) -> "capo_network_firewall.types.describe_rule_group_metadata_response.DescribeRuleGroupMetadataResponse":
        """<p>High-level information about a rule group, returned by operations like create and describe. You can use the information provided in the metadata to retrieve and manage a rule group. You can retrieve all objects for a rule group by calling <a>DescribeRuleGroup</a>. </p>

        Args:
            rule_group_name: <p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_group_arn: <p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            type: <p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p> <note> <p>This setting is required for requests that do not include the <code>RuleGroupARN</code>.</p> </note>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_rule_group_metadata_request.DescribeRuleGroupMetadataRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_rule_group_metadata_response.DescribeRuleGroupMetadataResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_rule_group_metadata

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_rule_group_metadata.describe_rule_group_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_rule_group_metadata_request.DescribeRuleGroupMetadataRequest = {}
        if rule_group_name is not None:
            input_["rule_group_name"] = rule_group_name
        if rule_group_arn is not None:
            input_["rule_group_arn"] = rule_group_arn
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_rule_group_summary(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        type: Optional[
            "capo_network_firewall.types.rule_group_type.RuleGroupType"
        ] = None,
    ) -> "capo_network_firewall.types.describe_rule_group_summary_response.DescribeRuleGroupSummaryResponse":
        """<p>Returns detailed information for a stateful rule group.</p> <p>For active threat defense Amazon Web Services managed rule groups, this operation provides insight into the protections enabled by the rule group, based on Suricata rule metadata fields. Summaries are available for rule groups you manage and for active threat defense Amazon Web Services managed rule groups.</p> <p>To modify how threat information appears in summaries, use the <code>SummaryConfiguration</code> parameter in <a>UpdateRuleGroup</a>.</p>

        Args:
            rule_group_name: <p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_group_arn: <p>Required. The Amazon Resource Name (ARN) of the rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            type: <p>The type of rule group you want a summary for. This is a required field.</p> <p>Valid value: <code>STATEFUL</code> </p> <p>Note that <code>STATELESS</code> exists but is not currently supported. If you provide <code>STATELESS</code>, an exception is returned.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_rule_group_summary_request.DescribeRuleGroupSummaryRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_rule_group_summary_response.DescribeRuleGroupSummaryResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_rule_group_summary

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_rule_group_summary.describe_rule_group_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_rule_group_summary_request.DescribeRuleGroupSummaryRequest = {}
        if rule_group_name is not None:
            input_["rule_group_name"] = rule_group_name
        if rule_group_arn is not None:
            input_["rule_group_arn"] = rule_group_arn
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_tls_inspection_configuration(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        tls_inspection_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        tls_inspection_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.describe_tls_inspection_configuration_response.DescribeTLSInspectionConfigurationResponse":
        """<p>Returns the data objects for the specified TLS inspection configuration.</p>

        Args:
            tls_inspection_configuration_arn: <p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            tls_inspection_configuration_name: <p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_tls_inspection_configuration_request.DescribeTLSInspectionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_tls_inspection_configuration_response.DescribeTLSInspectionConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_tls_inspection_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_tls_inspection_configuration.describe_tls_inspection_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_tls_inspection_configuration_request.DescribeTLSInspectionConfigurationRequest = {}
        if tls_inspection_configuration_arn is not None:
            input_["tls_inspection_configuration_arn"] = (
                tls_inspection_configuration_arn
            )
        if tls_inspection_configuration_name is not None:
            input_["tls_inspection_configuration_name"] = (
                tls_inspection_configuration_name
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_vpc_endpoint_association(
        self,
        vpc_endpoint_association_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.describe_vpc_endpoint_association_response.DescribeVpcEndpointAssociationResponse":
        """<p>Returns the data object for the specified VPC endpoint association. </p>

        Args:
            vpc_endpoint_association_arn: <p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.describe_vpc_endpoint_association_request.DescribeVpcEndpointAssociationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.describe_vpc_endpoint_association_response.DescribeVpcEndpointAssociationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.describe_vpc_endpoint_association

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.describe_vpc_endpoint_association.describe_vpc_endpoint_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.describe_vpc_endpoint_association_request.DescribeVpcEndpointAssociationRequest = {
            "vpc_endpoint_association_arn": vpc_endpoint_association_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detach_rule_groups_from_proxy_configuration(
        self,
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        rule_group_names: Optional[
            "capo_network_firewall.types.resource_name_list.ResourceNameList"
        ] = None,
        rule_group_arns: Optional[
            "capo_network_firewall.types.resource_arn_list.ResourceArnList"
        ] = None,
    ) -> "capo_network_firewall.types.detach_rule_groups_from_proxy_configuration_response.DetachRuleGroupsFromProxyConfigurationResponse":
        """<p>Detaches <a>ProxyRuleGroup</a> resources from a <a>ProxyConfiguration</a> </p> <p>A Proxy Configuration defines the monitoring and protection behavior for a Proxy. The details of the behavior are defined in the rule groups that you add to your configuration. </p>

        Args:
            proxy_configuration_name: <p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_configuration_arn: <p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_group_names: <p>The proxy rule group names to detach from the proxy configuration</p>
            rule_group_arns: <p>The proxy rule group arns to detach from the proxy configuration</p>
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request. </p> <p>To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.detach_rule_groups_from_proxy_configuration_request.DetachRuleGroupsFromProxyConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.detach_rule_groups_from_proxy_configuration_response.DetachRuleGroupsFromProxyConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.detach_rule_groups_from_proxy_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.detach_rule_groups_from_proxy_configuration.detach_rule_groups_from_proxy_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.detach_rule_groups_from_proxy_configuration_request.DetachRuleGroupsFromProxyConfigurationRequest = {
            "update_token": update_token
        }
        if proxy_configuration_name is not None:
            input_["proxy_configuration_name"] = proxy_configuration_name
        if proxy_configuration_arn is not None:
            input_["proxy_configuration_arn"] = proxy_configuration_arn
        if rule_group_names is not None:
            input_["rule_group_names"] = rule_group_names
        if rule_group_arns is not None:
            input_["rule_group_arns"] = rule_group_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_availability_zones(
        self,
        availability_zone_mappings: "capo_network_firewall.types.availability_zone_mappings.AvailabilityZoneMappings",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.disassociate_availability_zones_response.DisassociateAvailabilityZonesResponse":
        """<p>Removes the specified Availability Zone associations from a transit gateway-attached firewall. This removes the firewall endpoints from these Availability Zones and stops traffic filtering in those zones. Before removing an Availability Zone, ensure you've updated your transit gateway route tables to redirect traffic appropriately.</p> <note> <p>If <code>AvailabilityZoneChangeProtection</code> is enabled, you must first disable it using <a>UpdateAvailabilityZoneChangeProtection</a>.</p> </note> <p>To verify the status of your Availability Zone changes, use <a>DescribeFirewall</a>.</p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            availability_zone_mappings: <p>Required. The Availability Zones to remove from the firewall's configuration.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.disassociate_availability_zones_request.DisassociateAvailabilityZonesRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.disassociate_availability_zones_response.DisassociateAvailabilityZonesResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.disassociate_availability_zones

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.disassociate_availability_zones.disassociate_availability_zones(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.disassociate_availability_zones_request.DisassociateAvailabilityZonesRequest = {
            "availability_zone_mappings": availability_zone_mappings
        }
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_subnets(
        self,
        subnet_ids: "capo_network_firewall.types.az_subnets.AzSubnets",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.disassociate_subnets_response.DisassociateSubnetsResponse":
        """<p>Removes the specified subnet associations from the firewall. This removes the firewall endpoints from the subnets and removes any network filtering protections that the endpoints were providing. </p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            subnet_ids: <p>The unique identifiers for the subnets that you want to disassociate. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.disassociate_subnets_request.DisassociateSubnetsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.disassociate_subnets_response.DisassociateSubnetsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.disassociate_subnets

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.disassociate_subnets.disassociate_subnets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.disassociate_subnets_request.DisassociateSubnetsRequest = {
            "subnet_ids": subnet_ids
        }
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_analysis_report_results(
        self,
        analysis_report_id: "capo_network_firewall.types.analysis_report_id.AnalysisReportId",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        next_token: Optional[
            "capo_network_firewall.types.analysis_report_next_token.AnalysisReportNextToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.get_analysis_report_results_response.GetAnalysisReportResultsResponse":
        """<p>The results of a <code>COMPLETED</code> analysis report generated with <a>StartAnalysisReport</a>.</p> <p>For more information, see <a>AnalysisTypeReportResult</a>. </p>

        Args:
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            analysis_report_id: <p>The unique ID of the query that ran when you requested an analysis report. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.get_analysis_report_results_request.GetAnalysisReportResultsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.get_analysis_report_results_response.GetAnalysisReportResultsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.get_analysis_report_results

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.get_analysis_report_results.get_analysis_report_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.get_analysis_report_results_request.GetAnalysisReportResultsRequest = {
            "analysis_report_id": analysis_report_id
        }
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
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

    def iter_get_analysis_report_results(
        self,
        analysis_report_id: "capo_network_firewall.types.analysis_report_id.AnalysisReportId",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        next_token: Optional[
            "capo_network_firewall.types.analysis_report_next_token.AnalysisReportNextToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.analysis_type_report_result.AnalysisTypeReportResult]":
        _token = next_token
        while True:
            _response = self.get_analysis_report_results(
                analysis_report_id,
                config_overrides=config_overrides,
                firewall_name=firewall_name,
                firewall_arn=firewall_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("analysis_report_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_analysis_reports(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.list_analysis_reports_response.ListAnalysisReportsResponse":
        """<p>Returns a list of all traffic analysis reports generated within the last 30 days.</p>

        Args:
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_analysis_reports_request.ListAnalysisReportsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_analysis_reports_response.ListAnalysisReportsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_analysis_reports

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_analysis_reports.list_analysis_reports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_analysis_reports_request.ListAnalysisReportsRequest = {}
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
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

    def iter_list_analysis_reports(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.analysis_report.AnalysisReport]":
        _token = next_token
        while True:
            _response = self.list_analysis_reports(
                config_overrides=config_overrides,
                firewall_name=firewall_name,
                firewall_arn=firewall_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("analysis_reports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_container_associations(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_network_firewall.types.list_container_associations_response.ListContainerAssociationsResponse":
        """<p>Lists the container associations in your account and Region. Use the <code>NextToken</code> parameter in subsequent requests to retrieve additional results.</p>

        Args:
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_container_associations_request.ListContainerAssociationsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_container_associations_response.ListContainerAssociationsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_container_associations

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_container_associations.list_container_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_container_associations_request.ListContainerAssociationsRequest = {}
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

    def iter_list_container_associations(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.container_association_summary.ContainerAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_container_associations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("container_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_firewall_policies(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.list_firewall_policies_response.ListFirewallPoliciesResponse":
        """<p>Retrieves the metadata for the firewall policies that you have defined. Depending on your setting for max results and the number of firewall policies, a single call might not return the full list. </p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_firewall_policies_request.ListFirewallPoliciesRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_firewall_policies_response.ListFirewallPoliciesResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_firewall_policies

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_firewall_policies.list_firewall_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_firewall_policies_request.ListFirewallPoliciesRequest = {}
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

    def iter_list_firewall_policies(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.firewall_policy_metadata.FirewallPolicyMetadata]":
        _token = next_token
        while True:
            _response = self.list_firewall_policies(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("firewall_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_firewalls(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        vpc_ids: Optional["capo_network_firewall.types.vpc_ids.VpcIds"] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.list_firewalls_response.ListFirewallsResponse":
        """<p>Retrieves the metadata for the firewalls that you have defined. If you provide VPC identifiers in your request, this returns only the firewalls for those VPCs.</p> <p>Depending on your setting for max results and the number of firewalls, a single call might not return the full list. </p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            vpc_ids: <p>The unique identifiers of the VPCs that you want Network Firewall to retrieve the firewalls for. Leave this blank to retrieve all firewalls that you have defined.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_firewalls_request.ListFirewallsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_firewalls_response.ListFirewallsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_firewalls

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_firewalls.list_firewalls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_firewalls_request.ListFirewallsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if vpc_ids is not None:
            input_["vpc_ids"] = vpc_ids
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_firewalls(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        vpc_ids: Optional["capo_network_firewall.types.vpc_ids.VpcIds"] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.firewall_metadata.FirewallMetadata]":
        _token = next_token
        while True:
            _response = self.list_firewalls(
                config_overrides=config_overrides,
                next_token=_token,
                vpc_ids=vpc_ids,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("firewalls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_flow_operation_results(
        self,
        firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        flow_operation_id: "capo_network_firewall.types.flow_operation_id.FlowOperationId",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        availability_zone: Optional[
            "capo_network_firewall.types.availability_zone.AvailabilityZone"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        vpc_endpoint_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.list_flow_operation_results_response.ListFlowOperationResultsResponse":
        """<p>Returns the results of a specific flow operation. </p> <p>Flow operations let you manage the flows tracked in the flow table, also known as the firewall table.</p> <p>A flow is network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort. </p>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p>
            flow_operation_id: <p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            availability_zone: <p>The ID of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>
            vpc_endpoint_id: <p>A unique identifier for the primary endpoint associated with a firewall.</p>
            vpc_endpoint_association_arn: <p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_flow_operation_results_request.ListFlowOperationResultsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_flow_operation_results_response.ListFlowOperationResultsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_flow_operation_results

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_flow_operation_results.list_flow_operation_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_flow_operation_results_request.ListFlowOperationResultsRequest = {
            "firewall_arn": firewall_arn,
            "flow_operation_id": flow_operation_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if vpc_endpoint_association_arn is not None:
            input_["vpc_endpoint_association_arn"] = vpc_endpoint_association_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_flow_operation_results(
        self,
        firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        flow_operation_id: "capo_network_firewall.types.flow_operation_id.FlowOperationId",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        availability_zone: Optional[
            "capo_network_firewall.types.availability_zone.AvailabilityZone"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        vpc_endpoint_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.flow.Flow]":
        _token = next_token
        while True:
            _response = self.list_flow_operation_results(
                firewall_arn,
                flow_operation_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                availability_zone=availability_zone,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_endpoint_association_arn=vpc_endpoint_association_arn,
            )
            _page = _resolve_path(_response, ("flows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_flow_operations(
        self,
        firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        availability_zone: Optional[
            "capo_network_firewall.types.availability_zone.AvailabilityZone"
        ] = None,
        vpc_endpoint_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        flow_operation_type: Optional[
            "capo_network_firewall.types.flow_operation_type.FlowOperationType"
        ] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.list_flow_operations_response.ListFlowOperationsResponse":
        """<p>Returns a list of all flow operations ran in a specific firewall. You can optionally narrow the request scope by specifying the operation type or Availability Zone associated with a firewall's flow operations. </p> <p>Flow operations let you manage the flows tracked in the flow table, also known as the firewall table.</p> <p>A flow is network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort. </p>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p>
            availability_zone: <p>The ID of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>
            vpc_endpoint_association_arn: <p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>
            vpc_endpoint_id: <p>A unique identifier for the primary endpoint associated with a firewall.</p>
            flow_operation_type: <p>An optional string that defines whether any or all operation types are returned.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_flow_operations_request.ListFlowOperationsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_flow_operations_response.ListFlowOperationsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_flow_operations

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_flow_operations.list_flow_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_flow_operations_request.ListFlowOperationsRequest = {
            "firewall_arn": firewall_arn
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if vpc_endpoint_association_arn is not None:
            input_["vpc_endpoint_association_arn"] = vpc_endpoint_association_arn
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if flow_operation_type is not None:
            input_["flow_operation_type"] = flow_operation_type
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

    def iter_list_flow_operations(
        self,
        firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        availability_zone: Optional[
            "capo_network_firewall.types.availability_zone.AvailabilityZone"
        ] = None,
        vpc_endpoint_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        flow_operation_type: Optional[
            "capo_network_firewall.types.flow_operation_type.FlowOperationType"
        ] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.flow_operation_metadata.FlowOperationMetadata]":
        _token = next_token
        while True:
            _response = self.list_flow_operations(
                firewall_arn,
                config_overrides=config_overrides,
                availability_zone=availability_zone,
                vpc_endpoint_association_arn=vpc_endpoint_association_arn,
                vpc_endpoint_id=vpc_endpoint_id,
                flow_operation_type=flow_operation_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("flow_operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_proxies(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.list_proxies_response.ListProxiesResponse":
        """<p>Retrieves the metadata for the proxies that you have defined. Depending on your setting for max results and the number of proxies, a single call might not return the full list. </p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_proxies_request.ListProxiesRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_proxies_response.ListProxiesResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_proxies

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_proxies.list_proxies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_proxies_request.ListProxiesRequest = {}
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

    def iter_list_proxies(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.proxy_metadata.ProxyMetadata]":
        _token = next_token
        while True:
            _response = self.list_proxies(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("proxies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_proxy_configurations(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.list_proxy_configurations_response.ListProxyConfigurationsResponse":
        """<p>Retrieves the metadata for the proxy configuration that you have defined. Depending on your setting for max results and the number of proxy configurations, a single call might not return the full list. </p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_proxy_configurations_request.ListProxyConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_proxy_configurations_response.ListProxyConfigurationsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_proxy_configurations

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_proxy_configurations.list_proxy_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_proxy_configurations_request.ListProxyConfigurationsRequest = {}
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

    def iter_list_proxy_configurations(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.proxy_configuration_metadata.ProxyConfigurationMetadata]":
        _token = next_token
        while True:
            _response = self.list_proxy_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("proxy_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_proxy_rule_groups(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.list_proxy_rule_groups_response.ListProxyRuleGroupsResponse":
        """<p>Retrieves the metadata for the proxy rule groups that you have defined. Depending on your setting for max results and the number of proxy rule groups, a single call might not return the full list. </p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_proxy_rule_groups_request.ListProxyRuleGroupsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_proxy_rule_groups_response.ListProxyRuleGroupsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_proxy_rule_groups

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_proxy_rule_groups.list_proxy_rule_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_proxy_rule_groups_request.ListProxyRuleGroupsRequest = {}
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

    def iter_list_proxy_rule_groups(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.proxy_rule_group_metadata.ProxyRuleGroupMetadata]":
        _token = next_token
        while True:
            _response = self.list_proxy_rule_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("proxy_rule_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_rule_groups(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        scope: Optional[
            "capo_network_firewall.types.resource_managed_status.ResourceManagedStatus"
        ] = None,
        managed_type: Optional[
            "capo_network_firewall.types.resource_managed_type.ResourceManagedType"
        ] = None,
        subscription_status: Optional[
            "capo_network_firewall.types.subscription_status.SubscriptionStatus"
        ] = None,
        type: Optional[
            "capo_network_firewall.types.rule_group_type.RuleGroupType"
        ] = None,
    ) -> "capo_network_firewall.types.list_rule_groups_response.ListRuleGroupsResponse":
        """<p>Retrieves the metadata for the rule groups that you have defined. Depending on your setting for max results and the number of rule groups, a single call might not return the full list. </p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            scope: <p>The scope of the request. The default setting of <code>ACCOUNT</code> or a setting of <code>NULL</code> returns all of the rule groups in your account. A setting of <code>MANAGED</code> returns all available managed rule groups.</p>
            managed_type: <p>Indicates the general category of the Amazon Web Services managed rule group.</p>
            subscription_status: <p>Filters the results to show only rule groups with the specified subscription status. Use this to find subscribed or unsubscribed rule groups.</p>
            type: <p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_rule_groups_request.ListRuleGroupsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_rule_groups_response.ListRuleGroupsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_rule_groups

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_rule_groups.list_rule_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_rule_groups_request.ListRuleGroupsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if scope is not None:
            input_["scope"] = scope
        if managed_type is not None:
            input_["managed_type"] = managed_type
        if subscription_status is not None:
            input_["subscription_status"] = subscription_status
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_rule_groups(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        scope: Optional[
            "capo_network_firewall.types.resource_managed_status.ResourceManagedStatus"
        ] = None,
        managed_type: Optional[
            "capo_network_firewall.types.resource_managed_type.ResourceManagedType"
        ] = None,
        subscription_status: Optional[
            "capo_network_firewall.types.subscription_status.SubscriptionStatus"
        ] = None,
        type: Optional[
            "capo_network_firewall.types.rule_group_type.RuleGroupType"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.rule_group_metadata.RuleGroupMetadata]":
        _token = next_token
        while True:
            _response = self.list_rule_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                scope=scope,
                managed_type=managed_type,
                subscription_status=subscription_status,
                type=type,
            )
            _page = _resolve_path(_response, ("rule_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.tags_pagination_max_results.TagsPaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the tags associated with the specified resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.</p> <p>You can tag the Amazon Web Services resources that you manage through Network Firewall: firewalls, firewall policies, and rule groups. </p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_tags_for_resource

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }
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

    def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.tags_pagination_max_results.TagsPaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.tag.Tag]":
        _token = next_token
        while True:
            _response = self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tls_inspection_configurations(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "capo_network_firewall.types.list_tls_inspection_configurations_response.ListTLSInspectionConfigurationsResponse":
        """<p>Retrieves the metadata for the TLS inspection configurations that you have defined. Depending on your setting for max results and the number of TLS inspection configurations, a single call might not return the full list.</p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_tls_inspection_configurations_request.ListTLSInspectionConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_tls_inspection_configurations_response.ListTLSInspectionConfigurationsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_tls_inspection_configurations

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_tls_inspection_configurations.list_tls_inspection_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_tls_inspection_configurations_request.ListTLSInspectionConfigurationsRequest = {}
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

    def iter_list_tls_inspection_configurations(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.tls_inspection_configuration_metadata.TLSInspectionConfigurationMetadata]":
        _token = next_token
        while True:
            _response = self.list_tls_inspection_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tls_inspection_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_vpc_endpoint_associations(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.list_vpc_endpoint_associations_response.ListVpcEndpointAssociationsResponse":
        """<p>Retrieves the metadata for the VPC endpoint associations that you have defined. If you specify a fireawll, this returns only the endpoint associations for that firewall. </p> <p>Depending on your setting for max results and the number of associations, a single call might not return the full list. </p>

        Args:
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            max_results: <p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>If you don't specify this, Network Firewall retrieves all VPC endpoint associations that you have defined.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.list_vpc_endpoint_associations_request.ListVpcEndpointAssociationsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.list_vpc_endpoint_associations_response.ListVpcEndpointAssociationsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.list_vpc_endpoint_associations

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.list_vpc_endpoint_associations.list_vpc_endpoint_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.list_vpc_endpoint_associations_request.ListVpcEndpointAssociationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_vpc_endpoint_associations(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        next_token: Optional[
            "capo_network_firewall.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "Iterator[capo_network_firewall.types.vpc_endpoint_association_metadata.VpcEndpointAssociationMetadata]":
        _token = next_token
        while True:
            _response = self.list_vpc_endpoint_associations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                firewall_arn=firewall_arn,
            )
            _page = _resolve_path(_response, ("vpc_endpoint_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_resource_policy(
        self,
        resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        policy: "capo_network_firewall.types.policy_string.PolicyString",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates or updates an IAM policy for your rule group, firewall policy, or firewall. Use this to share these resources between accounts. This operation works in conjunction with the Amazon Web Services Resource Access Manager (RAM) service to manage resource sharing for Network Firewall. </p> <p>For information about using sharing with Network Firewall resources, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/sharing.html">Sharing Network Firewall resources</a> in the <i>Network Firewall Developer Guide</i>.</p> <p>Use this operation to create or update a resource policy for your Network Firewall rule group, firewall policy, or firewall. In the resource policy, you specify the accounts that you want to share the Network Firewall resource with and the operations that you want the accounts to be able to perform. </p> <p>When you add an account in the resource policy, you then run the following Resource Access Manager (RAM) operations to access and accept the shared resource. </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareInvitations.html">GetResourceShareInvitations</a> - Returns the Amazon Resource Names (ARNs) of the resource share invitations. </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_AcceptResourceShareInvitation.html">AcceptResourceShareInvitation</a> - Accepts the share invitation for a specified resource share. </p> </li> </ul> <p>For additional information about resource sharing using RAM, see <a href="https://docs.aws.amazon.com/ram/latest/userguide/what-is.html">Resource Access Manager User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the account that you want to share your Network Firewall resources with.</p>
            policy: <p>The IAM policy statement that lists the accounts that you want to share your Network Firewall resources with and the operations that you want the accounts to be able to perform. </p> <p>For a rule group resource, you can specify the following operations in the Actions section of the statement:</p> <ul> <li> <p>network-firewall:CreateFirewallPolicy</p> </li> <li> <p>network-firewall:UpdateFirewallPolicy</p> </li> <li> <p>network-firewall:ListRuleGroups</p> </li> </ul> <p>For a firewall policy resource, you can specify the following operations in the Actions section of the statement:</p> <ul> <li> <p>network-firewall:AssociateFirewallPolicy</p> </li> <li> <p>network-firewall:ListFirewallPolicies</p> </li> </ul> <p>For a firewall resource, you can specify the following operations in the Actions section of the statement:</p> <ul> <li> <p>network-firewall:CreateVpcEndpointAssociation</p> </li> <li> <p>network-firewall:DescribeFirewallMetadata</p> </li> <li> <p>network-firewall:ListFirewalls</p> </li> </ul> <p>In the Resource section of the statement, you specify the ARNs for the Network Firewall resources that you want to share with the account that you specified in <code>Arn</code>.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_resource_policy_exception.InvalidResourcePolicyException: <p>The policy statement failed validation.</p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.put_resource_policy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.put_resource_policy_request.PutResourcePolicyRequest = {
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

    def reject_network_firewall_transit_gateway_attachment(
        self,
        transit_gateway_attachment_id: "capo_network_firewall.types.transit_gateway_attachment_id.TransitGatewayAttachmentId",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.reject_network_firewall_transit_gateway_attachment_response.RejectNetworkFirewallTransitGatewayAttachmentResponse":
        """<p>Rejects a transit gateway attachment request for Network Firewall. When you reject the attachment request, Network Firewall cancels the creation of routing components between the transit gateway and firewall endpoints.</p> <p>Only the transit gateway owner can reject the attachment. After rejection, no traffic will flow through the firewall endpoints for this attachment.</p> <p>Use <a>DescribeFirewall</a> to monitor the rejection status. To accept the attachment instead of rejecting it, use <a>AcceptNetworkFirewallTransitGatewayAttachment</a>.</p> <note> <p>Once rejected, you cannot reverse this action. To establish connectivity, you must create a new transit gateway-attached firewall.</p> </note>

        Args:
            transit_gateway_attachment_id: <p>Required. The unique identifier of the transit gateway attachment to reject. This ID is returned in the response when creating a transit gateway-attached firewall.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.reject_network_firewall_transit_gateway_attachment_request.RejectNetworkFirewallTransitGatewayAttachmentRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.reject_network_firewall_transit_gateway_attachment_response.RejectNetworkFirewallTransitGatewayAttachmentResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.reject_network_firewall_transit_gateway_attachment

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.reject_network_firewall_transit_gateway_attachment.reject_network_firewall_transit_gateway_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.reject_network_firewall_transit_gateway_attachment_request.RejectNetworkFirewallTransitGatewayAttachmentRequest = {
            "transit_gateway_attachment_id": transit_gateway_attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_analysis_report(
        self,
        analysis_type: "capo_network_firewall.types.enabled_analysis_type.EnabledAnalysisType",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.start_analysis_report_response.StartAnalysisReportResponse":
        """<p>Generates a traffic analysis report for the timeframe and traffic type you specify.</p> <p>For information on the contents of a traffic analysis report, see <a>AnalysisReport</a>.</p>

        Args:
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            analysis_type: <p>The type of traffic that will be used to generate a report. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.start_analysis_report_request.StartAnalysisReportRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.start_analysis_report_response.StartAnalysisReportResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.start_analysis_report

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.start_analysis_report.start_analysis_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.start_analysis_report_request.StartAnalysisReportRequest = {
            "analysis_type": analysis_type
        }
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_flow_capture(
        self,
        firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        flow_filters: "capo_network_firewall.types.flow_filters.FlowFilters",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        availability_zone: Optional[
            "capo_network_firewall.types.availability_zone.AvailabilityZone"
        ] = None,
        vpc_endpoint_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        minimum_flow_age_in_seconds: Optional[
            "capo_network_firewall.types.age.Age"
        ] = None,
    ) -> "capo_network_firewall.types.start_flow_capture_response.StartFlowCaptureResponse":
        """<p>Begins capturing the flows in a firewall, according to the filters you define. Captures are similar, but not identical to snapshots. Capture operations provide visibility into flows that are not closed and are tracked by a firewall's flow table. Unlike snapshots, captures are a time-boxed view. </p> <p>A flow is network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort. </p> <note> <p>To avoid encountering operation limits, you should avoid starting captures with broad filters, like wide IP ranges. Instead, we recommend you define more specific criteria with <code>FlowFilters</code>, like narrow IP ranges, ports, or protocols.</p> </note>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p>
            availability_zone: <p>The ID of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>
            vpc_endpoint_association_arn: <p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>
            vpc_endpoint_id: <p>A unique identifier for the primary endpoint associated with a firewall.</p>
            minimum_flow_age_in_seconds: <p>The reqested <code>FlowOperation</code> ignores flows with an age (in seconds) lower than <code>MinimumFlowAgeInSeconds</code>. You provide this for start commands.</p> <note> <p>We recommend setting this value to at least 1 minute (60 seconds) to reduce chance of capturing flows that are not yet established.</p> </note>
            flow_filters: <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.start_flow_capture_request.StartFlowCaptureRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.start_flow_capture_response.StartFlowCaptureResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.start_flow_capture

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.start_flow_capture.start_flow_capture(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.start_flow_capture_request.StartFlowCaptureRequest = {
            "firewall_arn": firewall_arn,
            "flow_filters": flow_filters,
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if vpc_endpoint_association_arn is not None:
            input_["vpc_endpoint_association_arn"] = vpc_endpoint_association_arn
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if minimum_flow_age_in_seconds is not None:
            input_["minimum_flow_age_in_seconds"] = minimum_flow_age_in_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_flow_flush(
        self,
        firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        flow_filters: "capo_network_firewall.types.flow_filters.FlowFilters",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        availability_zone: Optional[
            "capo_network_firewall.types.availability_zone.AvailabilityZone"
        ] = None,
        vpc_endpoint_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        minimum_flow_age_in_seconds: Optional[
            "capo_network_firewall.types.age.Age"
        ] = None,
    ) -> "capo_network_firewall.types.start_flow_flush_response.StartFlowFlushResponse":
        """<p>Begins the flushing of traffic from the firewall, according to the filters you define. When the operation starts, impacted flows are temporarily marked as timed out before the Suricata engine prunes, or flushes, the flows from the firewall table.</p> <important> <p>While the flush completes, impacted flows are processed as midstream traffic. This may result in a temporary increase in midstream traffic metrics. We recommend that you double check your stream exception policy before you perform a flush operation.</p> </important>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p>
            availability_zone: <p>The ID of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>
            vpc_endpoint_association_arn: <p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>
            vpc_endpoint_id: <p>A unique identifier for the primary endpoint associated with a firewall.</p>
            minimum_flow_age_in_seconds: <p>The reqested <code>FlowOperation</code> ignores flows with an age (in seconds) lower than <code>MinimumFlowAgeInSeconds</code>. You provide this for start commands.</p>
            flow_filters: <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.start_flow_flush_request.StartFlowFlushRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.start_flow_flush_response.StartFlowFlushResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.start_flow_flush

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.start_flow_flush.start_flow_flush(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.start_flow_flush_request.StartFlowFlushRequest = {
            "firewall_arn": firewall_arn,
            "flow_filters": flow_filters,
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if vpc_endpoint_association_arn is not None:
            input_["vpc_endpoint_association_arn"] = vpc_endpoint_association_arn
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if minimum_flow_age_in_seconds is not None:
            input_["minimum_flow_age_in_seconds"] = minimum_flow_age_in_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        tags: "capo_network_firewall.types.tag_list.TagList",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.</p> <p>You can tag the Amazon Web Services resources that you manage through Network Firewall: firewalls, firewall policies, and rule groups. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p></p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.tag_resource

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn",
        tag_keys: "capo_network_firewall.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
    ) -> "capo_network_firewall.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the tags with the specified keys from the specified resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.</p> <p>You can manage tags for the Amazon Web Services resources that you manage through Network Firewall: firewalls, firewall policies, and rule groups. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p></p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.untag_resource

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.untag_resource_request.UntagResourceRequest = {
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

    def update_availability_zone_change_protection(
        self,
        availability_zone_change_protection: "capo_network_firewall.types.boolean.Boolean",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.update_availability_zone_change_protection_response.UpdateAvailabilityZoneChangeProtectionResponse":
        """<p>Modifies the <code>AvailabilityZoneChangeProtection</code> setting for a transit gateway-attached firewall. When enabled, this setting prevents accidental changes to the firewall's Availability Zone configuration. This helps protect against disrupting traffic flow in production environments.</p> <p>When enabled, you must disable this protection before using <a>AssociateAvailabilityZones</a> or <a>DisassociateAvailabilityZones</a> to modify the firewall's Availability Zone configuration.</p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            availability_zone_change_protection: <p>A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.resource_owner_check_exception.ResourceOwnerCheckException: <p>Unable to change the resource because your account doesn't own it. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_availability_zone_change_protection_request.UpdateAvailabilityZoneChangeProtectionRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_availability_zone_change_protection_response.UpdateAvailabilityZoneChangeProtectionResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_availability_zone_change_protection

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_availability_zone_change_protection.update_availability_zone_change_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_availability_zone_change_protection_request.UpdateAvailabilityZoneChangeProtectionRequest = {
            "availability_zone_change_protection": availability_zone_change_protection
        }
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_container_association(
        self,
        type: "capo_network_firewall.types.container_monitoring_type.ContainerMonitoringType",
        container_monitoring_configurations: "capo_network_firewall.types.container_monitoring_configurations.ContainerMonitoringConfigurations",
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        container_association_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        container_association_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        tags: Optional["capo_network_firewall.types.tag_list.TagList"] = None,
    ) -> "capo_network_firewall.types.update_container_association_response.UpdateContainerAssociationResponse":
        """<p>Updates the monitoring configurations and description of a container association. You can't change the container type after creation. Provide an update token to enable optimistic concurrency control.</p>

        Args:
            container_association_name: <p>The descriptive name of the container association.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            container_association_arn: <p>The Amazon Resource Name (ARN) of the container association.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            description: <p>A description of the container association. When omitted, the existing description remains unchanged. To clear the description, pass an empty string.</p>
            type: <p>The container type. This value must match the existing type and can't be changed. Valid values:</p> <ul> <li> <p> <code>ECS</code> - Amazon Elastic Container Service</p> </li> <li> <p> <code>EKS</code> - Amazon Elastic Kubernetes Service</p> </li> </ul>
            container_monitoring_configurations: <p>The updated monitoring configurations for the container association. Each configuration specifies an Amazon ECS or Amazon EKS cluster to monitor and optional attribute filters.</p>
            tags: <p>The key:value pairs to associate with the resource.</p>
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the container association. The token marks the state of the container association resource at the time of the request.</p> <p>To make changes to the container association, you provide the token in your request. Network Firewall uses the token to ensure that the container association hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the container association again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_container_association_request.UpdateContainerAssociationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_container_association_response.UpdateContainerAssociationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_container_association

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_container_association.update_container_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_container_association_request.UpdateContainerAssociationRequest = {
            "type": type,
            "container_monitoring_configurations": container_monitoring_configurations,
            "update_token": update_token,
        }
        if container_association_name is not None:
            input_["container_association_name"] = container_association_name
        if container_association_arn is not None:
            input_["container_association_arn"] = container_association_arn
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_firewall_analysis_settings(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        enabled_analysis_types: Optional[
            "capo_network_firewall.types.enabled_analysis_types.EnabledAnalysisTypes"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
    ) -> "capo_network_firewall.types.update_firewall_analysis_settings_response.UpdateFirewallAnalysisSettingsResponse":
        """<p>Enables specific types of firewall analysis on a specific firewall you define.</p>

        Args:
            enabled_analysis_types: <p>An optional setting indicating the specific traffic analysis types to enable on the firewall. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_firewall_analysis_settings_request.UpdateFirewallAnalysisSettingsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_firewall_analysis_settings_response.UpdateFirewallAnalysisSettingsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_firewall_analysis_settings

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_firewall_analysis_settings.update_firewall_analysis_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_firewall_analysis_settings_request.UpdateFirewallAnalysisSettingsRequest = {}
        if enabled_analysis_types is not None:
            input_["enabled_analysis_types"] = enabled_analysis_types
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if update_token is not None:
            input_["update_token"] = update_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_firewall_delete_protection(
        self,
        delete_protection: "capo_network_firewall.types.boolean.Boolean",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.update_firewall_delete_protection_response.UpdateFirewallDeleteProtectionResponse":
        """<p>Modifies the flag, <code>DeleteProtection</code>, which indicates whether it is possible to delete the firewall. If the flag is set to <code>TRUE</code>, the firewall is protected against deletion. This setting helps protect against accidentally deleting a firewall that's in use. </p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            delete_protection: <p>A flag indicating whether it is possible to delete the firewall. A setting of <code>TRUE</code> indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to <code>TRUE</code>.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.resource_owner_check_exception.ResourceOwnerCheckException: <p>Unable to change the resource because your account doesn't own it. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_firewall_delete_protection_request.UpdateFirewallDeleteProtectionRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_firewall_delete_protection_response.UpdateFirewallDeleteProtectionResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_firewall_delete_protection

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_firewall_delete_protection.update_firewall_delete_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_firewall_delete_protection_request.UpdateFirewallDeleteProtectionRequest = {
            "delete_protection": delete_protection
        }
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_firewall_description(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
    ) -> "capo_network_firewall.types.update_firewall_description_response.UpdateFirewallDescriptionResponse":
        """<p>Modifies the description for the specified firewall. Use the description to help you identify the firewall when you're working with it. </p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            description: <p>The new description for the firewall. If you omit this setting, Network Firewall removes the description for the firewall.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_firewall_description_request.UpdateFirewallDescriptionRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_firewall_description_response.UpdateFirewallDescriptionResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_firewall_description

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_firewall_description.update_firewall_description(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_firewall_description_request.UpdateFirewallDescriptionRequest = {}
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_firewall_encryption_configuration(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        encryption_configuration: Optional[
            "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_network_firewall.types.update_firewall_encryption_configuration_response.UpdateFirewallEncryptionConfigurationResponse":
        """<p>A complex type that contains settings for encryption of your firewall resources.</p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.resource_owner_check_exception.ResourceOwnerCheckException: <p>Unable to change the resource because your account doesn't own it. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_firewall_encryption_configuration_request.UpdateFirewallEncryptionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_firewall_encryption_configuration_response.UpdateFirewallEncryptionConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_firewall_encryption_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_firewall_encryption_configuration.update_firewall_encryption_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_firewall_encryption_configuration_request.UpdateFirewallEncryptionConfigurationRequest = {}
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_firewall_policy(
        self,
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        firewall_policy: "capo_network_firewall.types.firewall_policy.FirewallPolicy",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_policy_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_policy_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        dry_run: Optional["capo_network_firewall.types.boolean.Boolean"] = None,
        encryption_configuration: Optional[
            "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_network_firewall.types.update_firewall_policy_response.UpdateFirewallPolicyResponse":
        """<p>Updates the properties of the specified firewall policy.</p>

        Args:
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request. </p> <p>To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_policy_arn: <p>The Amazon Resource Name (ARN) of the firewall policy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_policy_name: <p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_policy: <p>The updated firewall policy to use for the firewall. You can't add or remove a <a>TLSInspectionConfiguration</a> after you create a firewall policy. However, you can replace an existing TLS inspection configuration with another <code>TLSInspectionConfiguration</code>.</p>
            description: <p>A description of the firewall policy.</p>
            dry_run: <p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>
            encryption_configuration: <p>A complex type that contains settings for encryption of your firewall policy resources.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_firewall_policy_request.UpdateFirewallPolicyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_firewall_policy_response.UpdateFirewallPolicyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_firewall_policy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_firewall_policy.update_firewall_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_firewall_policy_request.UpdateFirewallPolicyRequest = {
            "update_token": update_token,
            "firewall_policy": firewall_policy,
        }
        if firewall_policy_arn is not None:
            input_["firewall_policy_arn"] = firewall_policy_arn
        if firewall_policy_name is not None:
            input_["firewall_policy_name"] = firewall_policy_name
        if description is not None:
            input_["description"] = description
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_firewall_policy_change_protection(
        self,
        firewall_policy_change_protection: "capo_network_firewall.types.boolean.Boolean",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.update_firewall_policy_change_protection_response.UpdateFirewallPolicyChangeProtectionResponse":
        """<p>Modifies the flag, <code>ChangeProtection</code>, which indicates whether it is possible to change the firewall. If the flag is set to <code>TRUE</code>, the firewall is protected from changes. This setting helps protect against accidentally changing a firewall that's in use.</p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_policy_change_protection: <p>A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.resource_owner_check_exception.ResourceOwnerCheckException: <p>Unable to change the resource because your account doesn't own it. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_firewall_policy_change_protection_request.UpdateFirewallPolicyChangeProtectionRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_firewall_policy_change_protection_response.UpdateFirewallPolicyChangeProtectionResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_firewall_policy_change_protection

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_firewall_policy_change_protection.update_firewall_policy_change_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_firewall_policy_change_protection_request.UpdateFirewallPolicyChangeProtectionRequest = {
            "firewall_policy_change_protection": firewall_policy_change_protection
        }
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_logging_configuration(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        logging_configuration: Optional[
            "capo_network_firewall.types.logging_configuration.LoggingConfiguration"
        ] = None,
        enable_monitoring_dashboard: Optional[
            "capo_network_firewall.types.enable_monitoring_dashboard.EnableMonitoringDashboard"
        ] = None,
    ) -> "capo_network_firewall.types.update_logging_configuration_response.UpdateLoggingConfigurationResponse":
        """<p>Sets the logging configuration for the specified firewall. </p> <p>To change the logging configuration, retrieve the <a>LoggingConfiguration</a> by calling <a>DescribeLoggingConfiguration</a>, then change it and provide the modified object to this update call. You must change the logging configuration one <a>LogDestinationConfig</a> at a time inside the retrieved <a>LoggingConfiguration</a> object. </p> <p>You can perform only one of the following actions in any call to <code>UpdateLoggingConfiguration</code>: </p> <ul> <li> <p>Create a new log destination object by adding a single <code>LogDestinationConfig</code> array element to <code>LogDestinationConfigs</code>.</p> </li> <li> <p>Delete a log destination object by removing a single <code>LogDestinationConfig</code> array element from <code>LogDestinationConfigs</code>.</p> </li> <li> <p>Change the <code>LogDestination</code> setting in a single <code>LogDestinationConfig</code> array element.</p> </li> </ul> <p>You can't change the <code>LogDestinationType</code> or <code>LogType</code> in a <code>LogDestinationConfig</code>. To change these settings, delete the existing <code>LogDestinationConfig</code> object and create a new one, using two separate calls to this update operation.</p>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            logging_configuration: <p>Defines how Network Firewall performs logging for a firewall. If you omit this setting, Network Firewall disables logging for the firewall.</p>
            enable_monitoring_dashboard: <p>A boolean that lets you enable or disable the detailed firewall monitoring dashboard on the firewall. </p> <p>The monitoring dashboard provides comprehensive visibility into your firewall's flow logs and alert logs. After you enable detailed monitoring, you can access these dashboards directly from the <b>Monitoring</b> page of the Network Firewall console.</p> <p> Specify <code>TRUE</code> to enable the the detailed monitoring dashboard on the firewall. Specify <code>FALSE</code> to disable the the detailed monitoring dashboard on the firewall. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.log_destination_permission_exception.LogDestinationPermissionException: <p>Unable to send logs to a configured logging destination. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_logging_configuration_request.UpdateLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_logging_configuration_response.UpdateLoggingConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_logging_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_logging_configuration.update_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_logging_configuration_request.UpdateLoggingConfigurationRequest = {}
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if enable_monitoring_dashboard is not None:
            input_["enable_monitoring_dashboard"] = enable_monitoring_dashboard

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_proxy(
        self,
        nat_gateway_id: "capo_network_firewall.types.nat_gateway_id.NatGatewayId",
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        listener_properties_to_add: Optional[
            "capo_network_firewall.types.listener_properties_request.ListenerPropertiesRequest"
        ] = None,
        listener_properties_to_remove: Optional[
            "capo_network_firewall.types.listener_properties_request.ListenerPropertiesRequest"
        ] = None,
        tls_intercept_properties: Optional[
            "capo_network_firewall.types.tls_intercept_properties_request.TlsInterceptPropertiesRequest"
        ] = None,
    ) -> "capo_network_firewall.types.update_proxy_response.UpdateProxyResponse":
        """<p>Updates the properties of the specified proxy.</p>

        Args:
            nat_gateway_id: <p>The NAT Gateway the proxy is attached to. </p>
            proxy_name: <p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_arn: <p>The Amazon Resource Name (ARN) of a proxy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            listener_properties_to_add: <p>Listener properties for HTTP and HTTPS traffic to add. </p>
            listener_properties_to_remove: <p>Listener properties for HTTP and HTTPS traffic to remove. </p>
            tls_intercept_properties: <p>TLS decryption on traffic to filter on attributes in the HTTP header. </p>
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy. The token marks the state of the proxy resource at the time of the request. </p> <p>To make changes to the proxy, you provide the token in your request. Network Firewall uses the token to ensure that the proxy hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation you requested isn't supported by Network Firewall. </p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_proxy_request.UpdateProxyRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_proxy_response.UpdateProxyResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_proxy

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_proxy.update_proxy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_proxy_request.UpdateProxyRequest = {
            "nat_gateway_id": nat_gateway_id,
            "update_token": update_token,
        }
        if proxy_name is not None:
            input_["proxy_name"] = proxy_name
        if proxy_arn is not None:
            input_["proxy_arn"] = proxy_arn
        if listener_properties_to_add is not None:
            input_["listener_properties_to_add"] = listener_properties_to_add
        if listener_properties_to_remove is not None:
            input_["listener_properties_to_remove"] = listener_properties_to_remove
        if tls_intercept_properties is not None:
            input_["tls_intercept_properties"] = tls_intercept_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_proxy_configuration(
        self,
        default_rule_phase_actions: "capo_network_firewall.types.proxy_config_default_rule_phase_actions_request.ProxyConfigDefaultRulePhaseActionsRequest",
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.update_proxy_configuration_response.UpdateProxyConfigurationResponse":
        """<p>Updates the properties of the specified proxy configuration.</p>

        Args:
            proxy_configuration_name: <p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_configuration_arn: <p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            default_rule_phase_actions: <p>Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. </p>
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request. </p> <p>To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_proxy_configuration_request.UpdateProxyConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_proxy_configuration_response.UpdateProxyConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_proxy_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_proxy_configuration.update_proxy_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_proxy_configuration_request.UpdateProxyConfigurationRequest = {
            "default_rule_phase_actions": default_rule_phase_actions,
            "update_token": update_token,
        }
        if proxy_configuration_name is not None:
            input_["proxy_configuration_name"] = proxy_configuration_name
        if proxy_configuration_arn is not None:
            input_["proxy_configuration_arn"] = proxy_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_proxy_rule(
        self,
        proxy_rule_name: "capo_network_firewall.types.resource_name.ResourceName",
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        action: Optional[
            "capo_network_firewall.types.proxy_rule_phase_action.ProxyRulePhaseAction"
        ] = None,
        add_conditions: Optional[
            "capo_network_firewall.types.proxy_rule_condition_list.ProxyRuleConditionList"
        ] = None,
        remove_conditions: Optional[
            "capo_network_firewall.types.proxy_rule_condition_list.ProxyRuleConditionList"
        ] = None,
    ) -> (
        "capo_network_firewall.types.update_proxy_rule_response.UpdateProxyRuleResponse"
    ):
        """<p>Updates the properties of the specified proxy rule.</p>

        Args:
            proxy_rule_group_name: <p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_rule_group_arn: <p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_rule_name: <p>The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.</p>
            description: <p>A description of the proxy rule. </p>
            action: <p>Depending on the match action, the proxy either stops the evaluation (if the action is terminal - allow or deny), or continues it (if the action is alert) until it matches a rule with a terminal action. </p>
            add_conditions: <p>Proxy rule conditions to add. Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against. </p>
            remove_conditions: <p>Proxy rule conditions to remove. Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against. </p>
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule. The token marks the state of the proxy rule resource at the time of the request. </p> <p>To make changes to the proxy rule, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy rule again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_proxy_rule_request.UpdateProxyRuleRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_proxy_rule_response.UpdateProxyRuleResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_proxy_rule

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_proxy_rule.update_proxy_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_proxy_rule_request.UpdateProxyRuleRequest = {
            "proxy_rule_name": proxy_rule_name,
            "update_token": update_token,
        }
        if proxy_rule_group_name is not None:
            input_["proxy_rule_group_name"] = proxy_rule_group_name
        if proxy_rule_group_arn is not None:
            input_["proxy_rule_group_arn"] = proxy_rule_group_arn
        if description is not None:
            input_["description"] = description
        if action is not None:
            input_["action"] = action
        if add_conditions is not None:
            input_["add_conditions"] = add_conditions
        if remove_conditions is not None:
            input_["remove_conditions"] = remove_conditions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_proxy_rule_group_priorities(
        self,
        rule_groups: "capo_network_firewall.types.proxy_rule_group_priority_list.ProxyRuleGroupPriorityList",
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.update_proxy_rule_group_priorities_response.UpdateProxyRuleGroupPrioritiesResponse":
        """<p>Updates proxy rule group priorities within a proxy configuration.</p>

        Args:
            proxy_configuration_name: <p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_configuration_arn: <p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_groups: <p>proxy rule group resources to update to new positions. </p>
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request. </p> <p>To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_proxy_rule_group_priorities_request.UpdateProxyRuleGroupPrioritiesRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_proxy_rule_group_priorities_response.UpdateProxyRuleGroupPrioritiesResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_proxy_rule_group_priorities

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_proxy_rule_group_priorities.update_proxy_rule_group_priorities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_proxy_rule_group_priorities_request.UpdateProxyRuleGroupPrioritiesRequest = {
            "rule_groups": rule_groups,
            "update_token": update_token,
        }
        if proxy_configuration_name is not None:
            input_["proxy_configuration_name"] = proxy_configuration_name
        if proxy_configuration_arn is not None:
            input_["proxy_configuration_arn"] = proxy_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_proxy_rule_priorities(
        self,
        rule_group_request_phase: "capo_network_firewall.types.rule_group_request_phase.RuleGroupRequestPhase",
        rules: "capo_network_firewall.types.proxy_rule_priority_list.ProxyRulePriorityList",
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        proxy_rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        proxy_rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_network_firewall.types.update_proxy_rule_priorities_response.UpdateProxyRulePrioritiesResponse":
        """<p>Updates proxy rule priorities within a proxy rule group.</p>

        Args:
            proxy_rule_group_name: <p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            proxy_rule_group_arn: <p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_group_request_phase: <p>Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. </p>
            rules: <p>proxy rule resources to update to new positions. </p>
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule group. The token marks the state of the proxy rule group resource at the time of the request. </p> <p>To make changes to the proxy rule group, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_proxy_rule_priorities_request.UpdateProxyRulePrioritiesRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_proxy_rule_priorities_response.UpdateProxyRulePrioritiesResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_proxy_rule_priorities

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_proxy_rule_priorities.update_proxy_rule_priorities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_proxy_rule_priorities_request.UpdateProxyRulePrioritiesRequest = {
            "rule_group_request_phase": rule_group_request_phase,
            "rules": rules,
            "update_token": update_token,
        }
        if proxy_rule_group_name is not None:
            input_["proxy_rule_group_name"] = proxy_rule_group_name
        if proxy_rule_group_arn is not None:
            input_["proxy_rule_group_arn"] = proxy_rule_group_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_proxy_settings(
        self,
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        proxy_settings: Optional[
            "capo_network_firewall.types.proxy_settings.ProxySettings"
        ] = None,
    ) -> "capo_network_firewall.types.update_proxy_settings_response.UpdateProxySettingsResponse":
        """<p>Modifies the proxy listener configuration of a proxy mode firewall. Proxy mode firewalls are created with <code>NoSourcePreservation</code> set to <code>TRUE</code>. Use this operation to change the ports and protocols on which the firewall's proxy listens for traffic. </p>

        Args:
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            proxy_settings: <p>The proxy listener configuration to set on the firewall. This specifies the ports and protocols on which the firewall's proxy listens for traffic. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_operation_exception.InvalidOperationException: <p>The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.</p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.resource_owner_check_exception.ResourceOwnerCheckException: <p>Unable to change the resource because your account doesn't own it. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_proxy_settings_request.UpdateProxySettingsRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_proxy_settings_response.UpdateProxySettingsResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_proxy_settings

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_proxy_settings.update_proxy_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_proxy_settings_request.UpdateProxySettingsRequest = {}
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name
        if update_token is not None:
            input_["update_token"] = update_token
        if proxy_settings is not None:
            input_["proxy_settings"] = proxy_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rule_group(
        self,
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        rule_group_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        rule_group_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        rule_group: Optional["capo_network_firewall.types.rule_group.RuleGroup"] = None,
        rules: Optional["capo_network_firewall.types.rules_string.RulesString"] = None,
        type: Optional[
            "capo_network_firewall.types.rule_group_type.RuleGroupType"
        ] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        dry_run: Optional["capo_network_firewall.types.boolean.Boolean"] = None,
        encryption_configuration: Optional[
            "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        source_metadata: Optional[
            "capo_network_firewall.types.source_metadata.SourceMetadata"
        ] = None,
        analyze_rule_group: Optional[
            "capo_network_firewall.types.boolean.Boolean"
        ] = None,
        summary_configuration: Optional[
            "capo_network_firewall.types.summary_configuration.SummaryConfiguration"
        ] = None,
    ) -> (
        "capo_network_firewall.types.update_rule_group_response.UpdateRuleGroupResponse"
    ):
        """<p>Updates the rule settings for the specified rule group. You use a rule group by reference in one or more firewall policies. When you modify a rule group, you modify all firewall policies that use the rule group. </p> <p>To update a rule group, first call <a>DescribeRuleGroup</a> to retrieve the current <a>RuleGroup</a> object, update the object as needed, and then provide the updated object to this call. </p>

        Args:
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request. </p> <p>To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>
            rule_group_arn: <p>The Amazon Resource Name (ARN) of the rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_group_name: <p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            rule_group: <p>An object that defines the rule group rules. </p> <note> <p>You must provide either this rule group setting or a <code>Rules</code> setting, but not both. </p> </note>
            rules: <p>A string containing stateful rule group rules specifications in Suricata flat format, with one rule per line. Use this to import your existing Suricata compatible rule groups. </p> <note> <p>You must provide either this rules setting or a populated <code>RuleGroup</code> setting, but not both. </p> </note> <p>You can provide your rule group specification in Suricata flat format through this setting when you create or update your rule group. The call response returns a <a>RuleGroup</a> object that Network Firewall has populated from your string. </p>
            type: <p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p> <note> <p>This setting is required for requests that do not include the <code>RuleGroupARN</code>.</p> </note>
            description: <p>A description of the rule group. </p>
            dry_run: <p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>
            encryption_configuration: <p>A complex type that contains settings for encryption of your rule group resources.</p>
            source_metadata: <p>A complex type that contains metadata about the rule group that your own rule group is copied from. You can use the metadata to keep track of updates made to the originating rule group.</p>
            analyze_rule_group: <p>Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to <code>TRUE</code>, Network Firewall runs the analysis and then updates the rule group for you. To run the stateless rule group analyzer without updating the rule group, set <code>DryRun</code> to <code>TRUE</code>. </p>
            summary_configuration: <p>Updates the selected summary configuration for a rule group.</p> <p>Changes affect subsequent responses from <a>DescribeRuleGroupSummary</a>.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_rule_group_request.UpdateRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_rule_group_response.UpdateRuleGroupResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_rule_group

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_rule_group.update_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_rule_group_request.UpdateRuleGroupRequest = {
            "update_token": update_token
        }
        if rule_group_arn is not None:
            input_["rule_group_arn"] = rule_group_arn
        if rule_group_name is not None:
            input_["rule_group_name"] = rule_group_name
        if rule_group is not None:
            input_["rule_group"] = rule_group
        if rules is not None:
            input_["rules"] = rules
        if type is not None:
            input_["type"] = type
        if description is not None:
            input_["description"] = description
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if source_metadata is not None:
            input_["source_metadata"] = source_metadata
        if analyze_rule_group is not None:
            input_["analyze_rule_group"] = analyze_rule_group
        if summary_configuration is not None:
            input_["summary_configuration"] = summary_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_subnet_change_protection(
        self,
        subnet_change_protection: "capo_network_firewall.types.boolean.Boolean",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        update_token: Optional[
            "capo_network_firewall.types.update_token.UpdateToken"
        ] = None,
        firewall_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        firewall_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_network_firewall.types.update_subnet_change_protection_response.UpdateSubnetChangeProtectionResponse":
        """<p></p>

        Args:
            update_token: <p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>
            firewall_arn: <p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            firewall_name: <p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>
            subnet_change_protection: <p>A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.resource_owner_check_exception.ResourceOwnerCheckException: <p>Unable to change the resource because your account doesn't own it. </p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_subnet_change_protection_request.UpdateSubnetChangeProtectionRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_subnet_change_protection_response.UpdateSubnetChangeProtectionResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_subnet_change_protection

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_subnet_change_protection.update_subnet_change_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_subnet_change_protection_request.UpdateSubnetChangeProtectionRequest = {
            "subnet_change_protection": subnet_change_protection
        }
        if update_token is not None:
            input_["update_token"] = update_token
        if firewall_arn is not None:
            input_["firewall_arn"] = firewall_arn
        if firewall_name is not None:
            input_["firewall_name"] = firewall_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_tls_inspection_configuration(
        self,
        tls_inspection_configuration: "capo_network_firewall.types.tls_inspection_configuration.TLSInspectionConfiguration",
        update_token: "capo_network_firewall.types.update_token.UpdateToken",
        *,
        config_overrides: Optional[NetworkFirewallClientConfig] = None,
        tls_inspection_configuration_arn: Optional[
            "capo_network_firewall.types.resource_arn.ResourceArn"
        ] = None,
        tls_inspection_configuration_name: Optional[
            "capo_network_firewall.types.resource_name.ResourceName"
        ] = None,
        description: Optional[
            "capo_network_firewall.types.description.Description"
        ] = None,
        encryption_configuration: Optional[
            "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_network_firewall.types.update_tls_inspection_configuration_response.UpdateTLSInspectionConfigurationResponse":
        """<p>Updates the TLS inspection configuration settings for the specified TLS inspection configuration. You use a TLS inspection configuration by referencing it in one or more firewall policies. When you modify a TLS inspection configuration, you modify all firewall policies that use the TLS inspection configuration. </p> <p>To update a TLS inspection configuration, first call <a>DescribeTLSInspectionConfiguration</a> to retrieve the current <a>TLSInspectionConfiguration</a> object, update the object as needed, and then provide the updated object to this call. </p>

        Args:
            tls_inspection_configuration_arn: <p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p>
            tls_inspection_configuration_name: <p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p>
            tls_inspection_configuration: <p>The object that defines a TLS inspection configuration. This, along with <a>TLSInspectionConfigurationResponse</a>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a>. </p> <p>Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.</p> <p>To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html">Inspecting SSL/TLS traffic with TLS inspection configurations</a> in the <i>Network Firewall Developer Guide</i>.</p>
            description: <p>A description of the TLS inspection configuration. </p>
            encryption_configuration: <p>A complex type that contains the Amazon Web Services KMS encryption configuration settings for your TLS inspection configuration.</p>
            update_token: <p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the TLS inspection configuration. The token marks the state of the TLS inspection configuration resource at the time of the request. </p> <p>To make changes to the TLS inspection configuration, you provide the token in your request. Network Firewall uses the token to ensure that the TLS inspection configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the TLS inspection configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>

        Raises:
            capo_network_firewall.errors.internal_server_error.InternalServerError: <p>Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request. </p>
            capo_network_firewall.errors.invalid_request_exception.InvalidRequestException: <p>The operation failed because of a problem with your request. Examples include: </p> <ul> <li> <p>You specified an unsupported parameter name or value.</p> </li> <li> <p>You tried to update a property with a value that isn't among the available types.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.</p> </li> </ul>
            capo_network_firewall.errors.invalid_token_exception.InvalidTokenException: <p>The token you provided is stale or isn't valid for the operation. </p>
            capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to locate a resource using the parameters that you provided.</p>
            capo_network_firewall.errors.throttling_exception.ThrottlingException: <p>Unable to process the request due to throttling limitations.</p>
            capo_network_firewall.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_network_firewall.types.update_tls_inspection_configuration_request.UpdateTLSInspectionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_firewall.types.update_tls_inspection_configuration_response.UpdateTLSInspectionConfigurationResponse"
        ]:
            import capo_network_firewall._operations.network_firewall_20201112.update_tls_inspection_configuration

            output, http_response = (
                capo_network_firewall._operations.network_firewall_20201112.update_tls_inspection_configuration.update_tls_inspection_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_firewall.types.update_tls_inspection_configuration_request.UpdateTLSInspectionConfigurationRequest = {
            "tls_inspection_configuration": tls_inspection_configuration,
            "update_token": update_token,
        }
        if tls_inspection_configuration_arn is not None:
            input_["tls_inspection_configuration_arn"] = (
                tls_inspection_configuration_arn
            )
        if tls_inspection_configuration_name is not None:
            input_["tls_inspection_configuration_name"] = (
                tls_inspection_configuration_name
            )
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

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
