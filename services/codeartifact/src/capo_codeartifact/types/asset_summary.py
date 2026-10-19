"""Generated from Smithy shape ``com.amazonaws.codeartifact#AssetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.asset_hashes
    import capo_codeartifact.types.asset_name
    import capo_codeartifact.types.long_optional


class AssetSummary(TypedDict, closed=True):
    name: "capo_codeartifact.types.asset_name.AssetName"
    """<p> The name of the asset. </p>"""
    size: NotRequired["capo_codeartifact.types.long_optional.LongOptional"]
    """<p> The size of the asset. </p>"""
    hashes: NotRequired["capo_codeartifact.types.asset_hashes.AssetHashes"]
    """<p> The hashes of the asset. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "size" in value:
        out["size"] = value["size"]
    if "hashes" in value:
        import capo_codeartifact.types.asset_hashes

        out["hashes"] = capo_codeartifact.types.asset_hashes.serialize_json(
            value["hashes"]
        )
    return out


def deserialize_json(data: dict) -> AssetSummary:
    out: AssetSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("size") is not None:
        out["size"] = data["size"]
    if data.get("hashes") is not None:
        import capo_codeartifact.types.asset_hashes

        out["hashes"] = capo_codeartifact.types.asset_hashes.deserialize_json(
            data["hashes"]
        )
    return out
