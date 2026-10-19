"""Generated from Smithy shape ``com.amazonaws.opensearch#AWSDomainInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.owner_id
    import capo_opensearch.types.region


class AWSDomainInformation(TypedDict, closed=True):
    owner_id: NotRequired["capo_opensearch.types.owner_id.OwnerId"]
    """<p>The Amazon Web Services account ID of the domain owner.</p>"""
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>Name of the domain.</p>"""
    region: NotRequired["capo_opensearch.types.region.Region"]
    """<p>The Amazon Web Services Region in which the domain is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AWSDomainInformation) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    out["DomainName"] = value["domain_name"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> AWSDomainInformation:
    out: AWSDomainInformation = {}  # type: ignore[typeddict-item]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    return out
