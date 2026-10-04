"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ProvenanceRelation``."""

from typing import Literal, TypeAlias, cast

ProvenanceRelation: TypeAlias = Literal["DETECTED_FROM",]


# --- restJson1 ser/de ---
def serialize_json(value: ProvenanceRelation) -> str:
    return value


def deserialize_json(data: str) -> ProvenanceRelation:
    return cast(ProvenanceRelation, data)
