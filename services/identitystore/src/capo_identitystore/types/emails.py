"""Generated from Smithy shape ``com.amazonaws.identitystore#Emails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.email

Emails: TypeAlias = list["capo_identitystore.types.email.Email"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Emails) -> list:
    import capo_identitystore.types.email

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.email.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Emails:
    import capo_identitystore.types.email

    out: Emails = []
    for item in data:
        if item is None:
            continue
        out.append(capo_identitystore.types.email.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Emails) -> list[Any]:
    import capo_identitystore.types.email

    return [capo_identitystore.types.email.redact_sensitive(item) for item in value]
