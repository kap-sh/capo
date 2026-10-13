"""Generated from Smithy shape ``com.amazonaws.voiceid#TagList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_voice_id.types.tag

TagList: TypeAlias = list["capo_voice_id.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagList) -> list:
    import capo_voice_id.types.tag

    out: list = []
    for item in value:
        out.append(capo_voice_id.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TagList:
    import capo_voice_id.types.tag

    out: TagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_voice_id.types.tag.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: TagList) -> list[Any]:
    import capo_voice_id.types.tag

    return [capo_voice_id.types.tag.redact_sensitive(item) for item in value]
