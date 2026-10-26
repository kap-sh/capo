"""Generated from Smithy shape ``com.amazonaws.novaact#ToolSpec``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.tool_description
    import capo_nova_act.types.tool_input_schema
    import capo_nova_act.types.tool_name


class ToolSpec(TypedDict, closed=True):
    name: "capo_nova_act.types.tool_name.ToolName"
    """<p>The unique name of the tool that acts will use to invoke it.</p>"""
    description: "capo_nova_act.types.tool_description.ToolDescription"
    """<p>A description of what the tool does and how it should be used.</p>"""
    input_schema: "capo_nova_act.types.tool_input_schema.ToolInputSchema"
    """<p>The JSON schema that defines the expected input format for the tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolSpec) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_nova_act.types.tool_input_schema

    out["inputSchema"] = capo_nova_act.types.tool_input_schema.serialize_json(
        value["input_schema"]
    )
    return out


def deserialize_json(data: dict) -> ToolSpec:
    out: ToolSpec = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("inputSchema") is not None:
        import capo_nova_act.types.tool_input_schema

        out["input_schema"] = capo_nova_act.types.tool_input_schema.deserialize_json(
            data["inputSchema"]
        )
    else:
        out["input_schema"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: ToolSpec) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "input_schema" in value:
        out["input_schema"] = "*** Sensitive Data Redacted ***"
    return out
