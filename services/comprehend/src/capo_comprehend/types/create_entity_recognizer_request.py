"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateEntityRecognizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.entity_recognizer_input_data_config
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.language_code
    import capo_comprehend.types.policy
    import capo_comprehend.types.tag_list
    import capo_comprehend.types.version_name
    import capo_comprehend.types.vpc_config


class CreateEntityRecognizerRequest(TypedDict, closed=True):
    recognizer_name: "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
    """<p>The name given to the newly created recognizer. Recognizer names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The name must be unique in the account/Region.</p>"""
    version_name: NotRequired["capo_comprehend.types.version_name.VersionName"]
    """<p>The version name given to the newly created recognizer. Version names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same recognizer name in the account/Region.</p>"""
    data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    tags: NotRequired["capo_comprehend.types.tag_list.TagList"]
    """<p>Tags to associate with the entity recognizer. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department. </p>"""
    input_data_config: "capo_comprehend.types.entity_recognizer_input_data_config.EntityRecognizerInputDataConfig"
    """<p>Specifies the format and location of the input data. The S3 bucket containing the input data must be located in the same Region as the entity recognizer being created. </p>"""
    client_request_token: NotRequired[
        "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p> A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p> You can specify any of the following languages: English ("en"), Spanish ("es"), French ("fr"), Italian ("it"), German ("de"), or Portuguese ("pt"). If you plan to use this entity recognizer with PDF, Word, or image input files, you must specify English as the language. All training documents must be in the same language.</p>"""
    volume_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["capo_comprehend.types.vpc_config.VpcConfig"]
    """<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your custom entity recognizer. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>"""
    model_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>"""
    model_policy: NotRequired["capo_comprehend.types.policy.Policy"]
    r"""<p>The JSON resource-based policy to attach to your custom entity recognizer model. You can use this policy to allow another Amazon Web Services account to import your custom model.</p> <p>Provide your JSON as a UTF-8 encoded string without line breaks. To provide valid JSON for your policy, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>"{\"attribute\": \"value\", \"attribute\": [\"value\"]}"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{"attribute": "value", "attribute": ["value"]}'</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEntityRecognizerRequest) -> dict:
    out: dict = {}
    out["RecognizerName"] = value["recognizer_name"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "tags" in value:
        import capo_comprehend.types.tag_list

        out["Tags"] = capo_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    import capo_comprehend.types.entity_recognizer_input_data_config

    out["InputDataConfig"] = (
        capo_comprehend.types.entity_recognizer_input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import capo_comprehend.types.vpc_config

        out["VpcConfig"] = capo_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "model_kms_key_id" in value:
        out["ModelKmsKeyId"] = value["model_kms_key_id"]
    if "model_policy" in value:
        out["ModelPolicy"] = value["model_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEntityRecognizerRequest:
    out: CreateEntityRecognizerRequest = {}  # type: ignore[typeddict-item]
    if data.get("RecognizerName") is not None:
        out["recognizer_name"] = data["RecognizerName"]
    else:
        raise DeserializationError(
            "CreateEntityRecognizerRequest.recognizer_name required"
        )
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "CreateEntityRecognizerRequest.data_access_role_arn required"
        )
    if data.get("Tags") is not None:
        import capo_comprehend.types.tag_list

        out["tags"] = capo_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("InputDataConfig") is not None:
        import capo_comprehend.types.entity_recognizer_input_data_config

        out["input_data_config"] = (
            capo_comprehend.types.entity_recognizer_input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEntityRecognizerRequest.input_data_config required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEntityRecognizerRequest.language_code required"
        )
    if data.get("VolumeKmsKeyId") is not None:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if data.get("VpcConfig") is not None:
        import capo_comprehend.types.vpc_config

        out["vpc_config"] = capo_comprehend.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("ModelKmsKeyId") is not None:
        out["model_kms_key_id"] = data["ModelKmsKeyId"]
    if data.get("ModelPolicy") is not None:
        out["model_policy"] = data["ModelPolicy"]
    return out
