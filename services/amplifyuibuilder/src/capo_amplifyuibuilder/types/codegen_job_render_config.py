"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobRenderConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError, SerializationError
from capo_amplifyuibuilder.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.react_start_codegen_job_data


class _CodegenJobRenderConfig_react(TypedDict, closed=True):
    react: "capo_amplifyuibuilder.types.react_start_codegen_job_data.ReactStartCodegenJobData"


CodegenJobRenderConfig: TypeAlias = _CodegenJobRenderConfig_react | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobRenderConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CodegenJobRenderConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "react" in value:
        import capo_amplifyuibuilder.types.react_start_codegen_job_data

        return {
            "react": capo_amplifyuibuilder.types.react_start_codegen_job_data.serialize_json(
                value["react"]
            )
        }
    else:
        raise SerializationError("CodegenJobRenderConfig: no variant present")


def deserialize_json(data: dict) -> CodegenJobRenderConfig:
    if data.get("react") is not None:
        import capo_amplifyuibuilder.types.react_start_codegen_job_data

        return {
            "react": capo_amplifyuibuilder.types.react_start_codegen_job_data.deserialize_json(
                data["react"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CodegenJobRenderConfig: no recognized variant key")
