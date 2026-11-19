"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#PolicyTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iam_toolbox.types.policy_type

PolicyTypeList: TypeAlias = list["capo_iam_toolbox.types.policy_type.PolicyType"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyTypeList) -> list:
    import capo_iam_toolbox.types.policy_type

    out: list = []
    for item in value:
        out.append(capo_iam_toolbox.types.policy_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyTypeList:
    import capo_iam_toolbox.types.policy_type

    out: PolicyTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iam_toolbox.types.policy_type.deserialize_json(item))
    return out
