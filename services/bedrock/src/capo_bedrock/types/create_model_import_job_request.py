"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateModelImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.imported_model_name
    import capo_bedrock.types.job_name
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.model_data_source
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.vpc_config


class CreateModelImportJobRequest(TypedDict, closed=True):
    job_name: "capo_bedrock.types.job_name.JobName"
    """<p>The name of the import job.</p>"""
    imported_model_name: "capo_bedrock.types.imported_model_name.ImportedModelName"
    """<p>The name of the imported model.</p>"""
    role_arn: "capo_bedrock.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the model import job.</p>"""
    model_data_source: "capo_bedrock.types.model_data_source.ModelDataSource"
    """<p>The data source for the imported model.</p>"""
    job_tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>Tags to attach to this import job. </p>"""
    imported_model_tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>Tags to attach to the imported model.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    vpc_config: NotRequired["capo_bedrock.types.vpc_config.VpcConfig"]
    """<p>VPC configuration parameters for the private Virtual Private Cloud (VPC) that contains the resources you are using for the import job.</p>"""
    imported_model_kms_key_id: NotRequired["capo_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>The imported model is encrypted at rest using this key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelImportJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["importedModelName"] = value["imported_model_name"]
    out["roleArn"] = value["role_arn"]
    import capo_bedrock.types.model_data_source

    out["modelDataSource"] = capo_bedrock.types.model_data_source.serialize_json(
        value["model_data_source"]
    )
    if "job_tags" in value:
        import capo_bedrock.types.tag_list

        out["jobTags"] = capo_bedrock.types.tag_list.serialize_json(value["job_tags"])
    if "imported_model_tags" in value:
        import capo_bedrock.types.tag_list

        out["importedModelTags"] = capo_bedrock.types.tag_list.serialize_json(
            value["imported_model_tags"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "vpc_config" in value:
        import capo_bedrock.types.vpc_config

        out["vpcConfig"] = capo_bedrock.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "imported_model_kms_key_id" in value:
        out["importedModelKmsKeyId"] = value["imported_model_kms_key_id"]
    return out


def deserialize_json(data: dict) -> CreateModelImportJobRequest:
    out: CreateModelImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateModelImportJobRequest.job_name required")
    if data.get("importedModelName") is not None:
        out["imported_model_name"] = data["importedModelName"]
    else:
        raise DeserializationError(
            "CreateModelImportJobRequest.imported_model_name required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateModelImportJobRequest.role_arn required")
    if data.get("modelDataSource") is not None:
        import capo_bedrock.types.model_data_source

        out["model_data_source"] = (
            capo_bedrock.types.model_data_source.deserialize_json(
                data["modelDataSource"]
            )
        )
    else:
        raise DeserializationError(
            "CreateModelImportJobRequest.model_data_source required"
        )
    if data.get("jobTags") is not None:
        import capo_bedrock.types.tag_list

        out["job_tags"] = capo_bedrock.types.tag_list.deserialize_json(data["jobTags"])
    if data.get("importedModelTags") is not None:
        import capo_bedrock.types.tag_list

        out["imported_model_tags"] = capo_bedrock.types.tag_list.deserialize_json(
            data["importedModelTags"]
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("vpcConfig") is not None:
        import capo_bedrock.types.vpc_config

        out["vpc_config"] = capo_bedrock.types.vpc_config.deserialize_json(
            data["vpcConfig"]
        )
    if data.get("importedModelKmsKeyId") is not None:
        out["imported_model_kms_key_id"] = data["importedModelKmsKeyId"]
    return out
