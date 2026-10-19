"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ArcRoutingControlState``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.routing_control_arn
    import capo_arc_region_switch.types.routing_control_state_change


class ArcRoutingControlState(TypedDict, closed=True):
    routing_control_arn: (
        "capo_arc_region_switch.types.routing_control_arn.RoutingControlArn"
    )
    """<p>The Amazon Resource Name (ARN) of a routing control.</p>"""
    state: "capo_arc_region_switch.types.routing_control_state_change.RoutingControlStateChange"
    """<p>The state of an ARC routing control, On or Off.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArcRoutingControlState) -> dict:
    out: dict = {}
    out["routingControlArn"] = value["routing_control_arn"]
    import capo_arc_region_switch.types.routing_control_state_change

    out["state"] = (
        capo_arc_region_switch.types.routing_control_state_change.serialize_aws_json_1_0(
            value["state"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ArcRoutingControlState:
    out: ArcRoutingControlState = {}  # type: ignore[typeddict-item]
    if data.get("routingControlArn") is not None:
        out["routing_control_arn"] = data["routingControlArn"]
    else:
        out["routing_control_arn"] = ""
    if data.get("state") is not None:
        import capo_arc_region_switch.types.routing_control_state_change

        out["state"] = (
            capo_arc_region_switch.types.routing_control_state_change.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_arc_region_switch.types.routing_control_state_change.RoutingControlStateChange",
            "",
        )
    return out
