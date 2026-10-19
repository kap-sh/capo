"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.timestamp


class EventTimeRange(TypedDict, closed=True):
    from_time: "capo_devops_guru.types.timestamp.Timestamp"
    """<p> The time when the event started. </p>"""
    to_time: "capo_devops_guru.types.timestamp.Timestamp"
    """<p> The time when the event ended. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventTimeRange) -> dict:
    out: dict = {}
    import capo_devops_guru.types.timestamp

    out["FromTime"] = capo_devops_guru.types.timestamp.serialize_json(
        value["from_time"]
    )
    import capo_devops_guru.types.timestamp

    out["ToTime"] = capo_devops_guru.types.timestamp.serialize_json(value["to_time"])
    return out


def deserialize_json(data: dict) -> EventTimeRange:
    out: EventTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("FromTime") is not None:
        import capo_devops_guru.types.timestamp

        out["from_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["FromTime"]
        )
    else:
        import datetime

        out["from_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ToTime") is not None:
        import capo_devops_guru.types.timestamp

        out["to_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["ToTime"]
        )
    else:
        import datetime

        out["to_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
