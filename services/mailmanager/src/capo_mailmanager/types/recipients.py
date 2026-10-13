"""Generated from Smithy shape ``com.amazonaws.mailmanager#Recipients``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.email_address

Recipients: TypeAlias = list["capo_mailmanager.types.email_address.EmailAddress"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Recipients) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Recipients:
    return [item for item in data if item is not None]


def redact_sensitive(value: Recipients) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
