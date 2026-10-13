"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CedarTagSetAttribute``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cedar_tag_value

CedarTagSetAttribute: TypeAlias = list[
    "capo_verifiedpermissions.types.cedar_tag_value.CedarTagValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CedarTagSetAttribute) -> list:
    import capo_verifiedpermissions.types.cedar_tag_value

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.cedar_tag_value.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CedarTagSetAttribute:
    import capo_verifiedpermissions.types.cedar_tag_value

    out: CedarTagSetAttribute = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.cedar_tag_value.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: CedarTagSetAttribute) -> list[Any]:
    import capo_verifiedpermissions.types.cedar_tag_value

    return [
        capo_verifiedpermissions.types.cedar_tag_value.redact_sensitive(item)
        for item in value
    ]
