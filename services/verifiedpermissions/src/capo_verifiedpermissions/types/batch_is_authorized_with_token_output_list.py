"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedWithTokenOutputList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_output_item

BatchIsAuthorizedWithTokenOutputList: TypeAlias = list[
    "capo_verifiedpermissions.types.batch_is_authorized_with_token_output_item.BatchIsAuthorizedWithTokenOutputItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedWithTokenOutputList) -> list:
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_output_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.batch_is_authorized_with_token_output_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchIsAuthorizedWithTokenOutputList:
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_output_item

    out: BatchIsAuthorizedWithTokenOutputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.batch_is_authorized_with_token_output_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: BatchIsAuthorizedWithTokenOutputList) -> list[Any]:
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_output_item

    return [
        capo_verifiedpermissions.types.batch_is_authorized_with_token_output_item.redact_sensitive(
            item
        )
        for item in value
    ]
