"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RecordTypeSchemaOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.record_type_schema_override

RecordTypeSchemaOverrideList: TypeAlias = list[
    "capo_agent_registry_control.types.record_type_schema_override.RecordTypeSchemaOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordTypeSchemaOverrideList) -> list:
    import capo_agent_registry_control.types.record_type_schema_override

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry_control.types.record_type_schema_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecordTypeSchemaOverrideList:
    import capo_agent_registry_control.types.record_type_schema_override

    out: RecordTypeSchemaOverrideList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry_control.types.record_type_schema_override.deserialize_json(
                item
            )
        )
    return out
