"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationExecutionsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_execution

NetworkMigrationExecutionsList: TypeAlias = list[
    "capo_mgn.types.network_migration_execution.NetworkMigrationExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationExecutionsList) -> list:
    import capo_mgn.types.network_migration_execution

    out: list = []
    for item in value:
        out.append(capo_mgn.types.network_migration_execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkMigrationExecutionsList:
    import capo_mgn.types.network_migration_execution

    out: NetworkMigrationExecutionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.network_migration_execution.deserialize_json(item))
    return out


def redact_sensitive(value: NetworkMigrationExecutionsList) -> list[Any]:
    import capo_mgn.types.network_migration_execution

    return [
        capo_mgn.types.network_migration_execution.redact_sensitive(item)
        for item in value
    ]
