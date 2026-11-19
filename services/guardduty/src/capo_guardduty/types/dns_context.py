"""Generated from Smithy shape ``com.amazonaws.guardduty#DnsContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class DnsContext(TypedDict, closed=True):
    domain_suffix: NotRequired["capo_guardduty.types.string.String"]
    """<p>The suffix of the domain that was queried.</p>"""
    other_domains: NotRequired["capo_guardduty.types.string.String"]
    """<p>Other domains that were queried.</p>"""
    resolver_history: NotRequired["capo_guardduty.types.string.String"]
    """<p>The DNS resolution history for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DnsContext) -> dict:
    out: dict = {}
    if "domain_suffix" in value:
        out["domainSuffix"] = value["domain_suffix"]
    if "other_domains" in value:
        out["otherDomains"] = value["other_domains"]
    if "resolver_history" in value:
        out["resolverHistory"] = value["resolver_history"]
    return out


def deserialize_json(data: dict) -> DnsContext:
    out: DnsContext = {}  # type: ignore[typeddict-item]
    if data.get("domainSuffix") is not None:
        out["domain_suffix"] = data["domainSuffix"]
    if data.get("otherDomains") is not None:
        out["other_domains"] = data["otherDomains"]
    if data.get("resolverHistory") is not None:
        out["resolver_history"] = data["resolverHistory"]
    return out
