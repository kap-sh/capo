"""Generated from Smithy shape ``com.amazonaws.guardduty#DnsRequestAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.boolean
    import capo_guardduty.types.string


class DnsRequestAction(TypedDict, closed=True):
    domain: NotRequired["capo_guardduty.types.string.String"]
    """<p>The domain information for the DNS query.</p>"""
    protocol: NotRequired["capo_guardduty.types.string.String"]
    """<p>The network connection protocol observed in the activity that prompted GuardDuty to generate the finding.</p>"""
    blocked: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates whether the targeted port is blocked.</p>"""
    domain_with_suffix: NotRequired["capo_guardduty.types.string.String"]
    """<p>The second and top level domain involved in the activity that potentially prompted GuardDuty to generate this finding. For a list of top-level and second-level domains, see <a href="https://publicsuffix.org/">public suffix list</a>.</p>"""
    vpc_owner_account_id: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the VPC through which the DNS request was made.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DnsRequestAction) -> dict:
    out: dict = {}
    if "domain" in value:
        out["domain"] = value["domain"]
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "blocked" in value:
        out["blocked"] = value["blocked"]
    if "domain_with_suffix" in value:
        out["domainWithSuffix"] = value["domain_with_suffix"]
    if "vpc_owner_account_id" in value:
        out["vpcOwnerAccountId"] = value["vpc_owner_account_id"]
    return out


def deserialize_json(data: dict) -> DnsRequestAction:
    out: DnsRequestAction = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    if data.get("blocked") is not None:
        out["blocked"] = data["blocked"]
    if data.get("domainWithSuffix") is not None:
        out["domain_with_suffix"] = data["domainWithSuffix"]
    if data.get("vpcOwnerAccountId") is not None:
        out["vpc_owner_account_id"] = data["vpcOwnerAccountId"]
    return out
