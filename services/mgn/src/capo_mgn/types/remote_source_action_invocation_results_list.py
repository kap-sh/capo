"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionInvocationResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_invocation_result

RemoteSourceActionInvocationResultsList: TypeAlias = list[
    "capo_mgn.types.remote_source_action_invocation_result.RemoteSourceActionInvocationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionInvocationResultsList) -> list:
    import capo_mgn.types.remote_source_action_invocation_result

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.remote_source_action_invocation_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RemoteSourceActionInvocationResultsList:
    import capo_mgn.types.remote_source_action_invocation_result

    out: RemoteSourceActionInvocationResultsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mgn.types.remote_source_action_invocation_result.deserialize_json(item)
        )
    return out
