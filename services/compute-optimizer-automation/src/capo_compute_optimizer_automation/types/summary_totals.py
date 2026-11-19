"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#SummaryTotals``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.estimated_monthly_savings


class SummaryTotals(TypedDict, closed=True):
    automation_event_count: NotRequired["int"]
    """<p>The total number of automation events in this summary group.</p>"""
    estimated_monthly_savings: NotRequired[
        "capo_compute_optimizer_automation.types.estimated_monthly_savings.EstimatedMonthlySavings"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryTotals) -> dict:
    out: dict = {}
    if "automation_event_count" in value:
        out["automationEventCount"] = value["automation_event_count"]
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SummaryTotals:
    out: SummaryTotals = {}  # type: ignore[typeddict-item]
    if data.get("automationEventCount") is not None:
        out["automation_event_count"] = data["automationEventCount"]
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SummaryTotals) -> dict:
    out: dict = {}
    if "automation_event_count" in value:
        out["automationEventCount"] = value["automation_event_count"]
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.serialize_cbor(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SummaryTotals:
    out: SummaryTotals = {}  # type: ignore[typeddict-item]
    if data.get("automationEventCount") is not None:
        out["automation_event_count"] = data["automationEventCount"]
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_cbor(
                data["estimatedMonthlySavings"]
            )
        )
    return out
