"""Generated from Smithy shape ``com.amazonaws.billing#RejectionReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.rejection_reason

RejectionReasons: TypeAlias = list[
    "capo_billing.types.rejection_reason.RejectionReason"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectionReasons) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RejectionReasons:
    return [item for item in data if item is not None]
