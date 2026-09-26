"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistrySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_summary

RegistrySummaryList: TypeAlias = list[
    "capo_agent_registry_control.types.registry_summary.RegistrySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistrySummaryList) -> list:
    import capo_agent_registry_control.types.registry_summary

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry_control.types.registry_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RegistrySummaryList:
    import capo_agent_registry_control.types.registry_summary

    out: RegistrySummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry_control.types.registry_summary.deserialize_json(item)
        )
    return out
