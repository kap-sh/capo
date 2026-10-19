"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteDirectConnectGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_id


class DeleteDirectConnectGatewayRequest(TypedDict, closed=True):
    direct_connect_gateway_id: (
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    )
    """<p>The ID of the Direct Connect gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDirectConnectGatewayRequest) -> dict:
    out: dict = {}
    out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDirectConnectGatewayRequest:
    out: DeleteDirectConnectGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    else:
        out["direct_connect_gateway_id"] = ""
    return out
