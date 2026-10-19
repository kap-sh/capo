"""Generated from Smithy shape ``com.amazonaws.lakeformation#DatabaseResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string


class DatabaseResource(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, it is the account ID of the caller.</p>"""
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the database resource. Unique to the Data Catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DatabaseResource:
    out: DatabaseResource = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
