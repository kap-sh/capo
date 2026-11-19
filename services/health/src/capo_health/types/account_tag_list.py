"""Generated from Smithy shape ``com.amazonaws.health#AccountTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.account_tag

AccountTagList: TypeAlias = list["capo_health.types.account_tag.AccountTag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountTagList) -> list:
    import capo_health.types.account_tag

    out: list = []
    for item in value:
        out.append(capo_health.types.account_tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AccountTagList:
    import capo_health.types.account_tag

    out: AccountTagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.account_tag.deserialize_aws_json_1_1(item))
    return out
