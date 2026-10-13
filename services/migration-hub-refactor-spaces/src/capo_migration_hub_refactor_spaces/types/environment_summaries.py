"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#EnvironmentSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.environment_summary

EnvironmentSummaries: TypeAlias = list[
    "capo_migration_hub_refactor_spaces.types.environment_summary.EnvironmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSummaries) -> list:
    import capo_migration_hub_refactor_spaces.types.environment_summary

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub_refactor_spaces.types.environment_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnvironmentSummaries:
    import capo_migration_hub_refactor_spaces.types.environment_summary

    out: EnvironmentSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_migration_hub_refactor_spaces.types.environment_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: EnvironmentSummaries) -> list[Any]:
    import capo_migration_hub_refactor_spaces.types.environment_summary

    return [
        capo_migration_hub_refactor_spaces.types.environment_summary.redact_sensitive(
            item
        )
        for item in value
    ]
