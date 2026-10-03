"""Generated from Smithy shape ``com.amazonaws.devopsguru#ProactiveInsightSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.associated_resource_arns
    import capo_devops_guru.types.insight_id
    import capo_devops_guru.types.insight_name
    import capo_devops_guru.types.insight_severity
    import capo_devops_guru.types.insight_status
    import capo_devops_guru.types.insight_time_range
    import capo_devops_guru.types.prediction_time_range
    import capo_devops_guru.types.resource_collection
    import capo_devops_guru.types.service_collection


class ProactiveInsightSummary(TypedDict, closed=True):
    id: NotRequired["capo_devops_guru.types.insight_id.InsightId"]
    """<p>The ID of the proactive insight. </p>"""
    name: NotRequired["capo_devops_guru.types.insight_name.InsightName"]
    """<p>The name of the proactive insight. </p>"""
    severity: NotRequired["capo_devops_guru.types.insight_severity.InsightSeverity"]
    """<p>The severity of the insight. For more information, see <a href="https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities">Understanding insight severities</a> in the <i>Amazon DevOps Guru User Guide</i>.</p>"""
    status: NotRequired["capo_devops_guru.types.insight_status.InsightStatus"]
    """<p>The status of the proactive insight. </p>"""
    insight_time_range: NotRequired[
        "capo_devops_guru.types.insight_time_range.InsightTimeRange"
    ]
    prediction_time_range: NotRequired[
        "capo_devops_guru.types.prediction_time_range.PredictionTimeRange"
    ]
    resource_collection: NotRequired[
        "capo_devops_guru.types.resource_collection.ResourceCollection"
    ]
    service_collection: NotRequired[
        "capo_devops_guru.types.service_collection.ServiceCollection"
    ]
    """<p>A collection of the names of Amazon Web Services services.</p>"""
    associated_resource_arns: NotRequired[
        "capo_devops_guru.types.associated_resource_arns.AssociatedResourceArns"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Amazon Web Services resources that generated this insight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProactiveInsightSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "severity" in value:
        import capo_devops_guru.types.insight_severity

        out["Severity"] = capo_devops_guru.types.insight_severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import capo_devops_guru.types.insight_status

        out["Status"] = capo_devops_guru.types.insight_status.serialize_json(
            value["status"]
        )
    if "insight_time_range" in value:
        import capo_devops_guru.types.insight_time_range

        out["InsightTimeRange"] = (
            capo_devops_guru.types.insight_time_range.serialize_json(
                value["insight_time_range"]
            )
        )
    if "prediction_time_range" in value:
        import capo_devops_guru.types.prediction_time_range

        out["PredictionTimeRange"] = (
            capo_devops_guru.types.prediction_time_range.serialize_json(
                value["prediction_time_range"]
            )
        )
    if "resource_collection" in value:
        import capo_devops_guru.types.resource_collection

        out["ResourceCollection"] = (
            capo_devops_guru.types.resource_collection.serialize_json(
                value["resource_collection"]
            )
        )
    if "service_collection" in value:
        import capo_devops_guru.types.service_collection

        out["ServiceCollection"] = (
            capo_devops_guru.types.service_collection.serialize_json(
                value["service_collection"]
            )
        )
    if "associated_resource_arns" in value:
        import capo_devops_guru.types.associated_resource_arns

        out["AssociatedResourceArns"] = (
            capo_devops_guru.types.associated_resource_arns.serialize_json(
                value["associated_resource_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProactiveInsightSummary:
    out: ProactiveInsightSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Severity") is not None:
        import capo_devops_guru.types.insight_severity

        out["severity"] = capo_devops_guru.types.insight_severity.deserialize_json(
            data["Severity"]
        )
    if data.get("Status") is not None:
        import capo_devops_guru.types.insight_status

        out["status"] = capo_devops_guru.types.insight_status.deserialize_json(
            data["Status"]
        )
    if data.get("InsightTimeRange") is not None:
        import capo_devops_guru.types.insight_time_range

        out["insight_time_range"] = (
            capo_devops_guru.types.insight_time_range.deserialize_json(
                data["InsightTimeRange"]
            )
        )
    if data.get("PredictionTimeRange") is not None:
        import capo_devops_guru.types.prediction_time_range

        out["prediction_time_range"] = (
            capo_devops_guru.types.prediction_time_range.deserialize_json(
                data["PredictionTimeRange"]
            )
        )
    if data.get("ResourceCollection") is not None:
        import capo_devops_guru.types.resource_collection

        out["resource_collection"] = (
            capo_devops_guru.types.resource_collection.deserialize_json(
                data["ResourceCollection"]
            )
        )
    if data.get("ServiceCollection") is not None:
        import capo_devops_guru.types.service_collection

        out["service_collection"] = (
            capo_devops_guru.types.service_collection.deserialize_json(
                data["ServiceCollection"]
            )
        )
    if data.get("AssociatedResourceArns") is not None:
        import capo_devops_guru.types.associated_resource_arns

        out["associated_resource_arns"] = (
            capo_devops_guru.types.associated_resource_arns.deserialize_json(
                data["AssociatedResourceArns"]
            )
        )
    return out
