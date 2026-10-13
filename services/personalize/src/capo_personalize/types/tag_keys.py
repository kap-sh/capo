"""Generated from Smithy shape ``com.amazonaws.personalize#TagKeys``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.tag_key

TagKeys: TypeAlias = list["capo_personalize.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeys:
    return [item for item in data if item is not None]


def redact_sensitive(value: TagKeys) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
