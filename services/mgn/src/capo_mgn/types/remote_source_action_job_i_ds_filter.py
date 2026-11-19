"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionJobIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_job_id

RemoteSourceActionJobIDsFilter: TypeAlias = list[
    "capo_mgn.types.remote_source_action_job_id.RemoteSourceActionJobID"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionJobIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> RemoteSourceActionJobIDsFilter:
    return [item for item in data if item is not None]
