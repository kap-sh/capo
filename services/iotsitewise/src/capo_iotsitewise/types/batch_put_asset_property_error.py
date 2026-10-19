"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_put_asset_property_value_error_code
    import capo_iotsitewise.types.error_message
    import capo_iotsitewise.types.timestamps


class BatchPutAssetPropertyError(TypedDict, closed=True):
    error_code: "capo_iotsitewise.types.batch_put_asset_property_value_error_code.BatchPutAssetPropertyValueErrorCode"
    """<p>The error code.</p>"""
    error_message: "capo_iotsitewise.types.error_message.ErrorMessage"
    """<p>The associated error message.</p>"""
    timestamps: "capo_iotsitewise.types.timestamps.Timestamps"
    """<p>A list of timestamps for each error, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyError) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.batch_put_asset_property_value_error_code

    out["errorCode"] = (
        capo_iotsitewise.types.batch_put_asset_property_value_error_code.serialize_json(
            value["error_code"]
        )
    )
    out["errorMessage"] = value["error_message"]
    import capo_iotsitewise.types.timestamps

    out["timestamps"] = capo_iotsitewise.types.timestamps.serialize_json(
        value["timestamps"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutAssetPropertyError:
    out: BatchPutAssetPropertyError = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        import capo_iotsitewise.types.batch_put_asset_property_value_error_code

        out["error_code"] = (
            capo_iotsitewise.types.batch_put_asset_property_value_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_iotsitewise.types.batch_put_asset_property_value_error_code.BatchPutAssetPropertyValueErrorCode",
            "",
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    if data.get("timestamps") is not None:
        import capo_iotsitewise.types.timestamps

        out["timestamps"] = capo_iotsitewise.types.timestamps.deserialize_json(
            data["timestamps"]
        )
    else:
        out["timestamps"] = []
    return out
