"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.timestamp


class AnomalyTimeRange(TypedDict, closed=True):
    start_time: "capo_devops_guru.types.timestamp.Timestamp"
    """<p> The time when the anomalous behavior started. </p>"""
    end_time: NotRequired["capo_devops_guru.types.timestamp.Timestamp"]
    """<p> The time when the anomalous behavior ended. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyTimeRange) -> dict:
    out: dict = {}
    import capo_devops_guru.types.timestamp

    out["StartTime"] = capo_devops_guru.types.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_devops_guru.types.timestamp

        out["EndTime"] = capo_devops_guru.types.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> AnomalyTimeRange:
    out: AnomalyTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_devops_guru.types.timestamp

        out["start_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_devops_guru.types.timestamp

        out["end_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    return out
