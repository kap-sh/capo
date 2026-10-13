"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#RouteSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.route_summary

RouteSummaries: TypeAlias = list[
    "capo_migration_hub_refactor_spaces.types.route_summary.RouteSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSummaries) -> list:
    import capo_migration_hub_refactor_spaces.types.route_summary

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub_refactor_spaces.types.route_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteSummaries:
    import capo_migration_hub_refactor_spaces.types.route_summary

    out: RouteSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_migration_hub_refactor_spaces.types.route_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: RouteSummaries) -> list[Any]:
    import capo_migration_hub_refactor_spaces.types.route_summary

    return [
        capo_migration_hub_refactor_spaces.types.route_summary.redact_sensitive(item)
        for item in value
    ]
