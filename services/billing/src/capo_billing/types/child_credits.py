"""Generated from Smithy shape ``com.amazonaws.billing#ChildCredits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.child_credit

ChildCredits: TypeAlias = list["capo_billing.types.child_credit.ChildCredit"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChildCredits) -> list:
    import capo_billing.types.child_credit

    out: list = []
    for item in value:
        out.append(capo_billing.types.child_credit.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ChildCredits:
    import capo_billing.types.child_credit

    out: ChildCredits = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.child_credit.deserialize_aws_json_1_0(item))
    return out
