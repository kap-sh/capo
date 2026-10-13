"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.project_summary

ProjectSummaries: TypeAlias = list["capo_datazone.types.project_summary.ProjectSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectSummaries) -> list:
    import capo_datazone.types.project_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.project_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectSummaries:
    import capo_datazone.types.project_summary

    out: ProjectSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.project_summary.deserialize_json(item))
    return out


def redact_sensitive(value: ProjectSummaries) -> list[Any]:
    import capo_datazone.types.project_summary

    return [
        capo_datazone.types.project_summary.redact_sensitive(item) for item in value
    ]
