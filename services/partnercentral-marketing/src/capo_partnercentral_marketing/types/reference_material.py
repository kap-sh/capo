"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ReferenceMaterial``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_name


class ReferenceMaterial(TypedDict, closed=True):
    name: "capo_partnercentral_marketing.types.asset_name.AssetName"
    """The display name."""
    url: NotRequired["str"]
    """A stable public CDN URL for the file. AWS-authored content, so it is not presigned and carries no expiry — the same treatment as `LayoutPreview.url`, and withheld on the same condition: absent while the template's `EffectiveDateBegin` is in the future."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReferenceMaterial) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_cbor(data: dict) -> ReferenceMaterial:
    out: ReferenceMaterial = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out
