"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_asset_download_url
    import capo_socialmessaging.types.meta_flow_asset_name
    import capo_socialmessaging.types.meta_flow_asset_type


class MetaFlowAsset(TypedDict, closed=True):
    name: "capo_socialmessaging.types.meta_flow_asset_name.MetaFlowAssetName"
    """<p>The filename of the asset (for example, flow.json).</p>"""
    asset_type: "capo_socialmessaging.types.meta_flow_asset_type.MetaFlowAssetType"
    """<p>The type of asset. Currently the only supported value is FLOW_JSON.</p>"""
    download_url: "capo_socialmessaging.types.meta_flow_asset_download_url.MetaFlowAssetDownloadUrl"
    """<p>A presigned URL from Meta for downloading the asset. The URL expires after a short period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowAsset) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["assetType"] = value["asset_type"]
    out["downloadUrl"] = value["download_url"]
    return out


def deserialize_json(data: dict) -> MetaFlowAsset:
    out: MetaFlowAsset = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("assetType") is not None:
        out["asset_type"] = data["assetType"]
    else:
        out["asset_type"] = ""
    if data.get("downloadUrl") is not None:
        out["download_url"] = data["downloadUrl"]
    else:
        out["download_url"] = ""
    return out
