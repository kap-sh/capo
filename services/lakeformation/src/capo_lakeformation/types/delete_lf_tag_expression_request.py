"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeleteLFTagExpressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string


class DeleteLFTagExpressionRequest(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name for the LF-Tag expression.</p>"""
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID in which the LF-Tag expression is saved. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLFTagExpressionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_json(data: dict) -> DeleteLFTagExpressionRequest:
    out: DeleteLFTagExpressionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    return out
