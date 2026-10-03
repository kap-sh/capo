"""Generated from Smithy shape ``com.amazonaws.route53resolver#AssociateResolverRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.name
    import capo_route53resolver.types.resource_id


class AssociateResolverRuleRequest(TypedDict, closed=True):
    resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver rule that you want to associate with the VPC. To list the existing Resolver rules, use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html">ListResolverRules</a>.</p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>A name for the association that you're creating between a Resolver rule and a VPC.</p> <p>The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (_), and spaces. The name cannot consist of only numbers.</p>"""
    vpc_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the VPC that you want to associate the Resolver rule with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateResolverRuleRequest) -> dict:
    out: dict = {}
    out["ResolverRuleId"] = value["resolver_rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    out["VPCId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateResolverRuleRequest:
    out: AssociateResolverRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverRuleId") is not None:
        out["resolver_rule_id"] = data["ResolverRuleId"]
    else:
        raise DeserializationError(
            "AssociateResolverRuleRequest.resolver_rule_id required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("VPCId") is not None:
        out["vpc_id"] = data["VPCId"]
    else:
        raise DeserializationError("AssociateResolverRuleRequest.vpc_id required")
    return out
