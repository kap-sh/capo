"""Generated from Smithy shape ``com.amazonaws.mgn#JobsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.job

JobsList: TypeAlias = list["capo_mgn.types.job.Job"]


# --- restJson1 ser/de ---
def serialize_json(value: JobsList) -> list:
    import capo_mgn.types.job

    out: list = []
    for item in value:
        out.append(capo_mgn.types.job.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobsList:
    import capo_mgn.types.job

    out: JobsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.job.deserialize_json(item))
    return out


def redact_sensitive(value: JobsList) -> list[Any]:
    import capo_mgn.types.job

    return [capo_mgn.types.job.redact_sensitive(item) for item in value]
