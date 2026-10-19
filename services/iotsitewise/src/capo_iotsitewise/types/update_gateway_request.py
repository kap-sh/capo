"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.gateway_name
    import capo_iotsitewise.types.id


class UpdateGatewayRequest(TypedDict, closed=True):
    gateway_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the gateway to update.</p>"""
    gateway_name: "capo_iotsitewise.types.gateway_name.GatewayName"
    """<p>A unique name for the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayRequest) -> dict:
    out: dict = {}
    out["gatewayName"] = value["gateway_name"]
    return out


def deserialize_json(data: dict) -> UpdateGatewayRequest:
    out: UpdateGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("gatewayName") is not None:
        out["gateway_name"] = data["gatewayName"]
    else:
        out["gateway_name"] = ""
    return out
