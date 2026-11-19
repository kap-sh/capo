"""Generated from Smithy shape ``com.amazonaws.codedeploy#RelatedDeployments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.deployments_list


class RelatedDeployments(TypedDict, closed=True):
    auto_update_outdated_instances_root_deployment_id: NotRequired[
        "capo_codedeploy.types.deployment_id.DeploymentId"
    ]
    """<p>The deployment ID of the root deployment that triggered this deployment.</p>"""
    auto_update_outdated_instances_deployment_ids: NotRequired[
        "capo_codedeploy.types.deployments_list.DeploymentsList"
    ]
    """<p>The deployment IDs of 'auto-update outdated instances' deployments triggered by this deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelatedDeployments) -> dict:
    out: dict = {}
    if "auto_update_outdated_instances_root_deployment_id" in value:
        out["autoUpdateOutdatedInstancesRootDeploymentId"] = value[
            "auto_update_outdated_instances_root_deployment_id"
        ]
    if "auto_update_outdated_instances_deployment_ids" in value:
        import capo_codedeploy.types.deployments_list

        out["autoUpdateOutdatedInstancesDeploymentIds"] = (
            capo_codedeploy.types.deployments_list.serialize_aws_json_1_1(
                value["auto_update_outdated_instances_deployment_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RelatedDeployments:
    out: RelatedDeployments = {}  # type: ignore[typeddict-item]
    if data.get("autoUpdateOutdatedInstancesRootDeploymentId") is not None:
        out["auto_update_outdated_instances_root_deployment_id"] = data[
            "autoUpdateOutdatedInstancesRootDeploymentId"
        ]
    if data.get("autoUpdateOutdatedInstancesDeploymentIds") is not None:
        import capo_codedeploy.types.deployments_list

        out["auto_update_outdated_instances_deployment_ids"] = (
            capo_codedeploy.types.deployments_list.deserialize_aws_json_1_1(
                data["autoUpdateOutdatedInstancesDeploymentIds"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RelatedDeployments) -> dict:
    out: dict = {}
    if "auto_update_outdated_instances_root_deployment_id" in value:
        out["autoUpdateOutdatedInstancesRootDeploymentId"] = value[
            "auto_update_outdated_instances_root_deployment_id"
        ]
    if "auto_update_outdated_instances_deployment_ids" in value:
        import capo_codedeploy.types.deployments_list

        out["autoUpdateOutdatedInstancesDeploymentIds"] = (
            capo_codedeploy.types.deployments_list.serialize_cbor(
                value["auto_update_outdated_instances_deployment_ids"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RelatedDeployments:
    out: RelatedDeployments = {}  # type: ignore[typeddict-item]
    if data.get("autoUpdateOutdatedInstancesRootDeploymentId") is not None:
        out["auto_update_outdated_instances_root_deployment_id"] = data[
            "autoUpdateOutdatedInstancesRootDeploymentId"
        ]
    if data.get("autoUpdateOutdatedInstancesDeploymentIds") is not None:
        import capo_codedeploy.types.deployments_list

        out["auto_update_outdated_instances_deployment_ids"] = (
            capo_codedeploy.types.deployments_list.deserialize_cbor(
                data["autoUpdateOutdatedInstancesDeploymentIds"]
            )
        )
    return out
