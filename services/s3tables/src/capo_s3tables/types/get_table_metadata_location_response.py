"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableMetadataLocationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.metadata_location
    import capo_s3tables.types.version_token
    import capo_s3tables.types.warehouse_location


class GetTableMetadataLocationResponse(TypedDict, closed=True):
    version_token: "capo_s3tables.types.version_token.VersionToken"
    """<p>The version token.</p>"""
    metadata_location: NotRequired[
        "capo_s3tables.types.metadata_location.MetadataLocation"
    ]
    """<p>The metadata location.</p>"""
    warehouse_location: "capo_s3tables.types.warehouse_location.WarehouseLocation"
    """<p>The warehouse location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableMetadataLocationResponse) -> dict:
    out: dict = {}
    out["versionToken"] = value["version_token"]
    if "metadata_location" in value:
        out["metadataLocation"] = value["metadata_location"]
    out["warehouseLocation"] = value["warehouse_location"]
    return out


def deserialize_json(data: dict) -> GetTableMetadataLocationResponse:
    out: GetTableMetadataLocationResponse = {}  # type: ignore[typeddict-item]
    if data.get("versionToken") is not None:
        out["version_token"] = data["versionToken"]
    else:
        out["version_token"] = ""
    if data.get("metadataLocation") is not None:
        out["metadata_location"] = data["metadataLocation"]
    if data.get("warehouseLocation") is not None:
        out["warehouse_location"] = data["warehouseLocation"]
    else:
        out["warehouse_location"] = ""
    return out
