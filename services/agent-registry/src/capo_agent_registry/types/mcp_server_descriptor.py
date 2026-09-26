"""Generated from Smithy shape ``com.amazonaws.agentregistry#McpServerDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry.types.data_schema_version
    import capo_agent_registry.types.descriptor_data
    import capo_agent_registry.types.descriptor_source
    import capo_agent_registry.types.mcp_server_additional_data


class McpServerDescriptor(TypedDict, closed=True):
    data: NotRequired["capo_agent_registry.types.descriptor_data.DescriptorData"]
    """<p> The MCP server descriptor content, serialized as descriptor payload data.</p>"""
    data_schema_version: NotRequired[
        "capo_agent_registry.types.data_schema_version.DataSchemaVersion"
    ]
    """<p> The schema version of the descriptor payload.</p>"""
    additional_data: NotRequired[
        "capo_agent_registry.types.mcp_server_additional_data.McpServerAdditionalData"
    ]
    """<p> Additional data associated with the MCP server descriptor, such as tool definitions.</p>"""
    source: NotRequired["capo_agent_registry.types.descriptor_source.DescriptorSource"]
    """<p> The source location from which the MCP (Model Context Protocol) server descriptor content was retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: McpServerDescriptor) -> dict:
    out: dict = {}
    if "data" in value:
        out["data"] = value["data"]
    if "data_schema_version" in value:
        out["dataSchemaVersion"] = value["data_schema_version"]
    if "additional_data" in value:
        import capo_agent_registry.types.mcp_server_additional_data

        out["additionalData"] = (
            capo_agent_registry.types.mcp_server_additional_data.serialize_json(
                value["additional_data"]
            )
        )
    if "source" in value:
        import capo_agent_registry.types.descriptor_source

        out["source"] = capo_agent_registry.types.descriptor_source.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> McpServerDescriptor:
    out: McpServerDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        out["data"] = data["data"]
    if data.get("dataSchemaVersion") is not None:
        out["data_schema_version"] = data["dataSchemaVersion"]
    if data.get("additionalData") is not None:
        import capo_agent_registry.types.mcp_server_additional_data

        out["additional_data"] = (
            capo_agent_registry.types.mcp_server_additional_data.deserialize_json(
                data["additionalData"]
            )
        )
    if data.get("source") is not None:
        import capo_agent_registry.types.descriptor_source

        out["source"] = capo_agent_registry.types.descriptor_source.deserialize_json(
            data["source"]
        )
    return out
