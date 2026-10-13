"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#SetAttribute``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.attribute_value

SetAttribute: TypeAlias = list[
    "capo_verifiedpermissions.types.attribute_value.AttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetAttribute) -> list:
    import capo_verifiedpermissions.types.attribute_value

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.attribute_value.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SetAttribute:
    import capo_verifiedpermissions.types.attribute_value

    out: SetAttribute = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.attribute_value.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: SetAttribute) -> list[Any]:
    import capo_verifiedpermissions.types.attribute_value

    return [
        capo_verifiedpermissions.types.attribute_value.redact_sensitive(item)
        for item in value
    ]
