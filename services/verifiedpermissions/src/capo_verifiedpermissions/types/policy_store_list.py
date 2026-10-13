"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyStoreList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_store_item

PolicyStoreList: TypeAlias = list[
    "capo_verifiedpermissions.types.policy_store_item.PolicyStoreItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyStoreList) -> list:
    import capo_verifiedpermissions.types.policy_store_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.policy_store_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyStoreList:
    import capo_verifiedpermissions.types.policy_store_item

    out: PolicyStoreList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.policy_store_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: PolicyStoreList) -> list[Any]:
    import capo_verifiedpermissions.types.policy_store_item

    return [
        capo_verifiedpermissions.types.policy_store_item.redact_sensitive(item)
        for item in value
    ]
