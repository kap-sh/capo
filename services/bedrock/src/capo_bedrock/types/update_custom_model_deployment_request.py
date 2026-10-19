"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateCustomModelDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_arn
    import capo_bedrock.types.custom_model_deployment_identifier


class UpdateCustomModelDeploymentRequest(TypedDict, closed=True):
    model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn"
    """<p> ARN of the new custom model to deploy. This replaces the currently deployed model. </p>"""
    custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier"
    """<p> Identifier of the custom model deployment to update with the new custom model. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomModelDeploymentRequest) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(data: dict) -> UpdateCustomModelDeploymentRequest:
    out: UpdateCustomModelDeploymentRequest = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    return out
