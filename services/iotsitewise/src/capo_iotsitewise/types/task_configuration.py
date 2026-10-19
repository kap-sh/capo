"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TaskConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError, SerializationError
from capo_iotsitewise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotsitewise.types.container_task_configuration


class _TaskConfiguration_containerTaskConfiguration(TypedDict, closed=True):
    containerTaskConfiguration: (
        "capo_iotsitewise.types.container_task_configuration.ContainerTaskConfiguration"
    )


TaskConfiguration: TypeAlias = (
    _TaskConfiguration_containerTaskConfiguration | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TaskConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"TaskConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "containerTaskConfiguration" in value:
        import capo_iotsitewise.types.container_task_configuration

        return {
            "containerTaskConfiguration": capo_iotsitewise.types.container_task_configuration.serialize_json(
                value["containerTaskConfiguration"]
            )
        }
    else:
        raise SerializationError("TaskConfiguration: no variant present")


def deserialize_json(data: dict) -> TaskConfiguration:
    if data.get("containerTaskConfiguration") is not None:
        import capo_iotsitewise.types.container_task_configuration

        return {
            "containerTaskConfiguration": capo_iotsitewise.types.container_task_configuration.deserialize_json(
                data["containerTaskConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("TaskConfiguration: no recognized variant key")


def redact_sensitive(value: TaskConfiguration) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "containerTaskConfiguration" in value:
        import capo_iotsitewise.types.container_task_configuration

        out["containerTaskConfiguration"] = (
            capo_iotsitewise.types.container_task_configuration.redact_sensitive(
                value["containerTaskConfiguration"]
            )
        )
    return out
