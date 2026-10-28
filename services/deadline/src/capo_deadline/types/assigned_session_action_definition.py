"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSessionActionDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.assigned_environment_enter_session_action_definition
    import capo_deadline.types.assigned_environment_exit_session_action_definition
    import capo_deadline.types.assigned_sync_input_job_attachments_session_action_definition
    import capo_deadline.types.assigned_task_run_session_action_definition


class AssignedSessionActionDefinitionEnvEnterMember(TypedDict, closed=True):
    envEnter: "capo_deadline.types.assigned_environment_enter_session_action_definition.AssignedEnvironmentEnterSessionActionDefinition"


class AssignedSessionActionDefinitionEnvExitMember(TypedDict, closed=True):
    envExit: "capo_deadline.types.assigned_environment_exit_session_action_definition.AssignedEnvironmentExitSessionActionDefinition"


class AssignedSessionActionDefinitionTaskRunMember(TypedDict, closed=True):
    taskRun: "capo_deadline.types.assigned_task_run_session_action_definition.AssignedTaskRunSessionActionDefinition"


class AssignedSessionActionDefinitionSyncInputJobAttachmentsMember(
    TypedDict, closed=True
):
    syncInputJobAttachments: "capo_deadline.types.assigned_sync_input_job_attachments_session_action_definition.AssignedSyncInputJobAttachmentsSessionActionDefinition"


AssignedSessionActionDefinition: TypeAlias = (
    AssignedSessionActionDefinitionEnvEnterMember
    | AssignedSessionActionDefinitionEnvExitMember
    | AssignedSessionActionDefinitionTaskRunMember
    | AssignedSessionActionDefinitionSyncInputJobAttachmentsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssignedSessionActionDefinition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssignedSessionActionDefinition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "envEnter" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
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
