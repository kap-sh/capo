"""Generated from Smithy shape ``com.amazonaws.pi#Insight``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_pi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pi.types.context_type
    import capo_pi.types.data_list
    import capo_pi.types.insight_list
    import capo_pi.types.iso_timestamp
    import capo_pi.types.markdown_string
    import capo_pi.types.recommendation_list
    import capo_pi.types.severity
    import capo_pi.types.string


class Insight(TypedDict, closed=True):
    insight_id: "capo_pi.types.string.String"
    """<p>The unique identifier for the insight. For example, <code>insight-12345678901234567</code>.</p>"""
    insight_type: NotRequired["capo_pi.types.string.String"]
    """<p>The type of insight. For example, <code>HighDBLoad</code>, <code>HighCPU</code>, or <code>DominatingSQLs</code>.</p>"""
    context: NotRequired["capo_pi.types.context_type.ContextType"]
    """<p>Indicates if the insight is causal or correlated insight.</p>"""
    start_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The start time of the insight. For example, <code>2018-10-30T00:00:00Z</code>.</p>"""
    end_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The end time of the insight. For example, <code>2018-10-30T00:00:00Z</code>.</p>"""
    severity: NotRequired["capo_pi.types.severity.Severity"]
    """<p>The severity of the insight. The values are: <code>Low</code>, <code>Medium</code>, or <code>High</code>.</p>"""
    supporting_insights: NotRequired["capo_pi.types.insight_list.InsightList"]
    """<p>List of supporting insights that provide additional factors for the insight.</p>"""
    description: NotRequired["capo_pi.types.markdown_string.MarkdownString"]
    """<p>Description of the insight. For example: <code>A high severity Insight found between 02:00 to 02:30, where there was an unusually high DB load 600x above baseline. Likely performance impact</code>.</p>"""
    recommendations: NotRequired["capo_pi.types.recommendation_list.RecommendationList"]
    """<p>List of recommendations for the insight. For example, <code>Investigate the following SQLs that contributed to 100% of the total DBLoad during that time period: sql-id</code>.</p>"""
    insight_data: NotRequired["capo_pi.types.data_list.DataList"]
    """<p>List of data objects containing metrics and references from the time range while generating the insight.</p>"""
    baseline_data: NotRequired["capo_pi.types.data_list.DataList"]
    """<p> Metric names and values from the timeframe used as baseline to generate the insight.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Insight) -> dict:
    out: dict = {}
    out["InsightId"] = value["insight_id"]
    if "insight_type" in value:
        out["InsightType"] = value["insight_type"]
    if "context" in value:
        import capo_pi.types.context_type

        out["Context"] = capo_pi.types.context_type.serialize_aws_json_1_1(
            value["context"]
        )
    if "start_time" in value:
        import capo_pi.types.iso_timestamp

        out["StartTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_pi.types.iso_timestamp

        out["EndTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "severity" in value:
        import capo_pi.types.severity

        out["Severity"] = capo_pi.types.severity.serialize_aws_json_1_1(
            value["severity"]
        )
    if "supporting_insights" in value:
        import capo_pi.types.insight_list

        out["SupportingInsights"] = capo_pi.types.insight_list.serialize_aws_json_1_1(
            value["supporting_insights"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "recommendations" in value:
        import capo_pi.types.recommendation_list

        out["Recommendations"] = (
            capo_pi.types.recommendation_list.serialize_aws_json_1_1(
                value["recommendations"]
            )
        )
    if "insight_data" in value:
        import capo_pi.types.data_list

        out["InsightData"] = capo_pi.types.data_list.serialize_aws_json_1_1(
            value["insight_data"]
        )
    if "baseline_data" in value:
        import capo_pi.types.data_list

        out["BaselineData"] = capo_pi.types.data_list.serialize_aws_json_1_1(
            value["baseline_data"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Insight:
    out: Insight = {}  # type: ignore[typeddict-item]
    if data.get("InsightId") is not None:
        out["insight_id"] = data["InsightId"]
    else:
        raise DeserializationError("Insight.insight_id required")
    if data.get("InsightType") is not None:
        out["insight_type"] = data["InsightType"]
    if data.get("Context") is not None:
        import capo_pi.types.context_type

        out["context"] = capo_pi.types.context_type.deserialize_aws_json_1_1(
            data["Context"]
        )
    if data.get("StartTime") is not None:
        import capo_pi.types.iso_timestamp

        out["start_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_pi.types.iso_timestamp

        out["end_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("Severity") is not None:
        import capo_pi.types.severity

        out["severity"] = capo_pi.types.severity.deserialize_aws_json_1_1(
            data["Severity"]
        )
    if data.get("SupportingInsights") is not None:
        import capo_pi.types.insight_list

        out["supporting_insights"] = (
            capo_pi.types.insight_list.deserialize_aws_json_1_1(
                data["SupportingInsights"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Recommendations") is not None:
        import capo_pi.types.recommendation_list

        out["recommendations"] = (
            capo_pi.types.recommendation_list.deserialize_aws_json_1_1(
                data["Recommendations"]
            )
        )
    if data.get("InsightData") is not None:
        import capo_pi.types.data_list

        out["insight_data"] = capo_pi.types.data_list.deserialize_aws_json_1_1(
            data["InsightData"]
        )
    if data.get("BaselineData") is not None:
        import capo_pi.types.data_list

        out["baseline_data"] = capo_pi.types.data_list.deserialize_aws_json_1_1(
            data["BaselineData"]
        )
    return out


def redact_sensitive(value: Insight) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "supporting_insights" in value:
        import capo_pi.types.insight_list

        out["supporting_insights"] = capo_pi.types.insight_list.redact_sensitive(
            value["supporting_insights"]
        )
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "recommendations" in value:
        import capo_pi.types.recommendation_list

        out["recommendations"] = capo_pi.types.recommendation_list.redact_sensitive(
            value["recommendations"]
        )
    return out
