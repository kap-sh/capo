"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.boolean_value
    import capo_iotsitewise.types.put_asset_property_value_entries


class BatchPutAssetPropertyValueRequest(TypedDict, closed=True):
    enable_partial_entry_processing: NotRequired[
        "capo_iotsitewise.types.boolean_value.BooleanValue"
    ]
    """<p>This setting enables partial ingestion at entry-level. If set to <code>true</code>, we ingest all TQVs not resulting in an error. If set to <code>false</code>, an invalid TQV fails ingestion of the entire entry that contains it.</p>"""
    entries: "capo_iotsitewise.types.put_asset_property_value_entries.PutAssetPropertyValueEntries"
    """<p>The list of asset property value entries for the batch put request. You can specify up to 10 entries per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyValueRequest) -> dict:
    out: dict = {}
    if "enable_partial_entry_processing" in value:
        out["enablePartialEntryProcessing"] = value["enable_partial_entry_processing"]
    import capo_iotsitewise.types.put_asset_property_value_entries

    out["entries"] = (
        capo_iotsitewise.types.put_asset_property_value_entries.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutAssetPropertyValueRequest:
    out: BatchPutAssetPropertyValueRequest = {}  # type: ignore[typeddict-item]
    if data.get("enablePartialEntryProcessing") is not None:
        out["enable_partial_entry_processing"] = data["enablePartialEntryProcessing"]
    if data.get("entries") is not None:
        import capo_iotsitewise.types.put_asset_property_value_entries

        out["entries"] = (
            capo_iotsitewise.types.put_asset_property_value_entries.deserialize_json(
                data["entries"]
            )
        )
    else:
        out["entries"] = []
    return out
