"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateResponderGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.client_routing_policy
    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_type
    import capo_rtbfabric.types.listener_config
    import capo_rtbfabric.types.managed_endpoint_configuration
    import capo_rtbfabric.types.protocol
    import capo_rtbfabric.types.security_group_id_list
    import capo_rtbfabric.types.subnet_id_list
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.trust_store_configuration
    import capo_rtbfabric.types.vpc_id


class CreateResponderGatewayRequest(TypedDict, closed=True):
    vpc_id: "capo_rtbfabric.types.vpc_id.VpcId"
    """<p>The unique identifier of the Virtual Private Cloud (VPC).</p>"""
    subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList"
    """<p>Unique identifiers of the subnets. A service quota for your account sets the number of Availability Zones that your subnets can span. By default, this quota is one Availability Zone. To span more Availability Zones, request a quota increase.</p>"""
    security_group_ids: (
        "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The unique identifiers of the security groups.</p>"""
    domain_name: NotRequired["capo_rtbfabric.types.domain_name.DomainName"]
    """<p>The domain name for the responder gateway.</p>"""
    port: "int"
    """<p>The networking port to use.</p>"""
    protocol: "capo_rtbfabric.types.protocol.Protocol"
    """<p>The networking protocol to use.</p>"""
    listener_config: NotRequired["capo_rtbfabric.types.listener_config.ListenerConfig"]
    trust_store_configuration: NotRequired[
        "capo_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
    ]
    """<p>The configuration of the trust store.</p>"""
    managed_endpoint_configuration: NotRequired[
        "capo_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
    ]
    """<p>The configuration for the managed endpoint.</p>"""
    client_token: "str"
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    description: NotRequired["str"]
    """<p>An optional description for the responder gateway.</p>"""
    tags: NotRequired["capo_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""
    gateway_type: NotRequired["capo_rtbfabric.types.gateway_type.GatewayType"]
    """<p>The type of gateway. Valid values are <code>EXTERNAL</code> or <code>INTERNAL</code>.</p>"""
    client_routing_policy: NotRequired[
        "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
    ]
    """<p>The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. Valid values are the following:</p> <ul> <li> <p> <code>AVAILABILITY_ZONE_AFFINITY</code>: RTB Fabric routes each requester's traffic to gateway capacity in the requester's own Availability Zone when the gateway has capacity available there. Otherwise, RTB Fabric routes the traffic to gateway capacity in the other Availability Zones of the gateway.</p> </li> <li> <p> <code>ANY_AVAILABILITY_ZONE</code>: RTB Fabric routes each requester's traffic to gateway capacity in every Availability Zone that the subnets of the gateway span. The Availability Zone that the requester is in does not change this.</p> </li> </ul> <p>If you don't specify a value, RTB Fabric uses <code>AVAILABILITY_ZONE_AFFINITY</code>. To get the behavior of <code>ANY_AVAILABILITY_ZONE</code>, create the gateway with subnets in more than one Availability Zone. RTB Fabric does not support partial Availability Zone affinity, so <code>PARTIAL_AVAILABILITY_ZONE_AFFINITY</code> is not a valid value. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResponderGatewayRequest) -> dict:
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
    out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.serialize_json(value["tags"])
    if "gateway_type" in value:
        import capo_rtbfabric.types.gateway_type

        out["gatewayType"] = capo_rtbfabric.types.gateway_type.serialize_json(
            value["gateway_type"]
        )
    if "client_routing_policy" in value:
        import capo_rtbfabric.types.client_routing_policy

        out["clientRoutingPolicy"] = (
            capo_rtbfabric.types.client_routing_policy.serialize_json(
                value["client_routing_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateResponderGatewayRequest:
    out: CreateResponderGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("CreateResponderGatewayRequest.vpc_id required")
    if data.get("subnetIds") is not None:
        import capo_rtbfabric.types.subnet_id_list

        out["subnet_ids"] = capo_rtbfabric.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("CreateResponderGatewayRequest.subnet_ids required")
    if data.get("securityGroupIds") is not None:
        import capo_rtbfabric.types.security_group_id_list

        out["security_group_ids"] = (
            capo_rtbfabric.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateResponderGatewayRequest.security_group_ids required"
        )
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        raise DeserializationError("CreateResponderGatewayRequest.port required")
    if data.get("protocol") is not None:
        import capo_rtbfabric.types.protocol

        out["protocol"] = capo_rtbfabric.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        raise DeserializationError("CreateResponderGatewayRequest.protocol required")
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateResponderGatewayRequest.client_token required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    if data.get("gatewayType") is not None:
        import capo_rtbfabric.types.gateway_type

        out["gateway_type"] = capo_rtbfabric.types.gateway_type.deserialize_json(
            data["gatewayType"]
        )
    if data.get("clientRoutingPolicy") is not None:
        import capo_rtbfabric.types.client_routing_policy

        out["client_routing_policy"] = (
            capo_rtbfabric.types.client_routing_policy.deserialize_json(
                data["clientRoutingPolicy"]
            )
        )
    return out
