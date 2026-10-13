"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntityList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.entity_item

EntityList: TypeAlias = list["capo_verifiedpermissions.types.entity_item.EntityItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntityList) -> list:
    import capo_verifiedpermissions.types.entity_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.entity_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EntityList:
    import capo_verifiedpermissions.types.entity_item

    out: EntityList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.entity_item.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: EntityList) -> list[Any]:
    import capo_verifiedpermissions.types.entity_item

    return [
        capo_verifiedpermissions.types.entity_item.redact_sensitive(item)
        for item in value
    ]
