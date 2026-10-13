"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#EnvironmentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.environment_summary

EnvironmentList: TypeAlias = list[
    "capo_workspaces_thin_client.types.environment_summary.EnvironmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentList) -> list:
    import capo_workspaces_thin_client.types.environment_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_thin_client.types.environment_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnvironmentList:
    import capo_workspaces_thin_client.types.environment_summary

    out: EnvironmentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_thin_client.types.environment_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: EnvironmentList) -> list[Any]:
    import capo_workspaces_thin_client.types.environment_summary

    return [
        capo_workspaces_thin_client.types.environment_summary.redact_sensitive(item)
        for item in value
    ]
