"""Generated from Smithy shape ``com.amazonaws.identitystore#Roles``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.role

Roles: TypeAlias = list["capo_identitystore.types.role.Role"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Roles) -> list:
    import capo_identitystore.types.role

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.role.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Roles:
    import capo_identitystore.types.role

    out: Roles = []
    for item in data:
        if item is None:
            continue
        out.append(capo_identitystore.types.role.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Roles) -> list[Any]:
    import capo_identitystore.types.role

    return [capo_identitystore.types.role.redact_sensitive(item) for item in value]
