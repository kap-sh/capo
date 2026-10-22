"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRouteLoadBalancerSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class GatewayRouteLoadBalancerSecurityGroup(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the security group.</p>"""
    rule_arns: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The Amazon Resource Names (ARNs) of the security group rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRouteLoadBalancerSecurityGroup) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "rule_arns" in value:
        import capo_ecs.types.string_list

        out["ruleArns"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["rule_arns"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayRouteLoadBalancerSecurityGroup:
    out: GatewayRouteLoadBalancerSecurityGroup = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("ruleArns") is not None:
        import capo_ecs.types.string_list

        out["rule_arns"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["ruleArns"]
        )
    return out
