"""Generated from Smithy shape ``com.amazonaws.identitystore#Addresses``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.address

Addresses: TypeAlias = list["capo_identitystore.types.address.Address"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Addresses) -> list:
    import capo_identitystore.types.address

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.address.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Addresses:
    import capo_identitystore.types.address

    out: Addresses = []
    for item in data:
        if item is None:
            continue
        out.append(capo_identitystore.types.address.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Addresses) -> list[Any]:
    import capo_identitystore.types.address

    return [capo_identitystore.types.address.redact_sensitive(item) for item in value]
