"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRouteAlbResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route_load_balancer_security_group_list
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class GatewayRouteAlbResources(TypedDict, closed=True):
    acm_certificate_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Certificate Manager certificate.</p>"""
    load_balancer_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    listener_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    listener_rule_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the listener rule for production traffic.</p>"""
    test_listener_rule_arns: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The Amazon Resource Names (ARNs) of the listener rules for test traffic. There is one rule except when a test header configuration is being changed to another.</p>"""
    load_balancer_security_groups: NotRequired[
        "capo_ecs.types.gateway_route_load_balancer_security_group_list.GatewayRouteLoadBalancerSecurityGroupList"
    ]
    """<p>The security groups attached to the load balancer.</p>"""
    service_security_group_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service security group in which the gateway manages the ingress rule for this route.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRouteAlbResources) -> dict:
    out: dict = {}
    if "acm_certificate_arn" in value:
        out["acmCertificateArn"] = value["acm_certificate_arn"]
    if "load_balancer_arn" in value:
        out["loadBalancerArn"] = value["load_balancer_arn"]
    if "listener_arn" in value:
        out["listenerArn"] = value["listener_arn"]
    if "listener_rule_arn" in value:
        out["listenerRuleArn"] = value["listener_rule_arn"]
    if "test_listener_rule_arns" in value:
        import capo_ecs.types.string_list

        out["testListenerRuleArns"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["test_listener_rule_arns"]
        )
    if "load_balancer_security_groups" in value:
        import capo_ecs.types.gateway_route_load_balancer_security_group_list

        out["loadBalancerSecurityGroups"] = (
            capo_ecs.types.gateway_route_load_balancer_security_group_list.serialize_aws_json_1_1(
                value["load_balancer_security_groups"]
            )
        )
    if "service_security_group_arn" in value:
        out["serviceSecurityGroupArn"] = value["service_security_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayRouteAlbResources:
    out: GatewayRouteAlbResources = {}  # type: ignore[typeddict-item]
    if data.get("acmCertificateArn") is not None:
        out["acm_certificate_arn"] = data["acmCertificateArn"]
    if data.get("loadBalancerArn") is not None:
        out["load_balancer_arn"] = data["loadBalancerArn"]
    if data.get("listenerArn") is not None:
        out["listener_arn"] = data["listenerArn"]
    if data.get("listenerRuleArn") is not None:
        out["listener_rule_arn"] = data["listenerRuleArn"]
    if data.get("testListenerRuleArns") is not None:
        import capo_ecs.types.string_list

        out["test_listener_rule_arns"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["testListenerRuleArns"]
            )
        )
    if data.get("loadBalancerSecurityGroups") is not None:
        import capo_ecs.types.gateway_route_load_balancer_security_group_list

        out["load_balancer_security_groups"] = (
            capo_ecs.types.gateway_route_load_balancer_security_group_list.deserialize_aws_json_1_1(
                data["loadBalancerSecurityGroups"]
            )
        )
    if data.get("serviceSecurityGroupArn") is not None:
        out["service_security_group_arn"] = data["serviceSecurityGroupArn"]
    return out
