"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateDirectConnectGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.direct_connect_gateway_name


class UpdateDirectConnectGatewayRequest(TypedDict, closed=True):
    direct_connect_gateway_id: (
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    )
    """<p>The ID of the Direct Connect gateway to update.</p>"""
    new_direct_connect_gateway_name: (
        "capo_direct_connect.types.direct_connect_gateway_name.DirectConnectGatewayName"
    )
    """<p>The new name for the Direct Connect gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDirectConnectGatewayRequest) -> dict:
    out: dict = {}
    out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    out["newDirectConnectGatewayName"] = value["new_direct_connect_gateway_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDirectConnectGatewayRequest:
    out: UpdateDirectConnectGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    else:
        out["direct_connect_gateway_id"] = ""
    if data.get("newDirectConnectGatewayName") is not None:
        out["new_direct_connect_gateway_name"] = data["newDirectConnectGatewayName"]
    else:
        out["new_direct_connect_gateway_name"] = ""
    return out
