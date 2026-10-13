"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ServiceSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.service_summary

ServiceSummaries: TypeAlias = list[
    "capo_migration_hub_refactor_spaces.types.service_summary.ServiceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSummaries) -> list:
    import capo_migration_hub_refactor_spaces.types.service_summary

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub_refactor_spaces.types.service_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceSummaries:
    import capo_migration_hub_refactor_spaces.types.service_summary

    out: ServiceSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_migration_hub_refactor_spaces.types.service_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ServiceSummaries) -> list[Any]:
    import capo_migration_hub_refactor_spaces.types.service_summary

    return [
        capo_migration_hub_refactor_spaces.types.service_summary.redact_sensitive(item)
        for item in value
    ]
