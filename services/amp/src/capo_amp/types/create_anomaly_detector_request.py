"""Generated from Smithy shape ``com.amazonaws.amp#CreateAnomalyDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.anomaly_detector_alias
    import capo_amp.types.anomaly_detector_configuration
    import capo_amp.types.anomaly_detector_evaluation_interval
    import capo_amp.types.anomaly_detector_missing_data_action
    import capo_amp.types.idempotency_token
    import capo_amp.types.prometheus_metric_label_map
    import capo_amp.types.tag_map
    import capo_amp.types.workspace_id


class CreateAnomalyDetectorRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace where the anomaly detector will be created.</p>"""
    alias: "capo_amp.types.anomaly_detector_alias.AnomalyDetectorAlias"
    """<p>A user-friendly name for the anomaly detector.</p>"""
    evaluation_interval_in_seconds: NotRequired[
        "capo_amp.types.anomaly_detector_evaluation_interval.AnomalyDetectorEvaluationInterval"
    ]
    """<p>The frequency, in seconds, at which the anomaly detector evaluates metrics. The default value is 60 seconds.</p>"""
    missing_data_action: NotRequired[
        "capo_amp.types.anomaly_detector_missing_data_action.AnomalyDetectorMissingDataAction"
    ]
    """<p>Specifies the action to take when data is missing during evaluation.</p>"""
    configuration: (
        "capo_amp.types.anomaly_detector_configuration.AnomalyDetectorConfiguration"
    )
    """<p>The algorithm configuration for the anomaly detector.</p>"""
    labels: NotRequired[
        "capo_amp.types.prometheus_metric_label_map.PrometheusMetricLabelMap"
    ]
    """<p>The Amazon Managed Service for Prometheus metric labels to associate with the anomaly detector.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>The metadata to apply to the anomaly detector to assist with categorization and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnomalyDetectorRequest) -> dict:
    out: dict = {}
    out["alias"] = value["alias"]
    if "evaluation_interval_in_seconds" in value:
        out["evaluationIntervalInSeconds"] = value["evaluation_interval_in_seconds"]
    if "missing_data_action" in value:
        import capo_amp.types.anomaly_detector_missing_data_action

        out["missingDataAction"] = (
            capo_amp.types.anomaly_detector_missing_data_action.serialize_json(
                value["missing_data_action"]
            )
        )
    import capo_amp.types.anomaly_detector_configuration

    out["configuration"] = capo_amp.types.anomaly_detector_configuration.serialize_json(
        value["configuration"]
    )
    if "labels" in value:
        import capo_amp.types.prometheus_metric_label_map

        out["labels"] = capo_amp.types.prometheus_metric_label_map.serialize_json(
            value["labels"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAnomalyDetectorRequest:
    out: CreateAnomalyDetectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    else:
        raise DeserializationError("CreateAnomalyDetectorRequest.alias required")
    if data.get("evaluationIntervalInSeconds") is not None:
        out["evaluation_interval_in_seconds"] = data["evaluationIntervalInSeconds"]
    if data.get("missingDataAction") is not None:
        import capo_amp.types.anomaly_detector_missing_data_action

        out["missing_data_action"] = (
            capo_amp.types.anomaly_detector_missing_data_action.deserialize_json(
                data["missingDataAction"]
            )
        )
    if data.get("configuration") is not None:
        import capo_amp.types.anomaly_detector_configuration

        out["configuration"] = (
            capo_amp.types.anomaly_detector_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAnomalyDetectorRequest.configuration required"
        )
    if data.get("labels") is not None:
        import capo_amp.types.prometheus_metric_label_map

        out["labels"] = capo_amp.types.prometheus_metric_label_map.deserialize_json(
            data["labels"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    return out
