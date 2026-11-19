"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEventSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.summary_dimensions
    import capo_compute_optimizer_automation.types.summary_totals
    import capo_compute_optimizer_automation.types.time_period


class AutomationEventSummary(TypedDict, closed=True):
    key: NotRequired["str"]
    """<p>The key identifier for this summary grouping.</p>"""
    dimensions: NotRequired[
        "capo_compute_optimizer_automation.types.summary_dimensions.SummaryDimensions"
    ]
    """<p>The dimensions used to group this summary, such as event status.</p>"""
    time_period: NotRequired[
        "capo_compute_optimizer_automation.types.time_period.TimePeriod"
    ]
    """<p>The time period covered by this summary, with inclusive start time and exclusive end time.</p>"""
    total: NotRequired[
        "capo_compute_optimizer_automation.types.summary_totals.SummaryTotals"
    ]
    """<p>The aggregated totals for this summary, including event count and estimated savings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEventSummary) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "dimensions" in value:
        import capo_compute_optimizer_automation.types.summary_dimensions

        out["dimensions"] = (
            capo_compute_optimizer_automation.types.summary_dimensions.serialize_aws_json_1_0(
                value["dimensions"]
            )
        )
    if "time_period" in value:
        import capo_compute_optimizer_automation.types.time_period

        out["timePeriod"] = (
            capo_compute_optimizer_automation.types.time_period.serialize_aws_json_1_0(
                value["time_period"]
            )
        )
    if "total" in value:
        import capo_compute_optimizer_automation.types.summary_totals

        out["total"] = (
            capo_compute_optimizer_automation.types.summary_totals.serialize_aws_json_1_0(
                value["total"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutomationEventSummary:
    out: AutomationEventSummary = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("dimensions") is not None:
        import capo_compute_optimizer_automation.types.summary_dimensions

        out["dimensions"] = (
            capo_compute_optimizer_automation.types.summary_dimensions.deserialize_aws_json_1_0(
                data["dimensions"]
            )
        )
    if data.get("timePeriod") is not None:
        import capo_compute_optimizer_automation.types.time_period

        out["time_period"] = (
            capo_compute_optimizer_automation.types.time_period.deserialize_aws_json_1_0(
                data["timePeriod"]
            )
        )
    if data.get("total") is not None:
        import capo_compute_optimizer_automation.types.summary_totals

        out["total"] = (
            capo_compute_optimizer_automation.types.summary_totals.deserialize_aws_json_1_0(
                data["total"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutomationEventSummary) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "dimensions" in value:
        import capo_compute_optimizer_automation.types.summary_dimensions

        out["dimensions"] = (
            capo_compute_optimizer_automation.types.summary_dimensions.serialize_cbor(
                value["dimensions"]
            )
        )
    if "time_period" in value:
        import capo_compute_optimizer_automation.types.time_period

        out["timePeriod"] = (
            capo_compute_optimizer_automation.types.time_period.serialize_cbor(
                value["time_period"]
            )
        )
    if "total" in value:
        import capo_compute_optimizer_automation.types.summary_totals

        out["total"] = (
            capo_compute_optimizer_automation.types.summary_totals.serialize_cbor(
                value["total"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AutomationEventSummary:
    out: AutomationEventSummary = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("dimensions") is not None:
        import capo_compute_optimizer_automation.types.summary_dimensions

        out["dimensions"] = (
            capo_compute_optimizer_automation.types.summary_dimensions.deserialize_cbor(
                data["dimensions"]
            )
        )
    if data.get("timePeriod") is not None:
        import capo_compute_optimizer_automation.types.time_period

        out["time_period"] = (
            capo_compute_optimizer_automation.types.time_period.deserialize_cbor(
                data["timePeriod"]
            )
        )
    if data.get("total") is not None:
        import capo_compute_optimizer_automation.types.summary_totals

        out["total"] = (
            capo_compute_optimizer_automation.types.summary_totals.deserialize_cbor(
                data["total"]
            )
        )
    return out
