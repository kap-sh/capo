"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistoryErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_error_code
    import capo_iotsitewise.types.entry_id
    import capo_iotsitewise.types.error_message


class BatchGetAssetPropertyValueHistoryErrorEntry(TypedDict, closed=True):
    error_code: "capo_iotsitewise.types.batch_get_asset_property_value_history_error_code.BatchGetAssetPropertyValueHistoryErrorCode"
    """<p>The error code.</p>"""
    error_message: "capo_iotsitewise.types.error_message.ErrorMessage"
    """<p>The associated error message.</p>"""
    entry_id: "capo_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistoryErrorEntry) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.batch_get_asset_property_value_history_error_code

    out["errorCode"] = (
        capo_iotsitewise.types.batch_get_asset_property_value_history_error_code.serialize_json(
            value["error_code"]
        )
    )
    out["errorMessage"] = value["error_message"]
    out["entryId"] = value["entry_id"]
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueHistoryErrorEntry:
    out: BatchGetAssetPropertyValueHistoryErrorEntry = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        import capo_iotsitewise.types.batch_get_asset_property_value_history_error_code

        out["error_code"] = (
            capo_iotsitewise.types.batch_get_asset_property_value_history_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_iotsitewise.types.batch_get_asset_property_value_history_error_code.BatchGetAssetPropertyValueHistoryErrorCode",
            "",
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        out["entry_id"] = ""
    return out
