"""Generated from Smithy shape ``com.amazonaws.deadline#UpdatedSessionActionInfo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.completed_status
    import capo_deadline.types.process_exit_code
    import capo_deadline.types.session_action_progress_message
    import capo_deadline.types.session_action_progress_percent
    import capo_deadline.types.task_run_manifest_properties_list_request
    import capo_deadline.types.timestamp


class UpdatedSessionActionInfo(TypedDict, closed=True):
    completed_status: NotRequired[
        "capo_deadline.types.completed_status.CompletedStatus"
    ]
    """The status of the session upon completion."""
    process_exit_code: NotRequired[
        "capo_deadline.types.process_exit_code.ProcessExitCode"
    ]
    """The process exit code. The default Deadline Cloud worker agent converts unsigned 32-bit exit codes to signed 32-bit exit codes."""
    progress_message: NotRequired[
        "capo_deadline.types.session_action_progress_message.SessionActionProgressMessage"
    ]
    """A message to indicate the progress of the updated session action."""
    started_at: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """The date and time the resource started running."""
    ended_at: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """The date and time the resource ended running."""
    updated_at: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """The updated time."""
    progress_percent: NotRequired[
        "capo_deadline.types.session_action_progress_percent.SessionActionProgressPercent"
    ]
    """The percentage completed."""
    manifests: NotRequired[
        "capo_deadline.types.task_run_manifest_properties_list_request.TaskRunManifestPropertiesListRequest"
    ]
    """A list of output manifest properties reported by the worker agent, with each entry corresponding to a manifest property in the job."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedSessionActionInfo) -> dict:
    out: dict = {}
    if "completed_status" in value:
        import capo_deadline.types.completed_status

        out["completedStatus"] = capo_deadline.types.completed_status.serialize_json(
            value["completed_status"]
        )
    if "process_exit_code" in value:
        out["processExitCode"] = value["process_exit_code"]
    if "progress_message" in value:
        out["progressMessage"] = value["progress_message"]
    if "started_at" in value:
        import capo_deadline._protocol.serialize

        out["startedAt"] = capo_deadline._protocol.serialize.fmt_date_time(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_deadline._protocol.serialize

        out["endedAt"] = capo_deadline._protocol.serialize.fmt_date_time(
            value["ended_at"]
        )
    if "updated_at" in value:
        import capo_deadline._protocol.serialize

        out["updatedAt"] = capo_deadline._protocol.serialize.fmt_date_time(
            value["updated_at"]
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
        import capo_deadline.types.task_run_manifest_properties_list_request

        out["manifests"] = (
            capo_deadline.types.task_run_manifest_properties_list_request.serialize_json(
                value["manifests"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedSessionActionInfo:
    out: UpdatedSessionActionInfo = {}  # type: ignore[typeddict-item]
    if data.get("completedStatus") is not None:
        import capo_deadline.types.completed_status

        out["completed_status"] = capo_deadline.types.completed_status.deserialize_json(
            data["completedStatus"]
        )
    if data.get("processExitCode") is not None:
        out["process_exit_code"] = data["processExitCode"]
    if data.get("progressMessage") is not None:
        out["progress_message"] = data["progressMessage"]
    if data.get("startedAt") is not None:
        import datetime

        out["started_at"] = datetime.datetime.fromisoformat(
            data["startedAt"].replace("Z", "+00:00")
        )
    if data.get("endedAt") is not None:
        import datetime

        out["ended_at"] = datetime.datetime.fromisoformat(
            data["endedAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("progressPercent") is not None:
        out["progress_percent"] = float(data["progressPercent"])
    if data.get("manifests") is not None:
        import capo_deadline.types.task_run_manifest_properties_list_request

        out["manifests"] = (
            capo_deadline.types.task_run_manifest_properties_list_request.deserialize_json(
                data["manifests"]
            )
        )
    return out


def redact_sensitive(value: UpdatedSessionActionInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "progress_message" in value:
        out["progress_message"] = "*** Sensitive Data Redacted ***"
    return out
