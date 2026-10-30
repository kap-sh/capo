"""Generated from Smithy shape ``com.amazonaws.continuum#GetCollectorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.collector_arn
    import capo_continuum.types.collector_id
    import capo_continuum.types.collector_status
    import capo_continuum.types.collector_type
    import capo_continuum.types.config_recorder_arn
    import capo_continuum.types.kubernetes_cluster_role_arn


class GetCollectorOutput(TypedDict, closed=True):
    collector_id: "capo_continuum.types.collector_id.CollectorId"
    """The unique identifier of the Collector."""
    collector_arn: "capo_continuum.types.collector_arn.CollectorArn"
    """The ARN of the Collector."""
    type: "capo_continuum.types.collector_type.CollectorType"
    """The source collected by this Collector."""
    status: "capo_continuum.types.collector_status.CollectorStatus"
    """The current lifecycle status."""
    config_recorder_arn: NotRequired[
        "capo_continuum.types.config_recorder_arn.ConfigRecorderArn"
    ]
    """The ARN of the provisioned AWS Config Recorder."""
    kubernetes_cluster_role_arn: NotRequired[
        "capo_continuum.types.kubernetes_cluster_role_arn.KubernetesClusterRoleArn"
    ]
    """IAM role used to collect Kubernetes cluster metadata."""
    created_at: "datetime.datetime"
    """The timestamp when the Collector was created."""
    updated_at: "datetime.datetime"
    """The time of the last successful UpdateCollector call, returned at whole-second precision in the same date-time format as createdAt."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollectorOutput) -> dict:
    out: dict = {}
    out["collectorId"] = value["collector_id"]
    out["collectorArn"] = value["collector_arn"]
    import capo_continuum.types.collector_type

    out["type"] = capo_continuum.types.collector_type.serialize_json(value["type"])
    import capo_continuum.types.collector_status

    out["status"] = capo_continuum.types.collector_status.serialize_json(
        value["status"]
    )
    if "config_recorder_arn" in value:
        out["configRecorderArn"] = value["config_recorder_arn"]
    if "kubernetes_cluster_role_arn" in value:
        out["k8ClusterRole"] = value["kubernetes_cluster_role_arn"]
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_continuum._protocol.serialize

    out["updatedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetCollectorOutput:
    out: GetCollectorOutput = {}  # type: ignore[typeddict-item]
    if data.get("collectorId") is not None:
        out["collector_id"] = data["collectorId"]
    else:
        out["collector_id"] = ""
    if data.get("collectorArn") is not None:
        out["collector_arn"] = data["collectorArn"]
    else:
        out["collector_arn"] = ""
    if data.get("type") is not None:
        import capo_continuum.types.collector_type

        out["type"] = capo_continuum.types.collector_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast(
            "capo_continuum.types.collector_type.CollectorType", ""
        )
    if data.get("status") is not None:
        import capo_continuum.types.collector_status

        out["status"] = capo_continuum.types.collector_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_continuum.types.collector_status.CollectorStatus", ""
        )
    if data.get("configRecorderArn") is not None:
        out["config_recorder_arn"] = data["configRecorderArn"]
    if data.get("k8ClusterRole") is not None:
        out["kubernetes_cluster_role_arn"] = data["k8ClusterRole"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
