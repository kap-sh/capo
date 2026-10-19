"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateCustomModelDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_deployment_arn


class UpdateCustomModelDeploymentResponse(TypedDict, closed=True):
    custom_model_deployment_arn: (
        "capo_bedrock.types.custom_model_deployment_arn.CustomModelDeploymentArn"
    )
    """<p> ARN of the custom model deployment being updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomModelDeploymentResponse) -> dict:
    out: dict = {}
    out["customModelDeploymentArn"] = value["custom_model_deployment_arn"]
    return out


def deserialize_json(data: dict) -> UpdateCustomModelDeploymentResponse:
    out: UpdateCustomModelDeploymentResponse = {}  # type: ignore[typeddict-item]
    if data.get("customModelDeploymentArn") is not None:
        out["custom_model_deployment_arn"] = data["customModelDeploymentArn"]
    else:
        out["custom_model_deployment_arn"] = ""
    return out
