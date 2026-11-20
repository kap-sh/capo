"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.tag

TagList: TypeAlias = list["capo_opensearchmemory.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagList) -> list:
    import capo_opensearchmemory.types.tag

    out: list = []
    for item in value:
        out.append(capo_opensearchmemory.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TagList:
    import capo_opensearchmemory.types.tag

    out: TagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_opensearchmemory.types.tag.deserialize_aws_json_1_0(item))
    return out
