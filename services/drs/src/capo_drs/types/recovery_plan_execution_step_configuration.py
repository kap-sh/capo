"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionStepConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError, SerializationError
from capo_drs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_drs.types.execution_server_step_configuration
    import capo_drs.types.wait_step_configuration


class RecoveryPlanExecutionStepConfigurationExecutionServerStepConfigurationMember(
    TypedDict, closed=True
):
    executionServerStepConfiguration: "capo_drs.types.execution_server_step_configuration.ExecutionServerStepConfiguration"


class RecoveryPlanExecutionStepConfigurationWaitStepConfigurationMember(
    TypedDict, closed=True
):
    waitStepConfiguration: (
        "capo_drs.types.wait_step_configuration.WaitStepConfiguration"
    )


RecoveryPlanExecutionStepConfiguration: TypeAlias = (
    RecoveryPlanExecutionStepConfigurationExecutionServerStepConfigurationMember
    | RecoveryPlanExecutionStepConfigurationWaitStepConfigurationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionStepConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RecoveryPlanExecutionStepConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "executionServerStepConfiguration" in value:
        import capo_drs.types.execution_server_step_configuration

        return {
            "executionServerStepConfiguration": capo_drs.types.execution_server_step_configuration.serialize_json(
                value["executionServerStepConfiguration"]
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
        raise SerializationError(
            "RecoveryPlanExecutionStepConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RecoveryPlanExecutionStepConfiguration:
    if data.get("executionServerStepConfiguration") is not None:
        import capo_drs.types.execution_server_step_configuration

        return {
            "executionServerStepConfiguration": capo_drs.types.execution_server_step_configuration.deserialize_json(
                data["executionServerStepConfiguration"]
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
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RecoveryPlanExecutionStepConfiguration: no recognized variant key"
        )
