"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetFromSignedUrlRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093
    import capo_dataexchange.types.asset_name
    import capo_dataexchange.types.id


class ImportAssetFromSignedUrlRequestDetails(TypedDict, closed=True):
    asset_name: "capo_dataexchange.types.asset_name.AssetName"
    """<p>The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this import job.</p>"""
    md5_hash: "capo_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093.__stringMin24Max24PatternAZaZ094AZaZ092AZaZ093"
    """<p>The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this import request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetFromSignedUrlRequestDetails) -> dict:
    out: dict = {}
    out["AssetName"] = value["asset_name"]
    out["DataSetId"] = value["data_set_id"]
    out["Md5Hash"] = value["md5_hash"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ImportAssetFromSignedUrlRequestDetails:
    out: ImportAssetFromSignedUrlRequestDetails = {}  # type: ignore[typeddict-item]
    if data.get("AssetName") is not None:
        out["asset_name"] = data["AssetName"]
    else:
        out["asset_name"] = ""
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("Md5Hash") is not None:
        out["md5_hash"] = data["Md5Hash"]
    else:
        out["md5_hash"] = ""
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        out["revision_id"] = ""
    return out
