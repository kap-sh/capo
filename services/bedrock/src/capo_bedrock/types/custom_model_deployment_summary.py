"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDeploymentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_deployment_arn
    import capo_bedrock.types.custom_model_deployment_status
    import capo_bedrock.types.error_message
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.model_deployment_name
    import capo_bedrock.types.timestamp


class CustomModelDeploymentSummary(TypedDict, closed=True):
    custom_model_deployment_arn: (
        "capo_bedrock.types.custom_model_deployment_arn.CustomModelDeploymentArn"
    )
    """<p>The Amazon Resource Name (ARN) of the custom model deployment.</p>"""
    custom_model_deployment_name: (
        "capo_bedrock.types.model_deployment_name.ModelDeploymentName"
    )
    """<p>The name of the custom model deployment.</p>"""
    model_arn: "capo_bedrock.types.model_arn.ModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model associated with this deployment.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The date and time when the custom model deployment was created.</p>"""
    status: (
        "capo_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus"
    )
    """<p>The status of the custom model deployment. Possible values are <code>CREATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>"""
    last_updated_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The date and time when the custom model deployment was last modified.</p>"""
    failure_message: NotRequired["capo_bedrock.types.error_message.ErrorMessage"]
    """<p>If the deployment status is <code>FAILED</code>, this field contains a message describing the failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelDeploymentSummary) -> dict:
    out: dict = {}
    out["customModelDeploymentArn"] = value["custom_model_deployment_arn"]
    out["customModelDeploymentName"] = value["custom_model_deployment_name"]
    out["modelArn"] = value["model_arn"]
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    import capo_bedrock.types.custom_model_deployment_status

    out["status"] = capo_bedrock.types.custom_model_deployment_status.serialize_json(
        value["status"]
    )
    if "last_updated_at" in value:
        import capo_bedrock.types.timestamp

        out["lastUpdatedAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> CustomModelDeploymentSummary:
    out: CustomModelDeploymentSummary = {}  # type: ignore[typeddict-item]
    if data.get("customModelDeploymentArn") is not None:
        out["custom_model_deployment_arn"] = data["customModelDeploymentArn"]
    else:
        out["custom_model_deployment_arn"] = ""
    if data.get("customModelDeploymentName") is not None:
        out["custom_model_deployment_name"] = data["customModelDeploymentName"]
    else:
        out["custom_model_deployment_name"] = ""
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
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["last_updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    return out
