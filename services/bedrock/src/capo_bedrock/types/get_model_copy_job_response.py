"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelCopyJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.account_id
    import capo_bedrock.types.custom_model_arn
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.error_message
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.model_copy_job_arn
    import capo_bedrock.types.model_copy_job_status
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.timestamp


class GetModelCopyJobResponse(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.model_copy_job_arn.ModelCopyJobArn"
    """<p>The Amazon Resource Name (ARN) of the model copy job.</p>"""
    status: "capo_bedrock.types.model_copy_job_status.ModelCopyJobStatus"
    """<p>The status of the model copy job.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The time at which the model copy job was created.</p>"""
    target_model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn"
    """<p>The Amazon Resource Name (ARN) of the copied model.</p>"""
    target_model_name: NotRequired[
        "capo_bedrock.types.custom_model_name.CustomModelName"
    ]
    """<p>The name of the copied model.</p>"""
    source_account_id: "capo_bedrock.types.account_id.AccountId"
    """<p>The unique identifier of the account that the model being copied originated from.</p>"""
    source_model_arn: "capo_bedrock.types.model_arn.ModelArn"
    """<p>The Amazon Resource Name (ARN) of the original model being copied.</p>"""
    target_model_kms_key_arn: NotRequired["capo_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key encrypting the copied model.</p>"""
    target_model_tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>The tags associated with the copied model.</p>"""
    failure_message: NotRequired["capo_bedrock.types.error_message.ErrorMessage"]
    """<p>An error message for why the model copy job failed.</p>"""
    source_model_name: NotRequired[
        "capo_bedrock.types.custom_model_name.CustomModelName"
    ]
    """<p>The name of the original model being copied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelCopyJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    import capo_bedrock.types.model_copy_job_status

    out["status"] = capo_bedrock.types.model_copy_job_status.serialize_json(
        value["status"]
    )
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    out["targetModelArn"] = value["target_model_arn"]
    if "target_model_name" in value:
        out["targetModelName"] = value["target_model_name"]
    out["sourceAccountId"] = value["source_account_id"]
    out["sourceModelArn"] = value["source_model_arn"]
    if "target_model_kms_key_arn" in value:
        out["targetModelKmsKeyArn"] = value["target_model_kms_key_arn"]
    if "target_model_tags" in value:
        import capo_bedrock.types.tag_list

        out["targetModelTags"] = capo_bedrock.types.tag_list.serialize_json(
            value["target_model_tags"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "source_model_name" in value:
        out["sourceModelName"] = value["source_model_name"]
    return out


def deserialize_json(data: dict) -> GetModelCopyJobResponse:
    out: GetModelCopyJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("status") is not None:
        import capo_bedrock.types.model_copy_job_status

        out["status"] = capo_bedrock.types.model_copy_job_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.model_copy_job_status.ModelCopyJobStatus", ""
        )
    if data.get("creationTime") is not None:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("targetModelArn") is not None:
        out["target_model_arn"] = data["targetModelArn"]
    else:
        out["target_model_arn"] = ""
    if data.get("targetModelName") is not None:
        out["target_model_name"] = data["targetModelName"]
    if data.get("sourceAccountId") is not None:
        out["source_account_id"] = data["sourceAccountId"]
    else:
        out["source_account_id"] = ""
    if data.get("sourceModelArn") is not None:
        out["source_model_arn"] = data["sourceModelArn"]
    else:
        out["source_model_arn"] = ""
    if data.get("targetModelKmsKeyArn") is not None:
        out["target_model_kms_key_arn"] = data["targetModelKmsKeyArn"]
    if data.get("targetModelTags") is not None:
        import capo_bedrock.types.tag_list

        out["target_model_tags"] = capo_bedrock.types.tag_list.deserialize_json(
            data["targetModelTags"]
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("sourceModelName") is not None:
        out["source_model_name"] = data["sourceModelName"]
    return out
