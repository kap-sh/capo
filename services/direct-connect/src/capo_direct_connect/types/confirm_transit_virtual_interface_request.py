"""Generated from Smithy shape ``com.amazonaws.directconnect#ConfirmTransitVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.virtual_interface_id


class ConfirmTransitVirtualInterfaceRequest(TypedDict, closed=True):
    virtual_interface_id: (
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    )
    """<p>The ID of the virtual interface.</p>"""
    direct_connect_gateway_id: (
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    )
    """<p>The ID of the Direct Connect gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmTransitVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["virtualInterfaceId"] = value["virtual_interface_id"]
    out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmTransitVirtualInterfaceRequest:
    out: ConfirmTransitVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    else:
        out["virtual_interface_id"] = ""
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    else:
        out["direct_connect_gateway_id"] = ""
    return out
