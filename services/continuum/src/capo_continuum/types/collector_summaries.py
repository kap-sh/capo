"""Generated from Smithy shape ``com.amazonaws.continuum#CollectorSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.collector_summary

CollectorSummaries: TypeAlias = list[
    "capo_continuum.types.collector_summary.CollectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollectorSummaries) -> list:
    import capo_continuum.types.collector_summary

    out: list = []
    for item in value:
        out.append(capo_continuum.types.collector_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CollectorSummaries:
    import capo_continuum.types.collector_summary

    out: CollectorSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.collector_summary.deserialize_json(item))
    return out
