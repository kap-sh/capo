"""Generated from Smithy shape ``com.amazonaws.codedeploy#StopDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.nullable_boolean


class StopDeploymentInput(TypedDict, closed=True):
    deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    auto_rollback_enabled: NotRequired[
        "capo_codedeploy.types.nullable_boolean.NullableBoolean"
    ]
    """<p> Indicates, when a deployment is stopped, whether instances that have been updated should be rolled back to the previous version of the application revision. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDeploymentInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    if "auto_rollback_enabled" in value:
        out["autoRollbackEnabled"] = value["auto_rollback_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDeploymentInput:
    out: StopDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        out["deployment_id"] = ""
    if data.get("autoRollbackEnabled") is not None:
        out["auto_rollback_enabled"] = data["autoRollbackEnabled"]
    return out
