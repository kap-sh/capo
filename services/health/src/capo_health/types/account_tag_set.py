"""Generated from Smithy shape ``com.amazonaws.health#AccountTagSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.account_tag_key
    import capo_health.types.account_tag_value

AccountTagSet: TypeAlias = dict[
    "capo_health.types.account_tag_key.AccountTagKey",
    "capo_health.types.account_tag_value.AccountTagValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AccountTagSet) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountTagSet:
    out: AccountTagSet = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
