"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CedarTagRecordAttribute``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cedar_tag_value

CedarTagRecordAttribute: TypeAlias = dict[
    "str", "capo_verifiedpermissions.types.cedar_tag_value.CedarTagValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: CedarTagRecordAttribute) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_verifiedpermissions.types.cedar_tag_value

        out[key] = (
            capo_verifiedpermissions.types.cedar_tag_value.serialize_aws_json_1_0(value)
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CedarTagRecordAttribute:
    out: CedarTagRecordAttribute = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_verifiedpermissions.types.cedar_tag_value

        out[key] = (
            capo_verifiedpermissions.types.cedar_tag_value.deserialize_aws_json_1_0(
                value
            )
        )
    return out


def redact_sensitive(value: CedarTagRecordAttribute) -> dict[str, Any]:
    import capo_verifiedpermissions.types.cedar_tag_value

    return {
        key: capo_verifiedpermissions.types.cedar_tag_value.redact_sensitive(item)
        for key, item in value.items()
    }
