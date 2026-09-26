"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#Provenance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.provenance_relation
    import capo_agent_registry_control.types.source_details
    import capo_agent_registry_control.types.source_id
    import capo_agent_registry_control.types.source_type


class Provenance(TypedDict, closed=True):
    relation: "capo_agent_registry_control.types.provenance_relation.ProvenanceRelation"
    source_id: "capo_agent_registry_control.types.source_id.SourceId"
    """<p>The identifier of the upstream source that the registry record was detected from.</p>"""
    source_type: NotRequired["capo_agent_registry_control.types.source_type.SourceType"]
    """<p>The type of the upstream source that the registry record was detected from.</p>"""
    source_details: NotRequired[
        "capo_agent_registry_control.types.source_details.SourceDetails"
    ]
    """<p>Additional details about the upstream source that the registry record was detected from, such as the AgentCore Gateway or Runtime configuration. The populated member corresponds to the source type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Provenance) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.provenance_relation

    out["relation"] = (
        capo_agent_registry_control.types.provenance_relation.serialize_json(
            value["relation"]
        )
    )
    out["sourceId"] = value["source_id"]
    if "source_type" in value:
        import capo_agent_registry_control.types.source_type

        out["sourceType"] = (
            capo_agent_registry_control.types.source_type.serialize_json(
                value["source_type"]
            )
        )
    if "source_details" in value:
        import capo_agent_registry_control.types.source_details

        out["sourceDetails"] = (
            capo_agent_registry_control.types.source_details.serialize_json(
                value["source_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Provenance:
    out: Provenance = {}  # type: ignore[typeddict-item]
    if data.get("relation") is not None:
        import capo_agent_registry_control.types.provenance_relation

        out["relation"] = (
            capo_agent_registry_control.types.provenance_relation.deserialize_json(
                data["relation"]
            )
        )
    else:
        raise DeserializationError("Provenance.relation required")
    if data.get("sourceId") is not None:
        out["source_id"] = data["sourceId"]
    else:
        raise DeserializationError("Provenance.source_id required")
    if data.get("sourceType") is not None:
        import capo_agent_registry_control.types.source_type

        out["source_type"] = (
            capo_agent_registry_control.types.source_type.deserialize_json(
                data["sourceType"]
            )
        )
    if data.get("sourceDetails") is not None:
        import capo_agent_registry_control.types.source_details

        out["source_details"] = (
            capo_agent_registry_control.types.source_details.deserialize_json(
                data["sourceDetails"]
            )
        )
    return out
