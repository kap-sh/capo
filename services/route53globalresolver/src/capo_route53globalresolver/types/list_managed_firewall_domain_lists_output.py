"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListManagedFirewallDomainListsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.managed_firewall_domain_lists


class ListManagedFirewallDomainListsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    managed_firewall_domain_lists: "capo_route53globalresolver.types.managed_firewall_domain_lists.ManagedFirewallDomainLists"
    """<p>List of the Managed Domain Lists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedFirewallDomainListsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_route53globalresolver.types.managed_firewall_domain_lists

    out["managedFirewallDomainLists"] = (
        capo_route53globalresolver.types.managed_firewall_domain_lists.serialize_json(
            value["managed_firewall_domain_lists"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListManagedFirewallDomainListsOutput:
    out: ListManagedFirewallDomainListsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("managedFirewallDomainLists") is not None:
        import capo_route53globalresolver.types.managed_firewall_domain_lists

        out["managed_firewall_domain_lists"] = (
            capo_route53globalresolver.types.managed_firewall_domain_lists.deserialize_json(
                data["managedFirewallDomainLists"]
            )
        )
    else:
        out["managed_firewall_domain_lists"] = []
    return out
