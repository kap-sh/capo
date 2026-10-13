"""Generated from Smithy shape ``com.amazonaws.identitystore#PhoneNumbers``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.phone_number

PhoneNumbers: TypeAlias = list["capo_identitystore.types.phone_number.PhoneNumber"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhoneNumbers) -> list:
    import capo_identitystore.types.phone_number

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.phone_number.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PhoneNumbers:
    import capo_identitystore.types.phone_number

    out: PhoneNumbers = []
    for item in data:
        if item is None:
            continue
        out.append(capo_identitystore.types.phone_number.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: PhoneNumbers) -> list[Any]:
    import capo_identitystore.types.phone_number

    return [
        capo_identitystore.types.phone_number.redact_sensitive(item) for item in value
    ]
