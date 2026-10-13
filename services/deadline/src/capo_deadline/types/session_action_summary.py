"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.ended_at
    import capo_deadline.types.session_action_definition_summary
    import capo_deadline.types.session_action_id
    import capo_deadline.types.session_action_progress_percent
    import capo_deadline.types.session_action_status
    import capo_deadline.types.started_at
    import capo_deadline.types.task_run_manifest_properties_list_response
    import capo_deadline.types.timestamp


class SessionActionSummary(TypedDict, closed=True):
    session_action_id: "capo_deadline.types.session_action_id.SessionActionId"
    """<p>The session action ID.</p>"""
    status: "capo_deadline.types.session_action_status.SessionActionStatus"
    """<p>The status of the session action.</p>"""
    started_at: NotRequired["capo_deadline.types.started_at.StartedAt"]
    """<p>The date and time the resource started running.</p>"""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    worker_updated_at: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """<p>The Linux timestamp of the last date and time that the session action was updated.</p>"""
    progress_percent: NotRequired[
        "capo_deadline.types.session_action_progress_percent.SessionActionProgressPercent"
    ]
    """<p>The completion percentage for the session action.</p>"""
    manifests: NotRequired[
        "capo_deadline.types.task_run_manifest_properties_list_response.TaskRunManifestPropertiesListResponse"
    ]
    """<p>The list of manifest properties that describe file attachments for the task run.</p>"""
    definition: "capo_deadline.types.session_action_definition_summary.SessionActionDefinitionSummary"
    """<p>The session action definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionSummary) -> dict:
    out: dict = {}
    out["sessionActionId"] = value["session_action_id"]
    import capo_deadline.types.session_action_status

    out["status"] = capo_deadline.types.session_action_status.serialize_json(
        value["status"]
    )
    if "started_at" in value:
        import capo_deadline.types.started_at

        out["startedAt"] = capo_deadline.types.started_at.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_deadline.types.ended_at

        out["endedAt"] = capo_deadline.types.ended_at.serialize_json(value["ended_at"])
    if "worker_updated_at" in value:
        import capo_deadline.types.timestamp

        out["workerUpdatedAt"] = capo_deadline.types.timestamp.serialize_json(
            value["worker_updated_at"]
        )
    if "progress_percent" in value:
        out["progressPercent"] = (
            "NaN"
            if value["progress_percent"] != value["progress_percent"]
            else "Infinity"
            if value["progress_percent"] == float("inf")
            else "-Infinity"
            if value["progress_percent"] == float("-inf")
            else value["progress_percent"]
        )
    if "manifests" in value:
        import capo_deadline.types.task_run_manifest_properties_list_response

        out["manifests"] = (
            capo_deadline.types.task_run_manifest_properties_list_response.serialize_json(
                value["manifests"]
            )
        )
    import capo_deadline.types.session_action_definition_summary

    out["definition"] = (
        capo_deadline.types.session_action_definition_summary.serialize_json(
            value["definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> SessionActionSummary:
    out: SessionActionSummary = {}  # type: ignore[typeddict-item]
    if data.get("sessionActionId") is not None:
        out["session_action_id"] = data["sessionActionId"]
    else:
        raise DeserializationError("SessionActionSummary.session_action_id required")
    if data.get("status") is not None:
        import capo_deadline.types.session_action_status

        out["status"] = capo_deadline.types.session_action_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("SessionActionSummary.status required")
    if data.get("startedAt") is not None:
        import capo_deadline.types.started_at

        out["started_at"] = capo_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    if data.get("endedAt") is not None:
        import capo_deadline.types.ended_at

        out["ended_at"] = capo_deadline.types.ended_at.deserialize_json(data["endedAt"])
    if data.get("workerUpdatedAt") is not None:
        import capo_deadline.types.timestamp

        out["worker_updated_at"] = capo_deadline.types.timestamp.deserialize_json(
            data["workerUpdatedAt"]
        )
    if data.get("progressPercent") is not None:
        out["progress_percent"] = float(data["progressPercent"])
    if data.get("manifests") is not None:
        import capo_deadline.types.task_run_manifest_properties_list_response

        out["manifests"] = (
            capo_deadline.types.task_run_manifest_properties_list_response.deserialize_json(
                data["manifests"]
            )
        )
    if data.get("definition") is not None:
        import capo_deadline.types.session_action_definition_summary

        out["definition"] = (
            capo_deadline.types.session_action_definition_summary.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("SessionActionSummary.definition required")
    return out


def redact_sensitive(value: SessionActionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "definition" in value:
        import capo_deadline.types.session_action_definition_summary

        out["definition"] = (
            capo_deadline.types.session_action_definition_summary.redact_sensitive(
                value["definition"]
            )
        )
    return out
