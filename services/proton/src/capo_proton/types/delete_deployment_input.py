"""Generated from Smithy shape ``com.amazonaws.proton#DeleteDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.deployment_id


class DeleteDeploymentInput(TypedDict, closed=True):
    id: "capo_proton.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDeploymentInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDeploymentInput:
    out: DeleteDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
