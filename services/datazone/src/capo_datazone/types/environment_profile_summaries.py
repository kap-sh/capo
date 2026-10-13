"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentProfileSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.environment_profile_summary

EnvironmentProfileSummaries: TypeAlias = list[
    "capo_datazone.types.environment_profile_summary.EnvironmentProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentProfileSummaries) -> list:
    import capo_datazone.types.environment_profile_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.environment_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentProfileSummaries:
    import capo_datazone.types.environment_profile_summary

    out: EnvironmentProfileSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_datazone.types.environment_profile_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: EnvironmentProfileSummaries) -> list[Any]:
    import capo_datazone.types.environment_profile_summary

    return [
        capo_datazone.types.environment_profile_summary.redact_sensitive(item)
        for item in value
    ]
