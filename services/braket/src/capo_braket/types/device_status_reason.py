"""Generated from Smithy shape ``com.amazonaws.braket#DeviceStatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_braket.types.device_status_reason_code


class DeviceStatusReason(TypedDict, closed=True):
    reason: "capo_braket.types.device_status_reason_code.DeviceStatusReasonCode"
    """<p>The reason code for the current status of the device.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The time at which the device status reason started.</p>"""
    estimated_end_at: NotRequired["datetime.datetime"]
    """<p>The estimated time at which the current status reason will end.</p>"""
    updated_at: "datetime.datetime"
    """<p>The time of the most recent update to the device status reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceStatusReason) -> dict:
    out: dict = {}
    out["reason"] = value["reason"]
    if "started_at" in value:
        import capo_braket._protocol.serialize

        out["startedAt"] = capo_braket._protocol.serialize.fmt_date_time(
            value["started_at"]
        )
    if "estimated_end_at" in value:
        import capo_braket._protocol.serialize

        out["estimatedEndAt"] = capo_braket._protocol.serialize.fmt_date_time(
            value["estimated_end_at"]
        )
    import capo_braket._protocol.serialize

    out["updatedAt"] = capo_braket._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DeviceStatusReason:
    out: DeviceStatusReason = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    if data.get("startedAt") is not None:
        import datetime

        out["started_at"] = datetime.datetime.fromisoformat(
            data["startedAt"].replace("Z", "+00:00")
        )
    if data.get("estimatedEndAt") is not None:
        import datetime

        out["estimated_end_at"] = datetime.datetime.fromisoformat(
            data["estimatedEndAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
