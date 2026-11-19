"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_id

RemoteSourceActionIDsFilter: TypeAlias = list[
    "capo_mgn.types.remote_source_action_id.RemoteSourceActionID"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> RemoteSourceActionIDsFilter:
    return [item for item in data if item is not None]
