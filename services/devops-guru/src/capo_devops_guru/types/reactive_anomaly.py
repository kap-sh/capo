"""Generated from Smithy shape ``com.amazonaws.devopsguru#ReactiveAnomaly``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.anomaly_description
    import capo_devops_guru.types.anomaly_id
    import capo_devops_guru.types.anomaly_name
    import capo_devops_guru.types.anomaly_reported_time_range
    import capo_devops_guru.types.anomaly_resources
    import capo_devops_guru.types.anomaly_severity
    import capo_devops_guru.types.anomaly_source_details
    import capo_devops_guru.types.anomaly_status
    import capo_devops_guru.types.anomaly_time_range
    import capo_devops_guru.types.anomaly_type
    import capo_devops_guru.types.insight_id
    import capo_devops_guru.types.resource_collection


class ReactiveAnomaly(TypedDict, closed=True):
    id: NotRequired["capo_devops_guru.types.anomaly_id.AnomalyId"]
    """<p>The ID of the reactive anomaly. </p>"""
    severity: NotRequired["capo_devops_guru.types.anomaly_severity.AnomalySeverity"]
    """<p>The severity of the anomaly. The severity of anomalies that generate an insight determine that insight's severity. For more information, see <a href="https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities">Understanding insight severities</a> in the <i>Amazon DevOps Guru User Guide</i>.</p>"""
    status: NotRequired["capo_devops_guru.types.anomaly_status.AnomalyStatus"]
    """<p> The status of the anomaly. </p>"""
    anomaly_time_range: NotRequired[
        "capo_devops_guru.types.anomaly_time_range.AnomalyTimeRange"
    ]
    anomaly_reported_time_range: NotRequired[
        "capo_devops_guru.types.anomaly_reported_time_range.AnomalyReportedTimeRange"
    ]
    """<p> An <code>AnomalyReportedTimeRange</code> object that specifies the time range between when the anomaly is opened and the time when it is closed. </p>"""
    source_details: NotRequired[
        "capo_devops_guru.types.anomaly_source_details.AnomalySourceDetails"
    ]
    """<p> Details about the source of the analyzed operational data that triggered the anomaly. The one supported source is Amazon CloudWatch metrics. </p>"""
    associated_insight_id: NotRequired["capo_devops_guru.types.insight_id.InsightId"]
    """<p> The ID of the insight that contains this anomaly. An insight is composed of related anomalies. </p>"""
    resource_collection: NotRequired[
        "capo_devops_guru.types.resource_collection.ResourceCollection"
    ]
    type: NotRequired["capo_devops_guru.types.anomaly_type.AnomalyType"]
    """<p>The type of the reactive anomaly. It can be one of the following types.</p> <ul> <li> <p> <code>CAUSAL</code> - the anomaly can cause a new insight.</p> </li> <li> <p> <code>CONTEXTUAL</code> - the anomaly contains additional information about an insight or its causal anomaly.</p> </li> </ul>"""
    name: NotRequired["capo_devops_guru.types.anomaly_name.AnomalyName"]
    """<p>The name of the reactive anomaly.</p>"""
    description: NotRequired[
        "capo_devops_guru.types.anomaly_description.AnomalyDescription"
    ]
    """<p>A description of the reactive anomaly.</p>"""
    causal_anomaly_id: NotRequired["capo_devops_guru.types.anomaly_id.AnomalyId"]
    """<p>The ID of the causal anomaly that is associated with this reactive anomaly. The ID of a `CAUSAL` anomaly is always `NULL`.</p>"""
    anomaly_resources: NotRequired[
        "capo_devops_guru.types.anomaly_resources.AnomalyResources"
    ]
    """<p>The Amazon Web Services resources in which anomalous behavior was detected by DevOps Guru.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReactiveAnomaly) -> dict:
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
    if "type" in value:
        import capo_devops_guru.types.anomaly_type

        out["Type"] = capo_devops_guru.types.anomaly_type.serialize_json(value["type"])
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "causal_anomaly_id" in value:
        out["CausalAnomalyId"] = value["causal_anomaly_id"]
    if "anomaly_resources" in value:
        import capo_devops_guru.types.anomaly_resources

        out["AnomalyResources"] = (
            capo_devops_guru.types.anomaly_resources.serialize_json(
                value["anomaly_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReactiveAnomaly:
    out: ReactiveAnomaly = {}  # type: ignore[typeddict-item]
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
    if data.get("Type") is not None:
        import capo_devops_guru.types.anomaly_type

        out["type"] = capo_devops_guru.types.anomaly_type.deserialize_json(data["Type"])
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CausalAnomalyId") is not None:
        out["causal_anomaly_id"] = data["CausalAnomalyId"]
    if data.get("AnomalyResources") is not None:
        import capo_devops_guru.types.anomaly_resources

        out["anomaly_resources"] = (
            capo_devops_guru.types.anomaly_resources.deserialize_json(
                data["AnomalyResources"]
            )
        )
    return out
