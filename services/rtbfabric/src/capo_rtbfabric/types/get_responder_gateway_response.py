"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetResponderGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_rtbfabric.types.client_routing_policy
    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.gateway_type
    import capo_rtbfabric.types.listener_config
    import capo_rtbfabric.types.managed_endpoint_configuration
    import capo_rtbfabric.types.protocol
    import capo_rtbfabric.types.responder_gateway_status
    import capo_rtbfabric.types.security_group_id_list
    import capo_rtbfabric.types.subnet_id_list
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.trust_store_configuration
    import capo_rtbfabric.types.vpc_id


class GetResponderGatewayResponse(TypedDict, closed=True):
    vpc_id: "capo_rtbfabric.types.vpc_id.VpcId"
    """<p>The unique identifier of the Virtual Private Cloud (VPC).</p>"""
    subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList"
    """<p>The unique identifiers of the subnets.</p>"""
    security_group_ids: (
        "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The unique identifiers of the security groups.</p>"""
    status: "capo_rtbfabric.types.responder_gateway_status.ResponderGatewayStatus"
    """<p>The status of the request.</p>"""
    description: NotRequired["str"]
    """<p>The description of the responder gateway.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the responder gateway was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the responder gateway was updated.</p>"""
    domain_name: NotRequired["capo_rtbfabric.types.domain_name.DomainName"]
    """<p>The domain name of the responder gateway.</p>"""
    port: "int"
    """<p>The networking port.</p>"""
    protocol: "capo_rtbfabric.types.protocol.Protocol"
    """<p>The networking protocol.</p>"""
    listener_config: NotRequired["capo_rtbfabric.types.listener_config.ListenerConfig"]
    """<p>The listener configuration for the responder gateway.</p>"""
    trust_store_configuration: NotRequired[
        "capo_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
    ]
    """<p>The configuration of the trust store.</p>"""
    managed_endpoint_configuration: NotRequired[
        "capo_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
    ]
    """<p>The configuration of the managed endpoint.</p>"""
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    tags: NotRequired["capo_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""
    active_links_count: NotRequired["int"]
    """<p>The count of active links for the responder gateway.</p>"""
    total_links_count: NotRequired["int"]
    """<p>The total count of links for the responder gateway.</p>"""
    links_requested_count: NotRequired["int"]
    """<p>The count of requested links waiting for the responder gateway to accept or reject.</p>"""
    gateway_type: NotRequired["capo_rtbfabric.types.gateway_type.GatewayType"]
    """<p>The type of gateway. Valid values are <code>EXTERNAL</code> or <code>INTERNAL</code>.</p>"""
    external_inbound_endpoint: NotRequired[
        "capo_rtbfabric.types.domain_name.DomainName"
    ]
    """<p>The external inbound endpoint for the responder gateway.</p>"""
    client_routing_policy: NotRequired[
        "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
    ]
    """<p>The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. RTB Fabric omits this member if the gateway has never had a client routing policy. An omitted value means that the gateway uses <code>AVAILABILITY_ZONE_AFFINITY</code>. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResponderGatewayResponse) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import capo_rtbfabric.types.subnet_id_list

    out["subnetIds"] = capo_rtbfabric.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import capo_rtbfabric.types.security_group_id_list

    out["securityGroupIds"] = (
        capo_rtbfabric.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    import capo_rtbfabric.types.responder_gateway_status

    out["status"] = capo_rtbfabric.types.responder_gateway_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["createdAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["updatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    out["port"] = value["port"]
    import capo_rtbfabric.types.protocol

    out["protocol"] = capo_rtbfabric.types.protocol.serialize_json(value["protocol"])
    if "listener_config" in value:
        import capo_rtbfabric.types.listener_config

        out["listenerConfig"] = capo_rtbfabric.types.listener_config.serialize_json(
            value["listener_config"]
        )
    if "trust_store_configuration" in value:
        import capo_rtbfabric.types.trust_store_configuration

        out["trustStoreConfiguration"] = (
            capo_rtbfabric.types.trust_store_configuration.serialize_json(
                value["trust_store_configuration"]
            )
        )
    if "managed_endpoint_configuration" in value:
        import capo_rtbfabric.types.managed_endpoint_configuration

        out["managedEndpointConfiguration"] = (
            capo_rtbfabric.types.managed_endpoint_configuration.serialize_json(
                value["managed_endpoint_configuration"]
            )
        )
    out["gatewayId"] = value["gateway_id"]
    if "tags" in value:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.serialize_json(value["tags"])
    if "active_links_count" in value:
        out["activeLinksCount"] = value["active_links_count"]
    if "total_links_count" in value:
        out["totalLinksCount"] = value["total_links_count"]
    if "links_requested_count" in value:
        out["linksRequestedCount"] = value["links_requested_count"]
    if "gateway_type" in value:
        import capo_rtbfabric.types.gateway_type

        out["gatewayType"] = capo_rtbfabric.types.gateway_type.serialize_json(
            value["gateway_type"]
        )
    if "external_inbound_endpoint" in value:
        out["externalInboundEndpoint"] = value["external_inbound_endpoint"]
    if "client_routing_policy" in value:
        import capo_rtbfabric.types.client_routing_policy

        out["clientRoutingPolicy"] = (
            capo_rtbfabric.types.client_routing_policy.serialize_json(
                value["client_routing_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetResponderGatewayResponse:
    out: GetResponderGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("GetResponderGatewayResponse.vpc_id required")
    if data.get("subnetIds") is not None:
        import capo_rtbfabric.types.subnet_id_list

        out["subnet_ids"] = capo_rtbfabric.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("GetResponderGatewayResponse.subnet_ids required")
    if data.get("securityGroupIds") is not None:
        import capo_rtbfabric.types.security_group_id_list

        out["security_group_ids"] = (
            capo_rtbfabric.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "GetResponderGatewayResponse.security_group_ids required"
        )
    if data.get("status") is not None:
        import capo_rtbfabric.types.responder_gateway_status

        out["status"] = capo_rtbfabric.types.responder_gateway_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetResponderGatewayResponse.status required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["created_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        raise DeserializationError("GetResponderGatewayResponse.port required")
    if data.get("protocol") is not None:
        import capo_rtbfabric.types.protocol

        out["protocol"] = capo_rtbfabric.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        raise DeserializationError("GetResponderGatewayResponse.protocol required")
    if data.get("listenerConfig") is not None:
        import capo_rtbfabric.types.listener_config

        out["listener_config"] = capo_rtbfabric.types.listener_config.deserialize_json(
            data["listenerConfig"]
        )
    if data.get("trustStoreConfiguration") is not None:
        import capo_rtbfabric.types.trust_store_configuration

        out["trust_store_configuration"] = (
            capo_rtbfabric.types.trust_store_configuration.deserialize_json(
                data["trustStoreConfiguration"]
            )
        )
    if data.get("managedEndpointConfiguration") is not None:
        import capo_rtbfabric.types.managed_endpoint_configuration

        out["managed_endpoint_configuration"] = (
            capo_rtbfabric.types.managed_endpoint_configuration.deserialize_json(
                data["managedEndpointConfiguration"]
            )
        )
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("GetResponderGatewayResponse.gateway_id required")
    if data.get("tags") is not None:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    if data.get("activeLinksCount") is not None:
        out["active_links_count"] = data["activeLinksCount"]
    if data.get("totalLinksCount") is not None:
        out["total_links_count"] = data["totalLinksCount"]
    if data.get("linksRequestedCount") is not None:
        out["links_requested_count"] = data["linksRequestedCount"]
    if data.get("gatewayType") is not None:
        import capo_rtbfabric.types.gateway_type

        out["gateway_type"] = capo_rtbfabric.types.gateway_type.deserialize_json(
            data["gatewayType"]
        )
    if data.get("externalInboundEndpoint") is not None:
        out["external_inbound_endpoint"] = data["externalInboundEndpoint"]
    if data.get("clientRoutingPolicy") is not None:
        import capo_rtbfabric.types.client_routing_policy

        out["client_routing_policy"] = (
            capo_rtbfabric.types.client_routing_policy.deserialize_json(
                data["clientRoutingPolicy"]
            )
        )
    return out
