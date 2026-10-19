"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOverrideInputValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.tool_override_input_value_configuration


class ToolOverrideInputValue(TypedDict, closed=True):
    json_path: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The JSON path for the input value override.</p>"""
    value: "capo_qconnect.types.tool_override_input_value_configuration.ToolOverrideInputValueConfiguration"
    """<p>The override input value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolOverrideInputValue) -> dict:
    out: dict = {}
    out["jsonPath"] = value["json_path"]
    import capo_qconnect.types.tool_override_input_value_configuration

    out["value"] = (
        capo_qconnect.types.tool_override_input_value_configuration.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> ToolOverrideInputValue:
    out: ToolOverrideInputValue = {}  # type: ignore[typeddict-item]
    if data.get("jsonPath") is not None:
        out["json_path"] = data["jsonPath"]
    else:
        out["json_path"] = ""
    if data.get("value") is not None:
        import capo_qconnect.types.tool_override_input_value_configuration

        out["value"] = (
            capo_qconnect.types.tool_override_input_value_configuration.deserialize_json(
                data["value"]
            )
        )
    else:
        import capo_qconnect.types._unknown

        out["value"] = capo_qconnect.types._unknown.UnknownUnionMember("")
    return out


def redact_sensitive(value: ToolOverrideInputValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        import capo_qconnect.types.tool_override_input_value_configuration

        out["value"] = (
            capo_qconnect.types.tool_override_input_value_configuration.redact_sensitive(
                value["value"]
            )
        )
    return out
