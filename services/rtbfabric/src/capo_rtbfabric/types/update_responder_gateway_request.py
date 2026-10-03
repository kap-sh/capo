"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateResponderGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.client_routing_policy
    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.listener_config
    import capo_rtbfabric.types.managed_endpoint_configuration
    import capo_rtbfabric.types.protocol
    import capo_rtbfabric.types.trust_store_configuration


class UpdateResponderGatewayRequest(TypedDict, closed=True):
    domain_name: NotRequired["capo_rtbfabric.types.domain_name.DomainName"]
    """<p>Domain name for the responder gateway. This operation does not change the domain name of an existing gateway. To use a different domain name, delete the gateway and create a new one.</p>"""
    port: "int"
    """<p>Networking port to use. This operation does not change the port of an existing gateway. To use a different port, delete the gateway and create a new one.</p>"""
    protocol: "capo_rtbfabric.types.protocol.Protocol"
    """<p>Networking protocol to use. This operation does not change the protocol of an existing gateway. To use a different protocol, delete the gateway and create a new one.</p>"""
    listener_config: NotRequired["capo_rtbfabric.types.listener_config.ListenerConfig"]
    """<p>The listener configuration for the responder gateway.</p>"""
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
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    description: NotRequired["str"]
    """<p>An optional description for the responder gateway.</p>"""
    client_routing_policy: NotRequired[
        "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
    ]
    """<p>The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. Valid values are the following:</p> <ul> <li> <p> <code>AVAILABILITY_ZONE_AFFINITY</code>: RTB Fabric routes each requester's traffic to gateway capacity in the requester's own Availability Zone when the gateway has capacity available there. Otherwise, RTB Fabric routes the traffic to gateway capacity in the other Availability Zones of the gateway.</p> </li> <li> <p> <code>ANY_AVAILABILITY_ZONE</code>: RTB Fabric routes each requester's traffic to gateway capacity in every Availability Zone that the subnets of the gateway span. The Availability Zone that the requester is in does not change this.</p> </li> </ul> <p>If you don't specify a value, the gateway keeps its current client routing policy. Changing the policy sets the gateway status to <code>PENDING_UPDATE</code> until the change is complete. RTB Fabric does not support partial Availability Zone affinity, so <code>PARTIAL_AVAILABILITY_ZONE_AFFINITY</code> is not a valid value. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResponderGatewayRequest) -> dict:
    out: dict = {}
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
    if "client_routing_policy" in value:
        import capo_rtbfabric.types.client_routing_policy

        out["clientRoutingPolicy"] = (
            capo_rtbfabric.types.client_routing_policy.serialize_json(
                value["client_routing_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateResponderGatewayRequest:
    out: UpdateResponderGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        raise DeserializationError("UpdateResponderGatewayRequest.port required")
    if data.get("protocol") is not None:
        import capo_rtbfabric.types.protocol

        out["protocol"] = capo_rtbfabric.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        raise DeserializationError("UpdateResponderGatewayRequest.protocol required")
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
            "UpdateResponderGatewayRequest.client_token required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientRoutingPolicy") is not None:
        import capo_rtbfabric.types.client_routing_policy

        out["client_routing_policy"] = (
            capo_rtbfabric.types.client_routing_policy.deserialize_json(
                data["clientRoutingPolicy"]
            )
        )
    return out
