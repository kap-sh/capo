"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneMaintenanceSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.duration
    import capo_opensearch.types.start_at
    import capo_opensearch.types.string


class AutoTuneMaintenanceSchedule(TypedDict, closed=True):
    start_at: NotRequired["capo_opensearch.types.start_at.StartAt"]
    """<p>The Epoch timestamp at which the Auto-Tune maintenance schedule starts.</p>"""
    duration: NotRequired["capo_opensearch.types.duration.Duration"]
    """<p>The duration of the maintenance schedule. For example, <code>"Duration": {"Value": 2, "Unit": "HOURS"}</code>.</p>"""
    cron_expression_for_recurrence: NotRequired["capo_opensearch.types.string.String"]
    """<p>A cron expression for a recurring maintenance schedule during which Auto-Tune can deploy changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneMaintenanceSchedule) -> dict:
    out: dict = {}
    if "start_at" in value:
        import capo_opensearch.types.start_at

        out["StartAt"] = capo_opensearch.types.start_at.serialize_json(
            value["start_at"]
        )
    if "duration" in value:
        import capo_opensearch.types.duration

        out["Duration"] = capo_opensearch.types.duration.serialize_json(
            value["duration"]
        )
    if "cron_expression_for_recurrence" in value:
        out["CronExpressionForRecurrence"] = value["cron_expression_for_recurrence"]
    return out


def deserialize_json(data: dict) -> AutoTuneMaintenanceSchedule:
    out: AutoTuneMaintenanceSchedule = {}  # type: ignore[typeddict-item]
    if data.get("StartAt") is not None:
        import capo_opensearch.types.start_at

        out["start_at"] = capo_opensearch.types.start_at.deserialize_json(
            data["StartAt"]
        )
    if data.get("Duration") is not None:
        import capo_opensearch.types.duration

        out["duration"] = capo_opensearch.types.duration.deserialize_json(
            data["Duration"]
        )
    if data.get("CronExpressionForRecurrence") is not None:
        out["cron_expression_for_recurrence"] = data["CronExpressionForRecurrence"]
    return out
