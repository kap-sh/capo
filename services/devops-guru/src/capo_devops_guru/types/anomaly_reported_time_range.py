"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyReportedTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.timestamp


class AnomalyReportedTimeRange(TypedDict, closed=True):
    open_time: "capo_devops_guru.types.timestamp.Timestamp"
    """<p> The time when an anomaly is opened. </p>"""
    close_time: NotRequired["capo_devops_guru.types.timestamp.Timestamp"]
    """<p> The time when an anomaly is closed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyReportedTimeRange) -> dict:
    out: dict = {}
    import capo_devops_guru.types.timestamp

    out["OpenTime"] = capo_devops_guru.types.timestamp.serialize_json(
        value["open_time"]
    )
    if "close_time" in value:
        import capo_devops_guru.types.timestamp

        out["CloseTime"] = capo_devops_guru.types.timestamp.serialize_json(
            value["close_time"]
        )
    return out


def deserialize_json(data: dict) -> AnomalyReportedTimeRange:
    out: AnomalyReportedTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("OpenTime") is not None:
        import capo_devops_guru.types.timestamp

        out["open_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["OpenTime"]
        )
    else:
        import datetime

        out["open_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("CloseTime") is not None:
        import capo_devops_guru.types.timestamp

        out["close_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["CloseTime"]
        )
    return out
