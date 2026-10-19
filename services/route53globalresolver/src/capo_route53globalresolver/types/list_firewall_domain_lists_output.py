"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListFirewallDomainListsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.firewall_domain_lists


class ListFirewallDomainListsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    firewall_domain_lists: (
        "capo_route53globalresolver.types.firewall_domain_lists.FirewallDomainLists"
    )
    """<p>List of the DNS Firewall domain lists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFirewallDomainListsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_route53globalresolver.types.firewall_domain_lists

    out["firewallDomainLists"] = (
        capo_route53globalresolver.types.firewall_domain_lists.serialize_json(
            value["firewall_domain_lists"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListFirewallDomainListsOutput:
    out: ListFirewallDomainListsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("firewallDomainLists") is not None:
        import capo_route53globalresolver.types.firewall_domain_lists

        out["firewall_domain_lists"] = (
            capo_route53globalresolver.types.firewall_domain_lists.deserialize_json(
                data["firewallDomainLists"]
            )
        )
    else:
        out["firewall_domain_lists"] = []
    return out
