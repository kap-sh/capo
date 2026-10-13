"""Generated from Smithy shape ``com.amazonaws.identitystore#Photos``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.photo

Photos: TypeAlias = list["capo_identitystore.types.photo.Photo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Photos) -> list:
    import capo_identitystore.types.photo

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.photo.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Photos:
    import capo_identitystore.types.photo

    out: Photos = []
    for item in data:
        if item is None:
            continue
        out.append(capo_identitystore.types.photo.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Photos) -> list[Any]:
    import capo_identitystore.types.photo

    return [capo_identitystore.types.photo.redact_sensitive(item) for item in value]
