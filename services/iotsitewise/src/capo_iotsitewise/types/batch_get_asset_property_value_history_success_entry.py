"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistorySuccessEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_value_history
    import capo_iotsitewise.types.entry_id


class BatchGetAssetPropertyValueHistorySuccessEntry(TypedDict, closed=True):
    entry_id: "capo_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""
    asset_property_value_history: (
        "capo_iotsitewise.types.asset_property_value_history.AssetPropertyValueHistory"
    )
    """<p>The requested historical values for the specified asset property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistorySuccessEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    import capo_iotsitewise.types.asset_property_value_history

    out["assetPropertyValueHistory"] = (
        capo_iotsitewise.types.asset_property_value_history.serialize_json(
            value["asset_property_value_history"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueHistorySuccessEntry:
    out: BatchGetAssetPropertyValueHistorySuccessEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        out["entry_id"] = ""
    if data.get("assetPropertyValueHistory") is not None:
        import capo_iotsitewise.types.asset_property_value_history

        out["asset_property_value_history"] = (
            capo_iotsitewise.types.asset_property_value_history.deserialize_json(
                data["assetPropertyValueHistory"]
            )
        )
    else:
        out["asset_property_value_history"] = []
    return out
