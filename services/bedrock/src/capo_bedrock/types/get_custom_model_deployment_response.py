"""Generated from Smithy shape ``com.amazonaws.bedrock#GetCustomModelDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_arn
    import capo_bedrock.types.custom_model_deployment_arn
    import capo_bedrock.types.custom_model_deployment_description
    import capo_bedrock.types.custom_model_deployment_status
    import capo_bedrock.types.custom_model_deployment_update_details
    import capo_bedrock.types.error_message
    import capo_bedrock.types.model_deployment_name
    import capo_bedrock.types.timestamp


class GetCustomModelDeploymentResponse(TypedDict, closed=True):
    custom_model_deployment_arn: (
        "capo_bedrock.types.custom_model_deployment_arn.CustomModelDeploymentArn"
    )
    """<p>The Amazon Resource Name (ARN) of the custom model deployment.</p>"""
    model_deployment_name: (
        "capo_bedrock.types.model_deployment_name.ModelDeploymentName"
    )
    """<p>The name of the custom model deployment.</p>"""
    model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model associated with this deployment.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The date and time when the custom model deployment was created.</p>"""
    status: (
        "capo_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus"
    )
    """<p>The status of the custom model deployment. Possible values are:</p> <ul> <li> <p> <code>CREATING</code> - The deployment is being set up and prepared for inference.</p> </li> <li> <p> <code>ACTIVE</code> - The deployment is ready and available for inference requests.</p> </li> <li> <p> <code>FAILED</code> - The deployment failed to be created or became unavailable.</p> </li> </ul>"""
    description: NotRequired[
        "capo_bedrock.types.custom_model_deployment_description.CustomModelDeploymentDescription"
    ]
    """<p>The description of the custom model deployment.</p>"""
    update_details: NotRequired[
        "capo_bedrock.types.custom_model_deployment_update_details.CustomModelDeploymentUpdateDetails"
    ]
    """<p> Details about any pending or completed updates to the custom model deployment, including the new model ARN and update status. </p>"""
    failure_message: NotRequired["capo_bedrock.types.error_message.ErrorMessage"]
    """<p>If the deployment status is <code>FAILED</code>, this field contains a message describing the failure reason.</p>"""
    last_updated_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The date and time when the custom model deployment was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomModelDeploymentResponse) -> dict:
    out: dict = {}
    out["customModelDeploymentArn"] = value["custom_model_deployment_arn"]
    out["modelDeploymentName"] = value["model_deployment_name"]
    out["modelArn"] = value["model_arn"]
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    import capo_bedrock.types.custom_model_deployment_status

    out["status"] = capo_bedrock.types.custom_model_deployment_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "update_details" in value:
        import capo_bedrock.types.custom_model_deployment_update_details

        out["updateDetails"] = (
            capo_bedrock.types.custom_model_deployment_update_details.serialize_json(
                value["update_details"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "last_updated_at" in value:
        import capo_bedrock.types.timestamp

        out["lastUpdatedAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetCustomModelDeploymentResponse:
    out: GetCustomModelDeploymentResponse = {}  # type: ignore[typeddict-item]
    if data.get("customModelDeploymentArn") is not None:
        out["custom_model_deployment_arn"] = data["customModelDeploymentArn"]
    else:
        out["custom_model_deployment_arn"] = ""
    if data.get("modelDeploymentName") is not None:
        out["model_deployment_name"] = data["modelDeploymentName"]
    else:
        out["model_deployment_name"] = ""
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        import capo_bedrock.types.custom_model_deployment_status

        out["status"] = (
            capo_bedrock.types.custom_model_deployment_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus",
            "",
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("updateDetails") is not None:
        import capo_bedrock.types.custom_model_deployment_update_details

        out["update_details"] = (
            capo_bedrock.types.custom_model_deployment_update_details.deserialize_json(
                data["updateDetails"]
            )
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["last_updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
