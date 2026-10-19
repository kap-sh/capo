"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_days
    import capo_connect.types.hours_of_operation_time_slice


class HoursOfOperationConfig(TypedDict, closed=True):
    day: "capo_connect.types.hours_of_operation_days.HoursOfOperationDays"
    """<p>The day that the hours of operation applies to.</p>"""
    start_time: (
        "capo_connect.types.hours_of_operation_time_slice.HoursOfOperationTimeSlice"
    )
    """<p>The start time that your contact center opens.</p>"""
    end_time: (
        "capo_connect.types.hours_of_operation_time_slice.HoursOfOperationTimeSlice"
    )
    """<p>The end time that your contact center closes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationConfig) -> dict:
    out: dict = {}
    import capo_connect.types.hours_of_operation_days

    out["Day"] = capo_connect.types.hours_of_operation_days.serialize_json(value["day"])
    import capo_connect.types.hours_of_operation_time_slice

    out["StartTime"] = capo_connect.types.hours_of_operation_time_slice.serialize_json(
        value["start_time"]
    )
    import capo_connect.types.hours_of_operation_time_slice

    out["EndTime"] = capo_connect.types.hours_of_operation_time_slice.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> HoursOfOperationConfig:
    out: HoursOfOperationConfig = {}  # type: ignore[typeddict-item]
    if data.get("Day") is not None:
        import capo_connect.types.hours_of_operation_days

        out["day"] = capo_connect.types.hours_of_operation_days.deserialize_json(
            data["Day"]
        )
    else:
        import typing

        out["day"] = typing.cast(
            "capo_connect.types.hours_of_operation_days.HoursOfOperationDays", ""
        )
    if data.get("StartTime") is not None:
        import capo_connect.types.hours_of_operation_time_slice

        out["start_time"] = (
            capo_connect.types.hours_of_operation_time_slice.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("HoursOfOperationConfig.start_time required")
    if data.get("EndTime") is not None:
        import capo_connect.types.hours_of_operation_time_slice

        out["end_time"] = (
            capo_connect.types.hours_of_operation_time_slice.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("HoursOfOperationConfig.end_time required")
    return out
