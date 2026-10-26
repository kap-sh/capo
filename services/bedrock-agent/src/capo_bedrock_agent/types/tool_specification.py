"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ToolSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.non_empty_string
    import capo_bedrock_agent.types.tool_input_schema
    import capo_bedrock_agent.types.tool_name


class ToolSpecification(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.tool_name.ToolName"
    """<p>The name of the tool.</p>"""
    description: NotRequired["capo_bedrock_agent.types.non_empty_string.NonEmptyString"]
    """<p>The description of the tool.</p>"""
    input_schema: "capo_bedrock_agent.types.tool_input_schema.ToolInputSchema"
    """<p>The input schema for the tool.</p>"""
    strict: NotRequired["bool"]
    """<p>Whether the tool schema is strictly enforced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolSpecification) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.tool_input_schema

    out["inputSchema"] = capo_bedrock_agent.types.tool_input_schema.serialize_json(
        value["input_schema"]
    )
    if "strict" in value:
        out["strict"] = value["strict"]
    return out


def deserialize_json(data: dict) -> ToolSpecification:
    out: ToolSpecification = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("inputSchema") is not None:
        import capo_bedrock_agent.types.tool_input_schema

        out["input_schema"] = (
            capo_bedrock_agent.types.tool_input_schema.deserialize_json(
                data["inputSchema"]
            )
        )
    else:
        out["input_schema"] = {"$unknown": {"name": ""}}
    if data.get("strict") is not None:
        out["strict"] = data["strict"]
    return out
