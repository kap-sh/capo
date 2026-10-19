"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatelessRuleGroupReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.priority
    import capo_network_firewall.types.resource_arn


class StatelessRuleGroupReference(TypedDict, closed=True):
    resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the stateless rule group.</p>"""
    priority: "capo_network_firewall.types.priority.Priority"
    """<p>An integer setting that indicates the order in which to run the stateless rule groups in a single <a>FirewallPolicy</a>. Network Firewall applies each stateless rule group to a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatelessRuleGroupReference) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Priority"] = value["priority"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StatelessRuleGroupReference:
    out: StatelessRuleGroupReference = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    return out
