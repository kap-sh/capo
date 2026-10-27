"""Generated from Smithy shape ``com.amazonaws.billing#MultiplierType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of an investment multiplier. A value of <code>PERCENTAGE</code> applies a percentage of a value, expressed as a decimal string. A value of <code>CURRENCY_AMOUNT</code> applies a currency amount per unit of attestation input.</p>"""
MultiplierType: TypeAlias = Literal[
    "PERCENTAGE",
    "CURRENCY_AMOUNT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultiplierType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MultiplierType:
    return cast(MultiplierType, data)
