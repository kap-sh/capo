"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RulePreviewTotal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.estimated_monthly_savings


class RulePreviewTotal(TypedDict, closed=True):
    recommended_action_count: "int"
    """<p>The total number of recommended actions matching the rule preview configuration.</p>"""
    estimated_monthly_savings: "capo_compute_optimizer_automation.types.estimated_monthly_savings.EstimatedMonthlySavings"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RulePreviewTotal) -> dict:
    out: dict = {}
    out["recommendedActionCount"] = value["recommended_action_count"]
    import capo_compute_optimizer_automation.types.estimated_monthly_savings

    out["estimatedMonthlySavings"] = (
        capo_compute_optimizer_automation.types.estimated_monthly_savings.serialize_aws_json_1_0(
            value["estimated_monthly_savings"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RulePreviewTotal:
    out: RulePreviewTotal = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActionCount") is not None:
        out["recommended_action_count"] = data["recommendedActionCount"]
    else:
        out["recommended_action_count"] = 0
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    else:
        raise DeserializationError(
            "RulePreviewTotal.estimated_monthly_savings required"
        )
    return out
