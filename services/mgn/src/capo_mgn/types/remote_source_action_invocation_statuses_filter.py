"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionInvocationStatusesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_invocation_status

RemoteSourceActionInvocationStatusesFilter: TypeAlias = list[
    "capo_mgn.types.remote_source_action_invocation_status.RemoteSourceActionInvocationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionInvocationStatusesFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> RemoteSourceActionInvocationStatusesFilter:
    return [item for item in data if item is not None]
