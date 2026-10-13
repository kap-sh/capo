"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIR``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.topic_ir_contribution_analysis
    import capo_quicksight.types.topic_ir_filter_list
    import capo_quicksight.types.topic_ir_group_by_list
    import capo_quicksight.types.topic_ir_metric_list
    import capo_quicksight.types.topic_sort_clause
    import capo_quicksight.types.visual_options


class TopicIR(TypedDict, closed=True):
    metrics: NotRequired["capo_quicksight.types.topic_ir_metric_list.TopicIRMetricList"]
    """<p>The metrics for the <code>TopicIR</code>.</p>"""
    group_by_list: NotRequired[
        "capo_quicksight.types.topic_ir_group_by_list.TopicIRGroupByList"
    ]
    """<p>The GroupBy list for the <code>TopicIR</code>.</p>"""
    filters: NotRequired["capo_quicksight.types.topic_ir_filter_list.TopicIRFilterList"]
    """<p>The filters for the <code>TopicIR</code>.</p>"""
    sort: NotRequired["capo_quicksight.types.topic_sort_clause.TopicSortClause"]
    """<p>The sort for the <code>TopicIR</code>.</p>"""
    contribution_analysis: NotRequired[
        "capo_quicksight.types.topic_ir_contribution_analysis.TopicIRContributionAnalysis"
    ]
    """<p>The contribution analysis for the <code>TopicIR</code>.</p>"""
    visual: NotRequired["capo_quicksight.types.visual_options.VisualOptions"]
    """<p>The visual for the <code>TopicIR</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIR) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_quicksight.types.topic_ir_metric_list

        out["Metrics"] = capo_quicksight.types.topic_ir_metric_list.serialize_json(
            value["metrics"]
        )
    if "group_by_list" in value:
        import capo_quicksight.types.topic_ir_group_by_list

        out["GroupByList"] = (
            capo_quicksight.types.topic_ir_group_by_list.serialize_json(
                value["group_by_list"]
            )
        )
    if "filters" in value:
        import capo_quicksight.types.topic_ir_filter_list

        out["Filters"] = capo_quicksight.types.topic_ir_filter_list.serialize_json(
            value["filters"]
        )
    if "sort" in value:
        import capo_quicksight.types.topic_sort_clause

        out["Sort"] = capo_quicksight.types.topic_sort_clause.serialize_json(
            value["sort"]
        )
    if "contribution_analysis" in value:
        import capo_quicksight.types.topic_ir_contribution_analysis

        out["ContributionAnalysis"] = (
            capo_quicksight.types.topic_ir_contribution_analysis.serialize_json(
                value["contribution_analysis"]
            )
        )
    if "visual" in value:
        import capo_quicksight.types.visual_options

        out["Visual"] = capo_quicksight.types.visual_options.serialize_json(
            value["visual"]
        )
    return out


def deserialize_json(data: dict) -> TopicIR:
    out: TopicIR = {}  # type: ignore[typeddict-item]
    if data.get("Metrics") is not None:
        import capo_quicksight.types.topic_ir_metric_list

        out["metrics"] = capo_quicksight.types.topic_ir_metric_list.deserialize_json(
            data["Metrics"]
        )
    if data.get("GroupByList") is not None:
        import capo_quicksight.types.topic_ir_group_by_list

        out["group_by_list"] = (
            capo_quicksight.types.topic_ir_group_by_list.deserialize_json(
                data["GroupByList"]
            )
        )
    if data.get("Filters") is not None:
        import capo_quicksight.types.topic_ir_filter_list

        out["filters"] = capo_quicksight.types.topic_ir_filter_list.deserialize_json(
            data["Filters"]
        )
    if data.get("Sort") is not None:
        import capo_quicksight.types.topic_sort_clause

        out["sort"] = capo_quicksight.types.topic_sort_clause.deserialize_json(
            data["Sort"]
        )
    if data.get("ContributionAnalysis") is not None:
        import capo_quicksight.types.topic_ir_contribution_analysis

        out["contribution_analysis"] = (
            capo_quicksight.types.topic_ir_contribution_analysis.deserialize_json(
                data["ContributionAnalysis"]
            )
        )
    if data.get("Visual") is not None:
        import capo_quicksight.types.visual_options

        out["visual"] = capo_quicksight.types.visual_options.deserialize_json(
            data["Visual"]
        )
    return out


def redact_sensitive(value: TopicIR) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "metrics" in value:
        import capo_quicksight.types.topic_ir_metric_list

        out["metrics"] = capo_quicksight.types.topic_ir_metric_list.redact_sensitive(
            value["metrics"]
        )
    return out
