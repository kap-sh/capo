"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.environment_enter_session_action_definition
    import capo_deadline.types.environment_exit_session_action_definition
    import capo_deadline.types.sync_input_job_attachments_session_action_definition
    import capo_deadline.types.task_run_session_action_definition


class _SessionActionDefinition_envEnter(TypedDict, closed=True):
    envEnter: "capo_deadline.types.environment_enter_session_action_definition.EnvironmentEnterSessionActionDefinition"


class _SessionActionDefinition_envExit(TypedDict, closed=True):
    envExit: "capo_deadline.types.environment_exit_session_action_definition.EnvironmentExitSessionActionDefinition"


class _SessionActionDefinition_taskRun(TypedDict, closed=True):
    taskRun: "capo_deadline.types.task_run_session_action_definition.TaskRunSessionActionDefinition"


class _SessionActionDefinition_syncInputJobAttachments(TypedDict, closed=True):
    syncInputJobAttachments: "capo_deadline.types.sync_input_job_attachments_session_action_definition.SyncInputJobAttachmentsSessionActionDefinition"


SessionActionDefinition: TypeAlias = (
    _SessionActionDefinition_envEnter
    | _SessionActionDefinition_envExit
    | _SessionActionDefinition_taskRun
    | _SessionActionDefinition_syncInputJobAttachments
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionDefinition) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SessionActionDefinition: cannot serialize unknown variant {value.name!r}"
        )
    elif "envEnter" in value:
        import capo_deadline.types.environment_enter_session_action_definition

        return {
            "envEnter": capo_deadline.types.environment_enter_session_action_definition.serialize_json(
                value["envEnter"]
            )
        }
    elif "envExit" in value:
        import capo_deadline.types.environment_exit_session_action_definition

        return {
            "envExit": capo_deadline.types.environment_exit_session_action_definition.serialize_json(
                value["envExit"]
            )
        }
    elif "taskRun" in value:
        import capo_deadline.types.task_run_session_action_definition

        return {
            "taskRun": capo_deadline.types.task_run_session_action_definition.serialize_json(
                value["taskRun"]
            )
        }
    elif "syncInputJobAttachments" in value:
        import capo_deadline.types.sync_input_job_attachments_session_action_definition

        return {
            "syncInputJobAttachments": capo_deadline.types.sync_input_job_attachments_session_action_definition.serialize_json(
                value["syncInputJobAttachments"]
            )
        }
    else:
        raise SerializationError("SessionActionDefinition: no variant present")


def deserialize_json(data: dict) -> SessionActionDefinition:
    if data.get("envEnter") is not None:
        import capo_deadline.types.environment_enter_session_action_definition

        return {
            "envEnter": capo_deadline.types.environment_enter_session_action_definition.deserialize_json(
                data["envEnter"]
            )
        }
    elif data.get("envExit") is not None:
        import capo_deadline.types.environment_exit_session_action_definition

        return {
            "envExit": capo_deadline.types.environment_exit_session_action_definition.deserialize_json(
                data["envExit"]
            )
        }
    elif data.get("taskRun") is not None:
        import capo_deadline.types.task_run_session_action_definition

        return {
            "taskRun": capo_deadline.types.task_run_session_action_definition.deserialize_json(
                data["taskRun"]
            )
        }
    elif data.get("syncInputJobAttachments") is not None:
        import capo_deadline.types.sync_input_job_attachments_session_action_definition

        return {
            "syncInputJobAttachments": capo_deadline.types.sync_input_job_attachments_session_action_definition.deserialize_json(
                data["syncInputJobAttachments"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SessionActionDefinition: no recognized variant key")


def redact_sensitive(
    value: SessionActionDefinition,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "taskRun" in value:
        import capo_deadline.types.task_run_session_action_definition

        out["taskRun"] = (
            capo_deadline.types.task_run_session_action_definition.redact_sensitive(
                value["taskRun"]
            )
        )
    return out
