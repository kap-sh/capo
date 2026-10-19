"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchCreateFirewallRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.batch_create_firewall_rule_output_items


class BatchCreateFirewallRuleOutput(TypedDict, closed=True):
    failures: "capo_route53globalresolver.types.batch_create_firewall_rule_output_items.BatchCreateFirewallRuleOutputItems"
    """<p>High level information about the DNS Firewall rules that failed to create.</p>"""
    successes: "capo_route53globalresolver.types.batch_create_firewall_rule_output_items.BatchCreateFirewallRuleOutputItems"
    """<p>High level information about the DNS Firewall rules that were created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateFirewallRuleOutput) -> dict:
    out: dict = {}
    import capo_route53globalresolver.types.batch_create_firewall_rule_output_items

    out["failures"] = (
        capo_route53globalresolver.types.batch_create_firewall_rule_output_items.serialize_json(
            value["failures"]
        )
    )
    import capo_route53globalresolver.types.batch_create_firewall_rule_output_items

    out["successes"] = (
        capo_route53globalresolver.types.batch_create_firewall_rule_output_items.serialize_json(
            value["successes"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateFirewallRuleOutput:
    out: BatchCreateFirewallRuleOutput = {}  # type: ignore[typeddict-item]
    if data.get("failures") is not None:
        import capo_route53globalresolver.types.batch_create_firewall_rule_output_items

        out["failures"] = (
            capo_route53globalresolver.types.batch_create_firewall_rule_output_items.deserialize_json(
                data["failures"]
            )
        )
    else:
        out["failures"] = []
    if data.get("successes") is not None:
        import capo_route53globalresolver.types.batch_create_firewall_rule_output_items

        out["successes"] = (
            capo_route53globalresolver.types.batch_create_firewall_rule_output_items.deserialize_json(
                data["successes"]
            )
        )
    else:
        out["successes"] = []
    return out
