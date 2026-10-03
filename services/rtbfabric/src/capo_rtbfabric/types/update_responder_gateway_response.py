"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateResponderGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.client_routing_policy
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.responder_gateway_status


class UpdateResponderGatewayResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    status: "capo_rtbfabric.types.responder_gateway_status.ResponderGatewayStatus"
    """<p>The status of the request.</p>"""
    client_routing_policy: NotRequired[
        "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
    ]
    """<p>The client routing policy of the gateway. If the operation changed this policy, the gateway uses the new policy after its status returns to <code>ACTIVE</code>. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResponderGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    import capo_rtbfabric.types.responder_gateway_status

    out["status"] = capo_rtbfabric.types.responder_gateway_status.serialize_json(
        value["status"]
    )
    if "client_routing_policy" in value:
        import capo_rtbfabric.types.client_routing_policy

        out["clientRoutingPolicy"] = (
            capo_rtbfabric.types.client_routing_policy.serialize_json(
                value["client_routing_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateResponderGatewayResponse:
    out: UpdateResponderGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("UpdateResponderGatewayResponse.gateway_id required")
    if data.get("status") is not None:
        import capo_rtbfabric.types.responder_gateway_status

        out["status"] = capo_rtbfabric.types.responder_gateway_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateResponderGatewayResponse.status required")
    if data.get("clientRoutingPolicy") is not None:
        import capo_rtbfabric.types.client_routing_policy

        out["client_routing_policy"] = (
            capo_rtbfabric.types.client_routing_policy.deserialize_json(
                data["clientRoutingPolicy"]
            )
        )
    return out
