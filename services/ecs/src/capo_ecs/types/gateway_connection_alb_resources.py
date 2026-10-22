"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectionAlbResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class GatewayConnectionAlbResources(TypedDict, closed=True):
    acm_certificate_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Certificate Manager certificate that is attached to the load balancer listener.</p>"""
    load_balancer_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    load_balancer_security_group_arns: NotRequired[
        "capo_ecs.types.string_list.StringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the security groups that the gateway attaches to the load balancer.</p>"""
    listener_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the listener on the load balancer.</p>"""
    listener_rule_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the listener rule that routes production traffic to the service.</p>"""
    test_listener_rule_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the listener rule that routes test traffic to the service during progressive deployments.</p>"""
    target_group_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target group that receives production traffic.</p>"""
    alternate_target_group_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the alternate target group that the gateway uses during progressive deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectionAlbResources) -> dict:
    out: dict = {}
    if "acm_certificate_arn" in value:
        out["acmCertificateArn"] = value["acm_certificate_arn"]
    if "load_balancer_arn" in value:
        out["loadBalancerArn"] = value["load_balancer_arn"]
    if "load_balancer_security_group_arns" in value:
        import capo_ecs.types.string_list

        out["loadBalancerSecurityGroupArns"] = (
            capo_ecs.types.string_list.serialize_aws_json_1_1(
                value["load_balancer_security_group_arns"]
            )
        )
    if "listener_arn" in value:
        out["listenerArn"] = value["listener_arn"]
    if "listener_rule_arn" in value:
        out["listenerRuleArn"] = value["listener_rule_arn"]
    if "test_listener_rule_arn" in value:
        out["testListenerRuleArn"] = value["test_listener_rule_arn"]
    if "target_group_arn" in value:
        out["targetGroupArn"] = value["target_group_arn"]
    if "alternate_target_group_arn" in value:
        out["alternateTargetGroupArn"] = value["alternate_target_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayConnectionAlbResources:
    out: GatewayConnectionAlbResources = {}  # type: ignore[typeddict-item]
    if data.get("acmCertificateArn") is not None:
        out["acm_certificate_arn"] = data["acmCertificateArn"]
    if data.get("loadBalancerArn") is not None:
        out["load_balancer_arn"] = data["loadBalancerArn"]
    if data.get("loadBalancerSecurityGroupArns") is not None:
        import capo_ecs.types.string_list

        out["load_balancer_security_group_arns"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["loadBalancerSecurityGroupArns"]
            )
        )
    if data.get("listenerArn") is not None:
        out["listener_arn"] = data["listenerArn"]
    if data.get("listenerRuleArn") is not None:
        out["listener_rule_arn"] = data["listenerRuleArn"]
    if data.get("testListenerRuleArn") is not None:
        out["test_listener_rule_arn"] = data["testListenerRuleArn"]
    if data.get("targetGroupArn") is not None:
        out["target_group_arn"] = data["targetGroupArn"]
    if data.get("alternateTargetGroupArn") is not None:
        out["alternate_target_group_arn"] = data["alternateTargetGroupArn"]
    return out
