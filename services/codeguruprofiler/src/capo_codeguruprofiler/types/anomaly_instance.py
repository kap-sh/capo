"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AnomalyInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.timestamp
    import capo_codeguruprofiler.types.user_feedback


class AnomalyInstance(TypedDict, closed=True):
    id: "str"
    """<p> The universally unique identifier (UUID) of an instance of an anomaly in a metric. </p>"""
    start_time: "capo_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The start time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    end_time: NotRequired["capo_codeguruprofiler.types.timestamp.Timestamp"]
    """<p> The end time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    user_feedback: NotRequired["capo_codeguruprofiler.types.user_feedback.UserFeedback"]
    """<p>Feedback type on a specific instance of anomaly submitted by the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyInstance) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_codeguruprofiler.types.timestamp

    out["startTime"] = capo_codeguruprofiler.types.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_codeguruprofiler.types.timestamp

        out["endTime"] = capo_codeguruprofiler.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "user_feedback" in value:
        import capo_codeguruprofiler.types.user_feedback

        out["userFeedback"] = capo_codeguruprofiler.types.user_feedback.serialize_json(
            value["user_feedback"]
        )
    return out


def deserialize_json(data: dict) -> AnomalyInstance:
    out: AnomalyInstance = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("startTime") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["start_time"] = capo_codeguruprofiler.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["end_time"] = capo_codeguruprofiler.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("userFeedback") is not None:
        import capo_codeguruprofiler.types.user_feedback

        out["user_feedback"] = (
            capo_codeguruprofiler.types.user_feedback.deserialize_json(
                data["userFeedback"]
            )
        )
    return out
