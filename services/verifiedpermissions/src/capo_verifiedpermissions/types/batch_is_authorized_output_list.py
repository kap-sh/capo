"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedOutputList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_is_authorized_output_item

BatchIsAuthorizedOutputList: TypeAlias = list[
    "capo_verifiedpermissions.types.batch_is_authorized_output_item.BatchIsAuthorizedOutputItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedOutputList) -> list:
    import capo_verifiedpermissions.types.batch_is_authorized_output_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.batch_is_authorized_output_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchIsAuthorizedOutputList:
    import capo_verifiedpermissions.types.batch_is_authorized_output_item

    out: BatchIsAuthorizedOutputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.batch_is_authorized_output_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: BatchIsAuthorizedOutputList) -> list[Any]:
    import capo_verifiedpermissions.types.batch_is_authorized_output_item

    return [
        capo_verifiedpermissions.types.batch_is_authorized_output_item.redact_sensitive(
            item
        )
        for item in value
    ]
