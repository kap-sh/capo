"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ApplicationSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.application_summary

ApplicationSummaries: TypeAlias = list[
    "capo_migration_hub_refactor_spaces.types.application_summary.ApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummaries) -> list:
    import capo_migration_hub_refactor_spaces.types.application_summary

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub_refactor_spaces.types.application_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ApplicationSummaries:
    import capo_migration_hub_refactor_spaces.types.application_summary

    out: ApplicationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_migration_hub_refactor_spaces.types.application_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ApplicationSummaries) -> list[Any]:
    import capo_migration_hub_refactor_spaces.types.application_summary

    return [
        capo_migration_hub_refactor_spaces.types.application_summary.redact_sensitive(
            item
        )
        for item in value
    ]
