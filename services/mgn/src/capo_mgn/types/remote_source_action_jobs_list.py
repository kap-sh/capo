"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionJobsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_job

RemoteSourceActionJobsList: TypeAlias = list[
    "capo_mgn.types.remote_source_action_job.RemoteSourceActionJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionJobsList) -> list:
    import capo_mgn.types.remote_source_action_job

    out: list = []
    for item in value:
        out.append(capo_mgn.types.remote_source_action_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemoteSourceActionJobsList:
    import capo_mgn.types.remote_source_action_job

    out: RemoteSourceActionJobsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.remote_source_action_job.deserialize_json(item))
    return out


def redact_sensitive(value: RemoteSourceActionJobsList) -> list[Any]:
    import capo_mgn.types.remote_source_action_job

    return [
        capo_mgn.types.remote_source_action_job.redact_sensitive(item) for item in value
    ]
