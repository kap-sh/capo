"""Generated from Smithy shape ``com.amazonaws.dataexchange#UpdateAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.asset_name
    import capo_dataexchange.types.id


class UpdateAssetRequest(TypedDict, closed=True):
    asset_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for an asset.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""
    name: "capo_dataexchange.types.asset_name.AssetName"
    """<p>The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target Amazon S3 object key. When importing from Amazon API Gateway API, the API name is used as the asset name. When importing from Amazon Redshift, the datashare name is used as the asset name. When importing from AWS Lake Formation, the static values of "Database(s) included in the LF-tag policy" or "Table(s) included in LF-tag policy" are used as the name.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateAssetRequest:
    out: UpdateAssetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateAssetRequest.name required")
    return out
