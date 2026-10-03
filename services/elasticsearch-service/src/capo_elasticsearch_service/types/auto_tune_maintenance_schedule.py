"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneMaintenanceSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.duration
    import capo_elasticsearch_service.types.start_at
    import capo_elasticsearch_service.types.string


class AutoTuneMaintenanceSchedule(TypedDict, closed=True):
    start_at: NotRequired["capo_elasticsearch_service.types.start_at.StartAt"]
    """<p>Specifies timestamp at which Auto-Tune maintenance schedule start. </p>"""
    duration: NotRequired["capo_elasticsearch_service.types.duration.Duration"]
    """<p>Specifies maintenance schedule duration: duration value and duration unit. See the <a href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html" target="_blank">Developer Guide</a> for more information.</p>"""
    cron_expression_for_recurrence: NotRequired[
        "capo_elasticsearch_service.types.string.String"
    ]
    """<p>Specifies cron expression for a recurring maintenance schedule. See the <a href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html" target="_blank">Developer Guide</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneMaintenanceSchedule) -> dict:
    out: dict = {}
    if "start_at" in value:
        import capo_elasticsearch_service.types.start_at

        out["StartAt"] = capo_elasticsearch_service.types.start_at.serialize_json(
            value["start_at"]
        )
    if "duration" in value:
        import capo_elasticsearch_service.types.duration

        out["Duration"] = capo_elasticsearch_service.types.duration.serialize_json(
            value["duration"]
        )
    if "cron_expression_for_recurrence" in value:
        out["CronExpressionForRecurrence"] = value["cron_expression_for_recurrence"]
    return out


def deserialize_json(data: dict) -> AutoTuneMaintenanceSchedule:
    out: AutoTuneMaintenanceSchedule = {}  # type: ignore[typeddict-item]
    if data.get("StartAt") is not None:
        import capo_elasticsearch_service.types.start_at

        out["start_at"] = capo_elasticsearch_service.types.start_at.deserialize_json(
            data["StartAt"]
        )
    if data.get("Duration") is not None:
        import capo_elasticsearch_service.types.duration

        out["duration"] = capo_elasticsearch_service.types.duration.deserialize_json(
            data["Duration"]
        )
    if data.get("CronExpressionForRecurrence") is not None:
        out["cron_expression_for_recurrence"] = data["CronExpressionForRecurrence"]
    return out
