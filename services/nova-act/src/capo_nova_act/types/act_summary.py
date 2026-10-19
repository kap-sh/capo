"""Generated from Smithy shape ``com.amazonaws.novaact#ActSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.act_status
    import capo_nova_act.types.date_timestamp
    import capo_nova_act.types.trace_location
    import capo_nova_act.types.uuid_string


class ActSummary(TypedDict, closed=True):
    workflow_run_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run containing this act.</p>"""
    session_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the session containing this act.</p>"""
    act_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the act.</p>"""
    status: "capo_nova_act.types.act_status.ActStatus"
    """<p>The current execution status of the act.</p>"""
    started_at: "capo_nova_act.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the act started execution.</p>"""
    ended_at: NotRequired["capo_nova_act.types.date_timestamp.DateTimestamp"]
    """<p>The timestamp when the act completed execution, if applicable.</p>"""
    trace_location: NotRequired["capo_nova_act.types.trace_location.TraceLocation"]
    """<p>The location where trace information for this act is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActSummary) -> dict:
    out: dict = {}
    out["workflowRunId"] = value["workflow_run_id"]
    out["sessionId"] = value["session_id"]
    out["actId"] = value["act_id"]
    import capo_nova_act.types.act_status

    out["status"] = capo_nova_act.types.act_status.serialize_json(value["status"])
    import capo_nova_act.types.date_timestamp

    out["startedAt"] = capo_nova_act.types.date_timestamp.serialize_json(
        value["started_at"]
    )
    if "ended_at" in value:
        import capo_nova_act.types.date_timestamp

        out["endedAt"] = capo_nova_act.types.date_timestamp.serialize_json(
            value["ended_at"]
        )
    if "trace_location" in value:
        import capo_nova_act.types.trace_location

        out["traceLocation"] = capo_nova_act.types.trace_location.serialize_json(
            value["trace_location"]
        )
    return out


def deserialize_json(data: dict) -> ActSummary:
    out: ActSummary = {}  # type: ignore[typeddict-item]
    if data.get("workflowRunId") is not None:
        out["workflow_run_id"] = data["workflowRunId"]
    else:
        out["workflow_run_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("actId") is not None:
        out["act_id"] = data["actId"]
    else:
        out["act_id"] = ""
    if data.get("status") is not None:
        import capo_nova_act.types.act_status

        out["status"] = capo_nova_act.types.act_status.deserialize_json(data["status"])
    else:
        import typing

        out["status"] = typing.cast("capo_nova_act.types.act_status.ActStatus", "")
    if data.get("startedAt") is not None:
        import capo_nova_act.types.date_timestamp

        out["started_at"] = capo_nova_act.types.date_timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endedAt") is not None:
        import capo_nova_act.types.date_timestamp

        out["ended_at"] = capo_nova_act.types.date_timestamp.deserialize_json(
            data["endedAt"]
        )
    if data.get("traceLocation") is not None:
        import capo_nova_act.types.trace_location

        out["trace_location"] = capo_nova_act.types.trace_location.deserialize_json(
            data["traceLocation"]
        )
    return out
