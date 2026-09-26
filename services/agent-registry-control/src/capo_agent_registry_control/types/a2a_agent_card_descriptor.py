"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#A2aAgentCardDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.data_schema_version
    import capo_agent_registry_control.types.descriptor_data
    import capo_agent_registry_control.types.descriptor_source


class A2aAgentCardDescriptor(TypedDict, closed=True):
    data: NotRequired[
        "capo_agent_registry_control.types.descriptor_data.DescriptorData"
    ]
    """<p>The A2A agent card content, serialized as descriptor payload data.</p>"""
    data_schema_version: NotRequired[
        "capo_agent_registry_control.types.data_schema_version.DataSchemaVersion"
    ]
    """<p>The schema version of the descriptor payload.</p>"""
    source: NotRequired[
        "capo_agent_registry_control.types.descriptor_source.DescriptorSource"
    ]
    """<p>The optional source configuration used to synchronize the A2A agent card descriptor content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: A2aAgentCardDescriptor) -> dict:
    out: dict = {}
    if "data" in value:
        out["data"] = value["data"]
    if "data_schema_version" in value:
        out["dataSchemaVersion"] = value["data_schema_version"]
    if "source" in value:
        import capo_agent_registry_control.types.descriptor_source

        out["source"] = (
            capo_agent_registry_control.types.descriptor_source.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> A2aAgentCardDescriptor:
    out: A2aAgentCardDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        out["data"] = data["data"]
    if data.get("dataSchemaVersion") is not None:
        out["data_schema_version"] = data["dataSchemaVersion"]
    if data.get("source") is not None:
        import capo_agent_registry_control.types.descriptor_source

        out["source"] = (
            capo_agent_registry_control.types.descriptor_source.deserialize_json(
                data["source"]
            )
        )
    return out
