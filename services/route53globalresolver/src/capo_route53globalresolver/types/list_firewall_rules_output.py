"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListFirewallRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.firewall_rules


class ListFirewallRulesOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    firewall_rules: "capo_route53globalresolver.types.firewall_rules.FirewallRules"
    """<p>List of the firewall rules and information about them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFirewallRulesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_route53globalresolver.types.firewall_rules

    out["firewallRules"] = (
        capo_route53globalresolver.types.firewall_rules.serialize_json(
            value["firewall_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListFirewallRulesOutput:
    out: ListFirewallRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("firewallRules") is not None:
        import capo_route53globalresolver.types.firewall_rules

        out["firewall_rules"] = (
            capo_route53globalresolver.types.firewall_rules.deserialize_json(
                data["firewallRules"]
            )
        )
    else:
        out["firewall_rules"] = []
    return out
