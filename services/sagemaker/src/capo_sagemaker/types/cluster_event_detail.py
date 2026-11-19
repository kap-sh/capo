"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterEventDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.cluster_event_level
    import capo_sagemaker.types.cluster_event_resource_type
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_name
    import capo_sagemaker.types.cluster_operation_id
    import capo_sagemaker.types.event_details
    import capo_sagemaker.types.event_id
    import capo_sagemaker.types.timestamp


class ClusterEventDetail(TypedDict, closed=True):
    event_id: NotRequired["capo_sagemaker.types.event_id.EventId"]
    """<p>The unique identifier (UUID) of the event.</p>"""
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the HyperPod cluster associated with the event.</p>"""
    cluster_name: NotRequired["capo_sagemaker.types.cluster_name.ClusterName"]
    """<p>The name of the HyperPod cluster associated with the event.</p>"""
    instance_group_name: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The name of the instance group associated with the event, if applicable.</p>"""
    instance_id: NotRequired["str"]
    """<p>The EC2 instance ID associated with the event, if applicable.</p>"""
    resource_type: NotRequired[
        "capo_sagemaker.types.cluster_event_resource_type.ClusterEventResourceType"
    ]
    """<p>The type of resource associated with the event. Valid values are <code>Cluster</code>, <code>InstanceGroup</code>, or <code>Instance</code>.</p>"""
    event_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the event occurred.</p>"""
    event_details: NotRequired["capo_sagemaker.types.event_details.EventDetails"]
    """<p>Additional details about the event, including event-specific metadata.</p>"""
    description: NotRequired["str"]
    """<p>A human-readable description of the event.</p>"""
    event_level: NotRequired[
        "capo_sagemaker.types.cluster_event_level.ClusterEventLevel"
    ]
    """<p>The severity level of the event. Valid values are <code>Info</code>, <code>Warn</code>, and <code>Error</code>.</p>"""
    operation_id: NotRequired[
        "capo_sagemaker.types.cluster_operation_id.ClusterOperationId"
    ]
    """<p>The unique identifier (UUID) of the cluster operation that the event is associated with, such as a scaling operation. This field is not returned when the event is not associated with an operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterEventDetail) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["EventId"] = value["event_id"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "resource_type" in value:
        import capo_sagemaker.types.cluster_event_resource_type

        out["ResourceType"] = (
            capo_sagemaker.types.cluster_event_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "event_time" in value:
        import capo_sagemaker.types.timestamp

        out["EventTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["event_time"]
        )
    if "event_details" in value:
        import capo_sagemaker.types.event_details

        out["EventDetails"] = capo_sagemaker.types.event_details.serialize_aws_json_1_1(
            value["event_details"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "event_level" in value:
        import capo_sagemaker.types.cluster_event_level

        out["EventLevel"] = (
            capo_sagemaker.types.cluster_event_level.serialize_aws_json_1_1(
                value["event_level"]
            )
        )
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterEventDetail:
    out: ClusterEventDetail = {}  # type: ignore[typeddict-item]
    if data.get("EventId") is not None:
        out["event_id"] = data["EventId"]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ResourceType") is not None:
        import capo_sagemaker.types.cluster_event_resource_type

        out["resource_type"] = (
            capo_sagemaker.types.cluster_event_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if data.get("EventTime") is not None:
        import capo_sagemaker.types.timestamp

        out["event_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EventTime"]
        )
    if data.get("EventDetails") is not None:
        import capo_sagemaker.types.event_details

        out["event_details"] = (
            capo_sagemaker.types.event_details.deserialize_aws_json_1_1(
                data["EventDetails"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EventLevel") is not None:
        import capo_sagemaker.types.cluster_event_level

        out["event_level"] = (
            capo_sagemaker.types.cluster_event_level.deserialize_aws_json_1_1(
                data["EventLevel"]
            )
        )
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    return out
