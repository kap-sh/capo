"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIConditionalFormattingOption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.kpi_actual_value_conditional_formatting
    import capo_quicksight.types.kpi_comparison_value_conditional_formatting
    import capo_quicksight.types.kpi_primary_value_conditional_formatting
    import capo_quicksight.types.kpi_progress_bar_conditional_formatting


class KPIConditionalFormattingOption(TypedDict, closed=True):
    primary_value: NotRequired[
        "capo_quicksight.types.kpi_primary_value_conditional_formatting.KPIPrimaryValueConditionalFormatting"
    ]
    """<p>The conditional formatting for the primary value of a KPI visual.</p>"""
    progress_bar: NotRequired[
        "capo_quicksight.types.kpi_progress_bar_conditional_formatting.KPIProgressBarConditionalFormatting"
    ]
    """<p>The conditional formatting for the progress bar of a KPI visual.</p>"""
    actual_value: NotRequired[
        "capo_quicksight.types.kpi_actual_value_conditional_formatting.KPIActualValueConditionalFormatting"
    ]
    """<p>The conditional formatting for the actual value of a KPI visual.</p>"""
    comparison_value: NotRequired[
        "capo_quicksight.types.kpi_comparison_value_conditional_formatting.KPIComparisonValueConditionalFormatting"
    ]
    """<p>The conditional formatting for the comparison value of a KPI visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIConditionalFormattingOption) -> dict:
    out: dict = {}
    if "primary_value" in value:
        import capo_quicksight.types.kpi_primary_value_conditional_formatting

        out["PrimaryValue"] = (
            capo_quicksight.types.kpi_primary_value_conditional_formatting.serialize_json(
                value["primary_value"]
            )
        )
    if "progress_bar" in value:
        import capo_quicksight.types.kpi_progress_bar_conditional_formatting

        out["ProgressBar"] = (
            capo_quicksight.types.kpi_progress_bar_conditional_formatting.serialize_json(
                value["progress_bar"]
            )
        )
    if "actual_value" in value:
        import capo_quicksight.types.kpi_actual_value_conditional_formatting

        out["ActualValue"] = (
            capo_quicksight.types.kpi_actual_value_conditional_formatting.serialize_json(
                value["actual_value"]
            )
        )
    if "comparison_value" in value:
        import capo_quicksight.types.kpi_comparison_value_conditional_formatting

        out["ComparisonValue"] = (
            capo_quicksight.types.kpi_comparison_value_conditional_formatting.serialize_json(
                value["comparison_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> KPIConditionalFormattingOption:
    out: KPIConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryValue") is not None:
        import capo_quicksight.types.kpi_primary_value_conditional_formatting

        out["primary_value"] = (
            capo_quicksight.types.kpi_primary_value_conditional_formatting.deserialize_json(
                data["PrimaryValue"]
            )
        )
    if data.get("ProgressBar") is not None:
        import capo_quicksight.types.kpi_progress_bar_conditional_formatting

        out["progress_bar"] = (
            capo_quicksight.types.kpi_progress_bar_conditional_formatting.deserialize_json(
                data["ProgressBar"]
            )
        )
    if data.get("ActualValue") is not None:
        import capo_quicksight.types.kpi_actual_value_conditional_formatting

        out["actual_value"] = (
            capo_quicksight.types.kpi_actual_value_conditional_formatting.deserialize_json(
                data["ActualValue"]
            )
        )
    if data.get("ComparisonValue") is not None:
        import capo_quicksight.types.kpi_comparison_value_conditional_formatting

        out["comparison_value"] = (
            capo_quicksight.types.kpi_comparison_value_conditional_formatting.deserialize_json(
                data["ComparisonValue"]
            )
        )
    return out


def redact_sensitive(value: KPIConditionalFormattingOption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_value" in value:
        import capo_quicksight.types.kpi_primary_value_conditional_formatting

        out["primary_value"] = (
            capo_quicksight.types.kpi_primary_value_conditional_formatting.redact_sensitive(
                value["primary_value"]
            )
        )
    if "progress_bar" in value:
        import capo_quicksight.types.kpi_progress_bar_conditional_formatting

        out["progress_bar"] = (
            capo_quicksight.types.kpi_progress_bar_conditional_formatting.redact_sensitive(
                value["progress_bar"]
            )
        )
    if "actual_value" in value:
        import capo_quicksight.types.kpi_actual_value_conditional_formatting

        out["actual_value"] = (
            capo_quicksight.types.kpi_actual_value_conditional_formatting.redact_sensitive(
                value["actual_value"]
            )
        )
    if "comparison_value" in value:
        import capo_quicksight.types.kpi_comparison_value_conditional_formatting

        out["comparison_value"] = (
            capo_quicksight.types.kpi_comparison_value_conditional_formatting.redact_sensitive(
                value["comparison_value"]
            )
        )
    return out
