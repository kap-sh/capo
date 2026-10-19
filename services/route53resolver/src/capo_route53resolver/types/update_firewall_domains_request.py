"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateFirewallDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_domain_update_operation
    import capo_route53resolver.types.firewall_domains
    import capo_route53resolver.types.resource_id


class UpdateFirewallDomainsRequest(TypedDict, closed=True):
    firewall_domain_list_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the domain list whose domains you want to update. </p>"""
    operation: "capo_route53resolver.types.firewall_domain_update_operation.FirewallDomainUpdateOperation"
    """<p>What you want DNS Firewall to do with the domains that you are providing: </p> <ul> <li> <p> <code>ADD</code> - Add the domains to the ones that are already in the domain list. </p> </li> <li> <p> <code>REMOVE</code> - Search the domain list for the domains and remove them from the list.</p> </li> <li> <p> <code>REPLACE</code> - Update the domain list to exactly match the list that you are providing. </p> </li> </ul>"""
    domains: "capo_route53resolver.types.firewall_domains.FirewallDomains"
    """<p>A list of domains to use in the update operation.</p> <important> <p>There is a limit of 1000 domains per request.</p> </important> <p>Each domain specification in your domain list must satisfy the following requirements: </p> <ul> <li> <p>It can optionally start with <code>*</code> (asterisk).</p> </li> <li> <p>With the exception of the optional starting asterisk, it must only contain the following characters: <code>A-Z</code>, <code>a-z</code>, <code>0-9</code>, <code>-</code> (hyphen).</p> </li> <li> <p>It must be from 1-255 characters in length. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFirewallDomainsRequest) -> dict:
    out: dict = {}
    out["FirewallDomainListId"] = value["firewall_domain_list_id"]
    import capo_route53resolver.types.firewall_domain_update_operation

    out["Operation"] = (
        capo_route53resolver.types.firewall_domain_update_operation.serialize_aws_json_1_1(
            value["operation"]
        )
    )
    import capo_route53resolver.types.firewall_domains

    out["Domains"] = capo_route53resolver.types.firewall_domains.serialize_aws_json_1_1(
        value["domains"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFirewallDomainsRequest:
    out: UpdateFirewallDomainsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallDomainListId") is not None:
        out["firewall_domain_list_id"] = data["FirewallDomainListId"]
    else:
        out["firewall_domain_list_id"] = ""
    if data.get("Operation") is not None:
        import capo_route53resolver.types.firewall_domain_update_operation

        out["operation"] = (
            capo_route53resolver.types.firewall_domain_update_operation.deserialize_aws_json_1_1(
                data["Operation"]
            )
        )
    else:
        import typing

        out["operation"] = typing.cast(
            "capo_route53resolver.types.firewall_domain_update_operation.FirewallDomainUpdateOperation",
            "",
        )
    if data.get("Domains") is not None:
        import capo_route53resolver.types.firewall_domains

        out["domains"] = (
            capo_route53resolver.types.firewall_domains.deserialize_aws_json_1_1(
                data["Domains"]
            )
        )
    else:
        out["domains"] = []
    return out
