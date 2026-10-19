"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#GetRoutingControlStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.arn


class GetRoutingControlStateRequest(TypedDict, closed=True):
    routing_control_arn: "capo_route53_recovery_cluster.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the routing control that you want to get the state for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRoutingControlStateRequest) -> dict:
    out: dict = {}
    out["RoutingControlArn"] = value["routing_control_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRoutingControlStateRequest:
    out: GetRoutingControlStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("RoutingControlArn") is not None:
        out["routing_control_arn"] = data["RoutingControlArn"]
    else:
        out["routing_control_arn"] = ""
    return out
