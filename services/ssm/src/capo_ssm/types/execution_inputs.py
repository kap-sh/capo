"""Generated from Smithy shape ``com.amazonaws.ssm#ExecutionInputs``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError, SerializationError
from capo_ssm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_inputs


class _ExecutionInputs_Automation(TypedDict, closed=True):
    Automation: "capo_ssm.types.automation_execution_inputs.AutomationExecutionInputs"


ExecutionInputs: TypeAlias = _ExecutionInputs_Automation | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionInputs) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExecutionInputs: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Automation" in value:
        import capo_ssm.types.automation_execution_inputs

        return {
            "Automation": capo_ssm.types.automation_execution_inputs.serialize_aws_json_1_1(
                value["Automation"]
            )
        }
    else:
        raise SerializationError("ExecutionInputs: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ExecutionInputs:
    if data.get("Automation") is not None:
        import capo_ssm.types.automation_execution_inputs

        return {
            "Automation": capo_ssm.types.automation_execution_inputs.deserialize_aws_json_1_1(
                data["Automation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ExecutionInputs: no recognized variant key")
