"""Generated from Smithy shape ``com.amazonaws.voiceid#TagKeyList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_voice_id.types.tag_key

TagKeyList: TypeAlias = list["capo_voice_id.types.tag_key.TagKey"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TagKeyList:
    return [item for item in data if item is not None]


def redact_sensitive(value: TagKeyList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
