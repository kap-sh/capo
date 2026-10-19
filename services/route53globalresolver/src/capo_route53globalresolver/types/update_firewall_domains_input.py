"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateFirewallDomainsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.domains
    import capo_route53globalresolver.types.resource_id


class UpdateFirewallDomainsInput(TypedDict, closed=True):
    domains: "capo_route53globalresolver.types.domains.Domains"
    """<p>A list of the domains. You can add up to 1000 domains per request.</p>"""
    firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS Firewall domain list to which you want to add the domains.</p>"""
    operation: "str"
    """<p>The operation for updating the domain list. The allowed values are ADD, REMOVE, and REPLACE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFirewallDomainsInput) -> dict:
    out: dict = {}
    import capo_route53globalresolver.types.domains

    out["domains"] = capo_route53globalresolver.types.domains.serialize_json(
        value["domains"]
    )
    out["operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> UpdateFirewallDomainsInput:
    out: UpdateFirewallDomainsInput = {}  # type: ignore[typeddict-item]
    if data.get("domains") is not None:
        import capo_route53globalresolver.types.domains

        out["domains"] = capo_route53globalresolver.types.domains.deserialize_json(
            data["domains"]
        )
    else:
        out["domains"] = []
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    else:
        out["operation"] = ""
    return out
