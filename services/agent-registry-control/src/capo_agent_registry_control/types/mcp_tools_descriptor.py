"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#McpToolsDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.data_schema_version
    import capo_agent_registry_control.types.descriptor_data


class McpToolsDescriptor(TypedDict, closed=True):
    data: NotRequired[
        "capo_agent_registry_control.types.descriptor_data.DescriptorData"
    ]
    """<p>The MCP tools descriptor content, serialized as descriptor payload data.</p>"""
    data_schema_version: NotRequired[
        "capo_agent_registry_control.types.data_schema_version.DataSchemaVersion"
    ]
    """<p>The schema version of the descriptor payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: McpToolsDescriptor) -> dict:
    out: dict = {}
    if "data" in value:
        out["data"] = value["data"]
    if "data_schema_version" in value:
        out["dataSchemaVersion"] = value["data_schema_version"]
    return out


def deserialize_json(data: dict) -> McpToolsDescriptor:
    out: McpToolsDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        out["data"] = data["data"]
    if data.get("dataSchemaVersion") is not None:
        out["data_schema_version"] = data["dataSchemaVersion"]
    return out
