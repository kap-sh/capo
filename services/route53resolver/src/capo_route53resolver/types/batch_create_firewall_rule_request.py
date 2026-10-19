"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchCreateFirewallRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.create_firewall_rule_entries


class BatchCreateFirewallRuleRequest(TypedDict, closed=True):
    create_firewall_rule_entries: "capo_route53resolver.types.create_firewall_rule_entries.CreateFirewallRuleEntries"
    """<p>The list of firewall rules to create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreateFirewallRuleRequest) -> dict:
    out: dict = {}
    import capo_route53resolver.types.create_firewall_rule_entries

    out["CreateFirewallRuleEntries"] = (
        capo_route53resolver.types.create_firewall_rule_entries.serialize_aws_json_1_1(
            value["create_firewall_rule_entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCreateFirewallRuleRequest:
    out: BatchCreateFirewallRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("CreateFirewallRuleEntries") is not None:
        import capo_route53resolver.types.create_firewall_rule_entries

        out["create_firewall_rule_entries"] = (
            capo_route53resolver.types.create_firewall_rule_entries.deserialize_aws_json_1_1(
                data["CreateFirewallRuleEntries"]
            )
        )
    else:
        out["create_firewall_rule_entries"] = []
    return out
