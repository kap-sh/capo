"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.catalog
    import capo_marketplace_catalog.types.entity_id


class EntityRequest(TypedDict, closed=True):
    catalog: "capo_marketplace_catalog.types.catalog.Catalog"
    """<p>The name of the catalog the entity is present in. The only value at this time is <code>AWSMarketplace</code>.</p>"""
    entity_id: "capo_marketplace_catalog.types.entity_id.EntityId"
    """<p>The ID of the entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntityRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["EntityId"] = value["entity_id"]
    return out


def deserialize_json(data: dict) -> EntityRequest:
    out: EntityRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    else:
        out["entity_id"] = ""
    return out
