"""Generated from Smithy shape ``com.amazonaws.continuum#CodeIssueSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.issue_summary

CodeIssueSummaries: TypeAlias = list["capo_continuum.types.issue_summary.IssueSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeIssueSummaries) -> list:
    import capo_continuum.types.issue_summary

    out: list = []
    for item in value:
        out.append(capo_continuum.types.issue_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeIssueSummaries:
    import capo_continuum.types.issue_summary

    out: CodeIssueSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.issue_summary.deserialize_json(item))
    return out
