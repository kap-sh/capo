"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action

RemoteSourceActionsList: TypeAlias = list[
    "capo_mgn.types.remote_source_action.RemoteSourceAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionsList) -> list:
    import capo_mgn.types.remote_source_action

    out: list = []
    for item in value:
        out.append(capo_mgn.types.remote_source_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemoteSourceActionsList:
    import capo_mgn.types.remote_source_action

    out: RemoteSourceActionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.remote_source_action.deserialize_json(item))
    return out


def redact_sensitive(value: RemoteSourceActionsList) -> list[Any]:
    import capo_mgn.types.remote_source_action

    return [
        capo_mgn.types.remote_source_action.redact_sensitive(item) for item in value
    ]
