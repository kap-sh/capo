"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationInsightsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_insight

NetworkMigrationInsightsList: TypeAlias = list[
    "capo_mgn.types.network_migration_insight.NetworkMigrationInsight"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationInsightsList) -> list:
    import capo_mgn.types.network_migration_insight

    out: list = []
    for item in value:
        out.append(capo_mgn.types.network_migration_insight.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkMigrationInsightsList:
    import capo_mgn.types.network_migration_insight

    out: NetworkMigrationInsightsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.network_migration_insight.deserialize_json(item))
    return out
