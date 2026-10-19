"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UsageAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class UsageAmount(TypedDict, closed=True):
    start_hour: "datetime.datetime"
    """<p> The start hour of the usage period. </p>"""
    amount: "float"
    """<p> The usage amount for the period. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageAmount) -> dict:
    out: dict = {}
    import capo_bcm_pricing_calculator.types._prelude.timestamp

    out["startHour"] = (
        capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
            value["start_hour"]
        )
    )
    out["amount"] = (
        "NaN"
        if value["amount"] != value["amount"]
        else "Infinity"
        if value["amount"] == float("inf")
        else "-Infinity"
        if value["amount"] == float("-inf")
        else value["amount"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UsageAmount:
    out: UsageAmount = {}  # type: ignore[typeddict-item]
    if data.get("startHour") is not None:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["start_hour"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startHour"]
            )
        )
    else:
        import datetime

        out["start_hour"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("amount") is not None:
        out["amount"] = float(data["amount"])
    else:
        out["amount"] = 0.0
    return out
