"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyTemplatesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_template_item

PolicyTemplatesList: TypeAlias = list[
    "capo_verifiedpermissions.types.policy_template_item.PolicyTemplateItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyTemplatesList) -> list:
    import capo_verifiedpermissions.types.policy_template_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.policy_template_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyTemplatesList:
    import capo_verifiedpermissions.types.policy_template_item

    out: PolicyTemplatesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.policy_template_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: PolicyTemplatesList) -> list[Any]:
    import capo_verifiedpermissions.types.policy_template_item

    return [
        capo_verifiedpermissions.types.policy_template_item.redact_sensitive(item)
        for item in value
    ]
