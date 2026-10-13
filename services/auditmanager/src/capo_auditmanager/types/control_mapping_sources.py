"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlMappingSources``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.control_mapping_source

ControlMappingSources: TypeAlias = list[
    "capo_auditmanager.types.control_mapping_source.ControlMappingSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlMappingSources) -> list:
    import capo_auditmanager.types.control_mapping_source

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.control_mapping_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlMappingSources:
    import capo_auditmanager.types.control_mapping_source

    out: ControlMappingSources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_auditmanager.types.control_mapping_source.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ControlMappingSources) -> list[Any]:
    import capo_auditmanager.types.control_mapping_source

    return [
        capo_auditmanager.types.control_mapping_source.redact_sensitive(item)
        for item in value
    ]
