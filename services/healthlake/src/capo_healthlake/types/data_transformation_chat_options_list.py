"""Generated from Smithy shape ``com.amazonaws.healthlake#DataTransformationChatOptionsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_chat_option_string

DataTransformationChatOptionsList: TypeAlias = list[
    "capo_healthlake.types.data_transformation_chat_option_string.DataTransformationChatOptionString"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataTransformationChatOptionsList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> DataTransformationChatOptionsList:
    return [item for item in data if item is not None]


def redact_sensitive(value: DataTransformationChatOptionsList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
