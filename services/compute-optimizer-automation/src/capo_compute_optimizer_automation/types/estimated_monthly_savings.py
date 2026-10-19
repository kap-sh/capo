"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EstimatedMonthlySavings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.savings_estimation_mode


class EstimatedMonthlySavings(TypedDict, closed=True):
    currency: "str"
    """<p> The currency of the estimated savings. </p>"""
    before_discount_savings: "float"
    """<p> The estimated monthly savings before applying any discounts. </p>"""
    after_discount_savings: "float"
    """<p> The estimated monthly savings after applying any discounts. </p>"""
    savings_estimation_mode: "capo_compute_optimizer_automation.types.savings_estimation_mode.SavingsEstimationMode"
    """<p>The mode used to calculate savings, either BeforeDiscount or AfterDiscount.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EstimatedMonthlySavings) -> dict:
    out: dict = {}
    out["currency"] = value["currency"]
    out["beforeDiscountSavings"] = (
        "NaN"
        if value["before_discount_savings"] != value["before_discount_savings"]
        else "Infinity"
        if value["before_discount_savings"] == float("inf")
        else "-Infinity"
        if value["before_discount_savings"] == float("-inf")
        else value["before_discount_savings"]
    )
    out["afterDiscountSavings"] = (
        "NaN"
        if value["after_discount_savings"] != value["after_discount_savings"]
        else "Infinity"
        if value["after_discount_savings"] == float("inf")
        else "-Infinity"
        if value["after_discount_savings"] == float("-inf")
        else value["after_discount_savings"]
    )
    import capo_compute_optimizer_automation.types.savings_estimation_mode

    out["savingsEstimationMode"] = (
        capo_compute_optimizer_automation.types.savings_estimation_mode.serialize_aws_json_1_0(
            value["savings_estimation_mode"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EstimatedMonthlySavings:
    out: EstimatedMonthlySavings = {}  # type: ignore[typeddict-item]
    if data.get("currency") is not None:
        out["currency"] = data["currency"]
    else:
        out["currency"] = ""
    if data.get("beforeDiscountSavings") is not None:
        out["before_discount_savings"] = float(data["beforeDiscountSavings"])
    else:
        out["before_discount_savings"] = 0.0
    if data.get("afterDiscountSavings") is not None:
        out["after_discount_savings"] = float(data["afterDiscountSavings"])
    else:
        out["after_discount_savings"] = 0.0
    if data.get("savingsEstimationMode") is not None:
        import capo_compute_optimizer_automation.types.savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_compute_optimizer_automation.types.savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    else:
        import typing

        out["savings_estimation_mode"] = typing.cast(
            "capo_compute_optimizer_automation.types.savings_estimation_mode.SavingsEstimationMode",
            "",
        )
    return out
