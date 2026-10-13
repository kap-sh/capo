"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_item

PolicyList: TypeAlias = list["capo_verifiedpermissions.types.policy_item.PolicyItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyList) -> list:
    import capo_verifiedpermissions.types.policy_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.policy_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyList:
    import capo_verifiedpermissions.types.policy_item

    out: PolicyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.policy_item.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: PolicyList) -> list[Any]:
    import capo_verifiedpermissions.types.policy_item

    return [
        capo_verifiedpermissions.types.policy_item.redact_sensitive(item)
        for item in value
    ]
