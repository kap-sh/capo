"""Generated from Smithy shape ``com.amazonaws.deadline#JobSearchSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.job_search_summary

JobSearchSummaries: TypeAlias = list[
    "capo_deadline.types.job_search_summary.JobSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobSearchSummaries) -> list:
    import capo_deadline.types.job_search_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.job_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobSearchSummaries:
    import capo_deadline.types.job_search_summary

    out: JobSearchSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.job_search_summary.deserialize_json(item))
    return out


def redact_sensitive(value: JobSearchSummaries) -> list[Any]:
    import capo_deadline.types.job_search_summary

    return [
        capo_deadline.types.job_search_summary.redact_sensitive(item) for item in value
    ]
