"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistoryErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_error_code
    import capo_iotsitewise.types.timestamp


class BatchGetAssetPropertyValueHistoryErrorInfo(TypedDict, closed=True):
    error_code: "capo_iotsitewise.types.batch_get_asset_property_value_history_error_code.BatchGetAssetPropertyValueHistoryErrorCode"
    """<p>The error code.</p>"""
    error_timestamp: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the error occurred, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistoryErrorInfo) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.batch_get_asset_property_value_history_error_code

    out["errorCode"] = (
        capo_iotsitewise.types.batch_get_asset_property_value_history_error_code.serialize_json(
            value["error_code"]
        )
    )
    import capo_iotsitewise.types.timestamp

    out["errorTimestamp"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["error_timestamp"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueHistoryErrorInfo:
    out: BatchGetAssetPropertyValueHistoryErrorInfo = {}  # type: ignore[typeddict-item]
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
    if data.get("errorTimestamp") is not None:
        import capo_iotsitewise.types.timestamp

        out["error_timestamp"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["errorTimestamp"]
        )
    else:
        import datetime

        out["error_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
