"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ActionIdentifierList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.action_identifier

ActionIdentifierList: TypeAlias = list[
    "capo_verifiedpermissions.types.action_identifier.ActionIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionIdentifierList) -> list:
    import capo_verifiedpermissions.types.action_identifier

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.action_identifier.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ActionIdentifierList:
    import capo_verifiedpermissions.types.action_identifier

    out: ActionIdentifierList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.action_identifier.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: ActionIdentifierList) -> list[Any]:
    import capo_verifiedpermissions.types.action_identifier

    return [
        capo_verifiedpermissions.types.action_identifier.redact_sensitive(item)
        for item in value
    ]
