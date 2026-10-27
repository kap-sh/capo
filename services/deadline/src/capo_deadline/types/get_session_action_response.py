"""Generated from Smithy shape ``com.amazonaws.deadline#GetSessionActionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.acquired_limits
    import capo_deadline.types.ended_at
    import capo_deadline.types.process_exit_code
    import capo_deadline.types.session_action_definition
    import capo_deadline.types.session_action_id
    import capo_deadline.types.session_action_progress_message
    import capo_deadline.types.session_action_progress_percent
    import capo_deadline.types.session_action_status
    import capo_deadline.types.session_id
    import capo_deadline.types.started_at
    import capo_deadline.types.task_run_manifest_properties_list_response
    import capo_deadline.types.timestamp


class GetSessionActionResponse(TypedDict, closed=True):
    session_action_id: "capo_deadline.types.session_action_id.SessionActionId"
    """The session action ID."""
    status: "capo_deadline.types.session_action_status.SessionActionStatus"
    """The status of the session action."""
    started_at: NotRequired["capo_deadline.types.started_at.StartedAt"]
    """The date and time the resource started running."""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """The date and time the resource ended running."""
    worker_updated_at: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """The Linux timestamp of the date and time the session action was last updated."""
    progress_percent: NotRequired[
        "capo_deadline.types.session_action_progress_percent.SessionActionProgressPercent"
    ]
    """The percentage completed for a session action."""
    manifests: NotRequired[
        "capo_deadline.types.task_run_manifest_properties_list_response.TaskRunManifestPropertiesListResponse"
    ]
    """The list of manifest properties that describe file attachments for the task run."""
    session_id: "capo_deadline.types.session_id.SessionId"
    """The session ID for the session action."""
    process_exit_code: NotRequired[
        "capo_deadline.types.process_exit_code.ProcessExitCode"
    ]
    """The process exit code. The default Deadline Cloud worker agent converts unsigned 32-bit exit codes to signed 32-bit exit codes."""
    progress_message: NotRequired[
        "capo_deadline.types.session_action_progress_message.SessionActionProgressMessage"
    ]
    """The message that communicates the progress of the session action."""
    acquired_limits: NotRequired["capo_deadline.types.acquired_limits.AcquiredLimits"]
    """The limits and their amounts acquired during a session action. If no limits were acquired during the session, this field isn't returned."""
    definition: "capo_deadline.types.session_action_definition.SessionActionDefinition"
    """The session action definition."""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionActionResponse) -> dict:
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
    out["sessionId"] = value["session_id"]
    if "process_exit_code" in value:
        out["processExitCode"] = value["process_exit_code"]
    if "progress_message" in value:
        out["progressMessage"] = value["progress_message"]
    if "acquired_limits" in value:
        import capo_deadline.types.acquired_limits

        out["acquiredLimits"] = capo_deadline.types.acquired_limits.serialize_json(
            value["acquired_limits"]
        )
    import capo_deadline.types.session_action_definition

    out["definition"] = capo_deadline.types.session_action_definition.serialize_json(
        value["definition"]
    )
    return out


def deserialize_json(data: dict) -> GetSessionActionResponse:
    out: GetSessionActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionActionId") is not None:
        out["session_action_id"] = data["sessionActionId"]
    else:
        out["session_action_id"] = ""
    if data.get("status") is not None:
        import capo_deadline.types.session_action_status

        out["status"] = capo_deadline.types.session_action_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.session_action_status.SessionActionStatus", ""
        )
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
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("processExitCode") is not None:
        out["process_exit_code"] = data["processExitCode"]
    if data.get("progressMessage") is not None:
        out["progress_message"] = data["progressMessage"]
    if data.get("acquiredLimits") is not None:
        import capo_deadline.types.acquired_limits

        out["acquired_limits"] = capo_deadline.types.acquired_limits.deserialize_json(
            data["acquiredLimits"]
        )
    if data.get("definition") is not None:
        import capo_deadline.types.session_action_definition

        out["definition"] = (
            capo_deadline.types.session_action_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        out["definition"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: GetSessionActionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "progress_message" in value:
        out["progress_message"] = "*** Sensitive Data Redacted ***"
    if "definition" in value:
        import capo_deadline.types.session_action_definition

        out["definition"] = (
            capo_deadline.types.session_action_definition.redact_sensitive(
                value["definition"]
            )
        )
    return out
