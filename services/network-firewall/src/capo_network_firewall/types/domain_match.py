"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DomainMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.tls_inspection_domains


class DomainMatch(TypedDict, closed=True):
    domains: "capo_network_firewall.types.tls_inspection_domains.TLSInspectionDomains"
    """<p>The domains to match. You can specify an exact domain, such as <code>example.com</code>, or a domain with a single leading wildcard label, such as <code>*.example.com</code>. You can specify from 1 to 50 domains, and each domain can be up to 255 characters long.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainMatch) -> dict:
    out: dict = {}
    import capo_network_firewall.types.tls_inspection_domains

    out["Domains"] = (
        capo_network_firewall.types.tls_inspection_domains.serialize_aws_json_1_0(
            value["domains"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DomainMatch:
    out: DomainMatch = {}  # type: ignore[typeddict-item]
    if data.get("Domains") is not None:
        import capo_network_firewall.types.tls_inspection_domains

        out["domains"] = (
            capo_network_firewall.types.tls_inspection_domains.deserialize_aws_json_1_0(
                data["Domains"]
            )
        )
    else:
        out["domains"] = []
    return out
