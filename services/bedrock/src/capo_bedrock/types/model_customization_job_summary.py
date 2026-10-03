"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCustomizationJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_arn
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.customization_type
    import capo_bedrock.types.job_name
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.model_customization_job_arn
    import capo_bedrock.types.model_customization_job_status
    import capo_bedrock.types.status_details
    import capo_bedrock.types.timestamp


class ModelCustomizationJobSummary(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.model_customization_job_arn.ModelCustomizationJobArn"
    """<p>Amazon Resource Name (ARN) of the customization job.</p>"""
    base_model_arn: "capo_bedrock.types.model_arn.ModelArn"
    """<p>Amazon Resource Name (ARN) of the base model.</p>"""
    job_name: "capo_bedrock.types.job_name.JobName"
    """<p>Name of the customization job.</p>"""
    status: (
        "capo_bedrock.types.model_customization_job_status.ModelCustomizationJobStatus"
    )
    """<p>Status of the customization job. </p>"""
    status_details: NotRequired["capo_bedrock.types.status_details.StatusDetails"]
    """<p>Details about the status of the data processing sub-task of the job.</p>"""
    last_modified_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Time that the customization job was last modified.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>Creation time of the custom model. </p>"""
    end_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Time that the customization job ended.</p>"""
    custom_model_arn: NotRequired["capo_bedrock.types.custom_model_arn.CustomModelArn"]
    """<p>Amazon Resource Name (ARN) of the custom model.</p>"""
    custom_model_name: NotRequired[
        "capo_bedrock.types.custom_model_name.CustomModelName"
    ]
    """<p>Name of the custom model.</p>"""
    customization_type: NotRequired[
        "capo_bedrock.types.customization_type.CustomizationType"
    ]
    """<p>Specifies whether to carry out continued pre-training of a model or whether to fine-tune it. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelCustomizationJobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["baseModelArn"] = value["base_model_arn"]
    out["jobName"] = value["job_name"]
    import capo_bedrock.types.model_customization_job_status

    out["status"] = capo_bedrock.types.model_customization_job_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        import capo_bedrock.types.status_details

        out["statusDetails"] = capo_bedrock.types.status_details.serialize_json(
            value["status_details"]
        )
    if "last_modified_time" in value:
        import capo_bedrock.types.timestamp

        out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "end_time" in value:
        import capo_bedrock.types.timestamp

        out["endTime"] = capo_bedrock.types.timestamp.serialize_json(value["end_time"])
    if "custom_model_arn" in value:
        out["customModelArn"] = value["custom_model_arn"]
    if "custom_model_name" in value:
        out["customModelName"] = value["custom_model_name"]
    if "customization_type" in value:
        import capo_bedrock.types.customization_type

        out["customizationType"] = capo_bedrock.types.customization_type.serialize_json(
            value["customization_type"]
        )
    return out


def deserialize_json(data: dict) -> ModelCustomizationJobSummary:
    out: ModelCustomizationJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("ModelCustomizationJobSummary.job_arn required")
    if data.get("baseModelArn") is not None:
        out["base_model_arn"] = data["baseModelArn"]
    else:
        raise DeserializationError(
            "ModelCustomizationJobSummary.base_model_arn required"
        )
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("ModelCustomizationJobSummary.job_name required")
    if data.get("status") is not None:
        import capo_bedrock.types.model_customization_job_status

        out["status"] = (
            capo_bedrock.types.model_customization_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ModelCustomizationJobSummary.status required")
    if data.get("statusDetails") is not None:
        import capo_bedrock.types.status_details

        out["status_details"] = capo_bedrock.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if data.get("creationTime") is not None:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "ModelCustomizationJobSummary.creation_time required"
        )
    if data.get("endTime") is not None:
        import capo_bedrock.types.timestamp

        out["end_time"] = capo_bedrock.types.timestamp.deserialize_json(data["endTime"])
    if data.get("customModelArn") is not None:
        out["custom_model_arn"] = data["customModelArn"]
    if data.get("customModelName") is not None:
        out["custom_model_name"] = data["customModelName"]
    if data.get("customizationType") is not None:
        import capo_bedrock.types.customization_type

        out["customization_type"] = (
            capo_bedrock.types.customization_type.deserialize_json(
                data["customizationType"]
            )
        )
    return out
