"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.owner_id
    import capo_elasticsearch_service.types.region


class DomainInformation(TypedDict, closed=True):
    owner_id: NotRequired["capo_elasticsearch_service.types.owner_id.OwnerId"]
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    region: NotRequired["capo_elasticsearch_service.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: DomainInformation) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    out["DomainName"] = value["domain_name"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> DomainInformation:
    out: DomainInformation = {}  # type: ignore[typeddict-item]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    return out
