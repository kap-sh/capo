"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.virtual_gateway_id
    import capo_direct_connect.types.virtual_gateway_state


class VirtualGateway(TypedDict, closed=True):
    virtual_gateway_id: NotRequired[
        "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
    ]
    """<p>The ID of the virtual private gateway.</p>"""
    virtual_gateway_state: NotRequired[
        "capo_direct_connect.types.virtual_gateway_state.VirtualGatewayState"
    ]
    """<p>The state of the virtual private gateway. The following are the possible values:</p> <ul> <li> <p> <code>pending</code>: Initial state after creating the virtual private gateway.</p> </li> <li> <p> <code>available</code>: Ready for use by a private virtual interface.</p> </li> <li> <p> <code>deleting</code>: Initial state after deleting the virtual private gateway.</p> </li> <li> <p> <code>deleted</code>: The virtual private gateway is deleted. The private virtual interface is unable to send traffic over this gateway.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualGateway) -> dict:
    out: dict = {}
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    if "virtual_gateway_state" in value:
        out["virtualGatewayState"] = value["virtual_gateway_state"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VirtualGateway:
    out: VirtualGateway = {}  # type: ignore[typeddict-item]
    if data.get("virtualGatewayId") is not None:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    if data.get("virtualGatewayState") is not None:
        out["virtual_gateway_state"] = data["virtualGatewayState"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VirtualGateway) -> dict:
    out: dict = {}
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    if "virtual_gateway_state" in value:
        out["virtualGatewayState"] = value["virtual_gateway_state"]
    return out


def deserialize_cbor(data: dict) -> VirtualGateway:
    out: VirtualGateway = {}  # type: ignore[typeddict-item]
    if data.get("virtualGatewayId") is not None:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    if data.get("virtualGatewayState") is not None:
        out["virtual_gateway_state"] = data["virtualGatewayState"]
    return out
