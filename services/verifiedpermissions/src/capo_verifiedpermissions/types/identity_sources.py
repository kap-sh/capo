"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IdentitySources``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.identity_source_item

IdentitySources: TypeAlias = list[
    "capo_verifiedpermissions.types.identity_source_item.IdentitySourceItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentitySources) -> list:
    import capo_verifiedpermissions.types.identity_source_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.identity_source_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdentitySources:
    import capo_verifiedpermissions.types.identity_source_item

    out: IdentitySources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.identity_source_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: IdentitySources) -> list[Any]:
    import capo_verifiedpermissions.types.identity_source_item

    return [
        capo_verifiedpermissions.types.identity_source_item.redact_sensitive(item)
        for item in value
    ]
