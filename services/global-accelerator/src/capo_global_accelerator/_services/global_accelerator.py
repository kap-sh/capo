"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#GlobalAccelerator_V20180706``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_global_accelerator._auth._signers
import capo_global_accelerator._auth._sigv4
from capo_global_accelerator._auth._identity import Credentials
from capo_global_accelerator._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_global_accelerator._auth._zapros_handler import AuthMiddleware
from capo_global_accelerator._pagination import resolve_path as _resolve_path
from capo_global_accelerator._services._aws_config import aws_config
from capo_global_accelerator._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_global_accelerator.types.accelerator
    import capo_global_accelerator.types.add_custom_routing_endpoints_request
    import capo_global_accelerator.types.add_custom_routing_endpoints_response
    import capo_global_accelerator.types.add_endpoints_request
    import capo_global_accelerator.types.add_endpoints_response
    import capo_global_accelerator.types.advertise_byoip_cidr_request
    import capo_global_accelerator.types.advertise_byoip_cidr_response
    import capo_global_accelerator.types.allow_custom_routing_traffic_request
    import capo_global_accelerator.types.attachment
    import capo_global_accelerator.types.attachment_name
    import capo_global_accelerator.types.aws_account_id
    import capo_global_accelerator.types.byoip_cidr
    import capo_global_accelerator.types.cidr_authorization_context
    import capo_global_accelerator.types.client_affinity
    import capo_global_accelerator.types.create_accelerator_request
    import capo_global_accelerator.types.create_accelerator_response
    import capo_global_accelerator.types.create_cross_account_attachment_request
    import capo_global_accelerator.types.create_cross_account_attachment_response
    import capo_global_accelerator.types.create_custom_routing_accelerator_request
    import capo_global_accelerator.types.create_custom_routing_accelerator_response
    import capo_global_accelerator.types.create_custom_routing_endpoint_group_request
    import capo_global_accelerator.types.create_custom_routing_endpoint_group_response
    import capo_global_accelerator.types.create_custom_routing_listener_request
    import capo_global_accelerator.types.create_custom_routing_listener_response
    import capo_global_accelerator.types.create_endpoint_group_request
    import capo_global_accelerator.types.create_endpoint_group_response
    import capo_global_accelerator.types.create_listener_request
    import capo_global_accelerator.types.create_listener_response
    import capo_global_accelerator.types.cross_account_resource
    import capo_global_accelerator.types.custom_routing_accelerator
    import capo_global_accelerator.types.custom_routing_destination_configurations
    import capo_global_accelerator.types.custom_routing_endpoint_configurations
    import capo_global_accelerator.types.custom_routing_endpoint_group
    import capo_global_accelerator.types.custom_routing_listener
    import capo_global_accelerator.types.delete_accelerator_request
    import capo_global_accelerator.types.delete_cross_account_attachment_request
    import capo_global_accelerator.types.delete_custom_routing_accelerator_request
    import capo_global_accelerator.types.delete_custom_routing_endpoint_group_request
    import capo_global_accelerator.types.delete_custom_routing_listener_request
    import capo_global_accelerator.types.delete_endpoint_group_request
    import capo_global_accelerator.types.delete_listener_request
    import capo_global_accelerator.types.deny_custom_routing_traffic_request
    import capo_global_accelerator.types.deprovision_byoip_cidr_request
    import capo_global_accelerator.types.deprovision_byoip_cidr_response
    import capo_global_accelerator.types.describe_accelerator_attributes_request
    import capo_global_accelerator.types.describe_accelerator_attributes_response
    import capo_global_accelerator.types.describe_accelerator_request
    import capo_global_accelerator.types.describe_accelerator_response
    import capo_global_accelerator.types.describe_cross_account_attachment_request
    import capo_global_accelerator.types.describe_cross_account_attachment_response
    import capo_global_accelerator.types.describe_custom_routing_accelerator_attributes_request
    import capo_global_accelerator.types.describe_custom_routing_accelerator_attributes_response
    import capo_global_accelerator.types.describe_custom_routing_accelerator_request
    import capo_global_accelerator.types.describe_custom_routing_accelerator_response
    import capo_global_accelerator.types.describe_custom_routing_endpoint_group_request
    import capo_global_accelerator.types.describe_custom_routing_endpoint_group_response
    import capo_global_accelerator.types.describe_custom_routing_listener_request
    import capo_global_accelerator.types.describe_custom_routing_listener_response
    import capo_global_accelerator.types.describe_endpoint_group_request
    import capo_global_accelerator.types.describe_endpoint_group_response
    import capo_global_accelerator.types.describe_listener_request
    import capo_global_accelerator.types.describe_listener_response
    import capo_global_accelerator.types.destination_addresses
    import capo_global_accelerator.types.destination_port_mapping
    import capo_global_accelerator.types.destination_ports
    import capo_global_accelerator.types.endpoint_configurations
    import capo_global_accelerator.types.endpoint_group
    import capo_global_accelerator.types.endpoint_identifiers
    import capo_global_accelerator.types.endpoint_ids
    import capo_global_accelerator.types.generic_boolean
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.health_check_interval_seconds
    import capo_global_accelerator.types.health_check_path
    import capo_global_accelerator.types.health_check_port
    import capo_global_accelerator.types.health_check_protocol
    import capo_global_accelerator.types.idempotency_token
    import capo_global_accelerator.types.ip_address_type
    import capo_global_accelerator.types.ip_addresses
    import capo_global_accelerator.types.list_accelerators_request
    import capo_global_accelerator.types.list_accelerators_response
    import capo_global_accelerator.types.list_byoip_cidrs_request
    import capo_global_accelerator.types.list_byoip_cidrs_response
    import capo_global_accelerator.types.list_cross_account_attachments_request
    import capo_global_accelerator.types.list_cross_account_attachments_response
    import capo_global_accelerator.types.list_cross_account_resource_accounts_request
    import capo_global_accelerator.types.list_cross_account_resource_accounts_response
    import capo_global_accelerator.types.list_cross_account_resources_request
    import capo_global_accelerator.types.list_cross_account_resources_response
    import capo_global_accelerator.types.list_custom_routing_accelerators_request
    import capo_global_accelerator.types.list_custom_routing_accelerators_response
    import capo_global_accelerator.types.list_custom_routing_endpoint_groups_request
    import capo_global_accelerator.types.list_custom_routing_endpoint_groups_response
    import capo_global_accelerator.types.list_custom_routing_listeners_request
    import capo_global_accelerator.types.list_custom_routing_listeners_response
    import capo_global_accelerator.types.list_custom_routing_port_mappings_by_destination_request
    import capo_global_accelerator.types.list_custom_routing_port_mappings_by_destination_response
    import capo_global_accelerator.types.list_custom_routing_port_mappings_request
    import capo_global_accelerator.types.list_custom_routing_port_mappings_response
    import capo_global_accelerator.types.list_endpoint_groups_request
    import capo_global_accelerator.types.list_endpoint_groups_response
    import capo_global_accelerator.types.list_listeners_request
    import capo_global_accelerator.types.list_listeners_response
    import capo_global_accelerator.types.list_tags_for_resource_request
    import capo_global_accelerator.types.list_tags_for_resource_response
    import capo_global_accelerator.types.listener
    import capo_global_accelerator.types.max_results
    import capo_global_accelerator.types.port_mapping
    import capo_global_accelerator.types.port_mappings_max_results
    import capo_global_accelerator.types.port_overrides
    import capo_global_accelerator.types.port_ranges
    import capo_global_accelerator.types.principals
    import capo_global_accelerator.types.protocol
    import capo_global_accelerator.types.provision_byoip_cidr_request
    import capo_global_accelerator.types.provision_byoip_cidr_response
    import capo_global_accelerator.types.remove_custom_routing_endpoints_request
    import capo_global_accelerator.types.remove_endpoints_request
    import capo_global_accelerator.types.resource_arn
    import capo_global_accelerator.types.resources
    import capo_global_accelerator.types.tag_keys
    import capo_global_accelerator.types.tag_resource_request
    import capo_global_accelerator.types.tag_resource_response
    import capo_global_accelerator.types.tags
    import capo_global_accelerator.types.threshold_count
    import capo_global_accelerator.types.traffic_dial_percentage
    import capo_global_accelerator.types.untag_resource_request
    import capo_global_accelerator.types.untag_resource_response
    import capo_global_accelerator.types.update_accelerator_attributes_request
    import capo_global_accelerator.types.update_accelerator_attributes_response
    import capo_global_accelerator.types.update_accelerator_request
    import capo_global_accelerator.types.update_accelerator_response
    import capo_global_accelerator.types.update_cross_account_attachment_request
    import capo_global_accelerator.types.update_cross_account_attachment_response
    import capo_global_accelerator.types.update_custom_routing_accelerator_attributes_request
    import capo_global_accelerator.types.update_custom_routing_accelerator_attributes_response
    import capo_global_accelerator.types.update_custom_routing_accelerator_request
    import capo_global_accelerator.types.update_custom_routing_accelerator_response
    import capo_global_accelerator.types.update_custom_routing_listener_request
    import capo_global_accelerator.types.update_custom_routing_listener_response
    import capo_global_accelerator.types.update_endpoint_group_request
    import capo_global_accelerator.types.update_endpoint_group_response
    import capo_global_accelerator.types.update_listener_request
    import capo_global_accelerator.types.update_listener_response
    import capo_global_accelerator.types.withdraw_byoip_cidr_request
    import capo_global_accelerator.types.withdraw_byoip_cidr_response


class GlobalAcceleratorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class GlobalAcceleratorClient:
    """A client for the ``GlobalAccelerator`` service.

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
        self._config = GlobalAcceleratorClientConfig(
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
        self, config_overrides: Optional[GlobalAcceleratorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: GlobalAcceleratorClientConfig = config_overrides or {}
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

    def add_custom_routing_endpoints(
        self,
        endpoint_configurations: "capo_global_accelerator.types.custom_routing_endpoint_configurations.CustomRoutingEndpointConfigurations",
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.add_custom_routing_endpoints_response.AddCustomRoutingEndpointsResponse":
        """<p>Associate a virtual private cloud (VPC) subnet endpoint with your custom routing accelerator.</p> <p>The listener port range must be large enough to support the number of IP addresses that can be specified in your subnet. The number of ports required is: subnet size times the number of ports per destination EC2 instances. For example, a subnet defined as /24 requires a listener port range of at least 255 ports. </p> <p>Note: You must have enough remaining listener ports available to map to the subnet ports, or the call will fail with a LimitExceededException.</p> <p>By default, all destinations in a subnet in a custom routing accelerator cannot receive traffic. To enable all destinations to receive traffic, or to specify individual port mappings that can receive traffic, see the <a href="https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html"> AllowCustomRoutingTraffic</a> operation.</p>

        Args:
            endpoint_configurations: <p>The list of endpoint objects to add to a custom routing accelerator.</p>
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group for the custom routing endpoint.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.conflict_exception.ConflictException: <p>You can't use both of those options.</p>
            capo_global_accelerator.errors.endpoint_already_exists_exception.EndpointAlreadyExistsException: <p>The endpoint that you specified doesn't exist.</p>
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.add_custom_routing_endpoints_request.AddCustomRoutingEndpointsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.add_custom_routing_endpoints_response.AddCustomRoutingEndpointsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.add_custom_routing_endpoints

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.add_custom_routing_endpoints.add_custom_routing_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.add_custom_routing_endpoints_request.AddCustomRoutingEndpointsRequest = {
            "endpoint_configurations": endpoint_configurations,
            "endpoint_group_arn": endpoint_group_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_endpoints(
        self,
        endpoint_configurations: "capo_global_accelerator.types.endpoint_configurations.EndpointConfigurations",
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.add_endpoints_response.AddEndpointsResponse":
        """<p>Add endpoints to an endpoint group. The <code>AddEndpoints</code> API operation is the recommended option for adding endpoints. The alternative options are to add endpoints when you create an endpoint group (with the <a href="https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateEndpointGroup.html">CreateEndpointGroup</a> API) or when you update an endpoint group (with the <a href="https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateEndpointGroup.html">UpdateEndpointGroup</a> API). </p> <p>There are two advantages to using <code>AddEndpoints</code> to add endpoints in Global Accelerator:</p> <ul> <li> <p>It's faster, because Global Accelerator only has to resolve the new endpoints that you're adding, rather than resolving new and existing endpoints.</p> </li> <li> <p>It's more convenient, because you don't need to specify the current endpoints that are already in the endpoint group, in addition to the new endpoints that you want to add.</p> </li> </ul> <p>For information about endpoint types and requirements for endpoints that you can add to Global Accelerator, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.html"> Endpoints for standard accelerators</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Args:
            endpoint_configurations: <p>The list of endpoint objects.</p>
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.add_endpoints_request.AddEndpointsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.add_endpoints_response.AddEndpointsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.add_endpoints

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.add_endpoints.add_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.add_endpoints_request.AddEndpointsRequest = {
            "endpoint_configurations": endpoint_configurations,
            "endpoint_group_arn": endpoint_group_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def advertise_byoip_cidr(
        self,
        cidr: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.advertise_byoip_cidr_response.AdvertiseByoipCidrResponse":
        """<p>Advertises an IPv4 address range that is provisioned for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP). It can take a few minutes before traffic to the specified addresses starts routing to Amazon Web Services because of propagation delays. </p> <p>To stop advertising the BYOIP address range, use <a href="https://docs.aws.amazon.com/global-accelerator/latest/api/WithdrawByoipCidr.html"> WithdrawByoipCidr</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Args:
            cidr: <p>The address range, in CIDR notation. This must be the exact range that you provisioned. You can't advertise only a portion of the provisioned range.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.byoip_cidr_not_found_exception.ByoipCidrNotFoundException: <p>The CIDR that you specified was not found or is incorrect.</p>
            capo_global_accelerator.errors.incorrect_cidr_state_exception.IncorrectCidrStateException: <p>The CIDR that you specified is not valid for this action. For example, the state of the CIDR might be incorrect for this action.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.advertise_byoip_cidr_request.AdvertiseByoipCidrRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.advertise_byoip_cidr_response.AdvertiseByoipCidrResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.advertise_byoip_cidr

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.advertise_byoip_cidr.advertise_byoip_cidr(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.advertise_byoip_cidr_request.AdvertiseByoipCidrRequest = {
            "cidr": cidr
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def allow_custom_routing_traffic(
        self,
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        endpoint_id: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        destination_addresses: Optional[
            "capo_global_accelerator.types.destination_addresses.DestinationAddresses"
        ] = None,
        destination_ports: Optional[
            "capo_global_accelerator.types.destination_ports.DestinationPorts"
        ] = None,
        allow_all_traffic_to_endpoint: Optional[
            "capo_global_accelerator.types.generic_boolean.GenericBoolean"
        ] = None,
    ) -> None:
        """<p>Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC subnet endpoint that can receive traffic for a custom routing accelerator. You can allow traffic to all destinations in the subnet endpoint, or allow traffic to a specified list of destination IP addresses and ports in the subnet. Note that you cannot specify IP addresses or ports outside of the range that you configured for the endpoint group.</p> <p>After you make changes, you can verify that the updates are complete by checking the status of your accelerator: the status changes from IN_PROGRESS to DEPLOYED.</p>

        Args:
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group.</p>
            endpoint_id: <p>An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID.</p>
            destination_addresses: <p>A list of specific Amazon EC2 instance IP addresses (destination addresses) in a subnet that you want to allow to receive traffic. The IP addresses must be a subset of the IP addresses that you specified for the endpoint group.</p> <p> <code>DestinationAddresses</code> is required if <code>AllowAllTrafficToEndpoint</code> is <code>FALSE</code> or is not specified.</p>
            destination_ports: <p>A list of specific Amazon EC2 instance ports (destination ports) that you want to allow to receive traffic.</p>
            allow_all_traffic_to_endpoint: <p>Indicates whether all destination IP addresses and ports for a specified VPC subnet endpoint can receive traffic from a custom routing accelerator. The value is TRUE or FALSE. </p> <p>When set to TRUE, <i>all</i> destinations in the custom routing VPC subnet can receive traffic. Note that you cannot specify destination IP addresses and ports when the value is set to TRUE.</p> <p>When set to FALSE (or not specified), you <i>must</i> specify a list of destination IP addresses that are allowed to receive traffic. A list of ports is optional. If you don't specify a list of ports, the ports that can accept traffic is the same as the ports configured for the endpoint group.</p> <p>The default value is FALSE.</p>

        Raises:
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.allow_custom_routing_traffic_request.AllowCustomRoutingTrafficRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.allow_custom_routing_traffic

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.allow_custom_routing_traffic.allow_custom_routing_traffic(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.allow_custom_routing_traffic_request.AllowCustomRoutingTrafficRequest = {
            "endpoint_group_arn": endpoint_group_arn,
            "endpoint_id": endpoint_id,
        }
        if destination_addresses is not None:
            input_["destination_addresses"] = destination_addresses
        if destination_ports is not None:
            input_["destination_ports"] = destination_ports
        if allow_all_traffic_to_endpoint is not None:
            input_["allow_all_traffic_to_endpoint"] = allow_all_traffic_to_endpoint

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_accelerator(
        self,
        name: "capo_global_accelerator.types.generic_string.GenericString",
        idempotency_token: "capo_global_accelerator.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        ip_address_type: Optional[
            "capo_global_accelerator.types.ip_address_type.IpAddressType"
        ] = None,
        ip_addresses: Optional[
            "capo_global_accelerator.types.ip_addresses.IpAddresses"
        ] = None,
        enabled: Optional[
            "capo_global_accelerator.types.generic_boolean.GenericBoolean"
        ] = None,
        tags: Optional["capo_global_accelerator.types.tags.Tags"] = None,
    ) -> "capo_global_accelerator.types.create_accelerator_response.CreateAcceleratorResponse":
        """<p>Create an accelerator. An accelerator includes one or more listeners that process inbound connections and direct traffic to one or more endpoint groups, each of which includes endpoints, such as Network Load Balancers. </p> <important> <p>Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify <code>--region us-west-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            name: <p>The name of the accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters, periods (.), or hyphens (-), and must not begin or end with a hyphen or period.</p>
            ip_address_type: <p>The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL_STACK.</p>
            ip_addresses: <p>Optionally, if you've added your own IP address pool to Global Accelerator (BYOIP), you can choose an IPv4 address from your own pool to use for the accelerator's static IPv4 address when you create an accelerator. </p> <p>After you bring an address range to Amazon Web Services, it appears in your account as an address pool. When you create an accelerator, you can assign one IPv4 address from your range to it. Global Accelerator assigns you a second static IPv4 address from an Amazon IP address range. If you bring two IPv4 address ranges to Amazon Web Services, you can assign one IPv4 address from each range to your accelerator. This restriction is because Global Accelerator assigns each address range to a different network zone, for high availability.</p> <p>You can specify one or two addresses, separated by a space. Do not include the /32 suffix.</p> <p>Note that you can't update IP addresses for an existing accelerator. To change them, you must create a new accelerator with the new addresses.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the <i>Global Accelerator Developer Guide</i>.</p>
            enabled: <p>Indicates whether an accelerator is enabled. The value is true or false. The default value is true. </p> <p>If the value is set to true, an accelerator cannot be deleted. If set to false, the accelerator can be deleted.</p>
            idempotency_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of an accelerator.</p>
            tags: <p>Create tags for an accelerator.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html">Tagging in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.create_accelerator_request.CreateAcceleratorRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.create_accelerator_response.CreateAcceleratorResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.create_accelerator

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.create_accelerator.create_accelerator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.create_accelerator_request.CreateAcceleratorRequest = {
            "name": name,
            "idempotency_token": idempotency_token,
        }
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if ip_addresses is not None:
            input_["ip_addresses"] = ip_addresses
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cross_account_attachment(
        self,
        name: "capo_global_accelerator.types.attachment_name.AttachmentName",
        idempotency_token: "capo_global_accelerator.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        principals: Optional[
            "capo_global_accelerator.types.principals.Principals"
        ] = None,
        resources: Optional["capo_global_accelerator.types.resources.Resources"] = None,
        tags: Optional["capo_global_accelerator.types.tags.Tags"] = None,
    ) -> "capo_global_accelerator.types.create_cross_account_attachment_response.CreateCrossAccountAttachmentResponse":
        """<p>Create a cross-account attachment in Global Accelerator. You create a cross-account attachment to specify the <i>principals</i> who have permission to work with <i>resources</i> in accelerators in their own account. You specify, in the same attachment, the resources that are shared.</p> <p>A principal can be an Amazon Web Services account number or the Amazon Resource Name (ARN) for an accelerator. For account numbers that are listed as principals, to work with a resource listed in the attachment, you must sign in to an account specified as a principal. Then, you can work with resources that are listed, with any of your accelerators. If an accelerator ARN is listed in the cross-account attachment as a principal, anyone with permission to make updates to the accelerator can work with resources that are listed in the attachment. </p> <p>Specify each principal and resource separately. To specify two CIDR address pools, list them individually under <code>Resources</code>, and so on. For a command line operation, for example, you might use a statement like the following:</p> <p> <code> "Resources": [{"Cidr": "169.254.60.0/24"},{"Cidr": "169.254.59.0/24"}]</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html"> Working with cross-account attachments and resources in Global Accelerator</a> in the <i> Global Accelerator Developer Guide</i>.</p>

        Args:
            name: <p>The name of the cross-account attachment. </p>
            principals: <p>The principals to include in the cross-account attachment. A principal can be an Amazon Web Services account number or the Amazon Resource Name (ARN) for an accelerator. </p>
            resources: <p>The Amazon Resource Names (ARNs) for the resources to include in the cross-account attachment. A resource can be any supported Amazon Web Services resource type for Global Accelerator or a CIDR range for a bring your own IP address (BYOIP) address pool. </p>
            idempotency_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>
            tags: <p>Add tags for a cross-account attachment.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html">Tagging in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.create_cross_account_attachment_request.CreateCrossAccountAttachmentRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.create_cross_account_attachment_response.CreateCrossAccountAttachmentResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.create_cross_account_attachment

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.create_cross_account_attachment.create_cross_account_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.create_cross_account_attachment_request.CreateCrossAccountAttachmentRequest = {
            "name": name,
            "idempotency_token": idempotency_token,
        }
        if principals is not None:
            input_["principals"] = principals
        if resources is not None:
            input_["resources"] = resources
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_custom_routing_accelerator(
        self,
        name: "capo_global_accelerator.types.generic_string.GenericString",
        idempotency_token: "capo_global_accelerator.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        ip_address_type: Optional[
            "capo_global_accelerator.types.ip_address_type.IpAddressType"
        ] = None,
        ip_addresses: Optional[
            "capo_global_accelerator.types.ip_addresses.IpAddresses"
        ] = None,
        enabled: Optional[
            "capo_global_accelerator.types.generic_boolean.GenericBoolean"
        ] = None,
        tags: Optional["capo_global_accelerator.types.tags.Tags"] = None,
    ) -> "capo_global_accelerator.types.create_custom_routing_accelerator_response.CreateCustomRoutingAcceleratorResponse":
        """<p>Create a custom routing accelerator. A custom routing accelerator directs traffic to one of possibly thousands of Amazon EC2 instance destinations running in a single or multiple virtual private clouds (VPC) subnet endpoints.</p> <p>Be aware that, by default, all destination EC2 instances in a VPC subnet endpoint cannot receive traffic. To enable all destinations to receive traffic, or to specify individual port mappings that can receive traffic, see the <a href="https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html"> AllowCustomRoutingTraffic</a> operation.</p> <important> <p>Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify <code>--region us-west-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            name: <p>The name of a custom routing accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.</p>
            ip_address_type: <p>The IP address type that an accelerator supports. For a custom routing accelerator, the value must be IPV4.</p>
            ip_addresses: <p>Optionally, if you've added your own IP address pool to Global Accelerator (BYOIP), you can choose an IPv4 address from your own pool to use for the accelerator's static IPv4 address when you create an accelerator. </p> <p>After you bring an address range to Amazon Web Services, it appears in your account as an address pool. When you create an accelerator, you can assign one IPv4 address from your range to it. Global Accelerator assigns you a second static IPv4 address from an Amazon IP address range. If you bring two IPv4 address ranges to Amazon Web Services, you can assign one IPv4 address from each range to your accelerator. This restriction is because Global Accelerator assigns each address range to a different network zone, for high availability.</p> <p>You can specify one or two addresses, separated by a space. Do not include the /32 suffix.</p> <p>Note that you can't update IP addresses for an existing accelerator. To change them, you must create a new accelerator with the new addresses.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the <i>Global Accelerator Developer Guide</i>.</p>
            enabled: <p>Indicates whether an accelerator is enabled. The value is true or false. The default value is true. </p> <p>If the value is set to true, an accelerator cannot be deleted. If set to false, the accelerator can be deleted.</p>
            idempotency_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>
            tags: <p>Create tags for an accelerator.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html">Tagging in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.create_custom_routing_accelerator_request.CreateCustomRoutingAcceleratorRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.create_custom_routing_accelerator_response.CreateCustomRoutingAcceleratorResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.create_custom_routing_accelerator

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.create_custom_routing_accelerator.create_custom_routing_accelerator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.create_custom_routing_accelerator_request.CreateCustomRoutingAcceleratorRequest = {
            "name": name,
            "idempotency_token": idempotency_token,
        }
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if ip_addresses is not None:
            input_["ip_addresses"] = ip_addresses
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_custom_routing_endpoint_group(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        endpoint_group_region: "capo_global_accelerator.types.generic_string.GenericString",
        destination_configurations: "capo_global_accelerator.types.custom_routing_destination_configurations.CustomRoutingDestinationConfigurations",
        idempotency_token: "capo_global_accelerator.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.create_custom_routing_endpoint_group_response.CreateCustomRoutingEndpointGroupResponse":
        """<p>Create an endpoint group for the specified listener for a custom routing accelerator. An endpoint group is a collection of endpoints in one Amazon Web Services Region. </p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener for a custom routing endpoint.</p>
            endpoint_group_region: <p>The Amazon Web Services Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.</p>
            destination_configurations: <p>Sets the port range and protocol for all endpoints (virtual private cloud subnets) in a custom routing endpoint group to accept client traffic on.</p>
            idempotency_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.endpoint_group_already_exists_exception.EndpointGroupAlreadyExistsException: <p>The endpoint group that you specified already exists.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_port_range_exception.InvalidPortRangeException: <p>The port numbers that you specified are not valid numbers or are not unique for this accelerator.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.create_custom_routing_endpoint_group_request.CreateCustomRoutingEndpointGroupRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.create_custom_routing_endpoint_group_response.CreateCustomRoutingEndpointGroupResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.create_custom_routing_endpoint_group

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.create_custom_routing_endpoint_group.create_custom_routing_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.create_custom_routing_endpoint_group_request.CreateCustomRoutingEndpointGroupRequest = {
            "listener_arn": listener_arn,
            "endpoint_group_region": endpoint_group_region,
            "destination_configurations": destination_configurations,
            "idempotency_token": idempotency_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_custom_routing_listener(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        port_ranges: "capo_global_accelerator.types.port_ranges.PortRanges",
        idempotency_token: "capo_global_accelerator.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.create_custom_routing_listener_response.CreateCustomRoutingListenerResponse":
        """<p>Create a listener to process inbound connections from clients to a custom routing accelerator. Connections arrive to assigned static IP addresses on the port range that you specify. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator for a custom routing listener.</p>
            port_ranges: <p>The port range to support for connections from clients to your accelerator.</p> <p>Separately, you set port ranges for endpoints. For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html">About endpoints for custom routing accelerators</a>.</p>
            idempotency_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_port_range_exception.InvalidPortRangeException: <p>The port numbers that you specified are not valid numbers or are not unique for this accelerator.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.create_custom_routing_listener_request.CreateCustomRoutingListenerRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.create_custom_routing_listener_response.CreateCustomRoutingListenerResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.create_custom_routing_listener

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.create_custom_routing_listener.create_custom_routing_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.create_custom_routing_listener_request.CreateCustomRoutingListenerRequest = {
            "accelerator_arn": accelerator_arn,
            "port_ranges": port_ranges,
            "idempotency_token": idempotency_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_endpoint_group(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        endpoint_group_region: "capo_global_accelerator.types.generic_string.GenericString",
        idempotency_token: "capo_global_accelerator.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        endpoint_configurations: Optional[
            "capo_global_accelerator.types.endpoint_configurations.EndpointConfigurations"
        ] = None,
        traffic_dial_percentage: Optional[
            "capo_global_accelerator.types.traffic_dial_percentage.TrafficDialPercentage"
        ] = None,
        health_check_port: Optional[
            "capo_global_accelerator.types.health_check_port.HealthCheckPort"
        ] = None,
        health_check_protocol: Optional[
            "capo_global_accelerator.types.health_check_protocol.HealthCheckProtocol"
        ] = None,
        health_check_path: Optional[
            "capo_global_accelerator.types.health_check_path.HealthCheckPath"
        ] = None,
        health_check_interval_seconds: Optional[
            "capo_global_accelerator.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
        ] = None,
        threshold_count: Optional[
            "capo_global_accelerator.types.threshold_count.ThresholdCount"
        ] = None,
        port_overrides: Optional[
            "capo_global_accelerator.types.port_overrides.PortOverrides"
        ] = None,
    ) -> "capo_global_accelerator.types.create_endpoint_group_response.CreateEndpointGroupResponse":
        """<p>Create an endpoint group for the specified listener. An endpoint group is a collection of endpoints in one Amazon Web Services Region. A resource must be valid and active when you add it as an endpoint.</p> <p>For more information about endpoint types and requirements for endpoints that you can add to Global Accelerator, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.html"> Endpoints for standard accelerators</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>
            endpoint_group_region: <p>The Amazon Web Services Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.</p>
            endpoint_configurations: <p>The list of endpoint objects.</p>
            traffic_dial_percentage: <p>The percentage of traffic to send to an Amazon Web Services Region. Additional traffic is distributed to other endpoint groups for this listener. </p> <p>Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.</p> <p>The default value is 100.</p>
            health_check_port: <p>The port that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.</p>
            health_check_protocol: <p>The protocol that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.</p>
            health_check_path: <p>If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).</p>
            health_check_interval_seconds: <p>The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.</p>
            threshold_count: <p>The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</p>
            idempotency_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>
            port_overrides: <p>Override specific listener ports used to route traffic to endpoints that are part of this endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html"> Overriding listener ports</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.endpoint_group_already_exists_exception.EndpointGroupAlreadyExistsException: <p>The endpoint group that you specified already exists.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.create_endpoint_group_request.CreateEndpointGroupRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.create_endpoint_group_response.CreateEndpointGroupResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.create_endpoint_group

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.create_endpoint_group.create_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.create_endpoint_group_request.CreateEndpointGroupRequest = {
            "listener_arn": listener_arn,
            "endpoint_group_region": endpoint_group_region,
            "idempotency_token": idempotency_token,
        }
        if endpoint_configurations is not None:
            input_["endpoint_configurations"] = endpoint_configurations
        if traffic_dial_percentage is not None:
            input_["traffic_dial_percentage"] = traffic_dial_percentage
        if health_check_port is not None:
            input_["health_check_port"] = health_check_port
        if health_check_protocol is not None:
            input_["health_check_protocol"] = health_check_protocol
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if health_check_interval_seconds is not None:
            input_["health_check_interval_seconds"] = health_check_interval_seconds
        if threshold_count is not None:
            input_["threshold_count"] = threshold_count
        if port_overrides is not None:
            input_["port_overrides"] = port_overrides

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_listener(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        port_ranges: "capo_global_accelerator.types.port_ranges.PortRanges",
        protocol: "capo_global_accelerator.types.protocol.Protocol",
        idempotency_token: "capo_global_accelerator.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        client_affinity: Optional[
            "capo_global_accelerator.types.client_affinity.ClientAffinity"
        ] = None,
    ) -> (
        "capo_global_accelerator.types.create_listener_response.CreateListenerResponse"
    ):
        """<p>Create a listener to process inbound connections from clients to an accelerator. Connections arrive to assigned static IP addresses on a port, port range, or list of port ranges that you specify. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of your accelerator.</p>
            port_ranges: <p>The list of port ranges to support for connections from clients to your accelerator.</p>
            protocol: <p>The protocol for connections from clients to your accelerator.</p>
            client_affinity: <p>Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Client affinity gives you control over whether to always route each client to the same specific endpoint.</p> <p>Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is <code>NONE</code>, Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes. </p> <p>If you want a given client to always be routed to the same endpoint, set client affinity to <code>SOURCE_IP</code> instead. When you use the <code>SOURCE_IP</code> setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.</p> <p>The default value is <code>NONE</code>.</p>
            idempotency_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_port_range_exception.InvalidPortRangeException: <p>The port numbers that you specified are not valid numbers or are not unique for this accelerator.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.create_listener_request.CreateListenerRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.create_listener_response.CreateListenerResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.create_listener

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.create_listener.create_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.create_listener_request.CreateListenerRequest = {
            "accelerator_arn": accelerator_arn,
            "port_ranges": port_ranges,
            "protocol": protocol,
            "idempotency_token": idempotency_token,
        }
        if client_affinity is not None:
            input_["client_affinity"] = client_affinity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_accelerator(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> None:
        """<p>Delete an accelerator. Before you can delete an accelerator, you must disable it and remove all dependent resources (listeners and endpoint groups). To disable the accelerator, update the accelerator to set <code>Enabled</code> to false.</p> <important> <p>When you create an accelerator, by default, Global Accelerator provides you with a set of two static IP addresses. Alternatively, you can bring your own IP address ranges to Global Accelerator and assign IP addresses from those ranges. </p> <p>The IP addresses are assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you <i>delete</i> an accelerator, you lose the static IP addresses that are assigned to the accelerator, so you can no longer route traffic by using them. As a best practice, ensure that you have permissions in place to avoid inadvertently deleting accelerators. You can use IAM policies with Global Accelerator to limit the users who have permissions to delete an accelerator. For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/auth-and-access-control.html">Identity and access management</a> in the <i>Global Accelerator Developer Guide</i>.</p> </important>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of an accelerator.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_disabled_exception.AcceleratorNotDisabledException: <p>The accelerator that you specified could not be disabled.</p>
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.associated_listener_found_exception.AssociatedListenerFoundException: <p>The accelerator that you specified has a listener associated with it. You must remove all dependent resources from an accelerator before you can delete it.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.delete_accelerator_request.DeleteAcceleratorRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.delete_accelerator

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.delete_accelerator.delete_accelerator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.delete_accelerator_request.DeleteAcceleratorRequest = {
            "accelerator_arn": accelerator_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cross_account_attachment(
        self,
        attachment_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> None:
        """<p>Delete a cross-account attachment. When you delete an attachment, Global Accelerator revokes the permission to use the resources in the attachment from all principals in the list of principals. Global Accelerator revokes the permission for specific resources.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html"> Working with cross-account attachments and resources in Global Accelerator</a> in the <i> Global Accelerator Developer Guide</i>.</p>

        Args:
            attachment_arn: <p>The Amazon Resource Name (ARN) for the cross-account attachment to delete.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.attachment_not_found_exception.AttachmentNotFoundException: <p>No cross-account attachment was found.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.delete_cross_account_attachment_request.DeleteCrossAccountAttachmentRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.delete_cross_account_attachment

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.delete_cross_account_attachment.delete_cross_account_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.delete_cross_account_attachment_request.DeleteCrossAccountAttachmentRequest = {
            "attachment_arn": attachment_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_custom_routing_accelerator(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> None:
        """<p>Delete a custom routing accelerator. Before you can delete an accelerator, you must disable it and remove all dependent resources (listeners and endpoint groups). To disable the accelerator, update the accelerator to set <code>Enabled</code> to false.</p> <important> <p>When you create a custom routing accelerator, by default, Global Accelerator provides you with a set of two static IP addresses. </p> <p>The IP addresses are assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you <i>delete</i> an accelerator, you lose the static IP addresses that are assigned to the accelerator, so you can no longer route traffic by using them. As a best practice, ensure that you have permissions in place to avoid inadvertently deleting accelerators. You can use IAM policies with Global Accelerator to limit the users who have permissions to delete an accelerator. For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/auth-and-access-control.html">Identity and access management</a> in the <i>Global Accelerator Developer Guide</i>.</p> </important>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the custom routing accelerator to delete.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_disabled_exception.AcceleratorNotDisabledException: <p>The accelerator that you specified could not be disabled.</p>
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.associated_listener_found_exception.AssociatedListenerFoundException: <p>The accelerator that you specified has a listener associated with it. You must remove all dependent resources from an accelerator before you can delete it.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.delete_custom_routing_accelerator_request.DeleteCustomRoutingAcceleratorRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.delete_custom_routing_accelerator

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.delete_custom_routing_accelerator.delete_custom_routing_accelerator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.delete_custom_routing_accelerator_request.DeleteCustomRoutingAcceleratorRequest = {
            "accelerator_arn": accelerator_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_custom_routing_endpoint_group(
        self,
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> None:
        """<p>Delete an endpoint group from a listener for a custom routing accelerator.</p>

        Args:
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group to delete.</p>

        Raises:
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.delete_custom_routing_endpoint_group_request.DeleteCustomRoutingEndpointGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.delete_custom_routing_endpoint_group

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.delete_custom_routing_endpoint_group.delete_custom_routing_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.delete_custom_routing_endpoint_group_request.DeleteCustomRoutingEndpointGroupRequest = {
            "endpoint_group_arn": endpoint_group_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_custom_routing_listener(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> None:
        """<p>Delete a listener for a custom routing accelerator.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener to delete.</p>

        Raises:
            capo_global_accelerator.errors.associated_endpoint_group_found_exception.AssociatedEndpointGroupFoundException: <p>The listener that you specified has an endpoint group associated with it. You must remove all dependent resources from a listener before you can delete it.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.delete_custom_routing_listener_request.DeleteCustomRoutingListenerRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.delete_custom_routing_listener

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.delete_custom_routing_listener.delete_custom_routing_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.delete_custom_routing_listener_request.DeleteCustomRoutingListenerRequest = {
            "listener_arn": listener_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_endpoint_group(
        self,
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> None:
        """<p>Delete an endpoint group from a listener.</p>

        Args:
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group to delete.</p>

        Raises:
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.delete_endpoint_group_request.DeleteEndpointGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.delete_endpoint_group

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.delete_endpoint_group.delete_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.delete_endpoint_group_request.DeleteEndpointGroupRequest = {
            "endpoint_group_arn": endpoint_group_arn
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
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> None:
        """<p>Delete a listener from an accelerator.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>

        Raises:
            capo_global_accelerator.errors.associated_endpoint_group_found_exception.AssociatedEndpointGroupFoundException: <p>The listener that you specified has an endpoint group associated with it. You must remove all dependent resources from a listener before you can delete it.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.delete_listener_request.DeleteListenerRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.delete_listener

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.delete_listener.delete_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.delete_listener_request.DeleteListenerRequest = {
            "listener_arn": listener_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deny_custom_routing_traffic(
        self,
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        endpoint_id: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        destination_addresses: Optional[
            "capo_global_accelerator.types.destination_addresses.DestinationAddresses"
        ] = None,
        destination_ports: Optional[
            "capo_global_accelerator.types.destination_ports.DestinationPorts"
        ] = None,
        deny_all_traffic_to_endpoint: Optional[
            "capo_global_accelerator.types.generic_boolean.GenericBoolean"
        ] = None,
    ) -> None:
        """<p>Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC subnet endpoint that cannot receive traffic for a custom routing accelerator. You can deny traffic to all destinations in the VPC endpoint, or deny traffic to a specified list of destination IP addresses and ports. Note that you cannot specify IP addresses or ports outside of the range that you configured for the endpoint group.</p> <p>After you make changes, you can verify that the updates are complete by checking the status of your accelerator: the status changes from IN_PROGRESS to DEPLOYED.</p>

        Args:
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group.</p>
            endpoint_id: <p>An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID.</p>
            destination_addresses: <p>A list of specific Amazon EC2 instance IP addresses (destination addresses) in a subnet that you want to prevent from receiving traffic. The IP addresses must be a subset of the IP addresses allowed for the VPC subnet associated with the endpoint group.</p>
            destination_ports: <p>A list of specific Amazon EC2 instance ports (destination ports) in a subnet endpoint that you want to prevent from receiving traffic.</p>
            deny_all_traffic_to_endpoint: <p>Indicates whether all destination IP addresses and ports for a specified VPC subnet endpoint <i>cannot</i> receive traffic from a custom routing accelerator. The value is TRUE or FALSE. </p> <p>When set to TRUE, <i>no</i> destinations in the custom routing VPC subnet can receive traffic. Note that you cannot specify destination IP addresses and ports when the value is set to TRUE.</p> <p>When set to FALSE (or not specified), you <i>must</i> specify a list of destination IP addresses that cannot receive traffic. A list of ports is optional. If you don't specify a list of ports, the ports that can accept traffic is the same as the ports configured for the endpoint group.</p> <p>The default value is FALSE.</p>

        Raises:
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.deny_custom_routing_traffic_request.DenyCustomRoutingTrafficRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.deny_custom_routing_traffic

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.deny_custom_routing_traffic.deny_custom_routing_traffic(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.deny_custom_routing_traffic_request.DenyCustomRoutingTrafficRequest = {
            "endpoint_group_arn": endpoint_group_arn,
            "endpoint_id": endpoint_id,
        }
        if destination_addresses is not None:
            input_["destination_addresses"] = destination_addresses
        if destination_ports is not None:
            input_["destination_ports"] = destination_ports
        if deny_all_traffic_to_endpoint is not None:
            input_["deny_all_traffic_to_endpoint"] = deny_all_traffic_to_endpoint

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deprovision_byoip_cidr(
        self,
        cidr: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.deprovision_byoip_cidr_response.DeprovisionByoipCidrResponse":
        """<p>Releases the specified address range that you provisioned to use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool. </p> <p>Before you can release an address range, you must stop advertising it by using <a href="https://docs.aws.amazon.com/global-accelerator/latest/api/WithdrawByoipCidr.html">WithdrawByoipCidr</a> and you must not have any accelerators that are using static IP addresses allocated from its address range. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Args:
            cidr: <p>The address range, in CIDR notation. The prefix must be the same prefix that you specified when you provisioned the address range.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.byoip_cidr_not_found_exception.ByoipCidrNotFoundException: <p>The CIDR that you specified was not found or is incorrect.</p>
            capo_global_accelerator.errors.incorrect_cidr_state_exception.IncorrectCidrStateException: <p>The CIDR that you specified is not valid for this action. For example, the state of the CIDR might be incorrect for this action.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.deprovision_byoip_cidr_request.DeprovisionByoipCidrRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.deprovision_byoip_cidr_response.DeprovisionByoipCidrResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.deprovision_byoip_cidr

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.deprovision_byoip_cidr.deprovision_byoip_cidr(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.deprovision_byoip_cidr_request.DeprovisionByoipCidrRequest = {
            "cidr": cidr
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_accelerator(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.describe_accelerator_response.DescribeAcceleratorResponse":
        """<p>Describe an accelerator. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator to describe.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.describe_accelerator_request.DescribeAcceleratorRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.describe_accelerator_response.DescribeAcceleratorResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.describe_accelerator

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.describe_accelerator.describe_accelerator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.describe_accelerator_request.DescribeAcceleratorRequest = {
            "accelerator_arn": accelerator_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_accelerator_attributes(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.describe_accelerator_attributes_response.DescribeAcceleratorAttributesResponse":
        """<p>Describe the attributes of an accelerator. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator with the attributes that you want to describe.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.describe_accelerator_attributes_request.DescribeAcceleratorAttributesRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.describe_accelerator_attributes_response.DescribeAcceleratorAttributesResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.describe_accelerator_attributes

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.describe_accelerator_attributes.describe_accelerator_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.describe_accelerator_attributes_request.DescribeAcceleratorAttributesRequest = {
            "accelerator_arn": accelerator_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cross_account_attachment(
        self,
        attachment_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.describe_cross_account_attachment_response.DescribeCrossAccountAttachmentResponse":
        """<p>Gets configuration information about a cross-account attachment.</p>

        Args:
            attachment_arn: <p>The Amazon Resource Name (ARN) for the cross-account attachment to describe.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.attachment_not_found_exception.AttachmentNotFoundException: <p>No cross-account attachment was found.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.describe_cross_account_attachment_request.DescribeCrossAccountAttachmentRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.describe_cross_account_attachment_response.DescribeCrossAccountAttachmentResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.describe_cross_account_attachment

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.describe_cross_account_attachment.describe_cross_account_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.describe_cross_account_attachment_request.DescribeCrossAccountAttachmentRequest = {
            "attachment_arn": attachment_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_custom_routing_accelerator(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.describe_custom_routing_accelerator_response.DescribeCustomRoutingAcceleratorResponse":
        """<p>Describe a custom routing accelerator. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator to describe.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.describe_custom_routing_accelerator_request.DescribeCustomRoutingAcceleratorRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.describe_custom_routing_accelerator_response.DescribeCustomRoutingAcceleratorResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.describe_custom_routing_accelerator

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.describe_custom_routing_accelerator.describe_custom_routing_accelerator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.describe_custom_routing_accelerator_request.DescribeCustomRoutingAcceleratorRequest = {
            "accelerator_arn": accelerator_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_custom_routing_accelerator_attributes(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.describe_custom_routing_accelerator_attributes_response.DescribeCustomRoutingAcceleratorAttributesResponse":
        """<p>Describe the attributes of a custom routing accelerator. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the custom routing accelerator to describe the attributes for.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.describe_custom_routing_accelerator_attributes_request.DescribeCustomRoutingAcceleratorAttributesRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.describe_custom_routing_accelerator_attributes_response.DescribeCustomRoutingAcceleratorAttributesResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.describe_custom_routing_accelerator_attributes

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.describe_custom_routing_accelerator_attributes.describe_custom_routing_accelerator_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.describe_custom_routing_accelerator_attributes_request.DescribeCustomRoutingAcceleratorAttributesRequest = {
            "accelerator_arn": accelerator_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_custom_routing_endpoint_group(
        self,
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.describe_custom_routing_endpoint_group_response.DescribeCustomRoutingEndpointGroupResponse":
        """<p>Describe an endpoint group for a custom routing accelerator. </p>

        Args:
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group to describe.</p>

        Raises:
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.describe_custom_routing_endpoint_group_request.DescribeCustomRoutingEndpointGroupRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.describe_custom_routing_endpoint_group_response.DescribeCustomRoutingEndpointGroupResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.describe_custom_routing_endpoint_group

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.describe_custom_routing_endpoint_group.describe_custom_routing_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.describe_custom_routing_endpoint_group_request.DescribeCustomRoutingEndpointGroupRequest = {
            "endpoint_group_arn": endpoint_group_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_custom_routing_listener(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.describe_custom_routing_listener_response.DescribeCustomRoutingListenerResponse":
        """<p>The description of a listener for a custom routing accelerator.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener to describe.</p>

        Raises:
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.describe_custom_routing_listener_request.DescribeCustomRoutingListenerRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.describe_custom_routing_listener_response.DescribeCustomRoutingListenerResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.describe_custom_routing_listener

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.describe_custom_routing_listener.describe_custom_routing_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.describe_custom_routing_listener_request.DescribeCustomRoutingListenerRequest = {
            "listener_arn": listener_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_endpoint_group(
        self,
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.describe_endpoint_group_response.DescribeEndpointGroupResponse":
        """<p>Describe an endpoint group. </p>

        Args:
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group to describe.</p>

        Raises:
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.describe_endpoint_group_request.DescribeEndpointGroupRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.describe_endpoint_group_response.DescribeEndpointGroupResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.describe_endpoint_group

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.describe_endpoint_group.describe_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.describe_endpoint_group_request.DescribeEndpointGroupRequest = {
            "endpoint_group_arn": endpoint_group_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_listener(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.describe_listener_response.DescribeListenerResponse":
        """<p>Describe a listener. </p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener to describe.</p>

        Raises:
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.describe_listener_request.DescribeListenerRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.describe_listener_response.DescribeListenerResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.describe_listener

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.describe_listener.describe_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.describe_listener_request.DescribeListenerRequest = {
            "listener_arn": listener_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_accelerators(
        self,
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_accelerators_response.ListAcceleratorsResponse":
        """<p>List the accelerators for an Amazon Web Services account. </p>

        Args:
            max_results: <p>The number of Global Accelerator objects that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_accelerators_request.ListAcceleratorsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_accelerators_response.ListAcceleratorsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_accelerators

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_accelerators.list_accelerators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_accelerators_request.ListAcceleratorsRequest = {}
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

    def iter_list_accelerators(
        self,
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.accelerator.Accelerator]":
        _token = next_token
        while True:
            _response = self.list_accelerators(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("accelerators",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_byoip_cidrs(
        self,
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> (
        "capo_global_accelerator.types.list_byoip_cidrs_response.ListByoipCidrsResponse"
    ):
        """<p>Lists the IP address ranges that were specified in calls to <a href="https://docs.aws.amazon.com/global-accelerator/latest/api/ProvisionByoipCidr.html">ProvisionByoipCidr</a>, including the current state and a history of state changes.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_byoip_cidrs_request.ListByoipCidrsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_byoip_cidrs_response.ListByoipCidrsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_byoip_cidrs

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_byoip_cidrs.list_byoip_cidrs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_byoip_cidrs_request.ListByoipCidrsRequest = {}
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

    def iter_list_byoip_cidrs(
        self,
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.byoip_cidr.ByoipCidr]":
        _token = next_token
        while True:
            _response = self.list_byoip_cidrs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("byoip_cidrs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cross_account_attachments(
        self,
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_cross_account_attachments_response.ListCrossAccountAttachmentsResponse":
        """<p>List the cross-account attachments that have been created in Global Accelerator.</p>

        Args:
            max_results: <p>The number of cross-account attachment objects that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_cross_account_attachments_request.ListCrossAccountAttachmentsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_cross_account_attachments_response.ListCrossAccountAttachmentsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_cross_account_attachments

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_cross_account_attachments.list_cross_account_attachments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_cross_account_attachments_request.ListCrossAccountAttachmentsRequest = {}
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

    def iter_list_cross_account_attachments(
        self,
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.attachment.Attachment]":
        _token = next_token
        while True:
            _response = self.list_cross_account_attachments(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cross_account_attachments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cross_account_resource_accounts(
        self, *, config_overrides: Optional[GlobalAcceleratorClientConfig] = None
    ) -> "capo_global_accelerator.types.list_cross_account_resource_accounts_response.ListCrossAccountResourceAccountsResponse":
        """<p>List the accounts that have cross-account resources.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html"> Working with cross-account attachments and resources in Global Accelerator</a> in the <i> Global Accelerator Developer Guide</i>.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_cross_account_resource_accounts_request.ListCrossAccountResourceAccountsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_cross_account_resource_accounts_response.ListCrossAccountResourceAccountsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_cross_account_resource_accounts

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_cross_account_resource_accounts.list_cross_account_resource_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_cross_account_resource_accounts_request.ListCrossAccountResourceAccountsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_cross_account_resources(
        self,
        resource_owner_aws_account_id: "capo_global_accelerator.types.aws_account_id.AwsAccountId",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        accelerator_arn: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_cross_account_resources_response.ListCrossAccountResourcesResponse":
        """<p>List the cross-account resources available to work with.</p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of an accelerator in a cross-account attachment.</p>
            resource_owner_aws_account_id: <p>The account ID of a resource owner in a cross-account attachment.</p>
            max_results: <p>The number of cross-account resource objects that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_cross_account_resources_request.ListCrossAccountResourcesRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_cross_account_resources_response.ListCrossAccountResourcesResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_cross_account_resources

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_cross_account_resources.list_cross_account_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_cross_account_resources_request.ListCrossAccountResourcesRequest = {
            "resource_owner_aws_account_id": resource_owner_aws_account_id
        }
        if accelerator_arn is not None:
            input_["accelerator_arn"] = accelerator_arn
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

    def iter_list_cross_account_resources(
        self,
        resource_owner_aws_account_id: "capo_global_accelerator.types.aws_account_id.AwsAccountId",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        accelerator_arn: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.cross_account_resource.CrossAccountResource]":
        _token = next_token
        while True:
            _response = self.list_cross_account_resources(
                resource_owner_aws_account_id,
                config_overrides=config_overrides,
                accelerator_arn=accelerator_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cross_account_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_custom_routing_accelerators(
        self,
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_custom_routing_accelerators_response.ListCustomRoutingAcceleratorsResponse":
        """<p>List the custom routing accelerators for an Amazon Web Services account. </p>

        Args:
            max_results: <p>The number of custom routing Global Accelerator objects that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_custom_routing_accelerators_request.ListCustomRoutingAcceleratorsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_custom_routing_accelerators_response.ListCustomRoutingAcceleratorsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_accelerators

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_accelerators.list_custom_routing_accelerators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_custom_routing_accelerators_request.ListCustomRoutingAcceleratorsRequest = {}
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

    def iter_list_custom_routing_accelerators(
        self,
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.custom_routing_accelerator.CustomRoutingAccelerator]":
        _token = next_token
        while True:
            _response = self.list_custom_routing_accelerators(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("accelerators",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_custom_routing_endpoint_groups(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_custom_routing_endpoint_groups_response.ListCustomRoutingEndpointGroupsResponse":
        """<p>List the endpoint groups that are associated with a listener for a custom routing accelerator. </p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener to list endpoint groups for.</p>
            max_results: <p>The number of endpoint group objects that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_custom_routing_endpoint_groups_request.ListCustomRoutingEndpointGroupsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_custom_routing_endpoint_groups_response.ListCustomRoutingEndpointGroupsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_endpoint_groups

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_endpoint_groups.list_custom_routing_endpoint_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_custom_routing_endpoint_groups_request.ListCustomRoutingEndpointGroupsRequest = {
            "listener_arn": listener_arn
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

    def iter_list_custom_routing_endpoint_groups(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.custom_routing_endpoint_group.CustomRoutingEndpointGroup]":
        _token = next_token
        while True:
            _response = self.list_custom_routing_endpoint_groups(
                listener_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("endpoint_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_custom_routing_listeners(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_custom_routing_listeners_response.ListCustomRoutingListenersResponse":
        """<p>List the listeners for a custom routing accelerator. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator to list listeners for.</p>
            max_results: <p>The number of listener objects that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_custom_routing_listeners_request.ListCustomRoutingListenersRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_custom_routing_listeners_response.ListCustomRoutingListenersResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_listeners

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_listeners.list_custom_routing_listeners(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_custom_routing_listeners_request.ListCustomRoutingListenersRequest = {
            "accelerator_arn": accelerator_arn
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

    def iter_list_custom_routing_listeners(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.custom_routing_listener.CustomRoutingListener]":
        _token = next_token
        while True:
            _response = self.list_custom_routing_listeners(
                accelerator_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("listeners",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_custom_routing_port_mappings(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        endpoint_group_arn: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
        max_results: Optional[
            "capo_global_accelerator.types.port_mappings_max_results.PortMappingsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_custom_routing_port_mappings_response.ListCustomRoutingPortMappingsResponse":
        """<p>Provides a complete mapping from the public accelerator IP address and port to destination EC2 instance IP addresses and ports in the virtual public cloud (VPC) subnet endpoint for a custom routing accelerator. For each subnet endpoint that you add, Global Accelerator creates a new static port mapping for the accelerator. The port mappings don't change after Global Accelerator generates them, so you can retrieve and cache the full mapping on your servers. </p> <p>If you remove a subnet from your accelerator, Global Accelerator removes (reclaims) the port mappings. If you add a subnet to your accelerator, Global Accelerator creates new port mappings (the existing ones don't change). If you add or remove EC2 instances in your subnet, the port mappings don't change, because the mappings are created when you add the subnet to Global Accelerator.</p> <p>The mappings also include a flag for each destination denoting which destination IP addresses and ports are allowed or denied traffic.</p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator to list the custom routing port mappings for.</p>
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group to list the custom routing port mappings for.</p>
            max_results: <p>The number of destination port mappings that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_custom_routing_port_mappings_request.ListCustomRoutingPortMappingsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_custom_routing_port_mappings_response.ListCustomRoutingPortMappingsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_port_mappings

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_port_mappings.list_custom_routing_port_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_custom_routing_port_mappings_request.ListCustomRoutingPortMappingsRequest = {
            "accelerator_arn": accelerator_arn
        }
        if endpoint_group_arn is not None:
            input_["endpoint_group_arn"] = endpoint_group_arn
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

    def iter_list_custom_routing_port_mappings(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        endpoint_group_arn: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
        max_results: Optional[
            "capo_global_accelerator.types.port_mappings_max_results.PortMappingsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.port_mapping.PortMapping]":
        _token = next_token
        while True:
            _response = self.list_custom_routing_port_mappings(
                accelerator_arn,
                config_overrides=config_overrides,
                endpoint_group_arn=endpoint_group_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("port_mappings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_custom_routing_port_mappings_by_destination(
        self,
        endpoint_id: "capo_global_accelerator.types.generic_string.GenericString",
        destination_address: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.port_mappings_max_results.PortMappingsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_custom_routing_port_mappings_by_destination_response.ListCustomRoutingPortMappingsByDestinationResponse":
        """<p>List the port mappings for a specific EC2 instance (destination) in a VPC subnet endpoint. The response is the mappings for one destination IP address. This is useful when your subnet endpoint has mappings that span multiple custom routing accelerators in your account, or for scenarios where you only want to list the port mappings for a specific destination instance.</p>

        Args:
            endpoint_id: <p>The ID for the virtual private cloud (VPC) subnet.</p>
            destination_address: <p>The endpoint IP address in a virtual private cloud (VPC) subnet for which you want to receive back port mappings.</p>
            max_results: <p>The number of destination port mappings that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.endpoint_not_found_exception.EndpointNotFoundException: <p>The endpoint that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_custom_routing_port_mappings_by_destination_request.ListCustomRoutingPortMappingsByDestinationRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_custom_routing_port_mappings_by_destination_response.ListCustomRoutingPortMappingsByDestinationResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_port_mappings_by_destination

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_custom_routing_port_mappings_by_destination.list_custom_routing_port_mappings_by_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_custom_routing_port_mappings_by_destination_request.ListCustomRoutingPortMappingsByDestinationRequest = {
            "endpoint_id": endpoint_id,
            "destination_address": destination_address,
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

    def iter_list_custom_routing_port_mappings_by_destination(
        self,
        endpoint_id: "capo_global_accelerator.types.generic_string.GenericString",
        destination_address: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.port_mappings_max_results.PortMappingsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.destination_port_mapping.DestinationPortMapping]":
        _token = next_token
        while True:
            _response = self.list_custom_routing_port_mappings_by_destination(
                endpoint_id,
                destination_address,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("destination_port_mappings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_endpoint_groups(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_endpoint_groups_response.ListEndpointGroupsResponse":
        """<p>List the endpoint groups that are associated with a listener. </p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>
            max_results: <p>The number of endpoint group objects that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_endpoint_groups_request.ListEndpointGroupsRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_endpoint_groups_response.ListEndpointGroupsResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_endpoint_groups

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_endpoint_groups.list_endpoint_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_endpoint_groups_request.ListEndpointGroupsRequest = {
            "listener_arn": listener_arn
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

    def iter_list_endpoint_groups(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.endpoint_group.EndpointGroup]":
        _token = next_token
        while True:
            _response = self.list_endpoint_groups(
                listener_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("endpoint_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_listeners(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.list_listeners_response.ListListenersResponse":
        """<p>List the listeners for an accelerator. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator for which you want to list listener objects.</p>
            max_results: <p>The number of listener objects that you want to return with this call. The default value is 10.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_next_token_exception.InvalidNextTokenException: <p>There isn't another item to return.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_listeners_request.ListListenersRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_listeners_response.ListListenersResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_listeners

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_listeners.list_listeners(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_listeners_request.ListListenersRequest = {
            "accelerator_arn": accelerator_arn
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
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        max_results: Optional[
            "capo_global_accelerator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "Iterator[capo_global_accelerator.types.listener.Listener]":
        _token = next_token
        while True:
            _response = self.list_listeners(
                accelerator_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("listeners",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_global_accelerator.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all tags for an accelerator. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html">Tagging in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the accelerator to list tags for. An ARN uniquely identifies an accelerator.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.attachment_not_found_exception.AttachmentNotFoundException: <p>No cross-account attachment was found.</p>
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.list_tags_for_resource

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def provision_byoip_cidr(
        self,
        cidr: "capo_global_accelerator.types.generic_string.GenericString",
        cidr_authorization_context: "capo_global_accelerator.types.cidr_authorization_context.CidrAuthorizationContext",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.provision_byoip_cidr_response.ProvisionByoipCidrResponse":
        """<p>Provisions an IP address range to use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool. After the address range is provisioned, it is ready to be advertised using <a href="https://docs.aws.amazon.com/global-accelerator/latest/api/AdvertiseByoipCidr.html"> AdvertiseByoipCidr</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Args:
            cidr: <p>The public IPv4 address range, in CIDR notation. The most specific IP prefix that you can specify is /24. The address range cannot overlap with another address range that you've brought to this Amazon Web Services Region or another Region.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>
            cidr_authorization_context: <p>A signed document that proves that you are authorized to bring the specified IP address range to Amazon using BYOIP. </p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.incorrect_cidr_state_exception.IncorrectCidrStateException: <p>The CIDR that you specified is not valid for this action. For example, the state of the CIDR might be incorrect for this action.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.provision_byoip_cidr_request.ProvisionByoipCidrRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.provision_byoip_cidr_response.ProvisionByoipCidrResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.provision_byoip_cidr

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.provision_byoip_cidr.provision_byoip_cidr(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.provision_byoip_cidr_request.ProvisionByoipCidrRequest = {
            "cidr": cidr,
            "cidr_authorization_context": cidr_authorization_context,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_custom_routing_endpoints(
        self,
        endpoint_ids: "capo_global_accelerator.types.endpoint_ids.EndpointIds",
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> None:
        """<p>Remove endpoints from a custom routing accelerator.</p>

        Args:
            endpoint_ids: <p>The IDs for the endpoints. For custom routing accelerators, endpoint IDs are the virtual private cloud (VPC) subnet IDs. </p>
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group to remove endpoints from.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.conflict_exception.ConflictException: <p>You can't use both of those options.</p>
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.endpoint_not_found_exception.EndpointNotFoundException: <p>The endpoint that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.remove_custom_routing_endpoints_request.RemoveCustomRoutingEndpointsRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.remove_custom_routing_endpoints

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.remove_custom_routing_endpoints.remove_custom_routing_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.remove_custom_routing_endpoints_request.RemoveCustomRoutingEndpointsRequest = {
            "endpoint_ids": endpoint_ids,
            "endpoint_group_arn": endpoint_group_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_endpoints(
        self,
        endpoint_identifiers: "capo_global_accelerator.types.endpoint_identifiers.EndpointIdentifiers",
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> None:
        """<p>Remove endpoints from an endpoint group. </p> <p>The <code>RemoveEndpoints</code> API operation is the recommended option for removing endpoints. The alternative is to remove endpoints by updating an endpoint group by using the <a href="https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateEndpointGroup.html">UpdateEndpointGroup</a> API operation. There are two advantages to using <code>AddEndpoints</code> to remove endpoints instead:</p> <ul> <li> <p>It's more convenient, because you only need to specify the endpoints that you want to remove. With the <code>UpdateEndpointGroup</code> API operation, you must specify all of the endpoints in the endpoint group except the ones that you want to remove from the group.</p> </li> <li> <p>It's faster, because Global Accelerator doesn't need to resolve any endpoints. With the <code>UpdateEndpointGroup</code> API operation, Global Accelerator must resolve all of the endpoints that remain in the group.</p> </li> </ul>

        Args:
            endpoint_identifiers: <p>The identifiers of the endpoints that you want to remove.</p>
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.remove_endpoints_request.RemoveEndpointsRequest]",
        ) -> OperationResponse[None]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.remove_endpoints

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.remove_endpoints.remove_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.remove_endpoints_request.RemoveEndpointsRequest = {
            "endpoint_identifiers": endpoint_identifiers,
            "endpoint_group_arn": endpoint_group_arn,
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
        resource_arn: "capo_global_accelerator.types.resource_arn.ResourceArn",
        tags: "capo_global_accelerator.types.tags.Tags",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.tag_resource_response.TagResourceResponse":
        """<p>Add tags to an accelerator resource. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html">Tagging in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Global Accelerator resource to add tags to. An ARN uniquely identifies a resource.</p>
            tags: <p>The tags to add to a resource. A tag consists of a key and a value that you define.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.tag_resource

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_global_accelerator.types.resource_arn.ResourceArn",
        tag_keys: "capo_global_accelerator.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a Global Accelerator resource. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from an accelerator that was already removed.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html">Tagging in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Global Accelerator resource to remove tags from. An ARN uniquely identifies a resource.</p>
            tag_keys: <p>The tag key pairs that you want to remove from the specified resources.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.untag_resource

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.untag_resource_request.UntagResourceRequest = {
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

    def update_accelerator(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        name: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
        ip_address_type: Optional[
            "capo_global_accelerator.types.ip_address_type.IpAddressType"
        ] = None,
        ip_addresses: Optional[
            "capo_global_accelerator.types.ip_addresses.IpAddresses"
        ] = None,
        enabled: Optional[
            "capo_global_accelerator.types.generic_boolean.GenericBoolean"
        ] = None,
    ) -> "capo_global_accelerator.types.update_accelerator_response.UpdateAcceleratorResponse":
        """<p>Update an accelerator to make changes, such as the following: </p> <ul> <li> <p>Change the name of the accelerator.</p> </li> <li> <p>Disable the accelerator so that it no longer accepts or routes traffic, or so that you can delete it.</p> </li> <li> <p>Enable the accelerator, if it is disabled.</p> </li> <li> <p>Change the IP address type to dual-stack if it is IPv4, or change the IP address type to IPv4 if it's dual-stack.</p> </li> </ul> <p>Be aware that static IP addresses remain assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you delete the accelerator, you lose the static IP addresses that are assigned to it, so you can no longer route traffic by using them.</p> <important> <p>Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify <code>--region us-west-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator to update.</p>
            name: <p>The name of the accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters, periods (.), or hyphens (-), and must not begin or end with a hyphen or period.</p>
            ip_address_type: <p>The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL_STACK.</p>
            ip_addresses: <p>The IP addresses for an accelerator.</p>
            enabled: <p>Indicates whether an accelerator is enabled. The value is true or false. The default value is true. </p> <p>If the value is set to true, the accelerator cannot be deleted. If set to false, the accelerator can be deleted.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.conflict_exception.ConflictException: <p>You can't use both of those options.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.update_accelerator_request.UpdateAcceleratorRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.update_accelerator_response.UpdateAcceleratorResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.update_accelerator

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.update_accelerator.update_accelerator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.update_accelerator_request.UpdateAcceleratorRequest = {
            "accelerator_arn": accelerator_arn
        }
        if name is not None:
            input_["name"] = name
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if ip_addresses is not None:
            input_["ip_addresses"] = ip_addresses
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_accelerator_attributes(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        flow_logs_enabled: Optional[
            "capo_global_accelerator.types.generic_boolean.GenericBoolean"
        ] = None,
        flow_logs_s3_bucket: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
        flow_logs_s3_prefix: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.update_accelerator_attributes_response.UpdateAcceleratorAttributesResponse":
        """<p>Update the attributes for an accelerator. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator that you want to update.</p>
            flow_logs_enabled: <p>Update whether flow logs are enabled. The default value is false. If the value is true, <code>FlowLogsS3Bucket</code> and <code>FlowLogsS3Prefix</code> must be specified.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html">Flow Logs</a> in the <i>Global Accelerator Developer Guide</i>.</p>
            flow_logs_s3_bucket: <p>The name of the Amazon S3 bucket for the flow logs. Attribute is required if <code>FlowLogsEnabled</code> is <code>true</code>. The bucket must exist and have a bucket policy that grants Global Accelerator permission to write to the bucket.</p>
            flow_logs_s3_prefix: <p>Update the prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if <code>FlowLogsEnabled</code> is <code>true</code>. </p> <p>If you specify slash (/) for the S3 bucket prefix, the log file bucket folder structure will include a double slash (//), like the following:</p> <p>s3-bucket_name//AWSLogs/aws_account_id</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.update_accelerator_attributes_request.UpdateAcceleratorAttributesRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.update_accelerator_attributes_response.UpdateAcceleratorAttributesResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.update_accelerator_attributes

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.update_accelerator_attributes.update_accelerator_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.update_accelerator_attributes_request.UpdateAcceleratorAttributesRequest = {
            "accelerator_arn": accelerator_arn
        }
        if flow_logs_enabled is not None:
            input_["flow_logs_enabled"] = flow_logs_enabled
        if flow_logs_s3_bucket is not None:
            input_["flow_logs_s3_bucket"] = flow_logs_s3_bucket
        if flow_logs_s3_prefix is not None:
            input_["flow_logs_s3_prefix"] = flow_logs_s3_prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cross_account_attachment(
        self,
        attachment_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        name: Optional[
            "capo_global_accelerator.types.attachment_name.AttachmentName"
        ] = None,
        add_principals: Optional[
            "capo_global_accelerator.types.principals.Principals"
        ] = None,
        remove_principals: Optional[
            "capo_global_accelerator.types.principals.Principals"
        ] = None,
        add_resources: Optional[
            "capo_global_accelerator.types.resources.Resources"
        ] = None,
        remove_resources: Optional[
            "capo_global_accelerator.types.resources.Resources"
        ] = None,
    ) -> "capo_global_accelerator.types.update_cross_account_attachment_response.UpdateCrossAccountAttachmentResponse":
        """<p>Update a cross-account attachment to add or remove principals or resources. When you update an attachment to remove a principal (account ID or accelerator) or a resource, Global Accelerator revokes the permission for specific resources. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html"> Working with cross-account attachments and resources in Global Accelerator</a> in the <i> Global Accelerator Developer Guide</i>.</p>

        Args:
            attachment_arn: <p>The Amazon Resource Name (ARN) of the cross-account attachment to update.</p>
            name: <p>The name of the cross-account attachment. </p>
            add_principals: <p>The principals to add to the cross-account attachment. A principal is an account or the Amazon Resource Name (ARN) of an accelerator that the attachment gives permission to work with resources from another account. The resources are also listed in the attachment.</p> <p>To add more than one principal, separate the account numbers or accelerator ARNs, or both, with commas.</p>
            remove_principals: <p>The principals to remove from the cross-account attachment. A principal is an account or the Amazon Resource Name (ARN) of an accelerator that the attachment gives permission to work with resources from another account. The resources are also listed in the attachment.</p> <p>To remove more than one principal, separate the account numbers or accelerator ARNs, or both, with commas.</p>
            add_resources: <p>The resources to add to the cross-account attachment. A resource listed in a cross-account attachment can be used with an accelerator by the principals that are listed in the attachment.</p> <p>To add more than one resource, separate the resource ARNs with commas.</p>
            remove_resources: <p>The resources to remove from the cross-account attachment. A resource listed in a cross-account attachment can be used with an accelerator by the principals that are listed in the attachment.</p> <p>To remove more than one resource, separate the resource ARNs with commas.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.attachment_not_found_exception.AttachmentNotFoundException: <p>No cross-account attachment was found.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.update_cross_account_attachment_request.UpdateCrossAccountAttachmentRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.update_cross_account_attachment_response.UpdateCrossAccountAttachmentResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.update_cross_account_attachment

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.update_cross_account_attachment.update_cross_account_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.update_cross_account_attachment_request.UpdateCrossAccountAttachmentRequest = {
            "attachment_arn": attachment_arn
        }
        if name is not None:
            input_["name"] = name
        if add_principals is not None:
            input_["add_principals"] = add_principals
        if remove_principals is not None:
            input_["remove_principals"] = remove_principals
        if add_resources is not None:
            input_["add_resources"] = add_resources
        if remove_resources is not None:
            input_["remove_resources"] = remove_resources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_custom_routing_accelerator(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        name: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
        ip_address_type: Optional[
            "capo_global_accelerator.types.ip_address_type.IpAddressType"
        ] = None,
        ip_addresses: Optional[
            "capo_global_accelerator.types.ip_addresses.IpAddresses"
        ] = None,
        enabled: Optional[
            "capo_global_accelerator.types.generic_boolean.GenericBoolean"
        ] = None,
    ) -> "capo_global_accelerator.types.update_custom_routing_accelerator_response.UpdateCustomRoutingAcceleratorResponse":
        """<p>Update a custom routing accelerator. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the accelerator to update.</p>
            name: <p>The name of the accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters, periods (.), or hyphens (-), and must not begin or end with a hyphen or period.</p>
            ip_address_type: <p>The IP address type that an accelerator supports. For a custom routing accelerator, the value must be IPV4.</p>
            ip_addresses: <p>The IP addresses for an accelerator.</p>
            enabled: <p>Indicates whether an accelerator is enabled. The value is true or false. The default value is true. </p> <p>If the value is set to true, the accelerator cannot be deleted. If set to false, the accelerator can be deleted.</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.conflict_exception.ConflictException: <p>You can't use both of those options.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.update_custom_routing_accelerator_request.UpdateCustomRoutingAcceleratorRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.update_custom_routing_accelerator_response.UpdateCustomRoutingAcceleratorResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.update_custom_routing_accelerator

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.update_custom_routing_accelerator.update_custom_routing_accelerator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.update_custom_routing_accelerator_request.UpdateCustomRoutingAcceleratorRequest = {
            "accelerator_arn": accelerator_arn
        }
        if name is not None:
            input_["name"] = name
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if ip_addresses is not None:
            input_["ip_addresses"] = ip_addresses
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_custom_routing_accelerator_attributes(
        self,
        accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        flow_logs_enabled: Optional[
            "capo_global_accelerator.types.generic_boolean.GenericBoolean"
        ] = None,
        flow_logs_s3_bucket: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
        flow_logs_s3_prefix: Optional[
            "capo_global_accelerator.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_global_accelerator.types.update_custom_routing_accelerator_attributes_response.UpdateCustomRoutingAcceleratorAttributesResponse":
        """<p>Update the attributes for a custom routing accelerator. </p>

        Args:
            accelerator_arn: <p>The Amazon Resource Name (ARN) of the custom routing accelerator to update attributes for.</p>
            flow_logs_enabled: <p>Update whether flow logs are enabled. The default value is false. If the value is true, <code>FlowLogsS3Bucket</code> and <code>FlowLogsS3Prefix</code> must be specified.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html">Flow logs</a> in the <i>Global Accelerator Developer Guide</i>.</p>
            flow_logs_s3_bucket: <p>The name of the Amazon S3 bucket for the flow logs. Attribute is required if <code>FlowLogsEnabled</code> is <code>true</code>. The bucket must exist and have a bucket policy that grants Global Accelerator permission to write to the bucket.</p>
            flow_logs_s3_prefix: <p>Update the prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if <code>FlowLogsEnabled</code> is <code>true</code>. </p> <p>If you specify slash (/) for the S3 bucket prefix, the log file bucket folder structure will include a double slash (//), like the following:</p> <p>DOC-EXAMPLE-BUCKET//AWSLogs/aws_account_id</p>

        Raises:
            capo_global_accelerator.errors.accelerator_not_found_exception.AcceleratorNotFoundException: <p>The accelerator that you specified doesn't exist.</p>
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.transaction_in_progress_exception.TransactionInProgressException: <p>There's already a transaction in progress. Another transaction can't be processed.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.update_custom_routing_accelerator_attributes_request.UpdateCustomRoutingAcceleratorAttributesRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.update_custom_routing_accelerator_attributes_response.UpdateCustomRoutingAcceleratorAttributesResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.update_custom_routing_accelerator_attributes

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.update_custom_routing_accelerator_attributes.update_custom_routing_accelerator_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.update_custom_routing_accelerator_attributes_request.UpdateCustomRoutingAcceleratorAttributesRequest = {
            "accelerator_arn": accelerator_arn
        }
        if flow_logs_enabled is not None:
            input_["flow_logs_enabled"] = flow_logs_enabled
        if flow_logs_s3_bucket is not None:
            input_["flow_logs_s3_bucket"] = flow_logs_s3_bucket
        if flow_logs_s3_prefix is not None:
            input_["flow_logs_s3_prefix"] = flow_logs_s3_prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_custom_routing_listener(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        port_ranges: "capo_global_accelerator.types.port_ranges.PortRanges",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.update_custom_routing_listener_response.UpdateCustomRoutingListenerResponse":
        """<p>Update a listener for a custom routing accelerator. </p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener to update.</p>
            port_ranges: <p>The updated port range to support for connections from clients to your accelerator. If you remove ports that are currently being used by a subnet endpoint, the call fails.</p> <p>Separately, you set port ranges for endpoints. For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html">About endpoints for custom routing accelerators</a>.</p>

        Raises:
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_port_range_exception.InvalidPortRangeException: <p>The port numbers that you specified are not valid numbers or are not unique for this accelerator.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.update_custom_routing_listener_request.UpdateCustomRoutingListenerRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.update_custom_routing_listener_response.UpdateCustomRoutingListenerResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.update_custom_routing_listener

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.update_custom_routing_listener.update_custom_routing_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.update_custom_routing_listener_request.UpdateCustomRoutingListenerRequest = {
            "listener_arn": listener_arn,
            "port_ranges": port_ranges,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_endpoint_group(
        self,
        endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        endpoint_configurations: Optional[
            "capo_global_accelerator.types.endpoint_configurations.EndpointConfigurations"
        ] = None,
        traffic_dial_percentage: Optional[
            "capo_global_accelerator.types.traffic_dial_percentage.TrafficDialPercentage"
        ] = None,
        health_check_port: Optional[
            "capo_global_accelerator.types.health_check_port.HealthCheckPort"
        ] = None,
        health_check_protocol: Optional[
            "capo_global_accelerator.types.health_check_protocol.HealthCheckProtocol"
        ] = None,
        health_check_path: Optional[
            "capo_global_accelerator.types.health_check_path.HealthCheckPath"
        ] = None,
        health_check_interval_seconds: Optional[
            "capo_global_accelerator.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
        ] = None,
        threshold_count: Optional[
            "capo_global_accelerator.types.threshold_count.ThresholdCount"
        ] = None,
        port_overrides: Optional[
            "capo_global_accelerator.types.port_overrides.PortOverrides"
        ] = None,
    ) -> "capo_global_accelerator.types.update_endpoint_group_response.UpdateEndpointGroupResponse":
        """<p>Update an endpoint group. A resource must be valid and active when you add it as an endpoint.</p>

        Args:
            endpoint_group_arn: <p>The Amazon Resource Name (ARN) of the endpoint group.</p>
            endpoint_configurations: <p>The list of endpoint objects. A resource must be valid and active when you add it as an endpoint.</p>
            traffic_dial_percentage: <p>The percentage of traffic to send to an Amazon Web Services Region. Additional traffic is distributed to other endpoint groups for this listener. </p> <p>Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.</p> <p>The default value is 100.</p>
            health_check_port: <p>The port that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If the listener port is a list of ports, Global Accelerator uses the first port in the list.</p>
            health_check_protocol: <p>The protocol that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.</p>
            health_check_path: <p>If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).</p>
            health_check_interval_seconds: <p>The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.</p>
            threshold_count: <p>The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</p>
            port_overrides: <p>Override specific listener ports used to route traffic to endpoints that are part of this endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html"> Overriding listener ports</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.endpoint_group_not_found_exception.EndpointGroupNotFoundException: <p>The endpoint group that you specified doesn't exist.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.update_endpoint_group_request.UpdateEndpointGroupRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.update_endpoint_group_response.UpdateEndpointGroupResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.update_endpoint_group

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.update_endpoint_group.update_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.update_endpoint_group_request.UpdateEndpointGroupRequest = {
            "endpoint_group_arn": endpoint_group_arn
        }
        if endpoint_configurations is not None:
            input_["endpoint_configurations"] = endpoint_configurations
        if traffic_dial_percentage is not None:
            input_["traffic_dial_percentage"] = traffic_dial_percentage
        if health_check_port is not None:
            input_["health_check_port"] = health_check_port
        if health_check_protocol is not None:
            input_["health_check_protocol"] = health_check_protocol
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if health_check_interval_seconds is not None:
            input_["health_check_interval_seconds"] = health_check_interval_seconds
        if threshold_count is not None:
            input_["threshold_count"] = threshold_count
        if port_overrides is not None:
            input_["port_overrides"] = port_overrides

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_listener(
        self,
        listener_arn: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
        port_ranges: Optional[
            "capo_global_accelerator.types.port_ranges.PortRanges"
        ] = None,
        protocol: Optional["capo_global_accelerator.types.protocol.Protocol"] = None,
        client_affinity: Optional[
            "capo_global_accelerator.types.client_affinity.ClientAffinity"
        ] = None,
    ) -> (
        "capo_global_accelerator.types.update_listener_response.UpdateListenerResponse"
    ):
        """<p>Update a listener. </p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener to update.</p>
            port_ranges: <p>The updated list of port ranges for the connections from clients to the accelerator.</p>
            protocol: <p>The updated protocol for the connections from clients to the accelerator.</p>
            client_affinity: <p>Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Client affinity gives you control over whether to always route each client to the same specific endpoint.</p> <p>Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is <code>NONE</code>, Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes. </p> <p>If you want a given client to always be routed to the same endpoint, set client affinity to <code>SOURCE_IP</code> instead. When you use the <code>SOURCE_IP</code> setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.</p> <p>The default value is <code>NONE</code>.</p>

        Raises:
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.invalid_port_range_exception.InvalidPortRangeException: <p>The port numbers that you specified are not valid numbers or are not unique for this accelerator.</p>
            capo_global_accelerator.errors.limit_exceeded_exception.LimitExceededException: <p>Processing your request would cause you to exceed an Global Accelerator limit.</p>
            capo_global_accelerator.errors.listener_not_found_exception.ListenerNotFoundException: <p>The listener that you specified doesn't exist.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.update_listener_request.UpdateListenerRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.update_listener_response.UpdateListenerResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.update_listener

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.update_listener.update_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.update_listener_request.UpdateListenerRequest = {
            "listener_arn": listener_arn
        }
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges
        if protocol is not None:
            input_["protocol"] = protocol
        if client_affinity is not None:
            input_["client_affinity"] = client_affinity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def withdraw_byoip_cidr(
        self,
        cidr: "capo_global_accelerator.types.generic_string.GenericString",
        *,
        config_overrides: Optional[GlobalAcceleratorClientConfig] = None,
    ) -> "capo_global_accelerator.types.withdraw_byoip_cidr_response.WithdrawByoipCidrResponse":
        """<p>Stops advertising an address range that is provisioned as an address pool. You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time.</p> <p>It can take a few minutes before traffic to the specified addresses stops routing to Amazon Web Services because of propagation delays.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the <i>Global Accelerator Developer Guide</i>.</p>

        Args:
            cidr: <p>The address range, in CIDR notation.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>

        Raises:
            capo_global_accelerator.errors.access_denied_exception.AccessDeniedException: <p>You don't have access permission.</p>
            capo_global_accelerator.errors.byoip_cidr_not_found_exception.ByoipCidrNotFoundException: <p>The CIDR that you specified was not found or is incorrect.</p>
            capo_global_accelerator.errors.incorrect_cidr_state_exception.IncorrectCidrStateException: <p>The CIDR that you specified is not valid for this action. For example, the state of the CIDR might be incorrect for this action.</p>
            capo_global_accelerator.errors.internal_service_error_exception.InternalServiceErrorException: <p>There was an internal error for Global Accelerator.</p>
            capo_global_accelerator.errors.invalid_argument_exception.InvalidArgumentException: <p>An argument that you specified is invalid.</p>
            capo_global_accelerator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_global_accelerator.types.withdraw_byoip_cidr_request.WithdrawByoipCidrRequest]",
        ) -> OperationResponse[
            "capo_global_accelerator.types.withdraw_byoip_cidr_response.WithdrawByoipCidrResponse"
        ]:
            import capo_global_accelerator._operations.global_accelerator_v20180706.withdraw_byoip_cidr

            output, http_response = (
                capo_global_accelerator._operations.global_accelerator_v20180706.withdraw_byoip_cidr.withdraw_byoip_cidr(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_global_accelerator.types.withdraw_byoip_cidr_request.WithdrawByoipCidrRequest = {
            "cidr": cidr
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
