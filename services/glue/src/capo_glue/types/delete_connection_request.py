"""Generated from Smithy shape ``com.amazonaws.glue#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string


class DeleteConnectionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    connection_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the connection to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["ConnectionName"] = value["connection_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    else:
        out["connection_name"] = ""
    return out
