"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.id


class CreateGatewayResponse(TypedDict, closed=True):
    gateway_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the gateway device. You can use this ID when you call other IoT SiteWise API operations.</p>"""
    gateway_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the gateway, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:gateway/${GatewayId}</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["gatewayArn"] = value["gateway_arn"]
    return out


def deserialize_json(data: dict) -> CreateGatewayResponse:
    out: CreateGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("CreateGatewayResponse.gateway_id required")
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("CreateGatewayResponse.gateway_arn required")
    return out
