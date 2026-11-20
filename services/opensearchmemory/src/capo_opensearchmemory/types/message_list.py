"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MessageList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.message

MessageList: TypeAlias = list["capo_opensearchmemory.types.message.Message"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageList) -> list:
    import capo_opensearchmemory.types.message

    out: list = []
    for item in value:
        out.append(capo_opensearchmemory.types.message.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> MessageList:
    import capo_opensearchmemory.types.message

    out: MessageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_opensearchmemory.types.message.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: MessageList) -> list[Any]:
    import capo_opensearchmemory.types.message

    return [
        capo_opensearchmemory.types.message.redact_sensitive(item) for item in value
    ]
