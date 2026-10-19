"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchDeleteFirewallRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.delete_firewall_rule_entries


class BatchDeleteFirewallRuleRequest(TypedDict, closed=True):
    delete_firewall_rule_entries: "capo_route53resolver.types.delete_firewall_rule_entries.DeleteFirewallRuleEntries"
    """<p>The list of firewall rules to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteFirewallRuleRequest) -> dict:
    out: dict = {}
    import capo_route53resolver.types.delete_firewall_rule_entries

    out["DeleteFirewallRuleEntries"] = (
        capo_route53resolver.types.delete_firewall_rule_entries.serialize_aws_json_1_1(
            value["delete_firewall_rule_entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteFirewallRuleRequest:
    out: BatchDeleteFirewallRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeleteFirewallRuleEntries") is not None:
        import capo_route53resolver.types.delete_firewall_rule_entries

        out["delete_firewall_rule_entries"] = (
            capo_route53resolver.types.delete_firewall_rule_entries.deserialize_aws_json_1_1(
                data["DeleteFirewallRuleEntries"]
            )
        )
    else:
        out["delete_firewall_rule_entries"] = []
    return out
