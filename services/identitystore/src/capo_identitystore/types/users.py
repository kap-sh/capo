"""Generated from Smithy shape ``com.amazonaws.identitystore#Users``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.user

Users: TypeAlias = list["capo_identitystore.types.user.User"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Users) -> list:
    import capo_identitystore.types.user

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.user.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Users:
    import capo_identitystore.types.user

    out: Users = []
    for item in data:
        if item is None:
            continue
        out.append(capo_identitystore.types.user.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Users) -> list[Any]:
    import capo_identitystore.types.user

    return [capo_identitystore.types.user.redact_sensitive(item) for item in value]
