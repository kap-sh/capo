"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ParentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.entity_identifier

ParentList: TypeAlias = list[
    "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParentList) -> list:
    import capo_verifiedpermissions.types.entity_identifier

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ParentList:
    import capo_verifiedpermissions.types.entity_identifier

    out: ParentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: ParentList) -> list[Any]:
    import capo_verifiedpermissions.types.entity_identifier

    return [
        capo_verifiedpermissions.types.entity_identifier.redact_sensitive(item)
        for item in value
    ]
