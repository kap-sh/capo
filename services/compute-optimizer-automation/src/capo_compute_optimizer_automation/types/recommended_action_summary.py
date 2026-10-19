"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.recommended_action_total


class RecommendedActionSummary(TypedDict, closed=True):
    key: "str"
    """<p>The grouping key used to categorize the recommended actions in this summary.</p>"""
    total: "capo_compute_optimizer_automation.types.recommended_action_total.RecommendedActionTotal"
    """<p>Aggregate totals for the recommended actions in this group, including count and estimated savings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActionSummary) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_compute_optimizer_automation.types.recommended_action_total

    out["total"] = (
        capo_compute_optimizer_automation.types.recommended_action_total.serialize_aws_json_1_0(
            value["total"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendedActionSummary:
    out: RecommendedActionSummary = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("total") is not None:
        import capo_compute_optimizer_automation.types.recommended_action_total

        out["total"] = (
            capo_compute_optimizer_automation.types.recommended_action_total.deserialize_aws_json_1_0(
                data["total"]
            )
        )
    else:
        raise DeserializationError("RecommendedActionSummary.total required")
    return out
