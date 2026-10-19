"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedIngressPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.access_type
    import capo_ecs.types.managed_certificate
    import capo_ecs.types.managed_listener
    import capo_ecs.types.managed_listener_rule
    import capo_ecs.types.managed_load_balancer
    import capo_ecs.types.managed_security_groups
    import capo_ecs.types.managed_target_groups
    import capo_ecs.types.string


class ManagedIngressPath(TypedDict, closed=True):
    access_type: "capo_ecs.types.access_type.AccessType"
    """<p>The type of access to the endpoint for the Express service.</p>"""
    endpoint: "capo_ecs.types.string.String"
    """<p>The endpoint for access to the Express service.</p>"""
    load_balancer: NotRequired[
        "capo_ecs.types.managed_load_balancer.ManagedLoadBalancer"
    ]
    """<p>The Application Load Balancer associated with the Express service.</p>"""
    load_balancer_security_groups: NotRequired[
        "capo_ecs.types.managed_security_groups.ManagedSecurityGroups"
    ]
    """<p>The security groups associated with the Application Load Balancer.</p>"""
    certificate: NotRequired["capo_ecs.types.managed_certificate.ManagedCertificate"]
    """<p>The ACM certificate for the Express service's domain.</p>"""
    listener: NotRequired["capo_ecs.types.managed_listener.ManagedListener"]
    """<p>The listeners associated with the Application Load Balancer.</p>"""
    rule: NotRequired["capo_ecs.types.managed_listener_rule.ManagedListenerRule"]
    """<p>The listener rules for the Application Load Balancer.</p>"""
    target_groups: NotRequired[
        "capo_ecs.types.managed_target_groups.ManagedTargetGroups"
    ]
    """<p>The target groups associated with the Application Load Balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedIngressPath) -> dict:
    out: dict = {}
    import capo_ecs.types.access_type

    out["accessType"] = capo_ecs.types.access_type.serialize_aws_json_1_1(
        value["access_type"]
    )
    out["endpoint"] = value["endpoint"]
    if "load_balancer" in value:
        import capo_ecs.types.managed_load_balancer

        out["loadBalancer"] = (
            capo_ecs.types.managed_load_balancer.serialize_aws_json_1_1(
                value["load_balancer"]
            )
        )
    if "load_balancer_security_groups" in value:
        import capo_ecs.types.managed_security_groups

        out["loadBalancerSecurityGroups"] = (
            capo_ecs.types.managed_security_groups.serialize_aws_json_1_1(
                value["load_balancer_security_groups"]
            )
        )
    if "certificate" in value:
        import capo_ecs.types.managed_certificate

        out["certificate"] = capo_ecs.types.managed_certificate.serialize_aws_json_1_1(
            value["certificate"]
        )
    if "listener" in value:
        import capo_ecs.types.managed_listener

        out["listener"] = capo_ecs.types.managed_listener.serialize_aws_json_1_1(
            value["listener"]
        )
    if "rule" in value:
        import capo_ecs.types.managed_listener_rule

        out["rule"] = capo_ecs.types.managed_listener_rule.serialize_aws_json_1_1(
            value["rule"]
        )
    if "target_groups" in value:
        import capo_ecs.types.managed_target_groups

        out["targetGroups"] = (
            capo_ecs.types.managed_target_groups.serialize_aws_json_1_1(
                value["target_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedIngressPath:
    out: ManagedIngressPath = {}  # type: ignore[typeddict-item]
    if data.get("accessType") is not None:
        import capo_ecs.types.access_type

        out["access_type"] = capo_ecs.types.access_type.deserialize_aws_json_1_1(
            data["accessType"]
        )
    else:
        import typing

        out["access_type"] = typing.cast("capo_ecs.types.access_type.AccessType", "")
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("loadBalancer") is not None:
        import capo_ecs.types.managed_load_balancer

        out["load_balancer"] = (
            capo_ecs.types.managed_load_balancer.deserialize_aws_json_1_1(
                data["loadBalancer"]
            )
        )
    if data.get("loadBalancerSecurityGroups") is not None:
        import capo_ecs.types.managed_security_groups

        out["load_balancer_security_groups"] = (
            capo_ecs.types.managed_security_groups.deserialize_aws_json_1_1(
                data["loadBalancerSecurityGroups"]
            )
        )
    if data.get("certificate") is not None:
        import capo_ecs.types.managed_certificate

        out["certificate"] = (
            capo_ecs.types.managed_certificate.deserialize_aws_json_1_1(
                data["certificate"]
            )
        )
    if data.get("listener") is not None:
        import capo_ecs.types.managed_listener

        out["listener"] = capo_ecs.types.managed_listener.deserialize_aws_json_1_1(
            data["listener"]
        )
    if data.get("rule") is not None:
        import capo_ecs.types.managed_listener_rule

        out["rule"] = capo_ecs.types.managed_listener_rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    if data.get("targetGroups") is not None:
        import capo_ecs.types.managed_target_groups

        out["target_groups"] = (
            capo_ecs.types.managed_target_groups.deserialize_aws_json_1_1(
                data["targetGroups"]
            )
        )
    return out
