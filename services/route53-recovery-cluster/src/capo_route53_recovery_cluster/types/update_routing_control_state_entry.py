"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#UpdateRoutingControlStateEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.arn
    import capo_route53_recovery_cluster.types.routing_control_state


class UpdateRoutingControlStateEntry(TypedDict, closed=True):
    routing_control_arn: "capo_route53_recovery_cluster.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for a routing control state entry.</p>"""
    routing_control_state: (
        "capo_route53_recovery_cluster.types.routing_control_state.RoutingControlState"
    )
    """<p>The routing control state in a set of routing control state entries.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRoutingControlStateEntry) -> dict:
    out: dict = {}
    out["RoutingControlArn"] = value["routing_control_arn"]
    import capo_route53_recovery_cluster.types.routing_control_state

    out["RoutingControlState"] = (
        capo_route53_recovery_cluster.types.routing_control_state.serialize_aws_json_1_0(
            value["routing_control_state"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRoutingControlStateEntry:
    out: UpdateRoutingControlStateEntry = {}  # type: ignore[typeddict-item]
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
    return out
