"""Generated from Smithy shape ``com.amazonaws.mgn#ReplicationConfigurationTemplates``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.replication_configuration_template

ReplicationConfigurationTemplates: TypeAlias = list[
    "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationTemplates) -> list:
    import capo_mgn.types.replication_configuration_template

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.replication_configuration_template.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReplicationConfigurationTemplates:
    import capo_mgn.types.replication_configuration_template

    out: ReplicationConfigurationTemplates = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mgn.types.replication_configuration_template.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ReplicationConfigurationTemplates) -> list[Any]:
    import capo_mgn.types.replication_configuration_template

    return [
        capo_mgn.types.replication_configuration_template.redact_sensitive(item)
        for item in value
    ]
