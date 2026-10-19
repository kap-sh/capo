"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueSuccessEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_value
    import capo_iotsitewise.types.entry_id


class BatchGetAssetPropertyValueSuccessEntry(TypedDict, closed=True):
    entry_id: "capo_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""
    asset_property_value: NotRequired[
        "capo_iotsitewise.types.asset_property_value.AssetPropertyValue"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueSuccessEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    if "asset_property_value" in value:
        import capo_iotsitewise.types.asset_property_value

        out["assetPropertyValue"] = (
            capo_iotsitewise.types.asset_property_value.serialize_json(
                value["asset_property_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueSuccessEntry:
    out: BatchGetAssetPropertyValueSuccessEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        out["entry_id"] = ""
    if data.get("assetPropertyValue") is not None:
        import capo_iotsitewise.types.asset_property_value

        out["asset_property_value"] = (
            capo_iotsitewise.types.asset_property_value.deserialize_json(
                data["assetPropertyValue"]
            )
        )
    return out
