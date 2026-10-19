"""Generated from Smithy shape ``com.amazonaws.route53resolver#DisassociateFirewallRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class DisassociateFirewallRuleGroupRequest(TypedDict, closed=True):
    firewall_rule_group_association_id: (
        "capo_route53resolver.types.resource_id.ResourceId"
    )
    """<p>The identifier of the <a>FirewallRuleGroupAssociation</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFirewallRuleGroupRequest) -> dict:
    out: dict = {}
    out["FirewallRuleGroupAssociationId"] = value["firewall_rule_group_association_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFirewallRuleGroupRequest:
    out: DisassociateFirewallRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallRuleGroupAssociationId") is not None:
        out["firewall_rule_group_association_id"] = data[
            "FirewallRuleGroupAssociationId"
        ]
    else:
        out["firewall_rule_group_association_id"] = ""
    return out
