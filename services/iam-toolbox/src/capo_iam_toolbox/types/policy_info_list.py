"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#PolicyInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iam_toolbox.types.policy_info

PolicyInfoList: TypeAlias = list["capo_iam_toolbox.types.policy_info.PolicyInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyInfoList) -> list:
    import capo_iam_toolbox.types.policy_info

    out: list = []
    for item in value:
        out.append(capo_iam_toolbox.types.policy_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyInfoList:
    import capo_iam_toolbox.types.policy_info

    out: PolicyInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iam_toolbox.types.policy_info.deserialize_json(item))
    return out
