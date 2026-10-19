"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutomatedSnapshotPauseOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.pause_state
    import capo_elasticsearch_service.types.update_timestamp


class AutomatedSnapshotPauseOptions(TypedDict, closed=True):
    enabled: "capo_elasticsearch_service.types.boolean.Boolean"
    """<p>Whether automated snapshot pause is enabled for the domain.</p>"""
    start_time: NotRequired[
        "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The timestamp at which the automated snapshot pause begins.</p>"""
    end_time: NotRequired[
        "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The timestamp at which the automated snapshot pause ends.</p>"""
    state: NotRequired["capo_elasticsearch_service.types.pause_state.PauseState"]
    """<p>The current state of the automated snapshot pause. Valid values are <code>Active</code>, <code>Completed</code>, <code>Scheduled</code>, and <code>Disabled</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedSnapshotPauseOptions) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "start_time" in value:
        import capo_elasticsearch_service.types.update_timestamp

        out["StartTime"] = (
            capo_elasticsearch_service.types.update_timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_elasticsearch_service.types.update_timestamp

        out["EndTime"] = (
            capo_elasticsearch_service.types.update_timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "state" in value:
        import capo_elasticsearch_service.types.pause_state

        out["State"] = capo_elasticsearch_service.types.pause_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> AutomatedSnapshotPauseOptions:
    out: AutomatedSnapshotPauseOptions = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("StartTime") is not None:
        import capo_elasticsearch_service.types.update_timestamp

        out["start_time"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_elasticsearch_service.types.update_timestamp

        out["end_time"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    if data.get("State") is not None:
        import capo_elasticsearch_service.types.pause_state

        out["state"] = capo_elasticsearch_service.types.pause_state.deserialize_json(
            data["State"]
        )
    return out
