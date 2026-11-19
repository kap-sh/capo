"""Generated from Smithy shape ``com.amazonaws.codedeploy#ECSTaskSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.ecs_task_set_count
    import capo_codedeploy.types.ecs_task_set_identifier
    import capo_codedeploy.types.ecs_task_set_status
    import capo_codedeploy.types.target_group_info
    import capo_codedeploy.types.target_label
    import capo_codedeploy.types.traffic_weight


class ECSTaskSet(TypedDict, closed=True):
    identifer: NotRequired[
        "capo_codedeploy.types.ecs_task_set_identifier.ECSTaskSetIdentifier"
    ]
    """<p> A unique ID of an <code>ECSTaskSet</code>. </p>"""
    desired_count: "capo_codedeploy.types.ecs_task_set_count.ECSTaskSetCount"
    """<p> The number of tasks in a task set. During a deployment that uses the Amazon ECS compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses this value to determine how many tasks to create. After the updated task set is created, CodeDeploy shifts traffic to the new task set. </p>"""
    pending_count: "capo_codedeploy.types.ecs_task_set_count.ECSTaskSetCount"
    """<p> The number of tasks in the task set that are in the <code>PENDING</code> status during an Amazon ECS deployment. A task in the <code>PENDING</code> state is preparing to enter the <code>RUNNING</code> state. A task set enters the <code>PENDING</code> status when it launches for the first time, or when it is restarted after being in the <code>STOPPED</code> state. </p>"""
    running_count: "capo_codedeploy.types.ecs_task_set_count.ECSTaskSetCount"
    """<p> The number of tasks in the task set that are in the <code>RUNNING</code> status during an Amazon ECS deployment. A task in the <code>RUNNING</code> state is running and ready for use. </p>"""
    status: NotRequired["capo_codedeploy.types.ecs_task_set_status.ECSTaskSetStatus"]
    """<p> The status of the task set. There are three valid task set statuses: </p> <ul> <li> <p> <code>PRIMARY</code>: Indicates the task set is serving production traffic. </p> </li> <li> <p> <code>ACTIVE</code>: Indicates the task set is not serving production traffic. </p> </li> <li> <p> <code>DRAINING</code>: Indicates the tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group. </p> </li> </ul>"""
    traffic_weight: "capo_codedeploy.types.traffic_weight.TrafficWeight"
    """<p> The percentage of traffic served by this task set. </p>"""
    target_group: NotRequired["capo_codedeploy.types.target_group_info.TargetGroupInfo"]
    """<p> The target group associated with the task set. The target group is used by CodeDeploy to manage traffic to a task set. </p>"""
    task_set_label: NotRequired["capo_codedeploy.types.target_label.TargetLabel"]
    """<p> A label that identifies whether the ECS task set is an original target (<code>BLUE</code>) or a replacement target (<code>GREEN</code>). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSTaskSet) -> dict:
    out: dict = {}
    if "identifer" in value:
        out["identifer"] = value["identifer"]
    out["desiredCount"] = value.get("desired_count", 0)
    out["pendingCount"] = value.get("pending_count", 0)
    out["runningCount"] = value.get("running_count", 0)
    if "status" in value:
        out["status"] = value["status"]
    out["trafficWeight"] = (
        "NaN"
        if value.get("traffic_weight", 0) != value.get("traffic_weight", 0)
        else "Infinity"
        if value.get("traffic_weight", 0) == float("inf")
        else "-Infinity"
        if value.get("traffic_weight", 0) == float("-inf")
        else value.get("traffic_weight", 0)
    )
    if "target_group" in value:
        import capo_codedeploy.types.target_group_info

        out["targetGroup"] = (
            capo_codedeploy.types.target_group_info.serialize_aws_json_1_1(
                value["target_group"]
            )
        )
    if "task_set_label" in value:
        import capo_codedeploy.types.target_label

        out["taskSetLabel"] = capo_codedeploy.types.target_label.serialize_aws_json_1_1(
            value["task_set_label"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ECSTaskSet:
    out: ECSTaskSet = {}  # type: ignore[typeddict-item]
    if data.get("identifer") is not None:
        out["identifer"] = data["identifer"]
    if data.get("desiredCount") is not None:
        out["desired_count"] = data["desiredCount"]
    else:
        out["desired_count"] = 0
    if data.get("pendingCount") is not None:
        out["pending_count"] = data["pendingCount"]
    else:
        out["pending_count"] = 0
    if data.get("runningCount") is not None:
        out["running_count"] = data["runningCount"]
    else:
        out["running_count"] = 0
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("trafficWeight") is not None:
        out["traffic_weight"] = float(data["trafficWeight"])
    else:
        out["traffic_weight"] = 0
    if data.get("targetGroup") is not None:
        import capo_codedeploy.types.target_group_info

        out["target_group"] = (
            capo_codedeploy.types.target_group_info.deserialize_aws_json_1_1(
                data["targetGroup"]
            )
        )
    if data.get("taskSetLabel") is not None:
        import capo_codedeploy.types.target_label

        out["task_set_label"] = (
            capo_codedeploy.types.target_label.deserialize_aws_json_1_1(
                data["taskSetLabel"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSTaskSet) -> dict:
    out: dict = {}
    if "identifer" in value:
        out["identifer"] = value["identifer"]
    out["desiredCount"] = value.get("desired_count", 0)
    out["pendingCount"] = value.get("pending_count", 0)
    out["runningCount"] = value.get("running_count", 0)
    if "status" in value:
        out["status"] = value["status"]
    out["trafficWeight"] = value.get("traffic_weight", 0)
    if "target_group" in value:
        import capo_codedeploy.types.target_group_info

        out["targetGroup"] = capo_codedeploy.types.target_group_info.serialize_cbor(
            value["target_group"]
        )
    if "task_set_label" in value:
        import capo_codedeploy.types.target_label

        out["taskSetLabel"] = capo_codedeploy.types.target_label.serialize_cbor(
            value["task_set_label"]
        )
    return out


def deserialize_cbor(data: dict) -> ECSTaskSet:
    out: ECSTaskSet = {}  # type: ignore[typeddict-item]
    if data.get("identifer") is not None:
        out["identifer"] = data["identifer"]
    if data.get("desiredCount") is not None:
        out["desired_count"] = data["desiredCount"]
    else:
        out["desired_count"] = 0
    if data.get("pendingCount") is not None:
        out["pending_count"] = data["pendingCount"]
    else:
        out["pending_count"] = 0
    if data.get("runningCount") is not None:
        out["running_count"] = data["runningCount"]
    else:
        out["running_count"] = 0
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("trafficWeight") is not None:
        out["traffic_weight"] = float(data["trafficWeight"])
    else:
        out["traffic_weight"] = 0
    if data.get("targetGroup") is not None:
        import capo_codedeploy.types.target_group_info

        out["target_group"] = capo_codedeploy.types.target_group_info.deserialize_cbor(
            data["targetGroup"]
        )
    if data.get("taskSetLabel") is not None:
        import capo_codedeploy.types.target_label

        out["task_set_label"] = capo_codedeploy.types.target_label.deserialize_cbor(
            data["taskSetLabel"]
        )
    return out
