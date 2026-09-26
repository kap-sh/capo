"""Generated from Smithy shape ``com.amazonaws.agentregistry#CustomDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry.types.descriptor_data


class CustomDescriptor(TypedDict, closed=True):
    data: NotRequired["capo_agent_registry.types.descriptor_data.DescriptorData"]
    """<p>The custom descriptor content, serialized as descriptor payload data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDescriptor) -> dict:
    out: dict = {}
    if "data" in value:
        out["data"] = value["data"]
    return out


def deserialize_json(data: dict) -> CustomDescriptor:
    out: CustomDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        out["data"] = data["data"]
    return out
