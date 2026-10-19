"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteDevicePositionHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.batch_delete_device_position_history_error_list


class BatchDeleteDevicePositionHistoryResponse(TypedDict, closed=True):
    errors: "capo_location.types.batch_delete_device_position_history_error_list.BatchDeleteDevicePositionHistoryErrorList"
    """<p>Contains error details for each device history that failed to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDevicePositionHistoryResponse) -> dict:
    out: dict = {}
    import capo_location.types.batch_delete_device_position_history_error_list

    out["Errors"] = (
        capo_location.types.batch_delete_device_position_history_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDevicePositionHistoryResponse:
    out: BatchDeleteDevicePositionHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_location.types.batch_delete_device_position_history_error_list

        out["errors"] = (
            capo_location.types.batch_delete_device_position_history_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    return out
