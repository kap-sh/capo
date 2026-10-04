"""Generated from Smithy shape ``com.amazonaws.endusermessaging#JobResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.job_result

JobResults: TypeAlias = list["capo_endusermessaging.types.job_result.JobResult"]


# --- restJson1 ser/de ---
def serialize_json(value: JobResults) -> list:
    import capo_endusermessaging.types.job_result

    out: list = []
    for item in value:
        out.append(capo_endusermessaging.types.job_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobResults:
    import capo_endusermessaging.types.job_result

    out: JobResults = []
    for item in data:
        if item is None:
            continue
        out.append(capo_endusermessaging.types.job_result.deserialize_json(item))
    return out
