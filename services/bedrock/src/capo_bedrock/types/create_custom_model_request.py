"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateCustomModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_data_source
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.model_data_source
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.tag_list


class CreateCustomModelRequest(TypedDict, closed=True):
    model_name: "capo_bedrock.types.custom_model_name.CustomModelName"
    """<p>A unique name for the custom model.</p>"""
    model_source_config: NotRequired[
        "capo_bedrock.types.model_data_source.ModelDataSource"
    ]
    """<p>The data source for the model. The Amazon S3 URI in the model source must be for the Amazon-managed Amazon S3 bucket containing your model artifacts.</p>"""
    custom_model_data_source: NotRequired[
        "capo_bedrock.types.custom_model_data_source.CustomModelDataSource"
    ]
    """<p>The data source for the custom model. Use this field to specify a SageMaker AI model package ARN as the source for your custom model. Amazon Bedrock resolves the model package to retrieve the model artifacts.</p> <p>You can specify either <code>customModelDataSource</code> or <code>modelSourceConfig</code>, but not both.</p>"""
    model_kms_key_arn: NotRequired["capo_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the customer managed KMS key to encrypt the custom model. If you don't provide a KMS key, Amazon Bedrock uses an Amazon Web Services-managed KMS key to encrypt the model. </p> <p>If you provide a customer managed KMS key, your Amazon Bedrock service role must have permissions to use it. For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-import-model.html">Encryption of imported models</a>. </p>"""
    role_arn: NotRequired["capo_bedrock.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock assumes to perform tasks on your behalf. This role must have permissions to access the Amazon S3 bucket containing your model artifacts and the KMS key (if specified). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-import-iam-role.html">Setting up an IAM service role for importing models</a> in the Amazon Bedrock User Guide.</p> <p>This field is required when you use <code>modelSourceConfig</code> with an Amazon S3 data source. It is not required when you use <code>customModelDataSource</code> with a model package ARN, because Amazon Bedrock uses its own credentials to access the model artifacts.</p>"""
    model_tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the custom model resource. You can use these tags to organize and identify your resources.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomModelRequest) -> dict:
    out: dict = {}
    out["modelName"] = value["model_name"]
    if "model_source_config" in value:
        import capo_bedrock.types.model_data_source

        out["modelSourceConfig"] = capo_bedrock.types.model_data_source.serialize_json(
            value["model_source_config"]
        )
    if "custom_model_data_source" in value:
        import capo_bedrock.types.custom_model_data_source

        out["customModelDataSource"] = (
            capo_bedrock.types.custom_model_data_source.serialize_json(
                value["custom_model_data_source"]
            )
        )
    if "model_kms_key_arn" in value:
        out["modelKmsKeyArn"] = value["model_kms_key_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "model_tags" in value:
        import capo_bedrock.types.tag_list

        out["modelTags"] = capo_bedrock.types.tag_list.serialize_json(
            value["model_tags"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateCustomModelRequest:
    out: CreateCustomModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("modelName") is not None:
        out["model_name"] = data["modelName"]
    else:
        raise DeserializationError("CreateCustomModelRequest.model_name required")
    if data.get("modelSourceConfig") is not None:
        import capo_bedrock.types.model_data_source

        out["model_source_config"] = (
            capo_bedrock.types.model_data_source.deserialize_json(
                data["modelSourceConfig"]
            )
        )
    if data.get("customModelDataSource") is not None:
        import capo_bedrock.types.custom_model_data_source

        out["custom_model_data_source"] = (
            capo_bedrock.types.custom_model_data_source.deserialize_json(
                data["customModelDataSource"]
            )
        )
    if data.get("modelKmsKeyArn") is not None:
        out["model_kms_key_arn"] = data["modelKmsKeyArn"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("modelTags") is not None:
        import capo_bedrock.types.tag_list

        out["model_tags"] = capo_bedrock.types.tag_list.deserialize_json(
            data["modelTags"]
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    return out
