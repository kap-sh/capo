"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ImportFirewallDomainsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_id


class ImportFirewallDomainsInput(TypedDict, closed=True):
    domain_file_url: "str"
    """<p>The fully qualified URL of the file in Amazon S3 that contains the list of domains to import. The file should contain one domain per line.</p>"""
    firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the DNS Firewall domain list that you want to import the domain list to.</p>"""
    operation: "str"
    """<p>This value is <code>REPLACE</code>, and it updates the domain list to match the list of domains in the imported file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportFirewallDomainsInput) -> dict:
    out: dict = {}
    out["domainFileUrl"] = value["domain_file_url"]
    out["operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> ImportFirewallDomainsInput:
    out: ImportFirewallDomainsInput = {}  # type: ignore[typeddict-item]
    if data.get("domainFileUrl") is not None:
        out["domain_file_url"] = data["domainFileUrl"]
    else:
        out["domain_file_url"] = ""
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    else:
        out["operation"] = ""
    return out
