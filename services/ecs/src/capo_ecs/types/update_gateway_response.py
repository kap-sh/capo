"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_status
    import capo_ecs.types.string


class UpdateGatewayResponse(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the gateway.</p>"""
    status: NotRequired["capo_ecs.types.gateway_status.GatewayStatus"]
    """<p>The status of the gateway. After a successful update request, the status is <code>UPDATE_IN_PROGRESS</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGatewayResponse) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGatewayResponse:
    out: UpdateGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_ecs.types.gateway_status

        out["status"] = capo_ecs.types.gateway_status.deserialize_aws_json_1_1(
            data["status"]
        )
    return out
