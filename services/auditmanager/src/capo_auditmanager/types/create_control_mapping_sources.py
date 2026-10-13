"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateControlMappingSources``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.create_control_mapping_source

CreateControlMappingSources: TypeAlias = list[
    "capo_auditmanager.types.create_control_mapping_source.CreateControlMappingSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateControlMappingSources) -> list:
    import capo_auditmanager.types.create_control_mapping_source

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.create_control_mapping_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateControlMappingSources:
    import capo_auditmanager.types.create_control_mapping_source

    out: CreateControlMappingSources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_auditmanager.types.create_control_mapping_source.deserialize_json(item)
        )
    return out


def redact_sensitive(value: CreateControlMappingSources) -> list[Any]:
    import capo_auditmanager.types.create_control_mapping_source

    return [
        capo_auditmanager.types.create_control_mapping_source.redact_sensitive(item)
        for item in value
    ]
