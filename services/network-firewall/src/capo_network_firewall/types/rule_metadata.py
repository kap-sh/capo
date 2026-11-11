"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.rule_description_text
    import capo_network_firewall.types.rule_enabled


class RuleMetadata(TypedDict, closed=True):
    rule_enabled: NotRequired["capo_network_firewall.types.rule_enabled.RuleEnabled"]
    """<p>Specifies whether the rule is active. The default is <code>TRUE</code>. When you set this to <code>FALSE</code>, Network Firewall keeps the rule in the rule group but doesn't evaluate it against traffic and doesn't count it toward the rule group's consumed capacity.</p>"""
    rule_description: NotRequired[
        "capo_network_firewall.types.rule_description_text.RuleDescriptionText"
    ]
    """<p>A description of the rule, up to 512 characters. The description can span multiple lines. A description line can't itself look like a firewall rule; to disable a rule, set <code>RuleEnabled</code> to <code>FALSE</code> instead.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleMetadata) -> dict:
    out: dict = {}
    if "rule_enabled" in value:
        out["RuleEnabled"] = value["rule_enabled"]
    if "rule_description" in value:
        out["RuleDescription"] = value["rule_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleMetadata:
    out: RuleMetadata = {}  # type: ignore[typeddict-item]
    if data.get("RuleEnabled") is not None:
        out["rule_enabled"] = data["RuleEnabled"]
    if data.get("RuleDescription") is not None:
        out["rule_description"] = data["RuleDescription"]
    return out
