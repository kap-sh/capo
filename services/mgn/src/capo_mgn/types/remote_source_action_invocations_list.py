"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionInvocationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_invocation

RemoteSourceActionInvocationsList: TypeAlias = list[
    "capo_mgn.types.remote_source_action_invocation.RemoteSourceActionInvocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionInvocationsList) -> list:
    import capo_mgn.types.remote_source_action_invocation

    out: list = []
    for item in value:
        out.append(capo_mgn.types.remote_source_action_invocation.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemoteSourceActionInvocationsList:
    import capo_mgn.types.remote_source_action_invocation

    out: RemoteSourceActionInvocationsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mgn.types.remote_source_action_invocation.deserialize_json(item)
        )
    return out
