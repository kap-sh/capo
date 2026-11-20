"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SessionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.session_id

SessionIdList: TypeAlias = list["capo_opensearchmemory.types.session_id.SessionId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SessionIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SessionIdList:
    return [item for item in data if item is not None]
