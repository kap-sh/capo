"""Generated from Smithy shape ``com.amazonaws.endusermessaging#JobResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.job_resource

JobResourceList: TypeAlias = list[
    "capo_endusermessaging.types.job_resource.JobResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobResourceList) -> list:
    import capo_endusermessaging.types.job_resource

    out: list = []
    for item in value:
        out.append(capo_endusermessaging.types.job_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobResourceList:
    import capo_endusermessaging.types.job_resource

    out: JobResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_endusermessaging.types.job_resource.deserialize_json(item))
    return out
