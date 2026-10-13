"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSessionActionDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_deadline.types.assigned_environment_enter_session_action_definition
    import capo_deadline.types.assigned_environment_exit_session_action_definition
    import capo_deadline.types.assigned_sync_input_job_attachments_session_action_definition
    import capo_deadline.types.assigned_task_run_session_action_definition


class _AssignedSessionActionDefinition_envEnter(TypedDict, closed=True):
    envEnter: "capo_deadline.types.assigned_environment_enter_session_action_definition.AssignedEnvironmentEnterSessionActionDefinition"


class _AssignedSessionActionDefinition_envExit(TypedDict, closed=True):
    envExit: "capo_deadline.types.assigned_environment_exit_session_action_definition.AssignedEnvironmentExitSessionActionDefinition"


class _AssignedSessionActionDefinition_taskRun(TypedDict, closed=True):
    taskRun: "capo_deadline.types.assigned_task_run_session_action_definition.AssignedTaskRunSessionActionDefinition"


class _AssignedSessionActionDefinition_syncInputJobAttachments(TypedDict, closed=True):
    syncInputJobAttachments: "capo_deadline.types.assigned_sync_input_job_attachments_session_action_definition.AssignedSyncInputJobAttachmentsSessionActionDefinition"


AssignedSessionActionDefinition: TypeAlias = (
    _AssignedSessionActionDefinition_envEnter
    | _AssignedSessionActionDefinition_envExit
    | _AssignedSessionActionDefinition_taskRun
    | _AssignedSessionActionDefinition_syncInputJobAttachments
)


# --- restJson1 ser/de ---
def serialize_json(value: AssignedSessionActionDefinition) -> dict:
    if "envEnter" in value:
        import capo_deadline.types.assigned_environment_enter_session_action_definition

        return {
            "envEnter": capo_deadline.types.assigned_environment_enter_session_action_definition.serialize_json(
                value["envEnter"]
            )
        }
    elif "envExit" in value:
        import capo_deadline.types.assigned_environment_exit_session_action_definition

        return {
            "envExit": capo_deadline.types.assigned_environment_exit_session_action_definition.serialize_json(
                value["envExit"]
            )
        }
    elif "taskRun" in value:
        import capo_deadline.types.assigned_task_run_session_action_definition

        return {
            "taskRun": capo_deadline.types.assigned_task_run_session_action_definition.serialize_json(
                value["taskRun"]
            )
        }
    elif "syncInputJobAttachments" in value:
        import capo_deadline.types.assigned_sync_input_job_attachments_session_action_definition

        return {
            "syncInputJobAttachments": capo_deadline.types.assigned_sync_input_job_attachments_session_action_definition.serialize_json(
                value["syncInputJobAttachments"]
            )
        }
    else:
        raise SerializationError("AssignedSessionActionDefinition: no variant present")


def deserialize_json(data: dict) -> AssignedSessionActionDefinition:
    if data.get("envEnter") is not None:
        import capo_deadline.types.assigned_environment_enter_session_action_definition

        return {
            "envEnter": capo_deadline.types.assigned_environment_enter_session_action_definition.deserialize_json(
                data["envEnter"]
            )
        }
    elif data.get("envExit") is not None:
        import capo_deadline.types.assigned_environment_exit_session_action_definition

        return {
            "envExit": capo_deadline.types.assigned_environment_exit_session_action_definition.deserialize_json(
                data["envExit"]
            )
        }
    elif data.get("taskRun") is not None:
        import capo_deadline.types.assigned_task_run_session_action_definition

        return {
            "taskRun": capo_deadline.types.assigned_task_run_session_action_definition.deserialize_json(
                data["taskRun"]
            )
        }
    elif data.get("syncInputJobAttachments") is not None:
        import capo_deadline.types.assigned_sync_input_job_attachments_session_action_definition

        return {
            "syncInputJobAttachments": capo_deadline.types.assigned_sync_input_job_attachments_session_action_definition.deserialize_json(
                data["syncInputJobAttachments"]
            )
        }
    else:
        raise DeserializationError(
            "AssignedSessionActionDefinition: no recognized variant key"
        )


def redact_sensitive(value: AssignedSessionActionDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "taskRun" in value:
        import capo_deadline.types.assigned_task_run_session_action_definition

        out["taskRun"] = (
            capo_deadline.types.assigned_task_run_session_action_definition.redact_sensitive(
                value["taskRun"]
            )
        )
    return out
