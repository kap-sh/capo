"""Generated from Smithy shape ``com.amazonaws.devopsguru#ProactiveAnomaly``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.anomaly_description
    import capo_devops_guru.types.anomaly_id
    import capo_devops_guru.types.anomaly_limit
    import capo_devops_guru.types.anomaly_reported_time_range
    import capo_devops_guru.types.anomaly_resources
    import capo_devops_guru.types.anomaly_severity
    import capo_devops_guru.types.anomaly_source_details
    import capo_devops_guru.types.anomaly_source_metadata
    import capo_devops_guru.types.anomaly_status
    import capo_devops_guru.types.anomaly_time_range
    import capo_devops_guru.types.insight_id
    import capo_devops_guru.types.prediction_time_range
    import capo_devops_guru.types.resource_collection
    import capo_devops_guru.types.timestamp


class ProactiveAnomaly(TypedDict, closed=True):
    id: NotRequired["capo_devops_guru.types.anomaly_id.AnomalyId"]
    """<p> The ID of a proactive anomaly. </p>"""
    severity: NotRequired["capo_devops_guru.types.anomaly_severity.AnomalySeverity"]
    """<p>The severity of the anomaly. The severity of anomalies that generate an insight determine that insight's severity. For more information, see <a href="https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities">Understanding insight severities</a> in the <i>Amazon DevOps Guru User Guide</i>.</p>"""
    status: NotRequired["capo_devops_guru.types.anomaly_status.AnomalyStatus"]
    """<p> The status of a proactive anomaly. </p>"""
    update_time: NotRequired["capo_devops_guru.types.timestamp.Timestamp"]
    """<p> The time of the anomaly's most recent update. </p>"""
    anomaly_time_range: NotRequired[
        "capo_devops_guru.types.anomaly_time_range.AnomalyTimeRange"
    ]
    anomaly_reported_time_range: NotRequired[
        "capo_devops_guru.types.anomaly_reported_time_range.AnomalyReportedTimeRange"
    ]
    """<p> An <code>AnomalyReportedTimeRange</code> object that specifies the time range between when the anomaly is opened and the time when it is closed. </p>"""
    prediction_time_range: NotRequired[
        "capo_devops_guru.types.prediction_time_range.PredictionTimeRange"
    ]
    source_details: NotRequired[
        "capo_devops_guru.types.anomaly_source_details.AnomalySourceDetails"
    ]
    """<p> Details about the source of the analyzed operational data that triggered the anomaly. The one supported source is Amazon CloudWatch metrics. </p>"""
    associated_insight_id: NotRequired["capo_devops_guru.types.insight_id.InsightId"]
    """<p> The ID of the insight that contains this anomaly. An insight is composed of related anomalies. </p>"""
    resource_collection: NotRequired[
        "capo_devops_guru.types.resource_collection.ResourceCollection"
    ]
    limit: NotRequired["capo_devops_guru.types.anomaly_limit.AnomalyLimit"]
    """<p> A threshold that was exceeded by behavior in analyzed resources. Exceeding this threshold is related to the anomalous behavior that generated this anomaly. </p>"""
    source_metadata: NotRequired[
        "capo_devops_guru.types.anomaly_source_metadata.AnomalySourceMetadata"
    ]
    """<p>The metadata for the anomaly.</p>"""
    anomaly_resources: NotRequired[
        "capo_devops_guru.types.anomaly_resources.AnomalyResources"
    ]
    """<p>Information about a resource in which DevOps Guru detected anomalous behavior.</p>"""
    description: NotRequired[
        "capo_devops_guru.types.anomaly_description.AnomalyDescription"
    ]
    """<p> A description of the proactive anomaly. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProactiveAnomaly) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "severity" in value:
        import capo_devops_guru.types.anomaly_severity

        out["Severity"] = capo_devops_guru.types.anomaly_severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import capo_devops_guru.types.anomaly_status

        out["Status"] = capo_devops_guru.types.anomaly_status.serialize_json(
            value["status"]
        )
    if "update_time" in value:
        import capo_devops_guru.types.timestamp

        out["UpdateTime"] = capo_devops_guru.types.timestamp.serialize_json(
            value["update_time"]
        )
    if "anomaly_time_range" in value:
        import capo_devops_guru.types.anomaly_time_range

        out["AnomalyTimeRange"] = (
            capo_devops_guru.types.anomaly_time_range.serialize_json(
                value["anomaly_time_range"]
            )
        )
    if "anomaly_reported_time_range" in value:
        import capo_devops_guru.types.anomaly_reported_time_range

        out["AnomalyReportedTimeRange"] = (
            capo_devops_guru.types.anomaly_reported_time_range.serialize_json(
                value["anomaly_reported_time_range"]
            )
        )
    if "prediction_time_range" in value:
        import capo_devops_guru.types.prediction_time_range

        out["PredictionTimeRange"] = (
            capo_devops_guru.types.prediction_time_range.serialize_json(
                value["prediction_time_range"]
            )
        )
    if "source_details" in value:
        import capo_devops_guru.types.anomaly_source_details

        out["SourceDetails"] = (
            capo_devops_guru.types.anomaly_source_details.serialize_json(
                value["source_details"]
            )
        )
    if "associated_insight_id" in value:
        out["AssociatedInsightId"] = value["associated_insight_id"]
    if "resource_collection" in value:
        import capo_devops_guru.types.resource_collection

        out["ResourceCollection"] = (
            capo_devops_guru.types.resource_collection.serialize_json(
                value["resource_collection"]
            )
        )
    if "limit" in value:
        out["Limit"] = (
            "NaN"
            if value["limit"] != value["limit"]
            else "Infinity"
            if value["limit"] == float("inf")
            else "-Infinity"
            if value["limit"] == float("-inf")
            else value["limit"]
        )
    if "source_metadata" in value:
        import capo_devops_guru.types.anomaly_source_metadata

        out["SourceMetadata"] = (
            capo_devops_guru.types.anomaly_source_metadata.serialize_json(
                value["source_metadata"]
            )
        )
    if "anomaly_resources" in value:
        import capo_devops_guru.types.anomaly_resources

        out["AnomalyResources"] = (
            capo_devops_guru.types.anomaly_resources.serialize_json(
                value["anomaly_resources"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ProactiveAnomaly:
    out: ProactiveAnomaly = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Severity") is not None:
        import capo_devops_guru.types.anomaly_severity

        out["severity"] = capo_devops_guru.types.anomaly_severity.deserialize_json(
            data["Severity"]
        )
    if data.get("Status") is not None:
        import capo_devops_guru.types.anomaly_status

        out["status"] = capo_devops_guru.types.anomaly_status.deserialize_json(
            data["Status"]
        )
    if data.get("UpdateTime") is not None:
        import capo_devops_guru.types.timestamp

        out["update_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    if data.get("AnomalyTimeRange") is not None:
        import capo_devops_guru.types.anomaly_time_range

        out["anomaly_time_range"] = (
            capo_devops_guru.types.anomaly_time_range.deserialize_json(
                data["AnomalyTimeRange"]
            )
        )
    if data.get("AnomalyReportedTimeRange") is not None:
        import capo_devops_guru.types.anomaly_reported_time_range

        out["anomaly_reported_time_range"] = (
            capo_devops_guru.types.anomaly_reported_time_range.deserialize_json(
                data["AnomalyReportedTimeRange"]
            )
        )
    if data.get("PredictionTimeRange") is not None:
        import capo_devops_guru.types.prediction_time_range

        out["prediction_time_range"] = (
            capo_devops_guru.types.prediction_time_range.deserialize_json(
                data["PredictionTimeRange"]
            )
        )
    if data.get("SourceDetails") is not None:
        import capo_devops_guru.types.anomaly_source_details

        out["source_details"] = (
            capo_devops_guru.types.anomaly_source_details.deserialize_json(
                data["SourceDetails"]
            )
        )
    if data.get("AssociatedInsightId") is not None:
        out["associated_insight_id"] = data["AssociatedInsightId"]
    if data.get("ResourceCollection") is not None:
        import capo_devops_guru.types.resource_collection

        out["resource_collection"] = (
            capo_devops_guru.types.resource_collection.deserialize_json(
                data["ResourceCollection"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = float(data["Limit"])
    if data.get("SourceMetadata") is not None:
        import capo_devops_guru.types.anomaly_source_metadata

        out["source_metadata"] = (
            capo_devops_guru.types.anomaly_source_metadata.deserialize_json(
                data["SourceMetadata"]
            )
        )
    if data.get("AnomalyResources") is not None:
        import capo_devops_guru.types.anomaly_resources

        out["anomaly_resources"] = (
            capo_devops_guru.types.anomaly_resources.deserialize_json(
                data["AnomalyResources"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
