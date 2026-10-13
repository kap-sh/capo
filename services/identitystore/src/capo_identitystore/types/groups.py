"""Generated from Smithy shape ``com.amazonaws.identitystore#Groups``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.group

Groups: TypeAlias = list["capo_identitystore.types.group.Group"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Groups) -> list:
    import capo_identitystore.types.group

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Groups:
    import capo_identitystore.types.group

    out: Groups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_identitystore.types.group.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Groups) -> list[Any]:
    import capo_identitystore.types.group

    return [capo_identitystore.types.group.redact_sensitive(item) for item in value]
