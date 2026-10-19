"""Generated from Smithy shape ``com.amazonaws.glue#DeleteCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string


class DeleteCatalogRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCatalogRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCatalogRequest:
    out: DeleteCatalogRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        out["catalog_id"] = ""
    return out
