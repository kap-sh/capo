"""Generated from Smithy shape ``com.amazonaws.continuum#CodeFindingSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.finding_summary

CodeFindingSummaries: TypeAlias = list[
    "capo_continuum.types.finding_summary.FindingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeFindingSummaries) -> list:
    import capo_continuum.types.finding_summary

    out: list = []
    for item in value:
        out.append(capo_continuum.types.finding_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeFindingSummaries:
    import capo_continuum.types.finding_summary

    out: CodeFindingSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.finding_summary.deserialize_json(item))
    return out
