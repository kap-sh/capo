"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOverrideInputValueConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.tool_override_constant_input_value


class _ToolOverrideInputValueConfiguration_constant(TypedDict, closed=True):
    constant: "capo_qconnect.types.tool_override_constant_input_value.ToolOverrideConstantInputValue"


ToolOverrideInputValueConfiguration: TypeAlias = (
    _ToolOverrideInputValueConfiguration_constant | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolOverrideInputValueConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ToolOverrideInputValueConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "constant" in value:
        import capo_qconnect.types.tool_override_constant_input_value

        return {
            "constant": capo_qconnect.types.tool_override_constant_input_value.serialize_json(
                value["constant"]
            )
        }
    else:
        raise SerializationError(
            "ToolOverrideInputValueConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> ToolOverrideInputValueConfiguration:
    if data.get("constant") is not None:
        import capo_qconnect.types.tool_override_constant_input_value

        return {
            "constant": capo_qconnect.types.tool_override_constant_input_value.deserialize_json(
                data["constant"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ToolOverrideInputValueConfiguration: no recognized variant key"
        )


def redact_sensitive(value: ToolOverrideInputValueConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "constant" in value:
        import capo_qconnect.types.tool_override_constant_input_value

        out["constant"] = (
            capo_qconnect.types.tool_override_constant_input_value.redact_sensitive(
                value["constant"]
            )
        )
    return out
