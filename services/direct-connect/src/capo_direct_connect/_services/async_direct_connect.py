"""Generated from Smithy shape ``com.amazonaws.directconnect#OvertureService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_direct_connect._auth._signers
import capo_direct_connect._auth._sigv4
from capo_direct_connect._auth._identity import Credentials
from capo_direct_connect._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_direct_connect._auth._zapros_handler import AuthMiddleware
from capo_direct_connect._services._aws_config import aaws_config
from capo_direct_connect._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_direct_connect.types.accept_direct_connect_gateway_association_proposal_request
    import capo_direct_connect.types.accept_direct_connect_gateway_association_proposal_result
    import capo_direct_connect.types.agreement_name
    import capo_direct_connect.types.allocate_connection_on_interconnect_request
    import capo_direct_connect.types.allocate_hosted_connection_request
    import capo_direct_connect.types.allocate_private_virtual_interface_request
    import capo_direct_connect.types.allocate_public_virtual_interface_request
    import capo_direct_connect.types.allocate_transit_virtual_interface_request
    import capo_direct_connect.types.allocate_transit_virtual_interface_result
    import capo_direct_connect.types.asn
    import capo_direct_connect.types.associate_connection_with_lag_request
    import capo_direct_connect.types.associate_connections_to_resiliency_group_request
    import capo_direct_connect.types.associate_connections_to_resiliency_group_result
    import capo_direct_connect.types.associate_hosted_connection_request
    import capo_direct_connect.types.associate_mac_sec_key_request
    import capo_direct_connect.types.associate_mac_sec_key_response
    import capo_direct_connect.types.associate_virtual_interface_request
    import capo_direct_connect.types.associated_gateway_id
    import capo_direct_connect.types.bandwidth
    import capo_direct_connect.types.bgp_peer_id
    import capo_direct_connect.types.bgp_peer_id_list
    import capo_direct_connect.types.cak
    import capo_direct_connect.types.ckn
    import capo_direct_connect.types.confirm_connection_request
    import capo_direct_connect.types.confirm_connection_response
    import capo_direct_connect.types.confirm_customer_agreement_request
    import capo_direct_connect.types.confirm_customer_agreement_response
    import capo_direct_connect.types.confirm_private_virtual_interface_request
    import capo_direct_connect.types.confirm_private_virtual_interface_response
    import capo_direct_connect.types.confirm_public_virtual_interface_request
    import capo_direct_connect.types.confirm_public_virtual_interface_response
    import capo_direct_connect.types.confirm_transit_virtual_interface_request
    import capo_direct_connect.types.confirm_transit_virtual_interface_response
    import capo_direct_connect.types.connection
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.connection_id_list
    import capo_direct_connect.types.connection_identifier_list
    import capo_direct_connect.types.connection_name
    import capo_direct_connect.types.connections
    import capo_direct_connect.types.count
    import capo_direct_connect.types.create_bgp_peer_request
    import capo_direct_connect.types.create_bgp_peer_response
    import capo_direct_connect.types.create_connection_request
    import capo_direct_connect.types.create_direct_connect_gateway_association_proposal_request
    import capo_direct_connect.types.create_direct_connect_gateway_association_proposal_result
    import capo_direct_connect.types.create_direct_connect_gateway_association_request
    import capo_direct_connect.types.create_direct_connect_gateway_association_result
    import capo_direct_connect.types.create_direct_connect_gateway_request
    import capo_direct_connect.types.create_direct_connect_gateway_result
    import capo_direct_connect.types.create_interconnect_request
    import capo_direct_connect.types.create_lag_request
    import capo_direct_connect.types.create_private_virtual_interface_request
    import capo_direct_connect.types.create_public_virtual_interface_request
    import capo_direct_connect.types.create_resiliency_group_request
    import capo_direct_connect.types.create_resiliency_group_result
    import capo_direct_connect.types.create_transit_virtual_interface_request
    import capo_direct_connect.types.create_transit_virtual_interface_result
    import capo_direct_connect.types.customer_address
    import capo_direct_connect.types.delete_bgp_peer_request
    import capo_direct_connect.types.delete_bgp_peer_response
    import capo_direct_connect.types.delete_connection_request
    import capo_direct_connect.types.delete_direct_connect_gateway_association_proposal_request
    import capo_direct_connect.types.delete_direct_connect_gateway_association_proposal_result
    import capo_direct_connect.types.delete_direct_connect_gateway_association_request
    import capo_direct_connect.types.delete_direct_connect_gateway_association_result
    import capo_direct_connect.types.delete_direct_connect_gateway_request
    import capo_direct_connect.types.delete_direct_connect_gateway_result
    import capo_direct_connect.types.delete_interconnect_request
    import capo_direct_connect.types.delete_interconnect_response
    import capo_direct_connect.types.delete_lag_request
    import capo_direct_connect.types.delete_resiliency_group_request
    import capo_direct_connect.types.delete_resiliency_group_result
    import capo_direct_connect.types.delete_virtual_interface_request
    import capo_direct_connect.types.delete_virtual_interface_response
    import capo_direct_connect.types.describe_connection_loa_request
    import capo_direct_connect.types.describe_connection_loa_response
    import capo_direct_connect.types.describe_connections_on_interconnect_request
    import capo_direct_connect.types.describe_connections_request
    import capo_direct_connect.types.describe_customer_metadata_response
    import capo_direct_connect.types.describe_direct_connect_gateway_association_proposals_request
    import capo_direct_connect.types.describe_direct_connect_gateway_association_proposals_result
    import capo_direct_connect.types.describe_direct_connect_gateway_associations_request
    import capo_direct_connect.types.describe_direct_connect_gateway_associations_result
    import capo_direct_connect.types.describe_direct_connect_gateway_attachments_request
    import capo_direct_connect.types.describe_direct_connect_gateway_attachments_result
    import capo_direct_connect.types.describe_direct_connect_gateways_request
    import capo_direct_connect.types.describe_direct_connect_gateways_result
    import capo_direct_connect.types.describe_hosted_connections_request
    import capo_direct_connect.types.describe_interconnect_loa_request
    import capo_direct_connect.types.describe_interconnect_loa_response
    import capo_direct_connect.types.describe_interconnects_request
    import capo_direct_connect.types.describe_lags_request
    import capo_direct_connect.types.describe_loa_request
    import capo_direct_connect.types.describe_router_configuration_request
    import capo_direct_connect.types.describe_router_configuration_response
    import capo_direct_connect.types.describe_tags_request
    import capo_direct_connect.types.describe_tags_response
    import capo_direct_connect.types.describe_virtual_interfaces_request
    import capo_direct_connect.types.direct_connect_gateway_association_id
    import capo_direct_connect.types.direct_connect_gateway_association_proposal_id
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.direct_connect_gateway_name
    import capo_direct_connect.types.disassociate_connection_from_lag_request
    import capo_direct_connect.types.disassociate_connections_from_resiliency_group_request
    import capo_direct_connect.types.disassociate_connections_from_resiliency_group_result
    import capo_direct_connect.types.disassociate_mac_sec_key_request
    import capo_direct_connect.types.disassociate_mac_sec_key_response
    import capo_direct_connect.types.enable_site_link
    import capo_direct_connect.types.encryption_mode
    import capo_direct_connect.types.failure_test_history_status
    import capo_direct_connect.types.gateway_id_to_associate
    import capo_direct_connect.types.get_resiliency_group_request
    import capo_direct_connect.types.get_resiliency_group_result
    import capo_direct_connect.types.idempotency_token
    import capo_direct_connect.types.interconnect
    import capo_direct_connect.types.interconnect_id
    import capo_direct_connect.types.interconnect_name
    import capo_direct_connect.types.interconnects
    import capo_direct_connect.types.lag
    import capo_direct_connect.types.lag_id
    import capo_direct_connect.types.lag_name
    import capo_direct_connect.types.lags
    import capo_direct_connect.types.list_resiliency_group_associations_request
    import capo_direct_connect.types.list_resiliency_group_associations_result
    import capo_direct_connect.types.list_resiliency_groups_request
    import capo_direct_connect.types.list_resiliency_groups_result
    import capo_direct_connect.types.list_virtual_interface_routes_request
    import capo_direct_connect.types.list_virtual_interface_routes_response
    import capo_direct_connect.types.list_virtual_interface_test_history_request
    import capo_direct_connect.types.list_virtual_interface_test_history_response
    import capo_direct_connect.types.loa
    import capo_direct_connect.types.loa_content_type
    import capo_direct_connect.types.location_code
    import capo_direct_connect.types.locations
    import capo_direct_connect.types.long_asn
    import capo_direct_connect.types.max_result_set_size
    import capo_direct_connect.types.mtu
    import capo_direct_connect.types.new_bgp_peer
    import capo_direct_connect.types.new_private_virtual_interface
    import capo_direct_connect.types.new_private_virtual_interface_allocation
    import capo_direct_connect.types.new_public_virtual_interface
    import capo_direct_connect.types.new_public_virtual_interface_allocation
    import capo_direct_connect.types.new_transit_virtual_interface
    import capo_direct_connect.types.new_transit_virtual_interface_allocation
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.prefix_pool_allocated_count
    import capo_direct_connect.types.provider_name
    import capo_direct_connect.types.rate_limit
    import capo_direct_connect.types.request_billing_mode
    import capo_direct_connect.types.request_mac_sec
    import capo_direct_connect.types.resiliency_group_id
    import capo_direct_connect.types.resiliency_group_name
    import capo_direct_connect.types.resiliency_model
    import capo_direct_connect.types.resource_arn
    import capo_direct_connect.types.resource_arn_list
    import capo_direct_connect.types.route_filter_prefix_list
    import capo_direct_connect.types.route_filters
    import capo_direct_connect.types.router_type_identifier
    import capo_direct_connect.types.secret_arn
    import capo_direct_connect.types.start_bgp_failover_test_request
    import capo_direct_connect.types.start_bgp_failover_test_response
    import capo_direct_connect.types.stop_bgp_failover_test_request
    import capo_direct_connect.types.stop_bgp_failover_test_response
    import capo_direct_connect.types.tag_key_list
    import capo_direct_connect.types.tag_list
    import capo_direct_connect.types.tag_resource_request
    import capo_direct_connect.types.tag_resource_response
    import capo_direct_connect.types.test_duration
    import capo_direct_connect.types.test_id
    import capo_direct_connect.types.untag_resource_request
    import capo_direct_connect.types.untag_resource_response
    import capo_direct_connect.types.update_connection_request
    import capo_direct_connect.types.update_connections_billing_mode_request
    import capo_direct_connect.types.update_connections_billing_mode_response
    import capo_direct_connect.types.update_direct_connect_gateway_association_request
    import capo_direct_connect.types.update_direct_connect_gateway_association_result
    import capo_direct_connect.types.update_direct_connect_gateway_request
    import capo_direct_connect.types.update_direct_connect_gateway_response
    import capo_direct_connect.types.update_lag_request
    import capo_direct_connect.types.update_resiliency_group_request
    import capo_direct_connect.types.update_resiliency_group_result
    import capo_direct_connect.types.update_virtual_interface_attributes_request
    import capo_direct_connect.types.virtual_gateway_id
    import capo_direct_connect.types.virtual_gateways
    import capo_direct_connect.types.virtual_interface
    import capo_direct_connect.types.virtual_interface_id
    import capo_direct_connect.types.virtual_interface_name
    import capo_direct_connect.types.virtual_interfaces
    import capo_direct_connect.types.vlan


class AsyncDirectConnectClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncDirectConnectClient:
    """A client for the ``DirectConnect`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncDirectConnectClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncDirectConnectClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDirectConnectClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def accept_direct_connect_gateway_association_proposal(
        self,
        direct_connect_gateway_id: "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        proposal_id: "capo_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId",
        associated_gateway_owner_account: "capo_direct_connect.types.owner_account.OwnerAccount",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        override_allowed_prefixes_to_direct_connect_gateway: Optional[
            "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
    ) -> "capo_direct_connect.types.accept_direct_connect_gateway_association_proposal_result.AcceptDirectConnectGatewayAssociationProposalResult":
        """<p>Accepts a proposal request to attach a virtual private gateway or transit gateway to a Direct Connect gateway.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            proposal_id: <p>The ID of the request proposal.</p>
            associated_gateway_owner_account: <p>The ID of the Amazon Web Services account that owns the virtual private gateway or transit gateway.</p>
            override_allowed_prefixes_to_direct_connect_gateway: <p>Overrides the Amazon VPC prefixes advertised to the Direct Connect gateway.</p> <p>For information about how to set the prefixes, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-vgw.html#allowed-prefixes">Allowed Prefixes</a> in the <i>Direct Connect User Guide</i>.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.accept_direct_connect_gateway_association_proposal_request.AcceptDirectConnectGatewayAssociationProposalRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.accept_direct_connect_gateway_association_proposal_result.AcceptDirectConnectGatewayAssociationProposalResult"
        ]:
            import capo_direct_connect._operations.overture_service.accept_direct_connect_gateway_association_proposal

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.accept_direct_connect_gateway_association_proposal.async_accept_direct_connect_gateway_association_proposal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.accept_direct_connect_gateway_association_proposal_request.AcceptDirectConnectGatewayAssociationProposalRequest = {
            "direct_connect_gateway_id": direct_connect_gateway_id,
            "proposal_id": proposal_id,
            "associated_gateway_owner_account": associated_gateway_owner_account,
        }
        if override_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["override_allowed_prefixes_to_direct_connect_gateway"] = (
                override_allowed_prefixes_to_direct_connect_gateway
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def allocate_connection_on_interconnect(
        self,
        bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth",
        connection_name: "capo_direct_connect.types.connection_name.ConnectionName",
        owner_account: "capo_direct_connect.types.owner_account.OwnerAccount",
        interconnect_id: "capo_direct_connect.types.interconnect_id.InterconnectId",
        vlan: "capo_direct_connect.types.vlan.VLAN",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.connection.Connection":
        """<note> <p>Deprecated. Use <a>AllocateHostedConnection</a> instead.</p> </note> <p>Creates a hosted connection on an interconnect.</p> <p>Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the specified interconnect.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            bandwidth: <p>The bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, and 10Gbps. Note that only those Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps or 10Gbps hosted connection.</p>
            connection_name: <p>The name of the provisioned connection.</p>
            owner_account: <p>The ID of the Amazon Web Services account of the customer for whom the connection will be provisioned.</p>
            interconnect_id: <p>The ID of the interconnect on which the connection will be provisioned.</p>
            vlan: <p>The dedicated VLAN provisioned to the connection.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.allocate_connection_on_interconnect_request.AllocateConnectionOnInterconnectRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.connection.Connection"]:
            import capo_direct_connect._operations.overture_service.allocate_connection_on_interconnect

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.allocate_connection_on_interconnect.async_allocate_connection_on_interconnect(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.allocate_connection_on_interconnect_request.AllocateConnectionOnInterconnectRequest = {
            "bandwidth": bandwidth,
            "connection_name": connection_name,
            "owner_account": owner_account,
            "interconnect_id": interconnect_id,
            "vlan": vlan,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def allocate_hosted_connection(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        owner_account: "capo_direct_connect.types.owner_account.OwnerAccount",
        bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth",
        connection_name: "capo_direct_connect.types.connection_name.ConnectionName",
        vlan: "capo_direct_connect.types.vlan.VLAN",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        tags: Optional["capo_direct_connect.types.tag_list.TagList"] = None,
    ) -> "capo_direct_connect.types.connection.Connection":
        """<p>Creates a hosted connection on the specified interconnect or a link aggregation group (LAG) of interconnects.</p> <p>Allocates a VLAN number and a specified amount of capacity (bandwidth) for use by a hosted connection on the specified interconnect or LAG of interconnects. Amazon Web Services polices the hosted connection for the specified capacity and the Direct Connect Partner must also police the hosted connection for the specified capacity.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            connection_id: <p>The ID of the interconnect or LAG.</p>
            owner_account: <p>The ID of the Amazon Web Services account ID of the customer for the connection.</p>
            bandwidth: <p>The bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, 10Gbps, and 25Gbps. Note that only those Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps, 10Gbps, or 25Gbps hosted connection. </p>
            connection_name: <p>The name of the hosted connection.</p>
            vlan: <p>The dedicated VLAN provisioned to the hosted connection.</p>
            tags: <p>The tags associated with the connection.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.allocate_hosted_connection_request.AllocateHostedConnectionRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.connection.Connection"]:
            import capo_direct_connect._operations.overture_service.allocate_hosted_connection

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.allocate_hosted_connection.async_allocate_hosted_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.allocate_hosted_connection_request.AllocateHostedConnectionRequest = {
            "connection_id": connection_id,
            "owner_account": owner_account,
            "bandwidth": bandwidth,
            "connection_name": connection_name,
            "vlan": vlan,
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

    async def allocate_private_virtual_interface(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        owner_account: "capo_direct_connect.types.owner_account.OwnerAccount",
        new_private_virtual_interface_allocation: "capo_direct_connect.types.new_private_virtual_interface_allocation.NewPrivateVirtualInterfaceAllocation",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Provisions a private virtual interface to be owned by the specified Amazon Web Services account.</p> <p>Virtual interfaces created using this action must be confirmed by the owner using <a>ConfirmPrivateVirtualInterface</a>. Until then, the virtual interface is in the <code>Confirming</code> state and is not available to handle traffic.</p>

        Args:
            connection_id: <p>The ID of the connection on which the private virtual interface is provisioned.</p>
            owner_account: <p>The ID of the Amazon Web Services account that owns the virtual private interface.</p>
            new_private_virtual_interface_allocation: <p>Information about the private virtual interface.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.limit_exceeded_exception.LimitExceededException: <p>The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.allocate_private_virtual_interface_request.AllocatePrivateVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import capo_direct_connect._operations.overture_service.allocate_private_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.allocate_private_virtual_interface.async_allocate_private_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.allocate_private_virtual_interface_request.AllocatePrivateVirtualInterfaceRequest = {
            "connection_id": connection_id,
            "owner_account": owner_account,
            "new_private_virtual_interface_allocation": new_private_virtual_interface_allocation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def allocate_public_virtual_interface(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        owner_account: "capo_direct_connect.types.owner_account.OwnerAccount",
        new_public_virtual_interface_allocation: "capo_direct_connect.types.new_public_virtual_interface_allocation.NewPublicVirtualInterfaceAllocation",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Provisions a public virtual interface to be owned by the specified Amazon Web Services account.</p> <p>The owner of a connection calls this function to provision a public virtual interface to be owned by the specified Amazon Web Services account.</p> <p>Virtual interfaces created using this function must be confirmed by the owner using <a>ConfirmPublicVirtualInterface</a>. Until this step has been completed, the virtual interface is in the <code>confirming</code> state and is not available to handle traffic.</p> <p>When creating an IPv6 public virtual interface, omit the Amazon address and customer address. IPv6 addresses are automatically assigned from the Amazon pool of IPv6 addresses; you cannot specify custom IPv6 addresses.</p>

        Args:
            connection_id: <p>The ID of the connection on which the public virtual interface is provisioned.</p>
            owner_account: <p>The ID of the Amazon Web Services account that owns the public virtual interface.</p>
            new_public_virtual_interface_allocation: <p>Information about the public virtual interface.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.limit_exceeded_exception.LimitExceededException: <p>The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.allocate_public_virtual_interface_request.AllocatePublicVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import capo_direct_connect._operations.overture_service.allocate_public_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.allocate_public_virtual_interface.async_allocate_public_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.allocate_public_virtual_interface_request.AllocatePublicVirtualInterfaceRequest = {
            "connection_id": connection_id,
            "owner_account": owner_account,
            "new_public_virtual_interface_allocation": new_public_virtual_interface_allocation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def allocate_transit_virtual_interface(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        owner_account: "capo_direct_connect.types.owner_account.OwnerAccount",
        new_transit_virtual_interface_allocation: "capo_direct_connect.types.new_transit_virtual_interface_allocation.NewTransitVirtualInterfaceAllocation",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.allocate_transit_virtual_interface_result.AllocateTransitVirtualInterfaceResult":
        """<p>Provisions a transit virtual interface to be owned by the specified Amazon Web Services account. Use this type of interface to connect a transit gateway to your Direct Connect gateway.</p> <p>The owner of a connection provisions a transit virtual interface to be owned by the specified Amazon Web Services account.</p> <p>After you create a transit virtual interface, it must be confirmed by the owner using <a>ConfirmTransitVirtualInterface</a>. Until this step has been completed, the transit virtual interface is in the <code>requested</code> state and is not available to handle traffic.</p>

        Args:
            connection_id: <p>The ID of the connection on which the transit virtual interface is provisioned.</p>
            owner_account: <p>The ID of the Amazon Web Services account that owns the transit virtual interface.</p>
            new_transit_virtual_interface_allocation: <p>Information about the transit virtual interface.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.limit_exceeded_exception.LimitExceededException: <p>The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.allocate_transit_virtual_interface_request.AllocateTransitVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.allocate_transit_virtual_interface_result.AllocateTransitVirtualInterfaceResult"
        ]:
            import capo_direct_connect._operations.overture_service.allocate_transit_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.allocate_transit_virtual_interface.async_allocate_transit_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.allocate_transit_virtual_interface_request.AllocateTransitVirtualInterfaceRequest = {
            "connection_id": connection_id,
            "owner_account": owner_account,
            "new_transit_virtual_interface_allocation": new_transit_virtual_interface_allocation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_connections_to_resiliency_group(
        self,
        connection_identifiers: "capo_direct_connect.types.connection_identifier_list.ConnectionIdentifierList",
        resiliency_group_id: "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        client_token: Optional[
            "capo_direct_connect.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_direct_connect.types.associate_connections_to_resiliency_group_result.AssociateConnectionsToResiliencyGroupResult":
        """<p>Associates one or more connections with the specified resiliency group. This operation is atomic: either all of the specified connections are associated, or the operation fails and no changes are made.</p>

        Args:
            connection_identifiers: <p>The IDs or ARNs of the connections to associate with the resiliency group.</p>
            resiliency_group_id: <p>The ID of the resiliency group.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.limit_exceeded_exception.LimitExceededException: <p>The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.associate_connections_to_resiliency_group_request.AssociateConnectionsToResiliencyGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.associate_connections_to_resiliency_group_result.AssociateConnectionsToResiliencyGroupResult"
        ]:
            import capo_direct_connect._operations.overture_service.associate_connections_to_resiliency_group

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.associate_connections_to_resiliency_group.async_associate_connections_to_resiliency_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.associate_connections_to_resiliency_group_request.AssociateConnectionsToResiliencyGroupRequest = {
            "connection_identifiers": connection_identifiers,
            "resiliency_group_id": resiliency_group_id,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_connection_with_lag(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        lag_id: "capo_direct_connect.types.lag_id.LagId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.connection.Connection":
        """<p>Associates an existing connection with a link aggregation group (LAG). The connection is interrupted and re-established as a member of the LAG (connectivity to Amazon Web Services is interrupted). The connection must be hosted on the same Direct Connect endpoint as the LAG, and its bandwidth must match the bandwidth for the LAG. You can re-associate a connection that's currently associated with a different LAG; however, if removing the connection would cause the original LAG to fall below its setting for minimum number of operational connections, the request fails.</p> <p>Any virtual interfaces that are directly associated with the connection are automatically re-associated with the LAG. If the connection was originally associated with a different LAG, the virtual interfaces remain associated with the original LAG.</p> <p>For interconnects, any hosted connections are automatically re-associated with the LAG. If the interconnect was originally associated with a different LAG, the hosted connections remain associated with the original LAG.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            lag_id: <p>The ID of the LAG with which to associate the connection.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.limit_exceeded_exception.LimitExceededException: <p>The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.associate_connection_with_lag_request.AssociateConnectionWithLagRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.connection.Connection"]:
            import capo_direct_connect._operations.overture_service.associate_connection_with_lag

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.associate_connection_with_lag.async_associate_connection_with_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.associate_connection_with_lag_request.AssociateConnectionWithLagRequest = {
            "connection_id": connection_id,
            "lag_id": lag_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_hosted_connection(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        parent_connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.connection.Connection":
        """<p>Associates a hosted connection and its virtual interfaces with a link aggregation group (LAG) or interconnect. If the target interconnect or LAG has an existing hosted connection with a conflicting VLAN number or IP address, the operation fails. This action temporarily interrupts the hosted connection's connectivity to Amazon Web Services as it is being migrated.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            connection_id: <p>The ID of the hosted connection.</p>
            parent_connection_id: <p>The ID of the interconnect or the LAG.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.associate_hosted_connection_request.AssociateHostedConnectionRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.connection.Connection"]:
            import capo_direct_connect._operations.overture_service.associate_hosted_connection

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.associate_hosted_connection.async_associate_hosted_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.associate_hosted_connection_request.AssociateHostedConnectionRequest = {
            "connection_id": connection_id,
            "parent_connection_id": parent_connection_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_mac_sec_key(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        secret_arn: Optional["capo_direct_connect.types.secret_arn.SecretARN"] = None,
        ckn: Optional["capo_direct_connect.types.ckn.Ckn"] = None,
        cak: Optional["capo_direct_connect.types.cak.Cak"] = None,
    ) -> "capo_direct_connect.types.associate_mac_sec_key_response.AssociateMacSecKeyResponse":
        """<p>Associates a MAC Security (MACsec) Connection Key Name (CKN)/ Connectivity Association Key (CAK) pair with a Direct Connect connection.</p> <p>You must supply either the <code>secretARN,</code> or the CKN/CAK (<code>ckn</code> and <code>cak</code>) pair in the request.</p> <p>For information about MAC Security (MACsec) key considerations, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-key-consideration">MACsec pre-shared CKN/CAK key considerations </a> in the <i>Direct Connect User Guide</i>.</p>

        Args:
            connection_id: <p>The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).</p> <p>You can use <a>DescribeConnections</a>, <a>DescribeInterconnects</a>, or <a>DescribeLags</a> to retrieve connection ID.</p>
            secret_arn: <p>The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key to associate with the connection.</p> <p>You can use <a>DescribeConnections</a> or <a>DescribeLags</a> to retrieve the MAC Security (MACsec) secret key.</p> <p>If you use this request parameter, you do not use the <code>ckn</code> and <code>cak</code> request parameters.</p>
            ckn: <p>The MAC Security (MACsec) CKN to associate with the connection.</p> <p>You can create the CKN/CAK pair using an industry standard tool.</p> <p> The valid values are 64 hexadecimal characters (0-9, A-E).</p> <p>If you use this request parameter, you must use the <code>cak</code> request parameter and not use the <code>secretARN</code> request parameter.</p>
            cak: <p>The MAC Security (MACsec) CAK to associate with the connection.</p> <p>You can create the CKN/CAK pair using an industry standard tool.</p> <p> The valid values are 64 hexadecimal characters (0-9, A-E).</p> <p>If you use this request parameter, you must use the <code>ckn</code> request parameter and not use the <code>secretARN</code> request parameter.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.associate_mac_sec_key_request.AssociateMacSecKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.associate_mac_sec_key_response.AssociateMacSecKeyResponse"
        ]:
            import capo_direct_connect._operations.overture_service.associate_mac_sec_key

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.associate_mac_sec_key.async_associate_mac_sec_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.associate_mac_sec_key_request.AssociateMacSecKeyRequest = {
            "connection_id": connection_id
        }
        if secret_arn is not None:
            input_["secret_arn"] = secret_arn
        if ckn is not None:
            input_["ckn"] = ckn
        if cak is not None:
            input_["cak"] = cak

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_virtual_interface(
        self,
        virtual_interface_id: "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Associates a virtual interface with a specified link aggregation group (LAG) or connection. Connectivity to Amazon Web Services is temporarily interrupted as the virtual interface is being migrated. If the target connection or LAG has an associated virtual interface with a conflicting VLAN number or a conflicting IP address, the operation fails.</p> <p>Virtual interfaces associated with a hosted connection cannot be associated with a LAG; hosted connections must be migrated along with their virtual interfaces using <a>AssociateHostedConnection</a>.</p> <p>To reassociate a virtual interface to a new connection or LAG, the requester must own either the virtual interface itself or the connection to which the virtual interface is currently associated. Additionally, the requester must own the connection or LAG for the association.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            connection_id: <p>The ID of the LAG or connection.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.associate_virtual_interface_request.AssociateVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import capo_direct_connect._operations.overture_service.associate_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.associate_virtual_interface.async_associate_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.associate_virtual_interface_request.AssociateVirtualInterfaceRequest = {
            "virtual_interface_id": virtual_interface_id,
            "connection_id": connection_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def confirm_connection(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.confirm_connection_response.ConfirmConnectionResponse":
        """<p>Confirms the creation of the specified hosted connection on an interconnect.</p> <p>Upon creation, the hosted connection is initially in the <code>Ordering</code> state, and remains in this state until the owner confirms creation of the hosted connection.</p>

        Args:
            connection_id: <p>The ID of the hosted connection.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.confirm_connection_request.ConfirmConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.confirm_connection_response.ConfirmConnectionResponse"
        ]:
            import capo_direct_connect._operations.overture_service.confirm_connection

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.confirm_connection.async_confirm_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.confirm_connection_request.ConfirmConnectionRequest = {
            "connection_id": connection_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def confirm_customer_agreement(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        agreement_name: Optional[
            "capo_direct_connect.types.agreement_name.AgreementName"
        ] = None,
    ) -> "capo_direct_connect.types.confirm_customer_agreement_response.ConfirmCustomerAgreementResponse":
        """<p> The confirmation of the terms of agreement when creating the connection/link aggregation group (LAG). </p>

        Args:
            agreement_name: <p> The name of the customer agreement. </p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.confirm_customer_agreement_request.ConfirmCustomerAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.confirm_customer_agreement_response.ConfirmCustomerAgreementResponse"
        ]:
            import capo_direct_connect._operations.overture_service.confirm_customer_agreement

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.confirm_customer_agreement.async_confirm_customer_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.confirm_customer_agreement_request.ConfirmCustomerAgreementRequest = {}
        if agreement_name is not None:
            input_["agreement_name"] = agreement_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def confirm_private_virtual_interface(
        self,
        virtual_interface_id: "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        virtual_gateway_id: Optional[
            "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
        ] = None,
        direct_connect_gateway_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
    ) -> "capo_direct_connect.types.confirm_private_virtual_interface_response.ConfirmPrivateVirtualInterfaceResponse":
        """<p>Accepts ownership of a private virtual interface created by another Amazon Web Services account.</p> <p>After the virtual interface owner makes this call, the virtual interface is created and attached to the specified virtual private gateway or Direct Connect gateway, and is made available to handle traffic.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            virtual_gateway_id: <p>The ID of the virtual private gateway.</p>
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.confirm_private_virtual_interface_request.ConfirmPrivateVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.confirm_private_virtual_interface_response.ConfirmPrivateVirtualInterfaceResponse"
        ]:
            import capo_direct_connect._operations.overture_service.confirm_private_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.confirm_private_virtual_interface.async_confirm_private_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.confirm_private_virtual_interface_request.ConfirmPrivateVirtualInterfaceRequest = {
            "virtual_interface_id": virtual_interface_id
        }
        if virtual_gateway_id is not None:
            input_["virtual_gateway_id"] = virtual_gateway_id
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def confirm_public_virtual_interface(
        self,
        virtual_interface_id: "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.confirm_public_virtual_interface_response.ConfirmPublicVirtualInterfaceResponse":
        """<p>Accepts ownership of a public virtual interface created by another Amazon Web Services account.</p> <p>After the virtual interface owner makes this call, the specified virtual interface is created and made available to handle traffic.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.confirm_public_virtual_interface_request.ConfirmPublicVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.confirm_public_virtual_interface_response.ConfirmPublicVirtualInterfaceResponse"
        ]:
            import capo_direct_connect._operations.overture_service.confirm_public_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.confirm_public_virtual_interface.async_confirm_public_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.confirm_public_virtual_interface_request.ConfirmPublicVirtualInterfaceRequest = {
            "virtual_interface_id": virtual_interface_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def confirm_transit_virtual_interface(
        self,
        virtual_interface_id: "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        direct_connect_gateway_id: "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.confirm_transit_virtual_interface_response.ConfirmTransitVirtualInterfaceResponse":
        """<p>Accepts ownership of a transit virtual interface created by another Amazon Web Services account.</p> <p> After the owner of the transit virtual interface makes this call, the specified transit virtual interface is created and made available to handle traffic.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.confirm_transit_virtual_interface_request.ConfirmTransitVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.confirm_transit_virtual_interface_response.ConfirmTransitVirtualInterfaceResponse"
        ]:
            import capo_direct_connect._operations.overture_service.confirm_transit_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.confirm_transit_virtual_interface.async_confirm_transit_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.confirm_transit_virtual_interface_request.ConfirmTransitVirtualInterfaceRequest = {
            "virtual_interface_id": virtual_interface_id,
            "direct_connect_gateway_id": direct_connect_gateway_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bgp_peer(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        virtual_interface_id: Optional[
            "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        new_bgp_peer: Optional[
            "capo_direct_connect.types.new_bgp_peer.NewBGPPeer"
        ] = None,
    ) -> "capo_direct_connect.types.create_bgp_peer_response.CreateBGPPeerResponse":
        """<p>Creates a BGP peer on the specified virtual interface.</p> <p>You must create a BGP peer for the corresponding address family (IPv4/IPv6) in order to access Amazon Web Services resources that also use that address family.</p> <p>If logical redundancy is not supported by the connection, interconnect, or LAG, the BGP peer cannot be in the same address family as an existing BGP peer on the virtual interface.</p> <p>When creating a IPv6 BGP peer, omit the Amazon address and customer address. IPv6 addresses are automatically assigned from the Amazon pool of IPv6 addresses; you cannot specify custom IPv6 addresses.</p> <important> <p>If you let Amazon Web Services auto-assign IPv4 addresses, a /30 CIDR will be allocated from 169.254.0.0/16. Amazon Web Services does not recommend this option if you intend to use the customer router peer IP address as the source and destination for traffic. Instead you should use RFC 1918 or other addressing, and specify the address yourself. For more information about RFC 1918 see <a href="https://datatracker.ietf.org/doc/html/rfc1918"> Address Allocation for Private Internets</a>.</p> </important> <p>For a public virtual interface, the Autonomous System Number (ASN) must be private or already on the allow list for the virtual interface.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            new_bgp_peer: <p>Information about the BGP peer.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_bgp_peer_request.CreateBGPPeerRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.create_bgp_peer_response.CreateBGPPeerResponse"
        ]:
            import capo_direct_connect._operations.overture_service.create_bgp_peer

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_bgp_peer.async_create_bgp_peer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_bgp_peer_request.CreateBGPPeerRequest = {}
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
        if new_bgp_peer is not None:
            input_["new_bgp_peer"] = new_bgp_peer

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_connection(
        self,
        location: "capo_direct_connect.types.location_code.LocationCode",
        bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth",
        connection_name: "capo_direct_connect.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        lag_id: Optional["capo_direct_connect.types.lag_id.LagId"] = None,
        tags: Optional["capo_direct_connect.types.tag_list.TagList"] = None,
        provider_name: Optional[
            "capo_direct_connect.types.provider_name.ProviderName"
        ] = None,
        request_mac_sec: Optional[
            "capo_direct_connect.types.request_mac_sec.RequestMACSec"
        ] = None,
        billing_mode: Optional[
            "capo_direct_connect.types.request_billing_mode.RequestBillingMode"
        ] = None,
    ) -> "capo_direct_connect.types.connection.Connection":
        """<p>Creates a connection between a customer network and a specific Direct Connect location.</p> <p>A connection links your internal network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an Direct Connect router.</p> <p>To find the locations for your Region, use <a>DescribeLocations</a>.</p> <p>You can automatically add the new connection to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new connection is allocated on the same Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no connection is created.</p>

        Args:
            location: <p>The location of the connection.</p>
            bandwidth: <p>The bandwidth of the connection.</p>
            connection_name: <p>The name of the connection.</p>
            lag_id: <p>The ID of the LAG.</p>
            tags: <p>The tags to associate with the lag.</p>
            provider_name: <p>The name of the service provider associated with the requested connection.</p>
            request_mac_sec: <p>Indicates whether you want the connection to support MAC Security (MACsec).</p> <p>MAC Security (MACsec) is unavailable on hosted connections. For information about MAC Security (MACsec) prerequisites, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACSec.html">MAC Security in Direct Connect</a> in the <i>Direct Connect User Guide</i>.</p>
            billing_mode: <p>The billing mode for the connection.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_connection_request.CreateConnectionRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.connection.Connection"]:
            import capo_direct_connect._operations.overture_service.create_connection

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_connection.async_create_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_connection_request.CreateConnectionRequest = {
            "location": location,
            "bandwidth": bandwidth,
            "connection_name": connection_name,
        }
        if lag_id is not None:
            input_["lag_id"] = lag_id
        if tags is not None:
            input_["tags"] = tags
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if request_mac_sec is not None:
            input_["request_mac_sec"] = request_mac_sec
        if billing_mode is not None:
            input_["billing_mode"] = billing_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_direct_connect_gateway(
        self,
        direct_connect_gateway_name: "capo_direct_connect.types.direct_connect_gateway_name.DirectConnectGatewayName",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        tags: Optional["capo_direct_connect.types.tag_list.TagList"] = None,
        amazon_side_asn: Optional["capo_direct_connect.types.long_asn.LongAsn"] = None,
    ) -> "capo_direct_connect.types.create_direct_connect_gateway_result.CreateDirectConnectGatewayResult":
        """<p>Creates a Direct Connect gateway, which is an intermediate object that enables you to connect a set of virtual interfaces and virtual private gateways. A Direct Connect gateway is global and visible in any Amazon Web Services Region after it is created. The virtual interfaces and virtual private gateways that are connected through a Direct Connect gateway can be in different Amazon Web Services Regions. This enables you to connect to a VPC in any Region, regardless of the Region in which the virtual interfaces are located, and pass traffic between them.</p>

        Args:
            direct_connect_gateway_name: <p>The name of the Direct Connect gateway.</p>
            tags: <p>The key-value pair tags associated with the request.</p>
            amazon_side_asn: <p>The autonomous system number (ASN) for Border Gateway Protocol (BGP) to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294. The default is 64512.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_direct_connect_gateway_request.CreateDirectConnectGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.create_direct_connect_gateway_result.CreateDirectConnectGatewayResult"
        ]:
            import capo_direct_connect._operations.overture_service.create_direct_connect_gateway

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_direct_connect_gateway.async_create_direct_connect_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_direct_connect_gateway_request.CreateDirectConnectGatewayRequest = {
            "direct_connect_gateway_name": direct_connect_gateway_name
        }
        if tags is not None:
            input_["tags"] = tags
        if amazon_side_asn is not None:
            input_["amazon_side_asn"] = amazon_side_asn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_direct_connect_gateway_association(
        self,
        direct_connect_gateway_id: "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        gateway_id: Optional[
            "capo_direct_connect.types.gateway_id_to_associate.GatewayIdToAssociate"
        ] = None,
        add_allowed_prefixes_to_direct_connect_gateway: Optional[
            "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
        virtual_gateway_id: Optional[
            "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
        ] = None,
    ) -> "capo_direct_connect.types.create_direct_connect_gateway_association_result.CreateDirectConnectGatewayAssociationResult":
        """<p>Creates an association between a Direct Connect gateway and a virtual private gateway. The virtual private gateway must be attached to a VPC and must not be associated with another Direct Connect gateway.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            gateway_id: <p>The ID of the virtual private gateway or transit gateway.</p>
            add_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to advertise to the Direct Connect gateway</p> <p>This parameter is required when you create an association to a transit gateway.</p> <p>For information about how to set the prefixes, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-vgw.html#allowed-prefixes">Allowed Prefixes</a> in the <i>Direct Connect User Guide</i>.</p>
            virtual_gateway_id: <p>The ID of the virtual private gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_direct_connect_gateway_association_request.CreateDirectConnectGatewayAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.create_direct_connect_gateway_association_result.CreateDirectConnectGatewayAssociationResult"
        ]:
            import capo_direct_connect._operations.overture_service.create_direct_connect_gateway_association

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_direct_connect_gateway_association.async_create_direct_connect_gateway_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_direct_connect_gateway_association_request.CreateDirectConnectGatewayAssociationRequest = {
            "direct_connect_gateway_id": direct_connect_gateway_id
        }
        if gateway_id is not None:
            input_["gateway_id"] = gateway_id
        if add_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["add_allowed_prefixes_to_direct_connect_gateway"] = (
                add_allowed_prefixes_to_direct_connect_gateway
            )
        if virtual_gateway_id is not None:
            input_["virtual_gateway_id"] = virtual_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_direct_connect_gateway_association_proposal(
        self,
        direct_connect_gateway_id: "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        direct_connect_gateway_owner_account: "capo_direct_connect.types.owner_account.OwnerAccount",
        gateway_id: "capo_direct_connect.types.gateway_id_to_associate.GatewayIdToAssociate",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        add_allowed_prefixes_to_direct_connect_gateway: Optional[
            "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
        remove_allowed_prefixes_to_direct_connect_gateway: Optional[
            "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
    ) -> "capo_direct_connect.types.create_direct_connect_gateway_association_proposal_result.CreateDirectConnectGatewayAssociationProposalResult":
        """<p>Creates a proposal to associate the specified virtual private gateway or transit gateway with the specified Direct Connect gateway.</p> <p>You can associate a Direct Connect gateway and virtual private gateway or transit gateway that is owned by any Amazon Web Services account. </p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            direct_connect_gateway_owner_account: <p>The ID of the Amazon Web Services account that owns the Direct Connect gateway.</p>
            gateway_id: <p>The ID of the virtual private gateway or transit gateway.</p>
            add_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to advertise to the Direct Connect gateway.</p>
            remove_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_direct_connect_gateway_association_proposal_request.CreateDirectConnectGatewayAssociationProposalRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.create_direct_connect_gateway_association_proposal_result.CreateDirectConnectGatewayAssociationProposalResult"
        ]:
            import capo_direct_connect._operations.overture_service.create_direct_connect_gateway_association_proposal

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_direct_connect_gateway_association_proposal.async_create_direct_connect_gateway_association_proposal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_direct_connect_gateway_association_proposal_request.CreateDirectConnectGatewayAssociationProposalRequest = {
            "direct_connect_gateway_id": direct_connect_gateway_id,
            "direct_connect_gateway_owner_account": direct_connect_gateway_owner_account,
            "gateway_id": gateway_id,
        }
        if add_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["add_allowed_prefixes_to_direct_connect_gateway"] = (
                add_allowed_prefixes_to_direct_connect_gateway
            )
        if remove_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["remove_allowed_prefixes_to_direct_connect_gateway"] = (
                remove_allowed_prefixes_to_direct_connect_gateway
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_interconnect(
        self,
        interconnect_name: "capo_direct_connect.types.interconnect_name.InterconnectName",
        bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth",
        location: "capo_direct_connect.types.location_code.LocationCode",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        lag_id: Optional["capo_direct_connect.types.lag_id.LagId"] = None,
        tags: Optional["capo_direct_connect.types.tag_list.TagList"] = None,
        provider_name: Optional[
            "capo_direct_connect.types.provider_name.ProviderName"
        ] = None,
        request_mac_sec: Optional[
            "capo_direct_connect.types.request_mac_sec.RequestMACSec"
        ] = None,
    ) -> "capo_direct_connect.types.interconnect.Interconnect":
        """<p>Creates an interconnect between an Direct Connect Partner's network and a specific Direct Connect location.</p> <p>An interconnect is a connection that is capable of hosting other connections. The Direct Connect Partner can use an interconnect to provide Direct Connect hosted connections to customers through their own network services. Like a standard connection, an interconnect links the partner's network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end is connected to the partner's router, the other to an Direct Connect router.</p> <p>You can automatically add the new interconnect to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new interconnect is allocated on the same Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no interconnect is created.</p> <p>For each end customer, the Direct Connect Partner provisions a connection on their interconnect by calling <a>AllocateHostedConnection</a>. The end customer can then connect to Amazon Web Services resources by creating a virtual interface on their connection, using the VLAN assigned to them by the Direct Connect Partner.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            interconnect_name: <p>The name of the interconnect.</p>
            bandwidth: <p>The port bandwidth, in Gbps. The possible values are 1, 10, and 100.</p>
            location: <p>The location of the interconnect.</p>
            lag_id: <p>The ID of the LAG.</p>
            tags: <p>The tags to associate with the interconnect.</p>
            provider_name: <p>The name of the service provider associated with the interconnect.</p>
            request_mac_sec: <p>Indicates whether you want the interconnect to support MAC Security (MACsec).</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_interconnect_request.CreateInterconnectRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.interconnect.Interconnect"
        ]:
            import capo_direct_connect._operations.overture_service.create_interconnect

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_interconnect.async_create_interconnect(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_interconnect_request.CreateInterconnectRequest = {
            "interconnect_name": interconnect_name,
            "bandwidth": bandwidth,
            "location": location,
        }
        if lag_id is not None:
            input_["lag_id"] = lag_id
        if tags is not None:
            input_["tags"] = tags
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if request_mac_sec is not None:
            input_["request_mac_sec"] = request_mac_sec

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_lag(
        self,
        number_of_connections: "capo_direct_connect.types.count.Count",
        location: "capo_direct_connect.types.location_code.LocationCode",
        connections_bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth",
        lag_name: "capo_direct_connect.types.lag_name.LagName",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        connection_id: Optional[
            "capo_direct_connect.types.connection_id.ConnectionId"
        ] = None,
        tags: Optional["capo_direct_connect.types.tag_list.TagList"] = None,
        child_connection_tags: Optional[
            "capo_direct_connect.types.tag_list.TagList"
        ] = None,
        provider_name: Optional[
            "capo_direct_connect.types.provider_name.ProviderName"
        ] = None,
        request_mac_sec: Optional[
            "capo_direct_connect.types.request_mac_sec.RequestMACSec"
        ] = None,
        billing_mode: Optional[
            "capo_direct_connect.types.request_billing_mode.RequestBillingMode"
        ] = None,
    ) -> "capo_direct_connect.types.lag.Lag":
        """<p>Creates a link aggregation group (LAG) with the specified number of bundled physical dedicated connections between the customer network and a specific Direct Connect location. A LAG is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple interfaces, enabling you to treat them as a single interface.</p> <p>All connections in a LAG must use the same bandwidth (either 1Gbps, 10Gbps, 100Gbps, or 400Gbps) and must terminate at the same Direct Connect endpoint.</p> <p>You can have up to 10 dedicated connections per location. Regardless of this limit, if you request more connections for the LAG than Direct Connect can allocate on a single endpoint, no LAG is created..</p> <p>You can specify an existing physical dedicated connection or interconnect to include in the LAG (which counts towards the total number of connections). Doing so interrupts the current physical dedicated connection, and re-establishes them as a member of the LAG. The LAG will be created on the same Direct Connect endpoint to which the dedicated connection terminates. Any virtual interfaces associated with the dedicated connection are automatically disassociated and re-associated with the LAG. The connection ID does not change.</p> <p>If the Amazon Web Services account used to create a LAG is a registered Direct Connect Partner, the LAG is automatically enabled to host sub-connections. For a LAG owned by a partner, any associated virtual interfaces cannot be directly configured.</p>

        Args:
            number_of_connections: <p>The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1Gbps or 10Gbps, or two when the port speed is 100Gbps or 400Gbps.</p>
            location: <p>The location for the LAG.</p>
            connections_bandwidth: <p>The bandwidth of the individual physical dedicated connections bundled by the LAG. The possible values are 1Gbps,10Gbps, 100Gbps, and 400Gbps. </p>
            lag_name: <p>The name of the LAG.</p>
            connection_id: <p>The ID of an existing dedicated connection to migrate to the LAG.</p>
            tags: <p>The tags to associate with the LAG.</p>
            child_connection_tags: <p>The tags to associate with the automtically created LAGs.</p>
            provider_name: <p>The name of the service provider associated with the LAG.</p>
            request_mac_sec: <p>Indicates whether the connection will support MAC Security (MACsec).</p> <note> <p>All connections in the LAG must be capable of supporting MAC Security (MACsec). For information about MAC Security (MACsec) prerequisties, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-prerequisites">MACsec prerequisties</a> in the <i>Direct Connect User Guide</i>.</p> </note>
            billing_mode: <p>The billing mode for the LAG.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_lag_request.CreateLagRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.lag.Lag"]:
            import capo_direct_connect._operations.overture_service.create_lag

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_lag.async_create_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_lag_request.CreateLagRequest = {
            "number_of_connections": number_of_connections,
            "location": location,
            "connections_bandwidth": connections_bandwidth,
            "lag_name": lag_name,
        }
        if connection_id is not None:
            input_["connection_id"] = connection_id
        if tags is not None:
            input_["tags"] = tags
        if child_connection_tags is not None:
            input_["child_connection_tags"] = child_connection_tags
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if request_mac_sec is not None:
            input_["request_mac_sec"] = request_mac_sec
        if billing_mode is not None:
            input_["billing_mode"] = billing_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_private_virtual_interface(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        new_private_virtual_interface: "capo_direct_connect.types.new_private_virtual_interface.NewPrivateVirtualInterface",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Creates a private virtual interface. A virtual interface is the VLAN that transports Direct Connect traffic. A private virtual interface can be connected to either a Direct Connect gateway or a Virtual Private Gateway (VGW). Connecting the private virtual interface to a Direct Connect gateway enables the possibility for connecting to multiple VPCs, including VPCs in different Amazon Web Services Regions. Connecting the private virtual interface to a VGW only provides access to a single VPC within the same Region.</p> <p>Setting the MTU of a virtual interface to 8500 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call <a>DescribeConnections</a>. To check whether your virtual interface supports jumbo frames, call <a>DescribeVirtualInterfaces</a>.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            new_private_virtual_interface: <p>Information about the private virtual interface.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.limit_exceeded_exception.LimitExceededException: <p>The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_private_virtual_interface_request.CreatePrivateVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import capo_direct_connect._operations.overture_service.create_private_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_private_virtual_interface.async_create_private_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_private_virtual_interface_request.CreatePrivateVirtualInterfaceRequest = {
            "connection_id": connection_id,
            "new_private_virtual_interface": new_private_virtual_interface,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_public_virtual_interface(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        new_public_virtual_interface: "capo_direct_connect.types.new_public_virtual_interface.NewPublicVirtualInterface",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Creates a public virtual interface. A virtual interface is the VLAN that transports Direct Connect traffic. A public virtual interface supports sending traffic to public services of Amazon Web Services such as Amazon S3.</p> <p>When creating an IPv6 public virtual interface (<code>addressFamily</code> is <code>ipv6</code>), leave the <code>customer</code> and <code>amazon</code> address fields blank to use auto-assigned IPv6 space. Custom IPv6 addresses are not supported.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            new_public_virtual_interface: <p>Information about the public virtual interface.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.limit_exceeded_exception.LimitExceededException: <p>The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_public_virtual_interface_request.CreatePublicVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import capo_direct_connect._operations.overture_service.create_public_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_public_virtual_interface.async_create_public_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_public_virtual_interface_request.CreatePublicVirtualInterfaceRequest = {
            "connection_id": connection_id,
            "new_public_virtual_interface": new_public_virtual_interface,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resiliency_group(
        self,
        resiliency_group_name: "capo_direct_connect.types.resiliency_group_name.ResiliencyGroupName",
        intended_resiliency_model: "capo_direct_connect.types.resiliency_model.ResiliencyModel",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        client_token: Optional[
            "capo_direct_connect.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_direct_connect.types.tag_list.TagList"] = None,
    ) -> "capo_direct_connect.types.create_resiliency_group_result.CreateResiliencyGroupResult":
        """<p>Creates a resiliency group. A resiliency group lets you group Direct Connect connections together and manage them as a single unit to meet a target resiliency model.</p>

        Args:
            resiliency_group_name: <p>The name of the resiliency group.</p>
            intended_resiliency_model: <p>The resiliency model that the resiliency group is intended to meet. The valid values are <code>maximum-resiliency</code>, <code>high-resiliency</code>, and <code>basic-resiliency</code>.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>The tags to associate with the resiliency group.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.limit_exceeded_exception.LimitExceededException: <p>The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_resiliency_group_request.CreateResiliencyGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.create_resiliency_group_result.CreateResiliencyGroupResult"
        ]:
            import capo_direct_connect._operations.overture_service.create_resiliency_group

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_resiliency_group.async_create_resiliency_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_resiliency_group_request.CreateResiliencyGroupRequest = {
            "resiliency_group_name": resiliency_group_name,
            "intended_resiliency_model": intended_resiliency_model,
        }
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_transit_virtual_interface(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        new_transit_virtual_interface: "capo_direct_connect.types.new_transit_virtual_interface.NewTransitVirtualInterface",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.create_transit_virtual_interface_result.CreateTransitVirtualInterfaceResult":
        """<p>Creates a transit virtual interface. A transit virtual interface should be used to access one or more transit gateways associated with Direct Connect gateways. A transit virtual interface enables the connection of multiple VPCs attached to a transit gateway to a Direct Connect gateway.</p> <important> <p>If you associate your transit gateway with one or more Direct Connect gateways, the Autonomous System Number (ASN) used by the transit gateway and the Direct Connect gateway must be different. For example, if you use the default ASN 64512 for both your the transit gateway and Direct Connect gateway, the association request fails.</p> </important> <p>A jumbo MTU value must be either 1500 or 8500. No other values will be accepted. Setting the MTU of a virtual interface to 8500 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call <a>DescribeConnections</a>. To check whether your virtual interface supports jumbo frames, call <a>DescribeVirtualInterfaces</a>.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            new_transit_virtual_interface: <p>Information about the transit virtual interface.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.limit_exceeded_exception.LimitExceededException: <p>The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.create_transit_virtual_interface_request.CreateTransitVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.create_transit_virtual_interface_result.CreateTransitVirtualInterfaceResult"
        ]:
            import capo_direct_connect._operations.overture_service.create_transit_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.create_transit_virtual_interface.async_create_transit_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.create_transit_virtual_interface_request.CreateTransitVirtualInterfaceRequest = {
            "connection_id": connection_id,
            "new_transit_virtual_interface": new_transit_virtual_interface,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bgp_peer(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        virtual_interface_id: Optional[
            "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        asn: Optional["capo_direct_connect.types.asn.ASN"] = None,
        asn_long: Optional["capo_direct_connect.types.long_asn.LongAsn"] = None,
        customer_address: Optional[
            "capo_direct_connect.types.customer_address.CustomerAddress"
        ] = None,
        bgp_peer_id: Optional["capo_direct_connect.types.bgp_peer_id.BGPPeerId"] = None,
    ) -> "capo_direct_connect.types.delete_bgp_peer_response.DeleteBGPPeerResponse":
        """<p>Deletes the specified BGP peer on the specified virtual interface with the specified customer address and ASN.</p> <p>You cannot delete the last BGP peer from a virtual interface.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            asn: <p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>. </p> </li> <li> <p>If you enter a 4-byte ASN for the <code>asn</code> parameter, the API returns an error. </p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> </ul>
            asn_long: <p>The long ASN for the BGP peer to be deleted from a Direct Connect virtual interface. The valid range is from 1 to 4294967294 for BGP configuration. </p> <p>Note the following limitations when using <code>asnLong</code>:</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p> <code>asnLong</code> accepts any valid ASN value, regardless if it's 2-byte or 4-byte. </p> </li> <li> <p>When using a 4-byte <code>asnLong</code>, the API response returns <code>0</code> for the legacy <code>asn</code> attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.</p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul>
            customer_address: <p>The IP address assigned to the customer interface.</p>
            bgp_peer_id: <p>The ID of the BGP peer.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.delete_bgp_peer_request.DeleteBGPPeerRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.delete_bgp_peer_response.DeleteBGPPeerResponse"
        ]:
            import capo_direct_connect._operations.overture_service.delete_bgp_peer

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.delete_bgp_peer.async_delete_bgp_peer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.delete_bgp_peer_request.DeleteBGPPeerRequest = {}
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
        if asn is not None:
            input_["asn"] = asn
        if asn_long is not None:
            input_["asn_long"] = asn_long
        if customer_address is not None:
            input_["customer_address"] = customer_address
        if bgp_peer_id is not None:
            input_["bgp_peer_id"] = bgp_peer_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connection(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.connection.Connection":
        """<p>Deletes the specified connection.</p> <p>Deleting a connection only stops the Direct Connect port hour and data transfer charges. If you are partnering with any third parties to connect with the Direct Connect location, you must cancel your service with them separately.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.connection.Connection"]:
            import capo_direct_connect._operations.overture_service.delete_connection

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.delete_connection_request.DeleteConnectionRequest = {
            "connection_id": connection_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_direct_connect_gateway(
        self,
        direct_connect_gateway_id: "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.delete_direct_connect_gateway_result.DeleteDirectConnectGatewayResult":
        """<p>Deletes the specified Direct Connect gateway. You must first delete all virtual interfaces that are attached to the Direct Connect gateway and disassociate all virtual private gateways associated with the Direct Connect gateway.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.delete_direct_connect_gateway_request.DeleteDirectConnectGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.delete_direct_connect_gateway_result.DeleteDirectConnectGatewayResult"
        ]:
            import capo_direct_connect._operations.overture_service.delete_direct_connect_gateway

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.delete_direct_connect_gateway.async_delete_direct_connect_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.delete_direct_connect_gateway_request.DeleteDirectConnectGatewayRequest = {
            "direct_connect_gateway_id": direct_connect_gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_direct_connect_gateway_association(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        association_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
        ] = None,
        direct_connect_gateway_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        virtual_gateway_id: Optional[
            "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
        ] = None,
    ) -> "capo_direct_connect.types.delete_direct_connect_gateway_association_result.DeleteDirectConnectGatewayAssociationResult":
        """<p>Deletes the association between the specified Direct Connect gateway and virtual private gateway.</p> <p>We recommend that you specify the <code>associationID</code> to delete the association. Alternatively, if you own virtual gateway and a Direct Connect gateway association, you can specify the <code>virtualGatewayId</code> and <code>directConnectGatewayId</code> to delete an association.</p>

        Args:
            association_id: <p>The ID of the Direct Connect gateway association.</p>
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            virtual_gateway_id: <p>The ID of the virtual private gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.delete_direct_connect_gateway_association_request.DeleteDirectConnectGatewayAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.delete_direct_connect_gateway_association_result.DeleteDirectConnectGatewayAssociationResult"
        ]:
            import capo_direct_connect._operations.overture_service.delete_direct_connect_gateway_association

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.delete_direct_connect_gateway_association.async_delete_direct_connect_gateway_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.delete_direct_connect_gateway_association_request.DeleteDirectConnectGatewayAssociationRequest = {}
        if association_id is not None:
            input_["association_id"] = association_id
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        if virtual_gateway_id is not None:
            input_["virtual_gateway_id"] = virtual_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_direct_connect_gateway_association_proposal(
        self,
        proposal_id: "capo_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.delete_direct_connect_gateway_association_proposal_result.DeleteDirectConnectGatewayAssociationProposalResult":
        """<p>Deletes the association proposal request between the specified Direct Connect gateway and virtual private gateway or transit gateway.</p>

        Args:
            proposal_id: <p>The ID of the proposal.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.delete_direct_connect_gateway_association_proposal_request.DeleteDirectConnectGatewayAssociationProposalRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.delete_direct_connect_gateway_association_proposal_result.DeleteDirectConnectGatewayAssociationProposalResult"
        ]:
            import capo_direct_connect._operations.overture_service.delete_direct_connect_gateway_association_proposal

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.delete_direct_connect_gateway_association_proposal.async_delete_direct_connect_gateway_association_proposal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.delete_direct_connect_gateway_association_proposal_request.DeleteDirectConnectGatewayAssociationProposalRequest = {
            "proposal_id": proposal_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_interconnect(
        self,
        interconnect_id: "capo_direct_connect.types.interconnect_id.InterconnectId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.delete_interconnect_response.DeleteInterconnectResponse":
        """<p>Deletes the specified interconnect.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            interconnect_id: <p>The ID of the interconnect.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.delete_interconnect_request.DeleteInterconnectRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.delete_interconnect_response.DeleteInterconnectResponse"
        ]:
            import capo_direct_connect._operations.overture_service.delete_interconnect

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.delete_interconnect.async_delete_interconnect(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.delete_interconnect_request.DeleteInterconnectRequest = {
            "interconnect_id": interconnect_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_lag(
        self,
        lag_id: "capo_direct_connect.types.lag_id.LagId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.lag.Lag":
        """<p>Deletes the specified link aggregation group (LAG). You cannot delete a LAG if it has active virtual interfaces or hosted connections.</p>

        Args:
            lag_id: <p>The ID of the LAG.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.delete_lag_request.DeleteLagRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.lag.Lag"]:
            import capo_direct_connect._operations.overture_service.delete_lag

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.delete_lag.async_delete_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.delete_lag_request.DeleteLagRequest = {
            "lag_id": lag_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resiliency_group(
        self,
        resiliency_group_id: "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.delete_resiliency_group_result.DeleteResiliencyGroupResult":
        """<p>Deletes the specified resiliency group. Deletion is asynchronous: the resiliency group transitions through the <code>deleting</code> state before it reaches the <code>deleted</code> state. The response returns the resiliency group so you can observe its current state without a subsequent <a>GetResiliencyGroup</a> call.</p>

        Args:
            resiliency_group_id: <p>The ID of the resiliency group.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.delete_resiliency_group_request.DeleteResiliencyGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.delete_resiliency_group_result.DeleteResiliencyGroupResult"
        ]:
            import capo_direct_connect._operations.overture_service.delete_resiliency_group

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.delete_resiliency_group.async_delete_resiliency_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.delete_resiliency_group_request.DeleteResiliencyGroupRequest = {
            "resiliency_group_id": resiliency_group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_virtual_interface(
        self,
        virtual_interface_id: "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.delete_virtual_interface_response.DeleteVirtualInterfaceResponse":
        """<p>Deletes a virtual interface.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.delete_virtual_interface_request.DeleteVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.delete_virtual_interface_response.DeleteVirtualInterfaceResponse"
        ]:
            import capo_direct_connect._operations.overture_service.delete_virtual_interface

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.delete_virtual_interface.async_delete_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.delete_virtual_interface_request.DeleteVirtualInterfaceRequest = {
            "virtual_interface_id": virtual_interface_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_connection_loa(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        provider_name: Optional[
            "capo_direct_connect.types.provider_name.ProviderName"
        ] = None,
        loa_content_type: Optional[
            "capo_direct_connect.types.loa_content_type.LoaContentType"
        ] = None,
    ) -> "capo_direct_connect.types.describe_connection_loa_response.DescribeConnectionLoaResponse":
        """<note> <p>Deprecated. Use <a>DescribeLoa</a> instead.</p> </note> <p>Gets the LOA-CFA for a connection.</p> <p>The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that your APN partner or service provider uses when establishing your cross connect to Amazon Web Services at the colocation facility. For more information, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html">Requesting Cross Connects at Direct Connect Locations</a> in the <i>Direct Connect User Guide</i>.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            provider_name: <p>The name of the APN partner or service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.</p>
            loa_content_type: <p>The standard media type for the LOA-CFA document. The only supported value is application/pdf.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_connection_loa_request.DescribeConnectionLoaRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.describe_connection_loa_response.DescribeConnectionLoaResponse"
        ]:
            import capo_direct_connect._operations.overture_service.describe_connection_loa

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_connection_loa.async_describe_connection_loa(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_connection_loa_request.DescribeConnectionLoaRequest = {
            "connection_id": connection_id
        }
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if loa_content_type is not None:
            input_["loa_content_type"] = loa_content_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_connections(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        connection_id: Optional[
            "capo_direct_connect.types.connection_id.ConnectionId"
        ] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.connections.Connections":
        """<p>Displays the specified connection or all connections in this Region.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_connections_request.DescribeConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.connections.Connections"
        ]:
            import capo_direct_connect._operations.overture_service.describe_connections

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_connections.async_describe_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_connections_request.DescribeConnectionsRequest = {}
        if connection_id is not None:
            input_["connection_id"] = connection_id
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

    async def describe_connections_on_interconnect(
        self,
        interconnect_id: "capo_direct_connect.types.interconnect_id.InterconnectId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.connections.Connections":
        """<note> <p>Deprecated. Use <a>DescribeHostedConnections</a> instead.</p> </note> <p>Lists the connections that have been provisioned on the specified interconnect.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            interconnect_id: <p>The ID of the interconnect.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_connections_on_interconnect_request.DescribeConnectionsOnInterconnectRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.connections.Connections"
        ]:
            import capo_direct_connect._operations.overture_service.describe_connections_on_interconnect

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_connections_on_interconnect.async_describe_connections_on_interconnect(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_connections_on_interconnect_request.DescribeConnectionsOnInterconnectRequest = {
            "interconnect_id": interconnect_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_customer_metadata(
        self, *, config_overrides: Optional[AsyncDirectConnectClientConfig] = None
    ) -> "capo_direct_connect.types.describe_customer_metadata_response.DescribeCustomerMetadataResponse":
        """<p>Get and view a list of customer agreements, along with their signed status and whether the customer is an NNIPartner, NNIPartnerV2, or a nonPartner. </p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.describe_customer_metadata_response.DescribeCustomerMetadataResponse"
        ]:
            import capo_direct_connect._operations.overture_service.describe_customer_metadata

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_customer_metadata.async_describe_customer_metadata(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_direct_connect_gateway_association_proposals(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        direct_connect_gateway_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        proposal_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId"
        ] = None,
        associated_gateway_id: Optional[
            "capo_direct_connect.types.associated_gateway_id.AssociatedGatewayId"
        ] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.describe_direct_connect_gateway_association_proposals_result.DescribeDirectConnectGatewayAssociationProposalsResult":
        """<p>Describes one or more association proposals for connection between a virtual private gateway or transit gateway and a Direct Connect gateway. </p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            proposal_id: <p>The ID of the proposal.</p>
            associated_gateway_id: <p>The ID of the associated gateway.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_direct_connect_gateway_association_proposals_request.DescribeDirectConnectGatewayAssociationProposalsRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.describe_direct_connect_gateway_association_proposals_result.DescribeDirectConnectGatewayAssociationProposalsResult"
        ]:
            import capo_direct_connect._operations.overture_service.describe_direct_connect_gateway_association_proposals

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_direct_connect_gateway_association_proposals.async_describe_direct_connect_gateway_association_proposals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_direct_connect_gateway_association_proposals_request.DescribeDirectConnectGatewayAssociationProposalsRequest = {}
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        if proposal_id is not None:
            input_["proposal_id"] = proposal_id
        if associated_gateway_id is not None:
            input_["associated_gateway_id"] = associated_gateway_id
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

    async def describe_direct_connect_gateway_associations(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        association_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
        ] = None,
        associated_gateway_id: Optional[
            "capo_direct_connect.types.associated_gateway_id.AssociatedGatewayId"
        ] = None,
        direct_connect_gateway_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
        virtual_gateway_id: Optional[
            "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
        ] = None,
    ) -> "capo_direct_connect.types.describe_direct_connect_gateway_associations_result.DescribeDirectConnectGatewayAssociationsResult":
        """<p>Lists the associations between your Direct Connect gateways and virtual private gateways and transit gateways. You must specify one of the following:</p> <ul> <li> <p>A Direct Connect gateway</p> <p>The response contains all virtual private gateways and transit gateways associated with the Direct Connect gateway.</p> </li> <li> <p>A virtual private gateway</p> <p>The response contains the Direct Connect gateway.</p> </li> <li> <p>A transit gateway</p> <p>The response contains the Direct Connect gateway.</p> </li> <li> <p>A Direct Connect gateway and a virtual private gateway</p> <p>The response contains the association between the Direct Connect gateway and virtual private gateway.</p> </li> <li> <p>A Direct Connect gateway and a transit gateway</p> <p>The response contains the association between the Direct Connect gateway and transit gateway.</p> </li> <li> <p>A Direct Connect gateway and a virtual private gateway</p> <p>The response contains the association between the Direct Connect gateway and virtual private gateway.</p> </li> <li> <p>A Direct Connect gateway association to a Cloud WAN core network</p> <p>The response contains the Cloud WAN core network ID that the Direct Connect gateway is associated to.</p> </li> </ul>

        Args:
            association_id: <p>The ID of the Direct Connect gateway association.</p>
            associated_gateway_id: <p>The ID of the associated gateway.</p>
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token provided in the previous call to retrieve the next page.</p>
            virtual_gateway_id: <p>The ID of the virtual private gateway or transit gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_direct_connect_gateway_associations_request.DescribeDirectConnectGatewayAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.describe_direct_connect_gateway_associations_result.DescribeDirectConnectGatewayAssociationsResult"
        ]:
            import capo_direct_connect._operations.overture_service.describe_direct_connect_gateway_associations

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_direct_connect_gateway_associations.async_describe_direct_connect_gateway_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_direct_connect_gateway_associations_request.DescribeDirectConnectGatewayAssociationsRequest = {}
        if association_id is not None:
            input_["association_id"] = association_id
        if associated_gateway_id is not None:
            input_["associated_gateway_id"] = associated_gateway_id
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if virtual_gateway_id is not None:
            input_["virtual_gateway_id"] = virtual_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_direct_connect_gateway_attachments(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        direct_connect_gateway_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        virtual_interface_id: Optional[
            "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.describe_direct_connect_gateway_attachments_result.DescribeDirectConnectGatewayAttachmentsResult":
        """<p>Lists the attachments between your Direct Connect gateways and virtual interfaces. You must specify a Direct Connect gateway, a virtual interface, or both. If you specify a Direct Connect gateway, the response contains all virtual interfaces attached to the Direct Connect gateway. If you specify a virtual interface, the response contains all Direct Connect gateways attached to the virtual interface. If you specify both, the response contains the attachment between the Direct Connect gateway and the virtual interface.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token provided in the previous call to retrieve the next page.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_direct_connect_gateway_attachments_request.DescribeDirectConnectGatewayAttachmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.describe_direct_connect_gateway_attachments_result.DescribeDirectConnectGatewayAttachmentsResult"
        ]:
            import capo_direct_connect._operations.overture_service.describe_direct_connect_gateway_attachments

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_direct_connect_gateway_attachments.async_describe_direct_connect_gateway_attachments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_direct_connect_gateway_attachments_request.DescribeDirectConnectGatewayAttachmentsRequest = {}
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
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

    async def describe_direct_connect_gateways(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        direct_connect_gateway_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.describe_direct_connect_gateways_result.DescribeDirectConnectGatewaysResult":
        """<p>Lists all your Direct Connect gateways or only the specified Direct Connect gateway. Deleted Direct Connect gateways are not returned.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token provided in the previous call to retrieve the next page.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_direct_connect_gateways_request.DescribeDirectConnectGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.describe_direct_connect_gateways_result.DescribeDirectConnectGatewaysResult"
        ]:
            import capo_direct_connect._operations.overture_service.describe_direct_connect_gateways

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_direct_connect_gateways.async_describe_direct_connect_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_direct_connect_gateways_request.DescribeDirectConnectGatewaysRequest = {}
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
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

    async def describe_hosted_connections(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.connections.Connections":
        """<p>Lists the hosted connections that have been provisioned on the specified interconnect or link aggregation group (LAG).</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            connection_id: <p>The ID of the interconnect or LAG.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_hosted_connections_request.DescribeHostedConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.connections.Connections"
        ]:
            import capo_direct_connect._operations.overture_service.describe_hosted_connections

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_hosted_connections.async_describe_hosted_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_hosted_connections_request.DescribeHostedConnectionsRequest = {
            "connection_id": connection_id
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

    async def describe_interconnect_loa(
        self,
        interconnect_id: "capo_direct_connect.types.interconnect_id.InterconnectId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        provider_name: Optional[
            "capo_direct_connect.types.provider_name.ProviderName"
        ] = None,
        loa_content_type: Optional[
            "capo_direct_connect.types.loa_content_type.LoaContentType"
        ] = None,
    ) -> "capo_direct_connect.types.describe_interconnect_loa_response.DescribeInterconnectLoaResponse":
        """<note> <p>Deprecated. Use <a>DescribeLoa</a> instead.</p> </note> <p>Gets the LOA-CFA for the specified interconnect.</p> <p>The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to Amazon Web Services at the colocation facility. For more information, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html">Requesting Cross Connects at Direct Connect Locations</a> in the <i>Direct Connect User Guide</i>.</p>

        Args:
            interconnect_id: <p>The ID of the interconnect.</p>
            provider_name: <p>The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.</p>
            loa_content_type: <p>The standard media type for the LOA-CFA document. The only supported value is application/pdf.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_interconnect_loa_request.DescribeInterconnectLoaRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.describe_interconnect_loa_response.DescribeInterconnectLoaResponse"
        ]:
            import capo_direct_connect._operations.overture_service.describe_interconnect_loa

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_interconnect_loa.async_describe_interconnect_loa(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_interconnect_loa_request.DescribeInterconnectLoaRequest = {
            "interconnect_id": interconnect_id
        }
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if loa_content_type is not None:
            input_["loa_content_type"] = loa_content_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_interconnects(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        interconnect_id: Optional[
            "capo_direct_connect.types.interconnect_id.InterconnectId"
        ] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.interconnects.Interconnects":
        """<p>Lists the interconnects owned by the Amazon Web Services account or only the specified interconnect.</p>

        Args:
            interconnect_id: <p>The ID of the interconnect.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_interconnects_request.DescribeInterconnectsRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.interconnects.Interconnects"
        ]:
            import capo_direct_connect._operations.overture_service.describe_interconnects

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_interconnects.async_describe_interconnects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_interconnects_request.DescribeInterconnectsRequest = {}
        if interconnect_id is not None:
            input_["interconnect_id"] = interconnect_id
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

    async def describe_lags(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        lag_id: Optional["capo_direct_connect.types.lag_id.LagId"] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.lags.Lags":
        """<p>Describes all your link aggregation groups (LAG) or the specified LAG.</p>

        Args:
            lag_id: <p>The ID of the LAG.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_lags_request.DescribeLagsRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.lags.Lags"]:
            import capo_direct_connect._operations.overture_service.describe_lags

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_lags.async_describe_lags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_lags_request.DescribeLagsRequest = {}
        if lag_id is not None:
            input_["lag_id"] = lag_id
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

    async def describe_loa(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        provider_name: Optional[
            "capo_direct_connect.types.provider_name.ProviderName"
        ] = None,
        loa_content_type: Optional[
            "capo_direct_connect.types.loa_content_type.LoaContentType"
        ] = None,
    ) -> "capo_direct_connect.types.loa.Loa":
        """<p>Gets the LOA-CFA for a connection, interconnect, or link aggregation group (LAG).</p> <p>The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to Amazon Web Services at the colocation facility. For more information, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html">Requesting Cross Connects at Direct Connect Locations</a> in the <i>Direct Connect User Guide</i>.</p>

        Args:
            connection_id: <p>The ID of a connection, LAG, or interconnect.</p>
            provider_name: <p>The name of the service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.</p>
            loa_content_type: <p>The standard media type for the LOA-CFA document. The only supported value is application/pdf.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_loa_request.DescribeLoaRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.loa.Loa"]:
            import capo_direct_connect._operations.overture_service.describe_loa

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_loa.async_describe_loa(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_loa_request.DescribeLoaRequest = {
            "connection_id": connection_id
        }
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if loa_content_type is not None:
            input_["loa_content_type"] = loa_content_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_locations(
        self, *, config_overrides: Optional[AsyncDirectConnectClientConfig] = None
    ) -> "capo_direct_connect.types.locations.Locations":
        """<p>Lists the Direct Connect locations in the current Amazon Web Services Region. These are the locations that can be selected when calling <a>CreateConnection</a> or <a>CreateInterconnect</a>.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.locations.Locations"]:
            import capo_direct_connect._operations.overture_service.describe_locations

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_locations.async_describe_locations(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_router_configuration(
        self,
        virtual_interface_id: "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        router_type_identifier: Optional[
            "capo_direct_connect.types.router_type_identifier.RouterTypeIdentifier"
        ] = None,
    ) -> "capo_direct_connect.types.describe_router_configuration_response.DescribeRouterConfigurationResponse":
        """<p> Details about the router. </p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            router_type_identifier: <p>Identifies the router by a combination of vendor, platform, and software version. For example, <code>CiscoSystemsInc-2900SeriesRouters-IOS124</code>.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_router_configuration_request.DescribeRouterConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.describe_router_configuration_response.DescribeRouterConfigurationResponse"
        ]:
            import capo_direct_connect._operations.overture_service.describe_router_configuration

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_router_configuration.async_describe_router_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_router_configuration_request.DescribeRouterConfigurationRequest = {
            "virtual_interface_id": virtual_interface_id
        }
        if router_type_identifier is not None:
            input_["router_type_identifier"] = router_type_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_tags(
        self,
        resource_arns: "capo_direct_connect.types.resource_arn_list.ResourceArnList",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.describe_tags_response.DescribeTagsResponse":
        """<p>Describes the tags associated with the specified Direct Connect resources.</p>

        Args:
            resource_arns: <p>The Amazon Resource Names (ARNs) of the resources.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_tags_request.DescribeTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.describe_tags_response.DescribeTagsResponse"
        ]:
            import capo_direct_connect._operations.overture_service.describe_tags

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_tags.async_describe_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_tags_request.DescribeTagsRequest = {
            "resource_arns": resource_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_virtual_gateways(
        self, *, config_overrides: Optional[AsyncDirectConnectClientConfig] = None
    ) -> "capo_direct_connect.types.virtual_gateways.VirtualGateways":
        """<note> <p>Deprecated. Use <code>DescribeVpnGateways</code> instead. See <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html">DescribeVPNGateways</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p> </note> <p>Lists the virtual private gateways owned by the Amazon Web Services account.</p> <p>You can create one or more Direct Connect private virtual interfaces linked to a virtual private gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.virtual_gateways.VirtualGateways"
        ]:
            import capo_direct_connect._operations.overture_service.describe_virtual_gateways

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_virtual_gateways.async_describe_virtual_gateways(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_virtual_interfaces(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        connection_id: Optional[
            "capo_direct_connect.types.connection_id.ConnectionId"
        ] = None,
        virtual_interface_id: Optional[
            "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.virtual_interfaces.VirtualInterfaces":
        """<p>Displays all virtual interfaces for an Amazon Web Services account. Virtual interfaces deleted fewer than 15 minutes before you make the request are also returned. If you specify a connection ID, only the virtual interfaces associated with the connection are returned. If you specify a virtual interface ID, then only a single virtual interface is returned.</p> <p>A virtual interface (VLAN) transmits the traffic between the Direct Connect location and the customer network.</p> <ul> <li> <p>If you're using an <code>asn</code>, the response includes the ASN value in both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> <li> <p>If you're using <code>asnLong</code>, the response returns a value of <code>0</code> (zero) for the <code>asn</code> attribute because it exceeds the highest ASN value of 2,147,483,647 that it can support</p> </li> </ul>

        Args:
            connection_id: <p>The ID of the connection.</p>
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.describe_virtual_interfaces_request.DescribeVirtualInterfacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.virtual_interfaces.VirtualInterfaces"
        ]:
            import capo_direct_connect._operations.overture_service.describe_virtual_interfaces

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.describe_virtual_interfaces.async_describe_virtual_interfaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.describe_virtual_interfaces_request.DescribeVirtualInterfacesRequest = {}
        if connection_id is not None:
            input_["connection_id"] = connection_id
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
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

    async def disassociate_connection_from_lag(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        lag_id: "capo_direct_connect.types.lag_id.LagId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.connection.Connection":
        """<p>Disassociates a connection from a link aggregation group (LAG). The connection is interrupted and re-established as a standalone connection (the connection is not deleted; to delete the connection, use the <a>DeleteConnection</a> request). If the LAG has associated virtual interfaces or hosted connections, they remain associated with the LAG. A disassociated connection owned by an Direct Connect Partner is automatically converted to an interconnect.</p> <p>If disassociating the connection would cause the LAG to fall below its setting for minimum number of operational connections, the request fails, except when it's the last member of the LAG. If all connections are disassociated, the LAG continues to exist as an empty LAG with no physical connections. </p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            lag_id: <p>The ID of the LAG.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.disassociate_connection_from_lag_request.DisassociateConnectionFromLagRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.connection.Connection"]:
            import capo_direct_connect._operations.overture_service.disassociate_connection_from_lag

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.disassociate_connection_from_lag.async_disassociate_connection_from_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.disassociate_connection_from_lag_request.DisassociateConnectionFromLagRequest = {
            "connection_id": connection_id,
            "lag_id": lag_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_connections_from_resiliency_group(
        self,
        connection_identifiers: "capo_direct_connect.types.connection_identifier_list.ConnectionIdentifierList",
        resiliency_group_id: "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        client_token: Optional[
            "capo_direct_connect.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_direct_connect.types.disassociate_connections_from_resiliency_group_result.DisassociateConnectionsFromResiliencyGroupResult":
        """<p>Disassociates one or more connections from the specified resiliency group. This operation is atomic: either all of the specified connections are disassociated, or the operation fails and no changes are made.</p>

        Args:
            connection_identifiers: <p>The IDs or ARNs of the connections to disassociate from the resiliency group.</p>
            resiliency_group_id: <p>The ID of the resiliency group.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.disassociate_connections_from_resiliency_group_request.DisassociateConnectionsFromResiliencyGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.disassociate_connections_from_resiliency_group_result.DisassociateConnectionsFromResiliencyGroupResult"
        ]:
            import capo_direct_connect._operations.overture_service.disassociate_connections_from_resiliency_group

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.disassociate_connections_from_resiliency_group.async_disassociate_connections_from_resiliency_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.disassociate_connections_from_resiliency_group_request.DisassociateConnectionsFromResiliencyGroupRequest = {
            "connection_identifiers": connection_identifiers,
            "resiliency_group_id": resiliency_group_id,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_mac_sec_key(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        secret_arn: "capo_direct_connect.types.secret_arn.SecretARN",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.disassociate_mac_sec_key_response.DisassociateMacSecKeyResponse":
        """<p>Removes the association between a MAC Security (MACsec) security key and a Direct Connect connection.</p>

        Args:
            connection_id: <p>The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).</p> <p>You can use <a>DescribeConnections</a>, <a>DescribeInterconnects</a>, or <a>DescribeLags</a> to retrieve connection ID.</p>
            secret_arn: <p>The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key.</p> <p>You can use <a>DescribeConnections</a> to retrieve the ARN of the MAC Security (MACsec) secret key.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.disassociate_mac_sec_key_request.DisassociateMacSecKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.disassociate_mac_sec_key_response.DisassociateMacSecKeyResponse"
        ]:
            import capo_direct_connect._operations.overture_service.disassociate_mac_sec_key

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.disassociate_mac_sec_key.async_disassociate_mac_sec_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.disassociate_mac_sec_key_request.DisassociateMacSecKeyRequest = {
            "connection_id": connection_id,
            "secret_arn": secret_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resiliency_group(
        self,
        resiliency_group_id: "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> (
        "capo_direct_connect.types.get_resiliency_group_result.GetResiliencyGroupResult"
    ):
        """<p>Gets information about the specified resiliency group.</p>

        Args:
            resiliency_group_id: <p>The ID of the resiliency group.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.get_resiliency_group_request.GetResiliencyGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.get_resiliency_group_result.GetResiliencyGroupResult"
        ]:
            import capo_direct_connect._operations.overture_service.get_resiliency_group

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.get_resiliency_group.async_get_resiliency_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.get_resiliency_group_request.GetResiliencyGroupRequest = {
            "resiliency_group_id": resiliency_group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_resiliency_group_associations(
        self,
        resiliency_group_id: "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.list_resiliency_group_associations_result.ListResiliencyGroupAssociationsResult":
        """<p>Lists the connection associations for the specified resiliency group.</p>

        Args:
            resiliency_group_id: <p>The ID of the resiliency group.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.list_resiliency_group_associations_request.ListResiliencyGroupAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.list_resiliency_group_associations_result.ListResiliencyGroupAssociationsResult"
        ]:
            import capo_direct_connect._operations.overture_service.list_resiliency_group_associations

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.list_resiliency_group_associations.async_list_resiliency_group_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.list_resiliency_group_associations_request.ListResiliencyGroupAssociationsRequest = {
            "resiliency_group_id": resiliency_group_id
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

    async def list_resiliency_groups(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.list_resiliency_groups_result.ListResiliencyGroupsResult":
        """<p>Lists the resiliency groups owned by your Amazon Web Services account in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.list_resiliency_groups_request.ListResiliencyGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.list_resiliency_groups_result.ListResiliencyGroupsResult"
        ]:
            import capo_direct_connect._operations.overture_service.list_resiliency_groups

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.list_resiliency_groups.async_list_resiliency_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.list_resiliency_groups_request.ListResiliencyGroupsRequest = {}
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

    async def list_virtual_interface_routes(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        virtual_interface_id: Optional[
            "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        filters: Optional[
            "capo_direct_connect.types.route_filters.RouteFilters"
        ] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.list_virtual_interface_routes_response.ListVirtualInterfaceRoutesResponse":
        """<p>Lists the routes for the specified virtual interface.</p> <p>Use the <code>routeDirection</code> filter to control which routes are returned:</p> <ul> <li> <p> <code>accepted</code>: routes received from the customer network over the virtual interface.</p> </li> <li> <p> <code>advertised</code>: routes advertised to the customer network over the virtual interface.</p> </li> </ul>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            filters: <p>The filters to apply to the routes returned.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.list_virtual_interface_routes_request.ListVirtualInterfaceRoutesRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.list_virtual_interface_routes_response.ListVirtualInterfaceRoutesResponse"
        ]:
            import capo_direct_connect._operations.overture_service.list_virtual_interface_routes

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.list_virtual_interface_routes.async_list_virtual_interface_routes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.list_virtual_interface_routes_request.ListVirtualInterfaceRoutesRequest = {}
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_virtual_interface_test_history(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        test_id: Optional["capo_direct_connect.types.test_id.TestId"] = None,
        virtual_interface_id: Optional[
            "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        bgp_peers: Optional[
            "capo_direct_connect.types.bgp_peer_id_list.BGPPeerIdList"
        ] = None,
        status: Optional[
            "capo_direct_connect.types.failure_test_history_status.FailureTestHistoryStatus"
        ] = None,
        max_results: Optional[
            "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "capo_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_direct_connect.types.list_virtual_interface_test_history_response.ListVirtualInterfaceTestHistoryResponse":
        """<p>Lists the virtual interface failover test history.</p>

        Args:
            test_id: <p>The ID of the virtual interface failover test.</p>
            virtual_interface_id: <p>The ID of the virtual interface that was tested.</p>
            bgp_peers: <p>The BGP peers that were placed in the DOWN state during the virtual interface failover test.</p>
            status: <p>The status of the virtual interface failover test.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.list_virtual_interface_test_history_request.ListVirtualInterfaceTestHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.list_virtual_interface_test_history_response.ListVirtualInterfaceTestHistoryResponse"
        ]:
            import capo_direct_connect._operations.overture_service.list_virtual_interface_test_history

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.list_virtual_interface_test_history.async_list_virtual_interface_test_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.list_virtual_interface_test_history_request.ListVirtualInterfaceTestHistoryRequest = {}
        if test_id is not None:
            input_["test_id"] = test_id
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
        if bgp_peers is not None:
            input_["bgp_peers"] = bgp_peers
        if status is not None:
            input_["status"] = status
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

    async def start_bgp_failover_test(
        self,
        virtual_interface_id: "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        bgp_peers: Optional[
            "capo_direct_connect.types.bgp_peer_id_list.BGPPeerIdList"
        ] = None,
        test_duration_in_minutes: Optional[
            "capo_direct_connect.types.test_duration.TestDuration"
        ] = None,
    ) -> "capo_direct_connect.types.start_bgp_failover_test_response.StartBgpFailoverTestResponse":
        """<p>Starts the virtual interface failover test that verifies your configuration meets your resiliency requirements by placing the BGP peering session in the DOWN state. You can then send traffic to verify that there are no outages.</p> <p>You can run the test on public, private, transit, and hosted virtual interfaces.</p> <p>You can use <a href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceTestHistory.html">ListVirtualInterfaceTestHistory</a> to view the virtual interface test history.</p> <p>If you need to stop the test before the test interval completes, use <a href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StopBgpFailoverTest.html">StopBgpFailoverTest</a>.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface you want to test.</p>
            bgp_peers: <p>The BGP peers to place in the DOWN state.</p>
            test_duration_in_minutes: <p>The time in minutes that the virtual interface failover test will last.</p> <p>Maximum value: 4,320 minutes (72 hours).</p> <p>Default: 180 minutes (3 hours).</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.start_bgp_failover_test_request.StartBgpFailoverTestRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.start_bgp_failover_test_response.StartBgpFailoverTestResponse"
        ]:
            import capo_direct_connect._operations.overture_service.start_bgp_failover_test

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.start_bgp_failover_test.async_start_bgp_failover_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.start_bgp_failover_test_request.StartBgpFailoverTestRequest = {
            "virtual_interface_id": virtual_interface_id
        }
        if bgp_peers is not None:
            input_["bgp_peers"] = bgp_peers
        if test_duration_in_minutes is not None:
            input_["test_duration_in_minutes"] = test_duration_in_minutes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_bgp_failover_test(
        self,
        virtual_interface_id: "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.stop_bgp_failover_test_response.StopBgpFailoverTestResponse":
        """<p>Stops the virtual interface failover test.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface you no longer want to test.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.stop_bgp_failover_test_request.StopBgpFailoverTestRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.stop_bgp_failover_test_response.StopBgpFailoverTestResponse"
        ]:
            import capo_direct_connect._operations.overture_service.stop_bgp_failover_test

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.stop_bgp_failover_test.async_stop_bgp_failover_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.stop_bgp_failover_test_request.StopBgpFailoverTestRequest = {
            "virtual_interface_id": virtual_interface_id
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
        resource_arn: "capo_direct_connect.types.resource_arn.ResourceArn",
        tags: "capo_direct_connect.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified Direct Connect resource. Each resource can have a maximum of 50 tags.</p> <p>Each tag consists of a key and an optional value. If a tag with the same key is already associated with the resource, this action updates its value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags to add.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_direct_connect.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit on the number of tags that can be assigned.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_direct_connect._operations.overture_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_direct_connect.types.resource_arn.ResourceArn",
        tag_keys: "capo_direct_connect.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified Direct Connect resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys of the tags to remove.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_direct_connect._operations.overture_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connection(
        self,
        connection_id: "capo_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        connection_name: Optional[
            "capo_direct_connect.types.connection_name.ConnectionName"
        ] = None,
        encryption_mode: Optional[
            "capo_direct_connect.types.encryption_mode.EncryptionMode"
        ] = None,
    ) -> "capo_direct_connect.types.connection.Connection":
        """<p>Updates the Direct Connect connection configuration.</p> <p>You can update the following parameters for a connection:</p> <ul> <li> <p>The connection name</p> </li> <li> <p>The connection's MAC Security (MACsec) encryption mode.</p> </li> </ul>

        Args:
            connection_id: <p>The ID of the connection.</p> <p>You can use <a>DescribeConnections</a> to retrieve the connection ID.</p>
            connection_name: <p>The name of the connection.</p>
            encryption_mode: <p>The connection MAC Security (MACsec) encryption mode.</p> <p>The valid values are <code>no_encrypt</code>, <code>should_encrypt</code>, and <code>must_encrypt</code>.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.update_connection_request.UpdateConnectionRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.connection.Connection"]:
            import capo_direct_connect._operations.overture_service.update_connection

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.update_connection.async_update_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.update_connection_request.UpdateConnectionRequest = {
            "connection_id": connection_id
        }
        if connection_name is not None:
            input_["connection_name"] = connection_name
        if encryption_mode is not None:
            input_["encryption_mode"] = encryption_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connections_billing_mode(
        self,
        connection_ids: "capo_direct_connect.types.connection_id_list.ConnectionIdList",
        billing_mode: "capo_direct_connect.types.request_billing_mode.RequestBillingMode",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.update_connections_billing_mode_response.UpdateConnectionsBillingModeResponse":
        """<p>Updates the billing mode for the specified Direct Connect connections. You can update the billing mode for up to 200 connections in a single request.</p>

        Args:
            connection_ids: <p>The IDs of the connections to update. You can specify from 1 to 200 connections.</p>
            billing_mode: <p>The billing mode to apply to the specified connections. The valid values are <code>PayAsYouGo</code>, <code>FlatRateTier1</code>, <code>FlatRateTier2</code>, <code>FlatRateTier3</code>, <code>FlatRateTier4</code>, and <code>FlatRateTier5</code>.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.update_connections_billing_mode_request.UpdateConnectionsBillingModeRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.update_connections_billing_mode_response.UpdateConnectionsBillingModeResponse"
        ]:
            import capo_direct_connect._operations.overture_service.update_connections_billing_mode

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.update_connections_billing_mode.async_update_connections_billing_mode(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.update_connections_billing_mode_request.UpdateConnectionsBillingModeRequest = {
            "connection_ids": connection_ids,
            "billing_mode": billing_mode,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_direct_connect_gateway(
        self,
        direct_connect_gateway_id: "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        new_direct_connect_gateway_name: "capo_direct_connect.types.direct_connect_gateway_name.DirectConnectGatewayName",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "capo_direct_connect.types.update_direct_connect_gateway_response.UpdateDirectConnectGatewayResponse":
        """<p>Updates the name of a current Direct Connect gateway.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway to update.</p>
            new_direct_connect_gateway_name: <p>The new name for the Direct Connect gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.update_direct_connect_gateway_request.UpdateDirectConnectGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.update_direct_connect_gateway_response.UpdateDirectConnectGatewayResponse"
        ]:
            import capo_direct_connect._operations.overture_service.update_direct_connect_gateway

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.update_direct_connect_gateway.async_update_direct_connect_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.update_direct_connect_gateway_request.UpdateDirectConnectGatewayRequest = {
            "direct_connect_gateway_id": direct_connect_gateway_id,
            "new_direct_connect_gateway_name": new_direct_connect_gateway_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_direct_connect_gateway_association(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        association_id: Optional[
            "capo_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
        ] = None,
        add_allowed_prefixes_to_direct_connect_gateway: Optional[
            "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
        remove_allowed_prefixes_to_direct_connect_gateway: Optional[
            "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
    ) -> "capo_direct_connect.types.update_direct_connect_gateway_association_result.UpdateDirectConnectGatewayAssociationResult":
        """<p>Updates the specified attributes of the Direct Connect gateway association.</p> <p>Add or remove prefixes from the association.</p>

        Args:
            association_id: <p>The ID of the Direct Connect gateway association.</p>
            add_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to advertise to the Direct Connect gateway.</p>
            remove_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.update_direct_connect_gateway_association_request.UpdateDirectConnectGatewayAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.update_direct_connect_gateway_association_result.UpdateDirectConnectGatewayAssociationResult"
        ]:
            import capo_direct_connect._operations.overture_service.update_direct_connect_gateway_association

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.update_direct_connect_gateway_association.async_update_direct_connect_gateway_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.update_direct_connect_gateway_association_request.UpdateDirectConnectGatewayAssociationRequest = {}
        if association_id is not None:
            input_["association_id"] = association_id
        if add_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["add_allowed_prefixes_to_direct_connect_gateway"] = (
                add_allowed_prefixes_to_direct_connect_gateway
            )
        if remove_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["remove_allowed_prefixes_to_direct_connect_gateway"] = (
                remove_allowed_prefixes_to_direct_connect_gateway
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_lag(
        self,
        lag_id: "capo_direct_connect.types.lag_id.LagId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        lag_name: Optional["capo_direct_connect.types.lag_name.LagName"] = None,
        minimum_links: Optional["capo_direct_connect.types.count.Count"] = None,
        encryption_mode: Optional[
            "capo_direct_connect.types.encryption_mode.EncryptionMode"
        ] = None,
    ) -> "capo_direct_connect.types.lag.Lag":
        """<p>Updates the attributes of the specified link aggregation group (LAG).</p> <p>You can update the following LAG attributes:</p> <ul> <li> <p>The name of the LAG.</p> </li> <li> <p>The value for the minimum number of connections that must be operational for the LAG itself to be operational. </p> </li> <li> <p>The LAG's MACsec encryption mode.</p> <p>Amazon Web Services assigns this value to each connection which is part of the LAG.</p> </li> <li> <p>The tags</p> </li> </ul> <note> <p>If you adjust the threshold value for the minimum number of operational connections, ensure that the new value does not cause the LAG to fall below the threshold and become non-operational.</p> </note>

        Args:
            lag_id: <p>The ID of the LAG.</p>
            lag_name: <p>The name of the LAG.</p>
            minimum_links: <p>The minimum number of physical connections that must be operational for the LAG itself to be operational.</p>
            encryption_mode: <p>The LAG MAC Security (MACsec) encryption mode.</p> <p>Amazon Web Services applies the value to all connections which are part of the LAG.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.update_lag_request.UpdateLagRequest]",
        ) -> AsyncOperationResponse["capo_direct_connect.types.lag.Lag"]:
            import capo_direct_connect._operations.overture_service.update_lag

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.update_lag.async_update_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.update_lag_request.UpdateLagRequest = {
            "lag_id": lag_id
        }
        if lag_name is not None:
            input_["lag_name"] = lag_name
        if minimum_links is not None:
            input_["minimum_links"] = minimum_links
        if encryption_mode is not None:
            input_["encryption_mode"] = encryption_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resiliency_group(
        self,
        resiliency_group_id: "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId",
        resiliency_group_name: "capo_direct_connect.types.resiliency_group_name.ResiliencyGroupName",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        client_token: Optional[
            "capo_direct_connect.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_direct_connect.types.update_resiliency_group_result.UpdateResiliencyGroupResult":
        """<p>Updates the name of the specified resiliency group.</p>

        Args:
            resiliency_group_id: <p>The ID of the resiliency group.</p>
            resiliency_group_name: <p>The new name of the resiliency group.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.update_resiliency_group_request.UpdateResiliencyGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.update_resiliency_group_result.UpdateResiliencyGroupResult"
        ]:
            import capo_direct_connect._operations.overture_service.update_resiliency_group

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.update_resiliency_group.async_update_resiliency_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.update_resiliency_group_request.UpdateResiliencyGroupRequest = {
            "resiliency_group_id": resiliency_group_id,
            "resiliency_group_name": resiliency_group_name,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_virtual_interface_attributes(
        self,
        virtual_interface_id: "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        mtu: Optional["capo_direct_connect.types.mtu.MTU"] = None,
        enable_site_link: Optional[
            "capo_direct_connect.types.enable_site_link.EnableSiteLink"
        ] = None,
        virtual_interface_name: Optional[
            "capo_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
        ] = None,
        prefix_pool_allocated_count_ipv4: Optional[
            "capo_direct_connect.types.prefix_pool_allocated_count.PrefixPoolAllocatedCount"
        ] = None,
        prefix_pool_allocated_count_ipv6: Optional[
            "capo_direct_connect.types.prefix_pool_allocated_count.PrefixPoolAllocatedCount"
        ] = None,
        rate_limit: Optional["capo_direct_connect.types.rate_limit.RateLimit"] = None,
    ) -> "capo_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Updates the specified attributes of the specified virtual private interface.</p> <p>Setting the MTU of a virtual interface to 8500 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call <a>DescribeConnections</a>. To check whether your virtual interface supports jumbo frames, call <a>DescribeVirtualInterfaces</a>.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual private interface.</p>
            mtu: <p>The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500.</p>
            enable_site_link: <p>Indicates whether to enable or disable SiteLink.</p>
            virtual_interface_name: <p>The name of the virtual private interface.</p>
            prefix_pool_allocated_count_ipv4: <p>The number of inbound IPv4 route prefixes to allocate to the virtual interface. Not applicable to public virtual interfaces.</p>
            prefix_pool_allocated_count_ipv6: <p>The number of inbound IPv6 route prefixes to allocate to the virtual interface. Not applicable to public virtual interfaces.</p>
            rate_limit: <p>The rate limit (bandwidth allocation) to apply to the virtual interface. Use this to update the bandwidth allocation on an existing virtual interface.</p>

        Raises:
            capo_direct_connect.errors.direct_connect_client_exception.DirectConnectClientException: <p>One or more parameters are not valid.</p>
            capo_direct_connect.errors.direct_connect_server_exception.DirectConnectServerException: <p>A server-side error occurred.</p>
            capo_direct_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_direct_connect.types.update_virtual_interface_attributes_request.UpdateVirtualInterfaceAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import capo_direct_connect._operations.overture_service.update_virtual_interface_attributes

            (
                output,
                http_response,
            ) = await capo_direct_connect._operations.overture_service.update_virtual_interface_attributes.async_update_virtual_interface_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_direct_connect.types.update_virtual_interface_attributes_request.UpdateVirtualInterfaceAttributesRequest = {
            "virtual_interface_id": virtual_interface_id
        }
        if mtu is not None:
            input_["mtu"] = mtu
        if enable_site_link is not None:
            input_["enable_site_link"] = enable_site_link
        if virtual_interface_name is not None:
            input_["virtual_interface_name"] = virtual_interface_name
        if prefix_pool_allocated_count_ipv4 is not None:
            input_["prefix_pool_allocated_count_ipv4"] = (
                prefix_pool_allocated_count_ipv4
            )
        if prefix_pool_allocated_count_ipv6 is not None:
            input_["prefix_pool_allocated_count_ipv6"] = (
                prefix_pool_allocated_count_ipv6
            )
        if rate_limit is not None:
            input_["rate_limit"] = rate_limit

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
