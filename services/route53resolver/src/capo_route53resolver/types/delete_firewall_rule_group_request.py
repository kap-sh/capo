"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteFirewallRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class DeleteFirewallRuleGroupRequest(TypedDict, closed=True):
    firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the firewall rule group that you want to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFirewallRuleGroupRequest) -> dict:
    out: dict = {}
    out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFirewallRuleGroupRequest:
    out: DeleteFirewallRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallRuleGroupId") is not None:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    else:
        out["firewall_rule_group_id"] = ""
    return out
