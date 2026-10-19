"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#GetRoutingControlStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.arn
    import capo_route53_recovery_cluster.types.routing_control_name
    import capo_route53_recovery_cluster.types.routing_control_state


class GetRoutingControlStateResponse(TypedDict, closed=True):
    routing_control_arn: "capo_route53_recovery_cluster.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the response.</p>"""
    routing_control_state: (
        "capo_route53_recovery_cluster.types.routing_control_state.RoutingControlState"
    )
    """<p>The state of the routing control.</p>"""
    routing_control_name: NotRequired[
        "capo_route53_recovery_cluster.types.routing_control_name.RoutingControlName"
    ]
    """<p>The routing control name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRoutingControlStateResponse) -> dict:
    out: dict = {}
    out["RoutingControlArn"] = value["routing_control_arn"]
    import capo_route53_recovery_cluster.types.routing_control_state

    out["RoutingControlState"] = (
        capo_route53_recovery_cluster.types.routing_control_state.serialize_aws_json_1_0(
            value["routing_control_state"]
        )
    )
    if "routing_control_name" in value:
        out["RoutingControlName"] = value["routing_control_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRoutingControlStateResponse:
    out: GetRoutingControlStateResponse = {}  # type: ignore[typeddict-item]
    if data.get("RoutingControlArn") is not None:
        out["routing_control_arn"] = data["RoutingControlArn"]
    else:
        out["routing_control_arn"] = ""
    if data.get("RoutingControlState") is not None:
        import capo_route53_recovery_cluster.types.routing_control_state

        out["routing_control_state"] = (
            capo_route53_recovery_cluster.types.routing_control_state.deserialize_aws_json_1_0(
                data["RoutingControlState"]
            )
        )
    else:
        import typing

        out["routing_control_state"] = typing.cast(
            "capo_route53_recovery_cluster.types.routing_control_state.RoutingControlState",
            "",
        )
    if data.get("RoutingControlName") is not None:
        out["routing_control_name"] = data["RoutingControlName"]
    return out
