"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutomatedSnapshotPauseRequestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.update_timestamp


class AutomatedSnapshotPauseRequestOptions(TypedDict, closed=True):
    enabled: "capo_elasticsearch_service.types.boolean.Boolean"
    """<p>Whether to enable or disable automated snapshot pause for the domain.</p>"""
    start_time: NotRequired[
        "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The timestamp at which the automated snapshot pause should begin.</p>"""
    end_time: NotRequired[
        "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The timestamp at which the automated snapshot pause should end. The maximum allowed duration between <code>StartTime</code> and <code>EndTime</code> is 3 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedSnapshotPauseRequestOptions) -> dict:
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
    return out


def deserialize_json(data: dict) -> AutomatedSnapshotPauseRequestOptions:
    out: AutomatedSnapshotPauseRequestOptions = {}  # type: ignore[typeddict-item]
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
    return out
