"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ProvenanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.provenance

ProvenanceList: TypeAlias = list[
    "capo_agent_registry_control.types.provenance.Provenance"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvenanceList) -> list:
    import capo_agent_registry_control.types.provenance

    out: list = []
    for item in value:
        out.append(capo_agent_registry_control.types.provenance.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProvenanceList:
    import capo_agent_registry_control.types.provenance

    out: ProvenanceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_agent_registry_control.types.provenance.deserialize_json(item))
    return out
