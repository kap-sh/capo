"""Generated from Smithy shape ``com.amazonaws.codedeploy#LastDeploymentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.deployment_status
    import capo_codedeploy.types.timestamp


class LastDeploymentInfo(TypedDict, closed=True):
    deployment_id: NotRequired["capo_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. </p>"""
    status: NotRequired["capo_codedeploy.types.deployment_status.DeploymentStatus"]
    """<p>The status of the most recent deployment.</p>"""
    end_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the most recent deployment to the deployment group was complete.</p>"""
    create_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the most recent deployment to the deployment group started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastDeploymentInfo) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "status" in value:
        import capo_codedeploy.types.deployment_status

        out["status"] = capo_codedeploy.types.deployment_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "end_time" in value:
        import capo_codedeploy.types.timestamp

        out["endTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "create_time" in value:
        import capo_codedeploy.types.timestamp

        out["createTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LastDeploymentInfo:
    out: LastDeploymentInfo = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("status") is not None:
        import capo_codedeploy.types.deployment_status

        out["status"] = (
            capo_codedeploy.types.deployment_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("endTime") is not None:
        import capo_codedeploy.types.timestamp

        out["end_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if data.get("createTime") is not None:
        import capo_codedeploy.types.timestamp

        out["create_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["createTime"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LastDeploymentInfo) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "status" in value:
        import capo_codedeploy.types.deployment_status

        out["status"] = capo_codedeploy.types.deployment_status.serialize_cbor(
            value["status"]
        )
    if "end_time" in value:
        import capo_codedeploy.types.timestamp

        out["endTime"] = capo_codedeploy.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "create_time" in value:
        import capo_codedeploy.types.timestamp

        out["createTime"] = capo_codedeploy.types.timestamp.serialize_cbor(
            value["create_time"]
        )
    return out


def deserialize_cbor(data: dict) -> LastDeploymentInfo:
    out: LastDeploymentInfo = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("status") is not None:
        import capo_codedeploy.types.deployment_status

        out["status"] = capo_codedeploy.types.deployment_status.deserialize_cbor(
            data["status"]
        )
    if data.get("endTime") is not None:
        import capo_codedeploy.types.timestamp

        out["end_time"] = capo_codedeploy.types.timestamp.deserialize_cbor(
            data["endTime"]
        )
    if data.get("createTime") is not None:
        import capo_codedeploy.types.timestamp

        out["create_time"] = capo_codedeploy.types.timestamp.deserialize_cbor(
            data["createTime"]
        )
    return out
