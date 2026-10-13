"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentBlueprintSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.environment_blueprint_summary

EnvironmentBlueprintSummaries: TypeAlias = list[
    "capo_datazone.types.environment_blueprint_summary.EnvironmentBlueprintSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentBlueprintSummaries) -> list:
    import capo_datazone.types.environment_blueprint_summary

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.environment_blueprint_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnvironmentBlueprintSummaries:
    import capo_datazone.types.environment_blueprint_summary

    out: EnvironmentBlueprintSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_datazone.types.environment_blueprint_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: EnvironmentBlueprintSummaries) -> list[Any]:
    import capo_datazone.types.environment_blueprint_summary

    return [
        capo_datazone.types.environment_blueprint_summary.redact_sensitive(item)
        for item in value
    ]
