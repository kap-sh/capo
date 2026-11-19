"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.instance_id
    import capo_codedeploy.types.instance_status
    import capo_codedeploy.types.instance_type
    import capo_codedeploy.types.lifecycle_event_list
    import capo_codedeploy.types.timestamp


class InstanceSummary(TypedDict, closed=True):
    deployment_id: NotRequired["capo_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. </p>"""
    instance_id: NotRequired["capo_codedeploy.types.instance_id.InstanceId"]
    """<p>The instance ID.</p>"""
    status: NotRequired["capo_codedeploy.types.instance_status.InstanceStatus"]
    """<p>The deployment status for this instance:</p> <ul> <li> <p> <code>Pending</code>: The deployment is pending for this instance.</p> </li> <li> <p> <code>In Progress</code>: The deployment is in progress for this instance.</p> </li> <li> <p> <code>Succeeded</code>: The deployment has succeeded for this instance.</p> </li> <li> <p> <code>Failed</code>: The deployment has failed for this instance.</p> </li> <li> <p> <code>Skipped</code>: The deployment has been skipped for this instance.</p> </li> <li> <p> <code>Unknown</code>: The deployment status is unknown for this instance.</p> </li> </ul>"""
    last_updated_at: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the instance information was last updated.</p>"""
    lifecycle_events: NotRequired[
        "capo_codedeploy.types.lifecycle_event_list.LifecycleEventList"
    ]
    """<p>A list of lifecycle events for this instance.</p>"""
    instance_type: NotRequired["capo_codedeploy.types.instance_type.InstanceType"]
    """<p>Information about which environment an instance belongs to in a blue/green deployment.</p> <ul> <li> <p>BLUE: The instance is part of the original environment.</p> </li> <li> <p>GREEN: The instance is part of the replacement environment.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceSummary) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "status" in value:
        import capo_codedeploy.types.instance_status

        out["status"] = capo_codedeploy.types.instance_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "last_updated_at" in value:
        import capo_codedeploy.types.timestamp

        out["lastUpdatedAt"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_at"]
        )
    if "lifecycle_events" in value:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycleEvents"] = (
            capo_codedeploy.types.lifecycle_event_list.serialize_aws_json_1_1(
                value["lifecycle_events"]
            )
        )
    if "instance_type" in value:
        import capo_codedeploy.types.instance_type

        out["instanceType"] = (
            capo_codedeploy.types.instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceSummary:
    out: InstanceSummary = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    if data.get("status") is not None:
        import capo_codedeploy.types.instance_status

        out["status"] = capo_codedeploy.types.instance_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_codedeploy.types.timestamp

        out["last_updated_at"] = (
            capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["lastUpdatedAt"]
            )
        )
    if data.get("lifecycleEvents") is not None:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycle_events"] = (
            capo_codedeploy.types.lifecycle_event_list.deserialize_aws_json_1_1(
                data["lifecycleEvents"]
            )
        )
    if data.get("instanceType") is not None:
        import capo_codedeploy.types.instance_type

        out["instance_type"] = (
            capo_codedeploy.types.instance_type.deserialize_aws_json_1_1(
                data["instanceType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceSummary) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "status" in value:
        import capo_codedeploy.types.instance_status

        out["status"] = capo_codedeploy.types.instance_status.serialize_cbor(
            value["status"]
        )
    if "last_updated_at" in value:
        import capo_codedeploy.types.timestamp

        out["lastUpdatedAt"] = capo_codedeploy.types.timestamp.serialize_cbor(
            value["last_updated_at"]
        )
    if "lifecycle_events" in value:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycleEvents"] = (
            capo_codedeploy.types.lifecycle_event_list.serialize_cbor(
                value["lifecycle_events"]
            )
        )
    if "instance_type" in value:
        import capo_codedeploy.types.instance_type

        out["instanceType"] = capo_codedeploy.types.instance_type.serialize_cbor(
            value["instance_type"]
        )
    return out


def deserialize_cbor(data: dict) -> InstanceSummary:
    out: InstanceSummary = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    if data.get("status") is not None:
        import capo_codedeploy.types.instance_status

        out["status"] = capo_codedeploy.types.instance_status.deserialize_cbor(
            data["status"]
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_codedeploy.types.timestamp

        out["last_updated_at"] = capo_codedeploy.types.timestamp.deserialize_cbor(
            data["lastUpdatedAt"]
        )
    if data.get("lifecycleEvents") is not None:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycle_events"] = (
            capo_codedeploy.types.lifecycle_event_list.deserialize_cbor(
                data["lifecycleEvents"]
            )
        )
    if data.get("instanceType") is not None:
        import capo_codedeploy.types.instance_type

        out["instance_type"] = capo_codedeploy.types.instance_type.deserialize_cbor(
            data["instanceType"]
        )
    return out
