"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of an investment summary. A value of <code>MILESTONE_BASED</code> indicates a fixed investment amount disbursed on a schedule. A value of <code>OUTCOME_BASED</code> indicates an investment awarded based on the completion of a defined outcome or milestone.</p>"""
InvestmentType: TypeAlias = Literal[
    "MILESTONE_BASED",
    "OUTCOME_BASED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvestmentType:
    return cast(InvestmentType, data)
