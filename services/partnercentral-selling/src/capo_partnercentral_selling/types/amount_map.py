"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AmountMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.monetary_amount

AmountMap: TypeAlias = dict[
    "str", "capo_partnercentral_selling.types.monetary_amount.MonetaryAmount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: AmountMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> AmountMap:
    out: AmountMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: AmountMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
