"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetFromSignedUrlJobErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.asset_name


class ImportAssetFromSignedUrlJobErrorDetails(TypedDict, closed=True):
    asset_name: "capo_dataexchange.types.asset_name.AssetName"
    """<p>Details about the job error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetFromSignedUrlJobErrorDetails) -> dict:
    out: dict = {}
    out["AssetName"] = value["asset_name"]
    return out


def deserialize_json(data: dict) -> ImportAssetFromSignedUrlJobErrorDetails:
    out: ImportAssetFromSignedUrlJobErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("AssetName") is not None:
        out["asset_name"] = data["AssetName"]
    else:
        out["asset_name"] = ""
    return out
