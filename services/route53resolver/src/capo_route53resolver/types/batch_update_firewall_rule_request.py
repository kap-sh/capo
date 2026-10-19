"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchUpdateFirewallRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.update_firewall_rule_entries


class BatchUpdateFirewallRuleRequest(TypedDict, closed=True):
    update_firewall_rule_entries: "capo_route53resolver.types.update_firewall_rule_entries.UpdateFirewallRuleEntries"
    """<p>The list of firewall rules to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdateFirewallRuleRequest) -> dict:
    out: dict = {}
    import capo_route53resolver.types.update_firewall_rule_entries

    out["UpdateFirewallRuleEntries"] = (
        capo_route53resolver.types.update_firewall_rule_entries.serialize_aws_json_1_1(
            value["update_firewall_rule_entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdateFirewallRuleRequest:
    out: BatchUpdateFirewallRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("UpdateFirewallRuleEntries") is not None:
        import capo_route53resolver.types.update_firewall_rule_entries

        out["update_firewall_rule_entries"] = (
            capo_route53resolver.types.update_firewall_rule_entries.deserialize_aws_json_1_1(
                data["UpdateFirewallRuleEntries"]
            )
        )
    else:
        out["update_firewall_rule_entries"] = []
    return out
