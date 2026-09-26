"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#MatchedPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iam_toolbox.types.matched_policy

MatchedPolicyList: TypeAlias = list[
    "capo_iam_toolbox.types.matched_policy.MatchedPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchedPolicyList) -> list:
    import capo_iam_toolbox.types.matched_policy

    out: list = []
    for item in value:
        out.append(capo_iam_toolbox.types.matched_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchedPolicyList:
    import capo_iam_toolbox.types.matched_policy

    out: MatchedPolicyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iam_toolbox.types.matched_policy.deserialize_json(item))
    return out
