"""Generated from Smithy shape ``com.amazonaws.identitystore#Filters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.filter

Filters: TypeAlias = list["capo_identitystore.types.filter.Filter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filters) -> list:
    import capo_identitystore.types.filter

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Filters:
    import capo_identitystore.types.filter

    out: Filters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_identitystore.types.filter.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Filters) -> list[Any]:
    import capo_identitystore.types.filter

    return [capo_identitystore.types.filter.redact_sensitive(item) for item in value]
