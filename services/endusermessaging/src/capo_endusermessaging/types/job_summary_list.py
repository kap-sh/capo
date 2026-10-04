"""Generated from Smithy shape ``com.amazonaws.endusermessaging#JobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.job_summary

JobSummaryList: TypeAlias = list["capo_endusermessaging.types.job_summary.JobSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: JobSummaryList) -> list:
    import capo_endusermessaging.types.job_summary

    out: list = []
    for item in value:
        out.append(capo_endusermessaging.types.job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobSummaryList:
    import capo_endusermessaging.types.job_summary

    out: JobSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_endusermessaging.types.job_summary.deserialize_json(item))
    return out
