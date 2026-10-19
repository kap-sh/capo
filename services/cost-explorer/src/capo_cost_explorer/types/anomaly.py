"""Generated from Smithy shape ``com.amazonaws.costexplorer#Anomaly``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.anomaly_feedback_type
    import capo_cost_explorer.types.anomaly_score
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.impact
    import capo_cost_explorer.types.root_causes
    import capo_cost_explorer.types.year_month_day


class Anomaly(TypedDict, closed=True):
    anomaly_id: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier for the anomaly. </p>"""
    anomaly_start_date: NotRequired[
        "capo_cost_explorer.types.year_month_day.YearMonthDay"
    ]
    """<p>The first day the anomaly is detected. </p>"""
    anomaly_end_date: NotRequired[
        "capo_cost_explorer.types.year_month_day.YearMonthDay"
    ]
    """<p>The last day the anomaly is detected. </p>"""
    dimension_value: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The dimension for the anomaly (for example, an Amazon Web Services service in a service monitor). </p>"""
    root_causes: NotRequired["capo_cost_explorer.types.root_causes.RootCauses"]
    """<p>The list of identified root causes for the anomaly. </p>"""
    anomaly_score: "capo_cost_explorer.types.anomaly_score.AnomalyScore"
    """<p>The latest and maximum score for the anomaly. </p>"""
    impact: "capo_cost_explorer.types.impact.Impact"
    """<p>The dollar impact for the anomaly. </p>"""
    monitor_arn: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) for the cost monitor that generated this anomaly. </p>"""
    feedback: NotRequired[
        "capo_cost_explorer.types.anomaly_feedback_type.AnomalyFeedbackType"
    ]
    """<p>The feedback value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Anomaly) -> dict:
    out: dict = {}
    out["AnomalyId"] = value["anomaly_id"]
    if "anomaly_start_date" in value:
        out["AnomalyStartDate"] = value["anomaly_start_date"]
    if "anomaly_end_date" in value:
        out["AnomalyEndDate"] = value["anomaly_end_date"]
    if "dimension_value" in value:
        out["DimensionValue"] = value["dimension_value"]
    if "root_causes" in value:
        import capo_cost_explorer.types.root_causes

        out["RootCauses"] = capo_cost_explorer.types.root_causes.serialize_aws_json_1_1(
            value["root_causes"]
        )
    import capo_cost_explorer.types.anomaly_score

    out["AnomalyScore"] = capo_cost_explorer.types.anomaly_score.serialize_aws_json_1_1(
        value["anomaly_score"]
    )
    import capo_cost_explorer.types.impact

    out["Impact"] = capo_cost_explorer.types.impact.serialize_aws_json_1_1(
        value["impact"]
    )
    out["MonitorArn"] = value["monitor_arn"]
    if "feedback" in value:
        import capo_cost_explorer.types.anomaly_feedback_type

        out["Feedback"] = (
            capo_cost_explorer.types.anomaly_feedback_type.serialize_aws_json_1_1(
                value["feedback"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Anomaly:
    out: Anomaly = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyId") is not None:
        out["anomaly_id"] = data["AnomalyId"]
    else:
        out["anomaly_id"] = ""
    if data.get("AnomalyStartDate") is not None:
        out["anomaly_start_date"] = data["AnomalyStartDate"]
    if data.get("AnomalyEndDate") is not None:
        out["anomaly_end_date"] = data["AnomalyEndDate"]
    if data.get("DimensionValue") is not None:
        out["dimension_value"] = data["DimensionValue"]
    if data.get("RootCauses") is not None:
        import capo_cost_explorer.types.root_causes

        out["root_causes"] = (
            capo_cost_explorer.types.root_causes.deserialize_aws_json_1_1(
                data["RootCauses"]
            )
        )
    if data.get("AnomalyScore") is not None:
        import capo_cost_explorer.types.anomaly_score

        out["anomaly_score"] = (
            capo_cost_explorer.types.anomaly_score.deserialize_aws_json_1_1(
                data["AnomalyScore"]
            )
        )
    else:
        raise DeserializationError("Anomaly.anomaly_score required")
    if data.get("Impact") is not None:
        import capo_cost_explorer.types.impact

        out["impact"] = capo_cost_explorer.types.impact.deserialize_aws_json_1_1(
            data["Impact"]
        )
    else:
        raise DeserializationError("Anomaly.impact required")
    if data.get("MonitorArn") is not None:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        out["monitor_arn"] = ""
    if data.get("Feedback") is not None:
        import capo_cost_explorer.types.anomaly_feedback_type

        out["feedback"] = (
            capo_cost_explorer.types.anomaly_feedback_type.deserialize_aws_json_1_1(
                data["Feedback"]
            )
        )
    return out
