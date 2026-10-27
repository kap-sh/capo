"""Generated from Smithy shape ``com.amazonaws.billing#AdditionalRecipients``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.additional_recipient

AdditionalRecipients: TypeAlias = list[
    "capo_billing.types.additional_recipient.AdditionalRecipient"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AdditionalRecipients) -> list:
    import capo_billing.types.additional_recipient

    out: list = []
    for item in value:
        out.append(capo_billing.types.additional_recipient.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AdditionalRecipients:
    import capo_billing.types.additional_recipient

    out: AdditionalRecipients = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.additional_recipient.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: AdditionalRecipients) -> list[Any]:
    import capo_billing.types.additional_recipient

    return [
        capo_billing.types.additional_recipient.redact_sensitive(item) for item in value
    ]
