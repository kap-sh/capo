"""Generated from Smithy shape ``com.amazonaws.workspaces#DeployWorkspaceApplicationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.work_space_application_deployment


class DeployWorkspaceApplicationsResult(TypedDict, closed=True):
    deployment: NotRequired[
        "capo_workspaces.types.work_space_application_deployment.WorkSpaceApplicationDeployment"
    ]
    """<p>The list of deployed associations and information about them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployWorkspaceApplicationsResult) -> dict:
    out: dict = {}
    if "deployment" in value:
        import capo_workspaces.types.work_space_application_deployment

        out["Deployment"] = (
            capo_workspaces.types.work_space_application_deployment.serialize_aws_json_1_1(
                value["deployment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployWorkspaceApplicationsResult:
    out: DeployWorkspaceApplicationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Deployment") is not None:
        import capo_workspaces.types.work_space_application_deployment

        out["deployment"] = (
            capo_workspaces.types.work_space_application_deployment.deserialize_aws_json_1_1(
                data["Deployment"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeployWorkspaceApplicationsResult) -> dict:
    out: dict = {}
    if "deployment" in value:
        import capo_workspaces.types.work_space_application_deployment

        out["Deployment"] = (
            capo_workspaces.types.work_space_application_deployment.serialize_cbor(
                value["deployment"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeployWorkspaceApplicationsResult:
    out: DeployWorkspaceApplicationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Deployment") is not None:
        import capo_workspaces.types.work_space_application_deployment

        out["deployment"] = (
            capo_workspaces.types.work_space_application_deployment.deserialize_cbor(
                data["Deployment"]
            )
        )
    return out
