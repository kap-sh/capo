"""Generated from Smithy shape ``com.amazonaws.guardduty#Enrichment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class Enrichment(TypedDict, closed=True):
    country_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the country associated with the activity.</p>"""
    asn_org: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the organization that owns the autonomous system number (ASN).</p>"""
    threat_list_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the threat list that contains the indicator.</p>"""
    threat_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the threat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Enrichment) -> dict:
    out: dict = {}
    if "country_name" in value:
        out["countryName"] = value["country_name"]
    if "asn_org" in value:
        out["asnOrg"] = value["asn_org"]
    if "threat_list_name" in value:
        out["threatListName"] = value["threat_list_name"]
    if "threat_name" in value:
        out["threatName"] = value["threat_name"]
    return out


def deserialize_json(data: dict) -> Enrichment:
    out: Enrichment = {}  # type: ignore[typeddict-item]
    if data.get("countryName") is not None:
        out["country_name"] = data["countryName"]
    if data.get("asnOrg") is not None:
        out["asn_org"] = data["asnOrg"]
    if data.get("threatListName") is not None:
        out["threat_list_name"] = data["threatListName"]
    if data.get("threatName") is not None:
        out["threat_name"] = data["threatName"]
    return out
