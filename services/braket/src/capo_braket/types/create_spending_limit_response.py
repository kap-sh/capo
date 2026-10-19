"""Generated from Smithy shape ``com.amazonaws.braket#CreateSpendingLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.spending_limit_arn


class CreateSpendingLimitResponse(TypedDict, closed=True):
    spending_limit_arn: "capo_braket.types.spending_limit_arn.SpendingLimitArn"
    """<p>The Amazon Resource Name (ARN) of the created spending limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSpendingLimitResponse) -> dict:
    out: dict = {}
    out["spendingLimitArn"] = value["spending_limit_arn"]
    return out


def deserialize_json(data: dict) -> CreateSpendingLimitResponse:
    out: CreateSpendingLimitResponse = {}  # type: ignore[typeddict-item]
    if data.get("spendingLimitArn") is not None:
        out["spending_limit_arn"] = data["spendingLimitArn"]
    else:
        out["spending_limit_arn"] = ""
    return out
