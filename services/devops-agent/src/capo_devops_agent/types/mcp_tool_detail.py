"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPToolDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.tool_classification


class MCPToolDetail(TypedDict, closed=True):
    name: "str"
    """<p>The name of the MCP tool.</p>"""
    tool_classification: NotRequired[
        "capo_devops_agent.types.tool_classification.ToolClassification"
    ]
    """<p>The access categorization of the MCP tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPToolDetail) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "tool_classification" in value:
        import capo_devops_agent.types.tool_classification

        out["toolClassification"] = (
            capo_devops_agent.types.tool_classification.serialize_json(
                value["tool_classification"]
            )
        )
    return out


def deserialize_json(data: dict) -> MCPToolDetail:
    out: MCPToolDetail = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("toolClassification") is not None:
        import capo_devops_agent.types.tool_classification

        out["tool_classification"] = (
            capo_devops_agent.types.tool_classification.deserialize_json(
                data["toolClassification"]
            )
        )
    return out
