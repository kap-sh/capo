"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ProvenanceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.provenance_summary

ProvenanceSummaryList: TypeAlias = list[
    "capo_agent_registry_control.types.provenance_summary.ProvenanceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvenanceSummaryList) -> list:
    import capo_agent_registry_control.types.provenance_summary

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry_control.types.provenance_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProvenanceSummaryList:
    import capo_agent_registry_control.types.provenance_summary

    out: ProvenanceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry_control.types.provenance_summary.deserialize_json(item)
        )
    return out
