"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateCustomModelDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_deployment_arn


class CreateCustomModelDeploymentResponse(TypedDict, closed=True):
    custom_model_deployment_arn: (
        "capo_bedrock.types.custom_model_deployment_arn.CustomModelDeploymentArn"
    )
    """<p>The Amazon Resource Name (ARN) of the custom model deployment. Use this ARN as the <code>modelId</code> parameter when invoking the model with the <code>InvokeModel</code> or <code>Converse</code> operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomModelDeploymentResponse) -> dict:
    out: dict = {}
    out["customModelDeploymentArn"] = value["custom_model_deployment_arn"]
    return out


def deserialize_json(data: dict) -> CreateCustomModelDeploymentResponse:
    out: CreateCustomModelDeploymentResponse = {}  # type: ignore[typeddict-item]
    if data.get("customModelDeploymentArn") is not None:
        out["custom_model_deployment_arn"] = data["customModelDeploymentArn"]
    else:
        out["custom_model_deployment_arn"] = ""
    return out
