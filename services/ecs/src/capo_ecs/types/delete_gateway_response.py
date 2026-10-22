"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_status
    import capo_ecs.types.string


class DeleteGatewayResponse(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the deleted gateway.</p>"""
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the deleted gateway.</p>"""
    status: NotRequired["capo_ecs.types.gateway_status.GatewayStatus"]
    """<p>The status of the gateway. After a successful delete, the status is <code>DELETED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGatewayResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> DeleteGatewayResponse:
    out: DeleteGatewayResponse = {}  # type: ignore[typeddict-item]
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
