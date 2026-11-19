"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_arn

RemoteSourceActionArns: TypeAlias = list[
    "capo_mgn.types.remote_source_action_arn.RemoteSourceActionArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionArns) -> list:
    return list(value)


def deserialize_json(data: list) -> RemoteSourceActionArns:
    return [item for item in data if item is not None]
