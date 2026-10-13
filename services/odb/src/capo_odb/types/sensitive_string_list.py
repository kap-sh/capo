"""Generated from Smithy shape ``com.amazonaws.odb#SensitiveStringList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.sensitive_string

SensitiveStringList: TypeAlias = list["capo_odb.types.sensitive_string.SensitiveString"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SensitiveStringList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SensitiveStringList:
    return [item for item in data if item is not None]


def redact_sensitive(value: SensitiveStringList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
