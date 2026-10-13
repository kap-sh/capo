"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedWithTokenInputList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_input_item

BatchIsAuthorizedWithTokenInputList: TypeAlias = list[
    "capo_verifiedpermissions.types.batch_is_authorized_with_token_input_item.BatchIsAuthorizedWithTokenInputItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedWithTokenInputList) -> list:
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_input_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.batch_is_authorized_with_token_input_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchIsAuthorizedWithTokenInputList:
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_input_item

    out: BatchIsAuthorizedWithTokenInputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.batch_is_authorized_with_token_input_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: BatchIsAuthorizedWithTokenInputList) -> list[Any]:
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_input_item

    return [
        capo_verifiedpermissions.types.batch_is_authorized_with_token_input_item.redact_sensitive(
            item
        )
        for item in value
    ]
