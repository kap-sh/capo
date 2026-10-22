"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayOperationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class GatewayOperationError(TypedDict, closed=True):
    operation: NotRequired["capo_ecs.types.string.String"]
    """<p>The IAM-style action identifier of the operation that failed, such as <code>elasticloadbalancing:ModifyLoadBalancerAttributes</code>.</p>"""
    code: NotRequired["capo_ecs.types.string.String"]
    """<p>The error code returned by the failed operation, passed through from the downstream service, such as <code>AccessDenied</code>.</p>"""
    message: NotRequired["capo_ecs.types.string.String"]
    """<p>The detailed error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayOperationError) -> dict:
    out: dict = {}
    if "operation" in value:
        out["operation"] = value["operation"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayOperationError:
    out: GatewayOperationError = {}  # type: ignore[typeddict-item]
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
