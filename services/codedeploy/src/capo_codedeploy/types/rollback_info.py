"""Generated from Smithy shape ``com.amazonaws.codedeploy#RollbackInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.description


class RollbackInfo(TypedDict, closed=True):
    rollback_deployment_id: NotRequired[
        "capo_codedeploy.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the deployment rollback.</p>"""
    rollback_triggering_deployment_id: NotRequired[
        "capo_codedeploy.types.deployment_id.DeploymentId"
    ]
    """<p>The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.</p>"""
    rollback_message: NotRequired["capo_codedeploy.types.description.Description"]
    """<p>Information that describes the status of a deployment rollback (for example, whether the deployment can't be rolled back, is in progress, failed, or succeeded). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RollbackInfo) -> dict:
    out: dict = {}
    if "rollback_deployment_id" in value:
        out["rollbackDeploymentId"] = value["rollback_deployment_id"]
    if "rollback_triggering_deployment_id" in value:
        out["rollbackTriggeringDeploymentId"] = value[
            "rollback_triggering_deployment_id"
        ]
    if "rollback_message" in value:
        out["rollbackMessage"] = value["rollback_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RollbackInfo:
    out: RollbackInfo = {}  # type: ignore[typeddict-item]
    if data.get("rollbackDeploymentId") is not None:
        out["rollback_deployment_id"] = data["rollbackDeploymentId"]
    if data.get("rollbackTriggeringDeploymentId") is not None:
        out["rollback_triggering_deployment_id"] = data[
            "rollbackTriggeringDeploymentId"
        ]
    if data.get("rollbackMessage") is not None:
        out["rollback_message"] = data["rollbackMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RollbackInfo) -> dict:
    out: dict = {}
    if "rollback_deployment_id" in value:
        out["rollbackDeploymentId"] = value["rollback_deployment_id"]
    if "rollback_triggering_deployment_id" in value:
        out["rollbackTriggeringDeploymentId"] = value[
            "rollback_triggering_deployment_id"
        ]
    if "rollback_message" in value:
        out["rollbackMessage"] = value["rollback_message"]
    return out


def deserialize_cbor(data: dict) -> RollbackInfo:
    out: RollbackInfo = {}  # type: ignore[typeddict-item]
    if data.get("rollbackDeploymentId") is not None:
        out["rollback_deployment_id"] = data["rollbackDeploymentId"]
    if data.get("rollbackTriggeringDeploymentId") is not None:
        out["rollback_triggering_deployment_id"] = data[
            "rollbackTriggeringDeploymentId"
        ]
    if data.get("rollbackMessage") is not None:
        out["rollback_message"] = data["rollbackMessage"]
    return out
