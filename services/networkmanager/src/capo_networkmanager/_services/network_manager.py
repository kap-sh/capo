"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkManager``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_networkmanager._auth._signers
import capo_networkmanager._auth._sigv4
from capo_networkmanager._auth._identity import Credentials
from capo_networkmanager._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_networkmanager._auth._zapros_handler import AuthMiddleware
from capo_networkmanager._pagination import resolve_path as _resolve_path
from capo_networkmanager._services._aws_config import aws_config
from capo_networkmanager._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_networkmanager.types.accept_attachment_request
    import capo_networkmanager.types.accept_attachment_response
    import capo_networkmanager.types.action
    import capo_networkmanager.types.associate_connect_peer_request
    import capo_networkmanager.types.associate_connect_peer_response
    import capo_networkmanager.types.associate_customer_gateway_request
    import capo_networkmanager.types.associate_customer_gateway_response
    import capo_networkmanager.types.associate_link_request
    import capo_networkmanager.types.associate_link_response
    import capo_networkmanager.types.associate_transit_gateway_connect_peer_request
    import capo_networkmanager.types.associate_transit_gateway_connect_peer_response
    import capo_networkmanager.types.attachment
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.attachment_routing_policy_association_summary
    import capo_networkmanager.types.attachment_state
    import capo_networkmanager.types.attachment_type
    import capo_networkmanager.types.aws_account_id
    import capo_networkmanager.types.aws_location
    import capo_networkmanager.types.bandwidth
    import capo_networkmanager.types.bgp_options
    import capo_networkmanager.types.boolean
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.connect_attachment_options
    import capo_networkmanager.types.connect_peer_association
    import capo_networkmanager.types.connect_peer_id
    import capo_networkmanager.types.connect_peer_id_list
    import capo_networkmanager.types.connect_peer_summary
    import capo_networkmanager.types.connection
    import capo_networkmanager.types.connection_id
    import capo_networkmanager.types.connection_id_list
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.constrained_string_list
    import capo_networkmanager.types.core_network_change
    import capo_networkmanager.types.core_network_change_event
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.core_network_policy_alias
    import capo_networkmanager.types.core_network_policy_document
    import capo_networkmanager.types.core_network_policy_version
    import capo_networkmanager.types.core_network_routing_information
    import capo_networkmanager.types.core_network_summary
    import capo_networkmanager.types.create_connect_attachment_request
    import capo_networkmanager.types.create_connect_attachment_response
    import capo_networkmanager.types.create_connect_peer_request
    import capo_networkmanager.types.create_connect_peer_response
    import capo_networkmanager.types.create_connection_request
    import capo_networkmanager.types.create_connection_response
    import capo_networkmanager.types.create_core_network_prefix_list_association_request
    import capo_networkmanager.types.create_core_network_prefix_list_association_response
    import capo_networkmanager.types.create_core_network_request
    import capo_networkmanager.types.create_core_network_response
    import capo_networkmanager.types.create_device_request
    import capo_networkmanager.types.create_device_response
    import capo_networkmanager.types.create_direct_connect_gateway_attachment_request
    import capo_networkmanager.types.create_direct_connect_gateway_attachment_response
    import capo_networkmanager.types.create_global_network_request
    import capo_networkmanager.types.create_global_network_response
    import capo_networkmanager.types.create_link_request
    import capo_networkmanager.types.create_link_response
    import capo_networkmanager.types.create_site_request
    import capo_networkmanager.types.create_site_response
    import capo_networkmanager.types.create_site_to_site_vpn_attachment_request
    import capo_networkmanager.types.create_site_to_site_vpn_attachment_response
    import capo_networkmanager.types.create_transit_gateway_peering_request
    import capo_networkmanager.types.create_transit_gateway_peering_response
    import capo_networkmanager.types.create_transit_gateway_route_table_attachment_request
    import capo_networkmanager.types.create_transit_gateway_route_table_attachment_response
    import capo_networkmanager.types.create_vpc_attachment_request
    import capo_networkmanager.types.create_vpc_attachment_response
    import capo_networkmanager.types.customer_gateway_arn
    import capo_networkmanager.types.customer_gateway_arn_list
    import capo_networkmanager.types.customer_gateway_association
    import capo_networkmanager.types.delete_attachment_request
    import capo_networkmanager.types.delete_attachment_response
    import capo_networkmanager.types.delete_connect_peer_request
    import capo_networkmanager.types.delete_connect_peer_response
    import capo_networkmanager.types.delete_connection_request
    import capo_networkmanager.types.delete_connection_response
    import capo_networkmanager.types.delete_core_network_policy_version_request
    import capo_networkmanager.types.delete_core_network_policy_version_response
    import capo_networkmanager.types.delete_core_network_prefix_list_association_request
    import capo_networkmanager.types.delete_core_network_prefix_list_association_response
    import capo_networkmanager.types.delete_core_network_request
    import capo_networkmanager.types.delete_core_network_response
    import capo_networkmanager.types.delete_device_request
    import capo_networkmanager.types.delete_device_response
    import capo_networkmanager.types.delete_global_network_request
    import capo_networkmanager.types.delete_global_network_response
    import capo_networkmanager.types.delete_link_request
    import capo_networkmanager.types.delete_link_response
    import capo_networkmanager.types.delete_peering_request
    import capo_networkmanager.types.delete_peering_response
    import capo_networkmanager.types.delete_resource_policy_request
    import capo_networkmanager.types.delete_resource_policy_response
    import capo_networkmanager.types.delete_site_request
    import capo_networkmanager.types.delete_site_response
    import capo_networkmanager.types.deregister_transit_gateway_request
    import capo_networkmanager.types.deregister_transit_gateway_response
    import capo_networkmanager.types.describe_global_networks_request
    import capo_networkmanager.types.describe_global_networks_response
    import capo_networkmanager.types.device
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.device_id_list
    import capo_networkmanager.types.direct_connect_gateway_arn
    import capo_networkmanager.types.disassociate_connect_peer_request
    import capo_networkmanager.types.disassociate_connect_peer_response
    import capo_networkmanager.types.disassociate_customer_gateway_request
    import capo_networkmanager.types.disassociate_customer_gateway_response
    import capo_networkmanager.types.disassociate_link_request
    import capo_networkmanager.types.disassociate_link_response
    import capo_networkmanager.types.disassociate_transit_gateway_connect_peer_request
    import capo_networkmanager.types.disassociate_transit_gateway_connect_peer_response
    import capo_networkmanager.types.execute_core_network_change_set_request
    import capo_networkmanager.types.execute_core_network_change_set_response
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.external_region_code_list
    import capo_networkmanager.types.filter_map
    import capo_networkmanager.types.get_connect_attachment_request
    import capo_networkmanager.types.get_connect_attachment_response
    import capo_networkmanager.types.get_connect_peer_associations_request
    import capo_networkmanager.types.get_connect_peer_associations_response
    import capo_networkmanager.types.get_connect_peer_request
    import capo_networkmanager.types.get_connect_peer_response
    import capo_networkmanager.types.get_connections_request
    import capo_networkmanager.types.get_connections_response
    import capo_networkmanager.types.get_core_network_change_events_request
    import capo_networkmanager.types.get_core_network_change_events_response
    import capo_networkmanager.types.get_core_network_change_set_request
    import capo_networkmanager.types.get_core_network_change_set_response
    import capo_networkmanager.types.get_core_network_policy_request
    import capo_networkmanager.types.get_core_network_policy_response
    import capo_networkmanager.types.get_core_network_request
    import capo_networkmanager.types.get_core_network_response
    import capo_networkmanager.types.get_customer_gateway_associations_request
    import capo_networkmanager.types.get_customer_gateway_associations_response
    import capo_networkmanager.types.get_devices_request
    import capo_networkmanager.types.get_devices_response
    import capo_networkmanager.types.get_direct_connect_gateway_attachment_request
    import capo_networkmanager.types.get_direct_connect_gateway_attachment_response
    import capo_networkmanager.types.get_link_associations_request
    import capo_networkmanager.types.get_link_associations_response
    import capo_networkmanager.types.get_links_request
    import capo_networkmanager.types.get_links_response
    import capo_networkmanager.types.get_network_resource_counts_request
    import capo_networkmanager.types.get_network_resource_counts_response
    import capo_networkmanager.types.get_network_resource_relationships_request
    import capo_networkmanager.types.get_network_resource_relationships_response
    import capo_networkmanager.types.get_network_resources_request
    import capo_networkmanager.types.get_network_resources_response
    import capo_networkmanager.types.get_network_routes_request
    import capo_networkmanager.types.get_network_routes_response
    import capo_networkmanager.types.get_network_telemetry_request
    import capo_networkmanager.types.get_network_telemetry_response
    import capo_networkmanager.types.get_resource_policy_request
    import capo_networkmanager.types.get_resource_policy_response
    import capo_networkmanager.types.get_route_analysis_request
    import capo_networkmanager.types.get_route_analysis_response
    import capo_networkmanager.types.get_site_to_site_vpn_attachment_request
    import capo_networkmanager.types.get_site_to_site_vpn_attachment_response
    import capo_networkmanager.types.get_sites_request
    import capo_networkmanager.types.get_sites_response
    import capo_networkmanager.types.get_transit_gateway_connect_peer_associations_request
    import capo_networkmanager.types.get_transit_gateway_connect_peer_associations_response
    import capo_networkmanager.types.get_transit_gateway_peering_request
    import capo_networkmanager.types.get_transit_gateway_peering_response
    import capo_networkmanager.types.get_transit_gateway_registrations_request
    import capo_networkmanager.types.get_transit_gateway_registrations_response
    import capo_networkmanager.types.get_transit_gateway_route_table_attachment_request
    import capo_networkmanager.types.get_transit_gateway_route_table_attachment_response
    import capo_networkmanager.types.get_vpc_attachment_request
    import capo_networkmanager.types.get_vpc_attachment_response
    import capo_networkmanager.types.global_network
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.global_network_id_list
    import capo_networkmanager.types.integer
    import capo_networkmanager.types.ip_address
    import capo_networkmanager.types.link
    import capo_networkmanager.types.link_association
    import capo_networkmanager.types.link_id
    import capo_networkmanager.types.link_id_list
    import capo_networkmanager.types.list_attachment_routing_policy_associations_request
    import capo_networkmanager.types.list_attachment_routing_policy_associations_response
    import capo_networkmanager.types.list_attachments_request
    import capo_networkmanager.types.list_attachments_response
    import capo_networkmanager.types.list_connect_peers_request
    import capo_networkmanager.types.list_connect_peers_response
    import capo_networkmanager.types.list_core_network_policy_versions_request
    import capo_networkmanager.types.list_core_network_policy_versions_response
    import capo_networkmanager.types.list_core_network_prefix_list_associations_request
    import capo_networkmanager.types.list_core_network_prefix_list_associations_response
    import capo_networkmanager.types.list_core_network_routing_information_request
    import capo_networkmanager.types.list_core_network_routing_information_response
    import capo_networkmanager.types.list_core_networks_request
    import capo_networkmanager.types.list_core_networks_response
    import capo_networkmanager.types.list_organization_service_access_status_request
    import capo_networkmanager.types.list_organization_service_access_status_response
    import capo_networkmanager.types.list_peerings_request
    import capo_networkmanager.types.list_peerings_response
    import capo_networkmanager.types.list_tags_for_resource_request
    import capo_networkmanager.types.list_tags_for_resource_response
    import capo_networkmanager.types.location
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.network_resource
    import capo_networkmanager.types.network_resource_count
    import capo_networkmanager.types.network_resource_metadata_map
    import capo_networkmanager.types.network_telemetry
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.peering
    import capo_networkmanager.types.peering_id
    import capo_networkmanager.types.peering_state
    import capo_networkmanager.types.peering_type
    import capo_networkmanager.types.prefix_list_arn
    import capo_networkmanager.types.prefix_list_association
    import capo_networkmanager.types.put_attachment_routing_policy_label_request
    import capo_networkmanager.types.put_attachment_routing_policy_label_response
    import capo_networkmanager.types.put_core_network_policy_request
    import capo_networkmanager.types.put_core_network_policy_response
    import capo_networkmanager.types.put_resource_policy_request
    import capo_networkmanager.types.put_resource_policy_response
    import capo_networkmanager.types.register_transit_gateway_request
    import capo_networkmanager.types.register_transit_gateway_response
    import capo_networkmanager.types.reject_attachment_request
    import capo_networkmanager.types.reject_attachment_response
    import capo_networkmanager.types.relationship
    import capo_networkmanager.types.remove_attachment_routing_policy_label_request
    import capo_networkmanager.types.remove_attachment_routing_policy_label_response
    import capo_networkmanager.types.resource_arn
    import capo_networkmanager.types.restore_core_network_policy_version_request
    import capo_networkmanager.types.restore_core_network_policy_version_response
    import capo_networkmanager.types.route_analysis_endpoint_options_specification
    import capo_networkmanager.types.route_state_list
    import capo_networkmanager.types.route_table_identifier
    import capo_networkmanager.types.route_type_list
    import capo_networkmanager.types.site
    import capo_networkmanager.types.site_id
    import capo_networkmanager.types.site_id_list
    import capo_networkmanager.types.start_organization_service_access_update_request
    import capo_networkmanager.types.start_organization_service_access_update_response
    import capo_networkmanager.types.start_route_analysis_request
    import capo_networkmanager.types.start_route_analysis_response
    import capo_networkmanager.types.subnet_arn
    import capo_networkmanager.types.subnet_arn_list
    import capo_networkmanager.types.synthesized_json_core_network_policy_document
    import capo_networkmanager.types.synthesized_json_resource_policy_document
    import capo_networkmanager.types.tag_key_list
    import capo_networkmanager.types.tag_list
    import capo_networkmanager.types.tag_resource_request
    import capo_networkmanager.types.tag_resource_response
    import capo_networkmanager.types.transit_gateway_arn
    import capo_networkmanager.types.transit_gateway_arn_list
    import capo_networkmanager.types.transit_gateway_connect_peer_arn
    import capo_networkmanager.types.transit_gateway_connect_peer_arn_list
    import capo_networkmanager.types.transit_gateway_connect_peer_association
    import capo_networkmanager.types.transit_gateway_registration
    import capo_networkmanager.types.transit_gateway_route_table_arn
    import capo_networkmanager.types.untag_resource_request
    import capo_networkmanager.types.untag_resource_response
    import capo_networkmanager.types.update_connection_request
    import capo_networkmanager.types.update_connection_response
    import capo_networkmanager.types.update_core_network_request
    import capo_networkmanager.types.update_core_network_response
    import capo_networkmanager.types.update_device_request
    import capo_networkmanager.types.update_device_response
    import capo_networkmanager.types.update_direct_connect_gateway_attachment_request
    import capo_networkmanager.types.update_direct_connect_gateway_attachment_response
    import capo_networkmanager.types.update_global_network_request
    import capo_networkmanager.types.update_global_network_response
    import capo_networkmanager.types.update_link_request
    import capo_networkmanager.types.update_link_response
    import capo_networkmanager.types.update_network_resource_metadata_request
    import capo_networkmanager.types.update_network_resource_metadata_response
    import capo_networkmanager.types.update_site_request
    import capo_networkmanager.types.update_site_response
    import capo_networkmanager.types.update_vpc_attachment_request
    import capo_networkmanager.types.update_vpc_attachment_response
    import capo_networkmanager.types.vpc_arn
    import capo_networkmanager.types.vpc_options
    import capo_networkmanager.types.vpn_connection_arn


class NetworkManagerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class NetworkManagerClient:
    """A client for the ``NetworkManager`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = NetworkManagerClientConfig(
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
        self, config_overrides: Optional[NetworkManagerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: NetworkManagerClientConfig = config_overrides or {}
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

    def accept_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> (
        "capo_networkmanager.types.accept_attachment_response.AcceptAttachmentResponse"
    ):
        """<p>Accepts a core network attachment request. </p> <p>Once the attachment request is accepted by a core network owner, the attachment is created and connected to a core network.</p>

        Args:
            attachment_id: <p>The ID of the attachment. </p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.accept_attachment_request.AcceptAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.accept_attachment_response.AcceptAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.accept_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.accept_attachment.accept_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.accept_attachment_request.AcceptAttachmentRequest = {
            "attachment_id": attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_connect_peer(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        connect_peer_id: "capo_networkmanager.types.connect_peer_id.ConnectPeerId",
        device_id: "capo_networkmanager.types.device_id.DeviceId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        link_id: Optional["capo_networkmanager.types.link_id.LinkId"] = None,
    ) -> "capo_networkmanager.types.associate_connect_peer_response.AssociateConnectPeerResponse":
        """<p>Associates a core network Connect peer with a device and optionally, with a link. </p> <p>If you specify a link, it must be associated with the specified device. You can only associate core network Connect peers that have been created on a core network Connect attachment on a core network. </p>

        Args:
            global_network_id: <p>The ID of your global network.</p>
            connect_peer_id: <p>The ID of the Connect peer.</p>
            device_id: <p>The ID of the device.</p>
            link_id: <p>The ID of the link.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.associate_connect_peer_request.AssociateConnectPeerRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.associate_connect_peer_response.AssociateConnectPeerResponse"
        ]:
            import capo_networkmanager._operations.network_manager.associate_connect_peer

            output, http_response = (
                capo_networkmanager._operations.network_manager.associate_connect_peer.associate_connect_peer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.associate_connect_peer_request.AssociateConnectPeerRequest = {
            "global_network_id": global_network_id,
            "connect_peer_id": connect_peer_id,
            "device_id": device_id,
        }
        if link_id is not None:
            input_["link_id"] = link_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_customer_gateway(
        self,
        customer_gateway_arn: "capo_networkmanager.types.customer_gateway_arn.CustomerGatewayArn",
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        device_id: "capo_networkmanager.types.device_id.DeviceId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        link_id: Optional["capo_networkmanager.types.link_id.LinkId"] = None,
    ) -> "capo_networkmanager.types.associate_customer_gateway_response.AssociateCustomerGatewayResponse":
        """<p>Associates a customer gateway with a device and optionally, with a link. If you specify a link, it must be associated with the specified device. </p> <p>You can only associate customer gateways that are connected to a VPN attachment on a transit gateway or core network registered in your global network. When you register a transit gateway or core network, customer gateways that are connected to the transit gateway are automatically included in the global network. To list customer gateways that are connected to a transit gateway, use the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConnections.html">DescribeVpnConnections</a> EC2 API and filter by <code>transit-gateway-id</code>.</p> <p>You cannot associate a customer gateway with more than one device and link. </p>

        Args:
            customer_gateway_arn: <p>The Amazon Resource Name (ARN) of the customer gateway.</p>
            global_network_id: <p>The ID of the global network.</p>
            device_id: <p>The ID of the device.</p>
            link_id: <p>The ID of the link.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.associate_customer_gateway_request.AssociateCustomerGatewayRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.associate_customer_gateway_response.AssociateCustomerGatewayResponse"
        ]:
            import capo_networkmanager._operations.network_manager.associate_customer_gateway

            output, http_response = (
                capo_networkmanager._operations.network_manager.associate_customer_gateway.associate_customer_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.associate_customer_gateway_request.AssociateCustomerGatewayRequest = {
            "customer_gateway_arn": customer_gateway_arn,
            "global_network_id": global_network_id,
            "device_id": device_id,
        }
        if link_id is not None:
            input_["link_id"] = link_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_link(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        device_id: "capo_networkmanager.types.device_id.DeviceId",
        link_id: "capo_networkmanager.types.link_id.LinkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.associate_link_response.AssociateLinkResponse":
        """<p>Associates a link to a device. A device can be associated to multiple links and a link can be associated to multiple devices. The device and link must be in the same global network and the same site.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            device_id: <p>The ID of the device.</p>
            link_id: <p>The ID of the link.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.associate_link_request.AssociateLinkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.associate_link_response.AssociateLinkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.associate_link

            output, http_response = (
                capo_networkmanager._operations.network_manager.associate_link.associate_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.associate_link_request.AssociateLinkRequest = {
            "global_network_id": global_network_id,
            "device_id": device_id,
            "link_id": link_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_transit_gateway_connect_peer(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        transit_gateway_connect_peer_arn: "capo_networkmanager.types.transit_gateway_connect_peer_arn.TransitGatewayConnectPeerArn",
        device_id: "capo_networkmanager.types.device_id.DeviceId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        link_id: Optional["capo_networkmanager.types.link_id.LinkId"] = None,
    ) -> "capo_networkmanager.types.associate_transit_gateway_connect_peer_response.AssociateTransitGatewayConnectPeerResponse":
        """<p>Associates a transit gateway Connect peer with a device, and optionally, with a link. If you specify a link, it must be associated with the specified device. </p> <p>You can only associate transit gateway Connect peers that have been created on a transit gateway that's registered in your global network.</p> <p>You cannot associate a transit gateway Connect peer with more than one device and link. </p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            transit_gateway_connect_peer_arn: <p>The Amazon Resource Name (ARN) of the Connect peer.</p>
            device_id: <p>The ID of the device.</p>
            link_id: <p>The ID of the link.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.associate_transit_gateway_connect_peer_request.AssociateTransitGatewayConnectPeerRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.associate_transit_gateway_connect_peer_response.AssociateTransitGatewayConnectPeerResponse"
        ]:
            import capo_networkmanager._operations.network_manager.associate_transit_gateway_connect_peer

            output, http_response = (
                capo_networkmanager._operations.network_manager.associate_transit_gateway_connect_peer.associate_transit_gateway_connect_peer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.associate_transit_gateway_connect_peer_request.AssociateTransitGatewayConnectPeerRequest = {
            "global_network_id": global_network_id,
            "transit_gateway_connect_peer_arn": transit_gateway_connect_peer_arn,
            "device_id": device_id,
        }
        if link_id is not None:
            input_["link_id"] = link_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_connect_attachment(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        edge_location: "capo_networkmanager.types.external_region_code.ExternalRegionCode",
        transport_attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        options: "capo_networkmanager.types.connect_attachment_options.ConnectAttachmentOptions",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        routing_policy_label: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.create_connect_attachment_response.CreateConnectAttachmentResponse":
        """<p>Creates a core network Connect attachment from a specified core network attachment. </p> <p>A core network Connect attachment is a GRE-based tunnel attachment that you can use to establish a connection between a core network and an appliance. A core network Connect attachment uses an existing VPC attachment as the underlying transport mechanism.</p>

        Args:
            core_network_id: <p>The ID of a core network where you want to create the attachment. </p>
            edge_location: <p>The Region where the edge is located.</p>
            transport_attachment_id: <p>The ID of the attachment between the two connections.</p>
            routing_policy_label: <p>The routing policy label to apply to the Connect attachment for traffic routing decisions.</p>
            options: <p>Options for creating an attachment.</p>
            tags: <p>The list of key-value tags associated with the request.</p>
            client_token: <p>The client token associated with the request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_connect_attachment_request.CreateConnectAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_connect_attachment_response.CreateConnectAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_connect_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_connect_attachment.create_connect_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_connect_attachment_request.CreateConnectAttachmentRequest = {
            "core_network_id": core_network_id,
            "edge_location": edge_location,
            "transport_attachment_id": transport_attachment_id,
            "options": options,
        }
        if routing_policy_label is not None:
            input_["routing_policy_label"] = routing_policy_label
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_connection(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        device_id: "capo_networkmanager.types.device_id.DeviceId",
        connected_device_id: "capo_networkmanager.types.device_id.DeviceId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        link_id: Optional["capo_networkmanager.types.link_id.LinkId"] = None,
        connected_link_id: Optional["capo_networkmanager.types.link_id.LinkId"] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
    ) -> (
        "capo_networkmanager.types.create_connection_response.CreateConnectionResponse"
    ):
        """<p>Creates a connection between two devices. The devices can be a physical or virtual appliance that connects to a third-party appliance in a VPC, or a physical appliance that connects to another physical appliance in an on-premises network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            device_id: <p>The ID of the first device in the connection.</p>
            connected_device_id: <p>The ID of the second device in the connection.</p>
            link_id: <p>The ID of the link for the first device.</p>
            connected_link_id: <p>The ID of the link for the second device.</p>
            description: <p>A description of the connection.</p> <p>Length Constraints: Maximum length of 256 characters.</p>
            tags: <p>The tags to apply to the resource during creation.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_connection_request.CreateConnectionRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_connection_response.CreateConnectionResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_connection

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_connection.create_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_connection_request.CreateConnectionRequest = {
            "global_network_id": global_network_id,
            "device_id": device_id,
            "connected_device_id": connected_device_id,
        }
        if link_id is not None:
            input_["link_id"] = link_id
        if connected_link_id is not None:
            input_["connected_link_id"] = connected_link_id
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

    def create_connect_peer(
        self,
        connect_attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        peer_address: "capo_networkmanager.types.ip_address.IPAddress",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_address: Optional[
            "capo_networkmanager.types.ip_address.IPAddress"
        ] = None,
        bgp_options: Optional[
            "capo_networkmanager.types.bgp_options.BgpOptions"
        ] = None,
        inside_cidr_blocks: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
        subnet_arn: Optional["capo_networkmanager.types.subnet_arn.SubnetArn"] = None,
    ) -> "capo_networkmanager.types.create_connect_peer_response.CreateConnectPeerResponse":
        """<p>Creates a core network Connect peer for a specified core network connect attachment between a core network and an appliance. The peer address and transit gateway address must be the same IP address family (IPv4 or IPv6).</p>

        Args:
            connect_attachment_id: <p>The ID of the connection attachment.</p>
            core_network_address: <p>A Connect peer core network address. This only applies only when the protocol is <code>GRE</code>.</p>
            peer_address: <p>The Connect peer address.</p>
            bgp_options: <p>The Connect peer BGP options. This only applies only when the protocol is <code>GRE</code>.</p>
            inside_cidr_blocks: <p>The inside IP addresses used for BGP peering.</p>
            tags: <p>The tags associated with the peer request.</p>
            client_token: <p>The client token associated with the request.</p>
            subnet_arn: <p>The subnet ARN for the Connect peer. This only applies only when the protocol is NO_ENCAP.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_connect_peer_request.CreateConnectPeerRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_connect_peer_response.CreateConnectPeerResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_connect_peer

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_connect_peer.create_connect_peer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_connect_peer_request.CreateConnectPeerRequest = {
            "connect_attachment_id": connect_attachment_id,
            "peer_address": peer_address,
        }
        if core_network_address is not None:
            input_["core_network_address"] = core_network_address
        if bgp_options is not None:
            input_["bgp_options"] = bgp_options
        if inside_cidr_blocks is not None:
            input_["inside_cidr_blocks"] = inside_cidr_blocks
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if subnet_arn is not None:
            input_["subnet_arn"] = subnet_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_core_network(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
        policy_document: Optional[
            "capo_networkmanager.types.core_network_policy_document.CoreNetworkPolicyDocument"
        ] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.create_core_network_response.CreateCoreNetworkResponse":
        """<p>Creates a core network as part of your global network, and optionally, with a core network policy.</p>

        Args:
            global_network_id: <p>The ID of the global network that a core network will be a part of. </p>
            description: <p>The description of a core network.</p>
            tags: <p>Key-value tags associated with a core network request.</p>
            policy_document: <p>The policy document for creating a core network.</p>
            client_token: <p>The client token associated with a core network request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.core_network_policy_exception.CoreNetworkPolicyException: <p>Describes a core network policy exception.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_core_network_request.CreateCoreNetworkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_core_network_response.CreateCoreNetworkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_core_network

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_core_network.create_core_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_core_network_request.CreateCoreNetworkRequest = {
            "global_network_id": global_network_id
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if policy_document is not None:
            input_["policy_document"] = policy_document
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_core_network_prefix_list_association(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        prefix_list_arn: "capo_networkmanager.types.prefix_list_arn.PrefixListArn",
        prefix_list_alias: "capo_networkmanager.types.constrained_string.ConstrainedString",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.create_core_network_prefix_list_association_response.CreateCoreNetworkPrefixListAssociationResponse":
        """<p>Creates an association between a core network and a prefix list for routing control.</p>

        Args:
            core_network_id: <p>The ID of the core network to associate with the prefix list.</p>
            prefix_list_arn: <p>The ARN of the prefix list to associate with the core network.</p>
            prefix_list_alias: <p>An optional alias for the prefix list association.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_core_network_prefix_list_association_request.CreateCoreNetworkPrefixListAssociationRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_core_network_prefix_list_association_response.CreateCoreNetworkPrefixListAssociationResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_core_network_prefix_list_association

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_core_network_prefix_list_association.create_core_network_prefix_list_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_core_network_prefix_list_association_request.CreateCoreNetworkPrefixListAssociationRequest = {
            "core_network_id": core_network_id,
            "prefix_list_arn": prefix_list_arn,
            "prefix_list_alias": prefix_list_alias,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_device(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        aws_location: Optional[
            "capo_networkmanager.types.aws_location.AWSLocation"
        ] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        vendor: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        model: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        serial_number: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        location: Optional["capo_networkmanager.types.location.Location"] = None,
        site_id: Optional["capo_networkmanager.types.site_id.SiteId"] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
    ) -> "capo_networkmanager.types.create_device_response.CreateDeviceResponse":
        """<p>Creates a new device in a global network. If you specify both a site ID and a location, the location of the site is used for visualization in the Network Manager console.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            aws_location: <p>The Amazon Web Services location of the device, if applicable. For an on-premises device, you can omit this parameter.</p>
            description: <p>A description of the device.</p> <p>Constraints: Maximum length of 256 characters.</p>
            type: <p>The type of the device.</p>
            vendor: <p>The vendor of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>
            model: <p>The model of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>
            serial_number: <p>The serial number of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>
            location: <p>The location of the device.</p>
            site_id: <p>The ID of the site.</p>
            tags: <p>The tags to apply to the resource during creation.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_device_request.CreateDeviceRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_device_response.CreateDeviceResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_device

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_device.create_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_device_request.CreateDeviceRequest = {
            "global_network_id": global_network_id
        }
        if aws_location is not None:
            input_["aws_location"] = aws_location
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if vendor is not None:
            input_["vendor"] = vendor
        if model is not None:
            input_["model"] = model
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if location is not None:
            input_["location"] = location
        if site_id is not None:
            input_["site_id"] = site_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_direct_connect_gateway_attachment(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        direct_connect_gateway_arn: "capo_networkmanager.types.direct_connect_gateway_arn.DirectConnectGatewayArn",
        edge_locations: "capo_networkmanager.types.external_region_code_list.ExternalRegionCodeList",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        routing_policy_label: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.create_direct_connect_gateway_attachment_response.CreateDirectConnectGatewayAttachmentResponse":
        """<p>Creates an Amazon Web Services Direct Connect gateway attachment </p>

        Args:
            core_network_id: <p>The ID of the Cloud WAN core network that the Direct Connect gateway attachment should be attached to.</p>
            direct_connect_gateway_arn: <p>The ARN of the Direct Connect gateway attachment.</p>
            routing_policy_label: <p>The routing policy label to apply to the Direct Connect Gateway attachment for traffic routing decisions.</p>
            edge_locations: <p>One or more core network edge locations that the Direct Connect gateway attachment is associated with. </p>
            tags: <p>The key value tags to apply to the Direct Connect gateway attachment during creation.</p>
            client_token: <p>client token</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_direct_connect_gateway_attachment_request.CreateDirectConnectGatewayAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_direct_connect_gateway_attachment_response.CreateDirectConnectGatewayAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_direct_connect_gateway_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_direct_connect_gateway_attachment.create_direct_connect_gateway_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_direct_connect_gateway_attachment_request.CreateDirectConnectGatewayAttachmentRequest = {
            "core_network_id": core_network_id,
            "direct_connect_gateway_arn": direct_connect_gateway_arn,
            "edge_locations": edge_locations,
        }
        if routing_policy_label is not None:
            input_["routing_policy_label"] = routing_policy_label
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_global_network(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
    ) -> "capo_networkmanager.types.create_global_network_response.CreateGlobalNetworkResponse":
        """<p>Creates a new, empty global network.</p>

        Args:
            description: <p>A description of the global network.</p> <p>Constraints: Maximum length of 256 characters.</p>
            tags: <p>The tags to apply to the resource during creation.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_global_network_request.CreateGlobalNetworkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_global_network_response.CreateGlobalNetworkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_global_network

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_global_network.create_global_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_global_network_request.CreateGlobalNetworkRequest = {}
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

    def create_link(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        bandwidth: "capo_networkmanager.types.bandwidth.Bandwidth",
        site_id: "capo_networkmanager.types.site_id.SiteId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        provider: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
    ) -> "capo_networkmanager.types.create_link_response.CreateLinkResponse":
        r"""<p>Creates a new link for a specified site.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            description: <p>A description of the link.</p> <p>Constraints: Maximum length of 256 characters.</p>
            type: <p>The type of the link.</p> <p>Constraints: Maximum length of 128 characters. Cannot include the following characters: | \ ^</p>
            bandwidth: <p> The upload speed and download speed in Mbps. </p>
            provider: <p>The provider of the link.</p> <p>Constraints: Maximum length of 128 characters. Cannot include the following characters: | \ ^</p>
            site_id: <p>The ID of the site.</p>
            tags: <p>The tags to apply to the resource during creation.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_link_request.CreateLinkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_link_response.CreateLinkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_link

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_link.create_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_link_request.CreateLinkRequest = {
            "global_network_id": global_network_id,
            "bandwidth": bandwidth,
            "site_id": site_id,
        }
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if provider is not None:
            input_["provider"] = provider
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_site(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        location: Optional["capo_networkmanager.types.location.Location"] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
    ) -> "capo_networkmanager.types.create_site_response.CreateSiteResponse":
        """<p>Creates a new site in a global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            description: <p>A description of your site.</p> <p>Constraints: Maximum length of 256 characters.</p>
            location: <p>The site location. This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated.</p> <ul> <li> <p> <code>Address</code>: The physical address of the site.</p> </li> <li> <p> <code>Latitude</code>: The latitude of the site. </p> </li> <li> <p> <code>Longitude</code>: The longitude of the site.</p> </li> </ul>
            tags: <p>The tags to apply to the resource during creation.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_site_request.CreateSiteRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_site_response.CreateSiteResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_site

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_site.create_site(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_site_request.CreateSiteRequest = {
            "global_network_id": global_network_id
        }
        if description is not None:
            input_["description"] = description
        if location is not None:
            input_["location"] = location
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_site_to_site_vpn_attachment(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        vpn_connection_arn: "capo_networkmanager.types.vpn_connection_arn.VpnConnectionArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        routing_policy_label: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.create_site_to_site_vpn_attachment_response.CreateSiteToSiteVpnAttachmentResponse":
        """<p>Creates an Amazon Web Services site-to-site VPN attachment on an edge location of a core network.</p>

        Args:
            core_network_id: <p>The ID of a core network where you're creating a site-to-site VPN attachment.</p>
            vpn_connection_arn: <p>The ARN identifying the VPN attachment.</p>
            routing_policy_label: <p>The routing policy label to apply to the Site-to-Site VPN attachment for traffic routing decisions.</p>
            tags: <p>The tags associated with the request.</p>
            client_token: <p>The client token associated with the request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_site_to_site_vpn_attachment_request.CreateSiteToSiteVpnAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_site_to_site_vpn_attachment_response.CreateSiteToSiteVpnAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_site_to_site_vpn_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_site_to_site_vpn_attachment.create_site_to_site_vpn_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_site_to_site_vpn_attachment_request.CreateSiteToSiteVpnAttachmentRequest = {
            "core_network_id": core_network_id,
            "vpn_connection_arn": vpn_connection_arn,
        }
        if routing_policy_label is not None:
            input_["routing_policy_label"] = routing_policy_label
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_transit_gateway_peering(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        transit_gateway_arn: "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.create_transit_gateway_peering_response.CreateTransitGatewayPeeringResponse":
        """<p>Creates a transit gateway peering connection.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            transit_gateway_arn: <p>The ARN of the transit gateway for the peering request.</p>
            tags: <p>The list of key-value tags associated with the request.</p>
            client_token: <p>The client token associated with the request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_transit_gateway_peering_request.CreateTransitGatewayPeeringRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_transit_gateway_peering_response.CreateTransitGatewayPeeringResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_transit_gateway_peering

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_transit_gateway_peering.create_transit_gateway_peering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_transit_gateway_peering_request.CreateTransitGatewayPeeringRequest = {
            "core_network_id": core_network_id,
            "transit_gateway_arn": transit_gateway_arn,
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_transit_gateway_route_table_attachment(
        self,
        peering_id: "capo_networkmanager.types.peering_id.PeeringId",
        transit_gateway_route_table_arn: "capo_networkmanager.types.transit_gateway_route_table_arn.TransitGatewayRouteTableArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        routing_policy_label: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.create_transit_gateway_route_table_attachment_response.CreateTransitGatewayRouteTableAttachmentResponse":
        """<p>Creates a transit gateway route table attachment.</p>

        Args:
            peering_id: <p>The ID of the peer for the </p>
            transit_gateway_route_table_arn: <p>The ARN of the transit gateway route table for the attachment request. For example, <code>"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"</code>.</p>
            routing_policy_label: <p>The routing policy label to apply to the Transit Gateway route table attachment for traffic routing decisions.</p>
            tags: <p>The list of key-value tags associated with the request.</p>
            client_token: <p>The client token associated with the request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_transit_gateway_route_table_attachment_request.CreateTransitGatewayRouteTableAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_transit_gateway_route_table_attachment_response.CreateTransitGatewayRouteTableAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_transit_gateway_route_table_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_transit_gateway_route_table_attachment.create_transit_gateway_route_table_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_transit_gateway_route_table_attachment_request.CreateTransitGatewayRouteTableAttachmentRequest = {
            "peering_id": peering_id,
            "transit_gateway_route_table_arn": transit_gateway_route_table_arn,
        }
        if routing_policy_label is not None:
            input_["routing_policy_label"] = routing_policy_label
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_vpc_attachment(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        vpc_arn: "capo_networkmanager.types.vpc_arn.VpcArn",
        subnet_arns: "capo_networkmanager.types.subnet_arn_list.SubnetArnList",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        options: Optional["capo_networkmanager.types.vpc_options.VpcOptions"] = None,
        routing_policy_label: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        tags: Optional["capo_networkmanager.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.create_vpc_attachment_response.CreateVpcAttachmentResponse":
        """<p>Creates a VPC attachment on an edge location of a core network.</p>

        Args:
            core_network_id: <p>The ID of a core network for the VPC attachment.</p>
            vpc_arn: <p>The ARN of the VPC.</p>
            subnet_arns: <p>The subnet ARN of the VPC attachment.</p>
            options: <p>Options for the VPC attachment.</p>
            routing_policy_label: <p>The routing policy label to apply to the VPC attachment for traffic routing decisions.</p>
            tags: <p>The key-value tags associated with the request.</p>
            client_token: <p>The client token associated with the request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.create_vpc_attachment_request.CreateVpcAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.create_vpc_attachment_response.CreateVpcAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.create_vpc_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.create_vpc_attachment.create_vpc_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.create_vpc_attachment_request.CreateVpcAttachmentRequest = {
            "core_network_id": core_network_id,
            "vpc_arn": vpc_arn,
            "subnet_arns": subnet_arns,
        }
        if options is not None:
            input_["options"] = options
        if routing_policy_label is not None:
            input_["routing_policy_label"] = routing_policy_label
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> (
        "capo_networkmanager.types.delete_attachment_response.DeleteAttachmentResponse"
    ):
        """<p>Deletes an attachment. Supports all attachment types.</p>

        Args:
            attachment_id: <p>The ID of the attachment to delete.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_attachment_request.DeleteAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_attachment_response.DeleteAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_attachment.delete_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_attachment_request.DeleteAttachmentRequest = {
            "attachment_id": attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connection(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        connection_id: "capo_networkmanager.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> (
        "capo_networkmanager.types.delete_connection_response.DeleteConnectionResponse"
    ):
        """<p>Deletes the specified connection in your global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            connection_id: <p>The ID of the connection.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_connection_response.DeleteConnectionResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_connection

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_connection.delete_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_connection_request.DeleteConnectionRequest = {
            "global_network_id": global_network_id,
            "connection_id": connection_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connect_peer(
        self,
        connect_peer_id: "capo_networkmanager.types.connect_peer_id.ConnectPeerId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_connect_peer_response.DeleteConnectPeerResponse":
        """<p>Deletes a Connect peer.</p>

        Args:
            connect_peer_id: <p>The ID of the deleted Connect peer.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_connect_peer_request.DeleteConnectPeerRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_connect_peer_response.DeleteConnectPeerResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_connect_peer

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_connect_peer.delete_connect_peer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_connect_peer_request.DeleteConnectPeerRequest = {
            "connect_peer_id": connect_peer_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_core_network(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_core_network_response.DeleteCoreNetworkResponse":
        """<p>Deletes a core network along with all core network policies. This can only be done if there are no attachments on a core network.</p>

        Args:
            core_network_id: <p>The network ID of the deleted core network.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_core_network_request.DeleteCoreNetworkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_core_network_response.DeleteCoreNetworkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_core_network

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_core_network.delete_core_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_core_network_request.DeleteCoreNetworkRequest = {
            "core_network_id": core_network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_core_network_policy_version(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        policy_version_id: "capo_networkmanager.types.integer.Integer",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_core_network_policy_version_response.DeleteCoreNetworkPolicyVersionResponse":
        """<p>Deletes a policy version from a core network. You can't delete the current LIVE policy.</p>

        Args:
            core_network_id: <p>The ID of a core network for the deleted policy.</p>
            policy_version_id: <p>The version ID of the deleted policy.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_core_network_policy_version_request.DeleteCoreNetworkPolicyVersionRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_core_network_policy_version_response.DeleteCoreNetworkPolicyVersionResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_core_network_policy_version

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_core_network_policy_version.delete_core_network_policy_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_core_network_policy_version_request.DeleteCoreNetworkPolicyVersionRequest = {
            "core_network_id": core_network_id,
            "policy_version_id": policy_version_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_core_network_prefix_list_association(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        prefix_list_arn: "capo_networkmanager.types.prefix_list_arn.PrefixListArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_core_network_prefix_list_association_response.DeleteCoreNetworkPrefixListAssociationResponse":
        """<p>Deletes an association between a core network and a prefix list.</p>

        Args:
            core_network_id: <p>The ID of the core network from which to delete the prefix list association.</p>
            prefix_list_arn: <p>The ARN of the prefix list to disassociate from the core network.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_core_network_prefix_list_association_request.DeleteCoreNetworkPrefixListAssociationRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_core_network_prefix_list_association_response.DeleteCoreNetworkPrefixListAssociationResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_core_network_prefix_list_association

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_core_network_prefix_list_association.delete_core_network_prefix_list_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_core_network_prefix_list_association_request.DeleteCoreNetworkPrefixListAssociationRequest = {
            "core_network_id": core_network_id,
            "prefix_list_arn": prefix_list_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_device(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        device_id: "capo_networkmanager.types.device_id.DeviceId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_device_response.DeleteDeviceResponse":
        """<p>Deletes an existing device. You must first disassociate the device from any links and customer gateways.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            device_id: <p>The ID of the device.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_device_request.DeleteDeviceRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_device_response.DeleteDeviceResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_device

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_device.delete_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_device_request.DeleteDeviceRequest = {
            "global_network_id": global_network_id,
            "device_id": device_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_global_network(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_global_network_response.DeleteGlobalNetworkResponse":
        """<p>Deletes an existing global network. You must first delete all global network objects (devices, links, and sites), deregister all transit gateways, and delete any core networks.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_global_network_request.DeleteGlobalNetworkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_global_network_response.DeleteGlobalNetworkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_global_network

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_global_network.delete_global_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_global_network_request.DeleteGlobalNetworkRequest = {
            "global_network_id": global_network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_link(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        link_id: "capo_networkmanager.types.link_id.LinkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_link_response.DeleteLinkResponse":
        """<p>Deletes an existing link. You must first disassociate the link from any devices and customer gateways.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            link_id: <p>The ID of the link.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_link_request.DeleteLinkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_link_response.DeleteLinkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_link

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_link.delete_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_link_request.DeleteLinkRequest = {
            "global_network_id": global_network_id,
            "link_id": link_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_peering(
        self,
        peering_id: "capo_networkmanager.types.peering_id.PeeringId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_peering_response.DeletePeeringResponse":
        """<p>Deletes an existing peering connection.</p>

        Args:
            peering_id: <p>The ID of the peering connection to delete.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_peering_request.DeletePeeringRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_peering_response.DeletePeeringResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_peering

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_peering.delete_peering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_peering_request.DeletePeeringRequest = {
            "peering_id": peering_id
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
        resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a resource policy for the specified resource. This revokes the access of the principals specified in the resource policy.</p>

        Args:
            resource_arn: <p>The ARN of the policy to delete.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_resource_policy

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_site(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        site_id: "capo_networkmanager.types.site_id.SiteId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.delete_site_response.DeleteSiteResponse":
        """<p>Deletes an existing site. The site cannot be associated with any device or link.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            site_id: <p>The ID of the site.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.delete_site_request.DeleteSiteRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.delete_site_response.DeleteSiteResponse"
        ]:
            import capo_networkmanager._operations.network_manager.delete_site

            output, http_response = (
                capo_networkmanager._operations.network_manager.delete_site.delete_site(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.delete_site_request.DeleteSiteRequest = {
            "global_network_id": global_network_id,
            "site_id": site_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_transit_gateway(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        transit_gateway_arn: "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.deregister_transit_gateway_response.DeregisterTransitGatewayResponse":
        """<p>Deregisters a transit gateway from your global network. This action does not delete your transit gateway, or modify any of its attachments. This action removes any customer gateway associations.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            transit_gateway_arn: <p>The Amazon Resource Name (ARN) of the transit gateway.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.deregister_transit_gateway_request.DeregisterTransitGatewayRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.deregister_transit_gateway_response.DeregisterTransitGatewayResponse"
        ]:
            import capo_networkmanager._operations.network_manager.deregister_transit_gateway

            output, http_response = (
                capo_networkmanager._operations.network_manager.deregister_transit_gateway.deregister_transit_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.deregister_transit_gateway_request.DeregisterTransitGatewayRequest = {
            "global_network_id": global_network_id,
            "transit_gateway_arn": transit_gateway_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_global_networks(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        global_network_ids: Optional[
            "capo_networkmanager.types.global_network_id_list.GlobalNetworkIdList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.describe_global_networks_response.DescribeGlobalNetworksResponse":
        """<p>Describes one or more global networks. By default, all global networks are described. To describe the objects in your global network, you must use the appropriate <code>Get*</code> action. For example, to list the transit gateways in your global network, use <a>GetTransitGatewayRegistrations</a>.</p>

        Args:
            global_network_ids: <p>The IDs of one or more global networks. The maximum is 10.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.describe_global_networks_request.DescribeGlobalNetworksRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.describe_global_networks_response.DescribeGlobalNetworksResponse"
        ]:
            import capo_networkmanager._operations.network_manager.describe_global_networks

            output, http_response = (
                capo_networkmanager._operations.network_manager.describe_global_networks.describe_global_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.describe_global_networks_request.DescribeGlobalNetworksRequest = {}
        if global_network_ids is not None:
            input_["global_network_ids"] = global_network_ids
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

    def iter_describe_global_networks(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        global_network_ids: Optional[
            "capo_networkmanager.types.global_network_id_list.GlobalNetworkIdList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.global_network.GlobalNetwork]":
        _token = next_token
        while True:
            _response = self.describe_global_networks(
                config_overrides=config_overrides,
                global_network_ids=global_network_ids,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("global_networks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def disassociate_connect_peer(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        connect_peer_id: "capo_networkmanager.types.connect_peer_id.ConnectPeerId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.disassociate_connect_peer_response.DisassociateConnectPeerResponse":
        """<p>Disassociates a core network Connect peer from a device and a link. </p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            connect_peer_id: <p>The ID of the Connect peer to disassociate from a device.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.disassociate_connect_peer_request.DisassociateConnectPeerRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.disassociate_connect_peer_response.DisassociateConnectPeerResponse"
        ]:
            import capo_networkmanager._operations.network_manager.disassociate_connect_peer

            output, http_response = (
                capo_networkmanager._operations.network_manager.disassociate_connect_peer.disassociate_connect_peer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.disassociate_connect_peer_request.DisassociateConnectPeerRequest = {
            "global_network_id": global_network_id,
            "connect_peer_id": connect_peer_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_customer_gateway(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        customer_gateway_arn: "capo_networkmanager.types.customer_gateway_arn.CustomerGatewayArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.disassociate_customer_gateway_response.DisassociateCustomerGatewayResponse":
        """<p>Disassociates a customer gateway from a device and a link.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            customer_gateway_arn: <p>The Amazon Resource Name (ARN) of the customer gateway.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.disassociate_customer_gateway_request.DisassociateCustomerGatewayRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.disassociate_customer_gateway_response.DisassociateCustomerGatewayResponse"
        ]:
            import capo_networkmanager._operations.network_manager.disassociate_customer_gateway

            output, http_response = (
                capo_networkmanager._operations.network_manager.disassociate_customer_gateway.disassociate_customer_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.disassociate_customer_gateway_request.DisassociateCustomerGatewayRequest = {
            "global_network_id": global_network_id,
            "customer_gateway_arn": customer_gateway_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_link(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        device_id: "capo_networkmanager.types.device_id.DeviceId",
        link_id: "capo_networkmanager.types.link_id.LinkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> (
        "capo_networkmanager.types.disassociate_link_response.DisassociateLinkResponse"
    ):
        """<p>Disassociates an existing device from a link. You must first disassociate any customer gateways that are associated with the link.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            device_id: <p>The ID of the device.</p>
            link_id: <p>The ID of the link.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.disassociate_link_request.DisassociateLinkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.disassociate_link_response.DisassociateLinkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.disassociate_link

            output, http_response = (
                capo_networkmanager._operations.network_manager.disassociate_link.disassociate_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.disassociate_link_request.DisassociateLinkRequest = {
            "global_network_id": global_network_id,
            "device_id": device_id,
            "link_id": link_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_transit_gateway_connect_peer(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        transit_gateway_connect_peer_arn: "capo_networkmanager.types.transit_gateway_connect_peer_arn.TransitGatewayConnectPeerArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.disassociate_transit_gateway_connect_peer_response.DisassociateTransitGatewayConnectPeerResponse":
        """<p>Disassociates a transit gateway Connect peer from a device and link.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            transit_gateway_connect_peer_arn: <p>The Amazon Resource Name (ARN) of the transit gateway Connect peer.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.disassociate_transit_gateway_connect_peer_request.DisassociateTransitGatewayConnectPeerRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.disassociate_transit_gateway_connect_peer_response.DisassociateTransitGatewayConnectPeerResponse"
        ]:
            import capo_networkmanager._operations.network_manager.disassociate_transit_gateway_connect_peer

            output, http_response = (
                capo_networkmanager._operations.network_manager.disassociate_transit_gateway_connect_peer.disassociate_transit_gateway_connect_peer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.disassociate_transit_gateway_connect_peer_request.DisassociateTransitGatewayConnectPeerRequest = {
            "global_network_id": global_network_id,
            "transit_gateway_connect_peer_arn": transit_gateway_connect_peer_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def execute_core_network_change_set(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        policy_version_id: "capo_networkmanager.types.integer.Integer",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.execute_core_network_change_set_response.ExecuteCoreNetworkChangeSetResponse":
        """<p>Executes a change set on your core network. Deploys changes globally based on the policy submitted..</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            policy_version_id: <p>The ID of the policy version.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.execute_core_network_change_set_request.ExecuteCoreNetworkChangeSetRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.execute_core_network_change_set_response.ExecuteCoreNetworkChangeSetResponse"
        ]:
            import capo_networkmanager._operations.network_manager.execute_core_network_change_set

            output, http_response = (
                capo_networkmanager._operations.network_manager.execute_core_network_change_set.execute_core_network_change_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.execute_core_network_change_set_request.ExecuteCoreNetworkChangeSetRequest = {
            "core_network_id": core_network_id,
            "policy_version_id": policy_version_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_connect_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.get_connect_attachment_response.GetConnectAttachmentResponse":
        """<p>Returns information about a core network Connect attachment.</p>

        Args:
            attachment_id: <p>The ID of the attachment.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_connect_attachment_request.GetConnectAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_connect_attachment_response.GetConnectAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_connect_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_connect_attachment.get_connect_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_connect_attachment_request.GetConnectAttachmentRequest = {
            "attachment_id": attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_connections(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        connection_ids: Optional[
            "capo_networkmanager.types.connection_id_list.ConnectionIdList"
        ] = None,
        device_id: Optional["capo_networkmanager.types.device_id.DeviceId"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_connections_response.GetConnectionsResponse":
        """<p>Gets information about one or more of your connections in a global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            connection_ids: <p>One or more connection IDs.</p>
            device_id: <p>The ID of the device.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_connections_request.GetConnectionsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_connections_response.GetConnectionsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_connections

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_connections.get_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_connections_request.GetConnectionsRequest = {
            "global_network_id": global_network_id
        }
        if connection_ids is not None:
            input_["connection_ids"] = connection_ids
        if device_id is not None:
            input_["device_id"] = device_id
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

    def iter_get_connections(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        connection_ids: Optional[
            "capo_networkmanager.types.connection_id_list.ConnectionIdList"
        ] = None,
        device_id: Optional["capo_networkmanager.types.device_id.DeviceId"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.connection.Connection]":
        _token = next_token
        while True:
            _response = self.get_connections(
                global_network_id,
                config_overrides=config_overrides,
                connection_ids=connection_ids,
                device_id=device_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("connections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_connect_peer(
        self,
        connect_peer_id: "capo_networkmanager.types.connect_peer_id.ConnectPeerId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.get_connect_peer_response.GetConnectPeerResponse":
        """<p>Returns information about a core network Connect peer.</p>

        Args:
            connect_peer_id: <p>The ID of the Connect peer.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_connect_peer_request.GetConnectPeerRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_connect_peer_response.GetConnectPeerResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_connect_peer

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_connect_peer.get_connect_peer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_connect_peer_request.GetConnectPeerRequest = {
            "connect_peer_id": connect_peer_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_connect_peer_associations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        connect_peer_ids: Optional[
            "capo_networkmanager.types.connect_peer_id_list.ConnectPeerIdList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_connect_peer_associations_response.GetConnectPeerAssociationsResponse":
        """<p>Returns information about a core network Connect peer associations.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            connect_peer_ids: <p>The IDs of the Connect peers.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_connect_peer_associations_request.GetConnectPeerAssociationsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_connect_peer_associations_response.GetConnectPeerAssociationsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_connect_peer_associations

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_connect_peer_associations.get_connect_peer_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_connect_peer_associations_request.GetConnectPeerAssociationsRequest = {
            "global_network_id": global_network_id
        }
        if connect_peer_ids is not None:
            input_["connect_peer_ids"] = connect_peer_ids
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

    def iter_get_connect_peer_associations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        connect_peer_ids: Optional[
            "capo_networkmanager.types.connect_peer_id_list.ConnectPeerIdList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.connect_peer_association.ConnectPeerAssociation]":
        _token = next_token
        while True:
            _response = self.get_connect_peer_associations(
                global_network_id,
                config_overrides=config_overrides,
                connect_peer_ids=connect_peer_ids,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("connect_peer_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_core_network(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.get_core_network_response.GetCoreNetworkResponse":
        """<p>Returns information about the LIVE policy for a core network.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_core_network_request.GetCoreNetworkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_core_network_response.GetCoreNetworkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_core_network

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_core_network.get_core_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_core_network_request.GetCoreNetworkRequest = {
            "core_network_id": core_network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_core_network_change_events(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        policy_version_id: "capo_networkmanager.types.integer.Integer",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_core_network_change_events_response.GetCoreNetworkChangeEventsResponse":
        """<p>Returns information about a core network change event.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            policy_version_id: <p>The ID of the policy version.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_core_network_change_events_request.GetCoreNetworkChangeEventsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_core_network_change_events_response.GetCoreNetworkChangeEventsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_core_network_change_events

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_core_network_change_events.get_core_network_change_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_core_network_change_events_request.GetCoreNetworkChangeEventsRequest = {
            "core_network_id": core_network_id,
            "policy_version_id": policy_version_id,
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

    def iter_get_core_network_change_events(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        policy_version_id: "capo_networkmanager.types.integer.Integer",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.core_network_change_event.CoreNetworkChangeEvent]":
        _token = next_token
        while True:
            _response = self.get_core_network_change_events(
                core_network_id,
                policy_version_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("core_network_change_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_core_network_change_set(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        policy_version_id: "capo_networkmanager.types.integer.Integer",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_core_network_change_set_response.GetCoreNetworkChangeSetResponse":
        """<p>Returns a change set between the LIVE core network policy and a submitted policy.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            policy_version_id: <p>The ID of the policy version.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_core_network_change_set_request.GetCoreNetworkChangeSetRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_core_network_change_set_response.GetCoreNetworkChangeSetResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_core_network_change_set

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_core_network_change_set.get_core_network_change_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_core_network_change_set_request.GetCoreNetworkChangeSetRequest = {
            "core_network_id": core_network_id,
            "policy_version_id": policy_version_id,
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

    def iter_get_core_network_change_set(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        policy_version_id: "capo_networkmanager.types.integer.Integer",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.core_network_change.CoreNetworkChange]":
        _token = next_token
        while True:
            _response = self.get_core_network_change_set(
                core_network_id,
                policy_version_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("core_network_changes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_core_network_policy(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        policy_version_id: Optional["capo_networkmanager.types.integer.Integer"] = None,
        alias: Optional[
            "capo_networkmanager.types.core_network_policy_alias.CoreNetworkPolicyAlias"
        ] = None,
    ) -> "capo_networkmanager.types.get_core_network_policy_response.GetCoreNetworkPolicyResponse":
        """<p>Returns details about a core network policy. You can get details about your current live policy or any previous policy version.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            policy_version_id: <p>The ID of a core network policy version.</p>
            alias: <p>The alias of a core network policy </p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_core_network_policy_request.GetCoreNetworkPolicyRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_core_network_policy_response.GetCoreNetworkPolicyResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_core_network_policy

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_core_network_policy.get_core_network_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_core_network_policy_request.GetCoreNetworkPolicyRequest = {
            "core_network_id": core_network_id
        }
        if policy_version_id is not None:
            input_["policy_version_id"] = policy_version_id
        if alias is not None:
            input_["alias"] = alias

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_customer_gateway_associations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        customer_gateway_arns: Optional[
            "capo_networkmanager.types.customer_gateway_arn_list.CustomerGatewayArnList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_customer_gateway_associations_response.GetCustomerGatewayAssociationsResponse":
        """<p>Gets the association information for customer gateways that are associated with devices and links in your global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            customer_gateway_arns: <p>One or more customer gateway Amazon Resource Names (ARNs). The maximum is 10.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_customer_gateway_associations_request.GetCustomerGatewayAssociationsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_customer_gateway_associations_response.GetCustomerGatewayAssociationsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_customer_gateway_associations

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_customer_gateway_associations.get_customer_gateway_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_customer_gateway_associations_request.GetCustomerGatewayAssociationsRequest = {
            "global_network_id": global_network_id
        }
        if customer_gateway_arns is not None:
            input_["customer_gateway_arns"] = customer_gateway_arns
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

    def iter_get_customer_gateway_associations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        customer_gateway_arns: Optional[
            "capo_networkmanager.types.customer_gateway_arn_list.CustomerGatewayArnList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.customer_gateway_association.CustomerGatewayAssociation]":
        _token = next_token
        while True:
            _response = self.get_customer_gateway_associations(
                global_network_id,
                config_overrides=config_overrides,
                customer_gateway_arns=customer_gateway_arns,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("customer_gateway_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_devices(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        device_ids: Optional[
            "capo_networkmanager.types.device_id_list.DeviceIdList"
        ] = None,
        site_id: Optional["capo_networkmanager.types.site_id.SiteId"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_devices_response.GetDevicesResponse":
        """<p>Gets information about one or more of your devices in a global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            device_ids: <p>One or more device IDs. The maximum is 10.</p>
            site_id: <p>The ID of the site.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_devices_request.GetDevicesRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_devices_response.GetDevicesResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_devices

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_devices.get_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_devices_request.GetDevicesRequest = {
            "global_network_id": global_network_id
        }
        if device_ids is not None:
            input_["device_ids"] = device_ids
        if site_id is not None:
            input_["site_id"] = site_id
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

    def iter_get_devices(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        device_ids: Optional[
            "capo_networkmanager.types.device_id_list.DeviceIdList"
        ] = None,
        site_id: Optional["capo_networkmanager.types.site_id.SiteId"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.device.Device]":
        _token = next_token
        while True:
            _response = self.get_devices(
                global_network_id,
                config_overrides=config_overrides,
                device_ids=device_ids,
                site_id=site_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_direct_connect_gateway_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.get_direct_connect_gateway_attachment_response.GetDirectConnectGatewayAttachmentResponse":
        """<p>Returns information about a specific Amazon Web Services Direct Connect gateway attachment.</p>

        Args:
            attachment_id: <p>The ID of the Direct Connect gateway attachment that you want to see details about.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_direct_connect_gateway_attachment_request.GetDirectConnectGatewayAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_direct_connect_gateway_attachment_response.GetDirectConnectGatewayAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_direct_connect_gateway_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_direct_connect_gateway_attachment.get_direct_connect_gateway_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_direct_connect_gateway_attachment_request.GetDirectConnectGatewayAttachmentRequest = {
            "attachment_id": attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_link_associations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        device_id: Optional["capo_networkmanager.types.device_id.DeviceId"] = None,
        link_id: Optional["capo_networkmanager.types.link_id.LinkId"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_link_associations_response.GetLinkAssociationsResponse":
        """<p>Gets the link associations for a device or a link. Either the device ID or the link ID must be specified.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            device_id: <p>The ID of the device.</p>
            link_id: <p>The ID of the link.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_link_associations_request.GetLinkAssociationsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_link_associations_response.GetLinkAssociationsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_link_associations

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_link_associations.get_link_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_link_associations_request.GetLinkAssociationsRequest = {
            "global_network_id": global_network_id
        }
        if device_id is not None:
            input_["device_id"] = device_id
        if link_id is not None:
            input_["link_id"] = link_id
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

    def iter_get_link_associations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        device_id: Optional["capo_networkmanager.types.device_id.DeviceId"] = None,
        link_id: Optional["capo_networkmanager.types.link_id.LinkId"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.link_association.LinkAssociation]":
        _token = next_token
        while True:
            _response = self.get_link_associations(
                global_network_id,
                config_overrides=config_overrides,
                device_id=device_id,
                link_id=link_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("link_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_links(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        link_ids: Optional["capo_networkmanager.types.link_id_list.LinkIdList"] = None,
        site_id: Optional["capo_networkmanager.types.site_id.SiteId"] = None,
        type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        provider: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_links_response.GetLinksResponse":
        """<p>Gets information about one or more links in a specified global network.</p> <p>If you specify the site ID, you cannot specify the type or provider in the same request. You can specify the type and provider in the same request.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            link_ids: <p>One or more link IDs. The maximum is 10.</p>
            site_id: <p>The ID of the site.</p>
            type: <p>The link type.</p>
            provider: <p>The link provider.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_links_request.GetLinksRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_links_response.GetLinksResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_links

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_links.get_links(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_links_request.GetLinksRequest = {
            "global_network_id": global_network_id
        }
        if link_ids is not None:
            input_["link_ids"] = link_ids
        if site_id is not None:
            input_["site_id"] = site_id
        if type is not None:
            input_["type"] = type
        if provider is not None:
            input_["provider"] = provider
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

    def iter_get_links(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        link_ids: Optional["capo_networkmanager.types.link_id_list.LinkIdList"] = None,
        site_id: Optional["capo_networkmanager.types.site_id.SiteId"] = None,
        type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        provider: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.link.Link]":
        _token = next_token
        while True:
            _response = self.get_links(
                global_network_id,
                config_overrides=config_overrides,
                link_ids=link_ids,
                site_id=site_id,
                type=type,
                provider=provider,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("links",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_network_resource_counts(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        resource_type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_network_resource_counts_response.GetNetworkResourceCountsResponse":
        """<p>Gets the count of network resources, by resource type, for the specified global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            resource_type: <p>The resource type.</p> <p>The following are the supported resource types for Direct Connect:</p> <ul> <li> <p> <code>dxcon</code> </p> </li> <li> <p> <code>dx-gateway</code> </p> </li> <li> <p> <code>dx-vif</code> </p> </li> </ul> <p>The following are the supported resource types for Network Manager:</p> <ul> <li> <p> <code>attachment</code> </p> </li> <li> <p> <code>connect-peer</code> </p> </li> <li> <p> <code>connection</code> </p> </li> <li> <p> <code>core-network</code> </p> </li> <li> <p> <code>device</code> </p> </li> <li> <p> <code>link</code> </p> </li> <li> <p> <code>peering</code> </p> </li> <li> <p> <code>site</code> </p> </li> </ul> <p>The following are the supported resource types for Amazon VPC:</p> <ul> <li> <p> <code>customer-gateway</code> </p> </li> <li> <p> <code>transit-gateway</code> </p> </li> <li> <p> <code>transit-gateway-attachment</code> </p> </li> <li> <p> <code>transit-gateway-connect-peer</code> </p> </li> <li> <p> <code>transit-gateway-route-table</code> </p> </li> <li> <p> <code>vpn-connection</code> </p> </li> </ul>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_network_resource_counts_request.GetNetworkResourceCountsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_network_resource_counts_response.GetNetworkResourceCountsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_network_resource_counts

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_network_resource_counts.get_network_resource_counts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_network_resource_counts_request.GetNetworkResourceCountsRequest = {
            "global_network_id": global_network_id
        }
        if resource_type is not None:
            input_["resource_type"] = resource_type
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

    def iter_get_network_resource_counts(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        resource_type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.network_resource_count.NetworkResourceCount]":
        _token = next_token
        while True:
            _response = self.get_network_resource_counts(
                global_network_id,
                config_overrides=config_overrides,
                resource_type=resource_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("network_resource_counts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_network_resource_relationships(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        registered_gateway_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        aws_region: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        account_id: Optional[
            "capo_networkmanager.types.aws_account_id.AWSAccountId"
        ] = None,
        resource_type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        resource_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_network_resource_relationships_response.GetNetworkResourceRelationshipsResponse":
        """<p>Gets the network resource relationships for the specified global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            core_network_id: <p>The ID of a core network.</p>
            registered_gateway_arn: <p>The ARN of the registered gateway.</p>
            aws_region: <p>The Amazon Web Services Region.</p>
            account_id: <p>The Amazon Web Services account ID.</p>
            resource_type: <p>The resource type.</p> <p>The following are the supported resource types for Direct Connect:</p> <ul> <li> <p> <code>dxcon</code> </p> </li> <li> <p> <code>dx-gateway</code> </p> </li> <li> <p> <code>dx-vif</code> </p> </li> </ul> <p>The following are the supported resource types for Network Manager:</p> <ul> <li> <p> <code>attachment</code> </p> </li> <li> <p> <code>connect-peer</code> </p> </li> <li> <p> <code>connection</code> </p> </li> <li> <p> <code>core-network</code> </p> </li> <li> <p> <code>device</code> </p> </li> <li> <p> <code>link</code> </p> </li> <li> <p> <code>peering</code> </p> </li> <li> <p> <code>site</code> </p> </li> </ul> <p>The following are the supported resource types for Amazon VPC:</p> <ul> <li> <p> <code>customer-gateway</code> </p> </li> <li> <p> <code>transit-gateway</code> </p> </li> <li> <p> <code>transit-gateway-attachment</code> </p> </li> <li> <p> <code>transit-gateway-connect-peer</code> </p> </li> <li> <p> <code>transit-gateway-route-table</code> </p> </li> <li> <p> <code>vpn-connection</code> </p> </li> </ul>
            resource_arn: <p>The ARN of the gateway.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_network_resource_relationships_request.GetNetworkResourceRelationshipsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_network_resource_relationships_response.GetNetworkResourceRelationshipsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_network_resource_relationships

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_network_resource_relationships.get_network_resource_relationships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_network_resource_relationships_request.GetNetworkResourceRelationshipsRequest = {
            "global_network_id": global_network_id
        }
        if core_network_id is not None:
            input_["core_network_id"] = core_network_id
        if registered_gateway_arn is not None:
            input_["registered_gateway_arn"] = registered_gateway_arn
        if aws_region is not None:
            input_["aws_region"] = aws_region
        if account_id is not None:
            input_["account_id"] = account_id
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
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

    def iter_get_network_resource_relationships(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        registered_gateway_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        aws_region: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        account_id: Optional[
            "capo_networkmanager.types.aws_account_id.AWSAccountId"
        ] = None,
        resource_type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        resource_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.relationship.Relationship]":
        _token = next_token
        while True:
            _response = self.get_network_resource_relationships(
                global_network_id,
                config_overrides=config_overrides,
                core_network_id=core_network_id,
                registered_gateway_arn=registered_gateway_arn,
                aws_region=aws_region,
                account_id=account_id,
                resource_type=resource_type,
                resource_arn=resource_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("relationships",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_network_resources(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        registered_gateway_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        aws_region: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        account_id: Optional[
            "capo_networkmanager.types.aws_account_id.AWSAccountId"
        ] = None,
        resource_type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        resource_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_network_resources_response.GetNetworkResourcesResponse":
        """<p>Describes the network resources for the specified global network.</p> <p>The results include information from the corresponding Describe call for the resource, minus any sensitive information such as pre-shared keys.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            core_network_id: <p>The ID of a core network.</p>
            registered_gateway_arn: <p>The ARN of the gateway.</p>
            aws_region: <p>The Amazon Web Services Region.</p>
            account_id: <p>The Amazon Web Services account ID.</p>
            resource_type: <p>The resource type.</p> <p>The following are the supported resource types for Direct Connect:</p> <ul> <li> <p> <code>dxcon</code> </p> </li> <li> <p> <code>dx-gateway</code> </p> </li> <li> <p> <code>dx-vif</code> </p> </li> </ul> <p>The following are the supported resource types for Network Manager:</p> <ul> <li> <p> <code>attachment</code> </p> </li> <li> <p> <code>connect-peer</code> </p> </li> <li> <p> <code>connection</code> </p> </li> <li> <p> <code>core-network</code> </p> </li> <li> <p> <code>device</code> </p> </li> <li> <p> <code>link</code> </p> </li> <li> <p> <code>peering</code> </p> </li> <li> <p> <code>site</code> </p> </li> </ul> <p>The following are the supported resource types for Amazon VPC:</p> <ul> <li> <p> <code>customer-gateway</code> </p> </li> <li> <p> <code>transit-gateway</code> </p> </li> <li> <p> <code>transit-gateway-attachment</code> </p> </li> <li> <p> <code>transit-gateway-connect-peer</code> </p> </li> <li> <p> <code>transit-gateway-route-table</code> </p> </li> <li> <p> <code>vpn-connection</code> </p> </li> </ul>
            resource_arn: <p>The ARN of the resource.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_network_resources_request.GetNetworkResourcesRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_network_resources_response.GetNetworkResourcesResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_network_resources

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_network_resources.get_network_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_network_resources_request.GetNetworkResourcesRequest = {
            "global_network_id": global_network_id
        }
        if core_network_id is not None:
            input_["core_network_id"] = core_network_id
        if registered_gateway_arn is not None:
            input_["registered_gateway_arn"] = registered_gateway_arn
        if aws_region is not None:
            input_["aws_region"] = aws_region
        if account_id is not None:
            input_["account_id"] = account_id
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
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

    def iter_get_network_resources(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        registered_gateway_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        aws_region: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        account_id: Optional[
            "capo_networkmanager.types.aws_account_id.AWSAccountId"
        ] = None,
        resource_type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        resource_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.network_resource.NetworkResource]":
        _token = next_token
        while True:
            _response = self.get_network_resources(
                global_network_id,
                config_overrides=config_overrides,
                core_network_id=core_network_id,
                registered_gateway_arn=registered_gateway_arn,
                aws_region=aws_region,
                account_id=account_id,
                resource_type=resource_type,
                resource_arn=resource_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("network_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_network_routes(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        route_table_identifier: "capo_networkmanager.types.route_table_identifier.RouteTableIdentifier",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        exact_cidr_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        longest_prefix_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        subnet_of_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        supernet_of_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        prefix_list_ids: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        states: Optional[
            "capo_networkmanager.types.route_state_list.RouteStateList"
        ] = None,
        types: Optional[
            "capo_networkmanager.types.route_type_list.RouteTypeList"
        ] = None,
        destination_filters: Optional[
            "capo_networkmanager.types.filter_map.FilterMap"
        ] = None,
    ) -> (
        "capo_networkmanager.types.get_network_routes_response.GetNetworkRoutesResponse"
    ):
        """<p>Gets the network routes of the specified global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            route_table_identifier: <p>The ID of the route table.</p>
            exact_cidr_matches: <p>An exact CIDR block.</p>
            longest_prefix_matches: <p>The most specific route that matches the traffic (longest prefix match).</p>
            subnet_of_matches: <p>The routes with a subnet that match the specified CIDR filter.</p>
            supernet_of_matches: <p>The routes with a CIDR that encompasses the CIDR filter. Example: If you specify 10.0.1.0/30, then the result returns 10.0.1.0/29.</p>
            prefix_list_ids: <p>The IDs of the prefix lists.</p>
            states: <p>The route states.</p>
            types: <p>The route types.</p>
            destination_filters: <p>Filter by route table destination. Possible Values: TRANSIT_GATEWAY_ATTACHMENT_ID, RESOURCE_ID, or RESOURCE_TYPE.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_network_routes_request.GetNetworkRoutesRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_network_routes_response.GetNetworkRoutesResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_network_routes

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_network_routes.get_network_routes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_network_routes_request.GetNetworkRoutesRequest = {
            "global_network_id": global_network_id,
            "route_table_identifier": route_table_identifier,
        }
        if exact_cidr_matches is not None:
            input_["exact_cidr_matches"] = exact_cidr_matches
        if longest_prefix_matches is not None:
            input_["longest_prefix_matches"] = longest_prefix_matches
        if subnet_of_matches is not None:
            input_["subnet_of_matches"] = subnet_of_matches
        if supernet_of_matches is not None:
            input_["supernet_of_matches"] = supernet_of_matches
        if prefix_list_ids is not None:
            input_["prefix_list_ids"] = prefix_list_ids
        if states is not None:
            input_["states"] = states
        if types is not None:
            input_["types"] = types
        if destination_filters is not None:
            input_["destination_filters"] = destination_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_network_telemetry(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        registered_gateway_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        aws_region: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        account_id: Optional[
            "capo_networkmanager.types.aws_account_id.AWSAccountId"
        ] = None,
        resource_type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        resource_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_network_telemetry_response.GetNetworkTelemetryResponse":
        """<p>Gets the network telemetry of the specified global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            core_network_id: <p>The ID of a core network.</p>
            registered_gateway_arn: <p>The ARN of the gateway.</p>
            aws_region: <p>The Amazon Web Services Region.</p>
            account_id: <p>The Amazon Web Services account ID.</p>
            resource_type: <p>The resource type. The following are the supported resource types:</p> <ul> <li> <p> <code>connect-peer</code> </p> </li> <li> <p> <code>transit-gateway-connect-peer</code> </p> </li> <li> <p> <code>vpn-connection</code> </p> </li> </ul>
            resource_arn: <p>The ARN of the resource.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_network_telemetry_request.GetNetworkTelemetryRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_network_telemetry_response.GetNetworkTelemetryResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_network_telemetry

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_network_telemetry.get_network_telemetry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_network_telemetry_request.GetNetworkTelemetryRequest = {
            "global_network_id": global_network_id
        }
        if core_network_id is not None:
            input_["core_network_id"] = core_network_id
        if registered_gateway_arn is not None:
            input_["registered_gateway_arn"] = registered_gateway_arn
        if aws_region is not None:
            input_["aws_region"] = aws_region
        if account_id is not None:
            input_["account_id"] = account_id
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
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

    def iter_get_network_telemetry(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        registered_gateway_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        aws_region: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        account_id: Optional[
            "capo_networkmanager.types.aws_account_id.AWSAccountId"
        ] = None,
        resource_type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        resource_arn: Optional[
            "capo_networkmanager.types.resource_arn.ResourceArn"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.network_telemetry.NetworkTelemetry]":
        _token = next_token
        while True:
            _response = self.get_network_telemetry(
                global_network_id,
                config_overrides=config_overrides,
                core_network_id=core_network_id,
                registered_gateway_arn=registered_gateway_arn,
                aws_region=aws_region,
                account_id=account_id,
                resource_type=resource_type,
                resource_arn=resource_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("network_telemetry",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_resource_policy(
        self,
        resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Returns information about a resource policy.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_resource_policy

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_route_analysis(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        route_analysis_id: "capo_networkmanager.types.constrained_string.ConstrainedString",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> (
        "capo_networkmanager.types.get_route_analysis_response.GetRouteAnalysisResponse"
    ):
        """<p>Gets information about the specified route analysis.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            route_analysis_id: <p>The ID of the route analysis.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_route_analysis_request.GetRouteAnalysisRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_route_analysis_response.GetRouteAnalysisResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_route_analysis

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_route_analysis.get_route_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_route_analysis_request.GetRouteAnalysisRequest = {
            "global_network_id": global_network_id,
            "route_analysis_id": route_analysis_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sites(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        site_ids: Optional["capo_networkmanager.types.site_id_list.SiteIdList"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_sites_response.GetSitesResponse":
        """<p>Gets information about one or more of your sites in a global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            site_ids: <p>One or more site IDs. The maximum is 10.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_sites_request.GetSitesRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_sites_response.GetSitesResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_sites

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_sites.get_sites(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_sites_request.GetSitesRequest = {
            "global_network_id": global_network_id
        }
        if site_ids is not None:
            input_["site_ids"] = site_ids
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

    def iter_get_sites(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        site_ids: Optional["capo_networkmanager.types.site_id_list.SiteIdList"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.site.Site]":
        _token = next_token
        while True:
            _response = self.get_sites(
                global_network_id,
                config_overrides=config_overrides,
                site_ids=site_ids,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sites",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_site_to_site_vpn_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.get_site_to_site_vpn_attachment_response.GetSiteToSiteVpnAttachmentResponse":
        """<p>Returns information about a site-to-site VPN attachment.</p>

        Args:
            attachment_id: <p>The ID of the attachment.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_site_to_site_vpn_attachment_request.GetSiteToSiteVpnAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_site_to_site_vpn_attachment_response.GetSiteToSiteVpnAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_site_to_site_vpn_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_site_to_site_vpn_attachment.get_site_to_site_vpn_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_site_to_site_vpn_attachment_request.GetSiteToSiteVpnAttachmentRequest = {
            "attachment_id": attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_transit_gateway_connect_peer_associations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        transit_gateway_connect_peer_arns: Optional[
            "capo_networkmanager.types.transit_gateway_connect_peer_arn_list.TransitGatewayConnectPeerArnList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_transit_gateway_connect_peer_associations_response.GetTransitGatewayConnectPeerAssociationsResponse":
        """<p>Gets information about one or more of your transit gateway Connect peer associations in a global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            transit_gateway_connect_peer_arns: <p>One or more transit gateway Connect peer Amazon Resource Names (ARNs).</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_transit_gateway_connect_peer_associations_request.GetTransitGatewayConnectPeerAssociationsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_transit_gateway_connect_peer_associations_response.GetTransitGatewayConnectPeerAssociationsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_transit_gateway_connect_peer_associations

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_transit_gateway_connect_peer_associations.get_transit_gateway_connect_peer_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_transit_gateway_connect_peer_associations_request.GetTransitGatewayConnectPeerAssociationsRequest = {
            "global_network_id": global_network_id
        }
        if transit_gateway_connect_peer_arns is not None:
            input_["transit_gateway_connect_peer_arns"] = (
                transit_gateway_connect_peer_arns
            )
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

    def iter_get_transit_gateway_connect_peer_associations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        transit_gateway_connect_peer_arns: Optional[
            "capo_networkmanager.types.transit_gateway_connect_peer_arn_list.TransitGatewayConnectPeerArnList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.transit_gateway_connect_peer_association.TransitGatewayConnectPeerAssociation]":
        _token = next_token
        while True:
            _response = self.get_transit_gateway_connect_peer_associations(
                global_network_id,
                config_overrides=config_overrides,
                transit_gateway_connect_peer_arns=transit_gateway_connect_peer_arns,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("transit_gateway_connect_peer_associations",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_transit_gateway_peering(
        self,
        peering_id: "capo_networkmanager.types.peering_id.PeeringId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.get_transit_gateway_peering_response.GetTransitGatewayPeeringResponse":
        """<p>Returns information about a transit gateway peer.</p>

        Args:
            peering_id: <p>The ID of the peering request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_transit_gateway_peering_request.GetTransitGatewayPeeringRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_transit_gateway_peering_response.GetTransitGatewayPeeringResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_transit_gateway_peering

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_transit_gateway_peering.get_transit_gateway_peering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_transit_gateway_peering_request.GetTransitGatewayPeeringRequest = {
            "peering_id": peering_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_transit_gateway_registrations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        transit_gateway_arns: Optional[
            "capo_networkmanager.types.transit_gateway_arn_list.TransitGatewayArnList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.get_transit_gateway_registrations_response.GetTransitGatewayRegistrationsResponse":
        """<p>Gets information about the transit gateway registrations in a specified global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            transit_gateway_arns: <p>The Amazon Resource Names (ARNs) of one or more transit gateways. The maximum is 10.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_transit_gateway_registrations_request.GetTransitGatewayRegistrationsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_transit_gateway_registrations_response.GetTransitGatewayRegistrationsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_transit_gateway_registrations

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_transit_gateway_registrations.get_transit_gateway_registrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_transit_gateway_registrations_request.GetTransitGatewayRegistrationsRequest = {
            "global_network_id": global_network_id
        }
        if transit_gateway_arns is not None:
            input_["transit_gateway_arns"] = transit_gateway_arns
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

    def iter_get_transit_gateway_registrations(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        transit_gateway_arns: Optional[
            "capo_networkmanager.types.transit_gateway_arn_list.TransitGatewayArnList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.transit_gateway_registration.TransitGatewayRegistration]":
        _token = next_token
        while True:
            _response = self.get_transit_gateway_registrations(
                global_network_id,
                config_overrides=config_overrides,
                transit_gateway_arns=transit_gateway_arns,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("transit_gateway_registrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_transit_gateway_route_table_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.get_transit_gateway_route_table_attachment_response.GetTransitGatewayRouteTableAttachmentResponse":
        """<p>Returns information about a transit gateway route table attachment.</p>

        Args:
            attachment_id: <p>The ID of the transit gateway route table attachment.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_transit_gateway_route_table_attachment_request.GetTransitGatewayRouteTableAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_transit_gateway_route_table_attachment_response.GetTransitGatewayRouteTableAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_transit_gateway_route_table_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_transit_gateway_route_table_attachment.get_transit_gateway_route_table_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_transit_gateway_route_table_attachment_request.GetTransitGatewayRouteTableAttachmentRequest = {
            "attachment_id": attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vpc_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> (
        "capo_networkmanager.types.get_vpc_attachment_response.GetVpcAttachmentResponse"
    ):
        """<p>Returns information about a VPC attachment.</p>

        Args:
            attachment_id: <p>The ID of the attachment.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.get_vpc_attachment_request.GetVpcAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.get_vpc_attachment_response.GetVpcAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.get_vpc_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.get_vpc_attachment.get_vpc_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.get_vpc_attachment_request.GetVpcAttachmentRequest = {
            "attachment_id": attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_attachment_routing_policy_associations(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        attachment_id: Optional[
            "capo_networkmanager.types.attachment_id.AttachmentId"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.list_attachment_routing_policy_associations_response.ListAttachmentRoutingPolicyAssociationsResponse":
        """<p>Lists the routing policy associations for attachments in a core network.</p>

        Args:
            core_network_id: <p>The ID of the core network to list attachment routing policy associations for.</p>
            attachment_id: <p>The ID of a specific attachment to filter the routing policy associations.</p>
            max_results: <p>The maximum number of results to return in a single page.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_attachment_routing_policy_associations_request.ListAttachmentRoutingPolicyAssociationsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_attachment_routing_policy_associations_response.ListAttachmentRoutingPolicyAssociationsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_attachment_routing_policy_associations

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_attachment_routing_policy_associations.list_attachment_routing_policy_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_attachment_routing_policy_associations_request.ListAttachmentRoutingPolicyAssociationsRequest = {
            "core_network_id": core_network_id
        }
        if attachment_id is not None:
            input_["attachment_id"] = attachment_id
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

    def iter_list_attachment_routing_policy_associations(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        attachment_id: Optional[
            "capo_networkmanager.types.attachment_id.AttachmentId"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.attachment_routing_policy_association_summary.AttachmentRoutingPolicyAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_attachment_routing_policy_associations(
                core_network_id,
                config_overrides=config_overrides,
                attachment_id=attachment_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("attachment_routing_policy_associations",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_attachments(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        attachment_type: Optional[
            "capo_networkmanager.types.attachment_type.AttachmentType"
        ] = None,
        edge_location: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        state: Optional[
            "capo_networkmanager.types.attachment_state.AttachmentState"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.list_attachments_response.ListAttachmentsResponse":
        """<p>Returns a list of core network attachments.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            attachment_type: <p>The type of attachment.</p>
            edge_location: <p>The Region where the edge is located.</p>
            state: <p>The state of the attachment.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_attachments_request.ListAttachmentsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_attachments_response.ListAttachmentsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_attachments

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_attachments.list_attachments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_attachments_request.ListAttachmentsRequest = {}
        if core_network_id is not None:
            input_["core_network_id"] = core_network_id
        if attachment_type is not None:
            input_["attachment_type"] = attachment_type
        if edge_location is not None:
            input_["edge_location"] = edge_location
        if state is not None:
            input_["state"] = state
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

    def iter_list_attachments(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        attachment_type: Optional[
            "capo_networkmanager.types.attachment_type.AttachmentType"
        ] = None,
        edge_location: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        state: Optional[
            "capo_networkmanager.types.attachment_state.AttachmentState"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.attachment.Attachment]":
        _token = next_token
        while True:
            _response = self.list_attachments(
                config_overrides=config_overrides,
                core_network_id=core_network_id,
                attachment_type=attachment_type,
                edge_location=edge_location,
                state=state,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("attachments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_connect_peers(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        connect_attachment_id: Optional[
            "capo_networkmanager.types.attachment_id.AttachmentId"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> (
        "capo_networkmanager.types.list_connect_peers_response.ListConnectPeersResponse"
    ):
        """<p>Returns a list of core network Connect peers.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            connect_attachment_id: <p>The ID of the attachment.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_connect_peers_request.ListConnectPeersRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_connect_peers_response.ListConnectPeersResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_connect_peers

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_connect_peers.list_connect_peers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_connect_peers_request.ListConnectPeersRequest = {}
        if core_network_id is not None:
            input_["core_network_id"] = core_network_id
        if connect_attachment_id is not None:
            input_["connect_attachment_id"] = connect_attachment_id
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

    def iter_list_connect_peers(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        connect_attachment_id: Optional[
            "capo_networkmanager.types.attachment_id.AttachmentId"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.connect_peer_summary.ConnectPeerSummary]":
        _token = next_token
        while True:
            _response = self.list_connect_peers(
                config_overrides=config_overrides,
                core_network_id=core_network_id,
                connect_attachment_id=connect_attachment_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("connect_peers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_core_network_policy_versions(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.list_core_network_policy_versions_response.ListCoreNetworkPolicyVersionsResponse":
        """<p>Returns a list of core network policy versions.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_core_network_policy_versions_request.ListCoreNetworkPolicyVersionsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_core_network_policy_versions_response.ListCoreNetworkPolicyVersionsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_core_network_policy_versions

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_core_network_policy_versions.list_core_network_policy_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_core_network_policy_versions_request.ListCoreNetworkPolicyVersionsRequest = {
            "core_network_id": core_network_id
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

    def iter_list_core_network_policy_versions(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.core_network_policy_version.CoreNetworkPolicyVersion]":
        _token = next_token
        while True:
            _response = self.list_core_network_policy_versions(
                core_network_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("core_network_policy_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_core_network_prefix_list_associations(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        prefix_list_arn: Optional[
            "capo_networkmanager.types.prefix_list_arn.PrefixListArn"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.list_core_network_prefix_list_associations_response.ListCoreNetworkPrefixListAssociationsResponse":
        """<p>Lists the prefix list associations for a core network.</p>

        Args:
            core_network_id: <p>The ID of the core network to list prefix list associations for.</p>
            prefix_list_arn: <p>The ARN of a specific prefix list to filter the associations.</p>
            max_results: <p>The maximum number of results to return in a single page.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_core_network_prefix_list_associations_request.ListCoreNetworkPrefixListAssociationsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_core_network_prefix_list_associations_response.ListCoreNetworkPrefixListAssociationsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_core_network_prefix_list_associations

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_core_network_prefix_list_associations.list_core_network_prefix_list_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_core_network_prefix_list_associations_request.ListCoreNetworkPrefixListAssociationsRequest = {
            "core_network_id": core_network_id
        }
        if prefix_list_arn is not None:
            input_["prefix_list_arn"] = prefix_list_arn
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

    def iter_list_core_network_prefix_list_associations(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        prefix_list_arn: Optional[
            "capo_networkmanager.types.prefix_list_arn.PrefixListArn"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.prefix_list_association.PrefixListAssociation]":
        _token = next_token
        while True:
            _response = self.list_core_network_prefix_list_associations(
                core_network_id,
                config_overrides=config_overrides,
                prefix_list_arn=prefix_list_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("prefix_list_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_core_network_routing_information(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        segment_name: "capo_networkmanager.types.constrained_string.ConstrainedString",
        edge_location: "capo_networkmanager.types.external_region_code.ExternalRegionCode",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        next_hop_filters: Optional[
            "capo_networkmanager.types.filter_map.FilterMap"
        ] = None,
        local_preference_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        exact_as_path_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        med_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        community_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.list_core_network_routing_information_response.ListCoreNetworkRoutingInformationResponse":
        """<p>Lists routing information for a core network, including routes and their attributes.</p>

        Args:
            core_network_id: <p>The ID of the core network to retrieve routing information for.</p>
            segment_name: <p>The name of the segment to filter routing information by.</p>
            edge_location: <p>The edge location to filter routing information by.</p>
            next_hop_filters: <p>Filters to apply based on next hop information.</p>
            local_preference_matches: <p>Local preference values to match when filtering routing information.</p>
            exact_as_path_matches: <p>Exact AS path values to match when filtering routing information.</p>
            med_matches: <p>Multi-Exit Discriminator (MED) values to match when filtering routing information.</p>
            community_matches: <p>BGP community values to match when filtering routing information.</p>
            max_results: <p>The maximum number of routing information entries to return in a single page.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_core_network_routing_information_request.ListCoreNetworkRoutingInformationRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_core_network_routing_information_response.ListCoreNetworkRoutingInformationResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_core_network_routing_information

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_core_network_routing_information.list_core_network_routing_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_core_network_routing_information_request.ListCoreNetworkRoutingInformationRequest = {
            "core_network_id": core_network_id,
            "segment_name": segment_name,
            "edge_location": edge_location,
        }
        if next_hop_filters is not None:
            input_["next_hop_filters"] = next_hop_filters
        if local_preference_matches is not None:
            input_["local_preference_matches"] = local_preference_matches
        if exact_as_path_matches is not None:
            input_["exact_as_path_matches"] = exact_as_path_matches
        if med_matches is not None:
            input_["med_matches"] = med_matches
        if community_matches is not None:
            input_["community_matches"] = community_matches
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

    def iter_list_core_network_routing_information(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        segment_name: "capo_networkmanager.types.constrained_string.ConstrainedString",
        edge_location: "capo_networkmanager.types.external_region_code.ExternalRegionCode",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        next_hop_filters: Optional[
            "capo_networkmanager.types.filter_map.FilterMap"
        ] = None,
        local_preference_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        exact_as_path_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        med_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        community_matches: Optional[
            "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
        ] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.core_network_routing_information.CoreNetworkRoutingInformation]":
        _token = next_token
        while True:
            _response = self.list_core_network_routing_information(
                core_network_id,
                segment_name,
                edge_location,
                config_overrides=config_overrides,
                next_hop_filters=next_hop_filters,
                local_preference_matches=local_preference_matches,
                exact_as_path_matches=exact_as_path_matches,
                med_matches=med_matches,
                community_matches=community_matches,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("core_network_routing_information",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_core_networks(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> (
        "capo_networkmanager.types.list_core_networks_response.ListCoreNetworksResponse"
    ):
        """<p>Returns a list of owned and shared core networks.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_core_networks_request.ListCoreNetworksRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_core_networks_response.ListCoreNetworksResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_core_networks

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_core_networks.list_core_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_core_networks_request.ListCoreNetworksRequest = {}
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

    def iter_list_core_networks(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.core_network_summary.CoreNetworkSummary]":
        _token = next_token
        while True:
            _response = self.list_core_networks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("core_networks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_organization_service_access_status(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.list_organization_service_access_status_response.ListOrganizationServiceAccessStatusResponse":
        """<p>Gets the status of the Service Linked Role (SLR) deployment for the accounts in a given Amazon Web Services Organization.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_organization_service_access_status_request.ListOrganizationServiceAccessStatusRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_organization_service_access_status_response.ListOrganizationServiceAccessStatusResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_organization_service_access_status

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_organization_service_access_status.list_organization_service_access_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_organization_service_access_status_request.ListOrganizationServiceAccessStatusRequest = {}
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

    def list_peerings(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        peering_type: Optional[
            "capo_networkmanager.types.peering_type.PeeringType"
        ] = None,
        edge_location: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        state: Optional["capo_networkmanager.types.peering_state.PeeringState"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "capo_networkmanager.types.list_peerings_response.ListPeeringsResponse":
        """<p>Lists the peerings for a core network.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            peering_type: <p>Returns a list of a peering requests.</p>
            edge_location: <p>Returns a list edge locations for the </p>
            state: <p>Returns a list of the peering request states.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_peerings_request.ListPeeringsRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_peerings_response.ListPeeringsResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_peerings

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_peerings.list_peerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_peerings_request.ListPeeringsRequest = {}
        if core_network_id is not None:
            input_["core_network_id"] = core_network_id
        if peering_type is not None:
            input_["peering_type"] = peering_type
        if edge_location is not None:
            input_["edge_location"] = edge_location
        if state is not None:
            input_["state"] = state
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

    def iter_list_peerings(
        self,
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        core_network_id: Optional[
            "capo_networkmanager.types.core_network_id.CoreNetworkId"
        ] = None,
        peering_type: Optional[
            "capo_networkmanager.types.peering_type.PeeringType"
        ] = None,
        edge_location: Optional[
            "capo_networkmanager.types.external_region_code.ExternalRegionCode"
        ] = None,
        state: Optional["capo_networkmanager.types.peering_state.PeeringState"] = None,
        max_results: Optional[
            "capo_networkmanager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_networkmanager.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_networkmanager.types.peering.Peering]":
        _token = next_token
        while True:
            _response = self.list_peerings(
                config_overrides=config_overrides,
                core_network_id=core_network_id,
                peering_type=peering_type,
                edge_location=edge_location,
                state=state,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("peerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_networkmanager._operations.network_manager.list_tags_for_resource

            output, http_response = (
                capo_networkmanager._operations.network_manager.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_attachment_routing_policy_label(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        routing_policy_label: "capo_networkmanager.types.constrained_string.ConstrainedString",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.put_attachment_routing_policy_label_response.PutAttachmentRoutingPolicyLabelResponse":
        """<p>Applies a routing policy label to an attachment for traffic routing decisions.</p>

        Args:
            core_network_id: <p>The ID of the core network containing the attachment.</p>
            attachment_id: <p>The ID of the attachment to apply the routing policy label to.</p>
            routing_policy_label: <p>The routing policy label to apply to the attachment.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.put_attachment_routing_policy_label_request.PutAttachmentRoutingPolicyLabelRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.put_attachment_routing_policy_label_response.PutAttachmentRoutingPolicyLabelResponse"
        ]:
            import capo_networkmanager._operations.network_manager.put_attachment_routing_policy_label

            output, http_response = (
                capo_networkmanager._operations.network_manager.put_attachment_routing_policy_label.put_attachment_routing_policy_label(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.put_attachment_routing_policy_label_request.PutAttachmentRoutingPolicyLabelRequest = {
            "core_network_id": core_network_id,
            "attachment_id": attachment_id,
            "routing_policy_label": routing_policy_label,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_core_network_policy(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        policy_document: "capo_networkmanager.types.synthesized_json_core_network_policy_document.SynthesizedJsonCoreNetworkPolicyDocument",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        latest_version_id: Optional["capo_networkmanager.types.integer.Integer"] = None,
        client_token: Optional[
            "capo_networkmanager.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_networkmanager.types.put_core_network_policy_response.PutCoreNetworkPolicyResponse":
        """<p>Creates a new, immutable version of a core network policy. A subsequent change set is created showing the differences between the LIVE policy and the submitted policy.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            policy_document: <p>The policy document.</p>
            description: <p>a core network policy description.</p>
            latest_version_id: <p>The ID of a core network policy. </p>
            client_token: <p>The client token associated with the request.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.core_network_policy_exception.CoreNetworkPolicyException: <p>Describes a core network policy exception.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.put_core_network_policy_request.PutCoreNetworkPolicyRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.put_core_network_policy_response.PutCoreNetworkPolicyResponse"
        ]:
            import capo_networkmanager._operations.network_manager.put_core_network_policy

            output, http_response = (
                capo_networkmanager._operations.network_manager.put_core_network_policy.put_core_network_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.put_core_network_policy_request.PutCoreNetworkPolicyRequest = {
            "core_network_id": core_network_id,
            "policy_document": policy_document,
        }
        if description is not None:
            input_["description"] = description
        if latest_version_id is not None:
            input_["latest_version_id"] = latest_version_id
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        policy_document: "capo_networkmanager.types.synthesized_json_resource_policy_document.SynthesizedJsonResourcePolicyDocument",
        resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates or updates a resource policy.</p>

        Args:
            policy_document: <p>The JSON resource policy document.</p>
            resource_arn: <p>The ARN of the resource policy. </p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_networkmanager._operations.network_manager.put_resource_policy

            output, http_response = (
                capo_networkmanager._operations.network_manager.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "policy_document": policy_document,
            "resource_arn": resource_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_transit_gateway(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        transit_gateway_arn: "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.register_transit_gateway_response.RegisterTransitGatewayResponse":
        """<p>Registers a transit gateway in your global network. Not all Regions support transit gateways for global networks. For a list of the supported Regions, see <a href="https://docs.aws.amazon.com/network-manager/latest/tgwnm/what-are-global-networks.html#nm-available-regions">Region Availability</a> in the <i>Amazon Web Services Transit Gateways for Global Networks User Guide</i>. The transit gateway can be in any of the supported Amazon Web Services Regions, but it must be owned by the same Amazon Web Services account that owns the global network. You cannot register a transit gateway in more than one global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            transit_gateway_arn: <p>The Amazon Resource Name (ARN) of the transit gateway.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.register_transit_gateway_request.RegisterTransitGatewayRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.register_transit_gateway_response.RegisterTransitGatewayResponse"
        ]:
            import capo_networkmanager._operations.network_manager.register_transit_gateway

            output, http_response = (
                capo_networkmanager._operations.network_manager.register_transit_gateway.register_transit_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.register_transit_gateway_request.RegisterTransitGatewayRequest = {
            "global_network_id": global_network_id,
            "transit_gateway_arn": transit_gateway_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> (
        "capo_networkmanager.types.reject_attachment_response.RejectAttachmentResponse"
    ):
        """<p>Rejects a core network attachment request.</p>

        Args:
            attachment_id: <p>The ID of the attachment.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.reject_attachment_request.RejectAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.reject_attachment_response.RejectAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.reject_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.reject_attachment.reject_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.reject_attachment_request.RejectAttachmentRequest = {
            "attachment_id": attachment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_attachment_routing_policy_label(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.remove_attachment_routing_policy_label_response.RemoveAttachmentRoutingPolicyLabelResponse":
        """<p>Removes a routing policy label from an attachment.</p>

        Args:
            core_network_id: <p>The ID of the core network containing the attachment.</p>
            attachment_id: <p>The ID of the attachment to remove the routing policy label from.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.remove_attachment_routing_policy_label_request.RemoveAttachmentRoutingPolicyLabelRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.remove_attachment_routing_policy_label_response.RemoveAttachmentRoutingPolicyLabelResponse"
        ]:
            import capo_networkmanager._operations.network_manager.remove_attachment_routing_policy_label

            output, http_response = (
                capo_networkmanager._operations.network_manager.remove_attachment_routing_policy_label.remove_attachment_routing_policy_label(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.remove_attachment_routing_policy_label_request.RemoveAttachmentRoutingPolicyLabelRequest = {
            "core_network_id": core_network_id,
            "attachment_id": attachment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_core_network_policy_version(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        policy_version_id: "capo_networkmanager.types.integer.Integer",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.restore_core_network_policy_version_response.RestoreCoreNetworkPolicyVersionResponse":
        """<p>Restores a previous policy version as a new, immutable version of a core network policy. A subsequent change set is created showing the differences between the LIVE policy and restored policy.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            policy_version_id: <p>The ID of the policy version to restore.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.restore_core_network_policy_version_request.RestoreCoreNetworkPolicyVersionRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.restore_core_network_policy_version_response.RestoreCoreNetworkPolicyVersionResponse"
        ]:
            import capo_networkmanager._operations.network_manager.restore_core_network_policy_version

            output, http_response = (
                capo_networkmanager._operations.network_manager.restore_core_network_policy_version.restore_core_network_policy_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.restore_core_network_policy_version_request.RestoreCoreNetworkPolicyVersionRequest = {
            "core_network_id": core_network_id,
            "policy_version_id": policy_version_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_organization_service_access_update(
        self,
        action: "capo_networkmanager.types.action.Action",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.start_organization_service_access_update_response.StartOrganizationServiceAccessUpdateResponse":
        """<p>Enables the Network Manager service for an Amazon Web Services Organization. This can only be called by a management account within the organization. </p>

        Args:
            action: <p>The action to take for the update request. This can be either <code>ENABLE</code> or <code>DISABLE</code>.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.start_organization_service_access_update_request.StartOrganizationServiceAccessUpdateRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.start_organization_service_access_update_response.StartOrganizationServiceAccessUpdateResponse"
        ]:
            import capo_networkmanager._operations.network_manager.start_organization_service_access_update

            output, http_response = (
                capo_networkmanager._operations.network_manager.start_organization_service_access_update.start_organization_service_access_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.start_organization_service_access_update_request.StartOrganizationServiceAccessUpdateRequest = {
            "action": action
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_route_analysis(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        source: "capo_networkmanager.types.route_analysis_endpoint_options_specification.RouteAnalysisEndpointOptionsSpecification",
        destination: "capo_networkmanager.types.route_analysis_endpoint_options_specification.RouteAnalysisEndpointOptionsSpecification",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        include_return_path: Optional[
            "capo_networkmanager.types.boolean.Boolean"
        ] = None,
        use_middleboxes: Optional["capo_networkmanager.types.boolean.Boolean"] = None,
    ) -> "capo_networkmanager.types.start_route_analysis_response.StartRouteAnalysisResponse":
        """<p>Starts analyzing the routing path between the specified source and destination. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/tgw/route-analyzer.html">Route Analyzer</a>.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            source: <p>The source from which traffic originates.</p>
            destination: <p>The destination.</p>
            include_return_path: <p>Indicates whether to analyze the return path. The default is <code>false</code>.</p>
            use_middleboxes: <p>Indicates whether to include the location of middlebox appliances in the route analysis. The default is <code>false</code>.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.start_route_analysis_request.StartRouteAnalysisRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.start_route_analysis_response.StartRouteAnalysisResponse"
        ]:
            import capo_networkmanager._operations.network_manager.start_route_analysis

            output, http_response = (
                capo_networkmanager._operations.network_manager.start_route_analysis.start_route_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.start_route_analysis_request.StartRouteAnalysisRequest = {
            "global_network_id": global_network_id,
            "source": source,
            "destination": destination,
        }
        if include_return_path is not None:
            input_["include_return_path"] = include_return_path
        if use_middleboxes is not None:
            input_["use_middleboxes"] = use_middleboxes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn",
        tags: "capo_networkmanager.types.tag_list.TagList",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags to apply to the specified resource.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_networkmanager._operations.network_manager.tag_resource

            output, http_response = (
                capo_networkmanager._operations.network_manager.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn",
        tag_keys: "capo_networkmanager.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys to remove from the specified resource.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_networkmanager._operations.network_manager.untag_resource

            output, http_response = (
                capo_networkmanager._operations.network_manager.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.untag_resource_request.UntagResourceRequest = {
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

    def update_connection(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        connection_id: "capo_networkmanager.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        link_id: Optional["capo_networkmanager.types.link_id.LinkId"] = None,
        connected_link_id: Optional["capo_networkmanager.types.link_id.LinkId"] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
    ) -> (
        "capo_networkmanager.types.update_connection_response.UpdateConnectionResponse"
    ):
        """<p>Updates the information for an existing connection. To remove information for any of the parameters, specify an empty string.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            connection_id: <p>The ID of the connection.</p>
            link_id: <p>The ID of the link for the first device in the connection.</p>
            connected_link_id: <p>The ID of the link for the second device in the connection.</p>
            description: <p>A description of the connection.</p> <p>Length Constraints: Maximum length of 256 characters.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.update_connection_request.UpdateConnectionRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.update_connection_response.UpdateConnectionResponse"
        ]:
            import capo_networkmanager._operations.network_manager.update_connection

            output, http_response = (
                capo_networkmanager._operations.network_manager.update_connection.update_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.update_connection_request.UpdateConnectionRequest = {
            "global_network_id": global_network_id,
            "connection_id": connection_id,
        }
        if link_id is not None:
            input_["link_id"] = link_id
        if connected_link_id is not None:
            input_["connected_link_id"] = connected_link_id
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_core_network(
        self,
        core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
    ) -> "capo_networkmanager.types.update_core_network_response.UpdateCoreNetworkResponse":
        """<p>Updates the description of a core network.</p>

        Args:
            core_network_id: <p>The ID of a core network.</p>
            description: <p>The description of the update.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.update_core_network_request.UpdateCoreNetworkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.update_core_network_response.UpdateCoreNetworkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.update_core_network

            output, http_response = (
                capo_networkmanager._operations.network_manager.update_core_network.update_core_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.update_core_network_request.UpdateCoreNetworkRequest = {
            "core_network_id": core_network_id
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_device(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        device_id: "capo_networkmanager.types.device_id.DeviceId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        aws_location: Optional[
            "capo_networkmanager.types.aws_location.AWSLocation"
        ] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        vendor: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        model: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        serial_number: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        location: Optional["capo_networkmanager.types.location.Location"] = None,
        site_id: Optional["capo_networkmanager.types.site_id.SiteId"] = None,
    ) -> "capo_networkmanager.types.update_device_response.UpdateDeviceResponse":
        """<p>Updates the details for an existing device. To remove information for any of the parameters, specify an empty string.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            device_id: <p>The ID of the device.</p>
            aws_location: <p>The Amazon Web Services location of the device, if applicable. For an on-premises device, you can omit this parameter.</p>
            description: <p>A description of the device.</p> <p>Constraints: Maximum length of 256 characters.</p>
            type: <p>The type of the device.</p>
            vendor: <p>The vendor of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>
            model: <p>The model of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>
            serial_number: <p>The serial number of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>
            site_id: <p>The ID of the site.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.update_device_request.UpdateDeviceRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.update_device_response.UpdateDeviceResponse"
        ]:
            import capo_networkmanager._operations.network_manager.update_device

            output, http_response = (
                capo_networkmanager._operations.network_manager.update_device.update_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.update_device_request.UpdateDeviceRequest = {
            "global_network_id": global_network_id,
            "device_id": device_id,
        }
        if aws_location is not None:
            input_["aws_location"] = aws_location
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if vendor is not None:
            input_["vendor"] = vendor
        if model is not None:
            input_["model"] = model
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if location is not None:
            input_["location"] = location
        if site_id is not None:
            input_["site_id"] = site_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_direct_connect_gateway_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        edge_locations: Optional[
            "capo_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
        ] = None,
    ) -> "capo_networkmanager.types.update_direct_connect_gateway_attachment_response.UpdateDirectConnectGatewayAttachmentResponse":
        """<p>Updates the edge locations associated with an Amazon Web Services Direct Connect gateway attachment. </p>

        Args:
            attachment_id: <p>The ID of the Direct Connect gateway attachment for the updated edge locations. </p>
            edge_locations: <p>One or more edge locations to update for the Direct Connect gateway attachment. The updated array of edge locations overwrites the previous array of locations. <code>EdgeLocations</code> is only used for Direct Connect gateway attachments.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.update_direct_connect_gateway_attachment_request.UpdateDirectConnectGatewayAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.update_direct_connect_gateway_attachment_response.UpdateDirectConnectGatewayAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.update_direct_connect_gateway_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.update_direct_connect_gateway_attachment.update_direct_connect_gateway_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.update_direct_connect_gateway_attachment_request.UpdateDirectConnectGatewayAttachmentRequest = {
            "attachment_id": attachment_id
        }
        if edge_locations is not None:
            input_["edge_locations"] = edge_locations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_global_network(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
    ) -> "capo_networkmanager.types.update_global_network_response.UpdateGlobalNetworkResponse":
        """<p>Updates an existing global network. To remove information for any of the parameters, specify an empty string.</p>

        Args:
            global_network_id: <p>The ID of your global network.</p>
            description: <p>A description of the global network.</p> <p>Constraints: Maximum length of 256 characters.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.update_global_network_request.UpdateGlobalNetworkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.update_global_network_response.UpdateGlobalNetworkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.update_global_network

            output, http_response = (
                capo_networkmanager._operations.network_manager.update_global_network.update_global_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.update_global_network_request.UpdateGlobalNetworkRequest = {
            "global_network_id": global_network_id
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_link(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        link_id: "capo_networkmanager.types.link_id.LinkId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        type: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        bandwidth: Optional["capo_networkmanager.types.bandwidth.Bandwidth"] = None,
        provider: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
    ) -> "capo_networkmanager.types.update_link_response.UpdateLinkResponse":
        """<p>Updates the details for an existing link. To remove information for any of the parameters, specify an empty string.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            link_id: <p>The ID of the link.</p>
            description: <p>A description of the link.</p> <p>Constraints: Maximum length of 256 characters.</p>
            type: <p>The type of the link.</p> <p>Constraints: Maximum length of 128 characters.</p>
            bandwidth: <p>The upload and download speed in Mbps. </p>
            provider: <p>The provider of the link.</p> <p>Constraints: Maximum length of 128 characters.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service limit was exceeded.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.update_link_request.UpdateLinkRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.update_link_response.UpdateLinkResponse"
        ]:
            import capo_networkmanager._operations.network_manager.update_link

            output, http_response = (
                capo_networkmanager._operations.network_manager.update_link.update_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.update_link_request.UpdateLinkRequest = {
            "global_network_id": global_network_id,
            "link_id": link_id,
        }
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if bandwidth is not None:
            input_["bandwidth"] = bandwidth
        if provider is not None:
            input_["provider"] = provider

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_network_resource_metadata(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn",
        metadata: "capo_networkmanager.types.network_resource_metadata_map.NetworkResourceMetadataMap",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
    ) -> "capo_networkmanager.types.update_network_resource_metadata_response.UpdateNetworkResourceMetadataResponse":
        """<p>Updates the resource metadata for the specified global network.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            resource_arn: <p>The ARN of the resource.</p>
            metadata: <p>The resource metadata.</p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.update_network_resource_metadata_request.UpdateNetworkResourceMetadataRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.update_network_resource_metadata_response.UpdateNetworkResourceMetadataResponse"
        ]:
            import capo_networkmanager._operations.network_manager.update_network_resource_metadata

            output, http_response = (
                capo_networkmanager._operations.network_manager.update_network_resource_metadata.update_network_resource_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.update_network_resource_metadata_request.UpdateNetworkResourceMetadataRequest = {
            "global_network_id": global_network_id,
            "resource_arn": resource_arn,
            "metadata": metadata,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_site(
        self,
        global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId",
        site_id: "capo_networkmanager.types.site_id.SiteId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        description: Optional[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ] = None,
        location: Optional["capo_networkmanager.types.location.Location"] = None,
    ) -> "capo_networkmanager.types.update_site_response.UpdateSiteResponse":
        """<p>Updates the information for an existing site. To remove information for any of the parameters, specify an empty string.</p>

        Args:
            global_network_id: <p>The ID of the global network.</p>
            site_id: <p>The ID of your site.</p>
            description: <p>A description of your site.</p> <p>Constraints: Maximum length of 256 characters.</p>
            location: <p>The site location:</p> <ul> <li> <p> <code>Address</code>: The physical address of the site.</p> </li> <li> <p> <code>Latitude</code>: The latitude of the site. </p> </li> <li> <p> <code>Longitude</code>: The longitude of the site.</p> </li> </ul>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.update_site_request.UpdateSiteRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.update_site_response.UpdateSiteResponse"
        ]:
            import capo_networkmanager._operations.network_manager.update_site

            output, http_response = (
                capo_networkmanager._operations.network_manager.update_site.update_site(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.update_site_request.UpdateSiteRequest = {
            "global_network_id": global_network_id,
            "site_id": site_id,
        }
        if description is not None:
            input_["description"] = description
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_vpc_attachment(
        self,
        attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[NetworkManagerClientConfig] = None,
        add_subnet_arns: Optional[
            "capo_networkmanager.types.subnet_arn_list.SubnetArnList"
        ] = None,
        remove_subnet_arns: Optional[
            "capo_networkmanager.types.subnet_arn_list.SubnetArnList"
        ] = None,
        options: Optional["capo_networkmanager.types.vpc_options.VpcOptions"] = None,
    ) -> "capo_networkmanager.types.update_vpc_attachment_response.UpdateVpcAttachmentResponse":
        """<p>Updates a VPC attachment.</p>

        Args:
            attachment_id: <p>The ID of the attachment.</p>
            add_subnet_arns: <p>Adds a subnet ARN to the VPC attachment.</p>
            remove_subnet_arns: <p>Removes a subnet ARN from the attachment.</p>
            options: <p>Additional options for updating the VPC attachment. </p>

        Raises:
            capo_networkmanager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmanager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.</p>
            capo_networkmanager.errors.internal_server_exception.InternalServerException: <p>The request has failed due to an internal error.</p>
            capo_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_networkmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkmanager.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints.</p>
            capo_networkmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmanager.types.update_vpc_attachment_request.UpdateVpcAttachmentRequest]",
        ) -> OperationResponse[
            "capo_networkmanager.types.update_vpc_attachment_response.UpdateVpcAttachmentResponse"
        ]:
            import capo_networkmanager._operations.network_manager.update_vpc_attachment

            output, http_response = (
                capo_networkmanager._operations.network_manager.update_vpc_attachment.update_vpc_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkmanager.types.update_vpc_attachment_request.UpdateVpcAttachmentRequest = {
            "attachment_id": attachment_id
        }
        if add_subnet_arns is not None:
            input_["add_subnet_arns"] = add_subnet_arns
        if remove_subnet_arns is not None:
            input_["remove_subnet_arns"] = remove_subnet_arns
        if options is not None:
            input_["options"] = options

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
