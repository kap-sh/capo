"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateFirewallRuleGroupAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.mutation_protection_status
    import capo_route53resolver.types.name
    import capo_route53resolver.types.priority
    import capo_route53resolver.types.resource_id


class UpdateFirewallRuleGroupAssociationRequest(TypedDict, closed=True):
    firewall_rule_group_association_id: (
        "capo_route53resolver.types.resource_id.ResourceId"
    )
    """<p>The identifier of the <a>FirewallRuleGroupAssociation</a>. </p>"""
    priority: NotRequired["capo_route53resolver.types.priority.Priority"]
    """<p>The setting that determines the processing order of the rule group among the rule groups that you associate with the specified VPC. DNS Firewall filters VPC traffic starting from the rule group with the lowest numeric priority setting. </p> <p>You must specify a unique priority for each rule group that you associate with a single VPC. To make it easier to insert rule groups later, leave space between the numbers, for example, use 100, 200, and so on. You can change the priority setting for a rule group association after you create it.</p>"""
    mutation_protection: NotRequired[
        "capo_route53resolver.types.mutation_protection_status.MutationProtectionStatus"
    ]
    """<p>If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. </p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>The name of the rule group association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFirewallRuleGroupAssociationRequest) -> dict:
    out: dict = {}
    out["FirewallRuleGroupAssociationId"] = value["firewall_rule_group_association_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "mutation_protection" in value:
        import capo_route53resolver.types.mutation_protection_status

        out["MutationProtection"] = (
            capo_route53resolver.types.mutation_protection_status.serialize_aws_json_1_1(
                value["mutation_protection"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFirewallRuleGroupAssociationRequest:
    out: UpdateFirewallRuleGroupAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallRuleGroupAssociationId") is not None:
        out["firewall_rule_group_association_id"] = data[
            "FirewallRuleGroupAssociationId"
        ]
    else:
        out["firewall_rule_group_association_id"] = ""
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("MutationProtection") is not None:
        import capo_route53resolver.types.mutation_protection_status

        out["mutation_protection"] = (
            capo_route53resolver.types.mutation_protection_status.deserialize_aws_json_1_1(
                data["MutationProtection"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
