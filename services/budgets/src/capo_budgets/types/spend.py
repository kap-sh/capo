"""Generated from Smithy shape ``com.amazonaws.budgets#Spend``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.numeric_value
    import capo_budgets.types.unit_value


class Spend(TypedDict, closed=True):
    amount: "capo_budgets.types.numeric_value.NumericValue"
    """<p>The cost or usage amount that's associated with a budget forecast, actual spend, or budget threshold.</p>"""
    unit: "capo_budgets.types.unit_value.UnitValue"
    """<p>The unit of measurement that's used for the budget forecast, actual spend, or budget threshold.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Spend) -> dict:
    out: dict = {}
    out["Amount"] = value["amount"]
    out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Spend:
    out: Spend = {}  # type: ignore[typeddict-item]
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    else:
        out["amount"] = ""
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    else:
        out["unit"] = ""
    return out
