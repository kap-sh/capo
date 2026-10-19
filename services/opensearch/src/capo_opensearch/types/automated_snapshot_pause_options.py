"""Generated from Smithy shape ``com.amazonaws.opensearch#AutomatedSnapshotPauseOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.pause_state
    import capo_opensearch.types.timestamp


class AutomatedSnapshotPauseOptions(TypedDict, closed=True):
    enabled: "capo_opensearch.types.boolean.Boolean"
    """<p>Whether automated snapshot pause is enabled for the domain.</p>"""
    start_time: NotRequired["capo_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp at which the automated snapshot pause begins.</p>"""
    end_time: NotRequired["capo_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp at which the automated snapshot pause ends.</p>"""
    state: NotRequired["capo_opensearch.types.pause_state.PauseState"]
    """<p>The current state of the automated snapshot pause. Valid values are <code>Active</code>, <code>Completed</code>, <code>Scheduled</code>, and <code>Disabled</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedSnapshotPauseOptions) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "start_time" in value:
        import capo_opensearch.types.timestamp

        out["StartTime"] = capo_opensearch.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_opensearch.types.timestamp

        out["EndTime"] = capo_opensearch.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "state" in value:
        import capo_opensearch.types.pause_state

        out["State"] = capo_opensearch.types.pause_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> AutomatedSnapshotPauseOptions:
    out: AutomatedSnapshotPauseOptions = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("StartTime") is not None:
        import capo_opensearch.types.timestamp

        out["start_time"] = capo_opensearch.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_opensearch.types.timestamp

        out["end_time"] = capo_opensearch.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    if data.get("State") is not None:
        import capo_opensearch.types.pause_state

        out["state"] = capo_opensearch.types.pause_state.deserialize_json(data["State"])
    return out
