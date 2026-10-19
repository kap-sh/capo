"""Generated from Smithy shape ``com.amazonaws.dataexchange#ExportAssetToSignedUrlResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.id
    import capo_dataexchange.types.timestamp


class ExportAssetToSignedUrlResponseDetails(TypedDict, closed=True):
    asset_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the asset associated with this export job.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this export job.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this export response.</p>"""
    signed_url: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The signed URL for the export request.</p>"""
    signed_url_expires_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the signed URL expires, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportAssetToSignedUrlResponseDetails) -> dict:
    out: dict = {}
    out["AssetId"] = value["asset_id"]
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    if "signed_url" in value:
        out["SignedUrl"] = value["signed_url"]
    if "signed_url_expires_at" in value:
        import capo_dataexchange.types.timestamp

        out["SignedUrlExpiresAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["signed_url_expires_at"]
        )
    return out


def deserialize_json(data: dict) -> ExportAssetToSignedUrlResponseDetails:
    out: ExportAssetToSignedUrlResponseDetails = {}  # type: ignore[typeddict-item]
    if data.get("AssetId") is not None:
        out["asset_id"] = data["AssetId"]
    else:
        out["asset_id"] = ""
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        out["revision_id"] = ""
    if data.get("SignedUrl") is not None:
        out["signed_url"] = data["SignedUrl"]
    if data.get("SignedUrlExpiresAt") is not None:
        import capo_dataexchange.types.timestamp

        out["signed_url_expires_at"] = (
            capo_dataexchange.types.timestamp.deserialize_json(
                data["SignedUrlExpiresAt"]
            )
        )
    return out
