"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class DeleteGatewayRequest(TypedDict, closed=True):
    gateway: "capo_ecs.types.string.String"
    """<p>The name or Amazon Resource Name (ARN) of the gateway to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGatewayRequest) -> dict:
    out: dict = {}
    out["gateway"] = value["gateway"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGatewayRequest:
    out: DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("gateway") is not None:
        out["gateway"] = data["gateway"]
    else:
        out["gateway"] = ""
    return out
