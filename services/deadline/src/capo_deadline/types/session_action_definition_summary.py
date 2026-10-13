"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionDefinitionSummary``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_deadline.types.environment_enter_session_action_definition_summary
    import capo_deadline.types.environment_exit_session_action_definition_summary
    import capo_deadline.types.sync_input_job_attachments_session_action_definition_summary
    import capo_deadline.types.task_run_session_action_definition_summary


class _SessionActionDefinitionSummary_envEnter(TypedDict, closed=True):
    envEnter: "capo_deadline.types.environment_enter_session_action_definition_summary.EnvironmentEnterSessionActionDefinitionSummary"


class _SessionActionDefinitionSummary_envExit(TypedDict, closed=True):
    envExit: "capo_deadline.types.environment_exit_session_action_definition_summary.EnvironmentExitSessionActionDefinitionSummary"


class _SessionActionDefinitionSummary_taskRun(TypedDict, closed=True):
    taskRun: "capo_deadline.types.task_run_session_action_definition_summary.TaskRunSessionActionDefinitionSummary"


class _SessionActionDefinitionSummary_syncInputJobAttachments(TypedDict, closed=True):
    syncInputJobAttachments: "capo_deadline.types.sync_input_job_attachments_session_action_definition_summary.SyncInputJobAttachmentsSessionActionDefinitionSummary"


SessionActionDefinitionSummary: TypeAlias = (
    _SessionActionDefinitionSummary_envEnter
    | _SessionActionDefinitionSummary_envExit
    | _SessionActionDefinitionSummary_taskRun
    | _SessionActionDefinitionSummary_syncInputJobAttachments
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionDefinitionSummary) -> dict:
    if "envEnter" in value:
        import capo_deadline.types.environment_enter_session_action_definition_summary

        return {
            "envEnter": capo_deadline.types.environment_enter_session_action_definition_summary.serialize_json(
                value["envEnter"]
            )
        }
    elif "envExit" in value:
        import capo_deadline.types.environment_exit_session_action_definition_summary

        return {
            "envExit": capo_deadline.types.environment_exit_session_action_definition_summary.serialize_json(
                value["envExit"]
            )
        }
    elif "taskRun" in value:
        import capo_deadline.types.task_run_session_action_definition_summary

        return {
            "taskRun": capo_deadline.types.task_run_session_action_definition_summary.serialize_json(
                value["taskRun"]
            )
        }
    elif "syncInputJobAttachments" in value:
        import capo_deadline.types.sync_input_job_attachments_session_action_definition_summary

        return {
            "syncInputJobAttachments": capo_deadline.types.sync_input_job_attachments_session_action_definition_summary.serialize_json(
                value["syncInputJobAttachments"]
            )
        }
    else:
        raise SerializationError("SessionActionDefinitionSummary: no variant present")


def deserialize_json(data: dict) -> SessionActionDefinitionSummary:
    if data.get("envEnter") is not None:
        import capo_deadline.types.environment_enter_session_action_definition_summary

        return {
            "envEnter": capo_deadline.types.environment_enter_session_action_definition_summary.deserialize_json(
                data["envEnter"]
            )
        }
    elif data.get("envExit") is not None:
        import capo_deadline.types.environment_exit_session_action_definition_summary

        return {
            "envExit": capo_deadline.types.environment_exit_session_action_definition_summary.deserialize_json(
                data["envExit"]
            )
        }
    elif data.get("taskRun") is not None:
        import capo_deadline.types.task_run_session_action_definition_summary

        return {
            "taskRun": capo_deadline.types.task_run_session_action_definition_summary.deserialize_json(
                data["taskRun"]
            )
        }
    elif data.get("syncInputJobAttachments") is not None:
        import capo_deadline.types.sync_input_job_attachments_session_action_definition_summary

        return {
            "syncInputJobAttachments": capo_deadline.types.sync_input_job_attachments_session_action_definition_summary.deserialize_json(
                data["syncInputJobAttachments"]
            )
        }
    else:
        raise DeserializationError(
            "SessionActionDefinitionSummary: no recognized variant key"
        )


def redact_sensitive(value: SessionActionDefinitionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "taskRun" in value:
        import capo_deadline.types.task_run_session_action_definition_summary

        out["taskRun"] = (
            capo_deadline.types.task_run_session_action_definition_summary.redact_sensitive(
                value["taskRun"]
            )
        )
    return out
