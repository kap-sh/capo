"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanStepConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError, SerializationError
from capo_drs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_drs.types.server_step_configuration
    import capo_drs.types.wait_step_configuration


class _RecoveryPlanStepConfiguration_serverStepConfiguration(TypedDict, closed=True):
    serverStepConfiguration: (
        "capo_drs.types.server_step_configuration.ServerStepConfiguration"
    )


class _RecoveryPlanStepConfiguration_waitStepConfiguration(TypedDict, closed=True):
    waitStepConfiguration: (
        "capo_drs.types.wait_step_configuration.WaitStepConfiguration"
    )


RecoveryPlanStepConfiguration: TypeAlias = (
    _RecoveryPlanStepConfiguration_serverStepConfiguration
    | _RecoveryPlanStepConfiguration_waitStepConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanStepConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RecoveryPlanStepConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "serverStepConfiguration" in value:
        import capo_drs.types.server_step_configuration

        return {
            "serverStepConfiguration": capo_drs.types.server_step_configuration.serialize_json(
                value["serverStepConfiguration"]
            )
        }
    elif "waitStepConfiguration" in value:
        import capo_drs.types.wait_step_configuration

        return {
            "waitStepConfiguration": capo_drs.types.wait_step_configuration.serialize_json(
                value["waitStepConfiguration"]
            )
        }
    else:
        raise SerializationError("RecoveryPlanStepConfiguration: no variant present")


def deserialize_json(data: dict) -> RecoveryPlanStepConfiguration:
    if data.get("serverStepConfiguration") is not None:
        import capo_drs.types.server_step_configuration

        return {
            "serverStepConfiguration": capo_drs.types.server_step_configuration.deserialize_json(
                data["serverStepConfiguration"]
            )
        }
    elif data.get("waitStepConfiguration") is not None:
        import capo_drs.types.wait_step_configuration

        return {
            "waitStepConfiguration": capo_drs.types.wait_step_configuration.deserialize_json(
                data["waitStepConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "RecoveryPlanStepConfiguration: no recognized variant key"
        )
