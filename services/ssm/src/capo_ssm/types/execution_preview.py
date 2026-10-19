"""Generated from Smithy shape ``com.amazonaws.ssm#ExecutionPreview``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError, SerializationError
from capo_ssm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_preview


class _ExecutionPreview_Automation(TypedDict, closed=True):
    Automation: "capo_ssm.types.automation_execution_preview.AutomationExecutionPreview"


ExecutionPreview: TypeAlias = _ExecutionPreview_Automation | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionPreview) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ExecutionPreview: cannot serialize unknown variant {value.name!r}"
        )
    elif "Automation" in value:
        import capo_ssm.types.automation_execution_preview

        return {
            "Automation": capo_ssm.types.automation_execution_preview.serialize_aws_json_1_1(
                value["Automation"]
            )
        }
    else:
        raise SerializationError("ExecutionPreview: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ExecutionPreview:
    if data.get("Automation") is not None:
        import capo_ssm.types.automation_execution_preview

        return {
            "Automation": capo_ssm.types.automation_execution_preview.deserialize_aws_json_1_1(
                data["Automation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ExecutionPreview: no recognized variant key")
