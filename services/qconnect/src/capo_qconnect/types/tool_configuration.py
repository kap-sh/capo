"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.annotation
    import capo_qconnect.types.json_document
    import capo_qconnect.types.non_empty_sensitive_string
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.tool_instruction
    import capo_qconnect.types.tool_output_filter_list
    import capo_qconnect.types.tool_override_input_value_list
    import capo_qconnect.types.tool_type
    import capo_qconnect.types.user_interaction_configuration


class ToolConfiguration(TypedDict, closed=True):
    tool_name: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The name of the tool.</p>"""
    tool_type: "capo_qconnect.types.tool_type.ToolType"
    """<p>The type of the tool.</p>"""
    title: NotRequired[
        "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    ]
    """<p>The title of the tool configuration.</p>"""
    tool_id: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the tool, for example toolName from Model Context Provider server.</p>"""
    description: NotRequired[
        "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    ]
    """<p>The description of the tool configuration.</p>"""
    instruction: NotRequired["capo_qconnect.types.tool_instruction.ToolInstruction"]
    """<p>Instructions for using the tool.</p>"""
    override_input_values: NotRequired[
        "capo_qconnect.types.tool_override_input_value_list.ToolOverrideInputValueList"
    ]
    """<p>Override input values for the tool configuration.</p>"""
    output_filters: NotRequired[
        "capo_qconnect.types.tool_output_filter_list.ToolOutputFilterList"
    ]
    """<p>Output filters applies to the tool result.</p>"""
    input_schema: NotRequired["capo_qconnect.types.json_document.JSONDocument"]
    """<p>The input schema for the tool configuration.</p>"""
    output_schema: NotRequired["capo_qconnect.types.json_document.JSONDocument"]
    """<p>The output schema for the tool configuration.</p>"""
    annotations: NotRequired["capo_qconnect.types.annotation.Annotation"]
    """<p>Annotations for the tool configuration.</p>"""
    user_interaction_configuration: NotRequired[
        "capo_qconnect.types.user_interaction_configuration.UserInteractionConfiguration"
    ]
    """<p>Configuration for user interaction with the tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolConfiguration) -> dict:
    out: dict = {}
    out["toolName"] = value["tool_name"]
    out["toolType"] = value["tool_type"]
    if "title" in value:
        out["title"] = value["title"]
    if "tool_id" in value:
        out["toolId"] = value["tool_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "instruction" in value:
        import capo_qconnect.types.tool_instruction

        out["instruction"] = capo_qconnect.types.tool_instruction.serialize_json(
            value["instruction"]
        )
    if "override_input_values" in value:
        import capo_qconnect.types.tool_override_input_value_list

        out["overrideInputValues"] = (
            capo_qconnect.types.tool_override_input_value_list.serialize_json(
                value["override_input_values"]
            )
        )
    if "output_filters" in value:
        import capo_qconnect.types.tool_output_filter_list

        out["outputFilters"] = (
            capo_qconnect.types.tool_output_filter_list.serialize_json(
                value["output_filters"]
            )
        )
    if "input_schema" in value:
        out["inputSchema"] = value["input_schema"]
    if "output_schema" in value:
        out["outputSchema"] = value["output_schema"]
    if "annotations" in value:
        import capo_qconnect.types.annotation

        out["annotations"] = capo_qconnect.types.annotation.serialize_json(
            value["annotations"]
        )
    if "user_interaction_configuration" in value:
        import capo_qconnect.types.user_interaction_configuration

        out["userInteractionConfiguration"] = (
            capo_qconnect.types.user_interaction_configuration.serialize_json(
                value["user_interaction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ToolConfiguration:
    out: ToolConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("toolName") is not None:
        out["tool_name"] = data["toolName"]
    else:
        out["tool_name"] = ""
    if data.get("toolType") is not None:
        out["tool_type"] = data["toolType"]
    else:
        out["tool_type"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("toolId") is not None:
        out["tool_id"] = data["toolId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("instruction") is not None:
        import capo_qconnect.types.tool_instruction

        out["instruction"] = capo_qconnect.types.tool_instruction.deserialize_json(
            data["instruction"]
        )
    if data.get("overrideInputValues") is not None:
        import capo_qconnect.types.tool_override_input_value_list

        out["override_input_values"] = (
            capo_qconnect.types.tool_override_input_value_list.deserialize_json(
                data["overrideInputValues"]
            )
        )
    if data.get("outputFilters") is not None:
        import capo_qconnect.types.tool_output_filter_list

        out["output_filters"] = (
            capo_qconnect.types.tool_output_filter_list.deserialize_json(
                data["outputFilters"]
            )
        )
    if data.get("inputSchema") is not None:
        out["input_schema"] = data["inputSchema"]
    if data.get("outputSchema") is not None:
        out["output_schema"] = data["outputSchema"]
    if data.get("annotations") is not None:
        import capo_qconnect.types.annotation

        out["annotations"] = capo_qconnect.types.annotation.deserialize_json(
            data["annotations"]
        )
    if data.get("userInteractionConfiguration") is not None:
        import capo_qconnect.types.user_interaction_configuration

        out["user_interaction_configuration"] = (
            capo_qconnect.types.user_interaction_configuration.deserialize_json(
                data["userInteractionConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ToolConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    if "override_input_values" in value:
        out["override_input_values"] = "*** Sensitive Data Redacted ***"
    if "output_filters" in value:
        out["output_filters"] = "*** Sensitive Data Redacted ***"
    if "input_schema" in value:
        out["input_schema"] = "*** Sensitive Data Redacted ***"
    if "output_schema" in value:
        out["output_schema"] = "*** Sensitive Data Redacted ***"
    if "annotations" in value:
        out["annotations"] = "*** Sensitive Data Redacted ***"
    return out
