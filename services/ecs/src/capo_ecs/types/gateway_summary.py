"""Generated from Smithy shape ``com.amazonaws.ecs#GatewaySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class GatewaySummary(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the gateway.</p>"""
    status: NotRequired["capo_ecs.types.gateway_status.GatewayStatus"]
    """<p>The status of the gateway.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the gateway was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewaySummary) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import capo_ecs.types.gateway_status

        out["status"] = capo_ecs.types.gateway_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewaySummary:
    out: GatewaySummary = {}  # type: ignore[typeddict-item]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_ecs.types.gateway_status

        out["status"] = capo_ecs.types.gateway_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("createdAt") is not None:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    return out
