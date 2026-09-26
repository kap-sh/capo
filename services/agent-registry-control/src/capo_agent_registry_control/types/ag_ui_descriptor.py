"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AgUiDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.descriptor_source


class AgUiDescriptor(TypedDict, closed=True):
    source: NotRequired[
        "capo_agent_registry_control.types.descriptor_source.DescriptorSource"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AgUiDescriptor) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_agent_registry_control.types.descriptor_source

        out["source"] = (
            capo_agent_registry_control.types.descriptor_source.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgUiDescriptor:
    out: AgUiDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_agent_registry_control.types.descriptor_source

        out["source"] = (
            capo_agent_registry_control.types.descriptor_source.deserialize_json(
                data["source"]
            )
        )
    return out
