"""Generated from Smithy shape ``com.amazonaws.billing#SplitPortions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.split_portion

SplitPortions: TypeAlias = list["capo_billing.types.split_portion.SplitPortion"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SplitPortions) -> list:
    import capo_billing.types.split_portion

    out: list = []
    for item in value:
        out.append(capo_billing.types.split_portion.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SplitPortions:
    import capo_billing.types.split_portion

    out: SplitPortions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.split_portion.deserialize_aws_json_1_0(item))
    return out
