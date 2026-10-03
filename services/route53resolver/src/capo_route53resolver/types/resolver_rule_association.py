"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRuleAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.name
    import capo_route53resolver.types.resolver_rule_association_status
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.status_message


class ResolverRuleAssociation(TypedDict, closed=True):
    id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the association between a Resolver rule and a VPC. Resolver assigns this value when you submit an <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html">AssociateResolverRule</a> request.</p>"""
    resolver_rule_id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the Resolver rule that you associated with the VPC that is specified by <code>VPCId</code>.</p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>The name of an association between a Resolver rule and a VPC.</p> <p>The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (_), and spaces. The name cannot consist of only numbers.</p>"""
    vpc_id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the VPC that you associated the Resolver rule with.</p>"""
    status: NotRequired[
        "capo_route53resolver.types.resolver_rule_association_status.ResolverRuleAssociationStatus"
    ]
    """<p>A code that specifies the current status of the association between a Resolver rule and a VPC.</p>"""
    status_message: NotRequired[
        "capo_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>A detailed description of the status of the association between a Resolver rule and a VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverRuleAssociation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "resolver_rule_id" in value:
        out["ResolverRuleId"] = value["resolver_rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "vpc_id" in value:
        out["VPCId"] = value["vpc_id"]
    if "status" in value:
        import capo_route53resolver.types.resolver_rule_association_status

        out["Status"] = (
            capo_route53resolver.types.resolver_rule_association_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolverRuleAssociation:
    out: ResolverRuleAssociation = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ResolverRuleId") is not None:
        out["resolver_rule_id"] = data["ResolverRuleId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("VPCId") is not None:
        out["vpc_id"] = data["VPCId"]
    if data.get("Status") is not None:
        import capo_route53resolver.types.resolver_rule_association_status

        out["status"] = (
            capo_route53resolver.types.resolver_rule_association_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
