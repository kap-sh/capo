"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaConnect``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_mediaconnect._auth._signers
import capo_mediaconnect._auth._sigv4
from capo_mediaconnect._auth._identity import Credentials
from capo_mediaconnect._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mediaconnect._auth._zapros_handler import AuthMiddleware
from capo_mediaconnect._pagination import resolve_path as _resolve_path
from capo_mediaconnect._resources.media_connect.bridge_resource import BridgeResource
from capo_mediaconnect._resources.media_connect.entitlement_resource import (
    EntitlementResource,
)
from capo_mediaconnect._resources.media_connect.flow_media_stream_resource import (
    FlowMediaStreamResource,
)
from capo_mediaconnect._resources.media_connect.flow_output_resource import (
    FlowOutputResource,
)
from capo_mediaconnect._resources.media_connect.flow_resource import FlowResource
from capo_mediaconnect._resources.media_connect.flow_source_resource import (
    FlowSourceResource,
)
from capo_mediaconnect._resources.media_connect.flow_vpc_interface_resource import (
    FlowVpcInterfaceResource,
)
from capo_mediaconnect._resources.media_connect.gateway_instance_resource import (
    GatewayInstanceResource,
)
from capo_mediaconnect._resources.media_connect.gateway_resource import GatewayResource
from capo_mediaconnect._resources.media_connect.offering_resource import (
    OfferingResource,
)
from capo_mediaconnect._resources.media_connect.reservation_resource import (
    ReservationResource,
)
from capo_mediaconnect._resources.media_connect.router_input_resource import (
    RouterInputResource,
)
from capo_mediaconnect._resources.media_connect.router_network_interface_resource import (
    RouterNetworkInterfaceResource,
)
from capo_mediaconnect._resources.media_connect.router_output_resource import (
    RouterOutputResource,
)
from capo_mediaconnect._services._aws_config import aws_config
from capo_mediaconnect._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_add_bridge_output_request
    import capo_mediaconnect.types.__list_of_add_bridge_source_request
    import capo_mediaconnect.types.__list_of_add_media_stream_request
    import capo_mediaconnect.types.__list_of_add_output_request
    import capo_mediaconnect.types.__list_of_gateway_network
    import capo_mediaconnect.types.__list_of_grant_entitlement_request
    import capo_mediaconnect.types.__list_of_media_stream_output_configuration_request
    import capo_mediaconnect.types.__list_of_media_stream_source_configuration_request
    import capo_mediaconnect.types.__list_of_set_source_request
    import capo_mediaconnect.types.__list_of_string
    import capo_mediaconnect.types.__list_of_vpc_interface_request
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.add_bridge_outputs_request
    import capo_mediaconnect.types.add_bridge_outputs_response
    import capo_mediaconnect.types.add_bridge_sources_request
    import capo_mediaconnect.types.add_bridge_sources_response
    import capo_mediaconnect.types.add_egress_gateway_bridge_request
    import capo_mediaconnect.types.add_flow_media_streams_request
    import capo_mediaconnect.types.add_flow_media_streams_response
    import capo_mediaconnect.types.add_flow_outputs_request
    import capo_mediaconnect.types.add_flow_outputs_response
    import capo_mediaconnect.types.add_flow_sources_request
    import capo_mediaconnect.types.add_flow_sources_response
    import capo_mediaconnect.types.add_flow_vpc_interfaces_request
    import capo_mediaconnect.types.add_flow_vpc_interfaces_response
    import capo_mediaconnect.types.add_ingress_gateway_bridge_request
    import capo_mediaconnect.types.add_maintenance
    import capo_mediaconnect.types.batch_get_router_input_request
    import capo_mediaconnect.types.batch_get_router_input_response
    import capo_mediaconnect.types.batch_get_router_network_interface_request
    import capo_mediaconnect.types.batch_get_router_network_interface_response
    import capo_mediaconnect.types.batch_get_router_output_request
    import capo_mediaconnect.types.batch_get_router_output_response
    import capo_mediaconnect.types.bridge_arn
    import capo_mediaconnect.types.bridge_placement
    import capo_mediaconnect.types.client_token
    import capo_mediaconnect.types.create_bridge_request
    import capo_mediaconnect.types.create_bridge_response
    import capo_mediaconnect.types.create_flow_request
    import capo_mediaconnect.types.create_flow_response
    import capo_mediaconnect.types.create_gateway_request
    import capo_mediaconnect.types.create_gateway_response
    import capo_mediaconnect.types.create_router_input_request
    import capo_mediaconnect.types.create_router_input_response
    import capo_mediaconnect.types.create_router_network_interface_request
    import capo_mediaconnect.types.create_router_network_interface_response
    import capo_mediaconnect.types.create_router_output_request
    import capo_mediaconnect.types.create_router_output_response
    import capo_mediaconnect.types.delete_bridge_request
    import capo_mediaconnect.types.delete_bridge_response
    import capo_mediaconnect.types.delete_flow_request
    import capo_mediaconnect.types.delete_flow_response
    import capo_mediaconnect.types.delete_gateway_request
    import capo_mediaconnect.types.delete_gateway_response
    import capo_mediaconnect.types.delete_router_input_request
    import capo_mediaconnect.types.delete_router_input_response
    import capo_mediaconnect.types.delete_router_network_interface_request
    import capo_mediaconnect.types.delete_router_network_interface_response
    import capo_mediaconnect.types.delete_router_output_request
    import capo_mediaconnect.types.delete_router_output_response
    import capo_mediaconnect.types.deregister_gateway_instance_request
    import capo_mediaconnect.types.deregister_gateway_instance_response
    import capo_mediaconnect.types.describe_bridge_request
    import capo_mediaconnect.types.describe_bridge_response
    import capo_mediaconnect.types.describe_flow_request
    import capo_mediaconnect.types.describe_flow_response
    import capo_mediaconnect.types.describe_flow_source_metadata_request
    import capo_mediaconnect.types.describe_flow_source_metadata_response
    import capo_mediaconnect.types.describe_flow_source_thumbnail_request
    import capo_mediaconnect.types.describe_flow_source_thumbnail_response
    import capo_mediaconnect.types.describe_gateway_instance_request
    import capo_mediaconnect.types.describe_gateway_instance_response
    import capo_mediaconnect.types.describe_gateway_request
    import capo_mediaconnect.types.describe_gateway_response
    import capo_mediaconnect.types.describe_offering_request
    import capo_mediaconnect.types.describe_offering_response
    import capo_mediaconnect.types.describe_reservation_request
    import capo_mediaconnect.types.describe_reservation_response
    import capo_mediaconnect.types.desired_state
    import capo_mediaconnect.types.encoding_config
    import capo_mediaconnect.types.entitlement_status
    import capo_mediaconnect.types.fabric_configuration
    import capo_mediaconnect.types.failover_config
    import capo_mediaconnect.types.flow_arn
    import capo_mediaconnect.types.flow_size
    import capo_mediaconnect.types.flow_transit_encryption
    import capo_mediaconnect.types.gateway_arn
    import capo_mediaconnect.types.gateway_instance_arn
    import capo_mediaconnect.types.get_router_input_request
    import capo_mediaconnect.types.get_router_input_response
    import capo_mediaconnect.types.get_router_input_source_metadata_request
    import capo_mediaconnect.types.get_router_input_source_metadata_response
    import capo_mediaconnect.types.get_router_input_thumbnail_request
    import capo_mediaconnect.types.get_router_input_thumbnail_response
    import capo_mediaconnect.types.get_router_network_interface_request
    import capo_mediaconnect.types.get_router_network_interface_response
    import capo_mediaconnect.types.get_router_output_request
    import capo_mediaconnect.types.get_router_output_response
    import capo_mediaconnect.types.grant_flow_entitlements_request
    import capo_mediaconnect.types.grant_flow_entitlements_response
    import capo_mediaconnect.types.list_bridges_request
    import capo_mediaconnect.types.list_bridges_response
    import capo_mediaconnect.types.list_entitlements_request
    import capo_mediaconnect.types.list_entitlements_response
    import capo_mediaconnect.types.list_flows_request
    import capo_mediaconnect.types.list_flows_response
    import capo_mediaconnect.types.list_gateway_instances_request
    import capo_mediaconnect.types.list_gateway_instances_response
    import capo_mediaconnect.types.list_gateways_request
    import capo_mediaconnect.types.list_gateways_response
    import capo_mediaconnect.types.list_offerings_request
    import capo_mediaconnect.types.list_offerings_response
    import capo_mediaconnect.types.list_reservations_request
    import capo_mediaconnect.types.list_reservations_response
    import capo_mediaconnect.types.list_router_inputs_request
    import capo_mediaconnect.types.list_router_inputs_response
    import capo_mediaconnect.types.list_router_network_interfaces_request
    import capo_mediaconnect.types.list_router_network_interfaces_response
    import capo_mediaconnect.types.list_router_outputs_request
    import capo_mediaconnect.types.list_router_outputs_response
    import capo_mediaconnect.types.list_tags_for_global_resource_request
    import capo_mediaconnect.types.list_tags_for_global_resource_response
    import capo_mediaconnect.types.list_tags_for_resource_request
    import capo_mediaconnect.types.list_tags_for_resource_response
    import capo_mediaconnect.types.listed_bridge
    import capo_mediaconnect.types.listed_entitlement
    import capo_mediaconnect.types.listed_flow
    import capo_mediaconnect.types.listed_gateway
    import capo_mediaconnect.types.listed_gateway_instance
    import capo_mediaconnect.types.listed_router_input
    import capo_mediaconnect.types.listed_router_network_interface
    import capo_mediaconnect.types.listed_router_output
    import capo_mediaconnect.types.maintenance_configuration
    import capo_mediaconnect.types.max_results
    import capo_mediaconnect.types.media_stream_attributes_request
    import capo_mediaconnect.types.media_stream_type
    import capo_mediaconnect.types.monitoring_config
    import capo_mediaconnect.types.ndi_config
    import capo_mediaconnect.types.ndi_output_timecode_source
    import capo_mediaconnect.types.ndi_source_settings
    import capo_mediaconnect.types.offering
    import capo_mediaconnect.types.offering_arn
    import capo_mediaconnect.types.output_status
    import capo_mediaconnect.types.protocol
    import capo_mediaconnect.types.purchase_offering_request
    import capo_mediaconnect.types.purchase_offering_response
    import capo_mediaconnect.types.remove_bridge_output_request
    import capo_mediaconnect.types.remove_bridge_output_response
    import capo_mediaconnect.types.remove_bridge_source_request
    import capo_mediaconnect.types.remove_bridge_source_response
    import capo_mediaconnect.types.remove_flow_media_stream_request
    import capo_mediaconnect.types.remove_flow_media_stream_response
    import capo_mediaconnect.types.remove_flow_output_request
    import capo_mediaconnect.types.remove_flow_output_response
    import capo_mediaconnect.types.remove_flow_source_request
    import capo_mediaconnect.types.remove_flow_source_response
    import capo_mediaconnect.types.remove_flow_vpc_interface_request
    import capo_mediaconnect.types.remove_flow_vpc_interface_response
    import capo_mediaconnect.types.reservation
    import capo_mediaconnect.types.reservation_arn
    import capo_mediaconnect.types.restart_router_input_request
    import capo_mediaconnect.types.restart_router_input_response
    import capo_mediaconnect.types.restart_router_output_request
    import capo_mediaconnect.types.restart_router_output_response
    import capo_mediaconnect.types.revoke_flow_entitlement_request
    import capo_mediaconnect.types.revoke_flow_entitlement_response
    import capo_mediaconnect.types.router_content_quality_analysis_configuration
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_arn_list
    import capo_mediaconnect.types.router_input_configuration
    import capo_mediaconnect.types.router_input_filter_list
    import capo_mediaconnect.types.router_input_tier
    import capo_mediaconnect.types.router_input_transit_encryption
    import capo_mediaconnect.types.router_network_interface_arn
    import capo_mediaconnect.types.router_network_interface_arn_list
    import capo_mediaconnect.types.router_network_interface_configuration
    import capo_mediaconnect.types.router_network_interface_filter_list
    import capo_mediaconnect.types.router_output_arn
    import capo_mediaconnect.types.router_output_arn_list
    import capo_mediaconnect.types.router_output_configuration
    import capo_mediaconnect.types.router_output_filter_list
    import capo_mediaconnect.types.router_output_tier
    import capo_mediaconnect.types.routing_scope
    import capo_mediaconnect.types.set_source_request
    import capo_mediaconnect.types.start_flow_request
    import capo_mediaconnect.types.start_flow_response
    import capo_mediaconnect.types.start_router_input_request
    import capo_mediaconnect.types.start_router_input_response
    import capo_mediaconnect.types.start_router_output_request
    import capo_mediaconnect.types.start_router_output_response
    import capo_mediaconnect.types.state
    import capo_mediaconnect.types.stop_flow_request
    import capo_mediaconnect.types.stop_flow_response
    import capo_mediaconnect.types.stop_router_input_request
    import capo_mediaconnect.types.stop_router_input_response
    import capo_mediaconnect.types.stop_router_output_request
    import capo_mediaconnect.types.stop_router_output_response
    import capo_mediaconnect.types.tag_global_resource_request
    import capo_mediaconnect.types.tag_resource_request
    import capo_mediaconnect.types.take_router_input_request
    import capo_mediaconnect.types.take_router_input_response
    import capo_mediaconnect.types.untag_global_resource_request
    import capo_mediaconnect.types.untag_resource_request
    import capo_mediaconnect.types.update_bridge_flow_source_request
    import capo_mediaconnect.types.update_bridge_network_output_request
    import capo_mediaconnect.types.update_bridge_network_source_request
    import capo_mediaconnect.types.update_bridge_output_request
    import capo_mediaconnect.types.update_bridge_output_response
    import capo_mediaconnect.types.update_bridge_request
    import capo_mediaconnect.types.update_bridge_response
    import capo_mediaconnect.types.update_bridge_source_request
    import capo_mediaconnect.types.update_bridge_source_response
    import capo_mediaconnect.types.update_bridge_state_request
    import capo_mediaconnect.types.update_bridge_state_response
    import capo_mediaconnect.types.update_egress_gateway_bridge_request
    import capo_mediaconnect.types.update_encryption
    import capo_mediaconnect.types.update_failover_config
    import capo_mediaconnect.types.update_flow_entitlement_request
    import capo_mediaconnect.types.update_flow_entitlement_response
    import capo_mediaconnect.types.update_flow_media_stream_request
    import capo_mediaconnect.types.update_flow_media_stream_response
    import capo_mediaconnect.types.update_flow_output_request
    import capo_mediaconnect.types.update_flow_output_response
    import capo_mediaconnect.types.update_flow_request
    import capo_mediaconnect.types.update_flow_response
    import capo_mediaconnect.types.update_flow_source_request
    import capo_mediaconnect.types.update_flow_source_response
    import capo_mediaconnect.types.update_gateway_bridge_source_request
    import capo_mediaconnect.types.update_gateway_instance_request
    import capo_mediaconnect.types.update_gateway_instance_response
    import capo_mediaconnect.types.update_ingress_gateway_bridge_request
    import capo_mediaconnect.types.update_maintenance
    import capo_mediaconnect.types.update_router_input_request
    import capo_mediaconnect.types.update_router_input_response
    import capo_mediaconnect.types.update_router_network_interface_request
    import capo_mediaconnect.types.update_router_network_interface_response
    import capo_mediaconnect.types.update_router_output_request
    import capo_mediaconnect.types.update_router_output_response
    import capo_mediaconnect.types.vpc_interface_attachment


class MediaConnectClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class MediaConnectClient:
    """A client for the ``MediaConnect`` service.

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
        self._config = MediaConnectClientConfig(
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
        self.bridge_resource = BridgeResource(self)
        self.entitlement_resource = EntitlementResource(self)
        self.flow_media_stream_resource = FlowMediaStreamResource(self)
        self.flow_output_resource = FlowOutputResource(self)
        self.flow_resource = FlowResource(self)
        self.flow_source_resource = FlowSourceResource(self)
        self.flow_vpc_interface_resource = FlowVpcInterfaceResource(self)
        self.gateway_instance_resource = GatewayInstanceResource(self)
        self.gateway_resource = GatewayResource(self)
        self.offering_resource = OfferingResource(self)
        self.reservation_resource = ReservationResource(self)
        self.router_input_resource = RouterInputResource(self)
        self.router_network_interface_resource = RouterNetworkInterfaceResource(self)
        self.router_output_resource = RouterOutputResource(self)

    def operation_options(
        self, config_overrides: Optional[MediaConnectClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaConnectClientConfig = config_overrides or {}
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

    def list_entitlements(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_entitlements_response.ListEntitlementsResponse":
        """<p> Displays a list of all entitlements that have been granted to this account. This request returns 20 results per page.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListEntitlements</code> request with set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 20 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListEntitlements</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListEntitlements</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_entitlements_request.ListEntitlementsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_entitlements_response.ListEntitlementsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_entitlements

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_entitlements.list_entitlements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_entitlements_request.ListEntitlementsRequest = {}
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

    def iter_list_entitlements(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediaconnect.types.listed_entitlement.ListedEntitlement]":
        _token = next_token
        while True:
            _response = self.list_entitlements(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entitlements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_global_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.list_tags_for_global_resource_response.ListTagsForGlobalResourceResponse":
        """<p>Lists the tags associated with a global resource in AWS Elemental MediaConnect. The API supports the following global resources: router inputs, router outputs and router network interfaces. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the global resource whose tags you want to list.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_tags_for_global_resource_request.ListTagsForGlobalResourceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_tags_for_global_resource_response.ListTagsForGlobalResourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_tags_for_global_resource

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_tags_for_global_resource.list_tags_for_global_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_tags_for_global_resource_request.ListTagsForGlobalResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> List all tags on a MediaConnect resource in the current region.</p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) that identifies the MediaConnect resource for which to list the tags.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_tags_for_resource

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_global_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
    ) -> None:
        """<p>Adds tags to a global resource in AWS Elemental MediaConnect. The API supports the following global resources: router inputs, router outputs and router network interfaces. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the global resource to tag.</p>
            tags: <p>A map of tag keys and values to add to the global resource.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.tag_global_resource_request.TagGlobalResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediaconnect._operations.media_connect.tag_global_resource

            output, http_response = (
                capo_mediaconnect._operations.media_connect.tag_global_resource.tag_global_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.tag_global_resource_request.TagGlobalResourceRequest = {
            "resource_arn": resource_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
    ) -> None:
        """<p> Associates the specified tags to a resource with the specified <code>resourceArn</code> in the current region. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well.</p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) that identifies the MediaConnect resource to which to add tags.</p>
            tags: <p> A map from tag keys to values. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediaconnect._operations.media_connect.tag_resource

            output, http_response = (
                capo_mediaconnect._operations.media_connect.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_global_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        tag_keys: Optional[
            "capo_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
    ) -> None:
        """<p>Removes tags from a global resource in AWS Elemental MediaConnect. The API supports the following global resources: router inputs, router outputs and router network interfaces. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the global resource to remove tags from.</p>
            tag_keys: <p>The keys of the tags to remove from the global resource.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.untag_global_resource_request.UntagGlobalResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediaconnect._operations.media_connect.untag_global_resource

            output, http_response = (
                capo_mediaconnect._operations.media_connect.untag_global_resource.untag_global_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.untag_global_resource_request.UntagGlobalResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        tag_keys: Optional[
            "capo_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
    ) -> None:
        """<p> Deletes specified tags from a resource in the current region.</p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that you want to untag. </p>
            tag_keys: <p>The keys of the tags to be removed. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediaconnect._operations.media_connect.untag_resource

            output, http_response = (
                capo_mediaconnect._operations.media_connect.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_bridge(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        egress_gateway_bridge: Optional[
            "capo_mediaconnect.types.add_egress_gateway_bridge_request.AddEgressGatewayBridgeRequest"
        ] = None,
        ingress_gateway_bridge: Optional[
            "capo_mediaconnect.types.add_ingress_gateway_bridge_request.AddIngressGatewayBridgeRequest"
        ] = None,
        name: Optional[str] = None,
        outputs: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_output_request.__listOfAddBridgeOutputRequest"
        ] = None,
        placement_arn: Optional[str] = None,
        source_failover_config: Optional[
            "capo_mediaconnect.types.failover_config.FailoverConfig"
        ] = None,
        sources: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_source_request.__listOfAddBridgeSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.create_bridge_response.CreateBridgeResponse":
        """<p> Creates a new bridge. The request must include one source.</p>

        Args:
            egress_gateway_bridge: <p>An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>
            ingress_gateway_bridge: <p>An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>
            name: <p> The name of the bridge. This name can not be modified after the bridge is created.</p>
            outputs: <p> The outputs that you want to add to this bridge.</p>
            placement_arn: <p> The bridge placement Amazon Resource Number (ARN).</p>
            source_failover_config: <p> The settings for source failover.</p>
            sources: <p> The sources that you want to add to this bridge.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.create_bridge420_exception.CreateBridge420Exception: <p>Exception raised by Elemental MediaConnect when creating the bridge. See the error message for the operation for more information on the cause of this exception. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_bridge_request.CreateBridgeRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_bridge_response.CreateBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_bridge

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_bridge.create_bridge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.create_bridge_request.CreateBridgeRequest = {}
        if egress_gateway_bridge is not None:
            input_["egress_gateway_bridge"] = egress_gateway_bridge
        if ingress_gateway_bridge is not None:
            input_["ingress_gateway_bridge"] = ingress_gateway_bridge
        if name is not None:
            input_["name"] = name
        if outputs is not None:
            input_["outputs"] = outputs
        if placement_arn is not None:
            input_["placement_arn"] = placement_arn
        if source_failover_config is not None:
            input_["source_failover_config"] = source_failover_config
        if sources is not None:
            input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_bridge(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_bridge_response.DescribeBridgeResponse":
        """<p> Displays the details of a bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to describe.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_bridge_request.DescribeBridgeRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_bridge_response.DescribeBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_bridge

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_bridge.describe_bridge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.describe_bridge_request.DescribeBridgeRequest = {
            "bridge_arn": bridge_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bridge(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        egress_gateway_bridge: Optional[
            "capo_mediaconnect.types.update_egress_gateway_bridge_request.UpdateEgressGatewayBridgeRequest"
        ] = None,
        ingress_gateway_bridge: Optional[
            "capo_mediaconnect.types.update_ingress_gateway_bridge_request.UpdateIngressGatewayBridgeRequest"
        ] = None,
        source_failover_config: Optional[
            "capo_mediaconnect.types.update_failover_config.UpdateFailoverConfig"
        ] = None,
    ) -> "capo_mediaconnect.types.update_bridge_response.UpdateBridgeResponse":
        """<p> Updates the bridge.</p>

        Args:
            bridge_arn: <p> TheAmazon Resource Name (ARN) of the bridge that you want to update. </p>
            egress_gateway_bridge: <p> A cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>
            ingress_gateway_bridge: <p> A ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>
            source_failover_config: <p> The settings for source failover. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_bridge_request.UpdateBridgeRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_bridge_response.UpdateBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_bridge.update_bridge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_bridge_request.UpdateBridgeRequest = {
            "bridge_arn": bridge_arn
        }
        if egress_gateway_bridge is not None:
            input_["egress_gateway_bridge"] = egress_gateway_bridge
        if ingress_gateway_bridge is not None:
            input_["ingress_gateway_bridge"] = ingress_gateway_bridge
        if source_failover_config is not None:
            input_["source_failover_config"] = source_failover_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_bridge(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_bridge_response.DeleteBridgeResponse":
        """<p> Deletes a bridge. Before you can delete a bridge, you must stop the bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.delete_bridge_request.DeleteBridgeRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_bridge_response.DeleteBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_bridge

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_bridge.delete_bridge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.delete_bridge_request.DeleteBridgeRequest = {
            "bridge_arn": bridge_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_bridges(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        filter_arn: Optional[str] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_bridges_response.ListBridgesResponse":
        """<p> Displays a list of bridges that are associated with this account and an optionally specified Amazon Resource Name (ARN). This request returns a paginated result.</p>

        Args:
            filter_arn: <p> Filter the list results to display only the bridges associated with the selected ARN.</p>
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListBridges</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListBridges</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListBridges</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_bridges_request.ListBridgesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_bridges_response.ListBridgesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_bridges

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_bridges.list_bridges(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_bridges_request.ListBridgesRequest = {}
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
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

    def iter_list_bridges(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        filter_arn: Optional[str] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediaconnect.types.listed_bridge.ListedBridge]":
        _token = next_token
        while True:
            _response = self.list_bridges(
                config_overrides=config_overrides,
                filter_arn=filter_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("bridges",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def add_bridge_outputs(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        outputs: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_output_request.__listOfAddBridgeOutputRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_bridge_outputs_response.AddBridgeOutputsResponse":
        """<p> Adds outputs to an existing bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            outputs: <p> The outputs that you want to add to this bridge.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.add_bridge_outputs_request.AddBridgeOutputsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.add_bridge_outputs_response.AddBridgeOutputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_bridge_outputs

            output, http_response = (
                capo_mediaconnect._operations.media_connect.add_bridge_outputs.add_bridge_outputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.add_bridge_outputs_request.AddBridgeOutputsRequest = {
            "bridge_arn": bridge_arn
        }
        if outputs is not None:
            input_["outputs"] = outputs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_bridge_sources(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        sources: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_source_request.__listOfAddBridgeSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_bridge_sources_response.AddBridgeSourcesResponse":
        """<p> Adds sources to an existing bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            sources: <p> The sources that you want to add to this bridge.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.add_bridge_sources_request.AddBridgeSourcesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.add_bridge_sources_response.AddBridgeSourcesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_bridge_sources

            output, http_response = (
                capo_mediaconnect._operations.media_connect.add_bridge_sources.add_bridge_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.add_bridge_sources_request.AddBridgeSourcesRequest = {
            "bridge_arn": bridge_arn
        }
        if sources is not None:
            input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_bridge_output(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        output_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_bridge_output_response.RemoveBridgeOutputResponse":
        """<p> Removes an output from a bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            output_name: <p> The name of the bridge output that you want to remove.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.remove_bridge_output_request.RemoveBridgeOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.remove_bridge_output_response.RemoveBridgeOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_bridge_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.remove_bridge_output.remove_bridge_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.remove_bridge_output_request.RemoveBridgeOutputRequest = {
            "bridge_arn": bridge_arn,
            "output_name": output_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_bridge_source(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        source_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_bridge_source_response.RemoveBridgeSourceResponse":
        """<p> Removes a source from a bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            source_name: <p> The name of the bridge source that you want to remove.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.remove_bridge_source_request.RemoveBridgeSourceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.remove_bridge_source_response.RemoveBridgeSourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_bridge_source

            output, http_response = (
                capo_mediaconnect._operations.media_connect.remove_bridge_source.remove_bridge_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.remove_bridge_source_request.RemoveBridgeSourceRequest = {
            "bridge_arn": bridge_arn,
            "source_name": source_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bridge_output(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        output_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        network_output: Optional[
            "capo_mediaconnect.types.update_bridge_network_output_request.UpdateBridgeNetworkOutputRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.update_bridge_output_response.UpdateBridgeOutputResponse":
        """<p> Updates an existing bridge output.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            network_output: <p> The network of the bridge output. </p>
            output_name: <p> Tname of the output that you want to update. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_bridge_output_request.UpdateBridgeOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_bridge_output_response.UpdateBridgeOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_bridge_output.update_bridge_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_bridge_output_request.UpdateBridgeOutputRequest = {
            "bridge_arn": bridge_arn,
            "output_name": output_name,
        }
        if network_output is not None:
            input_["network_output"] = network_output

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bridge_source(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        source_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        flow_source: Optional[
            "capo_mediaconnect.types.update_bridge_flow_source_request.UpdateBridgeFlowSourceRequest"
        ] = None,
        network_source: Optional[
            "capo_mediaconnect.types.update_bridge_network_source_request.UpdateBridgeNetworkSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.update_bridge_source_response.UpdateBridgeSourceResponse":
        """<p> Updates an existing bridge source.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            flow_source: <p> The name of the flow that you want to update.</p>
            network_source: <p> The network for the bridge source. </p>
            source_name: <p> The name of the source that you want to update. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_bridge_source_request.UpdateBridgeSourceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_bridge_source_response.UpdateBridgeSourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge_source

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_bridge_source.update_bridge_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_bridge_source_request.UpdateBridgeSourceRequest = {
            "bridge_arn": bridge_arn,
            "source_name": source_name,
        }
        if flow_source is not None:
            input_["flow_source"] = flow_source
        if network_source is not None:
            input_["network_source"] = network_source

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bridge_state(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        desired_state: Optional[
            "capo_mediaconnect.types.desired_state.DesiredState"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.update_bridge_state_response.UpdateBridgeStateResponse"
    ):
        """<p> Updates the bridge state. </p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update the state of. </p>
            desired_state: <p> The desired state for the bridge. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_bridge_state_request.UpdateBridgeStateRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_bridge_state_response.UpdateBridgeStateResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge_state

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_bridge_state.update_bridge_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_bridge_state_request.UpdateBridgeStateRequest = {
            "bridge_arn": bridge_arn
        }
        if desired_state is not None:
            input_["desired_state"] = desired_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_flow(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        availability_zone: Optional[str] = None,
        entitlements: Optional[
            "capo_mediaconnect.types.__list_of_grant_entitlement_request.__listOfGrantEntitlementRequest"
        ] = None,
        media_streams: Optional[
            "capo_mediaconnect.types.__list_of_add_media_stream_request.__listOfAddMediaStreamRequest"
        ] = None,
        name: Optional[str] = None,
        outputs: Optional[
            "capo_mediaconnect.types.__list_of_add_output_request.__listOfAddOutputRequest"
        ] = None,
        source: Optional[
            "capo_mediaconnect.types.set_source_request.SetSourceRequest"
        ] = None,
        source_failover_config: Optional[
            "capo_mediaconnect.types.failover_config.FailoverConfig"
        ] = None,
        sources: Optional[
            "capo_mediaconnect.types.__list_of_set_source_request.__listOfSetSourceRequest"
        ] = None,
        vpc_interfaces: Optional[
            "capo_mediaconnect.types.__list_of_vpc_interface_request.__listOfVpcInterfaceRequest"
        ] = None,
        maintenance: Optional[
            "capo_mediaconnect.types.add_maintenance.AddMaintenance"
        ] = None,
        source_monitoring_config: Optional[
            "capo_mediaconnect.types.monitoring_config.MonitoringConfig"
        ] = None,
        flow_size: Optional["capo_mediaconnect.types.flow_size.FlowSize"] = None,
        ndi_config: Optional["capo_mediaconnect.types.ndi_config.NdiConfig"] = None,
        encoding_config: Optional[
            "capo_mediaconnect.types.encoding_config.EncodingConfig"
        ] = None,
        flow_tags: Optional[
            "capo_mediaconnect.types.__map_of_string.__mapOfString"
        ] = None,
    ) -> "capo_mediaconnect.types.create_flow_response.CreateFlowResponse":
        """<p> Creates a new flow. The request must include one source. The request optionally can include outputs (up to 50) and entitlements (up to 50).</p>

        Args:
            availability_zone: <p> The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current Amazon Web Services Region.</p>
            entitlements: <p> The entitlements that you want to grant on a flow.</p>
            media_streams: <p> The media streams that you want to add to the flow. You can associate these media streams with sources and outputs on the flow.</p>
            name: <p> The name of the flow.</p>
            outputs: <p> The outputs that you want to add to this flow.</p>
            source: <p> The settings for the source that you want to use for the new flow. </p>
            source_failover_config: <p> The settings for source failover. </p>
            sources: <p>The sources that are assigned to the flow. </p>
            vpc_interfaces: <p> The VPC interfaces you want on the flow.</p>
            maintenance: <p> The maintenance settings you want to use for the flow. </p>
            source_monitoring_config: <p> The settings for source monitoring. </p>
            flow_size: <p> Determines the processing capacity and feature set of the flow. Set this optional parameter to <code>LARGE</code> if you want to enable NDI sources or outputs on the flow. </p>
            ndi_config: <p> Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output. </p>
            flow_tags: <p> The key-value pairs that can be used to tag and organize the flow. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.create_flow420_exception.CreateFlow420Exception: <p>Exception raised by Elemental MediaConnect when creating the flow. See the error message for the operation for more information on the cause of this exception. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_flow_request.CreateFlowRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_flow_response.CreateFlowResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_flow

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_flow.create_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.create_flow_request.CreateFlowRequest = {}
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if entitlements is not None:
            input_["entitlements"] = entitlements
        if media_streams is not None:
            input_["media_streams"] = media_streams
        if name is not None:
            input_["name"] = name
        if outputs is not None:
            input_["outputs"] = outputs
        if source is not None:
            input_["source"] = source
        if source_failover_config is not None:
            input_["source_failover_config"] = source_failover_config
        if sources is not None:
            input_["sources"] = sources
        if vpc_interfaces is not None:
            input_["vpc_interfaces"] = vpc_interfaces
        if maintenance is not None:
            input_["maintenance"] = maintenance
        if source_monitoring_config is not None:
            input_["source_monitoring_config"] = source_monitoring_config
        if flow_size is not None:
            input_["flow_size"] = flow_size
        if ndi_config is not None:
            input_["ndi_config"] = ndi_config
        if encoding_config is not None:
            input_["encoding_config"] = encoding_config
        if flow_tags is not None:
            input_["flow_tags"] = flow_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_flow(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_flow_response.DescribeFlowResponse":
        """<p> Displays the details of a flow. The response includes the flow Amazon Resource Name (ARN), name, and Availability Zone, as well as details about the source, outputs, and entitlements.</p>

        Args:
            flow_arn: <p> The ARN of the flow that you want to describe.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_flow_request.DescribeFlowRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_flow_response.DescribeFlowResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_flow

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_flow.describe_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.describe_flow_request.DescribeFlowRequest = {
            "flow_arn": flow_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_flow(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        source_failover_config: Optional[
            "capo_mediaconnect.types.update_failover_config.UpdateFailoverConfig"
        ] = None,
        maintenance: Optional[
            "capo_mediaconnect.types.update_maintenance.UpdateMaintenance"
        ] = None,
        source_monitoring_config: Optional[
            "capo_mediaconnect.types.monitoring_config.MonitoringConfig"
        ] = None,
        ndi_config: Optional["capo_mediaconnect.types.ndi_config.NdiConfig"] = None,
        flow_size: Optional["capo_mediaconnect.types.flow_size.FlowSize"] = None,
        encoding_config: Optional[
            "capo_mediaconnect.types.encoding_config.EncodingConfig"
        ] = None,
    ) -> "capo_mediaconnect.types.update_flow_response.UpdateFlowResponse":
        """<p> Updates an existing flow.</p> <note> <p> Because <code>UpdateFlowSources</code> and <code>UpdateFlow</code> are separate operations, you can't change both the source type AND the flow size in a single request. </p> <ul> <li> <p>If you have a <code>MEDIUM</code> flow and you want to change the flow source to NDI®:</p> <ul> <li> <p>First, use the <code>UpdateFlow</code> operation to upgrade the flow size to <code>LARGE</code>. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlowSource</code> operation to configure the NDI source. </p> </li> </ul> </li> <li> <p>If you're switching from an NDI source to a transport stream (TS) source and want to downgrade the flow size: </p> <ul> <li> <p>First, use the <code>UpdateFlowSource</code> operation to change the flow source type. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlow</code> operation to downgrade the flow size to <code>MEDIUM</code>.</p> </li> </ul> </li> </ul> </note>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            source_failover_config: <p> The settings for source failover. </p>
            maintenance: <p> The maintenance setting of the flow. </p>
            source_monitoring_config: <p> The settings for source monitoring. </p>
            ndi_config: <p> Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output. </p>
            flow_size: <p> Determines the processing capacity and feature set of the flow. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_flow_request.UpdateFlowRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_flow_response.UpdateFlowResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_flow

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_flow.update_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_flow_request.UpdateFlowRequest = {
            "flow_arn": flow_arn
        }
        if source_failover_config is not None:
            input_["source_failover_config"] = source_failover_config
        if maintenance is not None:
            input_["maintenance"] = maintenance
        if source_monitoring_config is not None:
            input_["source_monitoring_config"] = source_monitoring_config
        if ndi_config is not None:
            input_["ndi_config"] = ndi_config
        if flow_size is not None:
            input_["flow_size"] = flow_size
        if encoding_config is not None:
            input_["encoding_config"] = encoding_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_flow(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_flow_response.DeleteFlowResponse":
        """<p> Deletes a flow. Before you can delete a flow, you must stop the flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.delete_flow_request.DeleteFlowRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_flow_response.DeleteFlowResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_flow

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_flow.delete_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.delete_flow_request.DeleteFlowRequest = {
            "flow_arn": flow_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_flows(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_flows_response.ListFlowsResponse":
        """<p> Displays a list of flows that are associated with this account. This request returns a paginated result.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListFlows</code> request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListFlows</code> request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListFlows</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_flows_request.ListFlowsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_flows_response.ListFlowsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_flows

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_flows.list_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_flows_request.ListFlowsRequest = {}
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

    def iter_list_flows(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediaconnect.types.listed_flow.ListedFlow]":
        _token = next_token
        while True:
            _response = self.list_flows(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("flows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def add_flow_media_streams(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        media_streams: Optional[
            "capo_mediaconnect.types.__list_of_add_media_stream_request.__listOfAddMediaStreamRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_flow_media_streams_response.AddFlowMediaStreamsResponse":
        """<p> Adds media streams to an existing flow. After you add a media stream to a flow, you can associate it with a source and/or an output that uses the ST 2110 JPEG XS or CDI protocol.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow.</p>
            media_streams: <p> The media streams that you want to add to the flow.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.add_flow_media_streams_request.AddFlowMediaStreamsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.add_flow_media_streams_response.AddFlowMediaStreamsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_flow_media_streams

            output, http_response = (
                capo_mediaconnect._operations.media_connect.add_flow_media_streams.add_flow_media_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.add_flow_media_streams_request.AddFlowMediaStreamsRequest = {
            "flow_arn": flow_arn
        }
        if media_streams is not None:
            input_["media_streams"] = media_streams

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_flow_outputs(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        outputs: Optional[
            "capo_mediaconnect.types.__list_of_add_output_request.__listOfAddOutputRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_flow_outputs_response.AddFlowOutputsResponse":
        """<p> Adds outputs to an existing flow. You can create up to 50 outputs per flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to add outputs to.</p>
            outputs: <p> A list of outputs that you want to add to the flow.</p>

        Raises:
            capo_mediaconnect.errors.add_flow_outputs420_exception.AddFlowOutputs420Exception: <p>Exception raised by Elemental MediaConnect when adding the flow output. See the error message for the operation for more information on the cause of this exception. </p>
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.add_flow_outputs_request.AddFlowOutputsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.add_flow_outputs_response.AddFlowOutputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_flow_outputs

            output, http_response = (
                capo_mediaconnect._operations.media_connect.add_flow_outputs.add_flow_outputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.add_flow_outputs_request.AddFlowOutputsRequest = {
            "flow_arn": flow_arn
        }
        if outputs is not None:
            input_["outputs"] = outputs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_flow_sources(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        sources: Optional[
            "capo_mediaconnect.types.__list_of_set_source_request.__listOfSetSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_flow_sources_response.AddFlowSourcesResponse":
        """<p> Adds sources to a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            sources: <p> A list of sources that you want to add to the flow.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.add_flow_sources_request.AddFlowSourcesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.add_flow_sources_response.AddFlowSourcesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_flow_sources

            output, http_response = (
                capo_mediaconnect._operations.media_connect.add_flow_sources.add_flow_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.add_flow_sources_request.AddFlowSourcesRequest = {
            "flow_arn": flow_arn
        }
        if sources is not None:
            input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_flow_vpc_interfaces(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        vpc_interfaces: Optional[
            "capo_mediaconnect.types.__list_of_vpc_interface_request.__listOfVpcInterfaceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_flow_vpc_interfaces_response.AddFlowVpcInterfacesResponse":
        """<p> Adds VPC interfaces to a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            vpc_interfaces: <p> A list of VPC interfaces that you want to add to the flow.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.add_flow_vpc_interfaces_request.AddFlowVpcInterfacesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.add_flow_vpc_interfaces_response.AddFlowVpcInterfacesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_flow_vpc_interfaces

            output, http_response = (
                capo_mediaconnect._operations.media_connect.add_flow_vpc_interfaces.add_flow_vpc_interfaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.add_flow_vpc_interfaces_request.AddFlowVpcInterfacesRequest = {
            "flow_arn": flow_arn
        }
        if vpc_interfaces is not None:
            input_["vpc_interfaces"] = vpc_interfaces

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_flow_source_metadata(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_flow_source_metadata_response.DescribeFlowSourceMetadataResponse":
        """<p> The <code>DescribeFlowSourceMetadata</code> API is used to view information about the flow's source transport stream and programs. This API displays status messages about the flow's source as well as details about the program's video, audio, and other data. </p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_flow_source_metadata_request.DescribeFlowSourceMetadataRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_flow_source_metadata_response.DescribeFlowSourceMetadataResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_flow_source_metadata

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_flow_source_metadata.describe_flow_source_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.describe_flow_source_metadata_request.DescribeFlowSourceMetadataRequest = {
            "flow_arn": flow_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_flow_source_thumbnail(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_flow_source_thumbnail_response.DescribeFlowSourceThumbnailResponse":
        """<p> Describes the thumbnail for the flow source. </p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_flow_source_thumbnail_request.DescribeFlowSourceThumbnailRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_flow_source_thumbnail_response.DescribeFlowSourceThumbnailResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_flow_source_thumbnail

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_flow_source_thumbnail.describe_flow_source_thumbnail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.describe_flow_source_thumbnail_request.DescribeFlowSourceThumbnailRequest = {
            "flow_arn": flow_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def grant_flow_entitlements(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        entitlements: Optional[
            "capo_mediaconnect.types.__list_of_grant_entitlement_request.__listOfGrantEntitlementRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.grant_flow_entitlements_response.GrantFlowEntitlementsResponse":
        """<p> Grants entitlements to an existing flow.</p>

        Args:
            entitlements: <p> The list of entitlements that you want to grant.</p>
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to grant entitlements on.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.grant_flow_entitlements420_exception.GrantFlowEntitlements420Exception: <p>Exception raised by Elemental MediaConnect when granting the entitlement. See the error message for the operation for more information on the cause of this exception. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.grant_flow_entitlements_request.GrantFlowEntitlementsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.grant_flow_entitlements_response.GrantFlowEntitlementsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.grant_flow_entitlements

            output, http_response = (
                capo_mediaconnect._operations.media_connect.grant_flow_entitlements.grant_flow_entitlements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.grant_flow_entitlements_request.GrantFlowEntitlementsRequest = {
            "flow_arn": flow_arn
        }
        if entitlements is not None:
            input_["entitlements"] = entitlements

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_flow_media_stream(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        media_stream_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_flow_media_stream_response.RemoveFlowMediaStreamResponse":
        """<p> Removes a media stream from a flow. This action is only available if the media stream is not associated with a source or output.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            media_stream_name: <p> The name of the media stream that you want to remove.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.remove_flow_media_stream_request.RemoveFlowMediaStreamRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.remove_flow_media_stream_response.RemoveFlowMediaStreamResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_flow_media_stream

            output, http_response = (
                capo_mediaconnect._operations.media_connect.remove_flow_media_stream.remove_flow_media_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.remove_flow_media_stream_request.RemoveFlowMediaStreamRequest = {
            "flow_arn": flow_arn,
            "media_stream_name": media_stream_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_flow_output(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        output_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_flow_output_response.RemoveFlowOutputResponse":
        """<p> Removes an output from an existing flow. This request can be made only on an output that does not have an entitlement associated with it. If the output has an entitlement, you must revoke the entitlement instead. When an entitlement is revoked from a flow, the service automatically removes the associated output.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to remove an output from.</p>
            output_arn: <p> The ARN of the output that you want to remove. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.remove_flow_output_request.RemoveFlowOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.remove_flow_output_response.RemoveFlowOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_flow_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.remove_flow_output.remove_flow_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.remove_flow_output_request.RemoveFlowOutputRequest = {
            "flow_arn": flow_arn,
            "output_arn": output_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_flow_source(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        source_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_flow_source_response.RemoveFlowSourceResponse":
        """<p> Removes a source from an existing flow. This request can be made only if there is more than one source on the flow. </p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to remove a source from.</p>
            source_arn: <p> The ARN of the source that you want to remove.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.remove_flow_source_request.RemoveFlowSourceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.remove_flow_source_response.RemoveFlowSourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_flow_source

            output, http_response = (
                capo_mediaconnect._operations.media_connect.remove_flow_source.remove_flow_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.remove_flow_source_request.RemoveFlowSourceRequest = {
            "flow_arn": flow_arn,
            "source_arn": source_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_flow_vpc_interface(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        vpc_interface_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_flow_vpc_interface_response.RemoveFlowVpcInterfaceResponse":
        """<p> Removes a VPC Interface from an existing flow. This request can be made only on a VPC interface that does not have a Source or Output associated with it. If the VPC interface is referenced by a Source or Output, you must first delete or update the Source or Output to no longer reference the VPC interface.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to remove a VPC interface from.</p>
            vpc_interface_name: <p> The name of the VPC interface that you want to remove.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.remove_flow_vpc_interface_request.RemoveFlowVpcInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.remove_flow_vpc_interface_response.RemoveFlowVpcInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_flow_vpc_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.remove_flow_vpc_interface.remove_flow_vpc_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.remove_flow_vpc_interface_request.RemoveFlowVpcInterfaceRequest = {
            "flow_arn": flow_arn,
            "vpc_interface_name": vpc_interface_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def revoke_flow_entitlement(
        self,
        entitlement_arn: str,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.revoke_flow_entitlement_response.RevokeFlowEntitlementResponse":
        """<p> Revokes an entitlement from a flow. Once an entitlement is revoked, the content becomes unavailable to the subscriber and the associated output is removed.</p>

        Args:
            entitlement_arn: <p> The Amazon Resource Name (ARN) of the entitlement that you want to revoke.</p>
            flow_arn: <p> The flow that you want to revoke an entitlement from.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.revoke_flow_entitlement_request.RevokeFlowEntitlementRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.revoke_flow_entitlement_response.RevokeFlowEntitlementResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.revoke_flow_entitlement

            output, http_response = (
                capo_mediaconnect._operations.media_connect.revoke_flow_entitlement.revoke_flow_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.revoke_flow_entitlement_request.RevokeFlowEntitlementRequest = {
            "entitlement_arn": entitlement_arn,
            "flow_arn": flow_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_flow(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.start_flow_response.StartFlowResponse":
        """<p> Starts a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to start.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.start_flow_request.StartFlowRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.start_flow_response.StartFlowResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.start_flow

            output, http_response = (
                capo_mediaconnect._operations.media_connect.start_flow.start_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.start_flow_request.StartFlowRequest = {
            "flow_arn": flow_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_flow(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.stop_flow_response.StopFlowResponse":
        """<p> Stops a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to stop.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.stop_flow_request.StopFlowRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.stop_flow_response.StopFlowResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.stop_flow

            output, http_response = (
                capo_mediaconnect._operations.media_connect.stop_flow.stop_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.stop_flow_request.StopFlowRequest = {
            "flow_arn": flow_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_flow_entitlement(
        self,
        entitlement_arn: str,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        description: Optional[str] = None,
        encryption: Optional[
            "capo_mediaconnect.types.update_encryption.UpdateEncryption"
        ] = None,
        entitlement_status: Optional[
            "capo_mediaconnect.types.entitlement_status.EntitlementStatus"
        ] = None,
        subscribers: Optional[
            "capo_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
    ) -> "capo_mediaconnect.types.update_flow_entitlement_response.UpdateFlowEntitlementResponse":
        """<p> Updates an entitlement. You can change an entitlement's description, subscribers, and encryption. If you change the subscribers, the service will remove the outputs that are are used by the subscribers that are removed.</p>

        Args:
            description: <p> A description of the entitlement. This description appears only on the MediaConnect console and will not be seen by the subscriber or end user.</p>
            encryption: <p> The type of encryption that will be used on the output associated with this entitlement. Allowable encryption types: static-key, speke.</p>
            entitlement_arn: <p> The Amazon Resource Name (ARN) of the entitlement that you want to update.</p>
            entitlement_status: <p> An indication of whether you want to enable the entitlement to allow access, or disable it to stop streaming content to the subscriber’s flow temporarily. If you don’t specify the <code>entitlementStatus</code> field in your request, MediaConnect leaves the value unchanged.</p>
            flow_arn: <p> The ARN of the flow that is associated with the entitlement that you want to update.</p>
            subscribers: <p> The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_flow_entitlement_request.UpdateFlowEntitlementRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_flow_entitlement_response.UpdateFlowEntitlementResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_flow_entitlement

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_flow_entitlement.update_flow_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_flow_entitlement_request.UpdateFlowEntitlementRequest = {
            "entitlement_arn": entitlement_arn,
            "flow_arn": flow_arn,
        }
        if description is not None:
            input_["description"] = description
        if encryption is not None:
            input_["encryption"] = encryption
        if entitlement_status is not None:
            input_["entitlement_status"] = entitlement_status
        if subscribers is not None:
            input_["subscribers"] = subscribers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_flow_media_stream(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        media_stream_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        attributes: Optional[
            "capo_mediaconnect.types.media_stream_attributes_request.MediaStreamAttributesRequest"
        ] = None,
        clock_rate: Optional[int] = None,
        description: Optional[str] = None,
        media_stream_type: Optional[
            "capo_mediaconnect.types.media_stream_type.MediaStreamType"
        ] = None,
        video_format: Optional[str] = None,
    ) -> "capo_mediaconnect.types.update_flow_media_stream_response.UpdateFlowMediaStreamResponse":
        """<p> Updates an existing media stream.</p>

        Args:
            attributes: <p> The attributes that you want to assign to the media stream.</p>
            clock_rate: <p>The sample rate for the stream. This value in measured in kHz. </p>
            description: <p>A description that can help you quickly identify what your media stream is used for. </p>
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that is associated with the media stream that you updated.</p>
            media_stream_name: <p> The media stream that you updated.</p>
            media_stream_type: <p>The type of media stream. </p>
            video_format: <p>The resolution of the video. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_flow_media_stream_request.UpdateFlowMediaStreamRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_flow_media_stream_response.UpdateFlowMediaStreamResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_flow_media_stream

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_flow_media_stream.update_flow_media_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_flow_media_stream_request.UpdateFlowMediaStreamRequest = {
            "flow_arn": flow_arn,
            "media_stream_name": media_stream_name,
        }
        if attributes is not None:
            input_["attributes"] = attributes
        if clock_rate is not None:
            input_["clock_rate"] = clock_rate
        if description is not None:
            input_["description"] = description
        if media_stream_type is not None:
            input_["media_stream_type"] = media_stream_type
        if video_format is not None:
            input_["video_format"] = video_format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_flow_output(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        output_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        cidr_allow_list: Optional[
            "capo_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
        description: Optional[str] = None,
        destination: Optional[str] = None,
        encryption: Optional[
            "capo_mediaconnect.types.update_encryption.UpdateEncryption"
        ] = None,
        max_latency: Optional[int] = None,
        media_stream_output_configurations: Optional[
            "capo_mediaconnect.types.__list_of_media_stream_output_configuration_request.__listOfMediaStreamOutputConfigurationRequest"
        ] = None,
        min_latency: Optional[int] = None,
        port: Optional[int] = None,
        protocol: Optional["capo_mediaconnect.types.protocol.Protocol"] = None,
        remote_id: Optional[str] = None,
        sender_control_port: Optional[int] = None,
        sender_ip_address: Optional[str] = None,
        smoothing_latency: Optional[int] = None,
        stream_id: Optional[str] = None,
        vpc_interface_attachment: Optional[
            "capo_mediaconnect.types.vpc_interface_attachment.VpcInterfaceAttachment"
        ] = None,
        output_status: Optional[
            "capo_mediaconnect.types.output_status.OutputStatus"
        ] = None,
        ndi_program_name: Optional[str] = None,
        ndi_speed_hq_quality: Optional[int] = None,
        router_integration_state: Optional[
            "capo_mediaconnect.types.state.State"
        ] = None,
        router_integration_transit_encryption: Optional[
            "capo_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
        ] = None,
        ndi_output_timecode_source: Optional[
            "capo_mediaconnect.types.ndi_output_timecode_source.NdiOutputTimecodeSource"
        ] = None,
    ) -> "capo_mediaconnect.types.update_flow_output_response.UpdateFlowOutputResponse":
        """<p> Updates an existing flow output.</p>

        Args:
            cidr_allow_list: <p> The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>
            description: <p> A description of the output. This description appears only on the MediaConnect console and will not be seen by the end user.</p>
            destination: <p> The IP address where you want to send the output.</p>
            encryption: <p> The type of key used for the encryption. If no <code>keyType</code> is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.</p>
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that is associated with the output that you want to update.</p>
            max_latency: <p> The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</p>
            media_stream_output_configurations: <p> The media streams that are associated with the output, and the parameters for those associations.</p>
            min_latency: <p> The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.</p>
            output_arn: <p> The ARN of the output that you want to update.</p>
            port: <p> The port to use when content is distributed to this output.</p>
            protocol: <p> The protocol to use for the output.</p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>
            remote_id: <p> The remote ID for the Zixi-pull stream.</p>
            sender_control_port: <p> The port that the flow uses to send outbound requests to initiate connection with the sender.</p>
            sender_ip_address: <p> The IP address that the flow communicates with to initiate connection with the sender.</p>
            smoothing_latency: <p> The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.</p>
            stream_id: <p> The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.</p>
            vpc_interface_attachment: <p> The name of the VPC interface attachment to use for this output.</p>
            output_status: <p> An indication of whether the output should transmit data or not. If you don't specify the <code>outputStatus</code> field in your request, MediaConnect leaves the value unchanged.</p>
            ndi_program_name: <p> A suffix for the name of the NDI® sender that the flow creates. If a custom name isn't specified, MediaConnect uses the output name. </p>
            ndi_speed_hq_quality: <p>A quality setting for the NDI Speed HQ encoder. </p>
            router_integration_state: <p>Indicates whether to enable or disable router integration for this flow output.</p>
            ndi_output_timecode_source: <p>Controls how MediaConnect generates timecodes for NDI output frames. If you don't specify this field, MediaConnect leaves the value unchanged.</p> <ul> <li> <p> <code>EMBEDDED_TIMECODE</code> - Preserves timecodes from the input transport stream. The timecodes must be embedded in the video stream as SEI timing messages. If no embedded timecode is detected, MediaConnect uses the UTC system time instead.</p> </li> <li> <p> <code>UTC_SYSTEM_TIME</code> - Generates timecodes based on the system clock time when each frame is sent.</p> </li> </ul>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_flow_output_request.UpdateFlowOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_flow_output_response.UpdateFlowOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_flow_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_flow_output.update_flow_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_flow_output_request.UpdateFlowOutputRequest = {
            "flow_arn": flow_arn,
            "output_arn": output_arn,
        }
        if cidr_allow_list is not None:
            input_["cidr_allow_list"] = cidr_allow_list
        if description is not None:
            input_["description"] = description
        if destination is not None:
            input_["destination"] = destination
        if encryption is not None:
            input_["encryption"] = encryption
        if max_latency is not None:
            input_["max_latency"] = max_latency
        if media_stream_output_configurations is not None:
            input_["media_stream_output_configurations"] = (
                media_stream_output_configurations
            )
        if min_latency is not None:
            input_["min_latency"] = min_latency
        if port is not None:
            input_["port"] = port
        if protocol is not None:
            input_["protocol"] = protocol
        if remote_id is not None:
            input_["remote_id"] = remote_id
        if sender_control_port is not None:
            input_["sender_control_port"] = sender_control_port
        if sender_ip_address is not None:
            input_["sender_ip_address"] = sender_ip_address
        if smoothing_latency is not None:
            input_["smoothing_latency"] = smoothing_latency
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if vpc_interface_attachment is not None:
            input_["vpc_interface_attachment"] = vpc_interface_attachment
        if output_status is not None:
            input_["output_status"] = output_status
        if ndi_program_name is not None:
            input_["ndi_program_name"] = ndi_program_name
        if ndi_speed_hq_quality is not None:
            input_["ndi_speed_hq_quality"] = ndi_speed_hq_quality
        if router_integration_state is not None:
            input_["router_integration_state"] = router_integration_state
        if router_integration_transit_encryption is not None:
            input_["router_integration_transit_encryption"] = (
                router_integration_transit_encryption
            )
        if ndi_output_timecode_source is not None:
            input_["ndi_output_timecode_source"] = ndi_output_timecode_source

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_flow_source(
        self,
        flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn",
        source_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        decryption: Optional[
            "capo_mediaconnect.types.update_encryption.UpdateEncryption"
        ] = None,
        description: Optional[str] = None,
        entitlement_arn: Optional[str] = None,
        ingest_port: Optional[int] = None,
        max_bitrate: Optional[int] = None,
        max_latency: Optional[int] = None,
        max_sync_buffer: Optional[int] = None,
        media_stream_source_configurations: Optional[
            "capo_mediaconnect.types.__list_of_media_stream_source_configuration_request.__listOfMediaStreamSourceConfigurationRequest"
        ] = None,
        min_latency: Optional[int] = None,
        protocol: Optional["capo_mediaconnect.types.protocol.Protocol"] = None,
        sender_control_port: Optional[int] = None,
        sender_ip_address: Optional[str] = None,
        source_listener_address: Optional[str] = None,
        source_listener_port: Optional[int] = None,
        stream_id: Optional[str] = None,
        vpc_interface_name: Optional[str] = None,
        whitelist_cidr: Optional[str] = None,
        gateway_bridge_source: Optional[
            "capo_mediaconnect.types.update_gateway_bridge_source_request.UpdateGatewayBridgeSourceRequest"
        ] = None,
        ndi_source_settings: Optional[
            "capo_mediaconnect.types.ndi_source_settings.NdiSourceSettings"
        ] = None,
        router_integration_state: Optional[
            "capo_mediaconnect.types.state.State"
        ] = None,
        router_integration_transit_decryption: Optional[
            "capo_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
        ] = None,
    ) -> "capo_mediaconnect.types.update_flow_source_response.UpdateFlowSourceResponse":
        """<p> Updates the source of a flow.</p> <note> <p> Because <code>UpdateFlowSources</code> and <code>UpdateFlow</code> are separate operations, you can't change both the source type AND the flow size in a single request. </p> <ul> <li> <p>If you have a <code>MEDIUM</code> flow and you want to change the flow source to NDI®:</p> <ul> <li> <p>First, use the <code>UpdateFlow</code> operation to upgrade the flow size to <code>LARGE</code>. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlowSource</code> operation to configure the NDI source. </p> </li> </ul> </li> <li> <p>If you're switching from an NDI source to a transport stream (TS) source and want to downgrade the flow size: </p> <ul> <li> <p>First, use the <code>UpdateFlowSource</code> operation to change the flow source type. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlow</code> operation to downgrade the flow size to <code>MEDIUM</code>.</p> </li> </ul> </li> </ul> </note>

        Args:
            decryption: <p>The type of encryption that is used on the content ingested from the source. </p>
            description: <p>A description of the source. This description is not visible outside of the current Amazon Web Services account. </p>
            entitlement_arn: <p>The Amazon Resource Name (ARN) of the entitlement that allows you to subscribe to the flow. The entitlement is set by the content originator, and the ARN is generated as part of the originator's flow. </p>
            flow_arn: <p> The ARN of the flow that you want to update. </p>
            ingest_port: <p>The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088. </p>
            max_bitrate: <p>The maximum bitrate for RIST, RTP, and RTP-FEC streams. </p>
            max_latency: <p>The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams. </p>
            max_sync_buffer: <p>The size of the buffer (in milliseconds) to use to sync incoming source data. </p>
            media_stream_source_configurations: <p>The media stream that is associated with the source, and the parameters for that association. </p>
            min_latency: <p>The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency. </p>
            protocol: <p>The protocol that the source uses to deliver the content to MediaConnect. </p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>
            sender_control_port: <p>The port that the flow uses to send outbound requests to initiate connection with the sender. </p>
            sender_ip_address: <p>The IP address that the flow communicates with to initiate connection with the sender. </p>
            source_arn: <p>The ARN of the source that you want to update. </p>
            source_listener_address: <p>The source IP or domain name for SRT-caller protocol. </p>
            source_listener_port: <p>Source port for SRT-caller protocol. </p>
            stream_id: <p>The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams. </p>
            vpc_interface_name: <p>The name of the VPC interface that you want to send your output to.</p>
            whitelist_cidr: <p>The range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. </p>
            gateway_bridge_source: <p>The source configuration for cloud flows receiving a stream from a bridge. </p>
            ndi_source_settings: <p> The settings for the NDI source. This includes the exact name of the upstream NDI sender that you want to connect to your source. </p>
            router_integration_state: <p>Indicates whether to enable or disable router integration for this flow source.</p>
            router_integration_transit_decryption: <p>The encryption configuration for the flow source when router integration is enabled.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_flow_source_request.UpdateFlowSourceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_flow_source_response.UpdateFlowSourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_flow_source

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_flow_source.update_flow_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_flow_source_request.UpdateFlowSourceRequest = {
            "flow_arn": flow_arn,
            "source_arn": source_arn,
        }
        if decryption is not None:
            input_["decryption"] = decryption
        if description is not None:
            input_["description"] = description
        if entitlement_arn is not None:
            input_["entitlement_arn"] = entitlement_arn
        if ingest_port is not None:
            input_["ingest_port"] = ingest_port
        if max_bitrate is not None:
            input_["max_bitrate"] = max_bitrate
        if max_latency is not None:
            input_["max_latency"] = max_latency
        if max_sync_buffer is not None:
            input_["max_sync_buffer"] = max_sync_buffer
        if media_stream_source_configurations is not None:
            input_["media_stream_source_configurations"] = (
                media_stream_source_configurations
            )
        if min_latency is not None:
            input_["min_latency"] = min_latency
        if protocol is not None:
            input_["protocol"] = protocol
        if sender_control_port is not None:
            input_["sender_control_port"] = sender_control_port
        if sender_ip_address is not None:
            input_["sender_ip_address"] = sender_ip_address
        if source_listener_address is not None:
            input_["source_listener_address"] = source_listener_address
        if source_listener_port is not None:
            input_["source_listener_port"] = source_listener_port
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if vpc_interface_name is not None:
            input_["vpc_interface_name"] = vpc_interface_name
        if whitelist_cidr is not None:
            input_["whitelist_cidr"] = whitelist_cidr
        if gateway_bridge_source is not None:
            input_["gateway_bridge_source"] = gateway_bridge_source
        if ndi_source_settings is not None:
            input_["ndi_source_settings"] = ndi_source_settings
        if router_integration_state is not None:
            input_["router_integration_state"] = router_integration_state
        if router_integration_transit_decryption is not None:
            input_["router_integration_transit_decryption"] = (
                router_integration_transit_decryption
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_gateway_instance(
        self,
        gateway_instance_arn: "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse":
        """<p> Displays the details of an instance. </p>

        Args:
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway instance that you want to describe.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_gateway_instance

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_gateway_instance.describe_gateway_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest = {
            "gateway_instance_arn": gateway_instance_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gateway_instance(
        self,
        gateway_instance_arn: "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        bridge_placement: Optional[
            "capo_mediaconnect.types.bridge_placement.BridgePlacement"
        ] = None,
    ) -> "capo_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse":
        """<p>Updates an existing gateway instance. </p>

        Args:
            bridge_placement: <p>The state of the instance. <code>ACTIVE</code> or <code>INACTIVE</code>. </p>
            gateway_instance_arn: <p>The Amazon Resource Name (ARN) of the gateway instance that you want to update. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_gateway_instance

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_gateway_instance.update_gateway_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest = {
            "gateway_instance_arn": gateway_instance_arn
        }
        if bridge_placement is not None:
            input_["bridge_placement"] = bridge_placement

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_gateway_instance(
        self,
        gateway_instance_arn: "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse":
        """<p> Deregisters an instance. Before you deregister an instance, all bridges running on the instance must be stopped. If you want to deregister an instance without stopping the bridges, you must use the --force option.</p>

        Args:
            force: <p> Force the deregistration of an instance. Force will deregister an instance, even if there are bridges running on it.</p>
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway that contains the instance that you want to deregister.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.deregister_gateway_instance

            output, http_response = (
                capo_mediaconnect._operations.media_connect.deregister_gateway_instance.deregister_gateway_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest = {
            "gateway_instance_arn": gateway_instance_arn
        }
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateway_instances(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        filter_arn: Optional[str] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse":
        """<p> Displays a list of instances associated with the Amazon Web Services account. This request returns a paginated result. You can use the filterArn property to display only the instances associated with the selected Gateway Amazon Resource Name (ARN).</p>

        Args:
            filter_arn: <p> Filter the list results to display only the instances associated with the selected Gateway ARN.</p>
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a ListInstances request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListInstances</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListInstances</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_gateway_instances

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_gateway_instances.list_gateway_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest = {}
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
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

    def iter_list_gateway_instances(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        filter_arn: Optional[str] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediaconnect.types.listed_gateway_instance.ListedGatewayInstance]":
        _token = next_token
        while True:
            _response = self.list_gateway_instances(
                config_overrides=config_overrides,
                filter_arn=filter_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_gateway(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        egress_cidr_blocks: Optional[
            "capo_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
        name: Optional[str] = None,
        networks: Optional[
            "capo_mediaconnect.types.__list_of_gateway_network.__listOfGatewayNetwork"
        ] = None,
    ) -> "capo_mediaconnect.types.create_gateway_response.CreateGatewayResponse":
        """<p> Creates a new gateway. The request must include at least one network (up to four).</p>

        Args:
            egress_cidr_blocks: <p> The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>
            name: <p> The name of the gateway. This name can not be modified after the gateway is created.</p>
            networks: <p> The list of networks that you want to add to the gateway.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.create_gateway420_exception.CreateGateway420Exception: <p>Exception raised by Elemental MediaConnect when creating the gateway. See the error message for the operation for more information on the cause of this exception. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_gateway_request.CreateGatewayRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_gateway

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_gateway.create_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.create_gateway_request.CreateGatewayRequest = {}
        if egress_cidr_blocks is not None:
            input_["egress_cidr_blocks"] = egress_cidr_blocks
        if name is not None:
            input_["name"] = name
        if networks is not None:
            input_["networks"] = networks

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_gateway(
        self,
        gateway_arn: "capo_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse":
        """<p> Displays the details of a gateway. The response includes the gateway Amazon Resource Name (ARN), name, and CIDR blocks, as well as details about the networks.</p>

        Args:
            gateway_arn: <p> The ARN of the gateway that you want to describe.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_gateway

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_gateway.describe_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway(
        self,
        gateway_arn: "capo_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse":
        """<p> Deletes a gateway. Before you can delete a gateway, you must deregister its instances and delete its bridges.</p>

        Args:
            gateway_arn: <p> The Amazon Resource Name (ARN) of the gateway that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_gateway

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateways(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_gateways_response.ListGatewaysResponse":
        """<p> Displays a list of gateways that are associated with this account. This request returns a paginated result.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListGateways</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_gateways_request.ListGatewaysRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_gateways

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_gateways_request.ListGatewaysRequest = {}
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

    def iter_list_gateways(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediaconnect.types.listed_gateway.ListedGateway]":
        _token = next_token
        while True:
            _response = self.list_gateways(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("gateways",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_offering(
        self,
        offering_arn: "capo_mediaconnect.types.offering_arn.OfferingArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_offering_response.DescribeOfferingResponse":
        """<p> Displays the details of an offering. The response includes the offering description, duration, outbound bandwidth, price, and Amazon Resource Name (ARN).</p>

        Args:
            offering_arn: <p> The ARN of the offering.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_offering_request.DescribeOfferingRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_offering_response.DescribeOfferingResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_offering

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_offering.describe_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.describe_offering_request.DescribeOfferingRequest = {
            "offering_arn": offering_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_offerings(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_offerings_response.ListOfferingsResponse":
        """<p> Displays a list of all offerings that are available to this account in the current Amazon Web Services Region. If you have an active reservation (which means you've purchased an offering that has already started and hasn't expired yet), your account isn't eligible for other offerings.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListOfferings</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_offerings_request.ListOfferingsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_offerings_response.ListOfferingsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_offerings

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_offerings.list_offerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_offerings_request.ListOfferingsRequest = {}
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

    def iter_list_offerings(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediaconnect.types.offering.Offering]":
        _token = next_token
        while True:
            _response = self.list_offerings(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("offerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def purchase_offering(
        self,
        offering_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        reservation_name: Optional[str] = None,
        start: Optional[str] = None,
    ) -> "capo_mediaconnect.types.purchase_offering_response.PurchaseOfferingResponse":
        """<p> Submits a request to purchase an offering. If you already have an active reservation, you can't purchase another offering.</p>

        Args:
            offering_arn: <p> The Amazon Resource Name (ARN) of the offering.</p>
            reservation_name: <p> The name that you want to use for the reservation.</p>
            start: <p> The date and time that you want the reservation to begin, in Coordinated Universal Time (UTC). </p> <p>You can specify any date and time between 12:00am on the first day of the current month to the current time on today's date, inclusive. Specify the start in a 24-hour notation. Use the following format: <code>YYYY-MM-DDTHH:mm:SSZ</code>, where <code>T</code> and <code>Z</code> are literal characters. For example, to specify 11:30pm on March 5, 2020, enter <code>2020-03-05T23:30:00Z</code>.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.purchase_offering_request.PurchaseOfferingRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.purchase_offering_response.PurchaseOfferingResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.purchase_offering

            output, http_response = (
                capo_mediaconnect._operations.media_connect.purchase_offering.purchase_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.purchase_offering_request.PurchaseOfferingRequest = {
            "offering_arn": offering_arn
        }
        if reservation_name is not None:
            input_["reservation_name"] = reservation_name
        if start is not None:
            input_["start"] = start

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_reservation(
        self,
        reservation_arn: "capo_mediaconnect.types.reservation_arn.ReservationArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_reservation_response.DescribeReservationResponse":
        """<p> Displays the details of a reservation. The response includes the reservation name, state, start date and time, and the details of the offering that make up the rest of the reservation (such as price, duration, and outbound bandwidth).</p>

        Args:
            reservation_arn: <p>The Amazon Resource Name (ARN) of the offering. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_reservation_request.DescribeReservationRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_reservation_response.DescribeReservationResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_reservation

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_reservation.describe_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.describe_reservation_request.DescribeReservationRequest = {
            "reservation_arn": reservation_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_reservations(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_reservations_response.ListReservationsResponse":
        """<p> Displays a list of all reservations that have been purchased by this account in the current Amazon Web Services Region. This list includes all reservations in all states (such as active and expired).</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListReservations</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListReservations</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListOfferings</code> request a second time and specify the <code>NextToken</code> value. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_reservations_request.ListReservationsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_reservations_response.ListReservationsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_reservations

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_reservations.list_reservations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_reservations_request.ListReservationsRequest = {}
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

    def iter_list_reservations(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediaconnect.types.reservation.Reservation]":
        _token = next_token
        while True:
            _response = self.list_reservations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("reservations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_router_input(
        self,
        name: str,
        configuration: "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration",
        maximum_bitrate: int,
        routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope",
        tier: "capo_mediaconnect.types.router_input_tier.RouterInputTier",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        transit_encryption: Optional[
            "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
        content_quality_analysis_configuration: Optional[
            "capo_mediaconnect.types.router_content_quality_analysis_configuration.RouterContentQualityAnalysisConfiguration"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.create_router_input_response.CreateRouterInputResponse"
    ):
        """<p>Creates a new router input in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router input.</p>
            configuration: <p>The configuration settings for the router input, which can include the protocol, network interface, and other details.</p>
            maximum_bitrate: <p>The maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - connects only to outputs in same Region. GLOBAL - connects to outputs in any Region.</p>
            tier: <p>The tier level for the router input.</p>
            region_name: <p>The Amazon Web Services Region for the router input. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router input. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            transit_encryption: <p>The transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The maintenance configuration settings for the router input, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router input.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>
            content_quality_analysis_configuration: <p>The content quality analysis configuration for the router input.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.router_input_service_quota_exceeded_exception.RouterInputServiceQuotaExceededException: <p>The request to create a new router input would exceed the service quotas for the account. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_router_input_request.CreateRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_router_input_response.CreateRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_router_input.create_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.create_router_input_request.CreateRouterInputRequest = {
            "name": name,
            "configuration": configuration,
            "maximum_bitrate": maximum_bitrate,
            "routing_scope": routing_scope,
            "tier": tier,
        }
        if region_name is not None:
            input_["region_name"] = region_name
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if content_quality_analysis_configuration is not None:
            input_["content_quality_analysis_configuration"] = (
                content_quality_analysis_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_input_response.GetRouterInputResponse":
        """<p>Retrieves information about a specific router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.get_router_input_request.GetRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_input_response.GetRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_input.get_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.get_router_input_request.GetRouterInputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "capo_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "capo_mediaconnect.types.router_input_tier.RouterInputTier"
        ] = None,
        transit_encryption: Optional[
            "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        content_quality_analysis_configuration: Optional[
            "capo_mediaconnect.types.router_content_quality_analysis_configuration.RouterContentQualityAnalysisConfiguration"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse"
    ):
        """<p>Updates the configuration of an existing router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to update.</p>
            name: <p>The updated name for the router input.</p>
            configuration: <p>The updated configuration settings for the router input. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - can be assigned only to outputs in the same Region. GLOBAL - can be assigned to outputs in any Region.</p>
            tier: <p>The updated tier level for the router input.</p>
            transit_encryption: <p>The updated transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router input, including any changes to preferred maintenance windows and schedules.</p>
            content_quality_analysis_configuration: <p>The content quality analysis configuration for the router input.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_router_input.update_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if routing_scope is not None:
            input_["routing_scope"] = routing_scope
        if tier is not None:
            input_["tier"] = tier
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if content_quality_analysis_configuration is not None:
            input_["content_quality_analysis_configuration"] = (
                content_quality_analysis_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> (
        "capo_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse"
    ):
        """<p>Deletes a router input from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_router_input.delete_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_router_inputs(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_mediaconnect.types.router_input_filter_list.RouterInputFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse":
        """<p>Retrieves a list of router inputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router inputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router inputs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_router_inputs

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_router_inputs.list_router_inputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_router_inputs(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_mediaconnect.types.router_input_filter_list.RouterInputFilterList"
        ] = None,
    ) -> "Iterator[capo_mediaconnect.types.listed_router_input.ListedRouterInput]":
        _token = next_token
        while True:
            _response = self.list_router_inputs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("router_inputs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_router_input_source_metadata(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse":
        """<p>Retrieves detailed metadata information about a specific router input source, including stream details and connection state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve metadata for.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_input_source_metadata

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_input_source_metadata.get_router_input_source_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_router_input_thumbnail(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse":
        """<p>Retrieves the thumbnail for a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to see a thumbnail of.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_input_thumbnail

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_input_thumbnail.get_router_input_thumbnail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restart_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse":
        """<p>Restarts a router input. This operation can be used to recover from errors or refresh the input state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to restart.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.restart_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.restart_router_input.restart_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.start_router_input_response.StartRouterInputResponse":
        """<p>Starts a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to start.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.start_router_input_request.StartRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.start_router_input_response.StartRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.start_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.start_router_input.start_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.start_router_input_request.StartRouterInputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.stop_router_input_response.StopRouterInputResponse":
        """<p>Stops a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to stop.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.stop_router_input_request.StopRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.stop_router_input_response.StopRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.stop_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.stop_router_input.stop_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.stop_router_input_request.StopRouterInputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_router_input(
        self,
        arns: "capo_mediaconnect.types.router_input_arn_list.RouterInputArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse":
        """<p>Retrieves information about multiple router inputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router inputs you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.batch_get_router_input.batch_get_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest = {
            "arns": arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_router_network_interface(
        self,
        name: str,
        configuration: "capo_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse":
        """<p>Creates a new router network interface in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router network interface.</p>
            configuration: <p>The configuration settings for the router network interface.</p>
            region_name: <p>The Amazon Web Services Region for the router network interface. Defaults to the current region if not specified.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router network interface.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.router_network_interface_service_quota_exceeded_exception.RouterNetworkInterfaceServiceQuotaExceededException: <p>The request to create a new router network interface would exceed the service quotas (limits) set for the account. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_router_network_interface.create_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest = {
            "name": name,
            "configuration": configuration,
        }
        if region_name is not None:
            input_["region_name"] = region_name
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

    def get_router_network_interface(
        self,
        arn: "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about a specific router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_network_interface.get_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_router_network_interface(
        self,
        arn: "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse":
        """<p>Updates the configuration of an existing router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to update.</p>
            name: <p>The updated name for the router network interface.</p>
            configuration: <p>The updated configuration settings for the router network interface. Changing the type of the configuration is not supported.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_router_network_interface.update_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_router_network_interface(
        self,
        arn: "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse":
        """<p>Deletes a router network interface from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_router_network_interface.delete_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_router_network_interfaces(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_mediaconnect.types.router_network_interface_filter_list.RouterNetworkInterfaceFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse":
        """<p>Retrieves a list of router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router network interfaces to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router network interfaces.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_router_network_interfaces

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_router_network_interfaces.list_router_network_interfaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_router_network_interfaces(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_mediaconnect.types.router_network_interface_filter_list.RouterNetworkInterfaceFilterList"
        ] = None,
    ) -> "Iterator[capo_mediaconnect.types.listed_router_network_interface.ListedRouterNetworkInterface]":
        _token = next_token
        while True:
            _response = self.list_router_network_interfaces(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("router_network_interfaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def batch_get_router_network_interface(
        self,
        arns: "capo_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about multiple router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router network interfaces you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.batch_get_router_network_interface.batch_get_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest = {
            "arns": arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_router_output(
        self,
        name: str,
        configuration: "capo_mediaconnect.types.router_output_configuration.RouterOutputConfiguration",
        maximum_bitrate: int,
        routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope",
        tier: "capo_mediaconnect.types.router_output_tier.RouterOutputTier",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        fabric_configuration: Optional[
            "capo_mediaconnect.types.fabric_configuration.FabricConfiguration"
        ] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse":
        """<p>Creates a new router output in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router output.</p>
            configuration: <p>The configuration settings for the router output.</p>
            maximum_bitrate: <p>The maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The tier level for the router output.</p>
            region_name: <p>The Amazon Web Services Region for the router output. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router output. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            maintenance_configuration: <p>The maintenance configuration settings for the router output, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag this router output.</p>
            fabric_configuration: <p>The fabric configuration settings for the router output.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.router_output_service_quota_exceeded_exception.RouterOutputServiceQuotaExceededException: <p>The request to create a new router output would exceed the service quotas (limits) set for the account. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_router_output.create_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest = {
            "name": name,
            "configuration": configuration,
            "maximum_bitrate": maximum_bitrate,
            "routing_scope": routing_scope,
            "tier": tier,
        }
        if region_name is not None:
            input_["region_name"] = region_name
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input_["tags"] = tags
        if fabric_configuration is not None:
            input_["fabric_configuration"] = fabric_configuration
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

    def get_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_output_response.GetRouterOutputResponse":
        """<p>Retrieves information about a specific router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.get_router_output_request.GetRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_output_response.GetRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_output.get_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.get_router_output_request.GetRouterOutputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.router_output_configuration.RouterOutputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "capo_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "capo_mediaconnect.types.router_output_tier.RouterOutputTier"
        ] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        fabric_configuration: Optional[
            "capo_mediaconnect.types.fabric_configuration.FabricConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse":
        """<p>Updates the configuration of an existing router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to update.</p>
            name: <p>The updated name for the router output.</p>
            configuration: <p>The updated configuration settings for the router output. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The updated tier level for the router output.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router output, including any changes to preferred maintenance windows and schedules.</p>
            fabric_configuration: <p>The updated fabric configuration settings for the router output. You cannot update the fabric configuration while the output has an active route. You must unroute the output before updating the fabric configuration.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_router_output.update_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if routing_scope is not None:
            input_["routing_scope"] = routing_scope
        if tier is not None:
            input_["tier"] = tier
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if fabric_configuration is not None:
            input_["fabric_configuration"] = fabric_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse":
        """<p>Deletes a router output from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_router_output.delete_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_router_outputs(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_mediaconnect.types.router_output_filter_list.RouterOutputFilterList"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse"
    ):
        """<p>Retrieves a list of router outputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router outputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router outputs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_router_outputs

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_router_outputs.list_router_outputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_router_outputs(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_mediaconnect.types.router_output_filter_list.RouterOutputFilterList"
        ] = None,
    ) -> "Iterator[capo_mediaconnect.types.listed_router_output.ListedRouterOutput]":
        _token = next_token
        while True:
            _response = self.list_router_outputs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("router_outputs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def restart_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse":
        """<p>Restarts a router output. This operation can be used to recover from errors or refresh the output state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to restart.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.restart_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.restart_router_output.restart_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> (
        "capo_mediaconnect.types.start_router_output_response.StartRouterOutputResponse"
    ):
        """<p>Starts a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to start.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.start_router_output_request.StartRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.start_router_output_response.StartRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.start_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.start_router_output.start_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.start_router_output_request.StartRouterOutputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse":
        """<p>Stops a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to stop.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.stop_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.stop_router_output.stop_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def take_router_input(
        self,
        router_output_arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        router_input_arn: Optional[
            "capo_mediaconnect.types.router_input_arn.RouterInputArn"
        ] = None,
    ) -> "capo_mediaconnect.types.take_router_input_response.TakeRouterInputResponse":
        """<p>Associates a router input with a router output in AWS Elemental MediaConnect.</p>

        Args:
            router_output_arn: <p>The Amazon Resource Name (ARN) of the router output that you want to associate with a router input.</p>
            router_input_arn: <p>The Amazon Resource Name (ARN) of the router input that you want to associate with a router output.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.take_router_input_request.TakeRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.take_router_input_response.TakeRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.take_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.take_router_input.take_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.take_router_input_request.TakeRouterInputRequest = {
            "router_output_arn": router_output_arn
        }
        if router_input_arn is not None:
            input_["router_input_arn"] = router_input_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_router_output(
        self,
        arns: "capo_mediaconnect.types.router_output_arn_list.RouterOutputArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse":
        """<p>Retrieves information about multiple router outputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router outputs you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.batch_get_router_output.batch_get_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest = {
            "arns": arns
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
