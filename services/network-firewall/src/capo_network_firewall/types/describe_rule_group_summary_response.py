"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeRuleGroupSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.description
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.summary


class DescribeRuleGroupSummaryResponse(TypedDict, closed=True):
    rule_group_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the rule group. </p>"""
    summary: NotRequired["capo_network_firewall.types.summary.Summary"]
    """<p>A complex type that contains rule information based on the rule group's configured summary settings. The content varies depending on the fields that you specified to extract in your SummaryConfiguration. When you haven't configured any summary settings, this returns an empty array. The response might include:</p> <ul> <li> <p>Rule identifiers</p> </li> <li> <p>Rule descriptions</p> </li> <li> <p>Any metadata fields that you specified in your SummaryConfiguration</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRuleGroupSummaryResponse) -> dict:
    out: dict = {}
    out["RuleGroupName"] = value["rule_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "summary" in value:
        import capo_network_firewall.types.summary

        out["Summary"] = capo_network_firewall.types.summary.serialize_aws_json_1_0(
            value["summary"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRuleGroupSummaryResponse:
    out: DescribeRuleGroupSummaryResponse = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
    else:
        out["rule_group_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Summary") is not None:
        import capo_network_firewall.types.summary

        out["summary"] = capo_network_firewall.types.summary.deserialize_aws_json_1_0(
            data["Summary"]
        )
    return out
