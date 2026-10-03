"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#UpdateRoutingControlStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53_recovery_cluster.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.arn
    import capo_route53_recovery_cluster.types.arns
    import capo_route53_recovery_cluster.types.routing_control_state


class UpdateRoutingControlStateRequest(TypedDict, closed=True):
    routing_control_arn: "capo_route53_recovery_cluster.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the routing control that you want to update the state for.</p>"""
    routing_control_state: (
        "capo_route53_recovery_cluster.types.routing_control_state.RoutingControlState"
    )
    """<p>The state of the routing control. You can set the value to ON or OFF.</p>"""
    safety_rules_to_override: NotRequired[
        "capo_route53_recovery_cluster.types.arns.Arns"
    ]
    """<p>The Amazon Resource Names (ARNs) for the safety rules that you want to override when you're updating the state of a routing control. You can override one safety rule or multiple safety rules by including one or more ARNs, separated by commas.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html"> Override safety rules to reroute traffic</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRoutingControlStateRequest) -> dict:
    out: dict = {}
    out["RoutingControlArn"] = value["routing_control_arn"]
    import capo_route53_recovery_cluster.types.routing_control_state

    out["RoutingControlState"] = (
        capo_route53_recovery_cluster.types.routing_control_state.serialize_aws_json_1_0(
            value["routing_control_state"]
        )
    )
    if "safety_rules_to_override" in value:
        import capo_route53_recovery_cluster.types.arns

        out["SafetyRulesToOverride"] = (
            capo_route53_recovery_cluster.types.arns.serialize_aws_json_1_0(
                value["safety_rules_to_override"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRoutingControlStateRequest:
    out: UpdateRoutingControlStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("RoutingControlArn") is not None:
        out["routing_control_arn"] = data["RoutingControlArn"]
    else:
        raise DeserializationError(
            "UpdateRoutingControlStateRequest.routing_control_arn required"
        )
    if data.get("RoutingControlState") is not None:
        import capo_route53_recovery_cluster.types.routing_control_state

        out["routing_control_state"] = (
            capo_route53_recovery_cluster.types.routing_control_state.deserialize_aws_json_1_0(
                data["RoutingControlState"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRoutingControlStateRequest.routing_control_state required"
        )
    if data.get("SafetyRulesToOverride") is not None:
        import capo_route53_recovery_cluster.types.arns

        out["safety_rules_to_override"] = (
            capo_route53_recovery_cluster.types.arns.deserialize_aws_json_1_0(
                data["SafetyRulesToOverride"]
            )
        )
    return out
