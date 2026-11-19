"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_count


class DeploymentOverview(TypedDict, closed=True):
    pending: "capo_codedeploy.types.instance_count.InstanceCount"
    """<p>The number of instances in the deployment in a pending state.</p>"""
    in_progress: "capo_codedeploy.types.instance_count.InstanceCount"
    """<p>The number of instances in which the deployment is in progress.</p>"""
    succeeded: "capo_codedeploy.types.instance_count.InstanceCount"
    """<p>The number of instances in the deployment to which revisions have been successfully deployed.</p>"""
    failed: "capo_codedeploy.types.instance_count.InstanceCount"
    """<p>The number of instances in the deployment in a failed state.</p>"""
    skipped: "capo_codedeploy.types.instance_count.InstanceCount"
    """<p>The number of instances in the deployment in a skipped state.</p>"""
    ready: "capo_codedeploy.types.instance_count.InstanceCount"
    """<p>The number of instances in a replacement environment ready to receive traffic in a blue/green deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentOverview) -> dict:
    out: dict = {}
    out["Pending"] = value.get("pending", 0)
    out["InProgress"] = value.get("in_progress", 0)
    out["Succeeded"] = value.get("succeeded", 0)
    out["Failed"] = value.get("failed", 0)
    out["Skipped"] = value.get("skipped", 0)
    out["Ready"] = value.get("ready", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentOverview:
    out: DeploymentOverview = {}  # type: ignore[typeddict-item]
    if data.get("Pending") is not None:
        out["pending"] = data["Pending"]
    else:
        out["pending"] = 0
    if data.get("InProgress") is not None:
        out["in_progress"] = data["InProgress"]
    else:
        out["in_progress"] = 0
    if data.get("Succeeded") is not None:
        out["succeeded"] = data["Succeeded"]
    else:
        out["succeeded"] = 0
    if data.get("Failed") is not None:
        out["failed"] = data["Failed"]
    else:
        out["failed"] = 0
    if data.get("Skipped") is not None:
        out["skipped"] = data["Skipped"]
    else:
        out["skipped"] = 0
    if data.get("Ready") is not None:
        out["ready"] = data["Ready"]
    else:
        out["ready"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentOverview) -> dict:
    out: dict = {}
    out["Pending"] = value.get("pending", 0)
    out["InProgress"] = value.get("in_progress", 0)
    out["Succeeded"] = value.get("succeeded", 0)
    out["Failed"] = value.get("failed", 0)
    out["Skipped"] = value.get("skipped", 0)
    out["Ready"] = value.get("ready", 0)
    return out


def deserialize_cbor(data: dict) -> DeploymentOverview:
    out: DeploymentOverview = {}  # type: ignore[typeddict-item]
    if data.get("Pending") is not None:
        out["pending"] = data["Pending"]
    else:
        out["pending"] = 0
    if data.get("InProgress") is not None:
        out["in_progress"] = data["InProgress"]
    else:
        out["in_progress"] = 0
    if data.get("Succeeded") is not None:
        out["succeeded"] = data["Succeeded"]
    else:
        out["succeeded"] = 0
    if data.get("Failed") is not None:
        out["failed"] = data["Failed"]
    else:
        out["failed"] = 0
    if data.get("Skipped") is not None:
        out["skipped"] = data["Skipped"]
    else:
        out["skipped"] = 0
    if data.get("Ready") is not None:
        out["ready"] = data["Ready"]
    else:
        out["ready"] = 0
    return out
